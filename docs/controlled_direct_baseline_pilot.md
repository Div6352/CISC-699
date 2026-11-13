# Controlled Direct LLM Baseline — Pilot Results

## Purpose

Evaluate whether adding explicit Boolean interpretation guidance to the direct natural-language routing baseline eliminates incorrect decisions in a preliminary two-scenario test.

## Experimental Configuration

- Model: `llama3.2:3b`
- Temperature: `0`
- Interpreter: `src/direct_nl_llm_router_controlled.py`
- Current workflow node: `Check Tests`
- Available destinations: `Deploy Code`, `Fix Code`
- Workflow variable: `tests_passed`
- Number of scenarios: 2
- Repetitions per scenario: 1

The controlled prompt includes Boolean guidance corresponding to the structured interpreter. The direct baseline still selects a destination without generating semantic contracts.

## Observed Results

| Scenario | Expected Destination | Actual Destination | Correct |
|---|---|---|---|
| `tests_passed = True` | `Deploy Code` | `Deploy Code` | Yes |
| `tests_passed = False` | `Fix Code` | `Deploy Code` | No |

**Pilot accuracy: 1/2 (50%).**

Raw model responses:

- Passing-tests scenario: `Deploy Code`
- Failing-tests scenario: `Deploy Code`

## Interpretation

The controlled direct baseline returned an allowed destination in both scenarios but selected the wrong destination when `tests_passed` was false.

Adding explicit Boolean guidance did not eliminate the observed routing error in this pilot. This observation does not establish why the model failed or whether the error would persist across additional repetitions.

## Limitations

- Only two scenarios were tested.
- Each scenario was executed once.
- These test conditions differ from the ten independent paraphrases used in the main experiment.
- The test does not measure complete workflow execution or persisted trace generation.
- The test does not establish the causal effect of semantic contracts.

## Next Evaluation

Run a separately labeled, prompt-controlled comparison using the existing ten independent natural-language cases and repeated decisions. Preserve the original baseline and experimental results unchanged.
