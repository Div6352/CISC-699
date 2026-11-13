
# CISC 699 - Capstone II A2 Research
# Complete Prototype Workflow Path and Trace Evaluation

import json
from datetime import datetime, timezone
from pathlib import Path

from graph import nodes, edges
from traced_contract_router import route_and_save_trace


REPEATS = 10

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = (
    PROJECT_ROOT
    / "docs"
    / "workflow_path_trace_experiment_results.json"
)

TRACE_FOLDER = (
    PROJECT_ROOT
    / "docs"
    / "workflow_path_trace_experiment_traces"
)

START_NODE = "Check Tests"

REQUIRED_TRACE_FIELDS = {
    "trace_id",
    "timestamp",
    "current_node",
    "workflow_data",
    "evaluated_contracts",
    "routing_status",
    "selected_next_node",
    "matched_contracts",
    "validation_results",
    "decision_explanation",
}


def make_reference_contracts():
    """
    Explicitly authored reference contracts.

    This experiment isolates deterministic workflow
    execution and trace persistence. It does not test
    LLM interpretation accuracy.
    """
    return [
        {
            "edge_id": "E01",
            "source": "Check Tests",
            "target": "Deploy Code",
            "condition": {
                "field": "tests_passed",
                "operator": "equals",
                "value": True,
            },
        },
        {
            "edge_id": "E02",
            "source": "Check Tests",
            "target": "Fix Code",
            "condition": {
                "field": "tests_passed",
                "operator": "equals",
                "value": False,
            },
        },
    ]


def terminal_nodes():
    return {
        node
        for node in nodes
        if not any(edge["source"] == node for edge in edges)
    }


def run_one_workflow(contracts, workflow_data):
    path = [START_NODE]
    trace_files = []
    trace_ids = []
    trace_checks = []

    current_node = START_NODE
    visited = set()
    terminals = terminal_nodes()

    while current_node not in terminals:
        if current_node in visited:
            return {
                "path": path,
                "status": "CYCLE_DETECTED",
                "trace_files": trace_files,
                "trace_ids": trace_ids,
                "trace_checks": trace_checks,
            }

        visited.add(current_node)

        result = route_and_save_trace(
            contracts,
            current_node,
            workflow_data,
            output_folder=str(TRACE_FOLDER),
        )

        routing = result["routing_result"]
        trace_path = Path(result["trace_file"])

        trace_exists = trace_path.is_file()

        if trace_exists:
            with trace_path.open("r", encoding="utf-8") as file:
                saved_trace = json.load(file)

            fields_present = REQUIRED_TRACE_FIELDS.issubset(
                saved_trace.keys()
            )

            trace_matches_result = (
                saved_trace["trace_id"] == result["trace_id"]
                and saved_trace["current_node"] == current_node
                and saved_trace["workflow_data"] == workflow_data
                and saved_trace["routing_status"] == routing["status"]
                and saved_trace["selected_next_node"]
                == routing["next_node"]
            )
        else:
            fields_present = False
            trace_matches_result = False

        trace_files.append(str(trace_path))
        trace_ids.append(result["trace_id"])

        trace_checks.append(
            {
                "exists": trace_exists,
                "required_fields_present": fields_present,
                "matches_routing_result": trace_matches_result,
            }
        )

        if routing["status"] != "ROUTED":
            return {
                "path": path,
                "status": routing["status"],
                "trace_files": trace_files,
                "trace_ids": trace_ids,
                "trace_checks": trace_checks,
            }

        next_node = routing["next_node"]

        if next_node is None:
            return {
                "path": path,
                "status": "MISSING_NEXT_NODE",
                "trace_files": trace_files,
                "trace_ids": trace_ids,
                "trace_checks": trace_checks,
            }

        path.append(next_node)
        current_node = next_node

    return {
        "path": path,
        "status": "COMPLETED",
        "trace_files": trace_files,
        "trace_ids": trace_ids,
        "trace_checks": trace_checks,
    }


