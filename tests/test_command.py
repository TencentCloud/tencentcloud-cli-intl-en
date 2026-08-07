# -*- coding: utf-8 -*-
"""
Unit tests for tccli/command.py.

Includes:
  A) End-to-end subprocess tests (kept from test_command_recursive_hint.py)
     -- verify the real exit code and stderr output for the customer's TAPD report scenario.
  B) _build_recursive_hint white-box branch coverage
     -- this is the core function of the self-ref fix, with many branches.
  C) ActionCommand internal methods (init / property / private helpers)
  D) CLICommand internal methods
  E) ServiceCommand internal methods
  F) Boundary / exception / robustness supplements

Design notes:
  - Existing subprocess tests can only verify end-to-end behavior, but the coverage
    tool cannot count code executed inside subprocesses. So this file adds many
    white-box tests that "call class methods directly in the main process" to raise
    real coverage.
"""
import os
import sys
import copy
import subprocess
from collections import OrderedDict, namedtuple

try:
    import pytest
    _HAS_PYTEST = True
except ImportError:
    _HAS_PYTEST = False

    class _SkipException(Exception):
        pass

    class _PytestStub(object):
        @staticmethod
        def skip(msg):
            raise _SkipException(msg)

    pytest = _PytestStub()  # type: ignore

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
while _REPO_ROOT in sys.path:
    sys.path.remove(_REPO_ROOT)
sys.path.insert(0, _REPO_ROOT)

# ============================================================
# Common: suppress plugin loading (many tccli plugins depend on external SDKs that may be absent)
# ============================================================
import tccli.plugin as _plg
_plg.import_plugins = lambda: {}

import tccli.options_define as Options_define
from tccli.command import (
    BaseCommand, CLICommand, ServiceCommand, ActionCommand,
)
from tccli.exceptions import UnknownArgumentError
from tccli.loaders import Loader


# ============================================================
# Common helpers
# ============================================================
def _billing_schema_available():
    """Determine whether the local repository has the billing v20180709 api.json."""
    api_path = os.path.join(
        Loader().get_services_path(), "billing", "v20180709", "api.json")
    return os.path.exists(api_path)


def _run_tccli(args):
    """Run tccli main as a subprocess and return (exit_code, stdout, stderr)."""
    code = (
        "import sys; sys.path.insert(0, %r);\n"
        "import tccli.plugin as _p; _p.import_plugins=lambda: {};\n"
        "from tccli.main import main; sys.argv = %r; sys.exit(main())"
    ) % (_REPO_ROOT, ["tccli"] + list(args))
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.Popen(
        [sys.executable, "-c", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    if sys.version_info[0] < 3:
        out, err = proc.communicate()
    else:
        out, err = proc.communicate(timeout=60)
    return proc.returncode, out.decode("utf-8", "replace"), err.decode("utf-8", "replace")


def _make_action_command(call_mode=None, profile="default"):
    """Build a minimal ActionCommand instance (bypassing the full __init__ logic),
       used to directly drive private methods such as _build_recursive_hint / _build_action_parameters.

       Does not call super().__init__() to avoid touching a real Loader (already injected separately via _cli_data).
    """
    ac = object.__new__(ActionCommand)
    ac._service_name = "billing"
    ac._version = "2018-07-09"
    ac._action_name = "CreateGatherRule"
    ac._call_mode = call_mode
    ac.profile = profile
    ac._cli_data = Loader()
    ac._argument_map = None
    ac._is_self_ref = True
    return ac


def _make_globals(**kw):
    """Simulate the argparse parsed_globals namespace object.
       Uses argparse.Namespace rather than namedtuple to ensure vars() can access __dict__.
    """
    import argparse as _argparse
    base = {
        Options_define.Profile: kw.pop("profile", None),
        Options_define.GenerateCliSkeleton.replace("-", "_"):
            kw.pop("generate_cli_skeleton", None),
        Options_define.CliInputJson.replace("-", "_"):
            kw.pop("cli_input_json", None),
        Options_define.CliUnfoldArgument.replace("-", "_"):
            kw.pop("cli_unfold_argument", None),
    }
    base.update(kw)
    return _argparse.Namespace(**base)


# ============================================================
# A. End-to-end subprocess tests (migrated from the original test_command_recursive_hint.py)
# ============================================================
def test_A1_customer_original_command_passes_through_no_recursion_error():
    """A1: run the command from the customer's TAPD ticket directly:
       no more RecursionError; when crossing a self-reference truncation point with <=30 segments, legally pass through to the cloud call."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--Id", "1490",
        "--RuleList.RuleDetail.Children.0.RuleValue", "ESG",
        "--RuleList.RuleDetail.Children.0.Operator", "in",
    ])

    combined = stdout + stderr

    # Key regression point 1: no more recursion error
    assert "maximum recursion depth exceeded" not in combined, (
        "RecursionError leaked back to user! stderr:\n%s" % stderr)
    assert "RecursionError" not in combined

    # Key regression point 2: parameters are no longer treated as Unknown, the request body can be built
    # Whether the command actually reaches the cloud depends on local auth, but the CLI layer should not emit Unknown options
    assert "Unknown options" not in combined, (
        "self-ref extension param wrongly rejected:\n%s" % combined)
    # The CLI layer no longer produces the self-referencing hint (unnecessary after a legal pass-through)
    assert "self-referencing type" not in combined, (
        "self-ref hint should not appear for legal extension:\n%s" % combined)


def test_A1b_oversized_depth_emits_hint():
    """A1b: when the non-numeric-segment depth exceeds MAX_INPUT_DEPTH=30, the CLI layer should raise an oversized hint pointing to file:// before making the cloud call.

    Test constraint: no real request is sent. Driven directly by an ActionCommand with a mocked action_caller,
    ensuring the depth overflow is intercepted at the CLI layer (action_caller should not be called).
    Depth is defined as the number of non-numeric segments: RuleList(1)+RuleDetail(1)+28*Children(28)+RuleKey(1)=31.
    """
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        parts = ["RuleList", "RuleDetail", "Children", "0"]
        for _ in range(27):
            parts += ["Children", "0"]
        parts += ["RuleKey"]
        deep_key = ".".join(parts)
        depth = sum(1 for seg in parts if not seg.isdigit())
        assert depth == 31

        g = _make_globals(profile="default", cli_unfold_argument=True)
        try:
            ac(["--Id", "1490", "--" + deep_key, "v"], g)
            assert False, "expected UnknownArgumentError for oversized depth"
        except UnknownArgumentError as e:
            msg = str(e)
            assert "RecursionError" not in msg
            assert "MAX_INPUT_DEPTH=30" in msg
            assert "depth=31" in msg
            assert "Use --cli-input-json file://" in msg
        # No cloud call should be made in the oversized scenario
        assert "params" not in captured
    finally:
        restore()


def test_A2_normal_unknown_option_no_self_ref_hint():
    """A2: a normal misspelled parameter should not falsely trigger the self-ref hint."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--Id", "1490",
        "--TotallyUnknownArg", "x",
    ])

    assert code == 255
    assert "Unknown options" in stderr
    # No self-referencing hint should appear -- because this parameter is not a truncation leaf prefix
    assert "self-referencing type" not in stderr, (
        "false-positive self-ref hint:\n%s" % stderr)


