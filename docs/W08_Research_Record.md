# Week 08 — Evaluation readiness Research Record

**Course:** CISC 699 — Capstone II  
**Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution  
**Scheduled week:** January 4–10, 2027  
**Work packages:** WP05, WP07, WP08, WP06  
**Status:** NOT STARTED — planning template; complete only after this week's work

## Objective and planned work
Finalize defensible scenarios and expected-route oracle, repetitions, comparability controls, logging fields, metric definitions and rerun/stop rules. Verify integration and component tests.

## Actual work performed
**PENDING:** Enter dated, personally verified activities after completing them. Identify source files, test commands, configuration, and outcomes. Do not paste planned activities here as completed work.

## Evidence and deliverables to retain
**Planned:** Versioned scenario set; oracle and adjudication notes; protocol; baseline/proposed comparability sheet; logging validation; readiness decision.  
**Actual paths and versions:** PENDING — add links or repository-relative paths after checking they exist.

## Verification and observations
**Planned check:** Check M5/M7 and Gate 4 only against documented evidence and any required approvals.  
**Observed results, failures, and blockers:** PENDING — include actual outputs and unresolved items.

## Methodological caution
Formal runs must not be presented as approved merely because older pilot JSON files exist.

## AI assistance and independent verification
**PENDING:** Describe any AI assistance actually used this week and how outputs, code, figures, and claims were independently checked.

## Next action and report contribution
W09: run the frozen controlled evaluation and preserve raw evidence. **Report linkage:** PENDING — record chapter/section and supported claims after verification.

## Early evaluation-readiness review � November 13, 2026
Reviewed the existing Chapter 4 methodology, 10-case evaluation dataset, three-method comparison script, and three-node workflow graph. Verified 30 saved comparison records covering IND01�IND10 three times each, with no expected-route oracle mismatches and consistent method summaries. Verified 20 saved workflow records reporting correct paths and 20 readable JSON trace files. Verified contract-reuse evidence containing 30 decisions, with 27 correct (90% accuracy), consistent with its saved summary. The separate graph-transition test uses a four-node example graph; the evaluated prototype uses three nodes. These checks reviewed previously recorded evidence only; no formal Week 9 evaluation was rerun. Evaluation readiness approval, protocol finalization, and scheduled Week 8 activities remain pending. AI assistance was used to guide read-only checks; outputs were verified in VS Code PowerShell.
- Benchmark source: `src/independent_evaluation_dataset.py`
- Syntax verification: Passed using Python `ast.parse`.
- Dataset SHA-256: `5F4C7EECAEA29B993522EEE00D4652186F8CB3387A5617CA94462EA1225D64B0`
- Gate 3 status: Dataset snapshot identified. Independent review of expected-route labels remains pending, including the workflow-supplied `Fix Code` destinations for IND04 and IND08 and the meaning of “all checks” in IND09.
### Early readiness findings

- Benchmark snapshot: `src/independent_evaluation_dataset.py` passed a Python syntax check using `ast.parse`. SHA-256: `5F4C7EECAEA29B993522EEE00D4652186F8CB3387A5617CA94462EA1225D64B0`.
- Expected routes: The benchmark has five `Deploy Code` cases and five `Fix Code` cases. The workflow supplies `Fix Code` for IND04 and IND08 because their wording only blocks deployment. IND09 uses “all checks” to refer to the test suite. Scoring definitions are in `docs/Semantic_Evaluation_Standard.md`.
- Preliminary comparison: `src/test_prompt_controlled_comparison.py` compares original direct LLM routing, Boolean-guidance-aligned direct LLM routing, and structured-contract routing. It documents three repetitions per case. Prompt wording, output constraints, and LLM call counts differ across methods. Saved evidence: `docs/prompt_controlled_comparison_results.json`. Proposal alignment: `docs/proposal_objective_alignment.md`.
- Gate 3 — Pending. The dataset snapshot and route mapping are documented. Confirm the expected-route label review or document the basis for accepting the labels under the work plan.
- Gate 4 — Pending. The available comparison protocol is a draft. Confirm the formal comparison methods, model settings and prompts, repetitions, required trace fields, readiness checks, and stop and rerun criteria before formal evaluation.
November 14, 2026: Simulated an interruption during IND01 repetition 2 using stubbed model calls. The runner preserved repetition 1, marked the run as stopped, and listed repetition 2 as missing. The test used a temporary folder and made no Ollama requests.
- November 14, 2026 — Structured timeout readiness test passed. A simulated `TimeoutError` during IND01 repetition 1 was preserved in the saved observation. The runner marked the run as stopped and listed repetition 2 as missing. Together with the interruption test, this verifies that the runner preserves completed observations and accounts for missing repetitions in both tested scenarios. The tests used temporary folders and made no Ollama requests.
- Expected-route proposal: Use `Deploy Code` when `tests_passed` is `True` and `Fix Code` when it is `False`, as defined by the benchmark workflow.
- Cases for review: IND04 and IND08 prohibit deployment. Their `Fix Code` label comes from the workflow graph. IND09 treats “all checks” as the test suite.
- Gate 3 status: Pending. Review or acceptance of this labeling rationale is unverified. Record the reviewer, date, decision, and any changes before freezing the benchmark for formal evaluation.
The planned evaluation uses three repetitions per case under each of the three methods. This yields 30 matched case–repetition groups and 90 routing decisions. Three repetitions fit the evaluation scope and let us measure within-case decision consistency on this benchmark.
- November 14, 2026 — Verified Python source revision `8804ae960f53140f8f130a84350213a6efda6885`. Git reported no changes under `src`. Local Ollama reported version `0.40.14` and model `llama3.2:3b` with digest `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`. No model calls were made. Recheck these values and save them alongside the formal run manifest before starting the evaluation.
- November 14, 2026 — Verified the provenance procedure with test data. `manifest.json` and `provenance.json` shared the same run ID, and the Git commit, Ollama version, and model digest fields were read back successfully. No model calls were made. Capture the actual values when preparing the formal Week 9 run.
## Week 8 closeout and Week 9 handoff

- Gate 3 — Pending. The benchmark snapshot and expected-route rationale are documented. Review or acceptance of the labels for IND04, IND08, and IND09 remains unverified.
- Gate 4 — Pending final protocol freeze. The interruption, structured timeout, and provenance checks passed with simulated inputs. The protocol specifies three repetitions per case per method.
- Week 9 preparation — Record the Gate 3 decision, freeze the evaluation protocol, and recheck the source revision and Ollama model digest before starting formal runs.