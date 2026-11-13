

from ollama_interpreter import interpret_with_ollama

sentence = "When every test succeeds, deploy the application."

print("A2 Research - Ollama Interpretation Test")
print("Input:", sentence)

result = interpret_with_ollama(sentence)

print("AI Interpretation:", result)

expected = {
    "field": "tests_passed",
    "operator": "equals",
    "value": True
}

if result == expected:
    print("PASS: AI interpretation matches!")
else:
    print("NOT MATCHED: AI interpretation differs.")
