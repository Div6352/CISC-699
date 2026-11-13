
# CISC 699 - Capstone II A2 Research
# Independent Direct Natural-Language Routing Evaluation

import json
import time
from pathlib import Path

from direct_nl_llm_router import direct_nl_llm_route
from independent_evaluation_dataset import independent_evaluation_cases


CURRENT_NODE = "Check Tests"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "independent_direct_nl_results.json"
)

ORIGINAL_PASS_EDGE = (
    "If all software tests have passed, proceed to deployment."
)

ORIGINAL_FAIL_EDGE = (
    "If any software test has failed, return to fixing the code."
)


def make_edges(case):
    """
    Replace only the edge corresponding to the case's
    expected semantic meaning.

    The expected value is used to construct the
    evaluation scenario, not passed to the LLM.
    """

    pass_description = ORIGINAL_PASS_EDGE
    fail_description = ORIGINAL_FAIL_EDGE

    if case["expected_value"] is True:
        pass_description = case["text"]
    else:
        fail_description = case["text"]

    return [
        {
            "edge_id": "E01",
            "source": CURRENT_NODE,
            "target": "Deploy Code",
            "text": pass_description
        },
        {
            "edge_id": "E02",
            "source": CURRENT_NODE,
            "target": "Fix Code",
            "text": fail_description
        }
    ]


def run_experiment():
    records = []

    print("\nIndependent Direct NL Routing Evaluation")
    print("=" * 55)

    for case in independent_evaluation_cases:
        edges = make_edges(case)

        # Evaluate the workflow state that should satisfy
        # the independently paraphrased edge.
        workflow_data = {
            "tests_passed": case["expected_value"]
        }

        expected_target = (
            "Deploy Code"
            if case["expected_value"] is True
            else "Fix Code"
        )

        start = time.perf_counter()

        actual_target = direct_nl_llm_route(
            edges,
            CURRENT_NODE,
            workflow_data
        )

        elapsed = time.perf_counter() - start

        correct = actual_target == expected_target

        records.append({
            "case_id": case["case_id"],
            "paraphrase": case["text"],
            "expected_value": case["expected_value"],
            "edges": edges,
            "workflow_data": workflow_data,
            "expected_target": expected_target,
            "actual_target": actual_target,
            "correct": correct,
            "seconds": elapsed
        })

        print(
            f"{case['case_id']}: "
            f"expected={expected_target}, "
            f"actual={actual_target}, "
            f"correct={correct}"
        )

    total = len(records)
    correct_count = sum(
        record["correct"] for record in records
    )

    total_seconds = sum(
        record["seconds"] for record in records
    )

    summary = {
        "total_cases": total,
        "correct_cases": correct_count,
        "accuracy": (
            correct_count / total if total else 0.0
        ),
        "total_seconds": total_seconds,
        "average_seconds": (
            total_seconds / total if total else None
        ),
        "limitations": [
            "Each case substitutes one natural-language edge.",
            "The opposite edge retains its original wording.",
            "Each case evaluates only the workflow state "
            "expected to satisfy the substituted edge.",
            "Expected values are used for benchmark setup "
            "and scoring, not included in the LLM prompt.",
            "The experiment makes one LLM call per case.",
            "This experiment does not measure repeatability.",
            "This experiment is not a complete matched "
            "end-to-end comparison against structured routing."
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

    print("\n" + "=" * 55)
    print("INDEPENDENT DIRECT NL SUMMARY")
    print("Total cases:", total)
    print("Correct cases:", correct_count)
    print(f"Accuracy: {summary['accuracy']:.1%}")
    print(
        "Total seconds:",
        round(total_seconds, 4)
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Experiment completed.")


if __name__ == "__main__":
    run_experiment()
