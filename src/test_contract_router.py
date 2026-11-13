
# CISC 699 - A2 Research Project
# Deterministic Semantic Contract Router Tests

from contract_router import route_with_explanation


def make_contract(target, expected_value):
    return {
        "source": "Check Tests",
        "target": target,
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": expected_value
        }
    }


contracts = [
    make_contract("Deploy Code", True),
    make_contract("Fix Code", False)
]


def check_result(
    test_name,
    test_contracts,
    workflow_data,
    expected_status,
    expected_node
):
    result = route_with_explanation(
        test_contracts,
        "Check Tests",
        workflow_data
    )

    assert result["status"] == expected_status, (
        f"{test_name}: unexpected status: {result}"
    )

    assert result["next_node"] == expected_node, (
        f"{test_name}: unexpected next node: {result}"
    )

    print(f"PASS: {test_name}")


# Test 1: All tests passed
check_result(
    "Passed tests route to deployment",
    contracts,
    {"tests_passed": True},
    "ROUTED",
    "Deploy Code"
)


# Test 2: Tests failed
check_result(
    "Failed tests route to fixing code",
    contracts,
    {"tests_passed": False},
    "ROUTED",
    "Fix Code"
)


# Test 3: No matching contract
check_result(
    "No matching contract",
    [make_contract("Deploy Code", True)],
    {"tests_passed": False},
    "NO_MATCH",
    None
)


# Test 4: Multiple matching contracts
check_result(
    "Ambiguous contracts",
    [
        make_contract("Deploy Code", True),
        make_contract("Fix Code", True)
    ],
    {"tests_passed": True},
    "AMBIGUOUS",
    None
)


# Test 5: Repeat the same decision
first_result = route_with_explanation(
    contracts,
    "Check Tests",
    {"tests_passed": True}
)

for run_number in range(1, 11):

    result = route_with_explanation(
        contracts,
        "Check Tests",
        {"tests_passed": True}
    )

    assert result == first_result, (
        f"Routing changed on repetition {run_number}"
    )

assert first_result["status"] == "ROUTED"
assert first_result["next_node"] == "Deploy Code"

print("PASS: Repeated routing is deterministic")


print("\nAll 5 router test scenarios passed!")
