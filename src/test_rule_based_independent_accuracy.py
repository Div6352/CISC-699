
# CISC 699 - Capstone II A2
# Rule-Based Independent Accuracy Evaluation

from independent_evaluation_dataset import independent_evaluation_cases
from nl_interpreter import interpret_condition

total = len(independent_evaluation_cases)
correct = 0
incorrect = 0
abstained = 0

print("\nA2 Research - Rule-Based Independent Evaluation")
print("=" * 50)

for case in independent_evaluation_cases:
    case_id = case["case_id"]
    sentence = case["text"]
    expected = case["expected_value"]

    result = interpret_condition(sentence)

    if result is None:
        predicted = None
        abstained += 1
        status = "ABSTAIN"

    else:
        predicted = result["value"]

        if predicted == expected:
            correct += 1
            status = "CORRECT"
        else:
            incorrect += 1
            status = "INCORRECT"

    print(f"\nCase: {case_id}")
    print(f"Expected: {expected}")
    print(f"Predicted: {predicted}")
    print(f"Result: {status}")

accuracy = correct / total * 100
abstention_rate = abstained / total * 100

print("\n" + "=" * 50)
print("RULE-BASED EVALUATION SUMMARY")
print("Total cases:", total)
print("Correct:", correct)
print("Incorrect:", incorrect)
print("Abstained:", abstained)
print(f"Accuracy: {accuracy:.1f}%")
print(f"Abstention rate: {abstention_rate:.1f}%")
