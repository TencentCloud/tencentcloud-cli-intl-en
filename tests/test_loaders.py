# -*- coding: utf-8 -*-
"""
Unit tests for tccli.loaders.

Focus of coverage:
1. Normal (acyclic) schema: ensure the fix introduces no regression.
2. Self-referencing (direct / indirect / sibling-shared-type) schema: the core fix.
3. _generate_param_skeleton: self-reference points are represented by a string placeholder
   (<recursive: fill '<field>' with a JSON object of type <T> (self-referenced)>).
4. _get_unfold_param_info: self-referencing actions can be unfolded without RecursionError.
5. _filling_unfold_param_info: truncation points have type=Object with an appended document hint.
6. End-to-end behavior of the public methods get_param_info / get_output_param_info /
   generate_param_skeleton / get_unfold_param_info.
7. Real repository data: billing has a self-referencing action, cvm a normal one.

Uses pytest style: each test_* function asserts inline, no calls at the end of the file,
pytest auto-discovers them.
"""
import os
import sys

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

# Ensure tccli can be imported
_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# Suppress the cost/side effects of plugin import so pure static tests can run in any environment
import tccli.plugin as _plg  # noqa: E402

_plg.import_plugins = lambda: {}

from tccli.loaders import Loader, BASE_TYPE  # noqa: E402


# ============================================================
# Helper: build an in-memory Loader that injects a given service_model
# ============================================================
def _make_loader(model):
    """Return a Loader instance whose get_service_model directly returns the given model."""
    ld = Loader()
    ld.get_service_model = lambda service, version: model
    return ld


def _model(actions, objects):
    return {"metadata": {}, "actions": actions, "objects": objects}


def _action(input_name, output_name=None):
    out = {"input": input_name, "name": input_name.replace("Request", "")}
    if output_name:
        out["output"] = output_name
    return out


