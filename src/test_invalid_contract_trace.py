
# CISC 699 - Capstone II A2
# Invalid Contract Trace Baseline Test

from contract_router import route_with_explanation
from execution_trace import create_execution_trace


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


print("\nA2 Research - Invalid Contract Trace Baseline")

contracts = [invalid_contract]
workflow_data = {"tests_passed": True}

# Attempt to route using an invalid contract
try:
    result = route_with_explanation(
        contracts,
        "Check Tests",
        workflow_data
    )

except ValueError as error:
    print("Invalid contract rejected: PASS")
    print("Error:", error)
    print("Routing result returned: NO")
    print("Execution trace created: NO")

else:
    # This branch runs only if the router returns normally.
    trace = create_execution_trace(
        "Check Tests",
        workflow_data,
        contracts,
        result
    )

    print("Routing status:", trace["routing_status"])
    print("Validation results:", trace["validation_results"])

    assert trace["selected_next_node"] is None

    failed_records = [
        record
        for record in trace["validation_results"]
        if record["valid"] is False
    ]

    assert len(failed_records) >= 1
    print("Failed validation recorded: PASS")


print("\nInvalid contract trace baseline completed!")
