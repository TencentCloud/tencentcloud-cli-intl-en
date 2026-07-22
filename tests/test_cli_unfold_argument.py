# -*- coding:utf-8 -*-
"""
recursive-nesting-30: unit tests for CliUnfoldArgument.

Coverage goals:
  1. ``convert_to_dict`` can still correctly build a nested dict from a flat key of
     arbitrary depth (including 30-segment self-reference / D=61);
  2. ``handle_array`` correctly turns pure-numeric keys into lists and raises on mixed keys;
  3. when ``build_action_parameters`` accepts the optional ``extra_unfold_args``, it can
     merge it with the registered argparse Namespace; ``None`` / empty dict behaves as before;
  4. red line (requirement 1.4): the output nesting does not pad None / empty dict.

Note: this file does not depend on any services/*/v*/api.json, so CI can still run it
after the repository is slimmed down.
"""

import argparse

import pytest

from tccli.cli_unfold_argument import CliUnfoldArgument
from tccli.exceptions import UnknownArgumentError


# ============================================================
# Helper: use argparse.Namespace to simulate flat args after argparse parsing
# ============================================================
def _ns(**kwargs):
    """Build an ``argparse.Namespace`` whose ``__dict__`` is ``vars(ns)``."""
    return argparse.Namespace(**kwargs)


def _build_unfold_arg():
    return CliUnfoldArgument()


# ============================================================
# A. convert_to_dict basic behavior
# ============================================================
def test_A1_convert_to_dict_simple_flat_key():
    """A1: a single-segment key lands at the top level of params_set."""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "Foo", "v")
    assert bag == {"Foo": "v"}


def test_A2_convert_to_dict_two_level():
    """A2: a two-segment key recursively creates one dict level."""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "A.B", "v")
    assert bag == {"A": {"B": "v"}}


def test_A3_convert_to_dict_with_array_index():
    """A3: a key with a numeric segment is still a dict at the convert_to_dict stage, relying on handle_array to turn it into a list."""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "A.0.B", "v")
    assert bag == {"A": {"0": {"B": "v"}}}


# ============================================================
# B. Correctness of convert_to_dict at D=5 / D=7 / D=61 (30-segment self-reference)
# ============================================================
def _build_self_ref_keys(num_levels):
    """Build a ``num_levels``-segment self-referencing flat key.

    Each segment is ``Children.0``, and the whole looks like ``Children.0.Children.0...LeafField``.
    Returns (key, depth).
    """
    parts = ["Children", "0"] * num_levels + ["LeafField"]
    key = ".".join(parts)
    return key, len(parts)


def test_B3_convert_to_dict_depth_61_self_ref_30_levels():
    """B3: a 30-segment self-reference (D=61) can be built correctly without hitting the recursion limit."""
    key, depth = _build_self_ref_keys(30)
    assert depth == 61

    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, key, "deep_value")

    # Walk down the 30 levels of Children/0 to the terminal LeafField
    cursor = bag
    for _ in range(30):
        assert "Children" in cursor
        cursor = cursor["Children"]
        assert "0" in cursor
        cursor = cursor["0"]
    assert cursor == {"LeafField": "deep_value"}


# ============================================================
# C. handle_array companion behavior: after handle_array, list indices align for 30-level self-reference
# ============================================================
def test_C1_handle_array_depth_61_no_padding():
    """C1: after handle_array, the D=61 nested structure still does not pad None / empty dict (red line 1.4)."""
    key, _ = _build_self_ref_keys(30)
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, key, "deep_value")
    out = arg.handle_array(bag, "--")

    # Expect: each level is {"Children": [{...}]} (list length 1, index 0)
    cursor = out
    for _ in range(30):
        assert isinstance(cursor, dict)
        assert "Children" in cursor
        children = cursor["Children"]
        assert isinstance(children, list)
        assert len(children) == 1, "the list must strictly contain only index 0, without None padding"
        cursor = children[0]
    # The terminal is a dict rather than None
    assert cursor == {"LeafField": "deep_value"}


def test_C2_handle_array_rejects_non_consecutive_index():
    """C2: handle_array raises on non-consecutive indices (1 without 0) per the existing contract -- regression protection, unaffected by this change."""
    arg = _build_unfold_arg()
    bag = {"A": {"1": "v"}}  # missing "0"
    with pytest.raises(UnknownArgumentError):
        arg.handle_array(bag, "--")


# ============================================================
# D. build_action_parameters accepting extra_unfold_args injection
# ============================================================
def test_D1_build_action_parameters_without_extra_args_unchanged():
    """D1: without passing extra_unfold_args, behavior is exactly as before."""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v", "A.1.B": "w"})
    out = arg.build_action_parameters(ns)
    assert out == {"A": [{"B": "v"}, {"B": "w"}]}


def test_D2_build_action_parameters_with_none_extra_args_unchanged():
    """D2: passing None / empty dict behaves the same as D1."""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v"})
    assert arg.build_action_parameters(ns, extra_unfold_args=None) == {"A": [{"B": "v"}]}
    assert arg.build_action_parameters(_ns(**{"A.0.B": "v"}), extra_unfold_args={}) \
        == {"A": [{"B": "v"}]}


def test_D3_build_action_parameters_extra_args_merge_with_namespace():
    """D3: extra_unfold_args merges with the Namespace to build the same nested structure (D=5)."""
    arg = _build_unfold_arg()
    ns = _ns(**{"Outer.Inner": "registered"})
    extra = {"Outer.Deep.0.X": "v1", "Outer.Deep.0.Y": "v2"}
    out = arg.build_action_parameters(ns, extra_unfold_args=extra)
    assert out == {
        "Outer": {
            "Inner": "registered",
            "Deep": [{"X": "v1", "Y": "v2"}],
        },
    }


