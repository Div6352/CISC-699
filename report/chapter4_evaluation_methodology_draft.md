# Chapter 4 — Evaluation Methodology

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary chapter draft based on recorded prototype experiments. Formal evaluation protocol and instructor requirements remain subject to review.

## 4.1 Introduction

This chapter describes the experimental methodology used to evaluate the prototype for structured natural-language edge semantics and deterministic workflow routing. The evaluation examines three related research concerns: the correctness and consistency of routing decisions, the computational overhead of natural-language interpretation and contract reuse, and the repeatability and auditability of workflow execution.

The evaluation separates natural-language interpretation from deterministic contract execution so that these components can be examined independently. It also distinguishes experiments involving LLM-generated contracts from experiments using manually authored reference contracts.

## 4.2 Evaluation Environment and Prototype

The prototype was developed in Python and executed in a local Windows environment. Natural-language interpretation and direct routing experiments used a locally hosted Ollama model, `llama3.2:3b`, configured with temperature zero.

The prototype includes components for semantic contract representation, contract validation, deterministic condition evaluation, routing, workflow graph-transition enforcement, and execution-trace generation.

The implemented workflow graph contains three nodes: `Check Tests`, `Deploy Code`, and `Fix Code`. The graph permits two outgoing transitions from `Check Tests`. A successful test state leads to `Deploy Code`, while an unsuccessful test state leads to `Fix Code`.

The graph does not contain a `Start` node. The two destinations have no outgoing transitions and therefore act as terminal nodes in the evaluated prototype.

The evaluation was conducted locally. It did not execute external software-development agents or perform actual code deployment.

## 4.3 Evaluation Questions

The experimental work addresses the following questions:

1. How accurately do direct natural-language routing and structured contract-based routing select the expected destination?
2. How consistently do the methods repeat their decisions when evaluated multiple times on the same natural-language case?
3. What computational overhead is associated with fresh contract interpretation compared with reusing existing contracts?
4. Can the deterministic execution component produce correct and repeatable terminal paths when supplied with reference contracts?
5. Can the implementation persist inspectable execution traces containing the required routing evidence?

These questions operationalize the broader research objective of improving determinism, repeatability, and auditability in graph-based workflow execution.

## 4.4 Natural-Language Evaluation Dataset

The routing comparison used 10 natural-language test cases representing alternative phrasings of test-related workflow conditions. Each case was evaluated three times per method.

The cases included expected successful-test and unsuccessful-test outcomes. The expected routing destinations were established from the corresponding Boolean workflow states.

The dataset therefore contained 10 distinct cases and 30 repeated routing decisions per method. Repetitions of the same case were not treated as independent natural-language scenarios.

The test cases were limited to a single Boolean workflow variable, `tests_passed`, and the two outgoing transitions from `Check Tests`. Consequently, the dataset does not represent the full range of possible natural-language conditions or graph structures.

## 4.5 Routing Comparison Methods

Three routing approaches were evaluated.

### 4.5.1 Original Direct Natural-Language Routing

The original direct baseline supplied natural-language edge conditions and workflow state to the LLM and requested a routing destination. The model returned a target node or a no-match outcome, subject to the baseline implementation's output checks.

This method did not first construct reusable structured semantic contracts.

### 4.5.2 Prompt-Controlled Direct Routing

A second direct baseline used the same direct-routing architecture while adding explicit Boolean interpretation guidance concerning passing and failing tests.

This additional baseline was intended to reduce a potential prompt-guidance imbalance in the original comparison.

The direct and structured approaches nevertheless retained different output formats, constraints, and execution procedures. The comparison therefore does not isolate the architecture as the sole cause of observed performance differences.

### 4.5.3 Fresh Structured Contract Interpretation and Routing

The structured method used the LLM to interpret natural-language edge conditions into structured contracts. The contracts represented a workflow source, destination, condition field, comparison operator, and expected Boolean value.

The prototype then evaluated the structured conditions using deterministic Python logic.

In the fresh-interpretation experiment, the method interpreted two outgoing edge conditions for each repeated decision. This produced 60 LLM calls for 30 routing decisions.

## 4.6 Repeated Routing Protocol

The prompt-controlled comparison evaluated all 10 cases three times under each of the three routing methods.

The experiment recorded the selected routing outcome, correctness relative to the expected destination, consistency across repeated evaluations, elapsed time, and the number of LLM calls.

The evaluation distinguished decision stability from correctness. A method could return the same destination repeatedly and still be incorrect.

All three approaches were evaluated on the same case collection, but their prompts and execution architectures were not fully equivalent. The results were therefore interpreted as observed prototype behavior rather than a controlled causal estimate of architectural effects.

## 4.7 Contract-Reuse Protocol

A separate experiment examined the overhead of constructing contracts once and reusing them for multiple deterministic routing decisions.

For each of the 10 natural-language cases, the prototype generated two outgoing-edge contracts once. It then reused those contracts for three routing decisions involving the same workflow state.

The experiment recorded contract construction time separately from deterministic routing time. Total measured time included both components.

