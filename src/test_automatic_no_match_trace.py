
# CISC 699 - Capstone II A2
# Automatic No-Match Routing Trace Test

import json
from pathlib import Path

from traced_contract_router import route_and_save_trace


# A valid contract that requires tests_passed = True
contracts = [
    {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    }
]


print("\nA2 Research - Automatic No-Match Routing Trace Test")

# The workflow state does not satisfy the contract.
# tests_passed = False, but the contract requires True.
output = route_and_save_trace(
    contracts=contracts,
    current_node="Check Tests",
    workflow_data={"tests_passed": False}
)

routing_result = output["routing_result"]
trace_file = Path(output["trace_file"])


# Verify that no destination was selected
assert routing_result["status"] == "NO_MATCH"
assert routing_result["next_node"] is None
assert len(routing_result["matched_contracts"]) == 0


# Verify that the JSON trace was saved
assert trace_file.is_file()


# Read the saved JSON trace
with open(trace_file, "r", encoding="utf-8") as file:
    saved_trace = json.load(file)


# Verify the trace contents
assert saved_trace["routing_status"] == "NO_MATCH"
assert saved_trace["selected_next_node"] is None
assert len(saved_trace["matched_contracts"]) == 0

# Verify the supplied contract was valid
assert len(saved_trace["validation_results"]) == 1
assert saved_trace["validation_results"][0]["valid"] is True

# Verify the unique trace identifier
assert saved_trace["trace_id"] == output["trace_id"]

# Verify the explanation
assert isinstance(saved_trace["decision_explanation"], str)
assert "No contracts matched" in saved_trace["decision_explanation"]


print("\nRouting status:", routing_result["status"])
print("Selected next node:", routing_result["next_node"])
print("Matching contracts:", len(routing_result["matched_contracts"]))
print("Trace saved:", trace_file.name)
print("Result: PASS")

print("\nAll automatic no-match routing trace tests passed!")
