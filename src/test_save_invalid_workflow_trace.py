
# CISC 699 - Capstone II A2
# Save Invalid Workflow Data Execution Trace

import json
from pathlib import Path

from contract_router import route_with_explanation
from execution_trace import (
    create_execution_trace,
    save_execution_trace
)


# Valid semantic contracts
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


# Invalid workflow data: required field is missing
workflow_data = {}
current_node = "Check Tests"

print("\nA2 Research - Invalid Workflow Data Trace Test")


# Step 1: Attempt routing
result = route_with_explanation(
    contracts,
    current_node,
    workflow_data
)


# Step 2: Verify routing was safely stopped
assert result["status"] == "INVALID_WORKFLOW_DATA"
assert result["next_node"] is None
assert result["matched_contracts"] == []

print("Invalid workflow data detected: PASS")
print("Unsafe routing prevented: PASS")


# Step 3: Verify contract validation succeeded
assert len(result["validation_results"]) == 2
assert all(
    record["valid"] is True
    for record in result["validation_results"]
)

print("Valid contracts correctly identified: PASS")


# Step 4: Create execution trace
trace = create_execution_trace(
    current_node,
    workflow_data,
    contracts,
    result
)

assert trace["routing_status"] == "INVALID_WORKFLOW_DATA"
assert trace["selected_next_node"] is None
assert "tests_passed" in trace["decision_explanation"]

print("Failure explanation recorded: PASS")


# Step 5: Save trace to JSON
project_root = Path(__file__).resolve().parent.parent
docs_folder = project_root / "docs"
docs_folder.mkdir(parents=True, exist_ok=True)

output_file = docs_folder / "invalid_workflow_data_trace.json"

save_execution_trace(trace, str(output_file))

assert output_file.is_file()

print("Execution trace saved: PASS")


# Step 6: Read saved JSON and verify its contents
with open(output_file, "r", encoding="utf-8") as file:
    saved_trace = json.load(file)

assert saved_trace["routing_status"] == "INVALID_WORKFLOW_DATA"
assert saved_trace["selected_next_node"] is None
assert saved_trace["workflow_data"] == {}
assert len(saved_trace["validation_results"]) == 2

print("Saved JSON contents verified: PASS")

print("\nFile:", output_file)
print("\nAll invalid workflow data trace tests passed!")
