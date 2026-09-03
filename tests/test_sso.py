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

from tccli import sso as sso_module
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


def _make_sso_info():
    """Build the base SSO information payload."""
    return {
        "token": "t",
        "uin": 123,
        "roleConfigurationId": "rid",
        "roleConfigurationName": "rname",
        "zoneId": "z",
        "site": "ap",
        "authUrl": "https://example.com",
        "expiresAt": int(time.time()) + 3600 * 12,
    }


def _make_refresh_credential(now, sso_remaining):
    """Build an expiring SSO credential that enters the refresh flow."""
    return {
        "type": "sso",
        "expiresAt": now + 10,
        "sso": {
            "expiresAt": now + sso_remaining,
            "token": "t",
            "uin": 123,
            "roleConfigurationId": "rid",
            "roleConfigurationName": "rname",
            "zoneId": "z",
            "site": "ap",
            "authUrl": "https://example.com",
        },
    }


# ---------------------------------------------------------------------------
# TestSaveCredential
# ---------------------------------------------------------------------------

class TestSaveCredential(unittest.TestCase):
    """Atomically replace the previous credential after a successful SSO login."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_sso_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")
        self.path_patcher = mock.patch.object(
            sso_module, "cred_path_of_profile", return_value=self.cred_path)
        self.path_patcher.start()

    def tearDown(self):
        self.path_patcher.stop()
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write_old_credential(self, data):
        with open(self.cred_path, "w") as cred_file:
            json.dump(data, cred_file)

    def _read_credential(self):
        with open(self.cred_path, "r") as cred_file:
            return json.load(cred_file)

    def _call_save(self, sso_info=None):
        sso_module.save_credential(
            _make_cred_resp(), sso_info or _make_sso_info(), "default")
        return self._read_credential()

    def test_legacy_default_duration_is_not_persisted(self):
        """Discard the legacy field when writing a new credential."""
        sso_info = _make_sso_info()
        sso_info["defaultDuration"] = 34200
        data = self._call_save(sso_info)
        self.assertNotIn("defaultDuration", data["sso"])

    def test_success_replaces_cvm_role_with_sso_credential(self):
        """Replace CVM role data with a complete SSO credential after login succeeds."""
        self._write_old_credential({"type": "cvm-role", "secretId": "OLD_ID"})
        data = self._call_save()
        self.assertEqual(data["type"], "sso")
        self.assertEqual(data["secretId"], "sid")
        self.assertEqual(data["secretKey"], "skey")
        self.assertEqual(data["token"], "tok")
        self.assertNotIn("defaultDuration", data["sso"])

    def test_atomic_replace_failure_preserves_old_credential(self):
        """Keep the previous CVM role credential when atomic replacement fails."""
        old_cred = {"type": "cvm-role", "secretId": "OLD_ID"}
        self._write_old_credential(old_cred)
        with mock.patch("tccli.utils.os.rename", side_effect=OSError("rename failed")):
            with self.assertRaises(Exception):
                self._call_save()
        self.assertEqual(self._read_credential(), old_cred)


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
        """Reject out-of-range durations before reading credentials or opening a browser."""
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
# TestAutoRefresh
# ---------------------------------------------------------------------------

class TestAutoRefresh(unittest.TestCase):
    """Test automatic credential refresh in sso.py."""

    def _run_refresh(self, sso_remaining, time_values=None):
        now = 100000.0
        cred = _make_refresh_credential(now, sso_remaining)
        patchers = [
            ("open", mock.patch(_BUILTINS_MODULE + ".open", mock.mock_open(read_data=json.dumps(cred)))),
            ("time", mock.patch.object(
                sso_module.time, "time", side_effect=time_values or [now, now])),
            ("gen_saml", mock.patch.object(
                sso_module, "gen_saml_response", return_value={"SAMLResponse": "saml"})),
            ("assume", mock.patch.object(
                sso_module, "assume_role_with_saml", return_value=_make_cred_resp())),
            ("save", mock.patch.object(sso_module, "save_credential")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            sso_module.maybe_refresh_credential("default")
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    def test_refresh_minimum_session_remaining_is_300(self):
        """Use a 300 second minimum remaining SSO session duration for refresh."""
        self.assertEqual(sso_module._SKEY_REFRESH_SAFE_DUR, 300)

    def test_no_refresh_below_minimum_session_remaining(self):
        """Do not refresh when the SSO session has fewer than 300 seconds left."""
        mocks = self._run_refresh(299)
        mocks["gen_saml"].assert_not_called()
        mocks["assume"].assert_not_called()

    def test_refresh_accepts_minimum_session_remaining(self):
        """Allow a refresh when exactly 300 seconds remain in the SSO session."""
        mocks = self._run_refresh(300)
        self.assertEqual(mocks["assume"].call_args[0][4], 300)

    def test_refresh_duration_capped_by_session_remaining(self):
        """Cap refreshed credential duration to the remaining SSO session time."""
        mocks = self._run_refresh(3000)
        self.assertEqual(mocks["assume"].call_args[0][4], 3000)

    def test_refresh_duration_uses_default_when_session_sufficient(self):
        """Use the default credential duration when the SSO session lasts long enough."""
        mocks = self._run_refresh(36000)
        self.assertEqual(mocks["assume"].call_args[0][4], sso_module._CRED_DEFAULT_DUR)

    def test_refresh_checks_session_with_current_time(self):
        """Skip SAML generation when the current remaining session time drops below 300 seconds."""
        now = 100000.0
        mocks = self._run_refresh(400, time_values=[now, now + 101])
        mocks["gen_saml"].assert_not_called()
        mocks["assume"].assert_not_called()


if __name__ == "__main__":
    unittest.main()
