
# CISC 699 - A2 Research Project
# Structured Ollama Accuracy Evaluation

from evaluation_dataset import evaluation_cases
from ollama_structured_interpreter import interpret_with_structured_ollama

total = len(evaluation_cases)
correct = 0
incorrect = 0
abstained = 0

print("\nA2 Research - Structured Ollama Evaluation")
print("=" * 50)

for case in evaluation_cases:
    case_id = case["case_id"]
    sentence = case["text"]
    expected = case["expected_value"]

    result = interpret_with_structured_ollama(sentence)

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

accuracy = (correct / total) * 100
abstention_rate = (abstained / total) * 100

print("\n" + "=" * 50)
print("STRUCTURED OLLAMA EVALUATION SUMMARY")
print(f"Total cases: {total}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Abstained: {abstained}")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Abstention rate: {abstention_rate:.1f}%")
