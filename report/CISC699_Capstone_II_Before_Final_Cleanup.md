# HARRISBURG UNIVERSITY OF SCIENCE AND TECHNOLOGY

## Natural-Language Edge Semantics and Deterministic Agent Execution

**Capstone II Research Report**

**Submitted by:** Divyam Nikunjkumar Brahmbhatt

**Degree Program:** Master of Science in Computer Science

**Concentration:** Software Engineering and Testing

**Course:** CISC 699 ? Applied Project in Computer and Information Science

**Lead Instructor:** Abdelhaq Ejnioui

**Submission Date:** February 12, 2027

---

# Table of Contents

- **Abstract**
- **AI-Use Disclosure and Contribution Statement**
- **Chapter 1 — Introduction**
  - 1.1 Background and Research Context
  - 1.2 Problem Statement
  - 1.3 Research Motivation
  - 1.4 Research Question
  - 1.5 Research Objectives
  - 1.6 Proposed Solution and Implemented Approach
  - 1.7 Scope of the Completed Research
  - 1.8 Research Method Overview
  - 1.9 Summary of Principal Findings
  - 1.10 Significance of the Research
  - 1.11 Organization of the Final Report
  - 1.12 Chapter Summary
- **Chapter 2 — Literature Review**
  - 2.1 Introduction
  - 2.2 Literature Search Strategy
  - 2.3 Autonomous Software-Engineering Agents
  - 2.4 Graph-Based Workflow Orchestration
  - 2.5 Natural-Language Reasoning and Decision Making
  - 2.6 Workflow Reliability, Observability, and Explainability
  - 2.7 Natural-Language Edge Semantics and Deterministic Agent Execution
  - 2.8 Relevant Methods, Frameworks, and Evaluation Foundations
  - 2.9 Comparison of Existing Approaches
  - 2.10 What Existing Literature Already Addresses
  - 2.11 Chapter Summary
  - References
- **Chapter 3 — System Design and Implementation**
  - 3.1 Introduction
  - 3.2 System Requirements and Design Objectives
  - 3.3 Implemented System Architecture
  - 3.4 Structured Semantic Contract Representation
  - 3.5 Contract Validation
  - 3.6 Deterministic Contract Evaluation
  - 3.7 Contract-Based Routing
  - 3.8 Workflow Graph and Transition Enforcement
  - 3.9 Natural-Language Interpretation with a Local Language Model
  - 3.10 Direct Natural-Language Routing Baselines
  - 3.11 Contract Reuse
  - 3.12 Execution-Trace Generation and Persistence
  - 3.13 Prototype Modules and Responsibilities
  - 3.14 Implementation Scope and Boundaries
  - 3.15 Chapter Summary
- **Chapter 4 — Evaluation Methodology**
  - 4.1 Introduction
  - 4.2 Evaluation Environment and Prototype
  - 4.3 Evaluation Questions
  - 4.4 Natural-Language Evaluation Dataset
  - 4.5 Routing Comparison Methods
  - 4.6 Repeated Routing Protocol
  - 4.7 Contract-Reuse Protocol
  - 4.8 Workflow-Path and Execution-Trace Protocol
  - 4.9 Evaluation Metrics
  - 4.10 Data Collection and Evidence Preservation
  - 4.11 Methodological Limitations
  - 4.12 Chapter Summary
- **Chapter 5 — Experimental Results**
  - 5.1 Introduction
  - 5.2 Prompt-Controlled Routing Comparison
  - 5.3 Contract-Reuse Experiment
  - 5.4 Complete Workflow-Path Evaluation
  - 5.5 Execution-Trace Persistence Results
  - 5.6 Consolidated Results
  - 5.7 Chapter Summary
- **Chapter 6 — Discussion, Limitations, and Threats to Validity**
  - 6.1 Introduction
  - 6.2 Interpretation of Routing Accuracy
  - 6.3 Determinism, Repeatability, and Correctness
  - 6.4 Interpretation of Contract-Reuse Findings
  - 6.5 Workflow-Path Repeatability
  - 6.6 Auditability and Execution-Trace Evidence
  - 6.7 Threats to Internal Validity
  - 6.8 Threats to Construct Validity
  - 6.9 Threats to External Validity
  - 6.10 Reliability and Reproducibility Considerations
  - 6.11 Implications for the Research Objectives
  - 6.12 Future Evaluation Priorities
  - 6.13 Chapter Summary
- **Chapter 7 — Conclusion and Future Work**
  - 7.1 Introduction
  - 7.2 Research Problem and Implemented Approach
  - 7.3 Summary of Experimental Findings
  - 7.4 Answer to the Research Question
  - 7.5 Research Contributions
  - 7.6 Limitations
  - 7.7 Future Work
  - 7.8 Final Conclusion

---

# Abstract

Natural-language conditions are increasingly used to control transitions in graph-based autonomous software-development workflows. However, direct interpretation of these conditions by language models can produce inconsistent or incorrect routing decisions. This study investigates whether structured semantic contracts can support more deterministic, repeatable, and auditable workflow routing.