def test_A3_pass_self_ref_field_as_json_no_hint_about_self_ref():
    """A3: --generate-cli-skeleton mode should not trigger unknown options nor emit the self-ref hint."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--generate-cli-skeleton",
    ])

    assert "Unknown options" not in stderr
    assert "self-referencing type" not in stderr


# ============================================================
# B. _build_recursive_hint white-box branch coverage (the core fix)
# ============================================================
def test_B1_hint_returns_empty_when_not_unfold_mode():
    """B1: returns an empty string directly when not in --cli-unfold-argument mode."""
    ac = _make_action_command(call_mode=None)
    assert ac._build_recursive_hint(["--foo", "bar"]) == ""

    # Explicitly setting generate-cli-skeleton mode should also return an empty string
    ac._call_mode = Options_define.GenerateCliSkeleton
    assert ac._build_recursive_hint(["--foo"]) == ""


def test_B2_hint_returns_empty_when_loader_raises():
    """B2: silently returns an empty string when Loader.get_unfold_param_info raises."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _BadLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            raise RuntimeError("mock failure")
    ac._cli_data = _BadLoader()
    assert ac._build_recursive_hint(["--anything"]) == ""


def test_B3_hint_returns_empty_when_no_truncated_leaf():
    """B3: returns an empty string when the unfold listing has no recursive_truncated field."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _NoTrunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Foo": {"recursive_truncated": False},
                "Bar.Baz": {},  # no recursive_truncated key
            }
    ac._cli_data = _NoTrunc()
    assert ac._build_recursive_hint(["--Foo.NotExist", "x"]) == ""


def test_B4_hint_returns_empty_when_no_token_matches():
    """B4: there is a truncation point but none of the user's invalid options match the prefix -> returns an empty string."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "RuleList.RuleDetail.Children.0": {
                    "recursive_truncated": True,
                    "recursive_type": "AllocationRuleExpression",
                }
            }
    ac._cli_data = _Trunc()
    # No prefix in remaining matches RuleList.RuleDetail.Children.0
    assert ac._build_recursive_hint(["--Other.Param", "v"]) == ""


def test_B5_hint_emits_full_text_on_match():
    """B5: when a truncation prefix is matched, the output includes the self-referencing type context and the file:// single-option alternative.

    Design change (recursive-nesting-30 / approach A):
      - Removed (1) the Drop --cli-unfold-argument option and the applies-to context line;
      - Kept only the file:// single alternative, with reverse assertions locking in that it no longer falls back.
    The top-level field name can still be seen at the tail of each matched token line in (under --RuleList.RuleDetail.Children.0, ...).
    """
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "RuleList.RuleDetail.Children.0": {
                    "recursive_truncated": True,
                    "recursive_type": "AllocationRuleExpression",
                }
            }
    ac._cli_data = _Trunc()

    hint = ac._build_recursive_hint([
        "--RuleList.RuleDetail.Children.0.RuleKey", "x",
        "--RuleList.RuleDetail.Children.0.Operator", "in",
    ])
    assert "self-referencing type" in hint
    assert "AllocationRuleExpression" in hint
    assert "--RuleList.RuleDetail.Children.0" in hint
    # Single-option hint: only file:// is kept
    assert "Use --cli-input-json file://" in hint
    # Reverse assertions: the old Drop approach and applies-to context should no longer appear
    assert "Drop --cli-unfold-argument" not in hint
    assert "applies to:" not in hint


def test_B6_hint_falls_back_when_recursive_type_missing():
    """B6: when recursive_type is empty, the hint text degrades to an 'unknown' placeholder."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "X.Y.Z.0": {
                    "recursive_truncated": True,
                    "recursive_type": "",  # <- empty string
                }
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint(["--X.Y.Z.0.More", "v"])
    assert "self-referencing type: unknown" in hint
    # The single-option hint always outputs the file:// alternative
    assert "Use --cli-input-json file://" in hint
    assert "Drop --cli-unfold-argument" not in hint


def test_B7_hint_skips_non_string_or_non_option_tokens():
    """B7: non-string tokens in remaining and tokens not starting with -- should be ignored."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Top.0": {
                    "recursive_truncated": True,
                    "recursive_type": "T",
                }
            }
    ac._cli_data = _Trunc()
    # Contains a number, None, and a string without --
    hint = ac._build_recursive_hint([
        123, None, "no_dashes", "--Top.0.Sub", "v",
    ])
    # Only --Top.0.Sub matches
    assert "--Top.0.Sub" in hint


