# Chapter 7 — Conclusion and Future Work

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary conclusion based on recorded prototype experiments

## 7.1 Introduction

This chapter concludes the research on structured natural-language edge semantics for deterministic execution in graph-based autonomous software-development workflows. It summarizes the implemented prototype, evaluates the findings in relation to the research question and objectives, identifies the principal contributions, and outlines directions for future work.

The conclusions are limited to the prototype, datasets, execution environment, and experimental conditions documented in Chapters 3–6.

## 7.2 Research Problem and Proposed Approach

Natural-language conditions offer a flexible way to describe transitions in graph-based workflows. However, directly interpreting those conditions during execution can introduce uncertainty into routing decisions.

The project investigated an alternative architecture in which natural-language edge conditions are interpreted into structured semantic contracts before deterministic routing occurs.

Each contract represents the information needed to evaluate a workflow transition, including its source node, destination node, condition field, comparison operator, and expected value.

The prototype separates the interpretation stage from the execution stage. The interpretation stage uses a locally hosted language model, while the execution stage uses Python-based contract validation, condition evaluation, routing, and graph-transition enforcement.

The implementation also provides structured execution traces to support inspection of routing decisions.

## 7.3 Summary of Experimental Findings

Three principal experiments informed the conclusions.

### 7.3.1 Natural-Language Routing Comparison

The prompt-controlled comparison evaluated 10 distinct natural-language cases, repeated three times per method.

Fresh structured routing produced 24 correct decisions out of 30, corresponding to 80% accuracy.

The original and prompt-controlled direct-routing baselines each produced 15 correct decisions out of 30, corresponding to 50% accuracy.

All three methods produced stable outcomes across the repeated cases. This demonstrated that repeated consistency did not necessarily imply correctness.

The structured method achieved higher observed accuracy in this experiment, but the comparison did not fully isolate the effect of structured representation from differences in prompts, output constraints, and execution procedures.

### 7.3.2 Contract Reuse and Computational Overhead

The contract-reuse experiment generated contracts once for each of 10 cases and reused them for three routing decisions per case.

The experiment recorded 27 correct decisions out of 30, corresponding to 90% accuracy.

It required 20 LLM calls and approximately 92.45 seconds of measured execution time, compared with 60 LLM calls and approximately 249.70 seconds in the fresh structured experiment.

The results demonstrate that the implemented reuse strategy reduced repeated LLM invocations and was associated with lower measured runtime.

However, the difference in observed accuracy cannot be attributed to contract reuse itself. Reusing an incorrect contract can reproduce an incorrect routing decision consistently.

### 7.3.3 Workflow Repeatability and Trace Persistence

The workflow-path experiment evaluated the two complete terminal paths supported by the implemented three-node graph.

Using manually authored reference contracts, all 20 workflow runs reached their expected terminal destinations.

Both scenarios produced stable paths across 10 repetitions.

The experiment generated 20 JSON execution traces. Subsequent verification confirmed that all 20 files were readable, their identifiers were unique, and their selected routing outcomes matched the expected results.

These findings demonstrate correct, repeatable execution and inspectable trace persistence for the tested reference-contract scenarios.

They do not establish the same performance for LLM-generated contracts or larger multi-transition workflows.

## 7.4 Answer to the Research Question

The central research question asked:

**How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?**

The prototype provides a partial, evidence-supported answer.

Structured semantic contracts make it possible to separate probabilistic natural-language interpretation from deterministic workflow evaluation. Once contracts are constructed, the routing component can apply their conditions consistently without requiring a new LLM interpretation for every decision.

The contract-reuse experiment demonstrated a reduction in repeated model calls and measured execution time.

The reference-contract workflow experiment demonstrated correct and repeatable routing within the implemented graph, together with persisted, inspectable execution traces.

The natural-language comparison also showed higher observed accuracy for the structured method than for the tested direct baselines, although the experimental design did not establish a fully controlled causal explanation for that difference.