A Python research prototype was implemented to separate language-model interpretation from deterministic condition evaluation. Using a local Ollama language model, the prototype converts natural-language edge descriptions into structured Boolean contracts. Validation, routing, graph-transition checking, and JSON execution tracing are handled by separate components.

The evaluation used ten independent natural-language cases, each repeated three times. In the prompt-controlled comparison, original direct routing and prompt-controlled direct routing each achieved 15 correct decisions out of 30 (50%), while fresh structured-contract routing achieved 24 out of 30 (80%). All three methods produced stable outcomes across all ten cases, demonstrating that repeatability alone does not establish correctness. Fresh structured routing required 249.70 seconds and 60 language-model calls, compared with 112.17 seconds and 30 calls for prompt-controlled direct routing. In a separate contract-reuse experiment, structured routing achieved 27 correct decisions out of 30 (90%) using 20 contract-construction calls. A reference-contract workflow experiment produced 20 correct tested paths and 20 validated execution traces.

These findings demonstrate the feasibility of separating semantic interpretation from deterministic routing. However, structurally valid contracts can still encode incorrect meanings, and the small Boolean benchmark, differing prompts, and separate experimental runs limit causal interpretation and generalizability.

---

# AI-Use Disclosure and Contribution Statement

## AI Tools Used

Two artificial intelligence tools were used during this Capstone II research project: ChatGPT and a locally executed Ollama language model (`llama3.2:3b`). No other AI tools were reported as used.

## ChatGPT Assistance

ChatGPT was used as an assistance tool during research planning, prototype development, debugging, experimental review, and report preparation. Its contributions included explaining implementation concepts, suggesting Python and PowerShell commands, assisting with code and documentation drafts, organizing experimental evidence, proposing verification procedures, and helping revise report language for clarity and consistency.

ChatGPT also assisted in preparing the research report's chapter drafts, abstract, reproducibility instructions, and evidence-audit procedures. AI-generated text and suggestions were treated as material requiring review rather than as independently verified research findings.

## Ollama Use in the Research Prototype

The local Ollama model (`llama3.2:3b`) was used as part of the experimental system. It interpreted natural-language workflow edge conditions into structured Boolean contracts and served as the language model for direct natural-language routing baselines.

Ollama's outputs were experimental observations, not authoritative answers. Their correctness was evaluated against predefined expected conditions and routing destinations. The model's occasional semantic interpretation errors are included in the reported findings.

## Student Contribution and Responsibility

The student was responsible for conducting the project, running the local experiments, retaining the resulting evidence, reviewing implementation behavior, checking reported numerical results, and making decisions about the final research claims and submission.

AI assistance does not transfer authorship or academic responsibility to the tools. The student remains responsible for verifying source references, technical descriptions, calculations, institutional requirements, and the final submitted report.

## Verification Status

The student executed local verification scripts to check recorded experimental summaries, expected and observed routing decisions, execution-trace records, and selected numerical claims in the report. ChatGPT assisted in preparing and reviewing these checks but did not independently execute them on the student's computer. These checks do not establish that every citation, methodological statement, or submission requirement has been independently verified. Any remaining verification must be completed before final submission.

---

# Chapter 1 — Introduction

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary introduction draft

## 1.1 Background and Research Context

Autonomous software-development systems increasingly rely on structured workflows to organize tasks, determine execution order, and coordinate decisions. Graph-based workflow representations are useful because they express computational activities as nodes and transitions as edges.

In these systems, an edge may represent a condition that determines which activity should execute next. Natural-language edge descriptions provide an accessible way to express such conditions. For example, a workflow designer might describe a transition using a statement such as “Proceed to deployment when all tests pass.”

Although this representation is understandable to human users, a software system must convert the description into an executable decision. When a language model interprets a natural-language condition directly during routing, the interpretation process may introduce errors or inconsistencies.

This research investigates a structured representation for natural-language edge conditions that separates semantic interpretation from deterministic workflow execution.

## 1.2 Problem Statement

Natural-language workflow conditions are flexible but may be ambiguous, incomplete, or interpreted incorrectly by a language model.

Direct language-model routing can also combine condition interpretation and destination selection into a single operation, making it more difficult to distinguish an interpretation error from an execution error.

Repeatedly interpreting the same edge description may introduce additional model calls and computational overhead.

Furthermore, without structured decision records, it may be difficult to inspect which condition was evaluated, which workflow state was used, and why a particular destination was selected.

The central problem addressed in this project is how to represent natural-language workflow-edge conditions in a form that supports consistent evaluation, repeatable routing, and inspectable execution evidence.

## 1.3 Research Motivation

The motivation for this work is to improve the reliability and inspectability of routing decisions in graph-based autonomous software-development workflows.

A workflow system should be able to distinguish between understanding a condition and applying that condition to the current state.

For example, interpreting “when all tests pass” as a Boolean requirement is a semantic task. Checking whether the workflow variable `tests_passed` equals `true` is a deterministic computational task.

Separating these responsibilities may make routing behavior easier to analyze and reduce the need for repeated language-model interpretation.

