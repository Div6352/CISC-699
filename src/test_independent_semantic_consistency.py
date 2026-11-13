
# CISC 699 - Capstone II A2 Research
# Saved Independent Semantic Consistency Evaluation
#
# Uses existing experiment results.
# Does not call Ollama or modify previous results.

import json
from pathlib import Path

from semantic_consistency_validator import (
    validate_semantic_consistency
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "matched_independent_nl_results.json"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "independent_semantic_consistency_results.json"
)


def run_evaluation():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        experiment = json.load(file)

    results = []

    for case in experiment["records"]:
        expected_value = case["expected_value"]

        target_edge_id = (
            "E01" if expected_value is True else "E02"
        )

        matching = [
            item
            for item in case["interpretations"]
            if item["edge_id"] == target_edge_id
        ]

        if len(matching) != 1:
            result = {
                "valid": False,
                "status": "MISSING_OR_DUPLICATE_EDGE",
                "expected_value": expected_value,
                "actual_value": None
            }
        else:
            interpretation = matching[0]
            condition = interpretation["predicted_condition"]

            contract = {
                "edge_id": target_edge_id,
                "source": "Check Tests",
                "target": (
                    "Deploy Code"
                    if target_edge_id == "E01"
                    else "Fix Code"
                ),
                "condition": condition
            }

            result = validate_semantic_consistency(
                contract,
                expected_value
            )

        results.append({
            "case_id": case["case_id"],
            "expected_value": expected_value,
            "semantic_validation": result,
            "structured_status": case["structured_status"],
            "structured_correct": case["structured_correct"]
        })

    total = len(results)

    matches = sum(
        item["semantic_validation"]["status"]
        == "SEMANTIC_MATCH"
        for item in results
    )

    mismatches = sum(
        item["semantic_validation"]["status"]
        == "SEMANTIC_MISMATCH"
        for item in results
    )

    other_failures = total - matches - mismatches

    summary = {
        "total_cases": total,
        "semantic_matches": matches,
        "semantic_mismatches": mismatches,
        "other_validation_failures": other_failures,
        "semantic_match_rate": (
            matches / total if total else 0.0
        ),
        "evaluation_type": (
            "Oracle-based retrospective semantic validation"
        ),
        "production_semantic_verification": False
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with OUTPUT_FILE.open(
        "w", encoding="utf-8"
    ) as file:
        json.dump(
            {
                "summary": summary,
                "records": results
            },
            file,
            indent=4
        )

    print("\nINDEPENDENT SEMANTIC CONSISTENCY RESULTS")
    print("=" * 50)

    for item in results:
        print(
            f"{item['case_id']}: "
            f"{item['semantic_validation']['status']}"
        )

    print("\nTotal cases:", total)
    print("Semantic matches:", matches)
    print("Semantic mismatches:", mismatches)
    print("Other validation failures:", other_failures)
    print(f"Semantic match rate: {summary['semantic_match_rate']:.1%}")
    print("Results saved to:", OUTPUT_FILE)
    print("Evaluation completed.")


if __name__ == "__main__":
    run_evaluation()
