# Chapter 5 — Experimental Results

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary results chapter based on recorded local experiments

## 5.1 Introduction

This chapter presents the observed results of the prototype evaluation described in Chapter 4. The experiments examined natural-language routing accuracy, repeated decision stability, computational overhead, contract reuse, complete workflow paths, and execution-trace persistence.

Three principal experimental datasets are reported: the prompt-controlled routing comparison, the contract-reuse experiment, and the workflow-path and trace-persistence experiment.

The results are presented separately because the experiments used different protocols and, in the workflow-path experiment, different sources of semantic contracts.

## 5.2 Prompt-Controlled Routing Comparison

The prompt-controlled comparison evaluated 10 distinct natural-language cases, each repeated three times under three routing methods. Each method therefore produced 30 routing decisions.

### 5.2.1 Routing Accuracy

| Routing Method | Correct Decisions | Total Decisions | Accuracy |
|---|---:|---:|---:|
| Original direct natural-language routing | 15 | 30 | 50.0% |
| Prompt-controlled direct routing | 15 | 30 | 50.0% |
| Fresh structured contract routing | 24 | 30 | 80.0% |

The fresh structured method achieved 24 correct decisions, compared with 15 correct decisions for each direct-routing baseline.

This represented a 30-percentage-point difference in observed accuracy between fresh structured routing and the prompt-controlled direct baseline.

The results describe the behavior of the tested implementations and prompts. They do not independently establish that structured representation was the sole cause of the observed accuracy difference.

### 5.2.2 Repeated Decision Stability

| Routing Method | Stable Cases | Total Cases |
|---|---:|---:|
| Original direct routing | 10 | 10 |
| Prompt-controlled direct routing | 10 | 10 |
| Fresh structured routing | 10 | 10 |

All three methods returned stable outcomes across the three repetitions of each case.

However, the direct-routing methods achieved only 50% accuracy despite exhibiting stability in every case.

This demonstrates that repeated decision stability and routing correctness are distinct evaluation properties.

### 5.2.3 Execution Time and LLM Calls

| Routing Method | Total Time | Average Time per Decision | LLM Calls |
|---|---:|---:|---:|
| Original direct routing | 100.73 s | 3.36 s | 30 |
| Prompt-controlled direct routing | 112.17 s | 3.74 s | 30 |
| Fresh structured routing | 249.70 s | 8.32 s | 60 |

The fresh structured method required the greatest measured execution time.

Its total time was approximately 2.23 times that of the prompt-controlled direct baseline.

The structured method also required twice as many LLM calls because it interpreted two outgoing edge conditions for each routing decision.

These measurements include the operations performed by the respective experimental implementations and should not be interpreted as hardware-independent performance benchmarks.

**Primary evidence:** `docs/prompt_controlled_comparison_results.json`

## 5.3 Contract-Reuse Experiment

The contract-reuse experiment evaluated the same collection of 10 natural-language cases with three routing decisions per case.

Unlike the fresh structured experiment, contracts were generated once per case and reused for subsequent deterministic routing decisions.

### 5.3.1 Routing Accuracy and Stability

| Metric | Result |
|---|---:|
| Distinct natural-language cases | 10 |
| Repetitions per case | 3 |
| Total routing decisions | 30 |
| Correct decisions | 27 |
| Routing accuracy | 90.0% |
| Stable cases | 10/10 |

The experiment produced 27 correct decisions out of 30.

All 10 cases produced stable routing outcomes across their three repetitions.

The observed accuracy was higher than that recorded in the earlier fresh structured experiment. However, contract reuse itself does not correct semantic interpretation errors, and the difference cannot be attributed to reuse without additional controlled evidence.

### 5.3.2 Contract Construction and Routing Time

| Timing Metric | Measured Value |
|---|---:|
| Contract construction time | 92.445498 s |
| Deterministic routing time | 0.000454 s |
| Total time including construction | 92.445952 s |
| Average total time per decision | 3.081532 s |
| Average deterministic routing time per decision | 0.00001514 s |

Almost all measured execution time was associated with contract construction.

The deterministic routing component accounted for approximately 0.000454 seconds across the 30 routing decisions.

The average total time per decision includes the cost of constructing contracts amortized across the repeated decisions. It does not represent the latency of a single deterministic routing operation.

### 5.3.3 Comparison with Fresh Structured Interpretation

| Metric | Fresh Structured | Contract Reuse |
|---|---:|---:|
| Correct decisions | 24/30 | 27/30 |
| Accuracy | 80.0% | 90.0% |
| Total measured time | 249.70 s | 92.45 s |
| LLM calls | 60 | 20 |
| Stable cases | 10/10 | 10/10 |

Contract reuse reduced the number of LLM calls from 60 to 20, a reduction of approximately 66.7%.

