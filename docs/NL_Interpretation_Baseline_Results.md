
# A2 Research — Natural-Language Interpretation Baseline Results

## Research Objective

Evaluate whether a rule-based interpreter can translate
natural-language edge conditions into structured semantic
conditions.

## Experimental Setup

Interpreter: Exact-match, rule-based Python interpreter

Dataset: Four natural-language conditions

- NL01: Original positive condition
- NL02: Original negative condition
- NL03: Positive paraphrase
- NL04: Negative paraphrase

Reference labels were manually specified.

## Results

| Case | Expected | Predicted | Correct |
|------|----------|-----------|---------|
| NL01 | True | True | Yes |
| NL02 | False | False | Yes |
| NL03 | True | None | No |
| NL04 | False | None | No |

Total cases: 4

Correct interpretations: 2

Accuracy: 50%

Abstention rate: 50%

## Research Observation

The interpreter correctly recognized both predefined
natural-language conditions.

However, it rejected two paraphrases expressing similar
meanings.

This demonstrates a limitation of exact-match rule-based
interpretation: it cannot recognize unseen wording without
additional rules.

## Limitations

1. The dataset contains only four examples.
2. Two examples were used to define the interpreter rules.
3. Reference labels have not undergone independent review.
4. Accuracy measures Boolean-value agreement rather than
   complete semantic-contract correctness.
5. No LLM-based comparison has been conducted yet.

## Conclusion

The rule-based baseline achieved 50% accuracy on this
initial four-case dataset.

The results provide a preliminary baseline for future
evaluation of natural-language edge interpretation.
