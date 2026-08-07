# -*- coding: utf-8 -*-
"""
Unit tests for the cycle detector in tccli/self_ref.py.

Cover the detector's capability contract (without relying on any SDK / real api.json):
  A. _dfs_has_cycle across cycle shapes: direct self-loop, indirect cycle, multi-level cycle, no cycle, base-type breakout.
  B. is_action_self_referencing Request / Response dual-entry semantics.
  C. Exception fallback to False.
"""
import os
import sys

try:
    import pytest  # noqa: F401
except ImportError:
    pass

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tccli.self_ref import (  # noqa: E402
    _dfs_has_cycle, is_action_self_referencing,
)


def _obj(members):
    return {"members": members}


def _m(name, type_, member, required=True):
    return {"name": name, "type": type_, "member": member,
            "document": "", "required": required}


# ============================================================
# A. _dfs_has_cycle cycle shapes
# ============================================================
def test_A1_direct_self_cycle():
    """A->A: a type references itself directly."""
    objects = {"A": _obj([_m("Self", "object", "A", False)])}
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A2_indirect_cycle():
    """A->B->A: a two-level indirect cycle."""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToA", "object", "A", False)]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A3_multi_level_cycle():
    """A->B->C->A: a multi-level cycle."""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToC", "object", "C")]),
        "C": _obj([_m("ToA", "object", "A", False)]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A4_no_cycle_linear_chain():
    """A->B->C->(string): a linear chain without a cycle."""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToC", "object", "C")]),
        "C": _obj([_m("Leaf", "string", "string")]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


def test_A5_base_type_breaks_traversal():
    """Base-type members are not traversed and must not be mistaken for a cycle."""
    objects = {
        "A": _obj([
            _m("Id", "string", "string"),
            _m("Count", "int", "int64", False),
        ]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


def test_A6_list_member_cycle():
    """Self-reference in a List<A> form (e.g. Node.Children: list of Node)."""
    objects = {
        "Node": _obj([
            _m("Val", "string", "string"),
            _m("Children", "list", "Node", False),
        ]),
    }
    assert _dfs_has_cycle(objects, "Node", frozenset(["Node"])) is True


def test_A7_diamond_no_cycle():
    """Diamond with a shared type but no cycle: A->B->D, A->C->D, D is a leaf."""
    objects = {
        "A": _obj([_m("ToB", "object", "B"), _m("ToC", "object", "C")]),
        "B": _obj([_m("ToD", "object", "D")]),
        "C": _obj([_m("ToD", "object", "D")]),
        "D": _obj([_m("Leaf", "string", "string")]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


# ============================================================
# B. is_action_self_referencing dual-entry semantics
# ============================================================
def _model_request_cycle_only():
    """Request has a cycle, Response does not."""
    return {"objects": {
        "TreeRequest": _obj([_m("Root", "object", "Node")]),
        "TreeResponse": _obj([_m("Ok", "string", "string")]),
        "Node": _obj([_m("Self", "object", "Node", False)]),
    }}


def _model_response_cycle_only():
    """Request has no cycle, Response has one."""
    return {"objects": {
        "TreeRequest": _obj([_m("A", "string", "string")]),
        "TreeResponse": _obj([_m("Root", "object", "Node")]),
        "Node": _obj([_m("Self", "object", "Node", False)]),
    }}


def test_B1_request_side_detects_request_cycle():
    model = _model_request_cycle_only()
    assert is_action_self_referencing("s", "v", "Tree", model) is True
    # default root_suffix="Request"
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Request") is True


def test_B2_request_side_ignores_response_cycle():
    """When Request has no cycle, the input side defaults to False (even if Response has a cycle)."""
    model = _model_response_cycle_only()
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_B3_response_side_detects_response_cycle():
    """The output side passes root_suffix='Response' explicitly and can detect a Response cycle."""
    model = _model_response_cycle_only()
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Response") is True


def test_B4_response_side_ignores_request_cycle():
    model = _model_request_cycle_only()
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Response") is False


# ============================================================
# C. Exception fallback
#
# _dfs_has_cycle focuses purely on cycle detection and does no defensive checks;
# bad data (missing objects/root type / dangling reference / invalid members) is
# uniformly caught as False by the is_action_self_referencing try/except.
# This group verifies that outer fault-tolerance contract.
# ============================================================
def test_C1_missing_objects_key_returns_false():
    assert is_action_self_referencing("s", "v", "X", {}) is False


def test_C2_none_service_model_returns_false():
    assert is_action_self_referencing("s", "v", "X", None) is False


def test_C3_missing_root_type_returns_false():
    """Returns False when the root type for the action is missing from objects."""
    model = {"objects": {"OtherRequest": _obj([_m("A", "string", "string")])}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C4_dangling_reference_returns_false():
    """Dangling reference: a field member points to a type absent from objects; the outer layer falls back to False."""
    model = {"objects": {
        "TreeRequest": _obj([_m("Root", "object", "NotThere", False)]),
    }}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C5_members_not_list_returns_false():
    """Dirty data: the root type's members is not a list; the outer layer falls back to False."""
    model = {"objects": {"TreeRequest": {"members": "not-a-list"}}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C6_non_dict_member_returns_false():
    """Dirty data: members contains non-dict elements; the outer layer falls back to False."""
    model = {"objects": {"TreeRequest": {"members": ["garbage", 123]}}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


if __name__ == "__main__":
    import pytest as _pt
    sys.exit(_pt.main([os.path.abspath(__file__), "-v"]))
