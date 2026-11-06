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


# ---------------------------------------------------------------------------
# TestLoginTokenCache
# ---------------------------------------------------------------------------

class TestLoginTokenCache(unittest.TestCase):
    """The SSO login state is cached in the credential file and reused by list-* and later logins."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_sso_token_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write_cred(self, cred):
        with open(self.cred_path, "w") as cred_file:
            json.dump(cred, cred_file)

    def _load(self):
        with mock.patch.object(
                sso_module, "cred_path_of_profile", return_value=self.cred_path):
            return sso_module.load_login_token("default")

    def test_load_token_from_saved_credential(self):
        """The login state saved by login can be read back."""
        info = _make_sso_info()
        with mock.patch.object(
                sso_module, "cred_path_of_profile", return_value=self.cred_path):
            sso_module.save_credential(_make_cred_resp(), info, "default", "login-token")
        loaded = self._load()
        self.assertEqual(loaded["token"], "login-token")
        self.assertEqual(loaded["site"], info["site"])
        self.assertEqual(loaded["expiresAt"], info["expiresAt"])

    def test_credential_without_login_token_has_no_session(self):
        """A credential written without ssoSession has no usable login state."""
        info = _make_sso_info()
        with mock.patch.object(
                sso_module, "cred_path_of_profile", return_value=self.cred_path):
            sso_module.save_credential(_make_cred_resp(), info, "default")
        self.assertIsNone(self._load())

    def test_expiring_login_token_is_rejected(self):
        """A login state inside the safety window is not reused."""
        self._write_cred({
            "type": "sso",
            "sso": {"site": "cn"},
            "ssoSession": {"token": "t", "expiresAt": int(time.time()) + 60},
        })
        self.assertIsNone(self._load())

    def test_non_sso_credential_has_no_session(self):
        self._write_cred({"type": "cvm-role", "ssoSession": {"token": "t", "expiresAt": time.time() + 3600}})
        self.assertIsNone(self._load())

    def test_missing_or_corrupted_file_is_tolerated(self):
        self.assertIsNone(self._load())
        with open(self.cred_path, "w") as cred_file:
            cred_file.write("{not json")
        self.assertIsNone(self._load())

    def test_saved_login_state_does_not_replace_sts_credential(self):
        """Caching the login state keeps the STS credential fields untouched."""
        info = _make_sso_info()
        with mock.patch.object(
                sso_module, "cred_path_of_profile", return_value=self.cred_path):
            sso_module.save_credential(_make_cred_resp(), info, "default", "login-token")
        with open(self.cred_path) as cred_file:
            cred = json.load(cred_file)
        self.assertEqual(cred["type"], "sso")
        self.assertEqual(cred["secretId"], "sid")
        self.assertEqual(cred["token"], "tok")
        self.assertIn("ssoSession", cred)


if __name__ == "__main__":
    unittest.main()
