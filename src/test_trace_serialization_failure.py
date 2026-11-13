
# CISC 699 - Capstone II A2
# Improved JSON Serialization Failure Test
# Verify that failed serialization leaves no incomplete trace file

import json
import tempfile
from pathlib import Path

from traced_contract_router import route_and_save_trace
from execution_trace import save_execution_trace


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


print("\nA2 Research - Improved JSON Serialization Failure Test")

with tempfile.TemporaryDirectory() as temporary_directory:

    trace_folder = Path(temporary_directory) / "execution_traces"
    trace_folder.mkdir()

    # --------------------------------------------------
    # TEST 1: Invalid JSON data must not create a trace
    # --------------------------------------------------

    workflow_data = {
        "tests_passed": True,
        "extra_metadata": {"alpha", "beta"}
    }

    error_detected = False

    try:
        route_and_save_trace(
            contracts=contracts,
            current_node="Check Tests",
            workflow_data=workflow_data,
            output_folder=trace_folder
        )

    except TypeError as error:
        error_detected = True
        print("\nExpected serialization error detected.")
        print("Exception type:", type(error).__name__)
        print("Exception message:", str(error))

    assert error_detected, (
        "Expected a TypeError during JSON serialization."
    )

    trace_files = list(trace_folder.iterdir())

    assert len(trace_files) == 0, (
        "Serialization failure left an unexpected file behind."
    )

    print("No incomplete trace file created: PASS")
    print("Serialization error propagated: PASS")

    # --------------------------------------------------
    # TEST 2: Existing JSON must remain unchanged
    # --------------------------------------------------

    existing_file = trace_folder / "existing_trace.json"

    original_trace = {
        "routing_status": "ROUTED",
        "selected_next_node": "Deploy Code"
    }

    save_execution_trace(
        original_trace,
        str(existing_file)
    )

    original_contents = existing_file.read_text(
        encoding="utf-8"
    )

    invalid_trace = {
        "routing_status": "ROUTED",
        "unsupported_data": {"alpha", "beta"}
    }

    replacement_error_detected = False

    try:
        save_execution_trace(
            invalid_trace,
            str(existing_file)
        )

    except TypeError:
        replacement_error_detected = True

    assert replacement_error_detected, (
        "Expected replacement serialization to fail."
    )

    # Confirm that the original file is unchanged.
    assert existing_file.read_text(
        encoding="utf-8"
    ) == original_contents

    with open(existing_file, "r", encoding="utf-8") as file:
        saved_trace = json.load(file)

    assert saved_trace == original_trace

    # Confirm that no temporary files remain.
    remaining_files = list(trace_folder.iterdir())

    assert remaining_files == [existing_file], (
        "Unexpected temporary files remain after failure."
    )

    print("Existing JSON trace preserved: PASS")
    print("No temporary files left behind: PASS")


print("\nOverall result: PASS")
print("All improved JSON serialization failure tests passed!")