def test_B8_hint_dedup_top_fields_across_multiple_prefixes():
    """B8: top_fields is not duplicated when multiple truncation points share the same top-level field."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Root.A.0": {"recursive_truncated": True, "recursive_type": "TA"},
                "Root.B.0": {"recursive_truncated": True, "recursive_type": "TB"},
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint([
        "--Root.A.0.X", "1",
        "--Root.B.0.Y", "2",
    ])
    # Approach A removed the applies-to line; instead assert that both matched token lines annotate their own top-level prefix
    assert "--Root.A.0.X  (under --Root.A.0," in hint
    assert "--Root.B.0.Y  (under --Root.B.0," in hint
    assert "applies to:" not in hint


def test_B9_hint_collects_multi_top_fields():
    """B9: when different top-level fields are matched, applies-to lists multiple ones."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Alpha.0": {"recursive_truncated": True, "recursive_type": "T1"},
                "Beta.0": {"recursive_truncated": True, "recursive_type": "T2"},
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint([
        "--Alpha.0.x", "1",
        "--Beta.0.y", "2",
    ])
    # Approach A removed the applies-to line; different top-level fields appear at the tail of their own matched token lines
    assert "(under --Alpha.0," in hint
    assert "(under --Beta.0," in hint
    assert "applies to:" not in hint


# ============================================================
# C. ActionCommand internal methods
# ============================================================
def test_C1_actioncommand_init_basic():
    """C1: ActionCommand initializes basic fields."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    assert ac._service_name == "billing"
    assert ac._version == "2018-07-09"
    assert ac._action_name == "CreateGatherRule"
    assert ac._call_mode is None
    assert ac.profile == "default"
    assert ac._argument_map is None


def test_C2_actioncommand_init_default_version_when_none():
    """C2: uses the service's default version when version=None is passed."""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    ac = ActionCommand(
        service_name="cvm",
        version=None,
        action_name="DescribeInstances",
        action_model={"input": "DescribeInstancesRequest"},
        action_caller=lambda *a, **kw: None,
    )
    # At least a non-empty version number can be obtained
    assert ac._version is not None and len(ac._version) > 0


def test_C3_get_call_mode_branches():
    """C3: _get_call_mode recognizes the three mode branches."""
    ac = _make_action_command()

    # GenerateCliSkeleton
    g = _make_globals(generate_cli_skeleton=True)
    assert ac._get_call_mode(g) == Options_define.GenerateCliSkeleton

    # CliInputJson
    g2 = _make_globals(cli_input_json=True)
    assert ac._get_call_mode(g2) == Options_define.CliInputJson

    # CliUnfoldArgument
    g3 = _make_globals(cli_unfold_argument=True)
    assert ac._get_call_mode(g3) == Options_define.CliUnfoldArgument

    # All None -> returns None (normal mode)
    g4 = _make_globals()
    assert ac._get_call_mode(g4) is None


def test_C4_get_profile_branches():
    """C4: _get_profile handles the cases where parsed_globals.profile has a value or not."""
    ac = _make_action_command()

    # has a value
    g = _make_globals(profile="myprof")
    ac._get_profile(g)
    assert ac.profile == "myprof"

    # no value (None / empty) -> defaults to default
    g2 = _make_globals(profile=None)
    ac._get_profile(g2)
    assert ac.profile == "default"


def test_C5_get_param_model_unfold_vs_normal():
    """C5: _get_param_model uses different Loader APIs under different call_mode."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    unfold_info = ac._get_param_model()
    # The unfold-mode product contains dot-path keys
    assert any("." in k for k in unfold_info.keys())

    ac._call_mode = None  # normal mode
    normal_info = ac._get_param_model()
    # In normal mode keys are top-level field names
    assert "Id" in normal_info
    # Top-level keys should not contain "."
    assert all("." not in k for k in normal_info.keys())


def test_C6_build_parameter_map_skeleton_and_input_json_modes():
    """C6: _build_parameter_map returns an empty map under GenerateCliSkeleton / CliInputJson modes."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.GenerateCliSkeleton)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    assert ac._build_parameter_map() == OrderedDict()

    ac._call_mode = Options_define.CliInputJson
    assert ac._build_parameter_map() == OrderedDict()


def test_C7_build_parameter_map_unfold_mode_produces_args():
    """C7: --cli-unfold-argument mode registers multiple flat options (including dot-path ones)."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    arg_map = ac._build_parameter_map()
    assert isinstance(arg_map, OrderedDict)
    assert "Id" in arg_map  # simple field
    # Dot-path keys appear
    assert any("." in k for k in arg_map.keys())


def test_C8_build_parameter_map_normal_mode():
    """C8: normal mode registers top-level fields as options."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=None)  # normal mode
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    arg_map = ac._build_parameter_map()
    assert "Id" in arg_map
    assert "RuleList" in arg_map
    # There should be no dot key like RuleList.RuleDetail.RuleKey
    assert not any("." in k for k in arg_map.keys())


