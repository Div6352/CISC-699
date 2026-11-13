
# CISC 699 - A2 Research Project
# Basic Edge Condition Evaluator

def evaluate_edge(condition, tests_passed):

    if condition == "tests_passed == True":
        return tests_passed is True

    elif condition == "tests_passed == False":
        return tests_passed is False

    else:
        raise ValueError("Unsupported edge condition")
# Test the edge evaluator

print("A2 Research - Edge Evaluator Test")

result1 = evaluate_edge("tests_passed == True", True)
print("Test 1:", result1)

result2 = evaluate_edge("tests_passed == False", True)
print("Test 2:", result2)

result3 = evaluate_edge("tests_passed == False", False)
print("Test 3:", result3)

# Select the next node from graph edges

def select_next_node(edges, current_node, tests_passed):
    for edge in edges:
        if edge["source"] == current_node:
            if evaluate_edge(edge["condition"], tests_passed):
                return edge["target"]

    return None
