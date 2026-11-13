
# CISC 699 - A2 Research Project
# Natural-Language Contract Builder

from nl_interpreter import interpret_condition
from contract_validator import validate_contract


def build_contract(edge):

    # Interpret the English-language condition
    condition = interpret_condition(edge["condition"])

    # Reject unrecognized language
    if condition is None:
        return None

    # Build the structured contract
    contract = {
        "edge_id": edge["edge_id"],
        "source": edge["source"],
        "target": edge["target"],
        "condition": condition
    }

    # Validate the generated contract
    if not validate_contract(contract):
        return None

    return contract
