
# CISC 699 - Capstone II A2 Research
# Semantic Contract Validator

def validate_contract(contract):
    """
    Validate the structural properties of a semantic contract.

    Checks:
    - Contract must be a dictionary.
    - Source and target nodes must be non-empty strings.
    - Optional edge_id must be a non-empty string.
    - Condition must use the supported tests_passed field.
    - Comparison operator must be equals.
    - Expected condition value must be a Boolean.

    Note:
    Structural validation does not establish semantic correctness
    or graph-transition permission. These responsibilities are
    handled by separate components.
    """

    # Step 1: Validate contract structure
    if not isinstance(contract, dict):
        return False

    # Step 2: Validate source node
    source = contract.get("source")

    if not isinstance(source, str) or not source.strip():
        return False

    # Step 3: Validate target node
    target = contract.get("target")

    if not isinstance(target, str) or not target.strip():
        return False

    # Step 4: Validate optional edge identifier
    if "edge_id" in contract:
        edge_id = contract["edge_id"]

        if not isinstance(edge_id, str) or not edge_id.strip():
            return False

    # Step 5: Validate semantic condition
    condition = contract.get("condition")

    if not isinstance(condition, dict):
        return False

    # Step 6: Validate supported condition field
    if condition.get("field") != "tests_passed":
        return False

    # Step 7: Validate supported comparison operator
    if condition.get("operator") != "equals":
        return False

    # Step 8: Require an actual Boolean value
    if type(condition.get("value")) is not bool:
        return False

    return True
