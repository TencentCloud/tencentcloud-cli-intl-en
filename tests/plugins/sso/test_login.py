# -*- coding: utf-8 -*-
import json
import os
import shutil
import sys
import tempfile
import time
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

_BUILTINS_MODULE = "__builtin__" if sys.version_info[0] == 2 else "builtins"

from tccli.plugins.sso import login as login_module


def _make_cred_resp():
    """Build a mock response from assume_role_with_saml."""
    return {
        "Credentials": {
            "TmpSecretId": "sid",
            "TmpSecretKey": "skey",
            "Token": "tok",
        },
        "ExpiredTime": int(time.time()) + 7200,
    }


_ACCOUNTS = [
    {"Uin": 123, "Name": "a"},
    {"Uin": 456, "Name": "b"},
]
_ROLES = [
    {"RoleConfigurationName": "role-a", "RoleConfigurationId": "rid-a"},
    {"RoleConfigurationName": "role-b", "RoleConfigurationId": "rid-b"},
]


# ---------------------------------------------------------------------------
# TestLoginDuration
# ---------------------------------------------------------------------------

class TestLoginDuration(unittest.TestCase):
    """Validate parsing, validation, and forwarding of one-time login duration."""

    def _run_login(self, args, legacy_duration=None):
        cred_data = {"sso": {"authUrl": "https://example.com"}}
        if legacy_duration is not None:
            cred_data["sso"]["defaultDuration"] = legacy_duration

        login_args = {"uin": "123", "rolename": "rname"}
        login_args.update(args)
        patchers = [
            ("open", mock.patch(_BUILTINS_MODULE + ".open", mock.mock_open(read_data=json.dumps(cred_data)))),
            ("exists", mock.patch.object(login_module.os.path, "exists", return_value=True)),
            ("cred_path", mock.patch.object(
                login_module.sso, "cred_path_of_profile", return_value="/tmp/default.credential")),
            ("get_token", mock.patch.object(
                login_module, "_get_token",
                side_effect=lambda auth_url, state, language: {
                    "State": state, "Token": "login-token", "Site": "ap"
                })),
            ("accounts", mock.patch.object(
                login_module.sso, "list_accounts_for_access_assignment",
                return_value=[{"Uin": 123, "Name": "account"}])),
            ("roles", mock.patch.object(
                login_module.sso, "list_role_configurations_for_account",
                return_value=[{"RoleConfigurationName": "rname", "RoleConfigurationId": "rid"}])),
            ("gen_saml", mock.patch.object(
                login_module.sso, "gen_saml_response", return_value={"SAMLResponse": "saml"})),
            ("verify", mock.patch.object(
                login_module.sso, "verify_login_skey", return_value={"ZoneId": "zone"})),
            ("assume", mock.patch.object(
                login_module.sso, "assume_role_with_saml", return_value=_make_cred_resp())),
            ("save", mock.patch.object(login_module.sso, "save_credential")),
            ("print", mock.patch.object(login_module, "print_message")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            login_module.login(login_args, "default", "zh-CN")
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    def test_cli_duration_is_used_only_for_current_login(self):
        """Forward CLI duration to STS without storing it in the credential."""
        mocks = self._run_login({"duration": 34200})
        self.assertEqual(mocks["assume"].call_args[0][4], 34200)
        saved_sso_info = mocks["save"].call_args[0][1]
        self.assertNotIn("defaultDuration", saved_sso_info)

    def test_default_duration_ignores_legacy_persisted_duration(self):
        """Use the default duration when no CLI value is provided."""
        mocks = self._run_login({}, legacy_duration=34200)
        self.assertEqual(mocks["assume"].call_args[0][4], login_module._DURATION_DEFAULT)

    def test_duration_boundaries_are_accepted(self):
        """Allow both 1800 and 43200 second duration boundaries."""
        for duration in (1800, 43200):
            mocks = self._run_login({"duration": duration})
            self.assertEqual(mocks["assume"].call_args[0][4], duration)

    def test_out_of_range_duration_stops_before_login_flow(self):
        """Reject invalid durations before reading credentials or opening a browser."""
        for duration in (1799, 43201):
            with mock.patch.object(login_module.sso, "cred_path_of_profile") as cred_path:
                with mock.patch.object(login_module, "_get_token") as get_token:
                    with mock.patch.object(login_module, "print_message") as print_message:
                        login_module.login({"duration": duration}, "default", "zh-CN")
            cred_path.assert_not_called()
            get_token.assert_not_called()
            self.assertIn("duration", print_message.call_args[0][0])


# ---------------------------------------------------------------------------
# TestLoginCredentialReplacement
# ---------------------------------------------------------------------------

class TestLoginCredentialReplacement(unittest.TestCase):
    """Keep the previous credential when SSO login fails."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_sso_login_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")
        self.old_cred = {
            "type": "cvm-role",
            "secretId": "OLD_ID",
            "sso": {"authUrl": "https://example.com"},
        }
        with open(self.cred_path, "w") as cred_file:
            json.dump(self.old_cred, cred_file)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_login_failure_preserves_old_credential(self):
        """Do not save a new credential when SSO network login fails."""
        with mock.patch.object(
                login_module.sso, "cred_path_of_profile", return_value=self.cred_path):
            with mock.patch.object(
                    login_module, "_get_token", side_effect=RuntimeError("login failed")):
                with mock.patch.object(login_module.sso, "save_credential") as save_credential:
                    with self.assertRaises(RuntimeError):
                        login_module.login({}, "default", "zh-CN")
        save_credential.assert_not_called()
        with open(self.cred_path, "r") as cred_file:
            self.assertEqual(json.load(cred_file), self.old_cred)


# ---------------------------------------------------------------------------
# TestLoginRememberSelection
# ---------------------------------------------------------------------------

class TestLoginRememberSelection(unittest.TestCase):
    """Default interactive selection to the last-used UIN and role."""

    def _run(self, cred_sso=None, args=None, accounts=None, roles=None, select_returns=None):
        cred_data = {"sso": {"authUrl": "https://example.com"}}
        if cred_sso:
            cred_data["sso"].update(cred_sso)
        if accounts is None:
            accounts = _ACCOUNTS
        if roles is None:
            roles = _ROLES

        if select_returns is None:
            select_patch = mock.patch.object(
                login_module.terminal, "select_from_items", return_value=0)
        else:
            select_patch = mock.patch.object(
                login_module.terminal, "select_from_items", side_effect=select_returns)

        patchers = [
            ("open", mock.patch(
                _BUILTINS_MODULE + ".open", mock.mock_open(read_data=json.dumps(cred_data)))),
            ("exists", mock.patch.object(login_module.os.path, "exists", return_value=True)),
            ("cred_path", mock.patch.object(
                login_module.sso, "cred_path_of_profile", return_value="/tmp/default.credential")),
            ("get_token", mock.patch.object(
                login_module, "_get_token",
                side_effect=lambda auth_url, state, language: {
                    "State": state, "Token": "login-token", "Site": "ap"
                })),
            ("accounts", mock.patch.object(
                login_module.sso, "list_accounts_for_access_assignment", return_value=accounts)),
            ("roles", mock.patch.object(
                login_module.sso, "list_role_configurations_for_account", return_value=roles)),
            ("gen_saml", mock.patch.object(
                login_module.sso, "gen_saml_response", return_value={"SAMLResponse": "saml"})),
            ("verify", mock.patch.object(
                login_module.sso, "verify_login_skey", return_value={"ZoneId": "zone"})),
            ("assume", mock.patch.object(
                login_module.sso, "assume_role_with_saml", return_value=_make_cred_resp())),
            ("save", mock.patch.object(login_module.sso, "save_credential")),
            ("print", mock.patch.object(login_module, "print_message")),
            ("select", select_patch),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            login_module.login(args or {}, "default", "zh-CN")
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    def _assert_selector_call(self, call, items, default_idx):
        self.assertEqual(call[0][1], items)
        self.assertEqual(call[0][2], 10)
        self.assertEqual(call[0][3], default_idx)

    def test_interactive_login_focuses_last_uin_and_role(self):
        """Use the stored numeric UIN and role as selector defaults."""
        mocks = self._run(
            cred_sso={"uin": 456, "roleConfigurationName": "role-b"},
            select_returns=[1, 1])
        calls = mocks["select"].call_args_list
        self.assertEqual(len(calls), 2)
        self._assert_selector_call(calls[0], ["a:123", "b:456"], 1)
        self._assert_selector_call(calls[1], ["role-a", "role-b"], 1)
        saved = mocks["save"].call_args[0][1]
        self.assertEqual(saved["uin"], 456)
        self.assertEqual(saved["roleConfigurationName"], "role-b")

    def test_unknown_last_uin_falls_back_to_first_account_and_role(self):
        """Start both selectors at the first item when the stored UIN is unknown."""
        mocks = self._run(
            cred_sso={"uin": 999, "roleConfigurationName": "role-b"},
            select_returns=[0, 0])
        calls = mocks["select"].call_args_list
        self._assert_selector_call(calls[0], ["a:123", "b:456"], 0)
        self._assert_selector_call(calls[1], ["role-a", "role-b"], 0)

    def test_unknown_last_role_falls_back_to_first_role(self):
        """Start at the first role when the stored role is unavailable."""
        mocks = self._run(
            cred_sso={"uin": 123, "roleConfigurationName": "missing"},
            select_returns=[0, 0])
        calls = mocks["select"].call_args_list
        self._assert_selector_call(calls[0], ["a:123", "b:456"], 0)
        self._assert_selector_call(calls[1], ["role-a", "role-b"], 0)

    def test_role_memory_is_not_applied_to_a_different_account(self):
        """Do not reuse a stored role after switching accounts."""
        mocks = self._run(
            cred_sso={"uin": 123, "roleConfigurationName": "role-b"},
            select_returns=[1, 0])
        calls = mocks["select"].call_args_list
        self._assert_selector_call(calls[0], ["a:123", "b:456"], 0)
        self._assert_selector_call(calls[1], ["role-a", "role-b"], 0)
        saved = mocks["save"].call_args[0][1]
        self.assertEqual(saved["uin"], 456)
        self.assertEqual(saved["roleConfigurationName"], "role-a")

    def test_no_history_starts_at_first_item(self):
        """Start both selectors at zero when no selection history exists."""
        mocks = self._run(select_returns=[0, 0])
        calls = mocks["select"].call_args_list
        self._assert_selector_call(calls[0], ["a:123", "b:456"], 0)
        self._assert_selector_call(calls[1], ["role-a", "role-b"], 0)

    def test_specified_uin_still_remembers_role_for_that_account(self):
        """Remember the role when an explicit UIN matches the stored account."""
        mocks = self._run(
            cred_sso={"uin": 456, "roleConfigurationName": "role-b"},
            args={"uin": "456"},
            select_returns=[1])
        calls = mocks["select"].call_args_list
        self.assertEqual(len(calls), 1)
        self._assert_selector_call(calls[0], ["role-a", "role-b"], 1)

    def test_specified_uin_of_another_account_does_not_reuse_last_role(self):
        """Do not reuse the stored role for a different explicit UIN."""
        mocks = self._run(
            cred_sso={"uin": 456, "roleConfigurationName": "role-b"},
            args={"uin": "123"},
            select_returns=[0])
        calls = mocks["select"].call_args_list
        self.assertEqual(len(calls), 1)
        self._assert_selector_call(calls[0], ["role-a", "role-b"], 0)

    def test_specified_uin_and_role_skip_selector(self):
        """Skip interactive selection when both UIN and role are specified."""
        mocks = self._run(args={"uin": "123", "rolename": "role-a"})
        mocks["select"].assert_not_called()
        saved = mocks["save"].call_args[0][1]
        self.assertEqual(saved["uin"], 123)
        self.assertEqual(saved["roleConfigurationName"], "role-a")


if __name__ == "__main__":
    unittest.main()
