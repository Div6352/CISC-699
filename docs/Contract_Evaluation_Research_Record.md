
# Deterministic Contract Evaluation Research Record

Course: CISC 699 - Capstone II

Project: A2 - Natural-Language Edge Semantics
and Deterministic Agent Execution

## 1. Objective

Evaluate the basic functionality and repeatability
of manually defined structured semantic contracts.

## 2. Implementation

Files:
- src/semantic_contract.py
- src/contract_validator.py
- src/contract_evaluator.py
- src/test_contract_validator.py
- src/test_contract_evaluator.py

Two semantic contracts were manually defined:

E01: tests_passed equals True
Target: Deploy Code

E02: tests_passed equals False
Target: Fix Code

## 3. Evaluation Results

Scenario 1:
Input: tests_passed = True
E01 result: True
E02 result: False
Status: PASS

Scenario 2:
Input: tests_passed = False
E01 result: False
E02 result: True
Status: PASS

## 4. Repeatability Test

Contract: E01
Input: tests_passed = True
Number of evaluations: 10

Observed results:
10 True results

Within-run agreement: 10/10 (100%)

Status: PASS

## 5. Evidence

evidence/WP04_Contract_Repeatability.png

## 6. Interpretation

The evaluator produced the expected Boolean
results for the two tested workflow states.

Repeated evaluation of E01 with an unchanged
input produced identical results across 10 runs.

## 7. Limitations

- Contracts were created manually.
- No LLM interpretation was performed.
- Natural-language semantic correctness
  was not independently evaluated.
- Repeatability was tested with one contract
  and one input in a single program execution.
- No direct LLM baseline comparison was performed.
- The validator supports only a limited schema.

## 8. Final Report Relevance

Chapter 3: Solution Design and Implementation

Chapter 4: Evaluation Methodology

Chapter 5: Results and Analysis

These results are preliminary prototype tests,
not the final experimental findings.

## 9. Next Research Activity

Connect validated semantic contracts to
deterministic workflow routing.