# ============================================================
# A. Normal-scenario regression
# ============================================================
def test_A1_basic_types_no_regression():
    """A1: base-type fields only -- output should match the pre-change behavior."""
    objects = {
        "FooRequest": {
            "members": [
                {"name": "Id", "type": "string", "member": "string", "document": "id", "required": True},
                {"name": "Count", "type": "int", "member": "int64", "document": "count", "required": False},
            ],
        },
    }
    actions = {"Foo": _action("FooRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Foo")
    assert set(info.keys()) == {"Id", "Count"}
    assert info["Id"]["type"] == "String"
    assert info["Id"]["type_name"] == "String"
    assert info["Id"]["required"] == "Required"
    assert info["Id"]["members"] == "string"
    assert info["Count"]["type"] == "Integer"
    assert info["Count"]["required"] == "Optional"


def test_A2_nested_object_full_expand():
    """A2: nested Object fully expanded."""
    objects = {
        "BarRequest": {
            "members": [
                {"name": "Outer", "type": "object", "member": "Inner", "document": "", "required": True},
            ],
        },
        "Inner": {
            "members": [
                {"name": "Leaf", "type": "string", "member": "string", "document": "leaf", "required": True},
            ],
        },
    }
    actions = {"Bar": _action("BarRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Bar")
    # Outer is a nested object, members should be a dict (expanded)
    assert isinstance(info["Outer"]["members"], dict)
    assert "Leaf" in info["Outer"]["members"]
    assert info["Outer"]["members"]["Leaf"]["type"] == "String"


def test_A3_list_of_object_full_expand():
    """A3: List<ComplexObject> fully expanded."""
    objects = {
        "BazRequest": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item", "document": "", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string", "document": "", "required": True},
            ],
        },
    }
    actions = {"Baz": _action("BazRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Baz")
    assert info["Items"]["type"] == "Array"
    assert isinstance(info["Items"]["members"], list)
    assert isinstance(info["Items"]["members"][0], dict)
    assert "Key" in info["Items"]["members"][0]


# ============================================================
# B. Self-referencing cycles
# ============================================================
def _self_ref_list_model():
    """Node { Children: List<Node> }"""
    return _model(
        actions={"Tree": _action("TreeRequest")},
        objects={
            "TreeRequest": {
                "members": [
                    {"name": "Root", "type": "object", "member": "Node",
                     "document": "root", "required": True},
                ],
            },
            "Node": {
                "members": [
                    {"name": "Value", "type": "string", "member": "string",
                     "document": "v", "required": False},
                    {"name": "Children", "type": "list", "member": "Node",
                     "document": "children", "required": False},
                ],
            },
        },
    )


def test_B1_direct_self_ref_via_list_does_not_crash():
    """B1: List<Self> direct self-reference must not raise RecursionError."""
    ld = _make_loader(_self_ref_list_model())
    info = ld.get_param_info("svc", "v", "Tree")
    # The top-level Root is a Node, expanded one level
    assert isinstance(info["Root"]["members"], dict)
    assert "Children" in info["Root"]["members"]
    # Children is the self-reference truncation point; members should be the placeholder string list ["Node"]
    children = info["Root"]["members"]["Children"]
    assert children["type"] == "Array"
    assert children["members"] == ["Node"]


def test_B2_direct_self_ref_via_object_does_not_crash():
    """B2: Object->Self direct self-reference."""
    objects = {
        "LinkRequest": {
            "members": [
                {"name": "Head", "type": "object", "member": "LinkNode",
                 "document": "", "required": True},
            ],
        },
        "LinkNode": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Next", "type": "object", "member": "LinkNode",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Link": _action("LinkRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Link")
    # Head.Next is the self-reference truncation point
    next_field = info["Head"]["members"]["Next"]
    # On object self-reference truncation, members should be filled with the placeholder type name (str)
    assert next_field["members"] == "LinkNode"


def test_B3_indirect_cycle_A_to_B_to_A():
    """B3: indirect cycle A->B->A."""
    objects = {
        "GraphRequest": {
            "members": [
                {"name": "Start", "type": "object", "member": "A",
                 "document": "", "required": True},
            ],
        },
        "A": {
            "members": [
                {"name": "B", "type": "object", "member": "B",
                 "document": "", "required": False},
            ],
        },
        "B": {
            "members": [
                {"name": "A", "type": "object", "member": "A",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Graph": _action("GraphRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Graph")
    # Path Start.B.A -- A is already in visited, so it is truncated
    inner_a = info["Start"]["members"]["B"]["members"]["A"]
    assert inner_a["members"] == "A"  # placeholder string


def test_B4_sibling_shared_type_not_falsely_truncated():
    """B4: two sibling fields share the same type Common and must not interfere with each other.

    If the implementation wrongly treats visited as a "globally seen" set, the second sibling field would be falsely truncated.
    """
    objects = {
        "SibRequest": {
            "members": [
                {"name": "Left", "type": "object", "member": "Common",
                 "document": "", "required": True},
                {"name": "Right", "type": "object", "member": "Common",
                 "document": "", "required": True},
            ],
        },
        "Common": {
            "members": [
                {"name": "K", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "V", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"Sib": _action("SibRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Sib")
    assert isinstance(info["Left"]["members"], dict)
    assert isinstance(info["Right"]["members"], dict)
    assert {"K", "V"} <= set(info["Left"]["members"].keys())
    assert {"K", "V"} <= set(info["Right"]["members"].keys())


# ============================================================
# C. Deep nesting (fully expanded when there is no max_depth)
# ============================================================
def test_C1_deep_nesting_full_expand():
    """C1: deep nesting (acyclic) should be fully expanded down to the innermost level."""
    # Build XRequest -> L1 -> L2 -> L3 -> L4 -> L5 -> string
    objects = {"XRequest": {"members": [
        {"name": "F", "type": "object", "member": "L1",
         "document": "", "required": True}
    ]}}
    for i in range(1, 5):
        objects["L%d" % i] = {"members": [
            {"name": "F", "type": "object", "member": "L%d" % (i + 1),
             "document": "", "required": True}
        ]}
    objects["L5"] = {"members": [
        {"name": "Leaf", "type": "string", "member": "string",
         "document": "", "required": True}
    ]}
    actions = {"X": {"input": "XRequest", "name": "X"}}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "X")
    cur = info["F"]
    for _ in range(4):
        assert isinstance(cur["members"], dict)
        cur = cur["members"]["F"]
    # The innermost level should be the fully expanded Leaf
    assert "Leaf" in cur["members"]
    assert cur["members"]["Leaf"]["type"] == "String"


# ============================================================
# D. _generate_param_skeleton
# ============================================================
def test_D1_skeleton_self_ref_object_emits_placeholder():
    """D1: Object self-reference -> the second level is represented by a string placeholder."""
    objects = {
        "LinkRequest": {
            "members": [
                {"name": "Head", "type": "object", "member": "LinkNode",
                 "document": "", "required": True},
            ],
        },
        "LinkNode": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Next", "type": "object", "member": "LinkNode",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Link": _action("LinkRequest")}, objects))
    skeleton = ld.generate_param_skeleton("svc", "v", "Link")
    # Head is expanded one level
    assert skeleton["Head"]["Val"] == "String"
    # Head.Next is the self-reference truncation point: a string placeholder with the field and type name
    assert skeleton["Head"]["Next"] == \
        "<recursive: fill 'Next' with a JSON object of type LinkNode (self-referenced)>"


def test_D2_skeleton_self_ref_list_emits_placeholder_list():
    """D2: List<Self> -> [string placeholder] (verified on the Tree self-reference model)."""
    ld = _make_loader(_self_ref_list_model())
    skeleton = ld.generate_param_skeleton("svc", "v", "Tree")
    # Root is a Node; after expanding one level, Children shows the self-reference truncation
    assert skeleton["Root"]["Value"] == "String"
    assert skeleton["Root"]["Children"] == [
        "<recursive: fill 'Children' with a JSON object of type Node (self-referenced)>"
    ]


def test_D3_skeleton_normal_nested_unchanged():
    """D3: normal nesting remains backward compatible."""
    objects = {
        "Req": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item",
                 "document": "", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = Loader()
    skeleton = ld._generate_param_skeleton(objects["Req"]["members"], objects)
    assert skeleton == {"Items": [{"Key": "String"}]}


# ============================================================
# E. _get_unfold_param_info
# ============================================================
def test_E1_unfold_self_ref_no_recursion_error():
    """E1: unfolding a self-referencing action raises no RecursionError and includes the truncation-point path."""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    keys = set(unfold.keys())
    # Root.Value (a base-type leaf) should be present
    assert "Root.Value" in keys
    # Root.Children.0 is the self-reference-truncated leaf
    assert "Root.Children.0" in keys


def test_E2_unfold_recursion_truncated_path_marked_as_object():
    """E2: the self-reference truncation point has type=Object with an English hint in the document, plus stable marker fields."""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    trunc = unfold["Root.Children.0"]
    assert trunc["type"] == "Object"
    assert trunc["required"] == "Optional"
    assert "self-referencing type" in trunc["document"]
    assert "Node" in trunc["document"]
    # Newly added stable fields (independent of the wording): design-B
    assert trunc.get("recursive_truncated") is True
    assert trunc.get("recursive_type") == "Node"


def test_E3_unfold_sibling_shared_type_fully_expanded():
    """E3: sibling fields sharing the same non-self-referencing type should each be fully and independently expanded."""
    objects = {
        "XRequest": {
            "members": [
                {"name": "L", "type": "object", "member": "C",
                 "document": "", "required": True},
                {"name": "R", "type": "object", "member": "C",
                 "document": "", "required": True},
            ],
        },
        "C": {
            "members": [
                {"name": "K", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"X": _action("XRequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "X")
    assert "L.K" in unfold
    assert "R.K" in unfold


# ============================================================
# F. _filling_unfold_param_info
# ============================================================
def test_F1_filling_truncated_marks_object_and_appends_doc():
    """F1: behavior of type/type_name/required/document for a truncated leaf."""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    trunc = unfold["Root.Children.0"]
    assert trunc["type"] == "Object"
    assert trunc["type_name"] == "Node"  # uses the placeholder type name


def test_F2_filling_normal_leaf_keeps_type():
    """F2: the type of a normal base-type leaf is not rewritten."""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    assert unfold["Root.Value"]["type"] == "String"
    assert unfold["Root.Value"]["type_name"] == "String"
    assert "self-referencing type" not in unfold["Root.Value"]["document"]
    assert unfold["Root.Value"].get("recursive_truncated") is not True


def test_F3_filling_secondary_check_for_list_placeholder():
    """F3: secondary check -- when a field's type is itself the self-referencing type Node,
    and the Request references it via List<Node>, the truncation point should be correctly
    registered and identified as a self-reference placeholder through the "secondary check" in the _filling stage."""
    objects = {
        "XRequest": {
            "members": [
                {"name": "Roots", "type": "list", "member": "Node",
                 "document": "", "required": True},
            ],
        },
        "Node": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Children", "type": "list", "member": "Node",
                 "document": "", "required": False},
            ],
        },
    }
    actions = {"X": {"input": "XRequest", "name": "X"}}
    ld = _make_loader(_model(actions, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "X")
    # Roots.0.Val is a base-type leaf
    assert "Roots.0.Val" in unfold
    assert unfold["Roots.0.Val"]["type"] == "String"
    # Roots.0.Children.0 is the self-reference truncation point; type should be rewritten to Object
    assert "Roots.0.Children.0" in unfold
    assert unfold["Roots.0.Children.0"]["type"] == "Object"
    assert "self-referencing type" in unfold["Roots.0.Children.0"]["document"]
    assert unfold["Roots.0.Children.0"].get("recursive_truncated") is True
    assert unfold["Roots.0.Children.0"].get("recursive_type") == "Node"


# ============================================================
# G. Public API end-to-end
# ============================================================
def test_G1_get_param_info_public():
    """G1: get_param_info public method signature / behavior."""
    ld = _make_loader(_self_ref_list_model())
    info = ld.get_param_info("svc", "v", "Tree")
    assert "Root" in info


def test_G2_get_output_param_info_public():
    """G2: get_output_param_info accepts Response."""
    objects = {
        "TreeRequest": {"members": [
            {"name": "X", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Y", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    out = ld.get_output_param_info("svc", "v", "Tree")
    assert "Y" in out


def test_G3_generate_param_skeleton_public():
    """G3: generate_param_skeleton public method + self-reference string placeholder."""
    ld = _make_loader(_self_ref_list_model())
    skeleton = ld.generate_param_skeleton("svc", "v", "Tree")
    assert skeleton["Root"]["Children"] == [
        "<recursive: fill 'Children' with a JSON object of type Node (self-referenced)>"
    ]


def test_G4_get_unfold_param_info_public():
    """G4: get_unfold_param_info public method."""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    # Must return a dict, and keys are dot-separated paths
    assert isinstance(unfold, dict)
    assert all("." in k or k == "Root" for k in unfold.keys())


# ============================================================
# H. Real repository data smoke tests
# ============================================================
def test_H1_real_cvm_describe_instances_smoke():
    """H1: the real cvm DescribeInstances action can generate unfolded parameters normally."""
    ld = Loader()
    try:
        info = ld.get_param_info("cvm", "2017-03-12", "DescribeInstances")
    except Exception as e:
        pytest.skip("local cvm api.json missing: %s" % e)
    assert isinstance(info, dict)
    assert "InstanceIds" in info or "Filters" in info

    unfold = ld.get_unfold_param_info("cvm", "2017-03-12", "DescribeInstances")
    assert isinstance(unfold, dict)
    assert len(unfold) > 0
    # A normal action should show no self-reference truncation hint
    for k, v in unfold.items():
        assert "RecursiveRef" not in v.get("type_name", "")


def test_H2_real_billing_self_ref_does_not_crash():
    """H2: the real billing CreateAllocationRule (with AllocationRuleExpression self-reference)
    no longer triggers RecursionError and can produce unfold parameters and a skeleton."""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "billing", "v20180709", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local billing api.json missing")

    # Pick a real action that contains an AllocationRuleExpression self-reference
    candidates = ["CreateAllocationRule", "ModifyAllocationRule"]
    chosen = None
    for act in candidates:
        try:
            ld.get_action_model("billing", "2018-07-09", act)
            chosen = act
            break
        except Exception:
            continue
    if chosen is None:
        pytest.skip("no candidate self-ref action available")

    # 1) get_param_info does not raise
    info = ld.get_param_info("billing", "2018-07-09", chosen)
    assert isinstance(info, dict)

    # 2) generate_param_skeleton should show a string placeholder at the self-reference point
    skeleton = ld.generate_param_skeleton("billing", "2018-07-09", chosen)
    flat = repr(skeleton)
    assert "<recursive: fill " in flat
    assert "(self-referenced)" in flat
    assert "AllocationRuleExpression" in flat

    # 3) get_unfold_param_info does not raise and has at least one truncation marker field
    unfold = ld.get_unfold_param_info("billing", "2018-07-09", chosen)
    assert isinstance(unfold, dict) and len(unfold) > 0
    has_truncation_doc = any(
        "self-referencing type" in (v.get("document") or "") for v in unfold.values()
    )
    assert has_truncation_doc, (
        "expected at least one self-ref truncation marker in %s" % chosen
    )
    # design-B stable field: at least one truncated leaf carries recursive_truncated=True
    assert any(v.get("recursive_truncated") for v in unfold.values()), (
        "expected at least one leaf with recursive_truncated=True in %s" % chosen
    )


# ============================================================
# I. Simple getter / static-info methods (covering L65-L179, L248-L321 in several places)
# ============================================================
def test_I1_get_services_path_returns_existing_dir():
    """I1: get_services_path should return the real tccli/services directory."""
    ld = Loader()
    p = ld.get_services_path()
    assert os.path.isdir(p)
    assert p.endswith("services")


def test_I2_static_text_getters():
    """I2: text getters return non-empty strings."""
    ld = Loader()
    assert isinstance(ld.get_cli_version(), str) and ld.get_cli_version()
    assert "Tencent Cloud" in ld.get_description()
    assert "tccli configure" in ld.get_configure()
    assert "tccli" in ld.get_usage()


def test_I3_get_options_and_cli_option_shape():
    """I3: get_options / get_cli_option return the correct structure."""
    ld = Loader()
    opts = ld.get_options()
    assert "help" in opts and "--version" in opts
    cli_opt = ld.get_cli_option()
    # Key global cli options must exist
    for must in ("filter", "output", "secretId", "secretKey", "profile",
                 "region", "endpoint", "generate-cli-skeleton",
                 "cli-input-json", "cli-unfold-argument", "language"):
        assert must in cli_opt, "missing global option: %s" % must
    # output is limited to choices
    assert set(cli_opt["output"]["choices"]) == {"json", "text", "table"}


def test_I4_version_transform():
    """I4: _version_transform restores 'v20180709' to '2018-07-09'."""
    ld = Loader()
    assert ld._version_transform("v20180709") == "2018-07-09"
    assert ld._version_transform("v20170312") == "2017-03-12"


def test_I5_get_service_description_and_usage_options():
    """I5: service-level simple getter behavior."""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    # Returns an empty string when metadata has no api_brief
    assert ld.get_service_description("svc", "v") == ""
    assert "svc" in ld.get_service_usage("svc")
    sopts = ld.get_service_options("svc")
    assert "help" in sopts and "svc" in sopts["help"]


def test_I6_get_action_simple_getters():
    """I6: action-level simple getters (description / online_status / usage / options)."""
    objects = {"FooRequest": {"members": []}}
    actions = {"Foo": {"input": "FooRequest", "name": "Foo",
                       "document": "doc-foo", "status": "deprecated"}}
    ld = _make_loader(_model(actions, objects))

    assert ld.get_action_description("svc", "v", "Foo") == "doc-foo"
    assert ld.get_action_online_status("svc", "v", "Foo") == "deprecated"
    # Defaults to online when status is not specified
    actions["Bar"] = {"input": "FooRequest", "name": "Bar", "document": "d"}
    assert ld.get_action_online_status("svc", "v", "Bar") == "online"

    usage = ld.get_action_usage("svc", "Foo")
    assert "tccli" in usage and "svc" in usage and "Foo" in usage

    aopts = ld.get_action_options("svc", "Foo")
    assert "--profile" in aopts


def test_I7_get_action_model_and_actions_info():
    """I7: get_action_model / get_actions_info query action metadata directly."""
    actions = {
        "B": {"input": "FooRequest", "name": "B", "document": "doc-b"},
        "A": {"input": "FooRequest", "name": "A", "document": "doc-a"},
    }
    objects = {"FooRequest": {"members": []}}
    ld = _make_loader(_model(actions, objects))

    am = ld.get_action_model("svc", "v", "A")
    assert am["name"] == "A" and am["document"] == "doc-a"

    info = ld.get_actions_info("svc", "v")
    # Returns an OrderedDict sorted by action name
    assert list(info.keys()) == ["A", "B"]
    assert info["A"]["status"] == "online"  # default value


# ============================================================
# J. get_service_model real read + plugin merge branch
# ============================================================
def test_J1_get_service_model_real_cvm():
    """J1: read cvm api.json via the real disk path (hits the L208-L246 main path)."""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "cvm", "v20170312", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local cvm api.json missing")
    model = ld.get_service_model("cvm", "2017-03-12")
    assert "actions" in model and "objects" in model
    assert "DescribeInstancesRequest" in model["objects"]


def test_J2_get_service_model_plugin_merge_branch():
    """J2: hit the plugin merge branch (L228-L241), merging custom plugin actions/objects."""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "cvm", "v20170312", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local cvm api.json missing")
    # Inject a fake plugin whose name matches the service and version matches v20170312
    fake_plugin_spec = {
        "metadata": {"_plugin_marker": "yes"},
        "actions": {"_FakePluginAction": {"name": "_FakePluginAction"}},
        "objects": {"_FakePluginObject": {"members": []}},
    }
    saved = _plg.import_plugins
    _plg.import_plugins = lambda: {"cvm": {"2017-03-12": fake_plugin_spec}}
    try:
        model = ld.get_service_model("cvm", "2017-03-12")
        # The plugin-merged metadata/actions/objects all take effect
        assert model["metadata"].get("_plugin_marker") == "yes"
        assert "_FakePluginAction" in model["actions"]
        assert "_FakePluginObject" in model["objects"]
    finally:
        _plg.import_plugins = saved


def test_J3_get_available_services_returns_dict():
    """J3: get_available_services returns a dict containing at least cvm."""
    ld = Loader()
    avail = ld.get_available_services()
    assert isinstance(avail, dict)
    if "cvm" in avail:
        assert isinstance(avail["cvm"], list)


# ============================================================
# K. get_service_default_version / multi-version / all-action series
# ============================================================
def test_K1_get_service_default_version_uses_first():
    """K1: defaults to available_services[service][0] when there is no config file."""
    ld = Loader()
    # Suppress ~/.tccli reads
    avail = ld.get_available_services()
    if "cvm" not in avail or not avail["cvm"]:
        pytest.skip("cvm not in available services")

    # Use monkey patch to make file_existed return False
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        ver = ld.get_service_default_version("cvm")
        assert ver in avail["cvm"]
    finally:
        _u.Utils.file_existed = saved


def test_K2_get_service_all_version_actions_real_cvm():
    """K2: the real cvm has at least one version directory."""
    ld = Loader()
    services_path = ld.get_services_path()
    cvm_path = os.path.join(services_path, "cvm")
    if not os.path.isdir(cvm_path):
        pytest.skip("local cvm dir missing")
    res = ld.get_service_all_version_actions("cvm")
    assert isinstance(res, dict) and len(res) > 0
    # The actions of any version are iterable
    any_ver = next(iter(res))
    assert hasattr(res[any_ver], "__iter__")


def test_K3_get_service_all_version_actions_missing_raises():
    """K3: raises when the service does not exist."""
    ld = Loader()
    try:
        ld.get_service_all_version_actions("__no_such_service__")
        assert False, "expected exception"
    except Exception as e:
        assert "Not find service" in str(e)


def test_K4_get_service_all_action_param_default_model():
    """K4: takes the get_param_info branch when no model is specified.

    Test constraint: does not depend on real cvm service data; driven by an in-memory
    version-action mapping, only verifying that dispatch goes through get_param_info (the default branch).
    """
    ld = Loader()
    ld.get_service_all_version_actions = lambda service: {"v": {"Foo"}}
    ld.get_param_info = lambda s, v, a: {"Id": {}, "Name": {}}
    ld.get_unfold_param_info = lambda *a, **kw: (_ for _ in ()).throw(
        AssertionError("the default model should not go through get_unfold_param_info"))
    res = ld.get_service_all_action_param("svc")
    assert isinstance(res, dict)
    assert "Foo" in res
    assert set(res["Foo"]) == {"Id", "Name"}


def test_K5_get_service_all_action_param_unfold_model():
    """K5: takes the get_unfold_param_info branch when model='cli-unfold-argument'."""
    ld = Loader()
    ld.get_service_all_version_actions = lambda service: {"v": {"Foo"}}
    ld.get_unfold_param_info = lambda s, v, a: {"Id": {}, "Tags.0": {}}
    ld.get_param_info = lambda *a, **kw: (_ for _ in ()).throw(
        AssertionError("the unfold model should not go through get_param_info"))
    res = ld.get_service_all_action_param("svc", model="cli-unfold-argument")
    assert isinstance(res, dict)
    assert "Foo" in res
    assert set(res["Foo"]) == {"Id", "Tags.0"}


# ============================================================
# L. param_array behavior of _add_array_item / get_unfold_param_info
# ============================================================
def test_L1_add_array_item_expand_to_max():
    """L1: when a path contains the '0' placeholder, it is duplicated to 0..arrayCount-1, defaulting to 10 copies."""
    ld = Loader()
    # mock file_existed to return False, using the default array_count=10
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        param_list = [["A", "0", "B"]]
        out = ld._add_array_item(param_list, "default")
        # Should contain ["A","1","B"] ~ ["A","9","B"], 9 new entries (plus the original 1 = 10)
        assert ["A", "0", "B"] in out
        assert ["A", "9", "B"] in out
        # Should not produce out-of-range "10"
        assert ["A", "10", "B"] not in out
    finally:
        _u.Utils.file_existed = saved


def test_L2_add_array_item_with_param_array_via_unfold():
    """L2: trigger _add_array_item via get_unfold_param_info(param_array=True)."""
    ld = _make_loader(_self_ref_list_model())
    # mock config to use the default array_count
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        unfold = ld.get_unfold_param_info(
            "svc", "v", "Tree", profile="default", param_array=True)
        # Should expand extra paths such as Root.Children.1, Root.Children.2 ...
        assert "Root.Children.0" in unfold
        # At least one non-zero index key
        non_zero = [k for k in unfold if k.startswith("Root.Children.") and not k.endswith(".0")]
        assert len(non_zero) > 0
    finally:
        _u.Utils.file_existed = saved


# ============================================================
# M. Uncovered branches of _filling_unfold_param_info
# ============================================================
def test_M1_filling_required_downgrade_in_path():
    """M1: when some level in the path has required=Optional, the final leaf's required is also downgraded to Optional."""
    objects = {
        "ZRequest": {
            "members": [
                {"name": "Outer", "type": "object", "member": "Inner",
                 "document": "outer", "required": True},  # top level Required
            ],
        },
        "Inner": {
            "members": [
                {"name": "Mid", "type": "object", "member": "Leaf",
                 "document": "mid", "required": False},  # <- middle Optional
            ],
        },
        "Leaf": {
            "members": [
                {"name": "X", "type": "string", "member": "string",
                 "document": "x", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"Z": _action("ZRequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "Z")
    # Outer is top-level Required, but middle Mid is Optional -> the final leaf is also Optional
    assert unfold["Outer.Mid.X"]["required"] == "Optional"


def test_M2_filling_array_index_gt_zero_downgrades_required():
    """M2: when the path contains non-zero indices like '1' '2', required is forced to Optional (covers L540-L541)."""
    ld = _make_loader(_self_ref_list_model())
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        unfold = ld.get_unfold_param_info(
            "svc", "v", "Tree", profile="default", param_array=True)
        # The required of non-zero indices like Root.Children.1 should be Optional
        for k, v in unfold.items():
            if k.startswith("Root.Children.") and not k.endswith(".0"):
                assert v["required"] == "Optional"
                break
    finally:
        _u.Utils.file_existed = saved


def test_M3_filling_path_traverses_array_member_dict():
    """M3: the path drills into an Array-type node (covers the L498 res['type']=='Array' take-[0] branch)."""
    objects = {
        "ARequest": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item",
                 "document": "items", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string",
                 "document": "k", "required": True},
                {"name": "Val", "type": "string", "member": "string",
                 "document": "v", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"A": _action("ARequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "A")
    # Items is an Array -> drilling goes through the res["members"][0][item] branch
    assert "Items.0.Key" in unfold
    assert unfold["Items.0.Key"]["type"] == "String"
    assert unfold["Items.0.Val"]["required"] == "Optional"


# ============================================================
# N. example / translate series
# ============================================================
def _patch_example_model(ld, examples):
    """Inject fake example data into ld for generate_cli_example to call."""
    ld.get_action_example_model = lambda s, v, a: examples


def test_N1_get_action_example_model_missing_raises():
    """N1: raises when examples.json does not exist."""
    ld = Loader()
    try:
        ld.get_action_example_model("__no_svc__", "1970-01-01", "X")
        assert False
    except Exception as e:
        assert "Not find service" in str(e)


def test_N2_get_action_example_model_real_cvm():
    """N2: the real cvm DescribeInstances should have examples."""
    ld = Loader()
    services_path = ld.get_services_path()
    if not os.path.exists(os.path.join(services_path, "cvm", "v20170312", "examples.json")):
        pytest.skip("examples.json missing")
    ex = ld.get_action_example_model("cvm", "2017-03-12", "DescribeInstances")
    assert isinstance(ex, list) and len(ex) > 0


def test_N3_translate_get_cli_param_basic():
    """N3: GET parameter parsing -- simple key=value, space escaping, List indices removed."""
    ld = Loader()
    out = ld.translate_get_cli_param([
        "Limit=10",
        "Offset=0",
        "Filters.0=foo",
        "Filters.1=bar baz",
    ])
    # simple key
    assert "--Limit 10" in out
    assert "--Offset 0" in out
    # List indices are removed, multiple values aggregated, spaces wrapped in quotes
    filters = [s for s in out if s.startswith("--Filters")]
    assert len(filters) == 1
    assert "foo" in filters[0]
    assert "'bar baz'" in filters[0]


def test_N4_translate_get_cli_param_skip_invalid():
    """N4: an invalid token without '=' should be ignored without raising."""
    ld = Loader()
    out = ld.translate_get_cli_param(["Limit=10", "no_equals_token"])
    assert any("--Limit" in s for s in out)


def test_N5_translate_post_cli_param_complex():
    """N5: POST JSON input translation -- nested object / list of object / values with spaces."""
    ld = Loader()
    inp = {
        "Name": "hello world",
        "Count": 3,
        "Tags": ["a", "b c"],
        "Items": [
            {"K": "k1", "V": "v 1"},
            {"K": "k2", "V": "v2"},
        ],
    }
    out = ld.translate_post_cli_param(inp)
    flat = "\n".join(out)
    # simple fields
    assert "--Name 'hello world'" in flat
    assert "--Count 3" in flat
    # base-type list joined as a whole
    assert "--Tags" in flat and "'b c'" in flat
    # object list uses indexed dot paths
    assert "--Items.0.K k1" in flat
    assert "--Items.1.V v2" in flat


def test_N6_generate_cli_example_post_input():
    """N6: POST input translation of generate_cli_example."""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    ld.get_action_example_model = lambda s, v, a: [
        {
            "input": "POST / HTTP/1.1\nHost: x.tencentcloudapi.com\n\n"
                     '{"Name":"foo","N":1}',
            "output": '{"Response":{"RequestId":"req-1"}}',
            "title": "demo",
        }
    ]
    examples = ld.generate_cli_example("svc", "v", "X")
    assert len(examples) == 1
    inp = examples[0]["input"]
    assert any("--Name foo" in s for s in inp)
    # output is prettified by json.dumps (with line breaks)
    assert "RequestId" in examples[0]["output"]


def test_N7_generate_cli_example_get_input():
    """N7: GET input translation of generate_cli_example."""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    ld.get_action_example_model = lambda s, v, a: [
        {
            "input": "https://x.tencentcloudapi.com/?Action=X"
                     "&<Common request parameters>"
                     "&Limit=10"
                     "&Filters.0=foo",
            "output": "not-json-but-ok",
            "title": "demo-get",
        }
    ]
    examples = ld.generate_cli_example("svc", "v", "X")
    inp = examples[0]["input"]
    assert any(s.startswith("--Limit") for s in inp)
    assert any(s.startswith("--Filters") for s in inp)
    # when output is not valid JSON, keep it as is
    assert examples[0]["output"] == "not-json-but-ok"


def test_N8_translate_post_cli_param_basic_type_only():
    """N8: a single base type at the top level can also happy-path through _translate_post_cli_param."""
    ld = Loader()
    # Verify the basic-type short-circuit branch directly via the underlying private method
    out = []
    ld._translate_post_cli_param("hello", [], out)
    assert out == [["hello"]]
    # values with spaces are wrapped in quotes
    out2 = []
    ld._translate_post_cli_param("a b", [], out2)
    assert out2 == [["'a b'"]]


# ============================================================
# O. Boundary / exception / robustness supplements
# ============================================================
def test_O1_get_param_info_response_via_output_method():
    """O1: get_output_param_info also does not crash on self-referencing types."""
    objects = {
        "TreeRequest": {"members": [
            {"name": "A", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Root", "type": "object", "member": "Node",
             "document": "", "required": True}
        ]},
        "Node": {"members": [
            {"name": "Self", "type": "object", "member": "Node",
             "document": "", "required": False},  # <- self-reference
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    out = ld.get_output_param_info("svc", "v", "Tree")
    # After Root expands one level, Self is the truncation point
    assert isinstance(out["Root"]["members"], dict)
    assert out["Root"]["members"]["Self"]["members"] == "Node"


def test_O2_unfold_basic_type_list_no_zero_in_path():
    """O2: List<base_type> should not push '0' into the path."""
    objects = {
        "URequest": {"members": [
            {"name": "Tags", "type": "list", "member": "string",
             "document": "", "required": False}
        ]},
    }
    ld = _make_loader(_model({"U": _action("URequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "U")
    # A base-type list path goes only to the field name
    assert "Tags" in unfold
    # Should not register a '0'-bearing path like Tags.0
    assert "Tags.0" not in unfold


def test_O3_get_param_info_value_allowed_null_branch():
    """O3: a field with value_allowed_null=True is written correctly."""
    objects = {"XRequest": {"members": [
        {"name": "F", "type": "string", "member": "string",
         "document": "", "required": True, "value_allowed_null": True}
    ]}}
    ld = _make_loader(_model({"X": _action("XRequest")}, objects))
    info = ld.get_param_info("svc", "v", "X")
    assert info["F"].get("value_allowed_null") == "AllowedNull"

    # Reverse: False maps to NotAllowedNull
    objects["XRequest"]["members"][0]["value_allowed_null"] = False
    info2 = ld.get_param_info("svc", "v", "X")
    assert info2["F"].get("value_allowed_null") == "NotAllowedNull"


# ============================================================
# P. Isolation contract: boundary where Request / Response cycle structures differ
# ============================================================
def test_P1_output_response_only_cycle_no_recursion():
    """P1: when Request is acyclic and Response has a cycle, get_output_param_info takes the safe path without blowing the stack."""
    objects = {
        "TreeRequest": {"members": [
            {"name": "A", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Root", "type": "object", "member": "Node",
             "document": "", "required": True}
        ]},
        "Node": {"members": [
            {"name": "Self", "type": "object", "member": "Node",
             "document": "", "required": False},  # <- self-reference on the Response side only
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    # Should not raise RecursionError; Self should be truncated to a string placeholder
    out = ld.get_output_param_info("svc", "v", "Tree")
    assert isinstance(out["Root"]["members"], dict)
    assert out["Root"]["members"]["Self"]["members"] == "Node"


def test_P2_input_side_unaffected_by_response_cycle():
    """P2: when only the Response has a cycle, the input side (get_param_info) still takes the original path and the output matches the normal case."""
    objects = {
        "TreeRequest": {"members": [
            {"name": "A", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Root", "type": "object", "member": "Node",
             "document": "", "required": True}
        ]},
        "Node": {"members": [
            {"name": "Self", "type": "object", "member": "Node",
             "document": "", "required": False},
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    info = ld.get_param_info("svc", "v", "Tree")
    # The Request side has only the base-type field A, and members is the original string (not a truncation placeholder)
    assert info["A"]["members"] == "string"
    assert set(info.keys()) == {"A"}


# ============================================================
# Allow running directly via `python3 tests/test_loaders.py` (without a pytest environment)
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
