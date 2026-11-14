# CISC 699 - Capstone II A2 Research
# Prompt-Controlled Three-Method Routing Comparison

import json
import time
from contextlib import redirect_stdout
from datetime import datetime, timezone
from hashlib import sha256
from io import StringIO
from pathlib import Path
from uuid import uuid4

from contract_router import route_with_explanation
from direct_nl_llm_router import direct_nl_llm_route
from direct_nl_llm_router_controlled import direct_nl_llm_route_controlled
from graph import is_permitted_transition
from independent_evaluation_dataset import independent_evaluation_cases
from test_repeated_matched_independent_nl import (
    CURRENT_NODE,
    build_contracts,
    make_edges,
)


REPEATS = 3
MODEL = "llama3.2:3b"
TEMPERATURE = 0
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "docs" / "comparison_runs"
METHODS = ("original_direct", "controlled_direct", "structured")

REQUEST_ERROR_PREFIXES = (
    "URLError:",
    "HTTPError:",
    "TimeoutError:",
    "ConnectionError:",
    "ConnectionRefusedError:",
    "ConnectionResetError:",
    "ConnectionAbortedError:",
    "RemoteDisconnected:",
)


def save_json(path, data):
    temporary_path = path.with_suffix(".json.tmp")
    with temporary_path.open("x", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")
    temporary_path.replace(path)


def timed_direct_call(function, edges, workflow_data):
    diagnostics = StringIO()
    error = None
    start = time.perf_counter()

    try:
        with redirect_stdout(diagnostics):
            result = function(edges, CURRENT_NODE, workflow_data)
    except Exception as exc:
        result = "LLM_ERROR"
        error = f"{type(exc).__name__}: {exc}"

    elapsed = time.perf_counter() - start
    diagnostic_text = diagnostics.getvalue()

    if diagnostic_text:
        print(diagnostic_text, end="")
    if result == "LLM_ERROR" and error is None:
        error = diagnostic_text.strip() or "Router returned LLM_ERROR"

    return {
        "result": result,
        "seconds": elapsed,
        "error": error,
        "diagnostics": diagnostic_text,
        "llm_calls": 1,
    }


def run_structured(edges, workflow_data):
    contracts, interpretations, construction_seconds = build_contracts(edges)

    start = time.perf_counter()
    routing = route_with_explanation(contracts, CURRENT_NODE, workflow_data)
    routing_seconds = time.perf_counter() - start

    status = routing["status"]
    target = routing["next_node"]

    if status == "ROUTED" and not is_permitted_transition(CURRENT_NODE, target):
        status = "INVALID_GRAPH_TRANSITION"
        target = None

    return {
        "status": status,
        "result": target,
        "construction_seconds": construction_seconds,
        "routing_seconds": routing_seconds,
        "seconds": construction_seconds + routing_seconds,
        "contracts": contracts,
        "interpretations": interpretations,
        "llm_calls": len(interpretations),
    }


def calculate_summary(records):
    summary = {}

    for method in METHODS:
        decisions = [record[method] for record in records]
        total = len(decisions)
        correct = sum(decision["correct"] for decision in decisions)
        total_seconds = sum(decision["seconds"] for decision in decisions)
        stable_cases = 0
        stable_valid_routes = 0
        incomplete_cases = 0

        for case in independent_evaluation_cases:
            observed = [
                (record[method].get("status", "ROUTED"), record[method]["result"])
                for record in records
                if record["case_id"] == case["case_id"]
            ]

            if len(observed) != REPEATS:
                incomplete_cases += 1
                continue

            if len(set(observed)) == 1:
                stable_cases += 1
                status, target = observed[0]
                if (
                    status == "ROUTED"
                    and target is not None
                    and is_permitted_transition(CURRENT_NODE, target)
                ):
                    stable_valid_routes += 1

        summary[method] = {
            "correct": correct,
            "total": total,
            "accuracy": correct / total if total else None,
            "stable_cases": stable_cases,
            "stable_valid_route_cases": stable_valid_routes,
            "stable_nonroute_cases": stable_cases - stable_valid_routes,
            "incomplete_cases": incomplete_cases,
            "total_cases": len(independent_evaluation_cases),
            "total_seconds": total_seconds,
            "average_seconds_per_decision": total_seconds / total if total else None,
            "total_llm_calls": sum(decision["llm_calls"] for decision in decisions),
        }

    return summary


def run_experiment():
    started_utc = datetime.now(timezone.utc)
    run_id = f"{started_utc:%Y%m%dT%H%M%SZ}-{uuid4().hex[:12]}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    dataset_path = PROJECT_ROOT / "src" / "independent_evaluation_dataset.py"
    planned = [
        (case["case_id"], repetition)
        for case in independent_evaluation_cases
        for repetition in range(1, REPEATS + 1)
    ]
    manifest = {
        "run_id": run_id,
        "experiment": "prompt_controlled_three_method_comparison",
        "started_utc": started_utc.isoformat(),
        "model": MODEL,
        "temperature": TEMPERATURE,
        "starting_node": CURRENT_NODE,
        "methods_in_order": METHODS,
        "dataset": "src/independent_evaluation_dataset.py",
        "dataset_sha256": sha256(dataset_path.read_bytes()).hexdigest(),
        "runner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "repeats_per_case": REPEATS,
        "planned_case_repetitions": planned,
    }
    save_json(run_dir / "manifest.json", manifest)
    print("Run evidence folder:", run_dir)

    records = []
    stop_reason = None

    try:
        for case in independent_evaluation_cases:
            edges = make_edges(case)
            workflow_data = {"tests_passed": case["expected_value"]}
            expected_target = (
                "Deploy Code" if case["expected_value"] is True else "Fix Code"
            )

            for repetition in range(1, REPEATS + 1):
                case_id = case["case_id"]
                print(f"\n{case_id} repetition {repetition}/{REPEATS}")

                decisions = {
                    "original_direct": timed_direct_call(
                        direct_nl_llm_route, edges, workflow_data
                    ),
                    "controlled_direct": timed_direct_call(
                        direct_nl_llm_route_controlled, edges, workflow_data
                    ),
                    "structured": run_structured(edges, workflow_data),
                }

                for decision in decisions.values():
                    decision["correct"] = (
                        decision["result"] == expected_target
                        and decision.get("status", "ROUTED") == "ROUTED"
                    )

                record = {
                    "run_id": run_id,
                    "case_id": case_id,
                    "repetition": repetition,
                    "paraphrase": case["text"],
                    "expected_value": case["expected_value"],
                    "workflow_data": workflow_data,
                    "expected_target": expected_target,
                    "edges": edges,
                    **decisions,
                }
                save_json(run_dir / f"{case_id}-{repetition:02d}.json", record)
                records.append(record)

                print(
                    "Original:", decisions["original_direct"]["result"],
                    "| Controlled:", decisions["controlled_direct"]["result"],
                    "| Structured:", decisions["structured"]["result"],
                    "| Expected:", expected_target,
                )

                direct_request_failed = any(
                    decisions[method]["result"] == "LLM_ERROR"
                    for method in ("original_direct", "controlled_direct")
                )
                structured_request_failed = any(
                    (item.get("error") or "").startswith(REQUEST_ERROR_PREFIXES)
                    for item in decisions["structured"].get("interpretations", [])
                )

                if direct_request_failed or structured_request_failed:
                    stop_reason = (
                        f"LLM request failed at {case_id}, repetition {repetition}."
                    )
                    break

            if stop_reason:
                break

    except KeyboardInterrupt:
        stop_reason = "Interrupted by user."
    except Exception as exc:
        stop_reason = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        completed = {
            (record["case_id"], record["repetition"]) for record in records
        }
        output = {
            **manifest,
            "finished_utc": datetime.now(timezone.utc).isoformat(),
            "status": "complete" if stop_reason is None else "stopped",
            "stop_reason": stop_reason,
            "completed_case_repetitions": len(completed),
            "missing_case_repetitions": [
                pair for pair in planned if pair not in completed
            ],
            "summary": calculate_summary(records),
            "records": records,
            "limitations": [
                "Ten manually defined paraphrases of one Boolean condition.",
                "Only one workflow state tested per case.",
                "Each direct method uses one LLM call per decision.",
                "Structured contracts are regenerated each repetition.",
                "Boolean guidance is aligned for the controlled comparison. "
                "Prompt wording and output constraints differ.",
                "Methods run sequentially. Order and local system conditions may affect timing.",
                "The structured evidence contains parsed conditions. Direct diagnostics "
                "contain the response text printed by each router.",
                "Repeatability measures consistency of edge decisions. "
                "Complete workflow paths and persisted execution traces require separate evidence.",
            ],
        }
        output_file = run_dir / "summary.json"
        save_json(output_file, output)
        print("\nResults saved to:", output_file)
        if stop_reason:
            print("Stop reason:", stop_reason)


if __name__ == "__main__":
    run_experiment()