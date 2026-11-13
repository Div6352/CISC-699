
# CISC 699 - Capstone II A2
# Automatic Execution Tracing Test

import json
from pathlib import Path

from traced_contract_router import route_and_save_trace


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


# Valid semantic contracts
valid_contracts = [
    make_contract("Deploy Code", True),
    make_contract("Fix Code", False)
]


# Invalid semantic contract
invalid_contracts = [
    {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "unknown_field",
            "operator": "equals",
            "value": True
        }
    }
]


# Three routing scenarios
test_cases = [
    {
        "name": "Successful Routing",
        "contracts": valid_contracts,
        "workflow_data": {"tests_passed": True},
        "expected_status": "ROUTED",
        "expected_target": "Deploy Code"
    },
    {
        "name": "Invalid Contract",
        "contracts": invalid_contracts,
        "workflow_data": {"tests_passed": True},
        "expected_status": "INVALID_CONTRACT",
        "expected_target": None
    },
    {
        "name": "Invalid Workflow Data",
        "contracts": valid_contracts,
        "workflow_data": {},
        "expected_status": "INVALID_WORKFLOW_DATA",
        "expected_target": None
    }
]


print("\nA2 Research - Automatic Execution Tracing Test")

trace_ids = set()
trace_files = set()
passed_tests = 0


for case in test_cases:

    # Route and automatically save the trace
    output = route_and_save_trace(
        contracts=case["contracts"],
        current_node="Check Tests",
        workflow_data=case["workflow_data"]
    )

    routing_result = output["routing_result"]
    trace_id = output["trace_id"]
    trace_file = Path(output["trace_file"])

    # Verify the routing result
    assert routing_result["status"] == case["expected_status"]
    assert routing_result["next_node"] == case["expected_target"]

    # Verify the trace file was created
    assert trace_file.is_file()

    # Read the saved JSON trace
    with open(trace_file, "r", encoding="utf-8") as file:
        saved_trace = json.load(file)

    # Verify trace contents
    assert saved_trace["routing_status"] == case["expected_status"]
    assert saved_trace["selected_next_node"] == case["expected_target"]
    assert saved_trace["trace_id"] == trace_id

    assert isinstance(saved_trace["decision_explanation"], str)
    assert saved_trace["decision_explanation"]

    assert isinstance(saved_trace["validation_results"], list)

    # Verify trace IDs and file paths are unique
    assert trace_id not in trace_ids
    assert str(trace_file) not in trace_files

    trace_ids.add(trace_id)
    trace_files.add(str(trace_file))

    passed_tests += 1

    print("\nScenario:", case["name"])
    print("Routing status:", routing_result["status"])
    print("Trace saved:", trace_file.name)
    print("Result: PASS")


print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed_tests)
print("Unique trace IDs:", len(trace_ids))
print("Unique trace files:", len(trace_files))

assert passed_tests == len(test_cases)
assert len(trace_ids) == len(test_cases)
assert len(trace_files) == len(test_cases)

print("\nAll automatic execution tracing tests passed!")
