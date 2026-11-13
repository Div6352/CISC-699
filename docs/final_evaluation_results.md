# CISC 699 Capstone II — Final Evaluation Results

**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution

**Research artifact:** Structured Natural-Language Edge Semantics Framework

**Purpose:** Consolidate the recorded implementation tests and experimental findings for the final Capstone II research report.

**Experimental model:** Ollama `llama3.2:3b`, temperature 0, for the LLM-based experiments described below.

## 1. Evaluation Overview

The research evaluates whether separating natural-language interpretation from deterministic semantic-contract execution can improve routing correctness, consistency, and traceability in a controlled graph-based software-development workflow.

The prototype uses a small workflow with a test-result decision:

- Current decision node: `Check Tests`
- Successful-test destination: `Deploy Code`
- Failed-test destination: `Fix Code`
- Workflow state variable: `tests_passed`
- Supported condition operator: `equals`

The evaluation comprises several distinct experiments. Results must be reported using the denominator and conditions of each experiment.

The experiments do not form one pooled dataset, and their percentages must not be combined into a single overall accuracy figure.

## 2. Summary of Recorded Experimental Results

| Evaluation | Recorded result | Interpretation |
|---|---|---|
| Initial rule-based natural-language baseline | 2/4 correct; 50% accuracy | Exact-match rules did not recognize two unseen paraphrases |
| Manually defined contract evaluation | Both Boolean workflow states passed | Basic condition evaluation behaved as expected |
| Contract evaluation repeatability | 10/10 identical results | One unchanged contract and input produced consistent results |
| Early graph evaluator | 4/4 tests passed | Expected routing and unsupported-condition rejection |
| Early contract routing safety | 4/4 tests passed | Expected routing, no-match, and ambiguity handling |
| Original matched routing comparison | Direct 5/10; structured 10/10 | Structured routing performed better on two repeated workflow states |
| Matched natural-language comparison | Direct 5/10; structured 10/10 | Contracts were generated once and reused |
| Independent natural-language comparison | Direct 5/10; structured 8/10 | Ten independent paraphrase cases |
| Independent interpretation repeatability | 25/30 correct | Interpretation accuracy and stability were evaluated separately |
| Oracle-based semantic consistency evaluation | 8/10 matches | Two semantically incorrect conditions passed structural validation |
| Repeated matched independent comparison | Direct 15/30; structured 24/30 | Ten cases, three repetitions each |
| Separate workflow-path repeatability experiment | 20/20 repeated paths | Includes a fixed initial workflow transition |
| Separate automatic trace repetition experiment | 20/20 successful runs | Unique trace identifiers and files reported |

These findings come from separate component records, experimental result files, and the research completion checklist.

## 3. Initial Rule-Based Interpretation Baseline

The initial interpreter used exact-match Python rules rather than an LLM.

Four natural-language conditions were evaluated, including two predefined expressions and two paraphrases.

| Metric | Result |
|---|---:|
| Total conditions | 4 |
| Correct interpretations | 2 |
| Incorrect or unsuccessful interpretations | 2 |
| Interpretation accuracy | 50% |
| Abstentions | 2 |
| Abstention rate | 50% |

Both predefined expressions were recognized correctly.

Both unseen paraphrases produced `None`.

This result establishes a preliminary limitation of the implemented exact-match baseline. It does not establish the performance of all rule-based natural-language systems.

**Source:** `docs/NL_Interpretation_Baseline_Results.md`

## 4. Deterministic Contract and Graph Component Tests

### 4.1 Contract Evaluation

Two manually defined conditions were evaluated:

- E01: `tests_passed equals True`, associated with `Deploy Code`.
- E02: `tests_passed equals False`, associated with `Fix Code`.

For `tests_passed = True`, E01 evaluated to `True` and E02 evaluated to `False`.

For `tests_passed = False`, E01 evaluated to `False` and E02 evaluated to `True`.

A separate repeatability test evaluated E01 ten times with the same input and observed ten identical `True` results.

