# Chapter 6 — Discussion, Limitations, and Threats to Validity

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary discussion based on recorded prototype experiments

## 6.1 Introduction

This chapter interprets the experimental findings presented in Chapter 5 in relation to the research objective: investigating whether structured natural-language edge semantics can improve determinism, repeatability, and auditability in graph-based autonomous software-development workflows.

The discussion focuses on the relationship between semantic interpretation and deterministic execution, the tradeoff between routing accuracy and computational overhead, the benefits and risks of contract reuse, and the scope of the workflow-path and execution-trace findings.

The experiments provide evidence about a limited local prototype rather than a production autonomous software-development system.

## 6.2 Interpretation of Routing Accuracy

The prompt-controlled comparison showed that fresh structured contract routing achieved 24 correct decisions out of 30, corresponding to 80% accuracy. Both the original and prompt-controlled direct-routing baselines achieved 15 correct decisions out of 30, corresponding to 50% accuracy.

The observed 30-percentage-point difference suggests that explicitly representing workflow conditions as structured contracts may be useful for separating condition interpretation from routing execution.

However, the experiment did not fully isolate the structured representation as the cause of the difference. The methods differed in their output requirements, validation constraints, number of model calls, and execution procedures.

Consequently, the findings support a promising prototype-level result rather than a general causal claim that structured routing is inherently more accurate than direct natural-language routing.

## 6.3 Determinism, Repeatability, and Correctness

All three methods in the prompt-controlled comparison produced stable decisions across repeated evaluations of the 10 test cases.

Nevertheless, the two direct-routing methods achieved only 50% accuracy.

This distinction is important: a system can make the same decision repeatedly without making the correct decision.

Deterministic execution therefore addresses the consistency of applying an interpreted rule, but it does not guarantee that the rule was interpreted correctly.

The prototype's separation of semantic interpretation from deterministic evaluation makes this distinction explicit. Once a contract has been constructed, its condition can be evaluated without requesting a new interpretation from the LLM.

This reduces one source of variation during repeated execution while leaving the correctness of the initial interpretation as a separate concern.

The recorded failures for cases IND06 and IND10 illustrate this limitation. Both conditions described unsuccessful tests and required the Boolean value `tests_passed = False`, but the language model generated `tests_passed = True` for the corresponding repair edge in all three repetitions of each case. These contracts passed structural validation despite their incorrect meaning. Because the deployment edge also required `tests_passed = True`, neither outgoing condition matched the failing-test workflow state, and the deterministic router returned `NO_MATCH` in all six decisions. The observed failure therefore arose during semantic interpretation, while deterministic evaluation consistently applied the generated contracts. This demonstrates why structural contract validity, routing repeatability, and semantic correctness must be assessed separately.

## 6.4 Interpretation of Contract-Reuse Findings

The contract-reuse experiment achieved 27 correct routing decisions out of 30, corresponding to 90% accuracy, with stable outcomes across all 10 cases.

It required 20 LLM calls and approximately 92.45 seconds of total measured time.

By comparison, the fresh structured experiment required 60 LLM calls and approximately 249.70 seconds.

The reduction in model calls is a direct consequence of the experimental protocol: contracts were constructed once per case instead of being reconstructed for every routing decision.

The measured runtime was approximately 63% lower in the reuse experiment.

However, the timing measurements were collected in separate experimental runs. Runtime conditions and model behavior may have contributed to the observed difference.

Furthermore, the higher observed accuracy in the reuse experiment does not demonstrate that reuse improves semantic interpretation. An incorrectly generated contract can be reused just as consistently as a correct one.

The findings therefore support contract reuse as a way to reduce repeated interpretation overhead, while emphasizing the need to validate contract meaning before reuse.

## 6.5 Workflow-Path Repeatability

The workflow-path experiment evaluated the two complete paths supported by the implemented three-node graph.

With manually authored reference contracts, all 20 workflow runs reached their expected terminal destinations.

Both scenarios produced stable outcomes across 10 repetitions.

These results demonstrate repeatable execution for the tested Boolean workflow states when semantic interpretation errors are excluded.

The finding is intentionally narrow. Each complete path contained one graph transition, and the experiment did not evaluate larger graphs, cycles, branching sequences across multiple intermediate nodes, or interactions with external agents.

Therefore, the results establish correct execution within the evaluated prototype rather than general workflow correctness.

## 6.6 Auditability and Execution-Trace Evidence

The traced router generated 20 JSON execution traces during the workflow-path experiment.

All 20 files were independently verified as readable, with unique trace identifiers and expected routing outcomes.

The traces included information such as the workflow state, evaluated contracts, routing status, selected destination, validation results, and decision explanation.

