# Matched Routing Comparison — Research Findings

## Experiment

**Project:** CISC 699 Capstone II A2  
**Model:** llama3.2:3b  
**Temperature:** 0  
**Scenarios:** 2  
**Repetitions per scenario:** 5  
**Total routing evaluations per approach:** 10

## Objective

Compare direct LLM routing against deterministic semantic-contract routing using identical workflow states and expected destinations.

## Results

| Metric | Direct LLM | Structured Contract Routing |
|---|---:|---:|
| Expected-route accuracy | 50% (5/10) | 100% (10/10) |
| Tests-passed scenario | 5/5 correct | 5/5 correct |
| Tests-failed scenario | 0/5 correct | 5/5 correct |
| Within-scenario decision consistency | 100% | 100% |
| Average measured routing time | 2.507547 seconds | 0.00001943 seconds |

The structured approach required approximately 13.334945 seconds to generate the two semantic contracts before routing.

## Error Analysis

For the workflow state `{"tests_passed": false}`, the direct LLM returned `NO_MATCH` in all five runs instead of the expected destination `Fix Code`.

The structured contract router returned `Fix Code` in all five runs.

This demonstrates that identical repeated decisions do not necessarily imply correct decisions.

## Interpretation

In this limited experiment, deterministic routing using validated semantic contracts achieved higher expected-route accuracy than direct LLM routing.

The findings are specific to the tested model, prompts, workflow states, and generated contracts.

## Limitations

- Only two workflow states were evaluated.
- Both scenarios were repeated five times, so the experiment contains only two distinct routing inputs.
- Semantic contracts were generated once and reused.
- The direct LLM prompt contained explicit routing rules.
- Natural-language edge interpretation was not evaluated independently for each routing run.
- The timing measurements compare different processing stages and do not establish end-to-end performance superiority.
- These results do not demonstrate generalization to larger graphs or more complex conditions.

## Next Research Actions

Expand the matched evaluation to additional scenarios, assess interpretation and routing separately, measure trace completeness, and consolidate the findings into the final research report.

**Source data:** `docs/matched_routing_comparison_results.json`
## Independent Natural-Language Interpretation Error Analysis

The independent evaluation contained 10 natural-language conditions. The structured Ollama interpreter correctly interpreted 8 conditions and incorrectly interpreted 2, producing an accuracy of 80% and an abstention rate of 0%.

### Confirmed Incorrect Cases

**IND06**

- Natural language: "If the test results contain even one failure, return to development."
- Expected condition value: `false`
- Predicted condition value: `true`
- Result: Incorrect

**IND10**

- Natural language: "If the test suite is not fully successful, return the code for fixes."
- Expected condition value: `false`
- Predicted condition value: `true`
- Result: Incorrect

### Research Interpretation

Both errors occurred in conditions describing unsuccessful tests and corrective workflow transitions. This suggests a potential weakness in the model's interpretation of some failure-related expressions.

The generated conditions were structurally valid but semantically incorrect relative to the expected values.

Consequently, structural contract validation alone is insufficient to guarantee that a semantic contract accurately captures its original natural-language meaning.

The results demonstrate the importance of separately evaluating natural-language interpretation accuracy and deterministic routing correctness.

### Limitations

The independent dataset contains only 10 cases, and these observations do not establish that all failure-related language is difficult for the model. Additional paraphrases and repeated trials are required to assess generalization.
## Consolidated A2 Research Findings

### 1. Matched Natural-Language Routing Comparison

A subsequent experiment compared direct natural-language LLM routing with structured semantic-contract routing using the same original natural-language edge descriptions.

Both approaches used the `llama3.2:3b` model with temperature 0.

Across 10 routing decisions (two workflow states repeated five times):

| Metric | Direct Natural-Language LLM | Structured Contracts |
|---|---:|---:|
| Correct decisions | 5/10 | 10/10 |
| Routing accuracy | 50% | 100% |
| Total measured time | 22.4867 seconds | 9.0886 seconds |

The structured method's total included approximately 9.0884 seconds of initial contract construction. Contracts were then reused for deterministic routing.

These results suggest that contract reuse can reduce repeated LLM inference costs. However, the experiment contained only two distinct workflow states, and the structured interpreter received additional Boolean interpretation guidance.

**Source:** `docs/fair_nl_comparison_results.json`

### 2. Matched Independent Natural-Language Evaluation

A broader experiment evaluated 10 independent paraphrases. Each case replaced one original edge description while retaining the opposite edge.

Both approaches received the same natural-language edge descriptions and workflow state.

| Metric | Direct Natural-Language LLM | Structured Contracts |
|---|---:|---:|
| Correct decisions | 5/10 | 8/10 |
| Routing accuracy | 50% | 80% |
| Total measured time | 36.7451 seconds | 80.9153 seconds |

The structured approach achieved 30 percentage points higher routing accuracy.

However, it required approximately 2.2 times the total measured execution time because it generated two contracts for every independent case.

The results therefore demonstrate an accuracy improvement in this small benchmark, but not an end-to-end latency advantage.

The direct LLM selected `Deploy Code` in all 10 cases, including all five failed-test scenarios.

**Source:** `docs/matched_independent_nl_results.json`

### 3. Independent Interpretation Repeatability

The structured Ollama interpreter was evaluated on 10 independent natural-language conditions, repeated three times each.

| Metric | Result |
|---|---:|
| Total interpretation attempts | 30 |
| Correct interpretations | 25 |
| Interpretation accuracy | 83.3% |
| Cases with identical normalized predictions | 9/10 |
| Case-level stability | 90% |

