
# CISC 699 - Capstone II A2
# Unexpected Execution Tracing Exception Test

import tempfile
from pathlib import Path
from unittest.mock import patch

from traced_contract_router import route_and_save_trace


# Valid semantic contract
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


print("\nA2 Research - Unexpected Tracing Exception Test")

with tempfile.TemporaryDirectory() as temporary_directory:

    trace_folder = Path(temporary_directory) / "execution_traces"

    # Simulate an unexpected failure during trace creation.
    with patch(
        "traced_contract_router.create_execution_trace",
        side_effect=RuntimeError("Simulated trace creation failure")
    ):

        error_detected = False

        try:
            route_and_save_trace(
                contracts=contracts,
                current_node="Check Tests",
                workflow_data={"tests_passed": True},
                output_folder=trace_folder
            )

        except RuntimeError as error:
            error_detected = True

            assert str(error) == "Simulated trace creation failure"

            print("\nExpected exception detected.")
            print("Exception type:", type(error).__name__)
            print("Exception message:", str(error))

    # Verify that the exception was propagated.
    assert error_detected

    # Verify that no JSON trace was saved.
    trace_files = (
        list(trace_folder.glob("*.json"))
        if trace_folder.exists()
        else []
    )

    assert len(trace_files) == 0

    print("Unexpected exception propagated: PASS")
    print("No JSON trace saved after failure: PASS")


print("\nOverall result: PASS")
print("All unexpected tracing exception tests passed!")
