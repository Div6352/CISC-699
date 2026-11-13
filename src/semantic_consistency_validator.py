
# CISC 699 - Capstone II A2 Research
# Oracle-Based Semantic Consistency Validation
#
# Research evaluation only:
# The expected Boolean value must come from an
# independently annotated benchmark, not from
# the model's generated contract.


def validate_semantic_consistency(contract, expected_value):
    """
    Compare a generated contract with an independently
    annotated expected Boolean interpretation.

    Returns a detailed validation result.

    This function is intended for benchmark evaluation,
    not as a production-time semantic oracle.
    """

    from contract_validator import validate_contract

    if type(expected_value) is not bool:
        return {
            "valid": False,
            "status": "INVALID_EXPECTED_VALUE",
            "expected_value": expected_value,
            "actual_value": None
        }

    if not validate_contract(contract):
        return {
            "valid": False,
            "status": "INVALID_CONTRACT_STRUCTURE",
            "expected_value": expected_value,
            "actual_value": None
        }

    actual_value = contract["condition"]["value"]

    if actual_value is not expected_value:
        return {
            "valid": False,
            "status": "SEMANTIC_MISMATCH",
            "expected_value": expected_value,
            "actual_value": actual_value
        }

    return {
        "valid": True,
        "status": "SEMANTIC_MATCH",
        "expected_value": expected_value,
        "actual_value": actual_value
    }