IND06 was consistently interpreted incorrectly across all three repetitions.

IND10 produced different interpretations across repetitions, demonstrating that temperature 0 did not guarantee identical semantic predictions.

These findings distinguish interpretation accuracy from interpretation repeatability. A stable interpretation can still be semantically incorrect.

**Source:** `docs/independent_interpretation_consistency_results.json`

### 4. Semantic Consistency Validation

An oracle-based retrospective validation experiment compared generated contract conditions with independently annotated expected Boolean values.

Results:

- Semantic matches: 8/10
- Semantic mismatches: 2/10
- Other validation failures: 0
- Semantic match rate: 80%

The two confirmed mismatches were IND06 and IND10.

In both cases, the expected Boolean value was `false`, but the generated contract contained `true`.

The contracts satisfied structural validation despite being semantically incorrect.

For the evaluated failed-test workflow states, deterministic routing returned `NO_MATCH` rather than incorrectly selecting deployment.

This demonstrates that deterministic routing can avoid arbitrary next-node selection when no contract matches, but it cannot repair incorrect natural-language interpretation.

The semantic consistency validator uses trusted benchmark annotations. It is an evaluation mechanism, not an independent production-time semantic verification system.

**Source:** `docs/independent_semantic_consistency_results.json`

### 5. Overall Research Interpretation

The experiments provide preliminary evidence that separating natural-language interpretation from deterministic execution can improve expected-route accuracy in the tested workflow.

They also identify important limitations:

- Semantic interpretation errors remain possible.
- Structural contract validity does not guarantee semantic correctness.
- Temperature 0 does not guarantee identical semantic interpretations.
- Deterministic execution does not imply correct contract generation.
- Contract construction introduces an initial computational cost.
- Latency advantages depend on contract reuse and the number of workflow executions.
- The direct and structured methods use different prompt guidance and output constraints.
- The independent benchmark contains only 10 paraphrases and a small workflow graph.
- These experiments do not establish generalization to larger autonomous software-development workflows.

The strongest supported conclusion is that **deterministic contract execution can improve routing reliability when contracts accurately represent their intended natural-language conditions, while semantic interpretation remains a critical source of errors requiring separate evaluation and validation.**

### 6. Future Research

Future experiments should evaluate larger workflow graphs, more diverse condition types, independently annotated semantic benchmarks, prompt-equivalent baselines, repeated end-to-end trials, and amortized latency across different contract-reuse counts.

Production-time semantic verification should also be investigated without assuming access to benchmark ground-truth labels.
## Repeated Matched Independent Natural-Language Evaluation

### Experimental Design

A repeated matched independent natural-language comparison was conducted using the ten independent paraphrase cases (IND01–IND10).

Each case was evaluated three times under the same workflow state and natural-language edge descriptions, producing 30 routing decisions per method.

The experiment compared:

- Direct natural-language LLM routing.
- LLM-generated structured semantic contracts followed by validation and deterministic routing.

The model was `llama3.2:3b`, configured with temperature 0. Structured contracts were regenerated for every repetition rather than reused across repetitions.

### Results

| Metric | Direct LLM | Structured Contracts |
|---|---:|---:|
| Total decisions | 30 | 30 |
| Correct decisions | 15 | 24 |
| Expected-route accuracy | 50.0% | 80.0% |
| Cases with identical repeated decisions | 10/10 | 10/10 |
| Total measured execution time | 89.5295 seconds | 253.5074 seconds |

The structured approach achieved a 30-percentage-point higher expected-route accuracy in this controlled benchmark.

Both methods produced stable decisions across all three repetitions for every case. However, stable decisions did not necessarily indicate correct decisions.

### Error Analysis

The direct LLM consistently selected `Deploy Code`, including in scenarios where the expected destination was `Fix Code`.

The structured approach produced incorrect interpretations for IND06 and IND10. In these cases, failure-related conditions were interpreted as requiring `tests_passed = True` rather than `False`.

These errors caused the structured router to produce no matching route for the failed-test state rather than select the expected repair transition.

Across the repeated experiment, 24 of 30 target paraphrase interpretations were correct.

### Execution Overhead

The direct LLM method required approximately 89.53 seconds in total.

The structured method required approximately 253.51 seconds, including fresh interpretation of both natural-language edges during every repetition.

Therefore, the structured approach was slower in this repeated end-to-end comparison. The additional interpretation calls contributed to its higher measured overhead.

### Interpretation and Limitations

The results provide evidence that structured semantic contracts can improve expected-route accuracy in the tested workflow, while deterministic execution remains dependent on the correctness of the generated contracts.

The experiment has several limitations:

- Only ten independent paraphrases and one workflow graph were evaluated.
- Each case used one workflow state.
- The structured interpreter received explicit Boolean interpretation guidance that was not supplied to the direct routing method.
- The structured method made two LLM interpretation calls per repetition, while the direct method made one routing call.
- Contract construction was repeated rather than amortized across multiple routing decisions.
- Decision stability was measured, but full workflow-path repeatability and trace persistence were not evaluated in this experiment.

Consequently, the observed accuracy difference cannot be attributed exclusively to the semantic-contract architecture.

### Research Significance

This experiment strengthens the proposal's repeated-comparison evidence by demonstrating that routing consistency, expected-route accuracy, and execution overhead can be evaluated separately.

The results also reinforce a central finding: deterministic execution provides consistent evaluation of structured contracts, but it does not guarantee that natural-language conditions were interpreted correctly.

**Source data:** `docs/repeated_matched_independent_nl_results.json`

**Experiment script:** `src/test_repeated_matched_independent_nl.py`