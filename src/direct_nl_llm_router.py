
# CISC 699 - Capstone II A2 Research
# Direct Natural-Language LLM Routing Baseline

import json
import urllib.request


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def direct_nl_llm_route(
    edge_descriptions,
    current_node,
    workflow_data
):
    """
    Select the next workflow node directly from
    natural-language edge descriptions.

    No structured semantic contracts are generated.
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

        print("RAW DIRECT NL RESPONSE:", repr(answer))

        if answer in allowed_targets or answer == "NO_MATCH":
            return answer

        return "INVALID_RESPONSE"

    except Exception as error:
        print("Direct NL routing request failed:", error)
        return "LLM_ERROR"
