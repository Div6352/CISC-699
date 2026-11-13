
# CISC 699 - Capstone II A2 Research
# Structured Semantic Contract Reuse Experiment

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
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
    / "contract_reuse_experiment_results.json"
)


def route_with_existing_contracts(contracts, workflow_data):
    start = time.perf_counter()

    try:
        routing = route_with_explanation(
            contracts,
            CURRENT_NODE,
            workflow_data,
        )

        status = routing["status"]
        target = routing["next_node"]

        if (
            status == "ROUTED"
            and not is_permitted_transition(
                CURRENT_NODE,
                target,
            )
        ):
            status = "INVALID_GRAPH_TRANSITION"
            target = None

        error = None

    except Exception as exc:
        status = "ROUTING_ERROR"
        target = None
        error = f"{type(exc).__name__}: {exc}"

    elapsed = time.perf_counter() - start

    return {
        "status": status,
        "target": target,
        "seconds": elapsed,
        "error": error,
    }


def run_experiment():
    records = []
    total_construction_seconds = 0.0
    total_routing_seconds = 0.0

    print("\nSTRUCTURED CONTRACT REUSE EXPERIMENT")
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

        # Interpret both outgoing edges ONCE per case.
        (
            contracts,
            interpretations,
            construction_seconds,
        ) = build_contracts(edges)

        total_construction_seconds += construction_seconds

        case_routes = []

        # Reuse the same contracts for all repetitions.
        for repetition in range(1, REPEATS + 1):
            routing = route_with_existing_contracts(
                contracts,
                workflow_data,
            )

            total_routing_seconds += routing["seconds"]

            correct = (
                routing["status"] == "ROUTED"
                and routing["target"] == expected_target
            )

            record = {
                "case_id": case["case_id"],
                "repetition": repetition,
                "paraphrase": case["text"],
                "expected_value": case["expected_value"],
                "workflow_data": workflow_data,
                "expected_target": expected_target,
                "observed_target": routing["target"],
                "status": routing["status"],
                "correct": correct,
                "routing_seconds": routing["seconds"],
                "routing_error": routing["error"],
            }

            records.append(record)

            case_routes.append(
                (routing["status"], routing["target"])
            )

            print(
                f"{case['case_id']} "
                f"repetition {repetition}/{REPEATS}: "
                f"Expected={expected_target}, "
                f"Actual={routing['target']}, "
                f"Correct={correct}"
            )

        records_for_case = [
            record
            for record in records
            if record["case_id"] == case["case_id"]
        ]

        # Store construction evidence separately.
        for record in records_for_case:
            record["contract_construction_seconds"] = (
                construction_seconds
            )
            record["interpretations"] = interpretations

        stable = len(set(case_routes)) == 1

        for record in records_for_case:
            record["case_stable"] = stable

    total_decisions = len(records)

    correct_decisions = sum(
        record["correct"]
        for record in records
    )

    stable_cases = sum(
        all(
            record["case_stable"]
            for record in records
            if record["case_id"] == case["case_id"]
        )
        for case in independent_evaluation_cases
    )

    total_seconds = (
        total_construction_seconds
        + total_routing_seconds
    )

    summary = {
        "total_cases": len(independent_evaluation_cases),
        "repeats_per_case": REPEATS,
        "total_decisions": total_decisions,
        "correct_decisions": correct_decisions,
        "accuracy": (
            correct_decisions / total_decisions
            if total_decisions else 0.0
        ),
        "stable_cases": stable_cases,
        "total_construction_seconds": (
            total_construction_seconds
        ),
        "total_routing_seconds": total_routing_seconds,
        "total_seconds_including_construction": total_seconds,
        "average_total_seconds_per_decision": (
            total_seconds / total_decisions
            if total_decisions else 0.0
        ),
        "average_routing_seconds_per_decision": (
            total_routing_seconds / total_decisions
            if total_decisions else 0.0
        ),
        "total_llm_calls": (
            len(independent_evaluation_cases) * 2
        ),
        "llm_calls_per_case": 2,
        "llm_calls_per_reused_decision": 0,
    }

    output = {
        "experiment": "structured_contract_reuse",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "model": "llama3.2:3b",
        "temperature": 0,
        "summary": summary,
        "records": records,
        "limitations": [
            "Ten manually defined paraphrases of one Boolean condition.",
            "Each case uses one workflow state.",
            "Contracts are generated once per case and reused three times.",
            "Two LLM interpretation calls are made per case.",
            "No direct LLM baseline is executed in this experiment.",
            "Comparison with previous experiments is cross-run.",
            "Contract construction cost is included in total time.",
            "Stability is not equivalent to correctness.",
            "No complete workflow path or persisted execution trace is measured.",
        ],
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Preserve existing evidence.
    with OUTPUT_FILE.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    print("\n" + "=" * 65)
    print("CONTRACT REUSE SUMMARY")
    print(
        "Correct decisions:",
        f"{correct_decisions}/{total_decisions}",
    )
    print("Accuracy:", f"{summary['accuracy']:.1%}")
    print(
        "Stable cases:",
        f"{stable_cases}/{len(independent_evaluation_cases)}",
    )
    print(
        "Contract construction seconds:",
        round(total_construction_seconds, 4),
    )
    print(
        "Deterministic routing seconds:",
        round(total_routing_seconds, 6),
    )
    print(
        "Total seconds including construction:",
        round(total_seconds, 4),
    )
    print(
        "Average seconds per decision:",
        round(summary["average_total_seconds_per_decision"], 4),
    )
    print("Total LLM calls:", summary["total_llm_calls"])
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    run_experiment()
