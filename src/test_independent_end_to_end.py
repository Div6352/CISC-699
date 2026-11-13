
# CISC 699 - Capstone II A2 Research
# Independent Natural-Language End-to-End Evaluation

import json
import time
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from contract_router import route_with_explanation
from graph import is_permitted_transition


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "independent_end_to_end_results.json"
)

CURRENT_NODE = "Check Tests"


def expected_target(expected_value):
    if expected_value is True:
        return "Deploy Code"
    return "Fix Code"


def evaluate_case(case):
    case_id = case["case_id"]
    text = case["text"]
    expected_value = case["expected_value"]
    target = expected_target(expected_value)

    print(f"\nEvaluating {case_id}: {text}")

    interpretation_start = time.perf_counter()

    try:
        condition = interpret_with_structured_ollama(text)
        interpretation_error = None
    except Exception as error:
        condition = None
        interpretation_error = (
            f"{type(error).__name__}: {error}"
        )

    interpretation_seconds = (
        time.perf_counter() - interpretation_start
    )

    interpretation_valid = (
        isinstance(condition, dict)
        and condition.get("field") == "tests_passed"
        and condition.get("operator") == "equals"
        and type(condition.get("value")) is bool
    )

    predicted_value = (
        condition["value"]
        if interpretation_valid
        else None
    )

    interpretation_correct = (
        interpretation_valid
        and predicted_value is expected_value
    )

    contract = None
    contract_valid = False
    graph_valid = False

    if interpretation_valid:
        contract = {
            "edge_id": case_id,
            "source": CURRENT_NODE,
            "target": target,
            "condition": condition
        }

        contract_valid = validate_contract(contract)

        graph_valid = is_permitted_transition(
            CURRENT_NODE,
            target
        )

    routing_records = []

    for workflow_value in (True, False):
        workflow_data = {
            "tests_passed": workflow_value
        }

        should_route = (
            workflow_value is expected_value
        )

        expected_status = (
            "ROUTED" if should_route else "NO_MATCH"
        )

        expected_next_node = (
            target if should_route else None
        )

        if not contract_valid or not graph_valid:
            routing_records.append({
                "workflow_data": workflow_data,
                "expected_status": expected_status,
                "expected_next_node": expected_next_node,
                "actual_status": "NOT_EVALUATED",
                "actual_next_node": None,
                "correct": False,
                "routing_seconds": None
            })
            continue

        routing_start = time.perf_counter()

        result = route_with_explanation(
            [contract],
            CURRENT_NODE,
            workflow_data
        )

        routing_seconds = (
            time.perf_counter() - routing_start
        )

        actual_status = result["status"]
        actual_next_node = result["next_node"]

        correct = (
            actual_status == expected_status
            and actual_next_node == expected_next_node
        )

        routing_records.append({
            "workflow_data": workflow_data,
            "expected_status": expected_status,
            "expected_next_node": expected_next_node,
            "actual_status": actual_status,
            "actual_next_node": actual_next_node,
            "correct": correct,
            "routing_seconds": routing_seconds
        })

    print("Expected condition:", expected_value)
    print("Predicted condition:", predicted_value)
    print(
        "Interpretation:",
        "CORRECT" if interpretation_correct else "INCORRECT"
    )

    for record in routing_records:
        print(
            "Routing with tests_passed =",
            record["workflow_data"]["tests_passed"],
            ":",
            "CORRECT" if record["correct"] else "INCORRECT"
        )

    return {
        "case_id": case_id,
        "text": text,
        "expected_value": expected_value,
        "expected_target": target,
        "predicted_condition": condition,
        "interpretation_valid": interpretation_valid,
        "interpretation_correct": interpretation_correct,
        "interpretation_error": interpretation_error,
        "interpretation_seconds": interpretation_seconds,
        "contract": contract,
        "contract_valid": contract_valid,
        "graph_valid": graph_valid,
        "routing_records": routing_records
    }


def run_experiment():
    print("\nA2 Research - Independent End-to-End Evaluation")
    print("=" * 60)

    results = []

    for case in independent_evaluation_cases:
        results.append(evaluate_case(case))

    total_cases = len(results)

    correct_interpretations = sum(
        result["interpretation_correct"]
        for result in results
    )

    valid_interpretations = sum(
        result["interpretation_valid"]
        for result in results
    )

    routing_records = [
        record
        for result in results
        for record in result["routing_records"]
    ]

    correct_routes = sum(
        record["correct"]
        for record in routing_records
    )

    total_routes = len(routing_records)

    completed_routing_times = [
        record["routing_seconds"]
        for record in routing_records
        if record["routing_seconds"] is not None
    ]

    interpretation_accuracy = (
        correct_interpretations / total_cases
        if total_cases else 0.0
    )

    routing_accuracy = (
        correct_routes / total_routes
        if total_routes else 0.0
    )

    summary = {
        "experiment": (
            "Independent natural-language interpretation "
            "and contract-routing evaluation"
        ),
        "model": "llama3.2:3b",
        "temperature": 0,
        "total_interpretation_cases": total_cases,
        "valid_interpretations": valid_interpretations,
        "correct_interpretations": correct_interpretations,
        "interpretation_accuracy": interpretation_accuracy,
        "total_routing_evaluations": total_routes,
        "correct_routing_evaluations": correct_routes,
        "routing_accuracy": routing_accuracy,
        "total_interpretation_seconds": sum(
            result["interpretation_seconds"]
            for result in results
        ),
        "average_interpretation_seconds": (
            sum(
                result["interpretation_seconds"]
                for result in results
            ) / total_cases
            if total_cases else None
        ),
        "average_routing_seconds": (
            sum(completed_routing_times)
            / len(completed_routing_times)
            if completed_routing_times
            else None
        ),
        "limitations": [
            "The dataset contains ten paraphrases of one "
            "Boolean workflow condition.",
            "Each natural-language edge is interpreted once.",
            "Routing is tested against both Boolean workflow states.",
            "The expected target is supplied by the benchmark "
            "definition, not inferred from the natural-language text.",
            "Graph permission is checked separately; this experiment "
            "does not invoke the traced routing pipeline.",
            "There is no matched direct-LLM baseline in this experiment.",
            "This is a small benchmark, not evidence of general "
            "natural-language understanding."
        ]
    }

    output = {
        "summary": summary,
        "results": results
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with OUTPUT_FILE.open(
        "w", encoding="utf-8"
    ) as file:
        json.dump(output, file, indent=4)

    print("\n" + "=" * 60)
    print("INDEPENDENT EVALUATION SUMMARY")
    print("Interpretations:", total_cases)
    print(
        "Correct interpretations:",
        f"{correct_interpretations}/{total_cases}"
    )
    print(
        "Interpretation accuracy:",
        f"{interpretation_accuracy:.1%}"
    )
    print("Routing evaluations:", total_routes)
    print(
        "Correct routing evaluations:",
        f"{correct_routes}/{total_routes}"
    )
    print(
        "Routing accuracy:",
        f"{routing_accuracy:.1%}"
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Evaluation completed.")


if __name__ == "__main__":
    run_experiment()
