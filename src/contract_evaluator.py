
# CISC 699 - A2 Research Project
# Deterministic Semantic Contract Evaluator

from contract_validator import validate_contract


def evaluate_contract(contract, workflow_data):
    """
    Validate and evaluate a semantic contract
    against the current workflow data.

    Returns:
        True if the condition matches.
        False if the condition does not match.

    Raises:
        ValueError if the contract is invalid.
    """

    # Step 1: Validate the semantic contract
    if not validate_contract(contract):
        raise ValueError("Invalid semantic contract")

    # Step 2: Extract the structured condition
    condition = contract["condition"]

    field = condition["field"]
    expected_value = condition["value"]

    # Step 3: Read the actual workflow value
    actual_value = workflow_data.get(field)

    # Step 4: Compare Boolean values strictly
    if type(actual_value) is not bool:
        return False

    return actual_value is expected_value
