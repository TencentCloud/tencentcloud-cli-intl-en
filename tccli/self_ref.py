# -*- coding: utf-8 -*-

"""Self-referencing type-graph detector.

Detect whether an action's type graph contains a cycle (composite types that
reference themselves or one another).

Contract (single source of truth for the isolation boundary):
  - Input side (command's ``__call__`` dispatch, ``get_param_info``,
    ``generate_param_skeleton``, ``get_unfold_param_info``) must detect the
    ``Request`` type graph via the default ``root_suffix="Request"``.
  - Output side (``get_output_param_info``) must detect the ``Response`` type
    graph via ``root_suffix="Response"``, because the two graphs may differ in
    structure.
  - On any exception, always fall back to ``False`` (prefer a miss -- backed by
    test cases -- over a false positive, which would change the behavior of the
    stable path).
"""

BASE_TYPE = frozenset([
    "int64", "uint64", "string", "float", "bool",
    "date", "datetime", "datetime_iso", "binary",
])


def _dfs_has_cycle(objects, type_name, path_visited):
    """Run a DFS over ``objects`` starting from ``type_name`` to detect a cycle.

    :param objects: the type graph, shaped like ``type_name -> {"members": [{...}, ...]}``.
    :param type_name: the type name currently being checked.
    :param path_visited: frozenset of type names already visited on the current DFS path.
    :return: True if a cycle is found.
    """
    # Bad data (missing type / invalid members) naturally raises here and is
    # uniformly caught as False by the outer is_action_self_referencing
    # try/except, so this function focuses purely on cycle detection and does no
    # defensive checks.
    for member in objects[type_name]["members"]:
        ref_name = member.get("member")  # the type name referenced by this field
        if not ref_name or ref_name in BASE_TYPE:  # base types are leaves, prune
            continue
        if ref_name in path_visited:  # loops back to a type on the current path -> cycle
            return True
        # Descend into the sub-type; a fresh set keeps each DFS branch path
        # independent and uncontaminated.
        if _dfs_has_cycle(objects, ref_name, path_visited | {ref_name}):
            return True
    return False


def is_action_self_referencing(service, version, action, service_model,
                               root_suffix="Request"):
    """Determine whether an ``action``'s type graph contains a self-referencing cycle.

    :param service: service name.
    :param version: version number (e.g. "2017-03-12").
    :param action: action name.
    :param service_model: the full service model dict, which must contain the "objects" key.
    :param root_suffix: the root type suffix to detect, ``"Request"`` (input graph, default)
        or ``"Response"`` (output graph). The two graphs may differ in structure,
        so callers that render output must pass ``"Response"`` explicitly.
    :return: True if the corresponding type graph contains a cycle.
    """
    try:
        objects = service_model.get("objects", {})
        root_type_name = action + root_suffix
        return _dfs_has_cycle(objects, root_type_name, frozenset([root_type_name]))
    except Exception:
        return False
