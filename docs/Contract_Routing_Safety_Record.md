
# Contract Routing Safety Test Record

Course: CISC 699 - Capstone II

Project: A2 - Natural-Language Edge Semantics
and Deterministic Agent Execution

## 1. Objective

Verify that deterministic contract routing
selects the expected destination and avoids
routing when conditions are unmatched or ambiguous.

## 2. Implementation Files

- src/semantic_contract.py
- src/contract_validator.py
- src/contract_evaluator.py
- src/contract_router.py
- src/test_contract_router.py

## 3. Test Results

Test 1: Successful tests
Input: tests_passed = True
Expected: Deploy Code
Observed: Deploy Code
Status: PASS

Test 2: Failed tests
Input: tests_passed = False
Expected: Fix Code
Observed: Fix Code
Status: PASS

Test 3: No matching contract
Input: tests_passed = None
Expected: None
Observed: None
Status: PASS

Test 4: Ambiguous routing
Input: Two matching contracts with different targets
Expected: None
Observed: None
Status: PASS

## 4. Preliminary Findings

The router selected the expected destination
for both supported Boolean workflow states.

When no contract matched, the router returned None.

When two contracts matched, the router returned None
instead of arbitrarily selecting a destination.

## 5. Limitations

- Only a small workflow was tested.
- Contracts were manually defined.
- No LLM-generated contracts were evaluated.
- Natural-language semantic correctness was not tested.
- Returning None does not explain why routing failed.
- Invalid routing metadata may still cause errors.
- These tests do not establish overall system safety.

## 6. Final Report Relevance

Chapter 3 - Solution Design and Implementation
Chapter 4 - Evaluation Methodology
Chapter 5 - Results and Analysis

These are preliminary prototype results,
not final experimental findings.

## 7. Next Research Activity

Improve routing diagnostics so the system can
distinguish successful routing, no-match cases,
and ambiguous routing.
