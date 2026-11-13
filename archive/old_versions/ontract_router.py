
# CISC 699 - A2 Research Project
# Deterministic Semantic Contract Router

from contract_evaluator import evaluate_contract


def select_next_node_from_contracts(
    contracts, current_node, workflow_data
):
    matching_targets = []

    for contract in contracts:

        # Consider only edges from the current node
        if contract["source"] != current_node:
            continue

        # Evaluate the semantic contract
        if evaluate_contract(contract, workflow_data):
            matching_targets.append(contract["target"])

    # Exactly one matching edge is required
    if len(matching_targets) == 1:
        return matching_targets[0]

    # No match or multiple matches: do not route
    return None
