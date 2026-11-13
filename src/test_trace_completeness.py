
# CISC 699 - Capstone II A2
# Execution Trace Completeness Test

from contract_router import route_with_explanation
from execution_trace import create_execution_trace


# Define semantic contracts
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


# Define workflow state
workflow_data = {"tests_passed": True}


# Execute deterministic routing
result = route_with_explanation(
    contracts,
    "Check Tests",
    workflow_data
)


# Generate execution trace
trace = create_execution_trace(
    "Check Tests",
    workflow_data,
    contracts,
    result
)


# Verify all required trace fields
required_fields = [
    "timestamp",
    "current_node",
    "workflow_data",
    "evaluated_contracts",
    "routing_status",
    "selected_next_node",
    "matched_contracts",
    "validation_results",
    "decision_explanation"
]


print("\nA2 Research - Execution Trace Completeness Test")

for field in required_fields:
    present = field in trace

    print(f"{field}: {'PRESENT' if present else 'MISSING'}")

    assert present, f"Missing required trace field: {field}"


# Verify routing decision
assert trace["routing_status"] == "ROUTED"
assert trace["selected_next_node"] == "Deploy Code"

print("\nRouting decision: PASS")


# Verify matched contract
assert len(trace["matched_contracts"]) == 1
assert trace["matched_contracts"][0]["target"] == "Deploy Code"
assert trace["matched_contracts"][0]["condition"]["value"] is True

print("Matched contract correctly recorded: PASS")


# Verify validation results
validation_results = trace["validation_results"]

assert len(validation_results) == 2

assert all(
    record["valid"] is True
    for record in validation_results
)

assert validation_results[0]["source"] == "Check Tests"
assert validation_results[0]["target"] == "Deploy Code"

assert validation_results[1]["source"] == "Check Tests"
assert validation_results[1]["target"] == "Fix Code"

print("Validation results correctly recorded: PASS")


# Verify decision explanation
explanation = trace["decision_explanation"]

assert isinstance(explanation, str)
assert "Exactly one contract matched" in explanation

print("Decision explanation correctly recorded: PASS")


print("\nAll execution trace completeness tests passed!")
