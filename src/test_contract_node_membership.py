
# CISC 699 - Capstone II A2 Research
# Workflow Graph Node Membership Test

from contract_validator import validate_contract

print("\nA2 Research - Contract Node Membership Test")

# Nodes in the example workflow graph
workflow_nodes = {
    "Start",
    "Check Tests",
    "Deploy Code",
    "Fix Code"
}

def check_node_membership(contract):
    """Check whether both contract nodes exist in the graph."""
    return (
        contract["source"] in workflow_nodes
        and contract["target"] in workflow_nodes
    )

# Test scenarios
test_cases = [
    (
        "Both nodes exist",
        "Check Tests",
        "Deploy Code",
        True
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
    ),
    (
        "Both nodes unknown",
        "Unknown Source",
        "Unknown Target",
        False
    )
]

passed = 0

for name, source, target, expected_membership in test_cases:

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
    membership_result = check_node_membership(contract)

    # Current validator accepts all four structurally valid contracts.
    assert structural_result is True, (
        f"Unexpected structural validation failure: {name}"
    )

    # Separate graph membership check verifies node existence.
    assert membership_result is expected_membership, (
        f"Unexpected node membership result: {name}"
    )

    passed += 1

    print(f"\nScenario: {name}")
    print("Structural validation:", structural_result)
    print("Graph node membership:", membership_result)
    print("Result: PASS")

print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed)

print("\nOverall result: PASS")
print("All contract node membership tests passed!")