The research therefore supports the feasibility of structured edge semantics as a mechanism for separating interpretation from deterministic execution and recording routing evidence.

It does not establish that the framework eliminates semantic errors, guarantees correct routing in all cases, or generalizes automatically to complex autonomous software-development systems.

## 7.5 Research Contributions

The project produced five principal contributions.

**Structured edge-contract representation.** The prototype implemented a machine-readable representation of natural-language workflow conditions using explicit fields, operators, values, and routing destinations.

**Separation of interpretation and execution.** The architecture distinguished LLM-based condition interpretation from deterministic contract evaluation and graph-transition enforcement.

**Comparative routing evidence.** The evaluation recorded direct-routing and structured-routing outcomes under repeated natural-language test cases, including an additional prompt-controlled direct baseline.

**Contract-reuse evaluation.** The experiments measured the overhead associated with fresh interpretation and demonstrated the reduction in LLM calls achieved by reusing constructed contracts.

**Workflow execution and trace evidence.** The prototype generated repeatable terminal paths under reference contracts and persisted JSON records of the tested routing decisions.

These contributions are prototype-level results and experimental artifacts rather than a complete production workflow framework.

## 7.6 Practical Implications

The findings suggest that structured semantic contracts may be useful when a workflow must evaluate the same natural-language condition repeatedly.

Separating interpretation from execution allows a system to avoid repeated model invocations for previously constructed conditions.

This design can also make the inputs to routing decisions more explicit and easier to inspect.

However, contract reuse creates a responsibility to assess the correctness of the initial interpretation. Deterministic evaluation can faithfully execute an incorrect contract.

Consequently, practical adoption would require stronger semantic validation, more extensive workflow testing, and reliable trace-management mechanisms.

## 7.7 Limitations of the Completed Work

The evaluation was limited to 10 distinct natural-language cases focused on a Boolean test condition.

The prototype used one locally hosted language-model configuration and a three-node graph with two permitted transitions.

The workflow-path experiment used manually authored contracts, and each complete path contained one transition.

The direct and structured comparison methods differed in their prompts, output constraints, and execution procedures.

Timing measurements were collected during separate local runs and may not generalize to other environments.

Execution-trace verification covered the tested successful decisions and selected trace properties. It did not establish guaranteed trace creation under all exceptional or system-failure conditions.

These limitations constrain the strength and generalizability of the conclusions.

## 7.8 Future Work

Future work should extend the semantic contract representation beyond a single Boolean condition to include additional variable types, comparison operators, and compound logical expressions.

A larger and more diverse natural-language dataset would support a stronger evaluation of interpretation accuracy and robustness.

Further comparisons should use more closely matched prompts, controlled execution conditions, and additional model configurations.

The workflow graph should be extended to include multiple sequential decisions, additional branches, and more realistic software-development operations.

Semantic validation should be strengthened to identify incorrectly interpreted but structurally valid contracts before execution.

Trace mechanisms could also be extended to cover exceptional outcomes, interrupted operations, integrity verification, and recovery.

Finally, integration with a more representative autonomous software-development workflow would help determine whether the observed prototype-level benefits persist in a broader operational setting.

## 7.9 Final Conclusion

This research implemented and evaluated a prototype for structured natural-language edge semantics and deterministic graph-based workflow routing.

The experiments demonstrated higher observed routing accuracy for the tested structured method than for the direct baselines, a reduction in model calls and measured runtime through contract reuse, and correct, repeatable terminal paths with inspectable traces under reference contracts.

The results also exposed important limitations. Structured contracts do not automatically ensure correct semantic interpretation, repeated outcomes can remain incorrect, and the tested workflow graph was small.

Within these boundaries, the project provides evidence that separating natural-language interpretation from deterministic execution is a feasible approach for improving the consistency and inspectability of routing decisions.

The work establishes a foundation for further research into more reliable, scalable, and auditable graph-based autonomous software-development workflows.
