
# CISC 699 - Capstone II A2
# Improved Deterministic Workflow-Path Repeatability Test

from contract_router import route_with_explanation


# Conditional workflow contracts
#
# Check Tests -> Deploy Code when tests_passed = True
# Check Tests -> Fix Code when tests_passed = False

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


# A fixed initial transition.
# This is test setup, not a semantic-contract decision.
initial_transition = {
    "Start": "Check Tests"
}


def execute_workflow(workflow_data):

    current_node = "Start"
    path = [current_node]

    # Step 1: Follow the fixed initial transition
    current_node = initial_transition[current_node]
    path.append(current_node)

    # Step 2: Use the deterministic semantic contract router
    result = route_with_explanation(
        contracts,
        current_node,
        workflow_data
    )

    assert result["status"] == "ROUTED", (
        "Expected ROUTED but received "
        + result["status"]
    )

    assert result["next_node"] is not None

    # Step 3: Record the selected destination
    current_node = result["next_node"]
    path.append(current_node)

    return path


print("\nA2 Research - Improved Workflow Path Repeatability Test")


scenarios = [
    {
        "name": "Tests Passed",
        "data": {"tests_passed": True},
        "expected": [
            "Start",
            "Check Tests",
            "Deploy Code"
        ]
    },
    {
        "name": "Tests Failed",
        "data": {"tests_passed": False},
        "expected": [
            "Start",
            "Check Tests",
            "Fix Code"
        ]
    }
]


repetitions = 10
total_executions = 0
total_correct = 0


for scenario in scenarios:

    paths = []

    for _ in range(repetitions):

        path = execute_workflow(scenario["data"])
        paths.append(path)

        total_executions += 1

        if path == scenario["expected"]:
            total_correct += 1

    identical_paths = all(
        path == paths[0]
        for path in paths
    )

    correct_paths = all(
        path == scenario["expected"]
        for path in paths
    )

    print("\nScenario:", scenario["name"])
    print("Expected path:", scenario["expected"])
    print("Observed path:", paths[0])
    print("Repeated executions:", repetitions)
    print("Identical paths:", identical_paths)
    print("Correct paths:", correct_paths)

    assert identical_paths, (
        "Workflow paths were not identical."
    )

    assert correct_paths, (
        "Workflow paths did not match the expected path."
    )

    print("Result: PASS")


accuracy = (
    total_correct / total_executions
) * 100


print("\nTotal executions:", total_executions)
print("Correct executions:", total_correct)
print(f"Expected-path accuracy: {accuracy:.2f}%")

assert total_correct == total_executions

print("\nAll improved workflow-path repeatability tests passed!")
