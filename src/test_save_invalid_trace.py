
# CISC 699 - Capstone II A2
# Save Invalid Contract Execution Trace

from pathlib import Path

from contract_router import route_with_explanation
from execution_trace import (
    create_execution_trace,
    save_execution_trace
)


# Invalid contract: unsupported condition field
invalid_contract = {
    "source": "Check Tests",
    "target": "Deploy Code",
    "condition": {
        "field": "unknown_field",
        "operator": "equals",
        "value": True
    }
}

contracts = [invalid_contract]
workflow_data = {"tests_passed": True}
current_node = "Check Tests"

print("\nA2 Research - Save Invalid Contract Trace")

# Attempt routing
result = route_with_explanation(
    contracts,
    current_node,
    workflow_data
)

# Verify that invalid contracts cannot select a destination
assert result["status"] == "INVALID_CONTRACT"
assert result["next_node"] is None
assert result["matched_contracts"] == []

# Verify that the failed validation is recorded
assert len(result["validation_results"]) == 1
assert result["validation_results"][0]["valid"] is False

print("Invalid contract rejected: PASS")
print("Failed validation recorded: PASS")

# Create the execution trace
trace = create_execution_trace(
    current_node,
    workflow_data,
    contracts,
    result
)

assert trace["routing_status"] == "INVALID_CONTRACT"
assert trace["selected_next_node"] is None

# Save the trace inside the project's docs folder
project_root = Path(__file__).resolve().parent.parent
docs_folder = project_root / "docs"
docs_folder.mkdir(exist_ok=True)

output_file = docs_folder / "invalid_contract_trace.json"

save_execution_trace(trace, str(output_file))

# Confirm the JSON file exists
assert output_file.is_file()

print("Execution trace saved: PASS")
print("File:", output_file)
print("\nAll invalid contract trace tests passed!")
