# Week 10 — Analysis and report integration Research Record

**Course:** CISC 699 — Capstone II  
**Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution  
**Scheduled week:** January 18–24, 2027  
**Work packages:** WP09, WP10  
**Status:** NOT STARTED — planning template; complete only after this week's work

## Objective and planned work
Calculate accuracy, consistency, path repeatability, trace completeness, validation outcomes and measurable overhead; inspect errors and limitations; integrate supported claims into report.

## Actual work performed
**PENDING:** Enter dated, personally verified activities after completing them. Identify source files, test commands, configuration, and outcomes. Do not paste planned activities here as completed work.

## Evidence and deliverables to retain
**Planned:** Analysis scripts/sheets; tables and figures; error classification; claim-to-evidence map; report sections; writing-guide status.  
**Actual paths and versions:** PENDING — add links or repository-relative paths after checking they exist.

## Verification and observations
**Planned check:** Verify calculations against raw data and check instructor writing guide availability/version.  
**Observed results, failures, and blockers:** PENDING — include actual outputs and unresolved items.

## Methodological caution
Separate pilot evidence from formal evaluation; do not generalize beyond tested scenarios/model.

## AI assistance and independent verification
**PENDING:** Describe any AI assistance actually used this week and how outputs, code, figures, and claims were independently checked.

## Next action and report contribution
W11: complete and technically review the full draft. **Report linkage:** PENDING — record chapter/section and supported claims after verification.
- November 14, 2026 — Analyzed all 30 validated Week 9 case–repetition observations from run `20261114T072805Z-7fea28e98cfa`. All methods scored 15/15 on deploy cases. On repair cases, original direct and guidance-aligned direct routing each scored 0/15, while structured routing scored 9/15. IND02, IND04, and IND08 accounted for all nine additional correct structured decisions. Structured routing returned `NO_MATCH` in all repetitions of IND06 and IND10. No experiments were rerun.
- Checked all six saved observations for IND06 and IND10. In every repetition, repair edge `E02` had an expected Boolean value of `False` and a predicted value of `True`. All six contracts passed structural validation, and all six routing outcomes were `NO_MATCH`. Classified these failures as Boolean interpretation errors. The repeated outcomes were consistent across runs, but they missed the expected repair route.
- Structured target-paraphrase condition interpretation accuracy was 24/30 (80%). The calculation used one benchmark paraphrase per saved observation and excluded the companion reference edge. The six errors were the three repetitions each of IND06 and IND10. This measure covers the condition field, operator, and value. The benchmark supplied the source and target nodes.
- Across 30 matched observations, mean decision time was 3.60 s for original direct routing, 4.02 s for guidance-aligned direct routing, and 8.45 s for structured-contract routing. Structured contract construction averaged 8.449015 s and deterministic routing averaged approximately 11 microseconds. Contract construction includes two LLM calls per decision. Methods ran sequentially on the same local setup, so the observed timing difference reflects the full methods as implemented.
- Verified `src/analyze_week09_results.py` by running `python src/analyze_week09_results.py`. The script checked the frozen benchmark fingerprint, matched run IDs, reconciled all 30 planned observations, and reproduced the saved accuracy counts and timing totals for all three methods. No model calls were made.