# -*- coding: utf-8 -*-
import json
import sys
import time
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tccli.plugins.sso import list as list_module


_ACCOUNTS = [
    {"Uin": 123, "Name": "a"},
    {"Uin": 456, "Name": "b"},
]

_ROLES = [
    {"RoleConfigurationName": "role-a", "RoleConfigurationId": "rid-a"},
    {"RoleConfigurationName": "role-b", "RoleConfigurationId": "rid-b"},
]

_SESSION = {"token": "login-token", "site": "cn", "expiresAt": time.time() + 3600}


class _BaseCase(unittest.TestCase):

    def _run(self, entrypoint, session=_SESSION, args=None, accounts=None, roles=None):
        patchers = [
            ("session", mock.patch.object(list_module.sso, "load_login_token", return_value=session)),
            ("accounts", mock.patch.object(
                list_module.sso, "list_accounts_for_access_assignment",
                return_value=_ACCOUNTS if accounts is None else accounts)),
            ("roles", mock.patch.object(
                list_module.sso, "list_role_configurations_for_account",
                return_value=_ROLES if roles is None else roles)),
            ("print", mock.patch.object(list_module, "print_message")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            entrypoint(args or {}, {"language": "en-US", "profile": "default"})
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    @staticmethod
    def _output(mocks):
        return "\n".join(call[0][0] if call[0] else "" for call in mocks["print"].call_args_list)


class TestListUin(_BaseCase):

    def test_lists_all_accounts_with_login_token(self):
        """list-uin fetches all member accounts with the cached login state."""
        mocks = self._run(list_module.list_uin_command_entrypoint)
        self.assertEqual(mocks["accounts"].call_args[0], ("login-token", "cn"))
        output = self._output(mocks)
        self.assertIn("123", output)
        self.assertIn("456", output)

    def test_json_output_keeps_uin_as_string(self):
        """Json output renders Uin as a string to avoid big-int precision loss in scripts."""
        mocks = self._run(list_module.list_uin_command_entrypoint, args={"output": "json"})
        payload = json.loads("\n".join(
            call[0][0] for call in mocks["print"].call_args_list))
        self.assertEqual(payload, [
            {"Uin": "123", "Name": "a"},
            {"Uin": "456", "Name": "b"},
        ])

    def test_expired_login_ask_for_relogin(self):
        """An expired login state only asks for re-login without any API call."""
        mocks = self._run(list_module.list_uin_command_entrypoint, session=None)
        mocks["accounts"].assert_not_called()
        self.assertIn("login state expired", self._output(mocks))

    def test_no_account_reports_message(self):
        mocks = self._run(list_module.list_uin_command_entrypoint, accounts=[])
        self.assertIn("no account found", self._output(mocks))


class TestListRole(_BaseCase):

    def test_lists_roles_of_specified_uin(self):
        """list-role --uin queries the roles of that uin and prints the role id."""
        mocks = self._run(list_module.list_role_command_entrypoint, args={"uin": "456"})
        self.assertEqual(mocks["roles"].call_args[0], ("456", "login-token", "cn"))
        output = self._output(mocks)
        self.assertIn("role-a", output)
        self.assertIn("rid-b", output)

    def test_json_output_includes_uin_and_role_id(self):
        """The same role has a different id under another uin, so json must carry both uin and role id."""
        mocks = self._run(
            list_module.list_role_command_entrypoint, args={"uin": "456", "output": "json"})
        payload = json.loads("\n".join(
            call[0][0] for call in mocks["print"].call_args_list))
        self.assertEqual(payload, [
            {"Uin": "456", "RoleConfigurationName": "role-a", "RoleConfigurationId": "rid-a"},
            {"Uin": "456", "RoleConfigurationName": "role-b", "RoleConfigurationId": "rid-b"},
        ])

    def test_uin_is_asked_interactively_when_omitted(self):
        """Ask for the uin interactively when --uin is omitted."""
        with mock.patch.object(list_module.terminal, "select_from_items", return_value=1) as select:
            mocks = self._run(list_module.list_role_command_entrypoint)
        self.assertEqual(select.call_args[0][1], ["a:123", "b:456"])
        self.assertEqual(mocks["roles"].call_args[0][0], "456")

    def test_expired_login_ask_for_relogin(self):
        mocks = self._run(list_module.list_role_command_entrypoint, session=None, args={"uin": "456"})
        mocks["roles"].assert_not_called()

    def test_no_role_reports_message(self):
        mocks = self._run(list_module.list_role_command_entrypoint, args={"uin": "456"}, roles=[])
        self.assertIn("no role found", self._output(mocks))


if __name__ == "__main__":
    unittest.main()
