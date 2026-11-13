
# CISC 699 - A2 Research Project
# Initial Reference Semantic Contracts

reference_contracts = {
    "NL01": {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    "NL02": {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }
    },
    "NL03": {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    "NL04": {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }
    }
}

# Additional provisional reference contracts

reference_contracts.update({
    "NL05": {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    "NL06": {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    "NL07": {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": True
        }
    },
    "NL08": {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }
    },
    "NL09": {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": False
        }
    }
})

print("A2 Research - Reference Semantic Contracts")

for case_id, contract in reference_contracts.items():
    print(case_id, ":", contract)
