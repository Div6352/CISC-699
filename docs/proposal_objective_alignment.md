# CISC 699 Capstone II — Proposal-to-Implementation Objective Alignment

**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution

**Purpose:** Assess how the Capstone II implementation and experimental evidence address the five research objectives defined in Section 1.9 of the original Capstone I proposal.

**Original proposal:** *Designing Structured Natural-Language Edge Semantics for Deterministic Agent Execution in Graph-Based Autonomous Software Development Workflows*, Section 1.9, page 4.

## 1. Research Question

The original research question asks:

"How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?"

The Capstone II prototype investigates this question by separating LLM-based natural-language interpretation from deterministic evaluation of structured semantic contracts.

The evaluation examines interpretation accuracy, routing correctness, repeated decisions, workflow-path repeatability, validation behavior, execution tracing, and execution overhead.

The findings are limited to the implemented prototype and controlled experiments.

## 2. Objective 1 — Examine Natural-Language Edge Interpretation

**Original objective:**

"To examine how natural-language edge conditions are interpreted within graph-based autonomous software-development workflows."

### Implementation and Evidence

The project implemented an initial exact-match rule-based interpreter and a later Ollama-based structured interpreter using the `llama3.2:3b` model.

The research examined predefined conditions, independent paraphrases, repeated interpretation attempts, and incorrect semantic interpretations.

Evidence includes:

- `docs/NL_Interpretation_Baseline_Results.md`
- `docs/matched_routing_research_findings.md`
- `docs/independent_interpretation_consistency_results.json`
- `docs/repeated_matched_independent_nl_results.json`
- `src/ollama_structured_interpreter.py`

### Findings

The initial four-case rule-based baseline achieved 50% interpretation accuracy, with a 50% abstention rate.

The independent LLM interpretation repeatability experiment achieved 25 correct interpretations across 30 attempts.

The repeated matched independent evaluation produced 24 correct target-paraphrase interpretations across 30 attempts.

Failure-related paraphrases, particularly IND06 and IND10, exposed semantic interpretation errors.

### Assessment

**Substantially addressed within the tested scope.**

The research investigated natural-language interpretation behavior and identified both successful interpretations and failure cases.

**Limitation:** The experiments used a small set of Boolean workflow conditions and do not establish generalization to complex natural-language instructions.

## 3. Objective 2 — Develop a Structured Semantic Representation

**Original objective:**

"To develop a structured semantic representation of edge conditions, including state variables, operators, expected values, and destination routes."

### Implementation and Evidence

The prototype represents workflow transitions using structured semantic contracts.

The implemented contract representation includes a source node, target node, and a condition specifying the field, operator, and expected Boolean value.

The implementation supports structural validation and deterministic evaluation of the supported condition schema.

Evidence includes:

- `src/semantic_contract.py`
- `src/contract_validator.py`
- `src/contract_evaluator.py`
- `docs/Contract_Evaluation_Research_Record.md`
- `docs/Semantic_Evaluation_Standard.md`

### Findings

The contract evaluator produced the expected Boolean results for the two tested workflow states.

A repeatability experiment evaluated one unchanged contract and input ten times, producing ten identical results.

Structural validation experiments also identified limitations in graph membership checking, edge identifier uniqueness, and acceptance of additional fields.

### Assessment

**Addressed for the implemented Boolean contract schema.**

A structured representation was developed and evaluated.

**Limitation:** The schema supports a narrow condition type. Structural validity does not establish semantic correctness, and the individual validator does not enforce every graph-level constraint.

## 4. Objective 3 — Implement a Controlled Prototype

**Original objective:**

"To implement a controlled prototype that separates natural-language interpretation from deterministic workflow-transition evaluation."

### Implementation and Evidence

The prototype separates natural-language interpretation, semantic contract construction, contract validation, condition evaluation, routing, graph-transition checking, and execution tracing.

Key implementation files include:

- `src/ollama_structured_interpreter.py`
- `src/semantic_contract.py`
- `src/contract_validator.py`
- `src/contract_evaluator.py`
- `src/contract_router.py`
- `src/graph.py`
- `src/traced_contract_router.py`
- `src/execution_trace.py`
- `src/test_ollama_workflow_integration.py`

The controlled workflow uses a test-result decision at `Check Tests` with two possible destinations:

- `Deploy Code` when `tests_passed` is `True`.
- `Fix Code` when `tests_passed` is `False`.

The traced routing wrapper checks whether a selected transition is permitted by the graph and saves a JSON execution trace.

### Findings

The implementation demonstrates separation between probabilistic interpretation and deterministic condition evaluation.

Integration testing has exercised LLM-generated conditions, contract validation, routing, graph-transition enforcement, and trace saving.

### Assessment

**Substantially addressed within the prototype scope.**

The principal architectural components have been implemented and integrated for the tested workflow.

**Limitation:** The prototype is not a production-scale autonomous software-development system. The individual contract validator does not independently enforce all graph constraints, and the integration test does not establish unrestricted multi-node workflow execution.

## 5. Objective 4 — Compare Against Direct Natural-Language Routing

**Original objective:**

"To evaluate the proposed approach against direct natural-language routing using repeated executions of predefined scenarios."

### Implementation and Evidence

The project implemented a direct LLM routing baseline and a structured semantic-contract routing approach.

Both methods were evaluated using predefined workflow states and expected destinations.