However, a structured representation does not automatically guarantee that the initial interpretation is correct. This research therefore evaluates both the potential benefits and the limitations of the approach.

## 1.4 Research Question

The research is guided by the following question, retained from the Capstone I proposal:

**How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?**

The completed prototype and experiments provide a bounded investigation of this question through Boolean edge conditions, deterministic routing, contract reuse, and execution-trace generation.

## 1.5 Research Objectives

The project follows five objectives derived from the original proposal.

1. **Examine natural-language edge interpretation.** Investigate how natural-language workflow conditions are interpreted and identify errors that may affect routing decisions.
2. **Develop a structured representation.** Represent workflow-edge conditions through explicit variables, operators, expected values, and routing destinations.
3. **Implement a working prototype.** Separate language-model interpretation from deterministic contract evaluation and graph-transition enforcement.
4. **Compare routing approaches.** Evaluate direct natural-language routing and structured contract-based routing under repeated test scenarios.
5. **Assess execution properties.** Measure routing correctness, repeated-decision consistency, workflow-path repeatability, trace completeness, validation behavior, and computational overhead within the implemented scope.

These objectives provide the basis for the evaluation methodology and results presented in later chapters.

## 1.6 Proposed Solution and Implemented Approach

The project investigates a structured natural-language edge semantics framework.

In the implemented approach, a locally hosted language model interprets a natural-language edge condition into a machine-readable semantic contract.

The contract contains information such as the source node, destination node, condition field, comparison operator, and expected value.

A deterministic evaluation component then compares the contract against the current workflow state.

A graph-enforcement layer checks whether the selected transition is permitted by the implemented workflow graph.

A trace mechanism records selected routing operations in JSON format for later inspection.

The implementation also includes direct language-model routing baselines, allowing the structured approach to be compared with destination selection performed directly by a language model.

## 1.7 Scope of the Completed Research

The completed prototype supports a deliberately limited workflow.

The implemented graph contains three nodes: `Check Tests`, `Deploy Code`, and `Fix Code`.

Two transitions originate from `Check Tests`, corresponding to successful and failed test conditions.

The structured condition language supports the Boolean workflow variable `tests_passed` with the comparison operator `equals`.

The natural-language evaluation includes 10 distinct test cases, each repeated three times in the principal routing comparisons.

A separate workflow-path experiment evaluates two terminal paths, each repeated 10 times using manually authored reference contracts.

The prototype does not implement a full autonomous software-development lifecycle, multi-agent coordination, or complex multi-step execution paths.

These boundaries define the scope of the findings and prevent unsupported generalization.

## 1.8 Research Method Overview

The research uses a prototype-based experimental approach.

First, the project implements structured semantic contracts, contract validation, deterministic condition evaluation, routing logic, graph-transition enforcement, and execution-trace persistence.

Second, it implements direct natural-language routing baselines using the same local language-model family.

Third, it evaluates routing outcomes using a dataset of natural-language test-condition descriptions with expected destinations.

Fourth, it measures the effect of generating contracts once and reusing them across repeated routing decisions.

Finally, it evaluates workflow-path correctness and trace persistence using manually authored reference contracts.

The experiments record routing accuracy, repeated-decision stability, model-call counts, execution time, workflow-path outcomes, and selected trace properties.

## 1.9 Summary of Principal Findings

The prompt-controlled routing comparison recorded 24 correct decisions out of 30 for fresh structured routing, compared with 15 correct decisions out of 30 for each direct-routing baseline.

All three methods produced stable outcomes across the repeated test cases, demonstrating that repeatability alone does not establish correctness.

The contract-reuse experiment recorded 27 correct decisions out of 30 while reducing the number of model calls from 60 in the fresh structured experiment to 20.

The workflow-path experiment recorded 20 correct terminal paths out of 20 using manually authored reference contracts.

The same experiment generated 20 JSON trace files that passed the selected verification checks.

These findings support the feasibility of separating natural-language interpretation from deterministic execution in the tested prototype.

They do not establish that structured routing eliminates semantic errors or guarantees correctness in larger autonomous workflows.

## 1.10 Significance of the Research

This research contributes a practical demonstration of how structured semantic contracts can be used between natural-language interpretation and graph-based workflow execution.

The separation makes the condition being evaluated explicit and allows previously constructed contracts to be reused.

The evaluation also illustrates an important limitation: a deterministic system can repeatedly execute an incorrectly interpreted contract.

By measuring routing accuracy, consistency, overhead, path correctness, and trace persistence separately, the project provides a more detailed understanding of the benefits and risks of the implemented approach.

The results may inform future research on more reliable and auditable autonomous workflow systems, subject to validation in broader settings.

## 1.11 Organization of the Final Report

The remainder of this report is organized into six chapters.

**Chapter 2 — Literature Review** examines the relevant research foundations and identifies the problem addressed by the project.

**Chapter 3 — System Design and Implementation** describes the completed prototype architecture, components, and implementation boundaries.

**Chapter 4 — Evaluation Methodology** explains the experimental datasets, comparison methods, procedures, and metrics.

**Chapter 5 — Experimental Results** reports the observed routing, contract-reuse, workflow-path, and trace-persistence findings.

