



# CISC 699 - A2 Research Project
# Local LLM Natural-Language Interpreter

import json
import urllib.request


def interpret_with_ollama(text):
    prompt = f"""
You are a workflow condition interpreter.

Determine whether the sentence describes:
- ALL tests passing
- ANY test failing

Rules:
1. If the condition requires all tests to pass,
   set value to true.

2. If the condition describes one or more tests
   failing, set value to false.

3. Pay attention to words like:
   "failed", "fails", "failures", and "not".

Examples:

Sentence: "If all tests pass, deploy."
Output: {{"field":"tests_passed","operator":"equals","value":true}}

Sentence: "If any test fails, fix the code."
Output: {{"field":"tests_passed","operator":"equals","value":false}}

Now interpret this sentence:

{text}

Return ONLY a JSON object with these keys:
"field", "operator", "value"

Use:
field = "tests_passed"
operator = "equals"
value = true or false
"""

    request_data = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "format": "json",
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(request_data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        result = json.load(response)

    raw_response = result.get("response", "")

    print("RAW OLLAMA RESPONSE:", repr(raw_response))

    try:
        condition = json.loads(raw_response)
    except (json.JSONDecodeError, TypeError):
        return None

    if not isinstance(condition, dict):
        return None

    if (
        set(condition.keys()) != {"field", "operator", "value"}
        or condition["field"] != "tests_passed"
        or condition["operator"] != "equals"
        or type(condition["value"]) is not bool
    ):
      return None 

    return condition
