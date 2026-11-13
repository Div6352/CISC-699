
# CISC 699 - Capstone II A2
# Direct LLM vs Structured Contract Routing Comparison

import time

from direct_llm_router import direct_llm_route
from contract_router import route_with_explanation


# Two predefined semantic contracts
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


test_cases = [
    ("Tests passed", {"tests_passed": True}, "Deploy Code"),
    ("Tests failed", {"tests_passed": False}, "Fix Code")
]


print("\nA2 Research - Routing Comparison")

for label, workflow_data, expected in test_cases:

    # Direct LLM routing
    start = time.perf_counter()
    direct_result = direct_llm_route(workflow_data)
    direct_time = time.perf_counter() - start

    # Deterministic semantic-contract routing
    start = time.perf_counter()
    structured_result = route_with_explanation(
        contracts,
        "Check Tests",
        workflow_data
    )
    structured_time = time.perf_counter() - start

    structured_node = structured_result["next_node"]

    print("\nScenario:", label)
    print("Expected:", expected)

    print("Direct LLM result:", direct_result)
    print("Direct LLM correct:", direct_result == expected)
    print("Direct LLM time (seconds):", round(direct_time, 6))

    print("Structured result:", structured_node)
    print("Structured correct:", structured_node == expected)
    print("Structured time (seconds):", round(structured_time, 6))

print("\nRouting comparison completed.")
