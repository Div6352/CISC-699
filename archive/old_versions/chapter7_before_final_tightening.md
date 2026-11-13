# Chapter 7 ? Conclusion and Future Work

**CISC 699 Capstone II A2**
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution
**Status:** Revised conclusion based on recorded prototype experiments

## 7.1 Introduction

This chapter summarizes the completed research, answers the central research question, identifies the contributions and limitations of the implemented prototype, and presents directions for future work. The conclusions are restricted to the experimental conditions and evidence reported in Chapters 3–6.

## 7.2 Research Problem and Implemented Approach

Natural-language descriptions offer flexibility when specifying transitions in graph-based autonomous workflows. However, using a language model to select workflow destinations directly may make it difficult to distinguish interpretation errors from execution behavior.

This project investigated an architecture that separates these responsibilities. A locally hosted language model interprets natural-language edge conditions into structured semantic contracts containing a source node, destination node, condition field, operator, and expected value. Python components then validate and evaluate those contracts, enforce permitted graph transitions, and record routing decisions.

The evaluated implementation supports Boolean equality conditions involving `tests_passed` within a three-node workflow. It is a focused routing prototype rather than a complete autonomous software-development system.

## 7.3 Summary of Experimental Findings

The completed evaluation produced three principal findings.

First, the prompt-controlled routing comparison evaluated 10 distinct natural-language cases, with three repetitions per method. Fresh structured routing achieved **24 correct decisions out of 30 (80%)**, while both the original and prompt-controlled direct-routing baselines achieved **15 out of 30 (50%)**. All three methods produced stable outcomes across repetitions, demonstrating that repeated consistency does not necessarily establish correctness. Differences in prompts, output constraints, and execution procedures prevent a fully isolated causal interpretation of the accuracy difference.

Second, the contract-reuse experiment achieved **27 correct decisions out of 30 (90%)**. Constructing contracts once per case required **20 LLM calls** and approximately **92.45 seconds**, compared with **60 calls** and approximately **249.70 seconds** for fresh structured interpretation in the separate comparison run. These observations support the computational benefit of avoiding repeated interpretation, but the accuracy difference cannot be attributed to reuse itself.

Third, the workflow-path experiment used manually authored reference contracts and evaluated two terminal paths, each repeated 10 times. All **20 workflow runs** reached their expected destinations, and all **20 generated JSON traces** passed the selected readability, identifier-uniqueness, and routing-outcome checks. These results establish repeatable execution for the tested reference-contract scenarios, not for arbitrary LLM-generated contracts or larger workflows.

## 7.4 Answer to the Research Question

The research question was:

**How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?**

The results provide a qualified answer.

Structured semantic contracts separate probabilistic language interpretation from deterministic condition evaluation. Once a contract has been constructed, the same explicit condition can be evaluated repeatedly without invoking the language model for each routing decision. This supports consistent application of the represented condition and makes the basis for routing more inspectable.

The contract-reuse experiment demonstrated fewer model calls and lower observed execution time than fresh interpretation in the separate experimental run. The reference-contract workflow experiment demonstrated repeatable terminal paths and persisted execution records. The natural-language comparison showed higher observed accuracy for the structured approach under the tested conditions, without establishing that the architectural separation alone caused the difference.

Accordingly, the project supports the **feasibility of separating interpretation from deterministic execution and recording routing evidence**. It does not establish that structured contracts eliminate semantic errors or guarantee correct decisions across arbitrary workflows.

## 7.5 Research Contributions

The completed project makes five prototype-level contributions:

1. **Structured edge semantics:** A machine-readable contract representation for workflow transition conditions.
2. **Separated execution architecture:** Distinct components for language interpretation, contract validation, deterministic evaluation, and graph-transition enforcement.
3. **Comparative evaluation:** Recorded direct and structured routing outcomes across repeated natural-language cases.
4. **Contract-reuse evidence:** Measurements of model-call requirements and runtime when previously constructed contracts are reused.
5. **Workflow and trace verification:** Repeatable reference-contract routing outcomes supported by persisted JSON execution records.

Together, these contributions provide an implemented and evaluated foundation for studying natural-language transition semantics in graph-based workflows.

## 7.6 Limitations

The findings are limited by the small dataset of 10 natural-language cases, a single local model configuration, Boolean equality conditions, and a three-node graph with two permitted transitions.

The workflow-path experiment used manually authored contracts, and each complete path involved only one transition. The routing methods also differed in prompt and output design, while runtime measurements came from separate local executions.

Additionally, the trace checks covered selected properties of successful runs; they did not establish guaranteed persistence under exceptional failures. These limitations restrict generalization to larger, more complex autonomous software-development environments.

## 7.7 Future Work

Future research should extend the contract schema to additional variable types, comparison operators, and compound conditions. Larger datasets and more closely controlled model comparisons would help distinguish semantic interpretation quality from execution-architecture effects.

The workflow implementation should also be expanded to multiple sequential decisions and realistic software-development activities. Stronger semantic validation is needed to detect contracts that are structurally valid but incorrectly represent their original natural-language conditions.

Finally, trace mechanisms should be evaluated under failures and interruptions, with additional attention to integrity, recovery, and long-term audit requirements.

## 7.8 Final Conclusion

This research implemented and evaluated a prototype that separates natural-language edge interpretation from deterministic graph-based workflow routing.

Within the tested conditions, structured routing showed higher observed accuracy than the direct baselines, contract reuse reduced repeated model calls and measured runtime, and reference-contract workflow execution produced repeatable paths with inspectable traces.

The central qualification remains important: **deterministic execution can consistently apply an incorrectly interpreted contract**. The project's contribution is therefore not a guarantee of correct autonomous execution, but an explicit, testable boundary between language interpretation and workflow control.

This foundation supports further investigation of reliable and auditable routing in more complex autonomous software-development workflows.
