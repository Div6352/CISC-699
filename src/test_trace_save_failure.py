
# CISC 699 - Capstone II A2
# Automatic Execution Trace Save Failure Test

import tempfile
from pathlib import Path

from traced_contract_router import route_and_save_trace


# A valid semantic contract
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


print("\nA2 Research - Trace Save Failure Test")

# Create a temporary directory for this test.
# No existing research files will be modified.
with tempfile.TemporaryDirectory() as temporary_directory:

    temporary_path = Path(temporary_directory)

    # Create a regular file, not a folder.
    blocking_file = temporary_path / "not_a_directory.txt"
    blocking_file.write_text(
        "This is a regular file.",
        encoding="utf-8"
    )

    print("\nSimulating an invalid trace output location.")

    error_detected = False

    try:
        # The wrapper expects output_folder to be a directory.
        # Supplying a regular file should cause an OSError.
        route_and_save_trace(
            contracts=contracts,
            current_node="Check Tests",
            workflow_data={"tests_passed": True},
            output_folder=blocking_file
        )

    except OSError as error:
        error_detected = True
        print("Expected file-system error detected.")
        print("Error type:", type(error).__name__)

    # Verify that the failure was not silently ignored.
    assert error_detected, (
        "Expected an OSError, but no error was raised."
    )

    # Verify that the original blocking file was not changed.
    assert blocking_file.is_file()
    assert blocking_file.read_text(
        encoding="utf-8"
    ) == "This is a regular file."

    print("Existing test file preserved: PASS")


print("\nTrace save failure detected: PASS")
print("Overall result: PASS")
print("\nAll trace save failure tests passed!")
