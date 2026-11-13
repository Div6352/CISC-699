
# CISC 699 - Capstone II A2
# Improved Decision Explanation Tests

from contract_router import route_with_explanation
from execution_trace import create_execution_trace


def make_contract(target, expected_value):
    return {
        "source": "Check Tests",
        "target": target,
        "condition": {
            "field": "tests_passed",
            "operator": "equals",
            "value": expected_value
        }
    }


test_cases = [
    {
        "name": "ROUTED",
        "contracts": [
            make_contract("Deploy Code", True),
            make_contract("Fix Code", False)
        ],
        "workflow_data": {"tests_passed": True},
        "expected_status": "ROUTED",
        "expected_target": "Deploy Code",
        "expected_matches": 1,
        "expected_phrase": "Exactly one contract matched"
    },
    {
        "name": "NO_MATCH",
        "contracts": [
            make_contract("Deploy Code", True)
        ],
        "workflow_data": {"tests_passed": False},
        "expected_status": "NO_MATCH",
        "expected_target": None,
        "expected_matches": 0,
        "expected_phrase": "No contracts matched"
    },
    {
        "name": "AMBIGUOUS",
        "contracts": [
            make_contract("Deploy Code", True),
            make_contract("Review Code", True)
        ],
        "workflow_data": {"tests_passed": True},
        "expected_status": "AMBIGUOUS",
        "expected_target": None,
        "expected_matches": 2,
        "expected_phrase": "Multiple contracts matched"
    },
    {
        "name": "INVALID_CONTRACT",
        "contracts": [
            {
                "source": "Check Tests",
                "target": "Deploy Code",
                "condition": {
                    "field": "unknown_field",
                    "operator": "equals",
                    "value": True
                }
            }
        ],
        "workflow_data": {"tests_passed": True},
        "expected_status": "INVALID_CONTRACT",
        "expected_target": None,
        "expected_matches": 0,
        "expected_phrase": "Contract validation failed"
    },
    {
        "name": "INVALID_WORKFLOW_DATA",
        "contracts": [
            make_contract("Deploy Code", True),
            make_contract("Fix Code", False)
        ],
        "workflow_data": {},
        "expected_status": "INVALID_WORKFLOW_DATA",
        "expected_target": None,
        "expected_matches": 0,
        "expected_phrase": "tests_passed"
    }
]


print("\nA2 Research - Improved Decision Explanation Tests")

passed_tests = 0

for case in test_cases:

    result = route_with_explanation(
        case["contracts"],
        "Check Tests",
        case["workflow_data"]
    )

    trace = create_execution_trace(
        "Check Tests",
        case["workflow_data"],
        case["contracts"],
        result
    )

    assert trace["routing_status"] == case["expected_status"], (
        f"{case['name']}: Unexpected routing status "
        f"{trace['routing_status']}"
    )

    assert trace["selected_next_node"] == case["expected_target"], (
        f"{case['name']}: Unexpected destination"
    )

    assert len(trace["matched_contracts"]) == case["expected_matches"], (
        f"{case['name']}: Unexpected number of matched contracts"
    )

    explanation = trace["decision_explanation"]

    assert isinstance(explanation, str)
    assert case["expected_phrase"] in explanation, (
        f"{case['name']}: Missing expected explanation"
    )

    print(f"{case['name']}: PASS")
    print("Explanation:", explanation)

    passed_tests += 1


print("\nTotal scenarios:", len(test_cases))
print("Passed scenarios:", passed_tests)

assert passed_tests == len(test_cases)

print("\nAll improved decision explanation tests passed!")
