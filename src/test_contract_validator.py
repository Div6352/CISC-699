
# CISC 699 - A2 Research Project
# Semantic Contract Validator Test

from contract_validator import validate_contract
from semantic_contract import (
    semantic_contract,
    semantic_contract_E02
)

print("\nA2 Research - Contract Validation Test")

result1 = validate_contract(semantic_contract)
print("E01 valid:", result1)

result2 = validate_contract(semantic_contract_E02)
print("E02 valid:", result2)

assert result1 is True
assert result2 is True

print("Both contract validation tests passed!")

# Test an invalid semantic contract

invalid_contract = {
    "edge_id": "E03",
    "source": "Check Tests",
    "target": "Deploy Code",
    "condition": {
        "field": "tests_passed",
        "operator": "greater_than",
        "value": True
    }
}

print("\nTesting invalid semantic contract...")

result3 = validate_contract(invalid_contract)

print("E03 valid:", result3)

assert result3 is False

print("Invalid contract correctly rejected!")

# Test a contract with a missing condition

missing_condition_contract = {
    "edge_id": "E04",
    "source": "Check Tests",
    "target": "Deploy Code"
}

print("\nTesting missing condition...")

result4 = validate_contract(missing_condition_contract)

print("E04 valid:", result4)

assert result4 is False

print("Missing condition correctly rejected!")
