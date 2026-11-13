
# CISC 699 - Capstone II A2 Research
# Matched Natural-Language Routing Comparison

import json
import time
from pathlib import Path

from direct_nl_llm_router import direct_nl_llm_route
from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from contract_router import route_with_explanation
from graph import is_permitted_transition


REPEATS = 5
CURRENT_NODE = "Check Tests"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = (
    PROJECT_ROOT / "docs" / "fair_nl_comparison_results.json"
)

EDGES = [
    {
        "edge_id": "E01",
        "source": "Check Tests",
        "target": "Deploy Code",
        "text": (
            "If all software tests have passed, "
            "proceed to deployment."
        ),
        "expected_value": True
    },
    {
        "edge_id": "E02",
        "source": "Check Tests",
        "target": "Fix Code",
        "text": (
            "If any software test has failed, "
            "return to fixing the code."
        ),
        "expected_value": False
    }
]

TEST_CASES = [
    {
        "case_id": "PASS",
        "workflow_data": {"tests_passed": True},
        "expected": "Deploy Code"
    },
    {
        "case_id": "FAIL",
        "workflow_data": {"tests_passed": False},
        "expected": "Fix Code"
    }
]


def build_contracts():
    contracts = []
    records = []

    start_total = time.perf_counter()

    for edge in EDGES:
        start = time.perf_counter()

        try:
            condition = interpret_with_structured_ollama(
                edge["text"]
            )
            error = None
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

        contract = None
        contract_valid = False

        if condition is not None:
            contract = {
                "edge_id": edge["edge_id"],
                "source": edge["source"],
                "target": edge["target"],
                "condition": condition
            }

            contract_valid = (
                validate_contract(contract)
                and is_permitted_transition(
                    edge["source"],
                    edge["target"]
                )
            )

            if contract_valid:
                contracts.append(contract)

        records.append({
            "edge_id": edge["edge_id"],
            "text": edge["text"],
            "expected_value": edge["expected_value"],
            "predicted_condition": condition,
            "interpretation_correct": interpretation_correct,
            "contract_valid": contract_valid,
            "interpretation_seconds": elapsed,
            "error": error
        })

    construction_seconds = (
        time.perf_counter() - start_total
    )

    return contracts, records, construction_seconds


def run_experiment():
    print("\nA2 Research - Matched Natural-Language Comparison")
    print("=" * 60)

    print("\nBuilding structured contracts...")
    contracts, interpretation_records, construction_seconds = (
        build_contracts()
    )

    records = []

    for case in TEST_CASES:
        print("\nScenario:", case["case_id"])

        for run_number in range(1, REPEATS + 1):
            workflow_data = case["workflow_data"]
            expected = case["expected"]

            direct_start = time.perf_counter()

            direct_result = direct_nl_llm_route(
                EDGES,
                CURRENT_NODE,
                workflow_data
            )

            direct_seconds = (
                time.perf_counter() - direct_start
            )

            structured_start = time.perf_counter()

            structured_result = route_with_explanation(
                contracts,
                CURRENT_NODE,
                workflow_data
            )

            structured_seconds = (
                time.perf_counter() - structured_start
            )

            structured_node = structured_result["next_node"]

            # Apply graph permissions to the structured decision.
            graph_permitted = (
                structured_result["status"] != "ROUTED"
                or is_permitted_transition(
                    CURRENT_NODE,
                    structured_node
                )
            )

            if not graph_permitted:
                structured_node = None
                structured_status = "INVALID_GRAPH_TRANSITION"
            else:
                structured_status = structured_result["status"]

            record = {
                "case_id": case["case_id"],
                "run": run_number,
                "workflow_data": workflow_data,
                "expected": expected,
                "direct_result": direct_result,
                "direct_correct": direct_result == expected,
                "direct_seconds": direct_seconds,
                "structured_result": structured_node,
                "structured_status": structured_status,
                "structured_correct": (
                    structured_status == "ROUTED"
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
        record["direct_correct"]
        for record in records
    )

    structured_correct = sum(
        record["structured_correct"]
        for record in records
    )

    total_direct_seconds = sum(
        record["direct_seconds"]
        for record in records
    )

    total_structured_routing_seconds = sum(
        record["structured_seconds"]
        for record in records
    )

    structured_total_seconds = (
        construction_seconds
        + total_structured_routing_seconds
    )

    summary = {
        "experiment": (
            "Matched natural-language edge routing comparison"
        ),
        "model": "llama3.2:3b",
        "temperature": 0,
        "distinct_workflow_states": len(TEST_CASES),
        "repeats_per_state": REPEATS,
        "total_decisions_per_method": total,
        "direct_correct": direct_correct,
        "structured_correct": structured_correct,
        "direct_accuracy": (
            direct_correct / total if total else 0.0
        ),
        "structured_accuracy": (
            structured_correct / total if total else 0.0
        ),
        "correct_edge_interpretations": sum(
            item["interpretation_correct"]
            for item in interpretation_records
        ),
        "total_edge_interpretations": len(
            interpretation_records
        ),
        "contract_construction_seconds": construction_seconds,
        "total_direct_seconds": total_direct_seconds,
        "total_structured_routing_seconds": (
            total_structured_routing_seconds
        ),
        "total_structured_seconds_including_construction": (
            structured_total_seconds
        ),
        "average_direct_seconds": (
            total_direct_seconds / total if total else None
        ),
        "average_structured_routing_seconds": (
            total_structured_routing_seconds / total
            if total else None
        ),
        "amortized_structured_seconds_per_decision": (
            structured_total_seconds / total
            if total else None
        ),
        "limitations": [
            "Only two distinct workflow states are evaluated.",
            "The structured approach interprets edges once "
            "and reuses the generated contracts.",
            "The direct LLM receives the natural-language edges "
            "on every routing call.",
            "Both approaches use the same underlying Ollama model.",
            "Contract interpretation errors are retained.",
            "The benchmark supplies expected Boolean values "
            "only for scoring.",
            "The experiment does not measure full graph execution "
            "or execution-trace persistence.",
            "Timing results depend on hardware and model warm-up."
        ]
    }

    output = {
        "edges": EDGES,
        "interpretation_records": interpretation_records,
        "contracts": contracts,
        "summary": summary,
        "records": records
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
    print("MATCHED COMPARISON SUMMARY")
    print("Decisions per method:", total)
    print(
        "Direct NL correct:",
        f"{direct_correct}/{total}"
    )
    print(
        "Structured correct:",
        f"{structured_correct}/{total}"
    )
    print(
        "Direct NL accuracy:",
        f"{summary['direct_accuracy']:.1%}"
    )
    print(
        "Structured accuracy:",
        f"{summary['structured_accuracy']:.1%}"
    )
    print(
        "Correct edge interpretations:",
        f"{summary['correct_edge_interpretations']}"
        f"/{summary['total_edge_interpretations']}"
    )
    print(
        "Contract construction seconds:",
        round(construction_seconds, 4)
    )
    print(
        "Total direct seconds:",
        round(total_direct_seconds, 4)
    )
    print(
        "Total structured seconds including construction:",
        round(structured_total_seconds, 4)
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Experiment completed.")


if __name__ == "__main__":
    run_experiment()
