
# CISC 699 - Capstone II A2 Research
# Ollama Semantic Contract and Workflow Integration Test

from pathlib import Path
from tempfile import TemporaryDirectory
import json

from ollama_structured_interpreter import interpret_with_structured_ollama
from contract_validator import validate_contract
from traced_contract_router import route_and_save_trace


def build_ollama_contract(edge_id, target, sentence):
    condition = interpret_with_structured_ollama(sentence)

    assert condition is not None, (
        f"{edge_id}: Ollama did not return a valid condition"
    )

    contract = {
        "edge_id": edge_id,
        "source": "Check Tests",
        "target": target,
        "condition": condition
    }

    assert validate_contract(contract), (
        f"{edge_id}: Invalid semantic contract"
    )

    return contract


def check_routing(contracts, tests_passed, expected_node, folder):
    execution = route_and_save_trace(
        contracts,
        "Check Tests",
        {"tests_passed": tests_passed},
        output_folder=folder
    )

    result = execution["routing_result"]

    assert result["status"] == "ROUTED", result
    assert result["next_node"] == expected_node, result
    assert len(result["matched_contracts"]) == 1, result
    assert result["decision_explanation"], result

    trace_file = Path(execution["trace_file"])

    assert trace_file.is_file(), "Execution trace was not saved"

    with trace_file.open("r", encoding="utf-8") as file:
        trace = json.load(file)

    assert trace["trace_id"] == execution["trace_id"]
    assert trace["routing_status"] == "ROUTED"
    assert trace["selected_next_node"] == expected_node
    assert trace["workflow_data"]["tests_passed"] is tests_passed
    assert trace["decision_explanation"]

    return result, execution["trace_id"]


print("\nA2 Research - Ollama Workflow Integration Test")

# Step 1: Interpret natural-language edge conditions.
contracts = [
    build_ollama_contract(
        "EDGE01",
        "Deploy Code",
        "If all software tests have passed, proceed to deployment."
    ),
    build_ollama_contract(
        "EDGE02",
        "Fix Code",
        "If any software test has failed, return to fixing the code."
    )
]

print("Ollama contract generation and validation: PASS")

# Step 2: Run deterministic routing and save execution traces.
with TemporaryDirectory() as temporary_folder:
    passed_result, passed_trace_id = check_routing(
        contracts, True, "Deploy Code", temporary_folder
    )

    print("Tests passed routing: PASS")

    failed_result, failed_trace_id = check_routing(
        contracts, False, "Fix Code", temporary_folder
    )

    print("Tests failed routing: PASS")

    # Step 3: Repeat the same routing decision.
    trace_ids = {passed_trace_id, failed_trace_id}

    for _ in range(10):
        repeated_result, trace_id = check_routing(
            contracts, True, "Deploy Code", temporary_folder
        )

        assert repeated_result == passed_result
        assert trace_id not in trace_ids
        trace_ids.add(trace_id)

    print("Repeated deterministic routing: PASS")
    print("Automatic execution trace saving: PASS")
    print("Unique execution trace identifiers: PASS")

    assert len(list(Path(temporary_folder).glob("trace_*.json"))) == 12

print("\nOverall result: PASS")
print("All Ollama workflow integration tests passed!")
