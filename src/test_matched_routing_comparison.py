
# CISC 699 - Capstone II A2
# Matched Direct LLM vs Structured Contract Routing Comparison

import json
import time
from pathlib import Path

from direct_llm_router import direct_llm_route
from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from contract_router import route_with_explanation


REPEATS = 5

EDGE_DESCRIPTIONS = [
    {
        "edge_id": "EDGE01",
        "source": "Check Tests",
        "target": "Deploy Code",
        "text": "If all software tests have passed, proceed to deployment."
    },
    {
        "edge_id": "EDGE02",
        "source": "Check Tests",
        "target": "Fix Code",
        "text": "If any software test has failed, return to fixing the code."
    }
]

TEST_CASES = [
    {
        "case_id": "MATCH01",
        "workflow_data": {"tests_passed": True},
        "expected": "Deploy Code"
    },
    {
        "case_id": "MATCH02",
        "workflow_data": {"tests_passed": False},
        "expected": "Fix Code"
    }
]


def build_contracts():
    contracts = []
    interpretation_times = []

    for edge in EDGE_DESCRIPTIONS:
        start = time.perf_counter()

        condition = interpret_with_structured_ollama(
            edge["text"]
        )

        elapsed = time.perf_counter() - start
        interpretation_times.append(elapsed)

        if condition is None:
            raise RuntimeError(
                f"Interpretation failed for {edge['edge_id']}"
            )

        contract = {
            "edge_id": edge["edge_id"],
            "source": edge["source"],
            "target": edge["target"],
            "condition": condition
        }

        if not validate_contract(contract):
            raise RuntimeError(
                f"Contract validation failed for {edge['edge_id']}"
            )

        contracts.append(contract)

    return contracts, interpretation_times


def run_experiment():
    print("\nA2 Research - Matched Routing Comparison")

    print("\nGenerating structured semantic contracts...")
    contracts, interpretation_times = build_contracts()

    records = []

    for case in TEST_CASES:
        print("\nScenario:", case["case_id"])

        for run_number in range(1, REPEATS + 1):
            workflow_data = case["workflow_data"]
            expected = case["expected"]

            direct_start = time.perf_counter()
            direct_result = direct_llm_route(workflow_data)
            direct_seconds = (
                time.perf_counter() - direct_start
            )

            structured_start = time.perf_counter()
            structured_result = route_with_explanation(
                contracts,
                "Check Tests",
                workflow_data
            )
            structured_seconds = (
                time.perf_counter() - structured_start
            )

            structured_node = structured_result["next_node"]

            record = {
                "case_id": case["case_id"],
                "run": run_number,
                "workflow_data": workflow_data,
                "expected": expected,
                "direct_result": direct_result,
                "direct_correct": direct_result == expected,
                "direct_seconds": direct_seconds,
                "structured_result": structured_node,
                "structured_status": structured_result["status"],
                "structured_correct": (
                    structured_result["status"] == "ROUTED"
                    and structured_node == expected
                ),
                "structured_seconds": structured_seconds
            }

            records.append(record)

            print(
                f"Run {run_number}: "
                f"direct={direct_result}, "
                f"structured={structured_node}"
            )

    total = len(records)

    direct_correct = sum(
        record["direct_correct"] for record in records
    )
    structured_correct = sum(
        record["structured_correct"] for record in records
    )

    summary = {
        "experiment": "Matched routing-stage comparison",
        "model": "llama3.2:3b",
        "temperature": 0,
        "repeats_per_scenario": REPEATS,
        "total_runs": total,
        "direct_correct": direct_correct,
        "structured_correct": structured_correct,
        "direct_accuracy": direct_correct / total,
        "structured_accuracy": structured_correct / total,
        "contract_interpretation_seconds": interpretation_times,
        "total_contract_interpretation_seconds": sum(
            interpretation_times
        ),
        "average_direct_seconds": sum(
            record["direct_seconds"] for record in records
        ) / total,
        "average_structured_routing_seconds": sum(
            record["structured_seconds"] for record in records
        ) / total,
        "limitations": [
            "Only two workflow states are tested.",
            "Contracts are generated once and reused.",
            "Direct LLM calls and deterministic routing "
            "represent different processing stages.",
            "The direct LLM prompt contains explicit routing rules.",
            "This is not a full end-to-end latency comparison."
        ]
    }

    output = {
        "edge_descriptions": EDGE_DESCRIPTIONS,
        "contracts": contracts,
        "summary": summary,
        "records": records
    }

    project_root = Path(__file__).resolve().parent.parent
    output_file = (
        project_root / "docs" /
        "matched_routing_comparison_results.json"
    )

    output_file.parent.mkdir(
        parents=True, exist_ok=True
    )

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    print("\nTotal runs:", total)
    print("Direct LLM correct:", f"{direct_correct}/{total}")
    print(
        "Structured routing correct:",
        f"{structured_correct}/{total}"
    )
    print("Results saved to:", output_file)
    print("\nMatched comparison completed!")


if __name__ == "__main__":
    run_experiment()