**Chapter 6 — Discussion, Limitations, and Threats to Validity** interprets the findings and identifies methodological and implementation limitations.

**Chapter 7 — Conclusion and Future Work** summarizes the research contributions, answers the research question within the available evidence, and identifies future research directions.

## 1.12 Chapter Summary

This chapter introduced the problem of interpreting natural-language conditions in graph-based autonomous software-development workflows.

It presented the research question, objectives, motivation, implemented approach, evaluation scope, and principal findings.

The project investigates whether representing natural-language edge conditions as structured contracts can separate probabilistic interpretation from deterministic execution while supporting repeatable routing and inspectable records.

The following chapter reviews the research foundations that motivate this approach.

---

# Chapter 2 — Literature Review

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary literature-review draft based on the Capstone I proposal

## 2.1 Introduction

Autonomous software-engineering systems have expanded the role of artificial intelligence from assisting developers with isolated tasks toward participating in executable software-development processes. Language-model-based agents can interact with repositories, development tools, and execution environments while using observations to inform subsequent actions.

Research on SWE-agent and OpenHands provides examples of this development (Yang et al., 2024; Wang et al., 2024). Related work on reasoning, agent coordination, and workflow orchestration provides foundations for organizing such actions into structured processes.

However, the ability to execute actions does not automatically establish how natural-language workflow conditions should be represented, validated, and evaluated.

This chapter reviews the research foundations relevant to structured natural-language edge semantics and identifies the specific problem addressed by the implemented prototype.

## 2.2 Literature Search Strategy

The literature review was organized around the research question:

**How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?**

The original Capstone I review organized relevant literature into several connected areas: autonomous software-engineering agents, graph-based workflow orchestration, language-model reasoning and decision-making, reliability and explainability, structured representations, and evaluation methods.

The review includes peer-reviewed research, scholarly books, technical papers, framework documentation, and industry research material.

These source categories serve different purposes. Research papers provide evidence about particular methods or systems, books provide broader conceptual foundations, and framework documentation describes implementation capabilities.

The original proposal also included a literature-search appendix. The final report should retain only search details that can be verified from that appendix; database coverage, search dates, and screening counts should not be invented.

## 2.3 Autonomous Software-Engineering Agents

Autonomous software-engineering agents extend language-model use beyond generating code suggestions. They may interact with repositories, inspect files, execute commands, run tests, and use execution feedback to guide subsequent actions.

SWE-agent investigates the role of agent-computer interfaces in enabling language-model agents to perform software-engineering tasks (Yang et al., 2024). Its relevance to this research lies in the connection between model-generated decisions and executable development operations.

OpenHands provides another example of a platform intended to support generalist AI software-development agents (Wang et al., 2024). It contributes to the broader context of agents interacting with software-development environments.

The StrongDM software-factory material represents an industry-oriented perspective on increasingly automated software-production processes (StrongDM Team, 2026).

These sources motivate the need to consider execution control as a distinct system concern. Although an agent may be capable of performing development operations, its ability to act does not by itself define the precise meaning of a natural-language condition governing the next workflow transition.

The present research therefore focuses on routing semantics rather than attempting to reproduce the full capabilities of an autonomous coding agent.

## 2.4 Graph-Based Workflow Orchestration

Graph-based workflow representations organize execution around nodes and transitions.

A node may represent an activity or execution state, while an edge represents a possible transition to another node. Conditional transitions allow workflow state to influence which destination is selected.

Petri-net research provides a formal foundation for analyzing states, transitions, and properties of concurrent systems (Murata, 1989). Although the implemented prototype is not a Petri-net system, this literature demonstrates the longstanding importance of explicit transition semantics.

LangGraph documentation provides a contemporary framework reference for organizing stateful, graph-based agent workflows (LangChain, Inc., n.d.).

AutoGen investigates multi-agent applications organized through agent conversations and interactions (Wu et al., 2024).

These approaches demonstrate that orchestration and coordination are important parts of agent-system design.

However, the existence of graph transitions or agent interactions does not resolve every question about how a natural-language edge description should become a precise executable condition.

The research gap addressed in this project concerns that interpretation-to-execution boundary.

## 2.5 Natural-Language Reasoning and Decision Making

Language models can participate in workflows by generating reasoning, choosing actions, and responding to observations.

ReAct explores the combination of reasoning and acting in language-model-based systems (Yao et al., 2023). Its relevance lies in demonstrating how language-model outputs can influence subsequent executable actions.

Reflexion examines the use of verbal feedback to support improvement in language-agent behavior (Shinn et al., 2023).

Russell and Norvig (2021) provide broader artificial-intelligence foundations for reasoning, agents, and decision-making.

These sources help explain why natural-language interpretation is useful in autonomous systems. Language models can process flexible instructions that would be difficult to express through fixed rules alone.

Nevertheless, generating a plausible interpretation is different from guaranteeing that the interpretation accurately captures the intended condition.

For workflow routing, an incorrectly interpreted condition may produce a repeatable but incorrect transition.

