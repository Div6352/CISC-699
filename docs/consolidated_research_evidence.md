# CISC 699 Capstone II A2 — Consolidated Research Evidence

**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Document status:** Preliminary experimental evidence summary  
**Purpose:** Consolidate observed results for final-report preparation and reproducibility review.

## 1. Research Objective

This project investigates whether structured natural-language edge semantics can improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows.

The implemented prototype separates natural-language condition interpretation from deterministic contract evaluation and graph-transition enforcement.

The experiments below examine different aspects of that architecture. Their measurements must be interpreted separately.

## 2. Prompt-Controlled Routing Comparison

**Evidence file:** `docs/prompt_controlled_comparison_results.json`

The experiment evaluated 10 independent natural-language test cases, repeated three times each, producing 30 routing decisions per method.

| Method | Correct Decisions | Accuracy | Stable Cases | Total Time | LLM Calls |
|---|---:|---:|---:|---:|---:|
| Original direct natural-language routing | 15/30 | 50.0% | 10/10 | 100.73 s | 30 |
| Prompt-controlled direct routing | 15/30 | 50.0% | 10/10 | 112.17 s | 30 |
| Fresh structured contract interpretation and routing | 24/30 | 80.0% | 10/10 | 249.70 s | 60 |

### Observations

Fresh structured interpretation achieved 30 percentage points higher observed routing accuracy than the prompt-controlled direct baseline.

However, fresh structured interpretation required approximately 2.23 times the total execution time of the prompt-controlled direct method in this run.

All methods produced stable outcomes across repeated evaluations of each case. Stability alone did not guarantee correctness.

### Limitations

- The experiment included 10 distinct natural-language cases, not 30 independent cases.
- Direct and structured approaches differed in output constraints and execution architecture.
- Prompt guidance was made more comparable but was not identical across methods.
- Timing was measured in sequential experimental runs and may be affected by runtime conditions.
- These results do not establish that the architecture alone caused the accuracy difference.

## 3. Contract-Reuse Experiment

**Evidence file:** `docs/contract_reuse_experiment_results.json`

This experiment constructed semantic contracts once per case and reused them for three routing decisions.

| Metric | Observed Result |
|---|---:|
| Independent test cases | 10 |
| Routing decisions | 30 |
| Correct routing decisions | 27/30 |
| Accuracy | 90.0% |
| Stable cases | 10/10 |
| Contract construction time | 92.4455 s |
| Deterministic routing time | 0.000454 s |
| Total measured time | 92.4460 s |
| Average total time per decision | 3.0815 s |
| Total LLM calls | 20 |

### Observations

Contract reuse reduced the number of LLM calls from 60 in the fresh structured experiment to 20.

The observed total runtime was approximately 63% lower than that of the earlier fresh structured experiment.

Deterministic routing itself accounted for only a very small portion of measured runtime.

### Limitations

- The 30 routing decisions reused 10 constructed contract sets.
- The same workflow state was reused within each case.
- Reusing an incorrect contract can reproduce an incorrect decision consistently.
- The 90% accuracy observed in this run does not prove that reuse improves semantic interpretation accuracy.
- Timing comparisons are across separate experimental runs rather than a controlled simultaneous benchmark.
- The average of 3.0815 seconds includes contract construction amortized across decisions; it is not the latency of an individual deterministic routing operation.

## 4. Complete Prototype Workflow-Path and Trace Experiment

**Results file:** `docs/workflow_path_trace_experiment_results.json`  
**Trace directory:** `docs/workflow_path_trace_experiment_traces/`

The implemented graph contains three nodes:

- `Check Tests`
- `Deploy Code`
- `Fix Code`

It supports two directed transitions:

- `Check Tests → Deploy Code`, when `tests_passed` is `True`.
- `Check Tests → Fix Code`, when `tests_passed` is `False`.

The experiment evaluated both workflow states, with 10 repetitions per state.

It used manually authored reference contracts to isolate deterministic execution, graph routing, and trace persistence.

| Metric | Observed Result |
|---|---:|
| Total workflow runs | 20 |
| Correct terminal paths | 20/20 |
| Path accuracy | 100.0% |
| Stable scenarios | 2/2 |
| Saved trace files | 20 |
| Unique trace identifiers | 20 |
| Unique trace filenames | 20 |
| Trace checks passed | 20/20 |

### Independent Evidence Verification

A separate verification script confirmed:

- The results JSON contained 20 workflow records.
- All 20 recorded paths were correct.
- All 20 trace files existed and could be read.
- All saved traces recorded the expected routing outcome.
- All 20 trace identifiers were unique.

### Limitations

- Each complete path contained one graph transition.
- The graph does not include a `Start` node.
- The experiment did not test multi-transition workflows.
- The contracts were manually authored rather than interpreted from natural language.
- No external software-development agent or deployment operation was executed.
- Unexpected exceptions may prevent trace creation.
- Trace verification covered the required fields and selected values; it was not a comprehensive audit of every possible failure mode.

## 5. Interpretation Across Experiments

The experiments provide evidence for three distinct properties of the implemented prototype.

**Semantic interpretation and routing accuracy:** The fresh structured approach achieved higher observed accuracy than both direct-routing baselines in the tested natural-language cases, although the comparison does not fully isolate the architectural cause.

**Computational overhead:** Fresh semantic interpretation incurred substantial LLM overhead. Reusing constructed contracts reduced model calls and total measured execution time in a separate experiment.

**Deterministic execution and auditability:** With manually authored reference contracts, the prototype produced correct, repeatable terminal paths for both tested Boolean workflow states. Each tested routing decision generated a persisted trace that passed the independent verification checks.

These findings support the feasibility of separating natural-language interpretation from deterministic workflow routing within the scope of the implemented prototype.

They do not establish universal routing correctness, generalization to complex graphs, or production-level reliability.

## 6. Evidence and Reproducibility Boundaries

All reported values are based on recorded local experimental output.

The experimental artifacts should be retained without modification, including result JSON files, source scripts, and generated trace files.

Before final submission, the evaluation protocol, execution environment, test-case selection, limitations, and any instructor-required approvals should be reviewed and documented.

These results constitute preliminary experimental evidence and should not be described as a formally approved final evaluation unless that approval has been obtained.

## 7. Final Report Placement

**Chapter 3 — Design and Implementation:** Contract representation, interpretation, deterministic evaluation, graph enforcement, and execution-trace architecture.

**Chapter 4 — Evaluation Methodology:** Test datasets, baselines, repeated trials, contract-reuse protocol, workflow-path protocol, metrics, and reproducibility procedures.

**Chapter 5 — Results:** Accuracy comparisons, measured overhead, contract-reuse results, path repeatability, and trace verification.

**Chapter 6 — Discussion and Validity:** Interpretation errors, repeatability versus correctness, prompt comparability, limited graph complexity, timing variability, and auditability boundaries.

**Appendices:** Experimental scripts, JSON result references, representative trace examples, and verification procedures.
