# -*- coding: utf-8 -*-
import os
import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

_BUILTINS_MODULE = "__builtin__" if sys.version_info[0] == 2 else "builtins"

from tccli.plugins.sso import terminal


_ITEMS = ["alpha", "beta", "gamma"]


class TestSelectFromItemsUnix(unittest.TestCase):
    """Test Unix selector defaults, Enter, and Backspace."""

    def _run(self, keys, default=0, items=None, page_size=10):
        with mock.patch.object(terminal, "_getch_wrap", side_effect=keys):
            with mock.patch.object(terminal.sys, "stdout"):
                return terminal._select_from_items_unix(
                    "prompt ", items or _ITEMS, page_size, default)

    def test_enter_returns_default_index(self):
        """Select the default index on Enter, including later pages."""
        self.assertEqual(self._run([terminal._ENTER], default=2), 2)
        items = ["i%d" % i for i in range(12)]
        self.assertEqual(self._run([terminal._ENTER], default=11, items=items), 11)

    def test_empty_backspace_keeps_default_index(self):
        """Keep the default index when Backspace is pressed on an empty search."""
        idx = self._run([terminal._BACKSPACE, terminal._ENTER], default=2)
        self.assertEqual(idx, 2)

    def test_search_enter_returns_original_index(self):
        """Return the original item index after searching."""
        idx = self._run(["b", terminal._ENTER], default=2)
        self.assertEqual(idx, 1)

    def test_backspace_after_search_resets_selection(self):
        """Reset selection after Backspace clears a search."""
        idx = self._run(["b", terminal._BACKSPACE, terminal._ENTER], default=2)
        self.assertEqual(idx, 0)


class TestSelectFromItemsWin(unittest.TestCase):
    """Test the Windows selector default index."""

    def _input_name(self):
        if sys.version_info[0] == 2:
            return "raw_input"
        return "input"

    def _run(self, answers, default=0, items=None):
        input_patch = mock.patch(
            _BUILTINS_MODULE + "." + self._input_name(), side_effect=answers)
        with input_patch:
            with mock.patch.object(terminal.sys, "stdout") as stdout:
                idx = terminal._select_from_items_win(
                    "choose: ", items or _ITEMS, 10, default)
        return idx, stdout

    def test_empty_input_returns_default_and_shows_it(self):
        """Show and return the default index for empty input."""
        idx, stdout = self._run([""], default=1)
        self.assertEqual(idx, 1)
        stdout.write.assert_any_call("choose: [1] ")

    def test_blank_input_returns_default(self):
        """Use the default index for whitespace-only input."""
        idx, _ = self._run(["  "], default=2)
        self.assertEqual(idx, 2)

    def test_numeric_input_returns_that_index(self):
        """Return a valid numeric selection."""
        idx, _ = self._run(["1"], default=0)
        self.assertEqual(idx, 1)

    def test_invalid_input_is_retried(self):
        """Retry invalid input until a valid index is entered."""
        idx, _ = self._run(["x", "9", "0"], default=2)
        self.assertEqual(idx, 0)


class TestSelectFromItemsDispatch(unittest.TestCase):

    def test_public_selector_matches_platform(self):
        if os.name == "nt":
            self.assertIs(terminal.select_from_items, terminal._select_from_items_win)
        else:
            self.assertIs(terminal.select_from_items, terminal._select_from_items_unix)


if __name__ == "__main__":
    unittest.main()
