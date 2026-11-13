
# CISC 699 - A2 Research Project
# Initial Natural-Language Evaluation Dataset

evaluation_cases = [
    {
        "case_id": "NL01",
        "text": "If all software tests have passed, proceed to deployment.",
        "expected_value": True
    },
    {
        "case_id": "NL02",
        "text": "If any software test has failed, return to fixing the code.",
        "expected_value": False
    },
    {
        "case_id": "NL03",
        "text": "When every test succeeds, deploy the application.",
        "expected_value": True
    },
    {
        "case_id": "NL04",
        "text": "If at least one test fails, fix the code.",
        "expected_value": False
    }
]

print("A2 Research - Evaluation Dataset")

# Additional natural-language evaluation cases

evaluation_cases.extend([
    {
        "case_id": "NL05",
        "text": "Deploy the code only when all tests pass.",
        "expected_value": True
    },
    {
        "case_id": "NL06",
        "text": "If every test is successful, continue to deployment.",
        "expected_value": True
    },
    {
        "case_id": "NL07",
        "text": "Proceed to deployment provided no tests have failed.",
        "expected_value": True
    },
    {
        "case_id": "NL08",
        "text": "Return to development if any test fails.",
        "expected_value": False
    },
    {
        "case_id": "NL09",
        "text": "When at least one test fails, fix the software.",
        "expected_value": False
    },
    {
        "case_id": "NL10",
        "text": "Do not deploy if the test suite contains failures.",
        "expected_value": False
    }
])


for case in evaluation_cases:
    print(case["case_id"], ":", case["text"])
    print("Expected value:", case["expected_value"])
    print()
