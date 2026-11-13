
# CISC 699 - Capstone II A2
# Direct LLM Routing Baseline Evaluation

from direct_llm_router import direct_llm_route


print("\nA2 Research - Direct LLM Routing Evaluation")
print("=" * 55)

test_cases = [
    (
        "Tests passed",
        {"tests_passed": True},
        "Deploy Code"
    ),
    (
        "Tests failed",
        {"tests_passed": False},
        "Fix Code"
    )
]

correct = 0
incorrect = 0

for label, workflow_data, expected in test_cases:

    result = direct_llm_route(workflow_data)

    is_correct = result == expected

    if is_correct:
        correct += 1
        status = "CORRECT"
    else:
        incorrect += 1
        status = "INCORRECT"

    print("\nScenario:", label)
    print("Expected:", expected)
    print("Actual:", result)
    print("Result:", status)

total = len(test_cases)
accuracy = (correct / total) * 100

print("\n" + "=" * 55)
print("DIRECT LLM BASELINE SUMMARY")
print("Total scenarios:", total)
print("Correct decisions:", correct)
print("Incorrect decisions:", incorrect)
print(f"Accuracy: {accuracy:.1f}%")

print("\nBaseline evaluation completed.")
print("Incorrect decisions are retained as research findings.")
