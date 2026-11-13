# Week 3 — Research Progress Record

**Course:** CISC 699 — Capstone II  
**Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution  
**Week:** W03 — November 9–15, 2026  
**Work Packages:** WP01, WP02, WP05  
**Status:** In progress

## 1. Objective

Verify the development environment and available research tools, and prepare the controlled evaluation protocol for comparing direct-LLM routing with structured semantic-contract routing.

## 2. Activities and Verification

The Python development environment was verified in Visual Studio Code. The project uses a Python virtual environment, and a basic Python script executed successfully.

Existing research code includes semantic-contract definition, validation, evaluation, workflow routing, and test scripts. A previously executed contract-evaluation test produced 10 identical Boolean results for an unchanged input.

The research package also contains saved JSON results from direct-LLM and structured-contract experiments, along with workflow execution traces. These artifacts are available for protocol review; their presence does not establish that the formal Week 9 evaluation has been completed.

## 3. Retained Evidence

- `evidence/WP01_Python_Environment.png`
- `evidence/WP04_Contract_Repeatability.png`
- `docs/prompt_controlled_comparison_results.json`
- `docs/contract_reuse_experiment_results.json`
- `docs/workflow_path_trace_experiment_results.json`

## 4. Observations and Decisions

The available evidence supports basic Python execution and repeatable evaluation of one manually defined semantic contract. The comparison protocol must clearly define common scenarios, expected routes, repetitions, model settings, and recorded outputs before formal evaluation.

## 5. Limitations and Pending Verification

The current record does not independently confirm the installed model version, complete dependency manifest, version-control status, or approval of the final correctness oracle and repetition rules.

## 6. AI Assistance

ChatGPT assisted with development guidance, evidence organization, and drafting this research record. The researcher verified the displayed Python outputs and recovered screenshots. Any additional technical claims require checking against the original artifacts.

## 7. Next Research Activity

Complete the environment and access manifest, document the draft comparison protocol, and prepare the Week 4 architecture and requirements traceability work.

## 8. Final Report Contribution

Chapter 3 — Solution Design and Implementation  
Chapter 4 — Evaluation Methodology
## Execution Trace Verification � November 13, 2026
The execution trace test reported success and saved docs/execution_trace_example.json. Independent PowerShell checks confirmed routing_status = INVALID_WORKFLOW_DATA, selected_next_node = null, and empty workflow_data = {}. All three checks passed. This verifies the missing-workflow-data scenario, not the entire test suite.

## Graph Transition Verification - November 13, 2026
Executed src/test_permitted_graph_transitions.py. All 7 scenarios passed: three permitted transitions were accepted, while two prohibited transitions and transitions involving unknown source or target nodes were rejected. Structural validation alone did not authorize prohibited transitions. This verifies the tested graph restrictions, not all possible workflow graphs.

## Duplicate Edge Identifier Verification - November 13, 2026
Executed src/test_duplicate_edge_ids.py. All 4 scenarios passed. Unique edge identifiers were accepted, while duplicate identifiers were rejected, including a three-contract case with one duplicate. This verifies identifier uniqueness for the tested scenarios.

## Contract Node Membership Verification - November 13, 2026
Executed src/test_contract_node_membership.py. All 4 scenarios passed. Contracts referencing existing workflow nodes were accepted, while unknown source nodes, unknown target nodes, and contracts with both nodes unknown were rejected. This confirms node membership checks for the tested scenarios.

## Extended Contract Validation - November 13, 2026
Executed src/test_extended_contract_validation.py. All 12 invalid-contract scenarios were correctly rejected, covering invalid contract types, missing or empty nodes, invalid edge identifiers, missing or malformed conditions, unsupported operators, and non-Boolean condition values. Result: 12/12 passed. This verifies the tested validation cases, not exhaustive input coverage.

## Missing Workflow Data Safety Verification - November 13, 2026
Executed src/test_missing_workflow_data.py. All 8 invalid-input scenarios passed. Each produced routing_status = INVALID_WORKFLOW_DATA and selected_next_node = None. The tested cases included missing, null, string, integer, empty-string, and list values, plus invalid workflow-data types. This supports fail-safe routing for the tested scenarios.

## Invalid Contract Trace Verification - November 13, 2026
Executed src/test_invalid_contract_trace.py. The tested invalid contract produced routing_status = INVALID_CONTRACT, with validation_results recording valid = False. The script reported Failed validation recorded: PASS. This verifies invalid-contract rejection and trace content for the tested scenario; saved-file persistence was not independently checked.