def test_D4_build_action_parameters_extra_args_depth_61():
    """D4: extra_unfold_args alone carries a D=61 flat key and still builds 30-level nesting correctly.

    End-to-end coverage path: a deeply nested key not registered with argparse -> collected by
    command.py's fallback branch -> through build_action_parameters(extra_unfold_args=...) ->
    convert_to_dict + handle_array outputs the request body.
    """
    key, _ = _build_self_ref_keys(30)
    arg = _build_unfold_arg()
    ns = _ns()  # empty Namespace -- the Namespace itself can only hold registered flat keys
    out = arg.build_action_parameters(ns, extra_unfold_args={key: "deep_value"})

    cursor = out
    for _ in range(30):
        assert isinstance(cursor, dict)
        assert "Children" in cursor
        children = cursor["Children"]
        assert isinstance(children, list) and len(children) == 1
        cursor = children[0]
    assert cursor == {"LeafField": "deep_value"}


def test_D5_build_action_parameters_extra_args_skip_none_values():
    """D5: items in extra_unfold_args whose value is None are skipped (consistent with Namespace behavior)."""
    arg = _build_unfold_arg()
    ns = _ns()
    out = arg.build_action_parameters(
        ns,
        extra_unfold_args={"A.0.B": "v", "A.0.C": None},
    )
    assert out == {"A": [{"B": "v"}]}


# ============================================================
# E. Legacy-compatible path (build_action_parameters_old / gen_param_dict / merge_dict)
# ============================================================
def test_E1_gen_param_dict_simple_flat_key():
    """E1: gen_param_dict handles a single-segment key."""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"Foo": "v"})
    assert out == [{"Foo": "v"}]


def test_E2_gen_param_dict_array_index():
    """E2: gen_param_dict handles a key with a numeric index and builds a pre-filled None list."""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"A.0.B": "v"})
    assert isinstance(out, list) and len(out) == 1
    assert out[0]["A"][0]["B"] == "v"


def test_E3_gen_param_dict_no_array_two_seg():
    """E3: gen_param_dict attaches the value directly for a single-level key without an index."""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"A.B": "v"})
    assert out == [{"A": {"B": "v"}}]


def test_E4_internal_gen_param_dict_empty_param():
    """E4: _gen_param_dict returns an empty dict directly when the input is empty."""
    arg = _build_unfold_arg()
    bag = {}
    out = arg._gen_param_dict([], bag)
    assert bag == {}


def test_E5_internal_gen_param_dict_three_seg_with_index():
    """E5: _gen_param_dict handles a 3-segment parameter with a numeric index."""
    arg = _build_unfold_arg()
    bag = {}
    arg._gen_param_dict(["A", "0", "x"], bag)
    assert bag == {"A": ["x"]}


def test_E6_internal_gen_param_dict_three_seg_object():
    """E6: _gen_param_dict handles a 3-segment parameter without an index."""
    arg = _build_unfold_arg()
    bag = {}
    arg._gen_param_dict(["A", "B", "v"], bag)
    assert bag == {"A": {"B": "v"}}


def test_E7_recur_merge_dict_dict_branch():
    """E7: recur_merge_dict recursively merges a new key across two dicts."""
    arg = _build_unfold_arg()
    src = {"A": {"X": "1"}}
    dis = {"A": {"Y": "2"}}
    out = arg.recur_merge_dict(src, dis)
    assert out == {"A": {"X": "1", "Y": "2"}}


def test_E8_recur_merge_dict_list_branch():
    """E8: recur_merge_dict merges scalar / dict elements by index across lists."""
    arg = _build_unfold_arg()
    src = [{"X": "1"}, "scalar2"]
    dis = [{"Y": "2"}, None]
    out = arg.recur_merge_dict(src, dis)
    # list[0] goes through dict recursion, list[1] through scalar assignment
    assert out[0] == {"X": "1", "Y": "2"}
    assert out[1] == "scalar2"


def test_E9_merge_dict_empty_returns_empty():
    """E9: merge_dict returns an empty dict for an empty list."""
    arg = _build_unfold_arg()
    assert arg.merge_dict([]) == {}


def test_E10_merge_dict_disjoint_keys():
    """E10: merge_dict merges two disjoint-key dicts into one."""
    arg = _build_unfold_arg()
    out = arg.merge_dict([{"A": "1"}, {"B": "2"}])
    assert out == {"A": "1", "B": "2"}


def test_E11_merge_dict_overlapping_keys_recurse():
    """E11: merge_dict recursively merges sub-structures for overlapping keys."""
    arg = _build_unfold_arg()
    out = arg.merge_dict([
        {"A": {"X": "1"}},
        {"A": {"Y": "2"}},
    ])
    assert out == {"A": {"X": "1", "Y": "2"}}


def test_E12_build_action_parameters_old_simple():
    """E12: build_action_parameters_old legacy path -- single-level key without an index."""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.B": "v"})
    out = arg.build_action_parameters_old(ns)
    assert out == {"A": {"B": "v"}}


def test_E13_build_action_parameters_old_with_array():
    """E13: build_action_parameters_old legacy path -- key with a numeric index."""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v1", "A.1.B": "v2"})
    out = arg.build_action_parameters_old(ns)
    assert out["A"][0]["B"] == "v1"
    assert out["A"][1]["B"] == "v2"


def test_E14_build_action_parameters_old_skips_none():
    """E14: build_action_parameters_old legacy path -- items whose value is None are skipped."""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.B": "v", "A.C": None})
    out = arg.build_action_parameters_old(ns)
    assert out == {"A": {"B": "v"}}
