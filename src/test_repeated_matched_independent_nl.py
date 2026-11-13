
# CISC 699 - Capstone II A2 Research
# Repeated Matched Independent Natural-Language Comparison

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
from direct_nl_llm_router import direct_nl_llm_route
from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from contract_router import route_with_explanation
from graph import is_permitted_transition


REPEATS = 3
CURRENT_NODE = "Check Tests"

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Use a NEW output file to preserve the original experiment.
OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "repeated_matched_independent_nl_results.json"
)

ORIGINAL_PASS_EDGE = (
    "If all software tests have passed, proceed to deployment."
)

ORIGINAL_FAIL_EDGE = (
    "If any software test has failed, return to fixing the code."
)


def make_edges(case):
    """Construct the same two-edge scenario for both methods."""

    pass_text = ORIGINAL_PASS_EDGE
    fail_text = ORIGINAL_FAIL_EDGE

    # The oracle determines scenario construction, not the LLM prompt.
    if case["expected_value"] is True:
        pass_text = case["text"]
    else:
        fail_text = case["text"]

    return [
        {
            "edge_id": "E01",
            "source": CURRENT_NODE,
            "target": "Deploy Code",
            "text": pass_text,
            "expected_value": True,
        },
        {
            "edge_id": "E02",
            "source": CURRENT_NODE,
            "target": "Fix Code",
            "text": fail_text,
            "expected_value": False,
        },
    ]


def build_contracts(edges):
    """Interpret both edges and retain valid structured contracts."""

    contracts = []
    interpretation_records = []

    start_total = time.perf_counter()

    for edge in edges:
        start = time.perf_counter()
        error = None

        try:
            condition = interpret_with_structured_ollama(
                edge["text"]
            )
        except Exception as exc:
            condition = None
            error = f"{type(exc).__name__}: {exc}"

        elapsed = time.perf_counter() - start

        interpretation_correct = (
            isinstance(condition, dict)
            and condition.get("field") == "tests_passed"
            and condition.get("operator") == "equals"
            and type(condition.get("value")) is bool
            and condition["value"] is edge["expected_value"]
        )

        valid_contract = False

        if condition is not None:
            contract = {
                "edge_id": edge["edge_id"],
                "source": edge["source"],
                "target": edge["target"],
                "condition": condition,
            }

            valid_contract = (
                validate_contract(contract)
                and is_permitted_transition(
                    edge["source"],
                    edge["target"],
                )
            )

            if valid_contract:
                contracts.append(contract)

        interpretation_records.append(
            {
                "edge_id": edge["edge_id"],
                "text": edge["text"],
                "expected_value": edge["expected_value"],
                "predicted_condition": condition,
                "interpretation_correct": interpretation_correct,
                "contract_valid": valid_contract,
                "seconds": elapsed,
                "error": error,
            }
        )

    construction_seconds = time.perf_counter() - start_total

    return contracts, interpretation_records, construction_seconds


