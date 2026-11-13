
# CISC 699 - Capstone II A2 Research
# Prompt-Controlled Three-Method Routing Comparison

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
from direct_nl_llm_router import direct_nl_llm_route
from direct_nl_llm_router_controlled import direct_nl_llm_route_controlled
from test_repeated_matched_independent_nl import (
    make_edges,
    build_contracts,
    CURRENT_NODE,
)
from contract_router import route_with_explanation
from graph import is_permitted_transition


REPEATS = 3

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "prompt_controlled_comparison_results.json"
)


def timed_direct_call(function, edges, workflow_data):
    start = time.perf_counter()
    error = None

    try:
        result = function(
            edges,
            CURRENT_NODE,
            workflow_data,
        )
    except Exception as exc:
        result = "LLM_ERROR"
        error = f"{type(exc).__name__}: {exc}"

    return {
        "result": result,
        "seconds": time.perf_counter() - start,
        "error": error,
        "llm_calls": 1,
    }


def run_structured(edges, workflow_data):
    contracts, interpretations, construction_seconds = (
        build_contracts(edges)
    )

    start = time.perf_counter()

    routing = route_with_explanation(
        contracts,
        CURRENT_NODE,
        workflow_data,
    )

    routing_seconds = time.perf_counter() - start
    status = routing["status"]
    target = routing["next_node"]

    if (
        status == "ROUTED"
        and not is_permitted_transition(CURRENT_NODE, target)
    ):
        status = "INVALID_GRAPH_TRANSITION"
        target = None

    return {
        "status": status,
        "result": target,
        "construction_seconds": construction_seconds,
        "routing_seconds": routing_seconds,
        "seconds": construction_seconds + routing_seconds,
        "interpretations": interpretations,
        "llm_calls": 2,
    }


def calculate_summary(records):
    methods = [
        "original_direct",
        "controlled_direct",
        "structured",
    ]

    summary = {}

    for method in methods:
        correct = sum(
            record[method]["correct"]
            for record in records
        )

        total_seconds = sum(
            record[method]["seconds"]
            for record in records
        )

        total_calls = sum(
            record[method]["llm_calls"]
            for record in records
        )

        stable_cases = 0

        for case in independent_evaluation_cases:
            case_records = [
                record
                for record in records
                if record["case_id"] == case["case_id"]
            ]

            observed = [
                (
                    record[method].get("status"),
                    record[method]["result"],
                )
                for record in case_records
            ]

            if len(set(observed)) == 1:
                stable_cases += 1

        summary[method] = {
            "correct": correct,
            "total": len(records),
            "accuracy": (
                correct / len(records)
                if records else 0.0
            ),
            "stable_cases": stable_cases,
            "total_cases": len(independent_evaluation_cases),
            "total_seconds": total_seconds,
            "average_seconds_per_decision": (
                total_seconds / len(records)
                if records else 0.0
            ),
            "total_llm_calls": total_calls,
        }

    return summary


def run_experiment():
    records = []

    print("\nPROMPT-CONTROLLED ROUTING COMPARISON")
    print("=" * 65)

    for case in independent_evaluation_cases:
        edges = make_edges(case)

        workflow_data = {
            "tests_passed": case["expected_value"]
        }

        expected_target = (
            "Deploy Code"
            if case["expected_value"] is True
            else "Fix Code"
        )

        for repetition in range(1, REPEATS + 1):
            print(
                f"\n{case['case_id']} "
                f"repetition {repetition}/{REPEATS}"
            )

            original = timed_direct_call(
                direct_nl_llm_route,
                edges,
                workflow_data,
            )

            controlled = timed_direct_call(
                direct_nl_llm_route_controlled,
                edges,
                workflow_data,
            )

            structured = run_structured(
                edges,
                workflow_data,
            )

            for result in [original, controlled, structured]:
                result["correct"] = (
                    result["result"] == expected_target
                    and result.get("status", "ROUTED") == "ROUTED"
                )

            record = {
                "case_id": case["case_id"],
                "repetition": repetition,
                "paraphrase": case["text"],
                "expected_value": case["expected_value"],
                "workflow_data": workflow_data,
                "expected_target": expected_target,
                "edges": edges,
                "original_direct": original,
                "controlled_direct": controlled,
                "structured": structured,
            }

            records.append(record)

            print(
                "Original:", original["result"],
                "| Controlled:", controlled["result"],
                "| Structured:", structured["result"],
                "| Expected:", expected_target,
            )

    summary = calculate_summary(records)

    output = {
        "experiment": "prompt_controlled_three_method_comparison",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "model": "llama3.2:3b",
        "temperature": 0,
        "repeats_per_case": REPEATS,
        "summary": summary,
        "records": records,
        "limitations": [
            "Ten manually defined paraphrases of one Boolean condition.",
            "Three repetitions per case.",
            "Only one workflow state tested per case.",
            "Direct methods use one LLM call per decision.",
            "Structured method uses two LLM calls per decision.",
            "Structured contracts are regenerated each repetition.",
            "Explicit Boolean guidance is aligned, but prompts and output constraints still differ.",
            "Methods run sequentially, so timing may be affected by order and local system conditions.",
            "Consistency measures repeated identical outputs, not correctness.",
            "No complete workflow path or persisted trace evaluation.",
        ],
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    print("\n" + "=" * 65)
    print("SUMMARY")

    for method, result in summary.items():
        print(
            f"{method}: "
            f"{result['correct']}/{result['total']} correct, "
            f"{result['accuracy']:.1%} accuracy, "
            f"{result['stable_cases']}/{result['total_cases']} stable cases, "
            f"{result['total_seconds']:.2f} seconds, "
            f"{result['total_llm_calls']} LLM calls"
        )

    print("\nResults saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    run_experiment()
