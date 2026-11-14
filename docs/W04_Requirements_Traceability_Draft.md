# Week 4 - Requirements Traceability Matrix

**Project:** A2 - Natural-Language Edge Semantics and Deterministic Agent Execution
**Status:** Draft - source and historical evidence review
**Source:** docs/proposal_objective_alignment.md, Capstone I proposal Section 1.9

| ID | Research requirement | Implementation | Test or evidence | Status |
|---|---|---|---|---|
| O1 | Examine natural-language interpretation | src/nl_interpreter.py; src/ollama_structured_interpreter.py | src/test_nl_interpreter.py; docs/NL_Interpretation_Baseline_Results.md; docs/repeated_matched_independent_nl_results.json | Evidence identified; limited Boolean conditions |
| O2 | Develop structured semantic representation | src/semantic_contract.py; src/contract_validator.py; src/contract_evaluator.py | src/test_contract_validator.py; src/test_contract_evaluator.py; docs/Contract_Evaluation_Research_Record.md | Implemented for supported Boolean schema |
| O3 | Implement controlled prototype separating interpretation and execution | src/nl_contract_builder.py; src/contract_router.py; src/graph.py; src/traced_contract_router.py; src/execution_trace.py | src/test_ollama_workflow_integration.py; src/test_permitted_graph_transitions.py; docs/Graph_Evaluator_Test_Record.md | Components identified; complete integration review pending |
| O4 | Compare structured and direct natural-language routing | src/direct_nl_llm_router.py; src/ollama_structured_interpreter.py | src/test_repeated_matched_independent_nl.py; docs/repeated_matched_independent_nl_results.json; docs/W03_Controlled_Comparison_Protocol_Draft.md | Preliminary evidence; formal Week 9 evaluation pending |
| O5 | Assess consistency, repeatability, accuracy, tracing, validation and overhead | src/contract_router.py; src/traced_contract_router.py; src/execution_trace.py | src/test_workflow_path_repeatability.py; src/test_trace_completeness.py; src/test_end_to_end_timing.py; docs/matched_routing_research_findings.md | Evidence identified across separate experiments |

## Design and Evaluation Qualifications

- The contract schema currently supports tests_passed, equals, and Boolean values.
- Structurally valid contracts may still contain incorrect semantic interpretations.
- Graph permission enforcement occurs in the traced router, not in the individual contract validator.
- The rule-based contract builder does not directly invoke the Ollama interpreters.
- Existing direct and structured LLM comparisons have prompt-equivalence limitations.
- Repeated routing consistency does not guarantee correct routing.
- Previously recorded experiments are historical evidence, not newly completed Week 4 tests.
- Formal controlled evaluation remains scheduled for Week 9.

## Verification Status

The five objectives were checked against docs/proposal_objective_alignment.md. Implementation paths were identified from the repository and selected source files inspected during Week 4. Individual test-to-requirement mappings remain provisional until the relevant test bodies and evidence are reviewed.

## Week 4 Test Review
O2: Validator and evaluator tests inspected.
O3: Integration and graph-transition tests inspected; graph test uses a separate example graph.
O4: Comparison methodology inspected; prompt and model-call differences remain limitations.
O5: Repeatability, trace completeness, and timing tests inspected.
All reviews were source-code inspections only; no new Week 4 tests were executed.
