# Week 3 Controlled Comparison Protocol â€” Draft

## Objective
Compare direct LLM routing with structured-contract routing under matched natural-language workflow conditions.

## Methods
- Direct baseline: LLM selects the next workflow node from natural-language instructions.
- Structured approach: LLM interprets the condition into a semantic contract; deterministic code validates and evaluates the contract.
- Use the same local model, workflow scenarios, available destinations, and reference answers where applicable.
- Record model settings, prompts, repetitions, and any differences between methods.

## Evaluation Procedure
1. Define independent test cases and expected destinations before evaluation.
2. Execute both approaches using the documented test cases.
3. Preserve raw responses, generated contracts, routing decisions, and failures.
4. Compare decisions against the same reference answers.
5. Report accuracy, invalid outputs, repeatability, and timing with clearly defined measurement boundaries.
6. Distinguish contract construction time from deterministic contract evaluation time.

## Fairness and Limitations
Document differences in prompting, number of LLM calls, contract reuse, and preprocessing. Do not attribute performance differences solely to semantic contracts without appropriate controls.

## Current Status
Protocol drafted during Week 3. Existing pilot and experimental results are preliminary evidence, not the formal Week 9 controlled evaluation.
