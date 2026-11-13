
# CISC 699 - A2 Research Project
# Deterministic Contract Evaluation Test

from contract_evaluator import evaluate_contract
from semantic_contract import (
    semantic_contract,
    semantic_contract_E02
)

print("\nA2 Research - Contract Evaluation Test")

# Define workflow data
workflow_data = {"tests_passed": True}

# Evaluate E01
result1 = evaluate_contract(
    semantic_contract,
    workflow_data
)

print("E01 evaluation:", result1)

# Evaluate E02
result2 = evaluate_contract(
    semantic_contract_E02,
    workflow_data
)

print("E02 evaluation:", result2)

# Verify expected results
assert result1 is True
assert result2 is False

print("Both contract evaluation tests passed!")
print("Failed-test scenario passed!")

# Test deterministic evaluation repeatability

print("\nTesting evaluation repeatability...")

repeat_results = []

for run in range(10):
    result = evaluate_contract(
        semantic_contract,
        {"tests_passed": True}
    )

    repeat_results.append(result)

    print("Run", run + 1, ":", result)

# Verify all 10 results are identical
assert len(set(repeat_results)) == 1

# Verify the repeated result matches expectation
assert repeat_results[0] is True

print("Repeatability test passed: 10 identical results!")

