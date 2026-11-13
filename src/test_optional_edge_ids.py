
# CISC 699 - Capstone II A2 Research
# Optional Edge Identifier Experiment

from contract_validator import validate_contract

print("\nA2 Research - Optional Edge Identifier Test")


def make_contract():
    return {
        "edge_id": "E01",
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }


test_cases = [
    (
        "Valid edge identifier",
        make_contract(),
        True
    ),
    (
        "Missing edge identifier",
        {key: value for key, value in make_contract().items()
         if key != "edge_id"},
        True
    ),
    (
        "Empty edge identifier",
        {**make_contract(), "edge_id": ""},
        False
    ),
    (
        "Numeric edge identifier",
        {**make_contract(), "edge_id": 123},
        False
    ),
    (
        "Whitespace-only edge identifier",
        {**make_contract(), "edge_id": "   "},
        False
    )
]

passed = 0

for name, contract, expected in test_cases:
    actual = validate_contract(contract)

    assert actual is expected, (
        f"FAILED: {name}. "
        f"Expected {expected}, got {actual}"
    )

    passed += 1

    print(f"\nScenario: {name}")
    print("Contract valid:", actual)
    print("Result: PASS")


print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed)
print("\nOverall result: PASS")
print("All optional edge identifier tests passed!")
