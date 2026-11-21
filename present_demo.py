from datetime import datetime
from pathlib import Path
import json
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parent
PYTHON = Path(sys.executable)
sys.path.insert(0, str(ROOT / "src"))


def section(title, explanation):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)
    print(explanation, flush=True)


def pause():
    input("\nPress Enter when you are ready to continue...")


def run_script(relative_path):
    result = subprocess.run(
        [str(PYTHON), "-u", str(ROOT / relative_path)],
        cwd=ROOT,
    )
    if result.returncode:
        raise RuntimeError(f"Check failed: {relative_path}")


def preflight():
    required = [
        "src/contract_validator.py",
        "src/contract_router.py",
        "src/traced_contract_router.py",
        "src/test_contract_validator.py",
        "src/test_contract_router.py",
        "src/test_ollama_workflow_integration.py",
        "docs/W04_System_Architecture_Draft.md",
        "docs/W04_Requirements_Traceability_Draft.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(f"Required file missing: {name}")

    with urllib.request.urlopen(
        "http://localhost:11434/api/version", timeout=5
    ) as response:
        runtime = json.load(response)

    with urllib.request.urlopen(
        "http://localhost:11434/api/tags", timeout=5
    ) as response:
        inventory = json.load(response)

    if not any(
        model["name"] == "llama3.2:3b"
        for model in inventory.get("models", [])
    ):
        raise RuntimeError("The required llama3.2:3b model is unavailable.")

    print("Python:", sys.version.split()[0])
    print("Ollama:", runtime["version"])
    print("Model: llama3.2:3b")
    print("Required project files: present")

    run_script("src/test_contract_validator.py")
    run_script("src/test_contract_router.py")


def main():
    section(
        "PRE-DEMO CHECK",
        "Checking the project, local model service, validation, and routing.",
    )
    preflight()

    if "--check" in sys.argv:
        section(
            "LIVE MODEL REHEARSAL",
            "Checking the same model integration used during the presentation.",
        )
        run_script("src/test_ollama_workflow_integration.py")
        print("\nPASS: All pre-demo checks completed.", flush=True)
        return

    section(
        "1. PROJECT EXPLANATION",
        "A natural-language rule describes when an edge should be used.\n"
        "The model converts the rule into a structured condition.\n"
        "Python validates the contract and evaluates it against workflow data.\n"
        "The router records its decision and explanation.",
    )
    pause()

    from contract_validator import validate_contract
    from traced_contract_router import route_and_save_trace

    contracts = [
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

    section(
        "2. STRUCTURED CONTRACT",
        "This authored example makes the routing rule visible.\n"
        "The live model-generated example follows later.",
    )
    print(json.dumps(contracts[0], indent=4))
    if not all(validate_contract(contract) for contract in contracts):
        raise RuntimeError("The example contracts failed validation.")
    print("\nBoth example contracts passed structural validation.")
    pause()

    evidence = (
        ROOT / "docs" / "demo_runs"
        / datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    )
    evidence.mkdir(parents=True, exist_ok=False)

    section(
        "3. BOTH ROUTING SCENARIOS",
        "Passing tests select Deploy Code.\n"
        "Failing tests select Fix Code.\n"
        "Each decision creates a saved JSON trace.",
    )

    for state, expected in [(True, "Deploy Code"), (False, "Fix Code")]:
        execution = route_and_save_trace(
            contracts,
            "Check Tests",
            {"tests_passed": state},
            output_folder=str(evidence),
        )
        routing = execution["routing_result"]
        if routing["status"] != "ROUTED" or routing["next_node"] != expected:
            raise RuntimeError(f"Unexpected routing result: {routing}")

        trace_path = Path(execution["trace_file"])
        saved = json.loads(trace_path.read_text(encoding="utf-8"))
        if (
            saved["trace_id"] != execution["trace_id"]
            or saved["selected_next_node"] != expected
        ):
            raise RuntimeError("Saved trace differs from the routing outcome.")

        print(f"\ntests_passed = {state}")
        print("Selected node:", routing["next_node"])
        print("Explanation:", routing["decision_explanation"])
        print("Verified saved trace:", trace_path.name)

    print("\nPersistent demo evidence:", evidence)
    pause()

    section(
        "4. VALIDATION AND REPEATABILITY",
        "The existing tests check invalid contracts, missing conditions,\n"
        "NO_MATCH, AMBIGUOUS, and ten repeated routing decisions.",
    )
    run_script("src/test_contract_validator.py")
    run_script("src/test_contract_router.py")
    pause()

    section(
        "5. WEEK 5 LIVE MODEL PILOT",
        "Ollama now interprets two natural-language conditions.\n"
        "The existing integration test validates generated contracts,\n"
        "checks both routes, repeats routing, and verifies temporary traces.\n"
        "Please allow time for the two model calls.",
    )
    run_script("src/test_ollama_workflow_integration.py")

    section(
        "DEMO COMPLETE",
        "All executed checks passed.\n"
        f"The two authored-example traces remain available in:\n{evidence}",
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDemo stopped by presenter.")
        sys.exit(130)
    except Exception as error:
        print(f"\nDEMO CHECK FAILED: {type(error).__name__}: {error}")
        print("Resolve this issue before presenting.")
        sys.exit(1)
