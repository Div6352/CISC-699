
# CISC 699 - Capstone II A2 Research
# Duplicate Edge Identifier Experiment

from contract_validator import validate_contract

print("\nA2 Research - Duplicate Edge Identifier Test")


def make_contract(edge_id, target, expected_value):
    return {
        "edge_id": edge_id,
        "source": "Check Tests",
        "target": target,
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": expected_value
        }
    }


def check_unique_edge_ids(contracts):
    """Check that every contract has a unique edge identifier."""
    edge_ids = [contract["edge_id"] for contract in contracts]
    return len(edge_ids) == len(set(edge_ids))


test_cases = [
    (
        "Two unique edge identifiers",
        [
            make_contract("E01", "Deploy Code", True),
            make_contract("E02", "Fix Code", False)
        ],
        True
    ),
    (
        "Two contracts with duplicate edge identifiers",
        [
            make_contract("E01", "Deploy Code", True),
            make_contract("E01", "Fix Code", False)
        ],
        False
    ),
    (
        "Three contracts with one duplicate identifier",
        [
            make_contract("E01", "Deploy Code", True),
            make_contract("E02", "Fix Code", False),
            make_contract("E01", "Deploy Code", True)
        ],
        False
    ),
    (
        "Three unique edge identifiers",
        [
            make_contract("E01", "Deploy Code", True),
            make_contract("E02", "Fix Code", False),
            make_contract("E03", "Deploy Code", True)
        ],
        True
    )
]

passed = 0

for name, contracts, expected_uniqueness in test_cases:

    # Existing validator checks each contract separately.
    structural_results = [
        validate_contract(contract)
        for contract in contracts
    ]

    assert all(structural_results), (
        f"Structural validation failed unexpectedly: {name}"
    )

    # Separate check examines identifiers across contracts.
    uniqueness_result = check_unique_edge_ids(contracts)

    assert uniqueness_result is expected_uniqueness, (
        f"Incorrect edge identifier uniqueness result: {name}"
    )

    passed += 1

    print(f"\nScenario: {name}")
    print("Individual contracts valid:", all(structural_results))
    print("Edge identifiers unique:", uniqueness_result)
    print("Result: PASS")


print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed)

print("\nOverall result: PASS")
print("All duplicate edge identifier tests passed!")
