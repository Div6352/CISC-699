
# CISC 699 - A2 Research Project
# Deterministic Contract Router Test

from contract_router import (
    select_next_node_from_contracts,
    route_with_explanation
)

from semantic_contract import (
    semantic_contract,
    semantic_contract_E02
)


# Collect both semantic contracts
contracts = [
    semantic_contract,
    semantic_contract_E02
]

current_node = "Check Tests"

print("\nA2 Research - Contract Router Test")


# Test 1: All tests passed
result1 = select_next_node_from_contracts(
    contracts,
    current_node,
    {"tests_passed": True}
)

print("Tests passed ->", result1)

assert result1 == "Deploy Code"


# Test 2: Tests failed
result2 = select_next_node_from_contracts(
    contracts,
    current_node,
    {"tests_passed": False}
)

print("Tests failed ->", result2)

assert result2 == "Fix Code"

print("Basic contract routing tests passed!")


# Test 3: Invalid workflow data
print("\nTesting invalid workflow data...")

result3 = select_next_node_from_contracts(
    contracts,
    current_node,
    {"tests_passed": None}
)

print("Invalid workflow data result:", result3)

assert result3 is None

print("Invalid workflow data test passed!")


# Test 4: Ambiguous routing
print("\nTesting ambiguous routing...")

ambiguous_contracts = [
    {
        "edge_id": "E05",
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    {
        "edge_id": "E06",
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }
]

result4 = select_next_node_from_contracts(
    ambiguous_contracts,
    "Check Tests",
    {"tests_passed": True}
)

print("Ambiguous routing result:", result4)

assert result4 is None

print("Ambiguous routing test passed!")


# Test 5: Successful routing explanation
print("\nTesting successful routing explanation...")

result5 = route_with_explanation(
    contracts,
    "Check Tests",
    {"tests_passed": True}
)

print("Routing explanation:", result5)

assert result5["status"] == "ROUTED"
assert result5["next_node"] == "Deploy Code"

print("Successful routing explanation test passed!")


# Test 6: Invalid workflow data explanation
print("\nTesting invalid workflow data explanation...")

result6 = route_with_explanation(
    contracts,
    "Check Tests",
    {"tests_passed": None}
)

print("Routing explanation:", result6)

assert result6["status"] == "INVALID_WORKFLOW_DATA"
assert result6["next_node"] is None

print("Invalid workflow data explanation test passed!")


# Test 7: Ambiguous routing explanation
print("\nTesting AMBIGUOUS explanation...")

result7 = route_with_explanation(
    ambiguous_contracts,
    "Check Tests",
    {"tests_passed": True}
)

print("Routing explanation:", result7)

assert result7["status"] == "AMBIGUOUS"
assert result7["next_node"] is None

print("AMBIGUOUS routing explanation test passed!")


print("\nAll contract router tests passed!")
