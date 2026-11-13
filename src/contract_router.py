
# CISC 699 - A2 Research Project
# Deterministic Semantic Contract Router

from contract_evaluator import evaluate_contract
from contract_validator import validate_contract


def select_next_node_from_contracts(
    contracts, current_node, workflow_data
):
    """
    Legacy routing function.

    Returns a destination only when exactly one
    valid contract matches.

    Invalid contracts raise ValueError.
    Invalid workflow data does not produce a route.
    """

    matching_targets = []

    for contract in contracts:

        if not validate_contract(contract):
            raise ValueError("Invalid semantic contract")

    # Validate workflow data before evaluating contracts
    if not isinstance(workflow_data, dict):
        return None

    if type(workflow_data.get("tests_passed")) is not bool:
        return None

    for contract in contracts:

        if contract["source"] != current_node:
            continue

        if evaluate_contract(contract, workflow_data):
            matching_targets.append(contract["target"])

    if len(matching_targets) == 1:
        return matching_targets[0]

    return None


def route_with_explanation(
    contracts, current_node, workflow_data
):
    """
    Route using validated semantic contracts.

    Possible statuses:
    ROUTED
    NO_MATCH
    AMBIGUOUS
    INVALID_CONTRACT
    INVALID_WORKFLOW_DATA
    """

    matching_contracts = []
    validation_results = []

    # Step 1: Validate every supplied contract
    for contract in contracts:

        is_valid = validate_contract(contract)

        validation_results.append({
            "source": (
                contract.get("source")
                if isinstance(contract, dict) else None
            ),
            "target": (
                contract.get("target")
                if isinstance(contract, dict) else None
            ),
            "valid": is_valid
        })

    # Step 2: Reject invalid contracts
    if not all(
        record["valid"] for record in validation_results
    ):
        return {
            "status": "INVALID_CONTRACT",
            "next_node": None,
            "matched_contracts": [],
            "validation_results": validation_results,
            "decision_explanation": (
                "Contract validation failed. "
                "Routing was stopped."
            )
        }

    # Step 3: Identify outgoing contracts
    outgoing_contracts = [
        contract
        for contract in contracts
        if contract["source"] == current_node
    ]

    # Step 4: No outgoing contracts
    if len(outgoing_contracts) == 0:
        return {
            "status": "NO_MATCH",
            "next_node": None,
            "matched_contracts": [],
            "validation_results": validation_results,
            "decision_explanation": (
                "No outgoing contracts exist for the "
                "current workflow node. "
                "No destination was selected."
            )
        }

    # Step 5: Validate workflow data
    if not isinstance(workflow_data, dict):
        return {
            "status": "INVALID_WORKFLOW_DATA",
            "next_node": None,
            "matched_contracts": [],
            "validation_results": validation_results,
            "decision_explanation": (
                "Workflow data must be a dictionary. "
                "Routing was stopped."
            )
        }

    if type(workflow_data.get("tests_passed")) is not bool:
        return {
            "status": "INVALID_WORKFLOW_DATA",
            "next_node": None,
            "matched_contracts": [],
            "validation_results": validation_results,
            "decision_explanation": (
                "The required tests_passed field is "
                "missing or is not a Boolean value. "
                "Routing was stopped."
            )
        }

    # Step 6: Evaluate outgoing contracts
    for contract in outgoing_contracts:

        if evaluate_contract(contract, workflow_data):
            matching_contracts.append(contract)

    # Step 7: Exactly one matching contract
    if len(matching_contracts) == 1:

        next_node = matching_contracts[0]["target"]

        return {
            "status": "ROUTED",
            "next_node": next_node,
            "matched_contracts": matching_contracts,
            "validation_results": validation_results,
            "decision_explanation": (
                "Exactly one contract matched. "
                "Routing to " + next_node + "."
            )
        }

    # Step 8: No matching contracts
    if len(matching_contracts) == 0:
        return {
            "status": "NO_MATCH",
            "next_node": None,
            "matched_contracts": [],
            "validation_results": validation_results,
            "decision_explanation": (
                "No contracts matched the current workflow state. "
                "No destination was selected."
            )
        }

    # Step 9: Multiple matching contracts
    return {
        "status": "AMBIGUOUS",
        "next_node": None,
        "matched_contracts": matching_contracts,
        "validation_results": validation_results,
        "decision_explanation": (
            "Multiple contracts matched the current "
            "workflow state. Routing was stopped "
            "to avoid an ambiguous decision."
        )
    }