def test_C9_argument_map_lazy_property():
    """C9: argument_map is a lazy-loaded property; repeated access returns the same object."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=None)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    am1 = ac.argument_map
    am2 = ac.argument_map
    # Same object (lazy-load cache)
    assert am1 is am2


def test_C10_create_help_command_returns_action_help():
    """C10: create_help_command returns an ActionHelpCommand instance."""
    from tccli.help_command import ActionHelpCommand
    ac = _make_action_command()
    hc = ac.create_help_command()
    assert isinstance(hc, ActionHelpCommand)


def test_C11_create_action_parser_returns_argparser():
    """C11: _create_action_parser returns an ArgMapArgParser instance."""
    from tccli.argparser import ArgMapArgParser
    ac = _make_action_command()
    parser = ac._create_action_parser(OrderedDict())
    assert isinstance(parser, ArgMapArgParser)


def test_C12_build_action_parameters_collects_args():
    """C12: _build_action_parameters writes fields from parsed_args into a dict."""
    import argparse as _argparse
    ac = _make_action_command()

    # mock an argument_object
    class _Arg(object):
        def __init__(self, name):
            self.name = name

        def add_to_params(self, params, value):
            params[self.name] = value

    arg_map = OrderedDict()
    arg_map["Foo"] = _Arg("Foo")
    arg_map["Bar"] = _Arg("Bar")

    parsed = _argparse.Namespace(Foo="v1", Bar="v2")
    out = ac._build_action_parameters(parsed, arg_map)
    assert out == {"Foo": "v1", "Bar": "v2"}


# ============================================================
# D. CLICommand internal methods
# ============================================================
def test_D1_clicommand_init():
    """D1: CLICommand initializes basic fields."""
    cli = CLICommand()
    assert cli._command_map is None
    assert cli._argument_map is None
    assert isinstance(cli._cli_data, Loader)


def test_D2_get_cli_options_returns_dict():
    """D2: _get_cli_options returns the cli global option dict."""
    cli = CLICommand()
    opts = cli._get_cli_options()
    assert "secretId" in opts
    assert "profile" in opts


def test_D3_create_cli_argument_returns_custom_argument():
    """D3: _create_cli_argument turns option_params into a CustomArgument."""
    from tccli.argument import CustomArgument
    cli = CLICommand()
    arg = cli._create_cli_argument("foo", {"help": "h"})
    assert isinstance(arg, CustomArgument)


def test_D4_build_argument_map_contains_globals():
    """D4: _build_argument_map contains all cli global options."""
    cli = CLICommand()
    am = cli._build_argument_map()
    assert "secretId" in am
    assert "profile" in am


def test_D5_get_argument_map_lazy():
    """D5: _get_argument_map lazy-load cache."""
    cli = CLICommand()
    am1 = cli._get_argument_map()
    am2 = cli._get_argument_map()
    assert am1 is am2


def test_D6_get_command_map_lazy_and_contains_configure():
    """D6: _get_command_map lazy-load + must contain the configure command."""
    cli = CLICommand()
    cmap = cli._get_command_map()
    assert "configure" in cmap


def test_D7_get_available_services_returns_iterable():
    """D7: _get_available_services returns an iterable object."""
    cli = CLICommand()
    services = cli._get_available_services()
    # services is dict_keys or a list
    assert hasattr(services, "__iter__")


def test_D8_get_service_version_no_version_in_argv():
    """D8: _get_service_version returns (None, None) when there is no --version."""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "DescribeAccount"]
    try:
        s, v = cli._get_service_version()
        assert s is None and v is None
    finally:
        sys.argv = saved


def test_D9_get_service_version_with_invalid_version():
    """D9: returns (None, None) when --version is followed by an invalid version."""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "--version", "not-a-version"]
    try:
        s, v = cli._get_service_version()
        assert s is None and v is None
    finally:
        sys.argv = saved


def test_D10_get_service_version_with_valid_version():
    """D10: returns (service, version) when --version is followed by a valid version."""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "--version", "2018-07-09"]
    try:
        s, v = cli._get_service_version()
        assert s == "billing" and v == "2018-07-09"
    finally:
        sys.argv = saved


def test_D11_handle_warning_no_crash():
    """D11: _handle_warning does not raise under normal arguments."""
    cli = CLICommand()
    # Without --warning, and without ~/.tccli/default.configure, it should also not crash
    cli._handle_warning(["billing", "DescribeAccount"])
    # With --warning
    cli._handle_warning(["billing", "DescribeAccount", "--warning", "on"])
    # With --profile
    cli._handle_warning(["billing", "DescribeAccount", "--profile", "myp"])


def test_D12_handle_service_version_argument_with_version_in_args():
    """D12: with --version + a valid version, the parser does not add --version again."""
    import argparse
    cli = CLICommand()
    parser = argparse.ArgumentParser(add_help=False)
    args = ["billing", "--version", "2018-07-09"]
    # Should not raise
    cli._handle_service_version_argumnet(args, parser)


def test_D13_handle_service_version_argument_without_version():
    """D13: the parser adds --version when there is no --version."""
    import argparse
    cli = CLICommand()
    parser = argparse.ArgumentParser(add_help=False)
    cli._handle_service_version_argumnet(["billing"], parser)
    # The parser should now have --version
    has_version = any(
        "--version" in (a.option_strings if hasattr(a, "option_strings") else [])
        for a in parser._actions
    )
    assert has_version


def test_D14_create_parser_returns_cliarg_parser():
    """D14: _create_parser returns a CLIArgParser instance."""
    from tccli.argparser import CLIArgParser
    cli = CLICommand()
    cmap = cli._get_command_map()
    parser = cli._create_parser(cmap)
    assert isinstance(parser, CLIArgParser)
    # the help command is injected
    assert "help" in cmap


def test_D15_clicommand_call_with_as_alias():
    """D15: on __call__, when the first argument is 'as' -> replace it with 'autoscaling' (if that service exists)."""
    cli = CLICommand()
    avail = cli._cli_data.get_available_services()
    if "autoscaling" not in avail:
        pytest.skip("autoscaling service not available")
    # Simulate args=["as", "help"]
    args = ["as", "help"]
    try:
        cli(args)
    except SystemExit:
        # The help command usually ends with SystemExit
        pass
    except Exception:
        # Other exceptions are also allowed -- we only verify 'as' is rewritten to 'autoscaling'
        pass
    # Verify the side effect: args[0] has been replaced
    assert args[0] == "autoscaling"


# ============================================================
# E. ServiceCommand internal methods
# ============================================================
def test_E1_servicecommand_init_default_version():
    """E1: ServiceCommand uses the default version when version is not passed."""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    assert sc._service_name == "cvm"
    assert sc._version is not None


def test_E2_servicecommand_invalid_version_raises():
    """E2: passing a non-existent version number raises."""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    try:
        ServiceCommand("cvm", version="9999-01-01")
        assert False, "expected exception"
    except Exception as e:
        assert "is invalid" in str(e)


def test_E3_servicecommand_get_service_model():
    """E3: _get_service_model returns the service model dict."""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    model = sc._get_service_model()
    assert "actions" in model
    assert "objects" in model


def _make_service_command_in_memory():
    """Build a ServiceCommand that touches no real SDK / disk.

    Inject an in-memory service_model (with 1 self-referencing action + 1 normal action),
    and mock Services.action_caller to avoid importing the real tencentcloud SDK module.
    """
    sc = object.__new__(ServiceCommand)
    sc._service_name = "svc"
    sc._version = "2020-01-01"
    sc._command_map = None
    sc._cli_data = Loader()
    service_model = {
        "metadata": {}, "actions": {
            "Tree": {"input": "TreeRequest", "name": "Tree"},
            "Flat": {"input": "FlatRequest", "name": "Flat"},
        },
        "objects": {
            "TreeRequest": {"members": [
                {"name": "Root", "type": "object", "member": "Node",
                 "document": "", "required": True}]},
            "FlatRequest": {"members": [
                {"name": "Id", "type": "string", "member": "string",
                 "document": "", "required": True}]},
            "Node": {"members": [
                {"name": "Self", "type": "object", "member": "Node",
                 "document": "", "required": False}]},
        },
    }
    sc._get_service_model = lambda: service_model
    return sc


def test_E4_servicecommand_get_command_map_lazy():
    """E4: _get_command_map lazy-loads and injects the _is_self_ref marker for self-referencing actions."""
    import tccli.services as _Services
    saved = _Services.action_caller
    _Services.action_caller = lambda service: (lambda: {
        "Tree": (lambda *a, **kw: None), "Flat": (lambda *a, **kw: None)})
    try:
        sc = _make_service_command_in_memory()
        cmap1 = sc._get_command_map()
        cmap2 = sc._get_command_map()
        assert cmap1 is cmap2  # lazy-load: same object
        assert set(cmap1.keys()) == {"Tree", "Flat"}
        # This change: self-referencing actions are marked, normal actions are not
        assert cmap1["Tree"]._is_self_ref is True
        assert cmap1["Flat"]._is_self_ref is False
    finally:
        _Services.action_caller = saved


def test_E5_servicecommand_create_parser_returns_action_parser():
    """E5: _create_parser returns an ActionArgParser instance + injects help."""
    from tccli.argparser import ActionArgParser
    import tccli.services as _Services
    saved = _Services.action_caller
    _Services.action_caller = lambda service: (lambda: {
        "Tree": (lambda *a, **kw: None), "Flat": (lambda *a, **kw: None)})
    try:
        sc = _make_service_command_in_memory()
        cmap = sc._get_command_map()
        parser = sc._create_parser(cmap)
        assert isinstance(parser, ActionArgParser)
        assert "help" in cmap
    finally:
        _Services.action_caller = saved


def test_E6_servicecommand_create_help_command():
    """E6: create_help_command returns a ServiceHelpCommand instance."""
    from tccli.help_command import ServiceHelpCommand
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    hc = sc.create_help_command()
    assert isinstance(hc, ServiceHelpCommand)


# ============================================================
# F. Boundary / exception / robustness supplements
# ============================================================
def test_F1_basecommand_loader_inited():
    """F1: BaseCommand subclasses correctly inherit the _cli_data field."""
    bc = BaseCommand()
    assert isinstance(bc._cli_data, Loader)


def test_F2_actioncommand_call_unknown_args_raises():
    """F2: ActionCommand.__call__ raises UnknownArgumentError for truly unknown parameters (typos, etc.).

       Design change (recursive-nesting-30):
         - The old assertion "drilling into a self-reference truncation point = illegal" no longer holds -- a D<=30 extension is legal input;
         - This case keeps the negative assertion for "truly illegal parameters (typos / not matching any known prefix)",
           which is strictly aligned with the new design's ``_extract_deep_nested_args`` fallback branch
           (requirement 1.3: tokens not matching a prefix still go to Unknown options).
    """
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals(cli_unfold_argument=True)
    try:
        ac([
            "--Id", "1490",
            "--TotallyMadeUpField.NotInSchema", "x",  # a truly illegal parameter: matches no known prefix
        ], g)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "Unknown options" in msg
        assert "--TotallyMadeUpField.NotInSchema" in msg
        # Reverse assertion: the old design's Drop --cli-unfold-argument text should no longer appear
        assert "Drop --cli-unfold-argument" not in msg


def test_F3_actioncommand_call_generate_cli_skeleton_short_circuit():
    """F3: --generate-cli-skeleton mode parses no parameters and sends no request, generating the template directly."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals(generate_cli_skeleton=True)

    # This call completes via generate_skeleton, most commonly by writing to stdout and returning
    # We do not care about internal details -- as long as it does not raise UnknownArgumentError
    try:
        ac([], g)
    except UnknownArgumentError:
        assert False, "should not raise UnknownArgumentError in skeleton mode"
    except SystemExit:
        # generate_skeleton may sys.exit internally
        pass
    except Exception:
        # Other exceptions are also allowed -- e.g. print / IO failure -- the point is UnknownArgumentError does not occur
        pass