The later repeated matched independent experiment used ten independent paraphrase cases, each repeated three times, producing 30 decisions per method.

Evidence includes:

- `src/direct_nl_llm_router.py`
- `src/test_repeated_matched_independent_nl.py`
- `docs/matched_independent_nl_results.json`
- `docs/repeated_matched_independent_nl_results.json`
- `docs/matched_routing_research_findings.md`

### Findings

| Metric | Direct LLM Routing | Structured Contract Routing |
|---|---:|---:|
| Total decisions | 30 | 30 |
| Correct decisions | 15 | 24 |
| Expected-route accuracy | 50% | 80% |
| Cases with identical repeated decisions | 10/10 | 10/10 |
| Total measured time | 89.5295 seconds | 253.5074 seconds |

The structured approach achieved 30 percentage points higher expected-route accuracy in this experiment.

However, both methods produced consistent repeated decisions, including consistently incorrect decisions.

The structured method required more total execution time because it regenerated both semantic contracts during every repetition.

### Assessment

**Addressed through controlled repeated comparisons.**

The experiments provide comparative evidence for the tested scenarios.

**Limitation:** The structured interpreter received additional Boolean interpretation guidance that was not provided to the direct LLM baseline. Therefore, the observed accuracy difference cannot be attributed exclusively to the architecture.

## 6. Objective 5 — Assess Reliability and Evaluation Metrics

**Original objective:**

"To assess decision consistency, workflow-path repeatability, expected-route accuracy, trace completeness, validation behavior, and execution overhead."

### Implementation and Evidence

The project evaluated the specified dimensions through component tests, repeated routing experiments, trace generation, validation tests, and comparative timing measurements.

Evidence includes:

- `docs/research_completion_checklist.txt`
- `docs/Contract_Routing_Safety_Record.md`
- `docs/Graph_Evaluator_Test_Record.md`
- `docs/matched_routing_research_findings.md`
- `docs/repeated_matched_independent_nl_results.json`
- `src/traced_contract_router.py`
- `src/execution_trace.py`

### Findings

**Decision consistency:** Both methods produced identical repeated decisions for all ten cases in the repeated independent comparison. This did not imply that the decisions were correct.

**Workflow-path repeatability:** A separate experiment reported 20/20 repeated paths. The tested path included a fixed initial transition that was not selected by semantic contract evaluation.

**Expected-route accuracy:** The repeated independent comparison reported 15/30 correct direct LLM decisions and 24/30 correct structured routing decisions.

**Trace completeness:** Trace completeness and persistence were tested in separate experiments. Repeated automatic tracing reported 20/20 successful runs with unique trace identifiers and files.

**Validation behavior:** Tests covered invalid contracts, unsupported conditions, no-match routing, ambiguous routing, invalid workflow data, and graph-transition checks.

**Execution overhead:** The repeated independent comparison measured 89.5295 seconds for direct routing and 253.5074 seconds for structured routing, including fresh contract interpretation during each repetition.

### Assessment

**Substantially addressed through separate evaluation experiments.**

The project measured the dimensions identified in the original proposal.

**Limitation:** The metrics were not all evaluated in one unified end-to-end benchmark. Full workflow-path repeatability and trace persistence were not evaluated as part of the 30-decision independent comparison.

## 7. Overall Proposal Alignment Summary

| Objective | Assessment |
|---|---|
| 1. Examine natural-language interpretation | Substantially addressed |
| 2. Develop structured semantic representation | Addressed within limited schema |
| 3. Implement controlled prototype | Substantially addressed |
| 4. Compare direct and structured routing | Addressed within controlled benchmark |
| 5. Assess consistency, accuracy, traces, validation, and overhead | Substantially addressed across separate experiments |

All five original research objectives have corresponding implementation or evaluation evidence.

However, these assessments do not establish that every proposed feature has been implemented completely or that every research limitation has been resolved.

## 8. Remaining Gaps and Qualifications

The following limitations must be explicitly discussed in the final Capstone II report:

1. The workflow graph is small and uses a Boolean test-result condition.
2. Natural-language interpretation can produce semantically incorrect but structurally valid contracts.
3. The individual contract validator does not enforce all graph-level constraints.
4. Some routing checks occur in the traced routing wrapper rather than the contract validator.
5. The structured and direct LLM prompts are not equivalent.
6. The independent dataset contains only ten paraphrases.
7. Repeated decision consistency does not imply correctness.
8. Contract generation introduces measurable execution overhead.
9. The repeated comparison does not evaluate full workflow paths or trace persistence.
10. Oracle-based semantic checks use benchmark reference labels and are not production-time semantic verification.
11. The prototype does not establish enterprise-scale reliability, general cybersecurity safety, or universal deterministic behavior.

## 9. Research Completion Assessment

The Capstone II work provides substantial evidence addressing the five research objectives established in the Capstone I proposal.

The principal research contribution is a controlled prototype and evaluation of a structured semantic-contract approach that separates natural-language interpretation from deterministic workflow-transition evaluation.

The results indicate improved expected-route accuracy for structured routing in the tested comparisons, while also revealing semantic interpretation failures, prompt-design limitations, and additional execution overhead.

The remaining work is to consolidate the experimental results, complete the final research report, verify references and university submission requirements, and perform final project verification.

**Current phase:** Final research review and report preparation.

**Final academic completion status:** Pending report preparation, submission-requirement verification, and final review.