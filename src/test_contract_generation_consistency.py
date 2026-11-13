
# CISC 699 - Capstone II A2 Research
# Independent Semantic Contract Generation Consistency Experiment

import json
import time
from pathlib import Path

from independent_evaluation_dataset import independent_evaluation_cases
from ollama_structured_interpreter import interpret_with_structured_ollama


REPEATS = 3

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "independent_interpretation_consistency_results.json"
)


def normalize_condition(condition):
    """Convert a valid interpretation into a comparable value."""
    if (
        isinstance(condition, dict)
        and condition.get("field") == "tests_passed"
        and condition.get("operator") == "equals"
        and type(condition.get("value")) is bool
    ):
        return condition["value"]

    return None


def run_experiment():
    print("\nA2 Research - Independent Interpretation Consistency")
    print("=" * 60)

    case_results = []

    for case in independent_evaluation_cases:
        case_id = case["case_id"]
        text = case["text"]
        expected_value = case["expected_value"]

        print(f"\nScenario: {case_id}")
        print("Condition:", text)

        runs = []

        for run_number in range(1, REPEATS + 1):
            start = time.perf_counter()

            try:
                condition = interpret_with_structured_ollama(text)
                error = None
            except Exception as exc:
                condition = None
                error = f"{type(exc).__name__}: {exc}"

            elapsed = time.perf_counter() - start
            predicted_value = normalize_condition(condition)

            correct = (
                predicted_value is expected_value
            )

            runs.append({
                "run": run_number,
                "condition": condition,
                "predicted_value": predicted_value,
                "correct": correct,
                "seconds": elapsed,
                "error": error
            })

            print(
                f"Run {run_number}: "
                f"predicted={predicted_value}, "
                f"expected={expected_value}, "
                f"correct={correct}"
            )

        predictions = [
            run["predicted_value"]
            for run in runs
        ]

        unique_predictions = set(predictions)
        all_identical = len(unique_predictions) == 1

        correct_runs = sum(
            run["correct"] for run in runs
        )

        case_results.append({
            "case_id": case_id,
            "text": text,
            "expected_value": expected_value,
            "runs": runs,
            "correct_runs": correct_runs,
            "unique_predictions": len(unique_predictions),
            "all_identical": all_identical
        })

        print("Correct runs:", f"{correct_runs}/{REPEATS}")
        print("All predictions identical:", all_identical)

    total_runs = sum(
        len(case["runs"])
        for case in case_results
    )

    correct_runs = sum(
        case["correct_runs"]
        for case in case_results
    )

    stable_cases = sum(
        case["all_identical"]
        for case in case_results
    )

    total_seconds = sum(
        run["seconds"]
        for case in case_results
        for run in case["runs"]
    )

    summary = {
        "experiment": "Independent interpretation consistency",
        "model": "llama3.2:3b",
        "temperature": 0,
        "total_cases": len(case_results),
        "repeats_per_case": REPEATS,
        "total_runs": total_runs,
        "correct_runs": correct_runs,
        "accuracy": (
            correct_runs / total_runs
            if total_runs else 0.0
        ),
        "stable_cases": stable_cases,
        "case_stability_rate": (
            stable_cases / len(case_results)
            if case_results else 0.0
        ),
        "total_seconds": total_seconds,
        "average_seconds_per_run": (
            total_seconds / total_runs
            if total_runs else None
        ),
        "limitations": [
            "Only ten independent paraphrases are tested.",
            "Each case is repeated three times.",
            "Temperature zero does not guarantee identical outputs.",
            "Stability is measured using normalized Boolean predictions.",
            "Identical incorrect predictions count as stable.",
            "The experiment evaluates interpretation, not routing.",
            "Results may vary across model versions and environments."
        ]
    }

    output = {
        "summary": summary,
        "cases": case_results
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
    print("CONSISTENCY SUMMARY")
    print("Total cases:", summary["total_cases"])
    print("Total runs:", summary["total_runs"])
    print(
        "Correct interpretations:",
        f"{correct_runs}/{total_runs}"
    )
    print(
        "Interpretation accuracy:",
        f"{summary['accuracy']:.1%}"
    )
    print(
        "Stable cases:",
        f"{stable_cases}/{len(case_results)}"
    )
    print(
        "Case stability rate:",
        f"{summary['case_stability_rate']:.1%}"
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Experiment completed.")


if __name__ == "__main__":
    run_experiment()
