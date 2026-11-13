
# CISC 699 - A2 Research Project
# Ollama Natural-Language Interpretation Evaluation

from evaluation_dataset import evaluation_cases
from ollama_interpreter import interpret_with_ollama

total = len(evaluation_cases)
correct = 0
abstained = 0

print("\nA2 Research - Ollama Accuracy Evaluation")
print("=" * 50)

for case in evaluation_cases:
    case_id = case["case_id"]
    sentence = case["text"]
    expected = case["expected_value"]

    result = interpret_with_ollama(sentence)

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
            status = "INCORRECT"

    print(f"\nCase: {case_id}")
    print(f"Sentence: {sentence}")
    print(f"Expected: {expected}")
    print(f"Predicted: {predicted}")
    print(f"Result: {status}")

accuracy = (correct / total) * 100
abstention_rate = (abstained / total) * 100

print("\n" + "=" * 50)
print("OLLAMA EVALUATION SUMMARY")
print(f"Total cases: {total}")
print(f"Correct: {correct}")
print(f"Abstained: {abstained}")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Abstention rate: {abstention_rate:.1f}%")
