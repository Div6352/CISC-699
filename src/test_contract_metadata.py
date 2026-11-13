
# CISC 699 - Capstone II A2
# Contract Metadata Validation Tests

from contract_validator import validate_contract


def make_contract():
    return {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }


print("\nA2 Research - Contract Metadata Validation Tests")

# Check a valid contract
assert validate_contract(make_contract()) is True
print("Valid contract: ACCEPTED")


# Test invalid metadata
test_cases = [
    ("Missing source", "source", None),
    ("Empty source", "source", ""),
    ("Invalid source type", "source", 123),
    ("Missing target", "target", None),
    ("Empty target", "target", ""),
    ("Invalid target type", "target", 123),
    ("Empty edge ID", "edge_id", ""),
    ("Invalid edge ID type", "edge_id", 123),
]

for name, field, value in test_cases:
    contract = make_contract()

    if value is None:
        contract.pop(field, None)
    else:
        contract[field] = value

    assert validate_contract(contract) is False, (
        f"Validator incorrectly accepted: {name}"
    )

    print(f"{name}: REJECTED")


# Check that a valid optional edge ID is accepted
contract = make_contract()
contract["edge_id"] = "edge_001"

assert validate_contract(contract) is True
print("Valid optional edge ID: ACCEPTED")

print("\nAll contract metadata validation tests passed!")