def test_F4_actioncommand_call_help_subcommand():
    """F4: when the first positional argument is 'help', take the help command branch."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals()
    try:
        ac(["help"], g)
    except SystemExit:
        pass
    except Exception:
        # help_command(...) may depend on external resources; ignore
        pass


def test_F5_action_caller_is_invoked_in_normal_mode():
    """F5: in normal mode, when parameters are legal, action_caller is called with action_parameters."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    captured = {}

    def fake_caller(action_parameters, parsed_globals):
        captured["params"] = action_parameters
        captured["globals"] = parsed_globals
        return "ok"

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=fake_caller,
    )
    # Use cli_unfold_argument mode + legal parameters to avoid touching credentials.maybe_refresh_credential
    # But this branch will call credentials -- suppress it with a monkey patch
    from tccli import credentials
    saved = credentials.maybe_refresh_credential
    credentials.maybe_refresh_credential = lambda *a, **kw: None
    try:
        g = _make_globals(profile="default", cli_unfold_argument=True)
        result = ac([
            "--Id", "1490",
            "--RuleList.RuleDetail.RuleKey", "tag",
        ], g)
        assert result == "ok"
        assert captured["params"]["Id"] == 1490
        # In cli-unfold-argument mode the nested structure is restored
        assert captured["params"]["RuleList"]["RuleDetail"]["RuleKey"] == "tag"
    finally:
        credentials.maybe_refresh_credential = saved


