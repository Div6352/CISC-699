
# CISC 699 - Capstone II A2 Research
# Permitted Workflow Graph Transitions Test

from contract_validator import validate_contract

print("\nA2 Research - Permitted Graph Transitions Test")

# Example workflow graph used for this experiment.
workflow_nodes = {
    "Start",
    "Check Tests",
    "Deploy Code",
    "Fix Code"
}

# Explicitly permitted directed transitions.
permitted_transitions = {
    ("Start", "Check Tests"),
    ("Check Tests", "Deploy Code"),
    ("Check Tests", "Fix Code")
}


def check_permitted_transition(contract):
    """Check whether a contract references a permitted graph edge."""
    source = contract["source"]
    target = contract["target"]

    return (
        source in workflow_nodes
        and target in workflow_nodes
        and (source, target) in permitted_transitions
    )


test_cases = [
    (
        "Permitted transition to Deploy Code",
        "Check Tests",
        "Deploy Code",
        True
    ),
    (
        "Permitted transition to Fix Code",
        "Check Tests",
        "Fix Code",
        True
    ),
    (
        "Permitted transition from Start",
        "Start",
        "Check Tests",
        True
    ),
    (
        "Existing nodes but prohibited transition",
        "Deploy Code",
        "Start",
        False
    ),
    (
        "Existing nodes but prohibited shortcut",
        "Start",
        "Deploy Code",
        False
    ),
    (
        "Unknown source node",
        "Unknown Node",
        "Deploy Code",
        False
    ),
    (
        "Unknown target node",
        "Check Tests",
        "Unknown Node",
        False
    )
]

passed = 0

for name, source, target, expected_permission in test_cases:

    contract = {
        "edge_id": "E01",
        "source": source,
        "target": target,
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }

    structural_result = validate_contract(contract)
    permission_result = check_permitted_transition(contract)

    # All contracts have valid structural fields.
    assert structural_result is True, (
        f"Structural validation failed unexpectedly: {name}"
    )

    # The separate graph check must identify allowed edges.
    assert permission_result is expected_permission, (
        f"Incorrect graph transition result: {name}"
    )

    passed += 1

    print(f"\nScenario: {name}")
    print("Structural validation:", structural_result)
    print("Permitted graph transition:", permission_result)
    print("Result: PASS")

print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed)

print("\nOverall result: PASS")
print("All permitted graph transition tests passed!")
