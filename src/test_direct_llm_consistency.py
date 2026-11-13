
# CISC 699 - Capstone II A2
# Direct LLM Routing Consistency Experiment

from direct_llm_router import direct_llm_route


REPEATS = 10

test_cases = [
    ("Tests passed", {"tests_passed": True}, "Deploy Code"),
    ("Tests failed", {"tests_passed": False}, "Fix Code"),
]

print("\nA2 Research - Direct LLM Consistency Experiment")

for label, workflow_data, expected in test_cases:
    responses = []

    print(f"\nScenario: {label}")

    for run_number in range(1, REPEATS + 1):
        result = direct_llm_route(workflow_data)
        responses.append(result)

        print(f"Run {run_number}: {result}")

    correct_count = sum(
        response == expected for response in responses
    )

    unique_responses = set(responses)

    print("Expected:", expected)
    print("Correct runs:", f"{correct_count}/{REPEATS}")
    print("Unique responses:", sorted(unique_responses))
    print("All runs identical:", len(unique_responses) == 1)

print("\nDirect LLM consistency experiment completed.")
