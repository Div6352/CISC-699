
# CISC 699 - Capstone II A2 Research
# Prompt-Controlled Direct Natural-Language LLM Baseline

import json
import urllib.request


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def direct_nl_llm_route_controlled(
    edge_descriptions,
    current_node,
    workflow_data
):
    """
    Route directly from natural-language edge conditions.

    Uses explicit Boolean guidance matching the structured
    interpreter, but does not generate semantic contracts.
    """

    available_edges = [
        {
            "source": edge["source"],
            "target": edge["target"],
            "description": edge["text"]
        }
        for edge in edge_descriptions
        if edge["source"] == current_node
    ]

    if not available_edges:
        return "NO_MATCH"

    allowed_targets = {
        edge["target"]
        for edge in available_edges
    }

    prompt = f"""
You are executing a software development workflow.

Current node:
{current_node}

Workflow state:
{json.dumps(workflow_data)}

Available outgoing edges, described in natural language:
{json.dumps(available_edges, indent=2)}

Interpret the natural-language conditions using
the following Boolean guidance:

If all tests must pass, tests_passed is true.
If any test fails, tests_passed is false.

Choose the destination of the edge whose
natural-language condition is satisfied
by the workflow state.

If no edge condition is satisfied, return NO_MATCH.

Return ONLY the exact destination node name
or NO_MATCH.

Do not explain your answer.
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
        with urllib.request.urlopen(
            request,
            timeout=120
        ) as response:
            result = json.loads(
                response.read().decode("utf-8")
            )

        answer = result.get("response", "").strip()

        print(
            "RAW CONTROLLED DIRECT RESPONSE:",
            repr(answer)
        )

        if answer in allowed_targets or answer == "NO_MATCH":
            return answer

        return "INVALID_RESPONSE"

    except Exception as error:
        print(
            "Controlled direct routing request failed:",
            error
        )
        return "LLM_ERROR"