The present prototype addresses this distinction by representing interpreted conditions as structured contracts before deterministic evaluation.

## 2.6 Workflow Reliability, Observability, and Explainability

Reliable workflow execution requires more than obtaining a successful final outcome. The execution process must also be sufficiently understandable to identify errors, inspect decisions, and reproduce relevant behavior.

Kleppmann (2017) provides a broader foundation for reasoning about reliable software and data-intensive systems.

Explainable artificial intelligence research addresses methods and challenges associated with understanding AI-system behavior (Barredo Arrieta et al., 2020).

These foundations are relevant because a workflow-routing decision can fail for different reasons. The natural-language condition may be interpreted incorrectly, the resulting contract may be malformed, the workflow state may be invalid, or the selected transition may violate the graph.

A structured architecture can make some of these failure categories more visible by separating interpretation, validation, evaluation, and graph enforcement.

Execution traces provide additional evidence by recording selected inputs, decisions, and outcomes.

However, trace generation alone does not establish complete auditability. Stronger audit guarantees would require consideration of exceptional failures, trace integrity, retention, and recovery.

## 2.7 Natural-Language Edge Semantics and Deterministic Agent Execution

The central research problem exists at the boundary between natural-language interpretation and executable workflow control.

A natural-language edge description expresses an intended condition in human-readable form. A workflow engine must convert that intention into a decision about whether a transition should occur.

One approach asks a language model to select the destination directly. This combines condition interpretation and routing selection in one model-driven operation.

An alternative approach first translates the natural-language condition into a structured representation and then evaluates that representation using deterministic software.

The implemented prototype investigates the second approach.

Its semantic contract contains a source node, destination node, condition field, comparison operator, and expected value.

For the evaluated workflow, the supported condition is a Boolean equality comparison over the variable `tests_passed`.

This design makes the interpreted condition explicit and reusable.

However, deterministic evaluation only guarantees consistent application of the contract under equivalent inputs. It does not establish that the original natural-language interpretation was correct.

The distinction between semantic correctness and execution determinism is therefore central to the research.

## 2.8 Relevant Methods, Frameworks, and Evaluation Foundations

Several methodological foundations inform the evaluation.

Structured-output research is relevant because machine-readable model outputs can be checked against expected representations. Geng et al. (2025) examine structured outputs from language models.

Graph and workflow research motivates the use of explicit transition conditions and controlled execution paths.

Software-reliability and explainability literature motivates recording execution evidence and distinguishing different failure categories.

The project operationalizes these concerns through several measurements:

- **Routing accuracy:** whether the selected destination matches the expected outcome.
- **Repeated-decision stability:** whether repeated evaluations of the same case produce the same outcome.
- **Workflow-path accuracy:** whether a tested workflow run reaches the expected terminal destination.
- **Trace verification:** whether selected routing records exist, are readable, and contain expected information.
- **Computational overhead:** the number of model calls and measured execution time.

These metrics represent selected aspects of the broader concepts of correctness, repeatability, auditability, and efficiency.

The experimental procedures and limitations are described in Chapter 4.

## 2.9 Comparison of Existing Approaches

The reviewed approaches address complementary aspects of autonomous software-development workflows, but they emphasize different technical problems.

SWE-agent and OpenHands demonstrate how language-model agents can interact with software-development environments and carry out engineering tasks (Yang et al., 2024; Wang et al., 2024). Their relevance to this project lies in the broader need to coordinate agent actions. However, agent task capability does not, by itself, establish a reusable semantic contract for interpreting natural-language graph-edge conditions.

LangGraph provides a graph-oriented foundation for organizing workflow states and conditional transitions (LangChain, Inc., n.d.). AutoGen emphasizes coordination through multi-agent conversations (Wu et al., 2024). These approaches demonstrate orchestration mechanisms, but their general capabilities should not be confused with a guarantee that arbitrary natural-language transition descriptions will be interpreted consistently.

ReAct combines reasoning with action (Yao et al., 2023), while Reflexion investigates feedback-driven improvement in language-agent behavior (Shinn et al., 2023). Such methods are relevant to model-driven decision-making, but they do not eliminate the distinction between probabilistic language interpretation and deterministic evaluation of an already structured condition.

Structured-output research provides a related foundation for producing machine-readable representations (Geng et al., 2025). Nevertheless, syntactic conformity alone does not prove that a generated condition correctly preserves the intended meaning of its natural-language source. This distinction matters because a structurally valid contract can still encode an incorrect Boolean interpretation.

The present research therefore focuses on a narrower architectural boundary. Natural-language edge descriptions are interpreted into structured contracts; the contracts are checked against a defined schema and evaluated by deterministic routing logic. The resulting decisions can then be examined through execution traces.

This separation supports repeatable evaluation of an unchanged contract, but it does not guarantee that the original interpretation is semantically correct. Reusing an incorrect contract can reproduce the same error consistently.

Consequently, the evaluation must distinguish routing correctness from repeated-decision stability, contract validity from semantic fidelity, and trace availability from complete system auditability. These distinctions motivate the experimental measures described in Chapter 4.

## 2.10 What Existing Literature Already Addresses

