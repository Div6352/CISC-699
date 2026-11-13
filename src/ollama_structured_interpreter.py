
# CISC 699 - A2 Research Project
# Structured-Output Ollama Interpreter

import json
import urllib.request


def interpret_with_structured_ollama(text):
    schema = {
        "type": "object",
        "properties": {
            "field": {
                "type": "string",
                "enum": ["tests_passed"]
            },
            "operator": {
                "type": "string",
                "enum": ["equals"]
            },
            "value": {
                "type": "boolean"
            }
        },
        "required": ["field", "operator", "value"],
        "additionalProperties": False
    }

    prompt = f"""
Interpret this workflow condition:

{text}

If all tests must pass, value is true.
If any test fails, value is false.

Return only the JSON object required by the schema.
"""

    request_data = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "format": schema,
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
    print("RAW STRUCTURED RESPONSE:", repr(raw_response))

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