This protocol required 20 LLM calls across 30 routing decisions, compared with 60 calls in the fresh structured experiment.

The reuse experiment measured routing accuracy and stability as well as execution time. Because contract generation occurred in a separate run, differences in observed accuracy were not attributed causally to reuse.

The repeated routing inputs within each case were identical. Consequently, stable decisions were expected from the deterministic evaluator and did not independently establish semantic correctness.

## 4.8 Workflow-Path and Execution-Trace Protocol

A separate experiment evaluated complete paths within the implemented three-node graph.

Two workflow scenarios were defined:

- `tests_passed = True`, with expected path `Check Tests → Deploy Code`.
- `tests_passed = False`, with expected path `Check Tests → Fix Code`.

Each scenario was repeated 10 times, producing 20 workflow runs.

This experiment used manually authored reference contracts rather than LLM-generated contracts. The purpose was to isolate deterministic routing, graph-transition enforcement, path repeatability, and execution-trace persistence from natural-language interpretation errors.

Each complete path contained one graph transition.

The experiment invoked the traced routing component, which evaluated the contracts, checked graph-transition permission, and saved a JSON execution trace.

For each run, the experiment recorded the observed path, completion status, correctness, trace identifier, trace filename, and trace validation results.

## 4.9 Evaluation Metrics

### 4.9.1 Routing Accuracy

Routing accuracy was calculated as the number of correct routing decisions divided by the total number of evaluated routing decisions.

A correct decision required the routing outcome to match the expected destination.

### 4.9.2 Decision Stability

Decision stability was measured at the case level. A case was considered stable when its repeated evaluations produced the same routing status and destination.

Stability was reported separately from accuracy because consistent incorrect decisions were possible.

### 4.9.3 Execution Time

Elapsed time was measured during experiment execution.

The comparison experiments reported total elapsed time and average time per routing decision.

The contract-reuse experiment separately measured contract construction time and deterministic routing time.

Timing comparisons across different experiment runs were interpreted cautiously because local runtime conditions could vary.

### 4.9.4 LLM Call Count

The number of model invocations was recorded to compare the computational demands of direct routing, fresh contract construction, and contract reuse.

For the reuse experiment, the deterministic routing phase required no additional LLM calls after the contracts had been constructed. This did not mean that the overall experiment had zero model cost.

### 4.9.5 Workflow-Path Accuracy

Workflow-path accuracy was calculated as the number of completed runs reaching the expected terminal path divided by the total number of workflow runs.

The metric applied to the actual three-node graph and did not measure longer multi-transition workflows.

### 4.9.6 Trace Persistence and Integrity Checks

Trace evaluation examined whether the expected JSON files existed, could be read, contained required fields, and agreed with selected routing outcomes.

The experiment also checked trace identifier and filename uniqueness.

These checks provided evidence of persistence and inspectability for the tested successful routing decisions. They did not prove that traces would always be saved during unexpected exceptions or system failures.

## 4.10 Data Collection and Evidence Preservation

Experimental scripts saved machine-readable results in JSON format under the project's `docs` directory.

The principal evidence artifacts were:

- `docs/prompt_controlled_comparison_results.json`
- `docs/contract_reuse_experiment_results.json`
- `docs/workflow_path_trace_experiment_results.json`
- `docs/workflow_path_trace_experiment_traces/`

The recorded results were subsequently inspected using separate verification commands.

The consolidated research evidence document was cross-checked against the saved JSON summaries for key accuracy, call-count, and trace-verification values.

Existing result files were retained rather than overwritten during later experiments.

## 4.11 Methodological Limitations

Several limitations affect the interpretation and generalizability of the evaluation.

First, the natural-language dataset consisted of 10 distinct cases focused on a single Boolean condition. Repeated decisions increased the number of observations but did not increase the number of independent natural-language scenarios.

Second, the direct and structured methods differed in output constraints, prompt formulation, and number of LLM calls. Even with additional guidance in the prompt-controlled direct baseline, the experiment did not fully isolate the causal effect of structured representation.

Third, the experiments were executed locally using one model configuration. The evaluation did not establish generalization to other LLMs, hardware configurations, or deployment environments.

Fourth, the contract-reuse experiment repeated identical workflow states within each case. Reuse reduced repeated model interpretation but could also preserve an initially incorrect semantic contract.

Fifth, the workflow-path experiment used manually authored reference contracts and a graph with one transition per complete path. It therefore measured deterministic execution under controlled conditions rather than end-to-end natural-language agent workflow performance.

Finally, trace verification covered recorded successful decisions and selected trace fields. It did not comprehensively test exceptional failures, interrupted writes, or recovery behavior.

## 4.12 Chapter Summary

The evaluation methodology combined repeated natural-language routing comparisons, a contract-reuse experiment, and a controlled workflow-path and trace-persistence experiment.

This separation made it possible to examine semantic interpretation accuracy, repeated decision behavior, computational overhead, deterministic routing, and trace inspectability as distinct properties of the prototype.

Chapter 5 presents the observed results from these experiments. Chapter 6 discusses their implications, limitations, and threats to validity.