These tests demonstrate basic deterministic condition evaluation for the supported Boolean schema.

**Source:** `docs/Contract_Evaluation_Research_Record.md`

### 4.2 Early Graph Evaluation

Four recorded tests passed:

1. Successful tests selected `Deploy Code`.
2. Failed tests selected `Fix Code`.
3. Three repeated failed-test evaluations selected `Fix Code` each time.
4. An unsupported condition produced the expected error behavior.

These tests demonstrate basic workflow evaluation and unsupported-condition rejection.

**Source:** `docs/Graph_Evaluator_Test_Record.md`

### 4.3 Early Contract Routing Safety

Four recorded tests passed:

1. Successful tests selected `Deploy Code`.
2. Failed tests selected `Fix Code`.
3. No matching contract produced no destination.
4. Two matching contracts produced no destination rather than an arbitrary selection.

The later routing implementation provides diagnostic statuses and explanations, including `ROUTED`, `NO_MATCH`, `AMBIGUOUS`, `INVALID_CONTRACT`, and `INVALID_WORKFLOW_DATA`.

These behaviors represent controlled handling of the tested cases, not proof of comprehensive system safety.

**Source:** `docs/Contract_Routing_Safety_Record.md`

**Implementation:** `src/contract_router.py`

## 5. Original Matched Routing Comparison

The initial matched routing experiment evaluated two workflow states, each repeated five times.

| Metric | Direct LLM | Structured Contract Routing |
|---|---:|---:|
| Total decisions | 10 | 10 |
| Correct decisions | 5 | 10 |
| Expected-route accuracy | 50% | 100% |
| Within-scenario decision consistency | 100% | 100% |
| Average measured routing time | 2.507547 s | 0.00001943 s |

The structured method also required approximately 13.334945 seconds to construct the two semantic contracts before routing.

The direct LLM returned `NO_MATCH` in all five failed-test evaluations rather than selecting `Fix Code`.

The structured router selected `Fix Code` in all five failed-test evaluations.

**Important timing qualification:** The extremely small structured routing time measures deterministic routing after contract construction. It is not an end-to-end comparison with LLM interpretation included.

**Source:** `docs/matched_routing_comparison_results.json`

## 6. Matched Natural-Language Comparison

A later experiment compared direct natural-language routing with structured contract routing using the same original natural-language edge descriptions.

| Metric | Direct LLM | Structured Contracts |
|---|---:|---:|
| Total decisions | 10 | 10 |
| Correct decisions | 5 | 10 |
| Expected-route accuracy | 50% | 100% |
| Total measured time | 22.4867 s | 9.0886 s |

The structured approach generated contracts once and reused them.

Its reported total included approximately 9.0884 seconds of initial contract construction.

This experiment suggests that contract reuse may reduce repeated model inference overhead for the tested states.

However, the experiment included only two distinct workflow states, and the structured interpreter received additional Boolean interpretation guidance.

**Source:** `docs/fair_nl_comparison_results.json`

## 7. Independent Natural-Language Comparison

A broader matched comparison evaluated ten independent natural-language paraphrase cases.

Each case was evaluated once.

| Metric | Direct LLM | Structured Contracts |
|---|---:|---:|
| Total decisions | 10 | 10 |
| Correct decisions | 5 | 8 |
| Expected-route accuracy | 50% | 80% |
| Total measured time | 36.7451 s | 80.9153 s |

The direct LLM selected `Deploy Code` for all ten cases, including the five failed-test cases.

The structured approach produced the expected destination in eight cases.

The structured approach was slower overall because it generated two contracts for each independent case.

This experiment supports an observed accuracy difference in the tested benchmark but does not demonstrate an end-to-end speed advantage.

**Source:** `docs/matched_independent_nl_results.json`

## 8. Independent Interpretation Repeatability

The structured Ollama interpreter was evaluated on ten independent natural-language conditions, with three interpretation attempts per condition.

