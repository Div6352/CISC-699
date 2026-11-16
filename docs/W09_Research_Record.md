# Week 09 — Controlled evaluation and data validation Research Record

**Course:** CISC 699 — Capstone II  
**Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution  
**Scheduled week:** January 11–17, 2027  
**Work packages:** WP08  
**Status:** NOT STARTED — planning template; complete only after this week's work

## Objective and planned work
Execute direct-LLM and structured-contract conditions on the frozen scenario set using approved repetitions; log model/configuration, prompts, contracts, decisions, routes, traces, errors and timing where reliable.

## Actual work performed
**PENDING:** Enter dated, personally verified activities after completing them. Identify source files, test commands, configuration, and outcomes. Do not paste planned activities here as completed work.

## Evidence and deliverables to retain
**Planned:** Immutable raw runs; run inventory; configuration manifest; missing/failed observation log; data-integrity checks; deviations.  
**Actual paths and versions:** PENDING — add links or repository-relative paths after checking they exist.

## Verification and observations
**Planned check:** Cross-check every result against scenario ID, condition, repetition and expected-route oracle.  
**Observed results, failures, and blockers:** PENDING — include actual outputs and unresolved items.

## Methodological caution
Never silently replace failed runs or alter protocol; record deviations and approved reruns.

## AI assistance and independent verification
**PENDING:** Describe any AI assistance actually used this week and how outputs, code, figures, and claims were independently checked.

## Next action and report contribution
W10: analyze only validated data and integrate findings into report. **Report linkage:** PENDING — record chapter/section and supported claims after verification.
## Early preparation and Week 8 handoff

- Week 8 readiness evidence and open decisions are recorded in `docs/W08_Research_Record.md` and preserved in GitHub commit `cd8e7d913e31f24bb8e89ef0d91e939a7b4f6bb3`.
- Gate 3 remains pending. Record the decision on the expected-route labeling rationale, including IND04, IND08, and IND09, before freezing the benchmark.
- Gate 4 remains pending. Freeze the comparison protocol, then recheck the Git source revision, Ollama version, and model digest before execution.
- The planned comparison uses 10 cases, three repetitions, and three methods, for 30 matched case–repetition groups and 90 routing decisions.
### Formal run validation checklist

- [ ] Before execution, record the Gate 3 label decision and the frozen Gate 4 protocol revision.
- [ ] Capture the source commit, Ollama version, and model digest. Verify that `manifest.json` and `provenance.json` share the same run ID.
- [ ] Reconcile the saved observations against all 30 planned case–repetition groups. Check each group for duplicate keys, the expected route, and one outcome for each of the three methods.
- [ ] Record errors, missing observations, and deviations. Preserve the original evidence and link any rerun to its original run ID.
- November 14, 2026 — Early Week 9 preflight passed. Git revision `cd8e7d913e31f24bb8e89ef0d91e939a7b4f6bb3` reported no changes under `src`. The benchmark SHA-256 was `5F4C7EECAEA29B993522EEE00D4652186F8CB3387A5617CA94462EA1225D64B0`. Ollama reported version `0.40.14` and model `llama3.2:3b` with digest `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`. These values matched the Week 8 evidence. No model calls were made.
- November 14, 2026 — Ran the deterministic workflow-path and trace check using manually authored reference contracts. The passing and failing test states each ran ten times. All 20 runs reached their expected destination, both scenarios produced identical paths across repetitions, and all 20 persisted traces passed the script’s checks. Evidence: `docs/workflow_path_runs/20261114T072055Z-4284a7908c79/results.json` and the adjacent `traces/` folder.
- Validated formal run `20261114T072805Z-7fea28e98cfa` against frozen protocol commit `7a75319f793bb26808c5c309a5d38263fcd69618`. The manifest, provenance, summary, and observations shared the same run ID. All 30 planned case–repetition groups were present and unique. Recomputed scores matched the frozen benchmark and saved summary.
- Expected-route accuracy was 15/30 (50%) for original direct routing, 15/30 (50%) for guidance-aligned direct routing, and 24/30 (80%) for structured-contract routing. All three methods were stable on 10/10 cases. The structured method's stable outcomes included two cases that consistently produced no route.
- Evidence: `docs/comparison_runs/20261114T072805Z-7fea28e98cfa/`. Use the validated observations for the Week 10 analysis of accuracy, repeatability, failure patterns, and timing.
**Status:** COMPLETE — formal evaluation executed and validated on November 14, 2026.