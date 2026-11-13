
# CISC 699 - Capstone II A2 Research
# Traced Deterministic Contract Router
# With Graph Transition Enforcement

import uuid
from pathlib import Path

from contract_router import route_with_explanation
from execution_trace import (
    create_execution_trace,
    save_execution_trace
)
from graph import is_permitted_transition


def route_and_save_trace(
    contracts,
    current_node,
    workflow_data,
    output_folder="docs/execution_traces"
):
    """
    Route workflow data using semantic contracts,
    enforce permitted graph transitions,
    and save a complete execution trace.

    Unexpected tracing and saving exceptions propagate
    to the caller.
    """

    # Step 1: Perform deterministic contract routing.
    routing_result = route_with_explanation(
        contracts,
        current_node,
        workflow_data
    )

    # Step 2: Enforce graph permissions before recording
    # the final routing decision.
    if routing_result["status"] == "ROUTED":
        next_node = routing_result["next_node"]

        if not is_permitted_transition(
            current_node,
            next_node
        ):
            routing_result = {
                **routing_result,
                "status": "INVALID_GRAPH_TRANSITION",
                "next_node": None,
                "decision_explanation": (
                    "Routing was rejected because the "
                    "selected transition is not permitted "
                    "by the workflow graph."
                )
            }

    # Step 3: Create a unique trace identifier.
    trace_id = uuid.uuid4().hex

    # Step 4: Create the execution trace.
    trace = create_execution_trace(
        current_node,
        workflow_data,
        contracts,
        routing_result
    )

    trace["trace_id"] = trace_id

    # Step 5: Create the destination directory.
    destination_folder = Path(output_folder)
    destination_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # Step 6: Generate a unique JSON filename.
    trace_file = destination_folder / (
        f"trace_{trace_id}.json"
    )

    # Step 7: Save the complete execution trace.
    save_execution_trace(
        trace,
        str(trace_file)
    )

    # Step 8: Return routing and trace information.
    return {
        "routing_result": routing_result,
        "trace_id": trace_id,
        "trace_file": str(trace_file),
        "trace": trace
    }