The original Capstone I proposal summarized the literature foundations and remaining A2 research gap in Table 2.1.

**Table 2.1 — Literature Themes and Identified Gap**

| Theme | Representative foundation | Remaining issue relevant to A2 |
|---|---|---|
| Autonomous SE agents | SWE-agent; OpenHands | Agent capability does not by itself define transition semantics. |
| Graph orchestration | LangGraph; AutoGen | Conditional routing exists, but natural-language edge semantics remain under-specified. |
| Reasoning and reflection | ReAct; Reflexion | Reasoning improves decision support but does not guarantee deterministic routing. |
| Evaluation and explainability | Structured evaluation; XAI | Process evidence can be improved through explicit traces and measurable metrics. |
| Research direction | StrongDM software-factory context | A2 focuses on a structured semantic boundary between language interpretation and execution. |

The table distinguishes the project's contribution from the broader capabilities already represented in the literature.

The identified gap is not that existing agent systems lack routing or that deterministic software execution is a new concept.

Rather, the project investigates a specific architectural boundary between interpreting natural-language workflow conditions and applying those conditions through explicit deterministic routing logic.

The prototype and experiments described in subsequent chapters evaluate this approach within a limited Boolean workflow.

## 2.11 Chapter Summary

This chapter reviewed the research foundations for autonomous software-engineering agents, graph-based orchestration, language-model reasoning, workflow reliability, explainability, and structured semantic representations.

The literature motivates the need for clear transition semantics when natural-language descriptions influence executable workflow decisions.

The project addresses this concern by separating language-model interpretation from deterministic condition evaluation, graph-transition enforcement, and execution-trace recording.

Chapter 3 describes the implemented prototype and the technical boundaries within which this approach was evaluated.

---

## References

Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion, 58*, 82–115. https://doi.org/10.1016/j.inffus.2019.12.012

Geng, S., Cooper, H., Moskal, M., Jenkins, S., Berman, J., Ranchin, N., West, R., Horvitz, E., & Nori, H. (2025). Generating structured outputs from language models: Benchmark and studies. arXiv:2501.10868. https://arxiv.org/abs/2501.10868

Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

LangChain, Inc. (n.d.). *LangGraph documentation*. https://docs.langchain.com/oss/python/langgraph/overview

Murata, T. (1989). Petri nets: Properties, analysis and applications. *Proceedings of the IEEE, 77*(4), 541–580. https://doi.org/10.1109/5.24143

Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4th ed.). Pearson.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems, 36*. https://doi.org/10.52202/075280-0377

StrongDM Team. (2026, February 9). *The StrongDM software factory: Building software with AI*. https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai

Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., . . . Neubig, G. (2024). OpenHands: An open platform for AI software developers as generalist agents. arXiv:2407.16741. https://arxiv.org/abs/2407.16741

Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2024). AutoGen: Enabling next-gen LLM applications via multi-agent conversations. *Conference on Language Modeling (COLM).* https://openreview.net/forum?id=BAakY1hNKS

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. *Advances in Neural Information Processing Systems, 37*. https://doi.org/10.52202/079017-1601

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*. https://arxiv.org/abs/2210.03629

---

# Chapter 3 — System Design and Implementation

**CISC 699 Capstone II A2**  
**Project:** Natural-Language Edge Semantics and Deterministic Agent Execution  
**Status:** Preliminary implementation chapter based on the developed prototype

## 3.1 Introduction

This chapter describes the design and implementation of the prototype developed to investigate structured natural-language edge semantics for deterministic routing in graph-based autonomous software-development workflows.

The implementation separates language-model-based interpretation of natural-language edge conditions from deterministic evaluation and graph-transition enforcement. It also includes a direct natural-language routing baseline and an execution-trace mechanism for recording routing decisions.

The chapter describes the implemented components and their interactions. It does not assume that every feature proposed during Capstone I was completed.

## 3.2 System Requirements and Design Objectives

The prototype was designed to address five principal technical objectives.

First, it needed a structured representation of workflow-edge conditions.

Second, it needed to distinguish probabilistic natural-language interpretation from deterministic condition evaluation.

Third, it needed to reject structurally invalid contracts and prevent transitions that were not permitted by the implemented graph.

Fourth, it needed to support comparisons between direct language-model routing and structured contract-based routing.

Fifth, it needed to produce inspectable records of selected workflow-routing decisions.

These objectives guided the implementation of the contract schema, validation and evaluation modules, graph representation, routing components, language-model interfaces, and trace persistence mechanism.

## 3.3 Implemented System Architecture

The implemented architecture contains two main routing approaches.

The **structured routing approach** interprets natural-language conditions into machine-readable contracts. A deterministic router then evaluates those contracts against the current workflow state. A traced routing wrapper additionally checks graph permissions and records the result.

The **direct routing approach** sends the workflow state and outgoing natural-language edge descriptions to the language model and requests a destination directly.

The distinction between these approaches is central to the experimental design.

### 3.3.1 Structured Routing Data Flow

The structured approach follows this general sequence:

