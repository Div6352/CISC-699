
# CISC 699 - A2 Research Project
# Natural-Language Interpreter Test

from nl_interpreter import interpret_condition

print("A2 Research - Natural-Language Interpreter Test")

# Test 1: Tests passed
result1 = interpret_condition(
    "If all software tests have passed, proceed to deployment."
)

print("Test 1:", result1)

assert result1 == {
    "field": "tests_passed",
    "operator": "equals",
    "value": True
}

# Test 2: Tests failed
result2 = interpret_condition(
    "If any software test has failed, return to fixing the code."
)

print("Test 2:", result2)

assert result2 == {
    "field": "tests_passed",
    "operator": "equals",
    "value": False
}

# Test 3: Unrecognized condition
result3 = interpret_condition(
    "Deploy whenever the weather is sunny."
)

print("Test 3:", result3)

assert result3 is None

print("All natural-language interpreter tests passed!")

# Test an unfamiliar paraphrase

print("\nTesting unfamiliar paraphrase...")

paraphrase = "When every test succeeds, deploy the application."

result4 = interpret_condition(paraphrase)

print("Paraphrase:", paraphrase)
print("Interpreter result:", result4)

# Current exact-match interpreter should reject it
assert result4 is None

print("Unfamiliar paraphrase test passed!")
