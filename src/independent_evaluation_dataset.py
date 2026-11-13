
# CISC 699 - A2 Research Project
# Independent Natural-Language Evaluation Dataset

independent_evaluation_cases = [
    {
        "case_id": "IND01",
        "text": "Deployment is permitted when the entire test suite succeeds.",
        "expected_value": True
    },
    {
        "case_id": "IND02",
        "text": "If a single test reports failure, send the code back for repairs.",
        "expected_value": False
    },
    {
        "case_id": "IND03",
        "text": "Release the application only if no tests are failing.",
        "expected_value": True
    },
    {
        "case_id": "IND04",
        "text": "Any unsuccessful test should prevent deployment.",
        "expected_value": False
    },
    {
        "case_id": "IND05",
        "text": "When the complete test suite passes, move to the release stage.",
        "expected_value": True
    },
    {
        "case_id": "IND06",
        "text": "If the test results contain even one failure, return to development.",
        "expected_value": False
    },
    {
        "case_id": "IND07",
        "text": "Proceed with deployment provided that every test is successful.",
        "expected_value": True
    },
    {
        "case_id": "IND08",
        "text": "Do not release the software when any test has failed.",
        "expected_value": False
    },
    {
        "case_id": "IND09",
        "text": "The application may be deployed after all checks pass.",
        "expected_value": True
    },
    {
        "case_id": "IND10",
        "text": "If the test suite is not fully successful, return the code for fixes.",
        "expected_value": False
    }
]