def run_experiment():
    # Exclusive output creation prevents overwriting results.
    if OUTPUT_FILE.exists():
        raise FileExistsError(
            f"Results already exist: {OUTPUT_FILE}"
        )

    if TRACE_FOLDER.exists():
        raise FileExistsError(
            f"Trace folder already exists: {TRACE_FOLDER}"
        )

    contracts = make_reference_contracts()
    records = []

    scenarios = [
        {
            "name": "tests_pass",
            "workflow_data": {"tests_passed": True},
            "expected_path": ["Check Tests", "Deploy Code"],
        },
        {
            "name": "tests_fail",
            "workflow_data": {"tests_passed": False},
            "expected_path": ["Check Tests", "Fix Code"],
        },
    ]

    for scenario in scenarios:
        for repetition in range(1, REPEATS + 1):
            result = run_one_workflow(
                contracts,
                scenario["workflow_data"],
            )

            correct_path = (
                result["status"] == "COMPLETED"
                and result["path"] == scenario["expected_path"]
            )

            record = {
                "scenario": scenario["name"],
                "repetition": repetition,
                "workflow_data": scenario["workflow_data"],
                "expected_path": scenario["expected_path"],
                "observed_path": result["path"],
                "status": result["status"],
                "correct_path": correct_path,
                "trace_files": result["trace_files"],
                "trace_ids": result["trace_ids"],
                "trace_checks": result["trace_checks"],
            }

            records.append(record)

            print(
                scenario["name"],
                f"repetition {repetition}/{REPEATS}",
                "| path:", " -> ".join(result["path"]),
                "| correct:", correct_path,
            )

    all_trace_ids = [
        trace_id
        for record in records
        for trace_id in record["trace_ids"]
    ]

    all_trace_files = [
        filename
        for record in records
        for filename in record["trace_files"]
    ]

    all_trace_checks = [
        check
        for record in records
        for check in record["trace_checks"]
    ]

    correct_paths = sum(
        record["correct_path"]
        for record in records
    )

    trace_checks_passed = sum(
        check["exists"]
        and check["required_fields_present"]
        and check["matches_routing_result"]
        for check in all_trace_checks
    )

    scenario_stability = {}

    for scenario in scenarios:
        scenario_records = [
            record
            for record in records
            if record["scenario"] == scenario["name"]
        ]

        observed = {
            (
                record["status"],
                tuple(record["observed_path"]),
            )
            for record in scenario_records
        }

        scenario_stability[scenario["name"]] = (
            len(observed) == 1
        )

    summary = {
        "total_scenarios": len(scenarios),
        "repeats_per_scenario": REPEATS,
        "total_workflow_runs": len(records),
        "correct_paths": correct_paths,
        "path_accuracy": (
            correct_paths / len(records)
            if records else 0.0
        ),
        "scenario_stability": scenario_stability,
        "total_trace_files": len(all_trace_files),
        "unique_trace_ids": len(set(all_trace_ids)),
        "unique_trace_filenames": len(set(all_trace_files)),
        "trace_checks_passed": trace_checks_passed,
        "total_trace_checks": len(all_trace_checks),
    }

    output = {
        "experiment": "workflow_path_trace_evaluation",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "contract_source": "manually_authored_reference_contracts",
        "summary": summary,
        "records": records,
        "limitations": [
            "Three-node workflow with two permitted transitions.",
            "Each complete workflow path contains one routed edge.",
            "Contracts are manually authored, not generated by an LLM.",
            "Two Boolean workflow states are evaluated.",
            "No external agent or software deployment is executed.",
            "No LLM interpretation accuracy is measured.",
            "Unexpected exceptions may prevent trace creation.",
            "Trace validation checks required fields and selected values.",
        ],
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    print("\n" + "=" * 65)
    print("WORKFLOW PATH AND TRACE SUMMARY")
    print(
        "Correct paths:",
        f"{correct_paths}/{len(records)}",
    )
    print(
        "Path accuracy:",
        f"{summary['path_accuracy']:.1%}",
    )
    print(
        "Stable scenarios:",
        f"{sum(scenario_stability.values())}/{len(scenarios)}",
    )
    print(
        "Trace files:",
        summary["total_trace_files"],
    )
    print(
        "Unique trace IDs:",
        summary["unique_trace_ids"],
    )
    print(
        "Unique trace filenames:",
        summary["unique_trace_filenames"],
    )
    print(
        "Trace checks passed:",
        f"{trace_checks_passed}/{len(all_trace_checks)}",
    )
    print("Results saved to:", OUTPUT_FILE)
    print("Trace folder:", TRACE_FOLDER)


if __name__ == "__main__":
    run_experiment()