| Metric | Result |
|---|---:|
| Total interpretation attempts | 30 |
| Correct interpretations | 25 |
| Interpretation accuracy | 83.3% |
| Cases with identical normalized predictions | 9/10 |
| Case-level stability | 90% |

IND06 was interpreted incorrectly in all three attempts.

IND10 produced different interpretations across repetitions.

This experiment demonstrates that temperature 0 does not guarantee identical semantic interpretation across all repeated model calls.

It also demonstrates that stable interpretations can be incorrect.

**Source:** `docs/independent_interpretation_consistency_results.json`

## 9. Oracle-Based Semantic Consistency Evaluation

A separate retrospective experiment compared generated contract conditions against benchmark reference labels.

| Metric | Result |
|---|---:|
| Total cases | 10 |
| Semantic matches | 8 |
| Semantic mismatches | 2 |
| Other validation failures | 0 |
| Semantic match rate | 80% |

The two mismatches were IND06 and IND10.

Both cases described unsuccessful test conditions. The expected Boolean value was `False`, but the generated condition contained `True`.

The contracts were structurally valid despite their semantic errors.

For the evaluated failed-test states, deterministic routing produced `NO_MATCH` rather than the expected `Fix Code` transition.

**Important qualification:** This evaluation used trusted benchmark annotations. It does not demonstrate that the prototype can independently verify natural-language meaning during production execution.

**Source:** `docs/independent_semantic_consistency_results.json`

## 10. Repeated Matched Independent Natural-Language Evaluation

### 10.1 Experimental Design

The repeated matched independent experiment used ten paraphrase cases, IND01 through IND10.

Each case was evaluated three times, producing 30 routing decisions per method.

Both approaches used the `llama3.2:3b` model at temperature 0.

The direct method made a natural-language routing decision for each repetition.

The structured method generated fresh semantic conditions for both available edges during each repetition, followed by contract validation and deterministic routing.

### 10.2 Main Results

| Metric | Direct LLM Routing | Structured Contract Routing |
|---|---:|---:|
| Independent cases | 10 | 10 |
| Repetitions per case | 3 | 3 |
| Total decisions | 30 | 30 |
| Correct decisions | 15 | 24 |
| Expected-route accuracy | 50.0% | 80.0% |
| Cases with identical repeated decisions | 10/10 | 10/10 |
| Total measured time | 89.5295 s | 253.5074 s |

The structured method achieved a 30-percentage-point higher expected-route accuracy.

Both approaches produced stable decisions across the three repetitions of every case.

However, some of these stable decisions were incorrect.

### 10.3 Error Analysis

The direct LLM consistently selected `Deploy Code`, including in failed-test scenarios where `Fix Code` was expected.

The structured interpreter misinterpreted IND06 and IND10 by generating a `True` condition when the intended value was `False`.

Those errors caused the deterministic router to return `NO_MATCH` rather than selecting the expected repair destination.

Across the repeated experiment, 24 of 30 target-paraphrase condition interpretations were correct.

### 10.4 Execution Overhead

The direct method required approximately 89.53 seconds.

The structured method required approximately 253.51 seconds.

The structured method therefore took approximately 2.83 times as long in this experiment.

This measurement includes fresh interpretation of both natural-language edges for every repetition.

It should not be confused with experiments in which semantic contracts were constructed once and reused.

### 10.5 Interpretation

The repeated comparison provides evidence that structured semantic-contract routing achieved higher expected-route accuracy in the tested benchmark.

However, the structured interpreter received explicit Boolean interpretation guidance that was not provided to the direct routing baseline.

The methods also made different numbers of model calls.

Therefore, the accuracy difference cannot be attributed exclusively to the semantic-contract architecture.

**Source:** `docs/repeated_matched_independent_nl_results.json`

**Experiment script:** `src/test_repeated_matched_independent_nl.py`

## 11. Workflow-Path Repeatability and Execution Tracing

Separate deterministic execution experiments reported:

