
# CISC 699 - Capstone II A2
# Missing and Invalid Workflow Data Safety Test

from contract_router import route_with_explanation


contracts = [
    {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }
    }
]


scenarios = [
    {
        "name": "Missing tests_passed field",
        "data": {}
    },
    {
        "name": "tests_passed is None",
        "data": {"tests_passed": None}
    },
    {
        "name": "tests_passed is a string",
        "data": {"tests_passed": "True"}
    },
    {
        "name": "tests_passed is an integer",
        "data": {"tests_passed": 1}
    },
    {
        "name": "tests_passed is an empty string",
        "data": {"tests_passed": ""}
    },
    {
        "name": "tests_passed is a list",
        "data": {"tests_passed": []}
    },
    {
        "name": "Workflow data is None",
        "data": None
    },
    {
        "name": "Workflow data is a list",
        "data": []
    }
]


print("\nA2 Research - Improved Workflow Data Safety Test")

passed_tests = 0

for scenario in scenarios:

    result = route_with_explanation(
        contracts,
        "Check Tests",
        scenario["data"]
    )

    print("\nScenario:", scenario["name"])
    print("Routing status:", result["status"])
    print("Selected next node:", result["next_node"])

    assert result["status"] == "INVALID_WORKFLOW_DATA", (
        "Expected INVALID_WORKFLOW_DATA."
    )

    assert result["next_node"] is None, (
        "Invalid workflow data selected a destination."
    )

    assert result["matched_contracts"] == [], (
        "Invalid workflow data matched a contract."
    )

    assert isinstance(result["decision_explanation"], str)
    assert result["decision_explanation"]

    passed_tests += 1
    print("Result: PASS")


print("\nTotal scenarios:", len(scenarios))
print("Passed scenarios:", passed_tests)

assert passed_tests == len(scenarios)

print("\nAll improved workflow data safety tests passed!")
