
# CISC 699 - A2 Research Project
# Natural-Language Interpretation Accuracy Test

from evaluation_dataset import evaluation_cases
from nl_interpreter import interpret_condition

correct = 0
total = len(evaluation_cases)
abstentions = 0

print("\nA2 Research - Interpretation Accuracy")

for case in evaluation_cases:

    prediction = interpret_condition(case["text"])

    if prediction is None:
        predicted_value = None
        abstentions += 1
    else:
        predicted_value = prediction["value"]

    is_correct = (
        predicted_value is not None
        and predicted_value == case["expected_value"]
    )

    if is_correct:
        correct += 1

    print(
        case["case_id"],
        "| Expected:", case["expected_value"],
        "| Predicted:", predicted_value,
        "| Correct:", is_correct
    )

accuracy = correct / total
abstention_rate = abstentions / total

print("\nCorrect:", correct, "out of", total)
print("Accuracy:", f"{accuracy:.1%}")
print("Abstention rate:", f"{abstention_rate:.1%}")
