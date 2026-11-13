
# CISC 699 - Capstone II A2
# Repeated Automatic Execution Tracing Reliability Test

import json
from pathlib import Path

from traced_contract_router import route_and_save_trace


# Two valid semantic contracts
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


# Repeat each workflow scenario 10 times
test_scenarios = [
    {
        "name": "Tests Passed",
        "workflow_data": {"tests_passed": True},
        "expected_target": "Deploy Code"
    },
    {
        "name": "Tests Failed",
        "workflow_data": {"tests_passed": False},
        "expected_target": "Fix Code"
    }
]


print("\nA2 Research - Repeated Automatic Tracing Reliability Test")

total_runs = 0
passed_runs = 0
trace_ids = set()
trace_files = set()


for scenario in test_scenarios:

    print("\nScenario:", scenario["name"])

    scenario_results = []

    for run_number in range(1, 11):

        # Route and automatically save a JSON trace
        output = route_and_save_trace(
            contracts=contracts,
            current_node="Check Tests",
            workflow_data=scenario["workflow_data"]
        )

        routing_result = output["routing_result"]
        trace_id = output["trace_id"]
        trace_file = Path(output["trace_file"])

        # Verify the deterministic routing decision
        assert routing_result["status"] == "ROUTED"
        assert routing_result["next_node"] == scenario["expected_target"]
        assert len(routing_result["matched_contracts"]) == 1

        # Verify that the trace file exists
        assert trace_file.is_file()

        # Load the saved JSON trace
        with open(trace_file, "r", encoding="utf-8") as file:
            saved_trace = json.load(file)

        # Verify the trace contents
        assert saved_trace["routing_status"] == "ROUTED"
        assert saved_trace["selected_next_node"] == scenario["expected_target"]
        assert saved_trace["workflow_data"] == scenario["workflow_data"]
        assert saved_trace["current_node"] == "Check Tests"
        assert saved_trace["trace_id"] == trace_id

        assert len(saved_trace["matched_contracts"]) == 1
        assert len(saved_trace["validation_results"]) == 2

        assert all(
            record["valid"]
            for record in saved_trace["validation_results"]
        )

        assert isinstance(saved_trace["decision_explanation"], str)
        assert saved_trace["decision_explanation"]

        # Verify that every execution has a unique trace
        assert trace_id not in trace_ids
        assert str(trace_file) not in trace_files

        trace_ids.add(trace_id)
        trace_files.add(str(trace_file))

        scenario_results.append(routing_result["next_node"])

        total_runs += 1
        passed_runs += 1

        print(
            "Run", run_number,
            "- Status:", routing_result["status"],
            "- Destination:", routing_result["next_node"],
            "- PASS"
        )

    # Verify that all 10 routing decisions were identical
    assert len(set(scenario_results)) == 1

    print("Scenario consistency: 10/10 PASS")


# Verify all 20 executions completed successfully
assert total_runs == 20
assert passed_runs == 20
assert len(trace_ids) == 20
assert len(trace_files) == 20


print("\n----------------------------------------")
print("REPEATED AUTOMATIC TRACING RESULTS")
print("----------------------------------------")
print("Total executions:", total_runs)
print("Passed executions:", passed_runs)
print("Unique trace IDs:", len(trace_ids))
print("Unique JSON trace files:", len(trace_files))
print("Routing consistency: 100% within each scenario")
print("Overall result: PASS")

print("\nAll repeated automatic tracing reliability tests passed!")
