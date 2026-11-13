
# CISC 699 - Capstone II A2
# Direct LLM Routing Baseline

import json
import urllib.request


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def direct_llm_route(workflow_data):
    """
    Ask the LLM to select a workflow destination directly.
    No semantic contracts are used.
    """

    prompt = f"""
You are routing a software development workflow.

Current node: Check Tests
Workflow state: {json.dumps(workflow_data)}

Choose the next node using these rules:
- If tests_passed is true, choose Deploy Code.
- If tests_passed is false, choose Fix Code.
- If tests_passed is missing or invalid, choose NO_MATCH.

Return only one of these exact values:
Deploy Code
Fix Code
NO_MATCH
"""

    request_data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(request_data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        answer = result.get("response", "").strip()
        print("RAW LLM RESPONSE:", repr(answer))

        if answer in ("Deploy Code", "Fix Code", "NO_MATCH"):
            return answer

        return "INVALID_RESPONSE"

    except Exception as error:
        print("Ollama request failed:", error)
        return "LLM_ERROR"