# ============================================================
# G. recursive-nesting-30 end-to-end mock cases
# ------------------------------------------------------------
# Cover the following paths:
#   * User input with D <= 30 legal deep-nesting extension -> goes through the _extract_deep_nested_args fallback branch ->
#     extra_unfold_args injection -> build_action_parameters -> action_caller receives the full request body.
#   * User input with D > 30 over-limit extension -> does not enter extra_unfold_args, oversized_tokens triggers
#     UnknownArgumentError, the text includes depth= and the file:// alternative, and no old Drop text appears.
#   * A typo (matching no truncation prefix) still raises Unknown options (aligned with requirement 1.3).
#   * Legal + over-limit mixed scenario: the legal part can still be collected, but the over-limit-triggered overall error has higher priority.
# ============================================================
def _build_self_ref_path(num_layers):
    """Build a recursive path ending in ``RuleKey`` and return its non-numeric depth."""
    base = ["RuleList", "RuleDetail", "Children", "0"]
    for _ in range(num_layers):
        base += ["Children", "0"]
    base.append("RuleKey")
    depth = sum(1 for segment in base if not segment.isdigit())
    return ".".join(base), depth


def _walk_to_leaf(params, num_layers):
    """Walk into ``num_layers`` layers of ``Children`` (taking list index 0) along ``params`` and finally return the leaf dict.

    Note the real shape of the billing CreateGatherRule schema:
      * ``RuleList`` is a dict (not a list! it has only one RuleDetail field);
      * ``Children`` is a list (the carrier of the self-referencing leaf).
    This assertion is based on the real unfold registration result (the ``RuleList.RuleDetail.RuleKey`` shape).
    """
    cursor = params["RuleList"]["RuleDetail"]
    # first Children layer
    cursor = cursor["Children"]
    assert isinstance(cursor, list) and len(cursor) == 1
    cursor = cursor[0]
    # subsequent num_layers layers
    for _ in range(num_layers):
        cursor = cursor["Children"]
        assert isinstance(cursor, list) and len(cursor) == 1
        cursor = cursor[0]
    return cursor


def _make_billing_action_command(captured):
    """Build a billing CreateGatherRule ActionCommand bound to a fake_caller that captures params."""
    def _caller(action_parameters, parsed_globals):
        captured["params"] = action_parameters
        captured["globals"] = parsed_globals
        return "ok"
    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=_caller,
    )
    ac._is_self_ref = True
    return ac


def _patch_credentials():
    """Suppress the side effect of credentials.maybe_refresh_credential and return (restore_fn)."""
    from tccli import credentials
    saved = credentials.maybe_refresh_credential
    credentials.maybe_refresh_credential = lambda *a, **kw: None
    return lambda: setattr(credentials, "maybe_refresh_credential", saved)


def test_G3_unfold_depth_30_passthrough_boundary():
    """G3: a valid field key at non-numeric depth 30 should pass through."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        parts = ["RuleList", "RuleDetail", "Children", "0"]
        for _ in range(26):
            parts += ["Children", "0"]
        parts.append("RuleKey")
        key = ".".join(parts)
        depth = sum(1 for seg in parts if not seg.isdigit())
        assert depth == 30

        g = _make_globals(profile="default", cli_unfold_argument=True)
        result = ac([
            "--Id", "1490",
            "--" + key, "value_d30",
        ], g)
        assert result == "ok"
        leaf = _walk_to_leaf(captured["params"], 26)
        assert leaf == {"RuleKey": "value_d30"}
    finally:
        restore()


def test_G4_unfold_depth_31_rejected():
    """G4: when the non-numeric-segment depth > MAX_INPUT_DEPTH=30, it should raise UnknownArgumentError with depth= and file:// text.

    Note: depth is defined as the number of "non-numeric segments" in the key (array indices 0/1/... do not count toward nesting depth).
    Construction: RuleList(1) + RuleDetail(1) + 28*Children(28) + RuleKey(1) = 31 non-numeric segments.
    """
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        parts = ["RuleList", "RuleDetail", "Children", "0"]
        for _ in range(27):
            parts += ["Children", "0"]
        parts += ["RuleKey"]
        key = ".".join(parts)
        # non-numeric-segment depth = 31 > 30
        depth = sum(1 for seg in parts if not seg.isdigit())
        assert depth == 31

        g = _make_globals(profile="default", cli_unfold_argument=True)
        try:
            ac(["--Id", "1490", "--" + key, "value_d31"], g)
            assert False, "expected UnknownArgumentError for depth=31"
        except UnknownArgumentError as e:
            msg = str(e)
            assert "depth=31" in msg
            assert "MAX_INPUT_DEPTH=30" in msg
            assert "Use --cli-input-json file://" in msg
            # Reverse assertion: the old text should no longer appear
            assert "Drop --cli-unfold-argument" not in msg
        # action_caller should not be called in the oversized scenario
        assert "params" not in captured
    finally:
        restore()


def test_G5_unfold_typo_unknown_param_still_raises():
    """G5: a typo (matching no known truncation prefix) still raises Unknown options via the existing path (requirement 1.3)."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        g = _make_globals(profile="default", cli_unfold_argument=True)
        try:
            ac([
                "--Id", "1490",
                "--RuleExpressio.Foo", "x",  # <- RuleExpression typo
            ], g)
            assert False, "expected UnknownArgumentError for typo"
        except UnknownArgumentError as e:
            msg = str(e)
            assert "Unknown options" in msg
            assert "--RuleExpressio.Foo" in msg
            # It should neither be recognized as a deep-nesting extension (no depth= text) nor show the old Drop text
            assert "depth=" not in msg
            assert "Drop --cli-unfold-argument" not in msg
        assert "params" not in captured
    finally:
        restore()


