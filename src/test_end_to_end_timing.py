

# CISC 699 - Capstone II A2
# Structured Workflow End-to-End Timing Experiment

import time

import contract_router

from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract


# Natural-language workflow edges
edges = [
    {
        "edge_id": "E1",
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": "If all software tests have passed, proceed to deployment."
    },
    {
        "edge_id": "E2",
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": "If any software test has failed, return to fixing the code."
    }
]


def build_structured_contracts():
    contracts = []

    for edge in edges:

        # Interpret natural-language condition using Ollama
        condition = interpret_with_structured_ollama(
            edge["condition"]
        )

        if condition is None:
            raise ValueError(
                f"Could not interpret edge {edge['edge_id']}"
            )

        # Build structured semantic contract
        contract = {
            "edge_id": edge["edge_id"],
            "source": edge["source"],
            "target": edge["target"],
            "condition": condition
        }

        # Validate the generated contract
        if not validate_contract(contract):
            raise ValueError(
                f"Invalid contract for edge {edge['edge_id']}"
            )

        contracts.append(contract)

    return contracts


print("\nA2 Research - End-to-End Timing Experiment")


# Step 1: Measure Ollama interpretation and contract construction
start = time.perf_counter()

contracts = build_structured_contracts()

construction_time = time.perf_counter() - start

print(
    "Contract construction time (seconds):",
    round(construction_time, 6)
)


# Step 2: Measure deterministic routing
test_cases = [
    ("Tests passed", {"tests_passed": True}, "Deploy Code"),
    ("Tests failed", {"tests_passed": False}, "Fix Code")
]

routing_start = time.perf_counter()

for label, workflow_data, expected in test_cases:

    result = contract_router.route_with_explanation(
        contracts,
        "Check Tests",
        workflow_data
    )

    print("\nScenario:", label)
    print("Expected:", expected)
    print("Actual:", result["next_node"])

    assert result["status"] == "ROUTED", (
        f"Unexpected routing status: {result['status']}"
    )

    assert result["next_node"] == expected, (
        f"Expected {expected}, got {result['next_node']}"
    )


routing_time = time.perf_counter() - routing_start


# Step 3: Calculate total measured time
total_time = construction_time + routing_time

print(
    "\nContract construction time:",
    round(construction_time, 6),
    "seconds"
)

print(
    "Routing time for both scenarios:",
    round(routing_time, 6),
    "seconds"
)

print(
    "Total measured time:",
    round(total_time, 6),
    "seconds"
)

print("\nEnd-to-end timing experiment passed!")
