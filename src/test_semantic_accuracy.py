
# CISC 699 - A2 Research Project
# Complete Semantic-Contract Accuracy Evaluation

from evaluation_dataset import evaluation_cases
from reference_contracts import reference_contracts
from nl_contract_builder import build_contract

correct = 0
total = 0
abstentions = 0

print("\nA2 Research - Semantic Contract Accuracy")

for case in evaluation_cases:

    case_id = case["case_id"]

    # Evaluate only cases with reference contracts
    if case_id not in reference_contracts:
        continue

    total += 1

    expected = reference_contracts[case_id]

    edge = {
        "edge_id": case_id,
        "source": expected["source"],
        "target": expected["target"],
        "condition": case["text"]
    }

    generated = build_contract(edge)

    if generated is None:
        abstentions += 1
        is_correct = False
    else:
        is_correct = (
            generated["source"] == expected["source"]
            and generated["target"] == expected["target"]
            and generated["condition"] == expected["condition"]
        )

    if is_correct:
        correct += 1

    print(
        case_id,
        "| Correct:", is_correct,
        "| Abstained:", generated is None
    )

accuracy = correct / total if total else 0
abstention_rate = abstentions / total if total else 0

print("\nCorrect:", correct, "out of", total)
print("Semantic accuracy:", f"{accuracy:.1%}")
print("Abstention rate:", f"{abstention_rate:.1%}")