This evidence supports the claim that the prototype can produce inspectable records of its tested routing decisions.

However, auditability is broader than generating trace files. A comprehensive audit system would also require stronger guarantees regarding exceptional failures, trace completeness, integrity protection, retention, and recovery.

The current implementation uses temporary-file-based replacement with file synchronization, which reduces the risk of partial trace files during normal writing. It does not guarantee trace creation or persistence under every possible failure condition.

## 6.7 Threats to Internal Validity

Internal validity concerns whether the observed differences can be attributed to the experimental methods rather than other factors.

Several threats were identified.

First, the direct and structured routing approaches differed in their prompts, output constraints, and execution procedures. Adding Boolean interpretation guidance to the controlled direct baseline reduced one source of imbalance but did not make the methods fully equivalent.

Second, the structured method made more LLM calls than the direct methods during fresh interpretation. This difference affected computational overhead and may also have influenced the observed routing outcomes.

Third, the experiments were conducted sequentially rather than through a randomized or counterbalanced execution schedule. Model-serving conditions, caching, and background system activity could have affected timing.

Fourth, the contract-reuse experiment was conducted separately from the fresh structured experiment. Differences in generated contracts could affect observed accuracy independently of the reuse strategy.

These limitations prevent strong causal conclusions about the architecture's effect on accuracy or runtime.

## 6.8 Threats to Construct Validity

Construct validity concerns whether the selected measurements adequately represent the intended research concepts.

Routing accuracy measured agreement with expected terminal destinations, but did not independently measure all aspects of natural-language understanding.

Decision stability measured repeated outcomes, but stable outcomes could be incorrect.

Workflow-path accuracy measured successful execution within a small graph, rather than correctness across complex autonomous workflows.

Trace checks measured the existence, readability, uniqueness, and selected contents of saved records. They did not measure every aspect of auditability, including tamper resistance or recovery after failure.

The evaluation therefore used operational metrics that captured selected aspects of determinism, repeatability, and auditability rather than complete implementations of those broader concepts.

## 6.9 Threats to External Validity

External validity concerns whether the findings generalize beyond the tested prototype.

The natural-language evaluation contained 10 distinct cases centered on the Boolean variable `tests_passed`.

The implementation used one local LLM configuration and one small workflow graph.

The experiments did not include more complex condition types, larger graphs, additional language models, diverse software-development tasks, or production agent interactions.

As a result, the findings should not be generalized to all graph-based autonomous software-development workflows without further testing.

## 6.10 Reliability and Reproducibility Considerations

The experiments preserved machine-readable JSON outputs and, for the workflow-path evaluation, individual execution-trace files.

The principal results were independently checked against saved summaries, and the workflow traces were inspected after generation.

These practices improve the inspectability of the reported findings.

Nevertheless, reproducing the exact timing and model outputs may depend on the local runtime environment, model version, hardware conditions, and inference behavior.

A final reproducibility package should document the execution environment, scripts, datasets, model configuration, experimental commands, and expected output structure.

The current evidence should be retained without modification while the final evaluation protocol and reporting requirements are reviewed.

## 6.11 Implications for the Research Objectives

The implementation and experiments address the research objectives at the prototype level. The routing comparisons examine natural-language interpretation; the contract schema and evaluator demonstrate the separation of interpretation from execution; and the reuse experiment measures the cost of repeated interpretation.

The reference-contract workflow experiment provides evidence of repeatable routing for the two supported Boolean states, while the trace checks demonstrate the availability of inspectable execution records.

Together, these findings establish feasibility within the evaluated scope, not a production-ready autonomous software-development framework.

## 6.12 Future Evaluation Priorities

Further evaluation should examine a larger and more diverse natural-language dataset, more complex condition representations, and graphs containing multiple sequential routing decisions.

Additional experiments should compare direct and structured routing using more closely matched prompts and execution constraints.

Contract validation could be extended to include semantic checks, graph membership, and stronger safeguards against incorrect but structurally valid interpretations.

Trace evaluation could be expanded to include exceptional routing outcomes, interrupted writes, integrity checks, and recovery behavior.

Further research could also examine additional LLM configurations and more representative software-development workflows.

## 6.13 Chapter Summary

The findings support the feasibility of separating probabilistic natural-language interpretation from deterministic workflow routing. Structured routing achieved higher observed accuracy than the tested direct baselines, although the experimental differences do not establish a causal advantage of the architecture alone.

Contract reuse reduced repeated model calls and observed runtime. Reference-contract execution produced repeatable terminal paths and inspectable traces.

Small datasets, unequal method configurations, limited graph complexity, and incomplete failure testing restrict generalization. Chapter 7 summarizes the contributions, answers the research question, and identifies future work.