The measured total time decreased from approximately 249.70 seconds to 92.45 seconds, a reduction of approximately 63.0%.

These timing measurements were collected in separate experimental runs. Runtime conditions and variation in model outputs may have affected the observed differences.

**Primary evidence:** `docs/contract_reuse_experiment_results.json`

## 5.4 Complete Workflow-Path Evaluation

The workflow-path experiment evaluated deterministic execution within the implemented three-node graph.

The two tested paths were:

- `Check Tests → Deploy Code`, for `tests_passed = True`.
- `Check Tests → Fix Code`, for `tests_passed = False`.

Each scenario was repeated 10 times.

The experiment used manually authored reference contracts, rather than LLM-generated contracts, to isolate deterministic execution behavior.

### 5.4.1 Path Correctness

| Metric | Result |
|---|---:|
| Workflow scenarios | 2 |
| Repetitions per scenario | 10 |
| Total workflow runs | 20 |
| Correct terminal paths | 20 |
| Path accuracy | 100.0% |

All 20 workflow runs reached their expected terminal paths.

This result establishes correct path execution for the two tested Boolean states under the reference-contract configuration.

It does not establish equivalent accuracy for contracts generated from natural language.

### 5.4.2 Workflow Repeatability

| Scenario | Expected Terminal Node | Repetitions | Stable Outcome |
|---|---|---:|---|
| Passing tests | Deploy Code | 10 | Yes |
| Failing tests | Fix Code | 10 | Yes |

Both scenarios produced stable paths across all 10 repetitions.

Each complete path contained one transition because the graph had no additional intermediate routing nodes.

The experiment therefore demonstrated repeatability within the implemented prototype, rather than across complex multi-transition workflows.

**Primary evidence:** `docs/workflow_path_trace_experiment_results.json`

## 5.5 Execution-Trace Persistence Results

The workflow-path experiment generated one execution trace for each routing decision.

The trace evaluation checked file existence, required trace fields, and agreement with selected routing values.

### 5.5.1 Trace Generation and Uniqueness

| Trace Metric | Result |
|---|---:|
| Workflow runs | 20 |
| Trace files generated | 20 |
| Unique trace identifiers | 20 |
| Unique trace filenames | 20 |
| Trace checks passed | 20/20 |

All 20 expected trace files were generated, and their identifiers and filenames were unique.

### 5.5.2 Independent Trace Verification

A separate verification procedure inspected the saved JSON results and trace files after the experiment completed.

The verification confirmed that all 20 trace files existed, could be parsed as JSON, contained unique identifiers, and recorded the expected routing outcomes.

The results support the inspectability and persistence of traces for the tested successful routing decisions.

The evaluation did not establish guaranteed trace persistence during unexpected exceptions, interrupted writes, or system failures.

**Primary evidence:** `docs/workflow_path_trace_experiment_results.json`  
**Trace artifacts:** `docs/workflow_path_trace_experiment_traces/`

## 5.6 Consolidated Results

| Evaluation Dimension | Observed Finding |
|---|---|
| Direct routing accuracy | 50.0% in both tested direct baselines |
| Fresh structured routing accuracy | 80.0% |
| Contract-reuse routing accuracy | 90.0% |
| Repeated routing stability | 10/10 stable cases in each routing method |
| Contract-reuse overhead | 20 LLM calls and 92.45 seconds total |
| Reference-contract path correctness | 20/20 correct paths |
| Reference-contract path repeatability | 2/2 stable scenarios |
| Execution-trace verification | 20/20 trace checks passed |

The evaluation produced three principal observations.

First, the structured routing method achieved higher observed accuracy than the direct-routing baselines on the tested natural-language cases, but required more computation when contracts were freshly generated for every decision.

Second, contract reuse reduced repeated model calls and measured total execution time while preserving deterministic routing behavior for the constructed contracts.

Third, when supplied with manually authored reference contracts, the prototype produced correct, repeatable terminal paths and persisted inspectable execution traces for all tested workflow runs.

The different accuracy figures must not be combined into a single overall accuracy estimate because they were produced under different experimental conditions.

## 5.7 Chapter Summary

The recorded experiments provide preliminary evidence that separating natural-language interpretation from deterministic contract evaluation can support consistent and inspectable routing decisions within the implemented prototype.

The results also show an important tradeoff: fresh structured interpretation introduced additional LLM overhead, while contract reuse reduced that overhead.

The controlled workflow-path experiment demonstrated correct and repeatable execution for the two supported terminal paths and verified trace persistence for the tested decisions.

Chapter 6 interprets these findings in relation to the research objectives and discuss threats to validity, including limited dataset diversity, prompt differences, semantic interpretation errors, runtime variability, and the restricted complexity of the workflow graph.
