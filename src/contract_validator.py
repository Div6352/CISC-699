
# CISC 699 - A2 Research Project
# Semantic Contract Validator

def validate_contract(contract):

    if not isinstance(contract, dict):
        return False

    # Validate source node
    source = contract.get("source")

    if not isinstance(source, str) or not source.strip():
        return False

    # Validate target node
    target = contract.get("target")

    if not isinstance(target, str) or not target.strip():
        return False

    # Validate optional edge identifier
    if "edge_id" in contract:
        edge_id = contract["edge_id"]

        if not isinstance(edge_id, str) or not edge_id.strip():
            return False

    # Validate semantic condition
    condition = contract.get("condition")

    if not isinstance(condition, dict):
        return False

    if condition.get("field") != "tests_passed":
        return False

    if condition.get("operator") != "equals":
        return False

    if type(condition.get("value")) is not bool:
        return False

    return True
