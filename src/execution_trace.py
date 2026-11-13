
# CISC 699 - A2 Research Project
# Execution Trace Recording for Deterministic Workflow Routing
# Improved with Safer JSON File Saving

import json
import os
import tempfile

from datetime import datetime, timezone
from pathlib import Path


def create_execution_trace(
    current_node,
    workflow_data,
    contracts,
    routing_result
):
    """
    Create a structured record of a workflow routing decision.
    """

    trace = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "current_node": current_node,
        "workflow_data": workflow_data,
        "evaluated_contracts": contracts,
        "routing_status": routing_result["status"],
        "selected_next_node": routing_result["next_node"],
        "matched_contracts": routing_result.get(
            "matched_contracts", []
        ),
        "validation_results": routing_result.get(
            "validation_results", []
        ),
        "decision_explanation": routing_result.get(
            "decision_explanation"
        )
    }

    return trace


def save_execution_trace(trace, filename):
    """
    Save an execution trace using a temporary file.

    JSON serialization is completed before writing.

    The destination file is replaced only after the
    temporary file has been written successfully.
    """

    # Step 1: Convert the complete trace into JSON.
    # Unsupported objects raise TypeError before a file is created.
    json_content = json.dumps(
        trace,
        indent=4
    )

    # Step 2: Identify the destination file and directory.
    destination = Path(filename)
    destination_directory = destination.parent

    temporary_filename = None

    try:
        # Step 3: Create a temporary file in the same directory.
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=destination_directory,
            prefix=".trace_temp_",
            suffix=".json",
            delete=False
        ) as temporary_file:

            temporary_filename = temporary_file.name

            # Step 4: Write the complete JSON content.
            temporary_file.write(json_content)

            # Flush the file contents before replacement.
            temporary_file.flush()
            os.fsync(temporary_file.fileno())

        # Step 5: Replace the destination only after writing succeeds.
        os.replace(
            temporary_filename,
            destination
        )

        temporary_filename = None

    finally:
        # Step 6: Remove any remaining temporary file
        # if writing or replacement failed.
        if (
            temporary_filename is not None
            and os.path.exists(temporary_filename)
        ):
            os.remove(temporary_filename)

    return filename
