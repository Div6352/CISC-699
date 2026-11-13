
# CISC 699 - Capstone II A2 Research
# Matched Independent Natural-Language Workflow Comparison

import json
import time
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
from direct_nl_llm_router import direct_nl_llm_route
from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from contract_router import route_with_explanation
from graph import is_permitted_transition


CURRENT_NODE = "Check Tests"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = (
    PROJECT_ROOT / "docs" / "matched_independent_nl_results.json"
)

ORIGINAL_PASS_EDGE = (
    "If all software tests have passed, proceed to deployment."
)

ORIGINAL_FAIL_EDGE = (
    "If any software test has failed, return to fixing the code."
)


def make_edges(case):
    """
    Replace one original edge with the independent paraphrase.

    The benchmark's expected_value determines which edge
    is replaced. It is not sent to either LLM.
    """

    pass_text = ORIGINAL_PASS_EDGE
    fail_text = ORIGINAL_FAIL_EDGE

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
            "expected_value": True
        },
        {
            "edge_id": "E02",
            "source": CURRENT_NODE,
            "target": "Fix Code",
            "text": fail_text,
            "expected_value": False
        }
    ]


def build_contracts(edges):
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
                "condition": condition
            }

            valid_contract = (
                validate_contract(contract)
                and is_permitted_transition(
                    edge["source"],
                    edge["target"]
                )
            )

            if valid_contract:
                contracts.append(contract)

        interpretation_records.append({
            "edge_id": edge["edge_id"],
            "text": edge["text"],
            "expected_value": edge["expected_value"],
            "predicted_condition": condition,
            "interpretation_correct": interpretation_correct,
            "contract_valid": valid_contract,
            "seconds": elapsed,
            "error": error
        })

    construction_seconds = (
        time.perf_counter() - start_total
    )

    return contracts, interpretation_records, construction_seconds


def run_experiment():
    records = []

    print("\nMatched Independent NL Comparison")
    print("=" * 60)

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

        # Direct LLM receives the workflow state
        # and the same natural-language edge descriptions.
        direct_start = time.perf_counter()

        direct_result = direct_nl_llm_route(
            edges,
            CURRENT_NODE,
            workflow_data
        )

        direct_seconds = (
            time.perf_counter() - direct_start
        )

        # Structured method independently interprets
        # both edge descriptions for this case.
        contracts, interpretations, construction_seconds = (
            build_contracts(edges)
        )

        structured_start = time.perf_counter()

        routing_result = route_with_explanation(
            contracts,
            CURRENT_NODE,
            workflow_data
        )

        structured_routing_seconds = (
            time.perf_counter() - structured_start
        )

        structured_target = routing_result["next_node"]
        structured_status = routing_result["status"]

        if (
            structured_status == "ROUTED"
            and not is_permitted_transition(
                CURRENT_NODE,
                structured_target
            )
        ):
            structured_target = None
            structured_status = "INVALID_GRAPH_TRANSITION"

        record = {
            "case_id": case["case_id"],
            "paraphrase": case["text"],
            "expected_value": case["expected_value"],
            "workflow_data": workflow_data,
            "expected_target": expected_target,
            "edges": edges,
            "direct_result": direct_result,
            "direct_correct": direct_result == expected_target,
            "direct_seconds": direct_seconds,
            "structured_result": structured_target,
            "structured_status": structured_status,
            "structured_correct": (
                structured_status == "ROUTED"
                and structured_target == expected_target
            ),
            "structured_construction_seconds": construction_seconds,
            "structured_routing_seconds": structured_routing_seconds,
            "interpretations": interpretations
        }

        records.append(record)

        print(
            f"{case['case_id']}: "
            f"direct={direct_result}, "
            f"structured={structured_target}, "
            f"expected={expected_target}"
        )

    total = len(records)

    direct_correct = sum(
        record["direct_correct"] for record in records
    )

    structured_correct = sum(
        record["structured_correct"] for record in records
    )

    direct_seconds = sum(
        record["direct_seconds"] for record in records
    )

    structured_construction_seconds = sum(
        record["structured_construction_seconds"]
        for record in records
    )

    structured_routing_seconds = sum(
        record["structured_routing_seconds"]
        for record in records
    )

    structured_total_seconds = (
        structured_construction_seconds
        + structured_routing_seconds
    )

    paraphrase_interpretations = []

    for record in records:
        target_edge_id = (
            "E01"
            if record["expected_value"] is True
            else "E02"
        )

        matching = [
            item
            for item in record["interpretations"]
            if item["edge_id"] == target_edge_id
        ]

        paraphrase_interpretations.extend(matching)

    correct_paraphrase_interpretations = sum(
        item["interpretation_correct"]
        for item in paraphrase_interpretations
    )

    summary = {
        "total_cases": total,
        "direct_correct": direct_correct,
        "structured_correct": structured_correct,
        "direct_accuracy": (
            direct_correct / total if total else 0.0
        ),
        "structured_accuracy": (
            structured_correct / total if total else 0.0
        ),
        "correct_paraphrase_interpretations": (
            correct_paraphrase_interpretations
        ),
        "total_paraphrase_interpretations": len(
            paraphrase_interpretations
        ),
        "total_direct_seconds": direct_seconds,
        "total_structured_construction_seconds": (
            structured_construction_seconds
        ),
        "total_structured_routing_seconds": (
            structured_routing_seconds
        ),
        "total_structured_seconds": (
            structured_total_seconds
        ),
        "limitations": [
            "Ten independent paraphrases are evaluated once each.",
            "Each case replaces one edge description.",
            "The opposite edge retains its original wording.",
            "Each case tests one workflow state.",
            "The benchmark oracle determines the substituted "
            "edge and expected destination.",
            "Both methods receive the same natural-language "
            "edge descriptions.",
            "The structured interpreter also receives explicit "
            "Boolean interpretation guidance.",
            "The structured method makes two interpretation "
            "calls per case, while the direct method makes "
            "one routing call.",
            "Structured contracts are rebuilt for each case.",
            "The experiment does not measure execution-trace "
            "persistence or full workflow execution."
        ]
    }

    output = {
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
    print("MATCHED INDEPENDENT SUMMARY")
    print("Total cases:", total)
    print(
        "Direct correct:",
        f"{direct_correct}/{total}"
    )
    print(
        "Structured correct:",
        f"{structured_correct}/{total}"
    )
    print(
        "Direct accuracy:",
        f"{summary['direct_accuracy']:.1%}"
    )
    print(
        "Structured accuracy:",
        f"{summary['structured_accuracy']:.1%}"
    )
    print(
        "Paraphrase interpretations correct:",
        f"{correct_paraphrase_interpretations}"
        f"/{len(paraphrase_interpretations)}"
    )
    print(
        "Total direct seconds:",
        round(direct_seconds, 4)
    )
    print(
        "Total structured seconds:",
        round(structured_total_seconds, 4)
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Experiment completed.")


if __name__ == "__main__":
    run_experiment()
