# Week 3 Controlled Comparison Protocol - Draft updated for Week 8

## Objective

Compare direct LLM routing with structured-contract routing under matched natural-language workflow conditions. Measure expected-route accuracy, edge-decision repeatability, and execution time.

## Benchmark and expected routes

Candidate benchmark: `src/independent_evaluation_dataset.py`, cases IND01 through IND10.
Dataset SHA-256: `5F4C7EECAEA29B993522EEE00D4652186F8CB3387A5617CA94462EA1225D64B0`.

The benchmark maps `tests_passed = True` to `Deploy Code` and `tests_passed = False` to `Fix Code`. The workflow supplies `Fix Code` for IND04 and IND08 because those cases only prohibit deployment. IND09 treats "all checks" as the test suite. Confirm the expected-route labels and document the review decision before freezing the benchmark. Apply the scoring definitions in `docs/Semantic_Evaluation_Standard.md`.

## Comparison methods

Use the same case, starting node, candidate edges, workflow state, and expected destination in each paired observation.

1. Original direct LLM routing. One model call per decision.
2. Boolean-guidance-aligned direct LLM routing. One model call per decision. This comparison helps assess the effect of explicit Boolean guidance.
3. Structured-contract routing. Two model calls per decision to interpret the candidate edges, followed by contract validation and deterministic routing. Regenerate contracts for each repetition.

The candidate design follows `src/test_prompt_controlled_comparison.py`. Its saved results in `docs/prompt_controlled_comparison_results.json` are preliminary evidence.

## Verified model settings

- Local Ollama service version: `0.40.14`
- Local model: `llama3.2:3b`
- Model digest: `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`
- All three request paths use temperature 0, streaming disabled, and a 120-second HTTP timeout. The reviewed settings contain no explicit seed. The structured interpreter requests schema-constrained output.
- The local `/api/version` and `/api/tags` endpoints confirmed the runtime and model inventory. Recheck both before the formal run.

## Repetitions and analysis

Proposed repetition rule: run each of the ten cases three times under all three methods. This yields 30 paired observations and 90 method-level routing decisions. Three repetitions keep the comparison feasible and allow observed decision consistency to be checked within each case.

- Expected-route accuracy: correct routes divided by observed attempts for each method. Count observed errors, abstentions, and invalid outputs as unsuccessful attempts. Report missing observations separately against the planned total.
- Edge-decision repeatability: report how many cases with all three repetitions have identical recorded outcomes. Report incomplete cases and stable failures separately from stable valid routes.
- Timing: report direct method wall-clock time and separate structured contract construction from deterministic routing time. Record the sequential method order when interpreting timing.
- The comparison measures decisions at one workflow node. Any complete-path or persisted execution-trace claim requires separate evidence.

## Run evidence, stop and rerun rules

Assign a unique run ID and a writable evidence location separate from the pilot JSON before making model calls. Record the benchmark fingerprint, script and prompt versions, runtime and model digest, run start time, and planned cases and repetitions.

For each case and repetition, preserve the workflow state, expected destination, method, raw response or reference to it, generated contract and validation status where applicable, routing outcome, elapsed time, and any error. Preserve completed observations as the run progresses. Record missing case-repetition pairs at closeout.

Keep incorrect routes, abstentions, and invalid outputs as observed results. Stop and record the interruption if Ollama becomes unavailable or evidence cannot be written. If an incomplete run is repeated under the finalized protocol, use a new run ID and link it to the original with the reason and scope. Retain the original evidence.

## Current status

Week 8 candidate protocol. Gate 3 remains pending expected-route label review or acceptance of the documented rationale. Gate 4 remains pending protocol finalization and a readiness check demonstrating that formal evidence can be saved under a unique run ID and retained after an interruption. The current three-method script saves to a fixed pilot filename after collecting all results, so check for an existing runner with the required evidence handling before changing code or starting formal Week 9 runs.
Before the formal run, recheck the Ollama version and model digest. Save both with the run manifest, along with the Git commit identifying the runner and prompt source files. If those files have local edits, commit the exact versions used before recording the commit ID.
Planned repetition rule: Run each of the ten cases three times under each of the three methods. This yields 30 matched case–repetition groups and 90 routing decisions. Three repetitions keep the comparison feasible and let us measure within-case decision consistency.
Before starting the formal evaluation, capture the Git commit, Ollama version, and model digest. After the runner prints its evidence folder, save those values in provenance.json in that folder, alongside manifest.json. Use the same run ID in both files. At closeout, verify that both files are present and their run IDs match.