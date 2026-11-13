
# CISC 699 - Capstone II A2
# Automatic Ambiguous Routing Trace Test

import json
from pathlib import Path

from traced_contract_router import route_and_save_trace


# Two valid contracts that both match tests_passed = True
ambiguous_contracts = [
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
        "target": "Review Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }
]


print("\nA2 Research - Automatic Ambiguous Routing Trace Test")

# Execute routing and automatically save the trace
output = route_and_save_trace(
    contracts=ambiguous_contracts,
    current_node="Check Tests",
    workflow_data={"tests_passed": True}
)

routing_result = output["routing_result"]
trace_file = Path(output["trace_file"])

# Verify that ambiguous routing is rejected
assert routing_result["status"] == "AMBIGUOUS"
assert routing_result["next_node"] is None
assert len(routing_result["matched_contracts"]) == 2

# Verify that the JSON trace was created
assert trace_file.is_file()

# Load the saved trace
with open(trace_file, "r", encoding="utf-8") as file:
    saved_trace = json.load(file)

# Verify the saved trace contents
assert saved_trace["routing_status"] == "AMBIGUOUS"
assert saved_trace["selected_next_node"] is None
assert len(saved_trace["matched_contracts"]) == 2

assert saved_trace["trace_id"] == output["trace_id"]
assert len(saved_trace["validation_results"]) == 2
assert all(
    record["valid"]
    for record in saved_trace["validation_results"]
)

assert isinstance(saved_trace["decision_explanation"], str)
assert "Multiple contracts matched" in saved_trace["decision_explanation"]

print("\nRouting status:", routing_result["status"])
print("Selected next node:", routing_result["next_node"])
print("Matching contracts:", len(routing_result["matched_contracts"]))
print("Trace saved:", trace_file.name)
print("Result: PASS")

print("\nAll automatic ambiguous routing trace tests passed!")