| Evaluation | Recorded result |
|---|---:|
| Repeated workflow paths | 20/20 |
| Repeated automatic trace runs | 20/20 |
| Unique trace identifiers and files | 20/20 |

The tested workflow-path sequence included a fixed initial transition from `Start` to `Check Tests`. That initial transition was not selected through semantic contract evaluation.

The traced routing wrapper supports automatic trace creation and persistence for evaluated routing decisions.

The trace records include the current node, workflow data, evaluated contracts, validation results, routing status, selected destination, explanation, and trace identifier.

The repeated independent LLM comparison did not evaluate full workflow-path repeatability or trace persistence.

**Sources:**
- `docs/research_completion_checklist.txt`
- `src/traced_contract_router.py`
- `src/execution_trace.py`

## 12. Validation and Failure-Handling Findings

The project recorded experiments involving:

- Invalid contract rejection.
- Extended contract validation.
- Additional contract fields.
- Graph node membership.
- Permitted graph transitions.
- Duplicate and optional edge identifiers.
- Missing or invalid workflow data.
- No-match routing.
- Ambiguous routing.
- Trace generation and persistence failures.
- JSON serialization and safer trace saving.

The implementation distinguishes structural contract validation from graph-transition enforcement.

Individual contract validation does not enforce every graph-level constraint.

The traced routing wrapper provides a separate graph-transition check for selected destinations.

The JSON-saving implementation uses a temporary file and replacement operation. The tests support the observed safer-saving behavior but do not establish universal filesystem durability.

**Source:** `docs/research_completion_checklist.txt`

## 13. Consolidated Findings

The combined experimental evidence supports the following conclusions within the tested prototype:

1. Deterministic contract evaluation produced consistent results for unchanged supported inputs.

2. Structured routing achieved higher expected-route accuracy than direct LLM routing in the recorded matched comparisons.

3. Repeated decision consistency did not guarantee routing correctness.

4. Structurally valid semantic contracts could still misrepresent their original natural-language conditions.

5. Deterministic routing could avoid arbitrary destination selection in tested no-match and ambiguous cases, but it could not correct incorrect semantic interpretation.

6. Contract construction introduced measurable overhead, particularly when contracts were regenerated for every decision.

7. Contract reuse and fresh interpretation produced different timing outcomes and must be analyzed separately.

8. Execution tracing and diagnostic routing improved observability within the implemented prototype.

9. The results provide preliminary evidence for the usefulness of separating semantic interpretation from deterministic execution, rather than proof of general reliability or safety.

## 14. Research Limitations

The final report must acknowledge that:

- The workflow graph is small and uses Boolean conditions.
- The independent benchmark contains ten paraphrase cases.
- Some natural-language conditions may be ambiguous without predefined workflow context.
- The structured and direct LLM prompts are not equivalent.
- Temperature 0 does not guarantee semantic correctness or identical interpretations.
- The individual validator does not enforce all graph-level constraints.
- Semantic consistency checking relies on benchmark reference labels.
- Not every metric was measured in one unified experiment.
- The repeated comparison evaluates routing decisions rather than complete workflow paths.
- The prototype does not establish generalization to production-scale autonomous software-development workflows.
- No comprehensive cybersecurity security assessment was performed.

## 15. Overall Evaluation Conclusion

The Capstone II research provides preliminary evidence that structured semantic-contract routing can improve expected-route accuracy in a controlled graph-based software-development workflow.

The repeated matched independent experiment achieved 80% expected-route accuracy for structured routing compared with 50% for direct LLM routing, while requiring greater total execution time when contracts were regenerated for each decision.

The findings also demonstrate that deterministic execution depends on the correctness of the generated semantic contracts.

The research contribution is therefore not a claim that LLM interpretation becomes deterministic or error-free. Rather, it is a controlled prototype and evaluation methodology that separates natural-language interpretation from explicit contract validation, deterministic transition evaluation, and execution trace recording.

**Research status:** Experimental results consolidated; final report drafting, source verification, and submission checks remain outstanding.