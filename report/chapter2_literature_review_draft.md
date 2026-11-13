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
