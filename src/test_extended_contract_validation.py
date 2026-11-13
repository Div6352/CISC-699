
# CISC 699 - Capstone II A2 Research
# Extended Semantic Contract Validation Test

from contract_validator import validate_contract

print("\nA2 Research - Extended Contract Validation Test")

# Each contract below must be rejected by the validator.
invalid_contracts = [
    ("Contract is None", None),
    ("Contract is a list", []),
    ("Missing source", {
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }),
    ("Empty source", {
        "source": "",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }),
    ("Missing target", {
        "source": "Check Tests",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }),
    ("Empty target", {
        "source": "Check Tests",
        "target": " ",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }),
    ("Invalid edge ID", {
        "edge_id": "",
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }),
    ("Missing condition", {
        "source": "Check Tests",
        "target": "Deploy Code"
    }),
    ("Invalid condition field", {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "unknown_field",
            "operator": "equals",
            "value": True
        }
    }),
    ("Invalid operator", {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "greater_than",
            "value": True
        }
    }),
    ("Non-Boolean condition value", {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": "True"
        }
    }),
    ("Integer condition value", {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": 1
        }
    })
]

passed = 0

for name, contract in invalid_contracts:
    result = validate_contract(contract)

    assert result is False, (
        f"FAIL: {name} was incorrectly accepted."
    )

    passed += 1
    print(f"{name}: PASS")

print("\nTotal invalid contracts:", len(invalid_contracts))
print("Correctly rejected:", passed)

assert passed == len(invalid_contracts)

print("\nOverall result: PASS")
print("All extended contract validation tests passed!")