def run_experiment():
    records = []

    print("\nREPEATED MATCHED INDEPENDENT NL COMPARISON")
    print("=" * 65)
    print("Cases:", len(independent_evaluation_cases))
    print("Repetitions per case:", REPEATS)

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
                f"\nRunning {case['case_id']} "
                f"repetition {repetition}/{REPEATS}"
            )

            # Direct natural-language LLM routing.
            direct_start = time.perf_counter()
            direct_error = None

            try:
                direct_result = direct_nl_llm_route(
                    edges,
                    CURRENT_NODE,
                    workflow_data,
                )
            except Exception as exc:
                direct_result = "LLM_ERROR"
                direct_error = f"{type(exc).__name__}: {exc}"

            direct_seconds = (
                time.perf_counter() - direct_start
            )

            # Fresh interpretation of both edges for every repetition.
            (
                contracts,
                interpretations,
                construction_seconds,
            ) = build_contracts(edges)

            # Deterministic routing using the generated contracts.
            routing_start = time.perf_counter()

            routing_result = route_with_explanation(
                contracts,
                CURRENT_NODE,
                workflow_data,
            )

            routing_seconds = (
                time.perf_counter() - routing_start
            )

            structured_status = routing_result["status"]
            structured_target = routing_result["next_node"]

            if (
                structured_status == "ROUTED"
                and not is_permitted_transition(
                    CURRENT_NODE,
                    structured_target,
                )
            ):
                structured_status = "INVALID_GRAPH_TRANSITION"
                structured_target = None

            target_edge_id = (
                "E01"
                if case["expected_value"] is True
                else "E02"
            )

            target_interpretation = next(
                (
                    item
                    for item in interpretations
                    if item["edge_id"] == target_edge_id
                ),
                None,
            )

            record = {
                "case_id": case["case_id"],
                "repetition": repetition,
                "paraphrase": case["text"],
                "expected_value": case["expected_value"],
                "workflow_data": workflow_data,
                "expected_target": expected_target,
                "edges": edges,
                "direct_result": direct_result,
                "direct_correct": direct_result == expected_target,
                "direct_seconds": direct_seconds,
                "direct_error": direct_error,
                "structured_result": structured_target,
                "structured_status": structured_status,
                "structured_correct": (
                    structured_status == "ROUTED"
                    and structured_target == expected_target
                ),
                "structured_construction_seconds": construction_seconds,
                "structured_routing_seconds": routing_seconds,
                "structured_total_seconds": (
                    construction_seconds + routing_seconds
                ),
                "paraphrase_interpretation_correct": (
                    target_interpretation["interpretation_correct"]
                    if target_interpretation is not None
                    else False
                ),
                "interpretations": interpretations,
            }

            records.append(record)

            print(
                f"Direct: {direct_result} | "
                f"Structured: {structured_target} | "
                f"Expected: {expected_target}"
            )

    total = len(records)

    direct_correct = sum(
        record["direct_correct"]
        for record in records
    )

    structured_correct = sum(
        record["structured_correct"]
        for record in records
    )

    interpretation_correct = sum(
        record["paraphrase_interpretation_correct"]
        for record in records
    )

    direct_seconds = sum(
        record["direct_seconds"]
        for record in records
    )

    structured_seconds = sum(
        record["structured_total_seconds"]
        for record in records
    )

    case_consistency = []

    for case in independent_evaluation_cases:
        case_records = [
            record
            for record in records
            if record["case_id"] == case["case_id"]
        ]

        direct_outputs = [
            record["direct_result"]
            for record in case_records
        ]

        structured_outputs = [
            (
                record["structured_status"],
                record["structured_result"],
            )
            for record in case_records
        ]

        direct_stable = len(set(direct_outputs)) == 1
        structured_stable = len(set(structured_outputs)) == 1

        case_consistency.append(
            {
                "case_id": case["case_id"],
                "direct_stable": direct_stable,
                "structured_stable": structured_stable,
                "direct_outputs": direct_outputs,
                "structured_outputs": [
                    {
                        "status": status,
                        "target": target,
                    }
                    for status, target in structured_outputs
                ],
            }
        )

    stable_direct_cases = sum(
        item["direct_stable"]
        for item in case_consistency
    )

    stable_structured_cases = sum(
        item["structured_stable"]
        for item in case_consistency
    )

    number_of_cases = len(independent_evaluation_cases)

    summary = {
        "total_cases": number_of_cases,
        "repeats_per_case": REPEATS,
        "total_decisions_per_method": total,
        "direct_correct": direct_correct,
        "structured_correct": structured_correct,
        "direct_accuracy": (
            direct_correct / total if total else 0.0
        ),
        "structured_accuracy": (
            structured_correct / total if total else 0.0
        ),
        "correct_paraphrase_interpretations": interpretation_correct,
        "total_paraphrase_interpretations": total,
        "stable_direct_cases": stable_direct_cases,
        "stable_structured_cases": stable_structured_cases,
        "direct_case_stability_rate": (
            stable_direct_cases / number_of_cases
            if number_of_cases else 0.0
        ),
        "structured_case_stability_rate": (
            stable_structured_cases / number_of_cases
            if number_of_cases else 0.0
        ),
        "total_direct_seconds": direct_seconds,
        "total_structured_seconds": structured_seconds,
        "limitations": [
            "Ten independent paraphrases with three repetitions each.",
            "Each case substitutes one edge; the opposite edge is unchanged.",
            "Only one workflow state is tested per independent case.",
            "The oracle determines scenario construction and expected route.",
            "The oracle is not supplied to either LLM prompt.",
            "The structured interpreter receives additional Boolean guidance.",
            "Each structured repetition includes two LLM interpretation calls.",
            "Each direct repetition includes one LLM routing call.",
            "Contracts are reconstructed for every repetition.",
            "Consistency means identical observed decisions, not correctness.",
            "Timing includes contract construction for the structured method.",
            "No full workflow execution or trace persistence is measured.",
            "Small benchmark and single local model limit generalizability.",
        ],
    }

    output = {
        "experiment": "repeated_matched_independent_nl",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "model": "llama3.2:3b",
        "temperature": 0,
        "summary": summary,
        "case_consistency": case_consistency,
        "records": records,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Exclusive creation prevents accidental overwrite of prior evidence.
    with OUTPUT_FILE.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    print("\n" + "=" * 65)
    print("REPEATED MATCHED INDEPENDENT SUMMARY")
    print(f"Direct correct: {direct_correct}/{total}")
    print(f"Structured correct: {structured_correct}/{total}")
    print(f"Direct accuracy: {summary['direct_accuracy']:.1%}")
    print(f"Structured accuracy: {summary['structured_accuracy']:.1%}")
    print(
        f"Direct stable cases: "
        f"{stable_direct_cases}/{number_of_cases}"
    )
    print(
        f"Structured stable cases: "
        f"{stable_structured_cases}/{number_of_cases}"
    )
    print(
        "Paraphrase interpretations correct:",
        f"{interpretation_correct}/{total}",
    )
    print("Direct total seconds:", round(direct_seconds, 4))
    print("Structured total seconds:", round(structured_seconds, 4))
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    run_experiment()