1. A natural-language edge description is supplied with its workflow source and destination context.
2. The language-model interpreter generates a structured condition.
3. The generated contract is checked for supported structural properties.
4. The deterministic evaluator compares the contract condition with workflow data.
5. The router determines whether the available contracts produce one matching destination, no matching destination, or an ambiguous or invalid result.
6. The traced routing wrapper checks whether the selected transition is permitted by the graph.
7. A JSON execution trace is generated for the completed traced-routing operation.

This separation allows previously generated contracts to be reused without requesting a new interpretation for every decision.

### 3.3.2 Direct Routing Data Flow

The direct baseline supplies the current workflow state and outgoing natural-language edge descriptions to the language model.

The model is asked to return a destination or a no-match result.

The baseline checks that a returned destination belongs to the supplied set of allowed targets.

A second direct baseline adds explicit Boolean interpretation guidance to the prompt. This provides an additional comparison condition, although the direct and structured approaches are not identical in their prompts or output constraints.

## 3.4 Structured Semantic Contract Representation

The structured semantic contract is the central representation used by the deterministic routing approach.

Each contract identifies the source node, destination node, workflow-data field, comparison operator, and expected value.

For the implemented prototype, the supported condition is limited to a Boolean comparison using the workflow-data field `tests_passed` and the operator `equals`.

A representative contract is:

```json
{
  "source": "Check Tests",
  "target": "Deploy Code",
  "field": "tests_passed",
  "operator": "equals",
  "value": true
}
```

The contract represents a transition from `Check Tests` to `Deploy Code` when the workflow state reports that the tests passed.

The prototype does not implement a general-purpose expression language containing arbitrary variables, numerical comparisons, or compound logical expressions.

## 3.5 Contract Validation

The contract-validation component checks whether an individual contract has the expected structural properties.

The implemented checks include the required source and target information, the supported field name, the supported comparison operator, and a Boolean condition value.

These checks distinguish supported contract structures from malformed or unsupported structures.

However, structural validation does not establish that a generated contract correctly expresses the meaning of the original natural-language edge description.

For example, a contract may contain a valid Boolean value while incorrectly reversing the intended condition.

Graph membership and transition permissions are also separate concerns. The individual contract validator does not independently establish that a source-target pair is a permitted graph edge.

This distinction is important when interpreting the evaluation results.

## 3.6 Deterministic Contract Evaluation

The deterministic evaluator compares the current workflow state with a validated contract condition.

For the implemented Boolean condition, evaluation determines whether the value of `tests_passed` equals the contract's expected Boolean value.

Unlike natural-language interpretation, this comparison does not require a language-model call.

When the same contract and workflow state are supplied repeatedly, the deterministic comparison is designed to produce the same result.

This provides execution-level consistency, although it does not guarantee that the contract's original semantic interpretation was correct.

## 3.7 Contract-Based Routing

The contract router evaluates the available contracts for a current workflow node and returns a routing outcome.

The implemented outcomes include:

- `ROUTED`
- `NO_MATCH`
- `AMBIGUOUS`
- `INVALID_CONTRACT`
- `INVALID_WORKFLOW_DATA`

A `ROUTED` outcome indicates that a destination was selected.

A `NO_MATCH` outcome indicates that no evaluated contract selected a destination.

An `AMBIGUOUS` outcome indicates that more than one contract matched.

The invalid-input outcomes distinguish certain unsupported contracts or workflow-data conditions from ordinary routing decisions.

The contract router itself is not graph-aware. Graph-transition permission is enforced by the traced routing wrapper.

## 3.8 Workflow Graph and Transition Enforcement

The implemented workflow graph contains three nodes:

- `Check Tests`
- `Deploy Code`
- `Fix Code`

The graph permits two outgoing transitions from `Check Tests`.

The transition to `Deploy Code` represents the successful-test condition.

The transition to `Fix Code` represents the failed-test condition.

Both destination nodes are terminal within the implemented graph.

The prototype does not contain a separate `Start` node or additional intermediate execution nodes.

The graph component checks whether a requested source-target transition is permitted.

The traced routing wrapper uses this check after contract routing. A selected destination that is not permitted by the graph can produce an `INVALID_GRAPH_TRANSITION` outcome.

This provides an additional enforcement layer beyond individual contract validation.

## 3.9 Natural-Language Interpretation with a Local Language Model

The structured interpretation component uses a locally hosted Ollama model, `llama3.2:3b`.

The interpreter requests a structured output containing the supported condition field, comparison operator, and Boolean value.

The model is configured with temperature zero to reduce sampling variability.

The interpreter also supplies explicit guidance about the meaning of successful and failed tests.

The source and destination nodes are provided through the workflow context rather than inferred entirely from the generated condition.

The resulting contract is checked for supported structure before it is used by the deterministic routing components.

Despite these constraints, the model can still produce a structurally valid contract with an incorrect Boolean interpretation. The implemented structural validator does not automatically detect every such semantic error.

## 3.10 Direct Natural-Language Routing Baselines

The project implemented two direct language-model routing variants.

The original direct baseline requests a routing destination from the language model using the current workflow state and outgoing natural-language edge descriptions.

