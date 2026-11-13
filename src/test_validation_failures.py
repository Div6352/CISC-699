
# CISC 699 - Capstone II A2
# Semantic Contract Validation Failure Tests

from contract_validator import validate_contract
from contract_evaluator import evaluate_contract


# A valid semantic contract
valid_contract = {
    "source": "Check Tests",
    "target": "Deploy Code",
    "condition": {
        "field": "tests_passed",
        "operator": "equals",
        "value": True
    }
}


# Invalid semantic contracts
invalid_contracts = [
    {
        "name": "Incorrect field name",
        "contract": {
            "source": "Check Tests",
            "target": "Deploy Code",
            "condition": {
                "field": "wrong_field",
                "operator": "equals",
                "value": True
            }
        }
    },
    {
        "name": "Unsupported operator",
        "contract": {
            "source": "Check Tests",
            "target": "Deploy Code",
            "condition": {
                "field": "tests_passed",
                "operator": "greater_than",
                "value": True
            }
        }
    },
    {
        "name": "Invalid Boolean value",
        "contract": {
            "source": "Check Tests",
            "target": "Deploy Code",
            "condition": {
                "field": "tests_passed",
                "operator": "equals",
                "value": "True"
            }
        }
    },
    {
        "name": "Missing condition",
        "contract": {
            "source": "Check Tests",
            "target": "Deploy Code"
        }
    }
]


print("\nA2 Research - Validation Failure Tests")

# Confirm the valid contract is accepted
assert validate_contract(valid_contract) is True
print("Valid contract: ACCEPTED")


# Confirm each invalid contract is rejected
for case in invalid_contracts:
    name = case["name"]
    contract = case["contract"]

    assert validate_contract(contract) is False, (
        f"Validator incorrectly accepted: {name}"
    )

    try:
        evaluate_contract(contract, {"tests_passed": True})
    except ValueError:
        print(f"{name}: REJECTED")
    else:
        raise AssertionError(
            f"Evaluator did not reject: {name}"
        )


print("\nAll validation failure tests passed!")