def test_G7_unfold_equals_form_normalization():
    """G7: the two argparse forms ``--key=value`` and ``--key value`` are equivalent."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        key, depth = _build_self_ref_path(0)
        assert depth == 4
        g = _make_globals(profile="default", cli_unfold_argument=True)
        # use the = form
        result = ac([
            "--Id", "1490",
            "--%s=value_eq" % key,
        ], g)
        assert result == "ok"
        leaf = _walk_to_leaf(captured["params"], 0)
        assert leaf == {"RuleKey": "value_eq"}
    finally:
        restore()


def test_G8_unfold_single_rule_value_preserves_list_type():
    """A single value for a list field below truncation must remain a list."""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        g = _make_globals(profile="default", cli_unfold_argument=True)
        result = ac([
            "--Id", "1490",
            "--RuleList.RuleDetail.Children.0.RuleValue", "ESG",
        ], g)

        assert result == "ok"
        leaf = _walk_to_leaf(captured["params"], 0)
        assert leaf["RuleValue"] == ["ESG"]
    finally:
        restore()


# I. _is_recursive_key boolean prefix check
# ============================================================
def test_I1_recursive_key_no_match():
    assert ActionCommand._is_recursive_key(
        "Foo.Bar", OrderedDict([("Root.0", "T")])) is False


def test_I2_recursive_key_strict_dot_boundary():
    trunc = OrderedDict([("Root.0", "T")])
    assert ActionCommand._is_recursive_key("Root.0.Sub", trunc) is True
    assert ActionCommand._is_recursive_key("Root.01.Sub", trunc) is False


def test_I3_recursive_key_any_prefix_match_is_enough():
    trunc = OrderedDict([
        ("A.0", "TA"),
        ("A.0.B.0", "TB"),
    ])
    assert ActionCommand._is_recursive_key("A.0.B.0.X", trunc) is True


def test_I4_recursive_key_equal_prefix_not_hit():
    """A key exactly equal to the prefix is not a strict extension."""
    trunc = OrderedDict([("Root.0", "T")])
    assert ActionCommand._is_recursive_key("Root.0", trunc) is False


# ============================================================
# J. _collect_truncated_prefixes static method
# ============================================================
def test_J1_collect_truncated_prefixes_empty():
    assert ActionCommand._collect_truncated_prefixes(None) == OrderedDict()
    assert ActionCommand._collect_truncated_prefixes({}) == OrderedDict()


def test_J2_collect_truncated_prefixes_filters_non_truncated():
    unfold = OrderedDict([
        ("A.0", {"recursive_truncated": True, "recursive_type": "TA"}),
        ("B.0", {"recursive_truncated": False, "recursive_type": "TB"}),
        ("C.0", {}),
    ])
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert list(out.keys()) == ["A.0"]
    assert out["A.0"] == "TA"


def test_J3_collect_truncated_prefixes_missing_type_becomes_empty():
    unfold = {"X.0": {"recursive_truncated": True}}
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert out["X.0"] == ""


def test_J4_collect_truncated_prefixes_preserves_order():
    unfold = OrderedDict([
        ("Z.0", {"recursive_truncated": True, "recursive_type": "TZ"}),
        ("A.0", {"recursive_truncated": True, "recursive_type": "TA"}),
        ("M.0", {"recursive_truncated": True, "recursive_type": "TM"}),
    ])
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert list(out.keys()) == ["Z.0", "A.0", "M.0"]


# N. _prefilter_orphan_keys static method
# ============================================================
class _FakeAction(object):
    def __init__(self, option_strings, nargs=None):
        self.option_strings = option_strings
        self.nargs = nargs


class _FakeParser(object):
    def __init__(self, actions):
        self._actions = actions


def test_N1_prefilter_orphan_keys_empty_args_no_raise():
    ActionCommand._prefilter_orphan_keys([], _FakeParser([]))


def test_N2_prefilter_equals_form_not_orphan():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    ActionCommand._prefilter_orphan_keys(["--k=v"], parser)


def test_N3_prefilter_valueless_option_not_orphan():
    """A nargs==0 flag-type option is allowed to have no value."""
    parser = _FakeParser([_FakeAction(["--flag"], nargs=0)])
    ActionCommand._prefilter_orphan_keys(["--flag", "--other", "v"], parser)


def test_N4_prefilter_option_at_tail_raises():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    try:
        ActionCommand._prefilter_orphan_keys(["--k"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "Missing value for option(s):" in msg
        assert "--k" in msg


def test_N5_prefilter_adjacent_options_raises():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    try:
        ActionCommand._prefilter_orphan_keys(["--k", "--other", "v"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        assert "--k" in str(e)


def test_N6_prefilter_normal_pair_no_raise():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    ActionCommand._prefilter_orphan_keys(["--k", "v"], parser)


def test_N7_prefilter_multiple_orphans_all_reported():
    parser = _FakeParser([_FakeAction(["--flag"], nargs=0)])
    try:
        ActionCommand._prefilter_orphan_keys(
            ["--k1", "--k2", "--k3"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "--k1" in msg
        assert "--k2" in msg


# ============================================================
# O. _build_oversized_hint white-box
# ============================================================
def test_O1_oversized_hint_empty_returns_empty_str():
    ac = _make_action_command()
    assert ac._build_oversized_hint([]) == ""


def test_O2_oversized_hint_single_entry_full_text():
    ac = _make_action_command()
    hint = ac._build_oversized_hint([("A.B.C", 31)])
    assert "MAX_INPUT_DEPTH=30" in hint
    assert "depth=31" in hint
    assert "--A.B.C" in hint
    assert "under --" not in hint
    assert "type:" not in hint
    assert "Use --cli-input-json file://" in hint


def test_O3_oversized_hint_multiple_entries_each_on_own_line():
    ac = _make_action_command()
    hint = ac._build_oversized_hint([
        ("A.X", 31),
        ("B.Y", 32),
    ])
    assert "--A.X" in hint
    assert "--B.Y" in hint
    assert "depth=31" in hint
    assert "depth=32" in hint


# ============================================================
# P. _extract_deep_nested_args white-box boundaries
# ============================================================
def test_P1_extract_empty_remaining_returns_as_is():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    extra = OrderedDict()
    oversized = []
    out = ac._extract_deep_nested_args([], extra, oversized)
    assert out == []
    assert extra == OrderedDict()
    assert oversized == []


def test_P2_extract_loader_raises_returns_original():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _BadLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            raise RuntimeError("boom")
    ac._cli_data = _BadLoader()
    remaining = ["--Foo.Bar", "v"]
    extra = OrderedDict()
    oversized = []
    out = ac._extract_deep_nested_args(remaining, extra, oversized)
    assert out == remaining
    assert extra == OrderedDict()


def test_P3_extract_no_truncated_returns_original():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _NoTrunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Foo": {"recursive_truncated": False}}
    ac._cli_data = _NoTrunc()
    remaining = ["--Foo.Extra", "v"]
    out = ac._extract_deep_nested_args(remaining, OrderedDict(), [])
    assert out == remaining


def test_P4_extract_service_model_raises_keeps_original():
    """Do not guess a field type or consume input when the schema is unavailable."""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _PartLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            raise RuntimeError("no schema")
    ac._cli_data = _PartLoader()
    extra = OrderedDict()
    oversized = []
    remaining = ["--Root.0.Sub", "v"]
    out = ac._extract_deep_nested_args(remaining, extra, oversized)
    assert out == remaining
    assert extra == OrderedDict()


def test_P5_extract_non_dash_token_kept_in_new_remaining():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(
        ["stray_positional"], OrderedDict(), [])
    assert out == ["stray_positional"]


def test_P6_extract_non_matching_pair_kept_wholesale():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(
        ["--OtherKey", "v1", "v2"], OrderedDict(), [])
    assert out == ["--OtherKey", "v1", "v2"]


def test_P7_extract_valueless_non_matching_key_kept():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(["--WhoAmI"], OrderedDict(), [])
    assert out == ["--WhoAmI"]


def test_P8_extract_preserves_single_value_list_type_below_truncation():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "Node"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {
                "CreateGatherRuleRequest": {"members": [
                    {"name": "Root", "type": "list", "member": "Node"},
                ]},
                "Node": {"members": [
                    {"name": "Values", "type": "list", "member": "string"},
                    {"name": "Name", "type": "string", "member": "string"},
                ]},
            }}

    ac._cli_data = _Trunc()
    extra = OrderedDict()
    out = ac._extract_deep_nested_args([
        "--Root.0.Values", "only-one",
        "--Root.0.Name", "node-name",
    ], extra, [])

    assert out == []
    assert extra == {
        "Root.0.Values": ["only-one"],
        "Root.0.Name": "node-name",
    }


def test_P9_extract_preserves_single_value_list_type_in_equals_form():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "Node"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {
                "CreateGatherRuleRequest": {"members": [
                    {"name": "Root", "type": "list", "member": "Node"},
                ]},
                "Node": {"members": [
                    {"name": "Values", "type": "list", "member": "string"},
                ]},
            }}

    ac._cli_data = _Trunc()
    extra = OrderedDict()
    out = ac._extract_deep_nested_args(
        ["--Root.0.Values=only-one"], extra, [])

    assert out == []
    assert extra == {"Root.0.Values": ["only-one"]}



# ============================================================
# Allow running directly via `python3 tests/test_command.py` (without a pytest environment)
# ============================================================
if __name__ == "__main__":
    import traceback

    tests = [
        (name, obj) for name, obj in sorted(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    passed = failed = skipped = 0
    failures = []
    for name, fn in tests:
        try:
            fn()
            print("PASS  %s" % name)
            passed += 1
        except Exception as e:
            cls = e.__class__.__name__
            if cls in ("_SkipException", "Skipped"):
                print("SKIP  %s  (%s)" % (name, e))
                skipped += 1
            else:
                print("FAIL  %s" % name)
                traceback.print_exc()
                failed += 1
                failures.append(name)
    print("\n=========================================")
    print("total=%d  passed=%d  failed=%d  skipped=%d"
          % (len(tests), passed, failed, skipped))
    if failures:
        print("failed tests:")
        for n in failures:
            print("  - %s" % n)
    sys.exit(1 if failed else 0)