The prompt-controlled baseline uses the same general direct-routing architecture but adds explicit guidance about the Boolean meaning of passing and failing tests.

Both baselines use the locally hosted model with temperature zero.

Their outputs are checked against the supplied allowed destinations.

These baselines were used to compare direct destination selection with the structured approach under repeated natural-language test cases.

The baselines do not implement the same intermediate contract representation and deterministic evaluation process as the structured approach.

## 3.11 Contract Reuse

The implementation supports generating structured contracts once and applying them to repeated routing decisions.

In the contract-reuse experiment, two contracts were generated for each natural-language test case.

Those contracts were then reused for three routing decisions involving the same case.

This avoided additional LLM interpretation calls during the repeated deterministic decisions.

The reuse mechanism reduces repeated interpretation overhead, but it also preserves any semantic error present in the original contracts.

Therefore, contract reuse is an execution-efficiency mechanism rather than a substitute for semantic validation.

## 3.12 Execution-Trace Generation and Persistence

The traced routing component records selected routing operations as JSON execution traces.

The trace information includes a timestamp, current workflow node, workflow data, evaluated contracts, routing status, selected destination, matched contracts, validation results, and a decision explanation.

The traced routing wrapper also assigns a unique trace identifier.

The persistence implementation writes the serialized trace through a temporary file, flushes and synchronizes the file, and then replaces the destination file.

This approach reduces the risk of incomplete files during normal write operations.

However, the implementation does not guarantee that every exception or system failure produces a persisted trace.

The trace mechanism should therefore be understood as a tested audit-support feature, not as a complete fault-tolerant audit infrastructure.

## 3.13 Prototype Modules and Responsibilities

The implementation is organized into Python modules with distinct responsibilities.

| Module | Principal responsibility |
|---|---|
| `semantic_contract.py` | Defines the structured contract representation |
| `contract_validator.py` | Checks supported contract structure |
| `contract_evaluator.py` | Evaluates contract conditions against workflow data |
| `contract_router.py` | Selects routing outcomes from evaluated contracts |
| `graph.py` | Defines permitted workflow transitions |
| `traced_contract_router.py` | Applies graph enforcement and saves routing traces |
| `execution_trace.py` | Constructs and persists execution-trace records |
| `ollama_structured_interpreter.py` | Interprets natural-language conditions into structured data |
| `direct_nl_llm_router.py` | Implements the original direct-routing baseline |
| `direct_nl_llm_router_controlled.py` | Implements the prompt-controlled direct-routing baseline |

The evaluation scripts use these components to conduct routing comparisons, contract-reuse tests, and workflow-path and trace experiments.

## 3.14 Implementation Scope and Boundaries

The completed prototype demonstrates a narrow but functional separation between language-model interpretation and deterministic graph routing.

Its implemented condition language supports one Boolean workflow-data field and one comparison operator.

Its graph contains three nodes and two permitted transitions.

Its workflow-path evaluation uses manually authored reference contracts and one transition per complete terminal path.

The prototype does not execute a full autonomous software-development lifecycle, coordinate multiple autonomous agents, or demonstrate complex multi-step workflow execution.

These boundaries are essential when interpreting the experimental results and describing the project's contributions.

## 3.15 Chapter Summary

This chapter described the implemented prototype architecture and its major components.

The system separates natural-language condition interpretation from deterministic contract evaluation, supports direct-routing baselines, enforces graph-transition permissions through a traced routing wrapper, and persists JSON records of tested routing operations.

The implementation provides the technical foundation for the evaluation methodology presented in Chapter 4.

Its limited Boolean condition language and small workflow graph also define the scope within which the experimental findings should be interpreted.

---

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

---

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

A case-level inspection of the fresh structured-routing records identified six incorrect decisions across IND06 and IND10, with three repetitions per case. Both conditions required `tests_passed = False`, but the generated repair-edge contracts specified `tests_passed = True`. The contracts were recorded as structurally valid, and the router returned `NO_MATCH` for all six decisions. These six outcomes account for the difference between the 30 evaluated decisions and the 24 correct structured-routing decisions.

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

---

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

---

# Chapter 7 — Conclusion and Future Work

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

The findings provide a qualified answer. Structured contracts establish an explicit boundary between language-model interpretation and deterministic condition evaluation. Once generated, a contract can be evaluated repeatedly without additional language-model calls, while routing decisions can be recorded for inspection.

The experiments demonstrate the feasibility of this separation within the tested Boolean workflow. They also show that repeatable execution and structurally valid contracts do not guarantee correct interpretation of the original natural-language condition.

Therefore, the demonstrated contribution is a more explicit and testable routing process, not proof of universally correct or fully auditable autonomous execution.

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

This research implemented and evaluated a structured-contract approach to natural-language workflow routing.

The prototype demonstrates a practical separation between interpretation, deterministic evaluation, graph-transition enforcement, and trace recording within a limited Boolean workflow.

Its central qualification is that **deterministic execution can consistently apply an incorrectly interpreted contract**. Reliable extensions must therefore address semantic fidelity as well as repeatability, execution correctness, and trace integrity.
