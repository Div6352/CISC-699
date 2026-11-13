
# CISC 699 - Capstone II A2 Research
# Extra Semantic Contract Fields Test

from contract_validator import validate_contract

print("\nA2 Research - Extra Contract Fields Test")

# A valid contract without additional fields
valid_contract = {
    "edge_id": "E01",
    "source": "Check Tests",
    "target": "Deploy Code",
    "condition": {
        "field": "tests_passed",
        "operator": "equals",
        "value": True
    }
}

# Test 1: Standard valid contract
result1 = validate_contract(valid_contract)

assert result1 is True
print("Standard valid contract accepted: PASS")

# Test 2: Unexpected top-level field
contract_with_extra_field = {
    **valid_contract,
    "unexpected_field": "extra information"
}

result2 = validate_contract(contract_with_extra_field)

assert result2 is True
print("Extra top-level field accepted: PASS")

# Test 3: Unexpected condition field
contract_with_extra_condition_field = {
    **valid_contract,
    "condition": {
        **valid_contract["condition"],
        "unexpected_condition_field": "extra information"
    }
}

result3 = validate_contract(contract_with_extra_condition_field)

assert result3 is True
print("Extra condition field accepted: PASS")

# Test 4: Both types of unexpected fields
contract_with_both = {
    **contract_with_extra_field,
    "condition": {
        **valid_contract["condition"],
        "unexpected_condition_field": "extra information"
    }
}

result4 = validate_contract(contract_with_both)

assert result4 is True
print("Both unexpected fields accepted: PASS")

print("\nTotal scenarios: 4")
print("Passed scenarios: 4")

print("\nOverall result: PASS")
print("All extra contract fields tests passed!")
