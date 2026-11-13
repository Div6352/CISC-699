
# CISC 699 - A2 Research Project
# Connected graph evaluator test

from graph import edges

from edge_evaluator import select_next_node, evaluate_edge


print("\nA2 Research - Connected Graph Test")

current_node = "Check Tests"

# Test the True path
result1 = select_next_node(edges, current_node, True)
print("Input True ->", result1)

# Test the False path
result2 = select_next_node(edges, current_node, False)
print("Input False ->", result2)

# Verify both paths
assert result1 == "Deploy Code"
assert result2 == "Fix Code"

print("Both routing tests passed!")

# Test unsupported edge condition

print("\nTesting unsupported condition...")

try:
    result = evaluate_edge("unknown_condition", True)
    print("Unexpected result:", result)

except ValueError as error:
    print("Condition rejected:", error)
