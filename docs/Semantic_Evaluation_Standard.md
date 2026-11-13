# A2 Research — Semantic Evaluation Standard

## Objective

Evaluate whether a natural-language interpreter preserves the intended meaning of workflow edge conditions.

## Evaluation Dimensions

### 1. Condition Correctness

Does the generated condition match the intended field, operator, and value?

Example:

"If all software tests have passed, proceed to deployment."

Expected condition:
- Field: `tests_passed`
- Operator: `equals`
- Value: `True`

### 2. Routing Correctness

Does the generated contract preserve the intended source node and target node?

Example:
- Source: `Check Tests`
- Target: `Deploy Code`

### 3. Interpretation Coverage

Does the interpreter produce a valid interpretation or return `None`?

Returning `None` is treated as an abstention, not as a successful semantic interpretation.

Abstentions must be reported separately and included as unsuccessful cases when calculating overall interpretation accuracy.

### 4. Ambiguity and Insufficient Information

Some sentences describe a restriction without specifying a complete routing action.

Example:

"Do not deploy if the test suite contains failures."

This does not explicitly identify `Fix Code` as the next workflow node.

Such examples must be labeled carefully rather than assuming a destination.

When a predefined workflow graph or benchmark annotation supplies the destination, the evaluation must distinguish that supplied information from information independently inferred by the interpreter.

## Evaluation Rules

A complete semantic contract is correct only when:

1. The condition field matches the reference.
2. The operator matches the reference.
3. The condition value matches the reference.
4. The source node matches the reference.
5. The target node matches the reference.

An interpretation is incorrect if any required component differs from the reference.

Abstentions are counted separately and are also included as unsuccessful cases when calculating overall accuracy.

The following metrics must be distinguished:

- **Condition interpretation accuracy:** Agreement of the generated field, operator, and value with the reference condition.
- **Complete semantic-contract accuracy:** Agreement of all five contract components with an independently reviewed reference contract.
- **Expected-route accuracy:** Whether the selected next node matches the benchmark's expected destination.
- **Interpretation coverage:** The proportion of cases for which the interpreter produces an interpretation rather than abstaining.
- **Decision repeatability:** Whether repeated evaluations of the same case produce identical routing decisions.

Decision repeatability does not establish semantic correctness. An interpretation or routing decision can be stable but incorrect.

## Historical Rule-Based Baseline

The initial natural-language interpretation baseline used an exact-match, rule-based Python interpreter and four natural-language conditions.

Results:

| Metric | Result |
|---|---:|
| Total cases | 4 |
| Correct interpretations | 2 |
| Interpretation accuracy | 50% |
| Abstentions | 2 |
| Abstention rate | 50% |

The interpreter recognized the two predefined conditions but abstained on two unseen paraphrases.

These results measure agreement with manually specified Boolean reference values, not independently verified complete semantic-contract accuracy.

**Source:** `docs/NL_Interpretation_Baseline_Results.md`

## Later Independent LLM Evaluation

Later experiments evaluated LLM-based interpretation and routing using a different dataset, model, and experimental design.

The repeated matched independent natural-language evaluation used ten paraphrase cases, each evaluated three times.

Results:

| Metric | Direct LLM Routing | Structured Contract Routing |
|---|---:|---:|
| Routing decisions | 30 | 30 |
| Correct routing decisions | 15 | 24 |
| Expected-route accuracy | 50% | 80% |
| Cases with identical repeated decisions | 10/10 | 10/10 |

The structured method also produced 24 correct target-paraphrase condition interpretations across 30 attempts.

These interpretation results should not be described as independently evaluated complete semantic-contract accuracy because the experiment supplied the source and target nodes from predefined workflow scenarios.

**Source:** `docs/repeated_matched_independent_nl_results.json`

**Experiment script:** `src/test_repeated_matched_independent_nl.py`

## Research Limitations

1. Reference labels require independent review.

2. The current ten-case independent dataset is preliminary and uses a small Boolean workflow graph.

3. The initial four-case rule-based baseline and later LLM experiments use different datasets and methods. Their accuracy figures must not be combined into a single overall accuracy measure.

4. Structural validation verifies contract format and permitted values but does not guarantee that the generated condition preserves the original natural-language meaning.

5. The structured LLM interpreter received additional Boolean interpretation guidance that was not supplied to the direct LLM routing method. Therefore, differences in expected-route accuracy cannot be attributed exclusively to the semantic-contract architecture.

6. The current experiments do not independently establish complete semantic-contract accuracy across generated source nodes, target nodes, and conditions.

7. Temperature 0 does not guarantee correct or identical semantic interpretations across repeated model calls.

8. Repeated decisions can be consistent while remaining incorrect.

9. Oracle-based semantic consistency checks rely on trusted benchmark annotations and do not constitute an independent production-time semantic verification system.

10. Future experiments should use independently reviewed reference contracts, larger workflow graphs, more diverse condition types, prompt-equivalent comparisons, and separate reporting of condition accuracy, complete contract accuracy, routing accuracy, coverage, and repeatability.

## Evaluation Conclusion

The evaluation standard separates natural-language interpretation correctness from deterministic routing correctness.

The available results provide preliminary evidence that structured semantic contracts can improve expected-route accuracy in the tested workflow. However, deterministic execution depends on the semantic correctness of the generated contracts.

A structurally valid contract may still misrepresent its original natural-language condition. Therefore, interpretation accuracy, contract validity, routing correctness, and repeatability must be evaluated and reported as distinct research outcomes.