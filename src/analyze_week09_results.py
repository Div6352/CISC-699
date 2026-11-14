import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "docs/comparison_runs/20261114T072805Z-7fea28e98cfa"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    manifest = read_json(RUN / "manifest.json")
    summary = read_json(RUN / "summary.json")
    provenance = read_json(RUN / "provenance.json")
    dataset = (ROOT / manifest["dataset"]).read_bytes()
    require(
        hashlib.sha256(dataset).hexdigest() == manifest["dataset_sha256"],
        "Benchmark fingerprint differs from the run manifest.",
    )

    cases = ast.literal_eval(ast.parse(dataset).body[-1].value)
    routes = {
        case["case_id"]: "Deploy Code" if case["expected_value"] else "Fix Code"
        for case in cases
    }

    rows = [read_json(path) for path in sorted(RUN.glob("IND*.json"))]
    keys = [(row["case_id"], row["repetition"]) for row in rows]
    planned = {tuple(pair) for pair in manifest["planned_case_repetitions"]}
    require(
        len(keys) == len(planned) == 30 and set(keys) == planned,
        "Saved observations do not match the 30 planned groups.",
    )

    run_id = manifest["run_id"]
    require(
        summary["run_id"] == provenance["run_id"] == run_id
        and all(row["run_id"] == run_id for row in rows),
        "Run IDs differ across the evidence files.",
    )

    for method in manifest["methods_in_order"]:
        correct = 0
        total_seconds = 0.0

        for row in rows:
            expected = routes[row["case_id"]]
            decision = row[method]
            hit = (
                decision["result"] == expected
                and decision.get("status", "ROUTED") == "ROUTED"
            )
            require(
                row["expected_target"] == expected and decision["correct"] == hit,
                f"Score mismatch for {row['case_id']}, repetition "
                f"{row['repetition']}, {method}.",
            )
            correct += hit
            total_seconds += decision["seconds"]

        saved = summary["summary"][method]
        require(
            saved["total"] == len(rows)
            and saved["correct"] == correct
            and abs(saved["total_seconds"] - total_seconds) < 1e-6,
            f"Summary mismatch for {method}.",
        )
        print(
            f"{method}: {correct}/{len(rows)} correct, "
            f"{total_seconds:.2f} s total, {total_seconds / len(rows):.2f} s mean"
        )

    print("PASS: Frozen benchmark, saved decisions, and summary reconcile.")


if __name__ == "__main__":
    main()
