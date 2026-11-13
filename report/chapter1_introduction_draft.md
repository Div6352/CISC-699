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
