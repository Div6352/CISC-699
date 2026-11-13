
# CISC 699 - A2 Research Project
# Execution Trace Test

import json
from pathlib import Path

from contract_router import route_with_explanation
from execution_trace import (
    create_execution_trace,
    save_execution_trace
)


# Define two semantic contracts
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


# Define invalid workflow state
workflow_data = {}


# Execute deterministic routing
result = route_with_explanation(
    contracts,
    "Check Tests",
    workflow_data
)


# Create an execution trace
trace = create_execution_trace(
    "Check Tests",
    workflow_data,
    contracts,
    result
)


# Save the trace inside the project's docs folder
project_root = Path(__file__).resolve().parent.parent

trace_path = (
    project_root
    / "docs"
    / "execution_trace_example.json"
)

trace_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

save_execution_trace(trace, trace_path)


# Verify the saved trace
with trace_path.open("r", encoding="utf-8") as file:
    saved_trace = json.load(file)


assert saved_trace["current_node"] == "Check Tests"

assert saved_trace["routing_status"] == "INVALID_WORKFLOW_DATA"

assert saved_trace["selected_next_node"] is None

assert saved_trace["workflow_data"] == {}

assert len(saved_trace["evaluated_contracts"]) == 2

assert "timestamp" in saved_trace

assert saved_trace["decision_explanation"]

assert len(saved_trace["validation_results"]) == 2


print("\nA2 Research - Execution Trace Test")

print("Routing status:", saved_trace["routing_status"])

print("Selected node:", saved_trace["selected_next_node"])

print("Workflow data:", saved_trace["workflow_data"])

print("Trace saved to:", trace_path)

print("Execution trace test passed!")
