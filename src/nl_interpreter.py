
# CISC 699 - A2 Research Project
# Initial Rule-Based Natural-Language Interpreter

def interpret_condition(text):

    normalized = text.strip().lower()

    if normalized == (
        "if all software tests have passed, "
        "proceed to deployment."
    ):
        return {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }

    if normalized == (
        "if any software test has failed, "
        "return to fixing the code."
    ):
        return {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }

    # Unknown language: do not guess
    return None
