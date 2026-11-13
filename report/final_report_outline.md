# CISC 699 Capstone II — Detailed Final Report Outline

**Project Title:** Designing Structured Natural-Language Edge Semantics for Deterministic Agent Execution in Graph-Based Autonomous Software Development Workflows

**Research Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution

**Course:** CISC 699 — Applied Project in Computer Information Science

**Institution:** Harrisburg University of Science and Technology

**Document Purpose:** Detailed blueprint for preparing the completed Capstone II technical research report.

**Primary Authority:** CISC 699 Final Report Guide, provided by the instructor.

**Supporting Documents:**
- GRAD 695 Capstone I Research Proposal.
- Individual 13-Week Research Schedule and Research Work Plan.
- `report/proposal_migration_audit.md`
- `docs/proposal_objective_alignment.md`
- `docs/final_evaluation_results.md`
- Project implementation, tests, and experimental result files.

**Document Status:** Planning outline. This is not the final report.

---

# A. Report-Wide Requirements

## A.1 Academic Purpose

The final report must demonstrate:

1. A clearly defined research problem supported by credible literature.
2. A research question and objectives consistent with the approved proposal.
3. A computational solution that was actually implemented.
4. A defensible and reproducible evaluation methodology.
5. Experimental findings supported by recorded evidence.
6. Critical analysis of successful and unsuccessful outcomes.
7. A realistic discussion of limitations and threats to validity.
8. Supported contributions to software engineering and cybersecurity engineering.
9. Clear documentation enabling another researcher to inspect and reproduce the work.
10. Alignment between the report, source code, experimental outputs, appendices, and presentation.

The report must not present proposed work as completed work.

## A.2 Required Final Report Structure

| Component | Suggested Length |
|---|---:|
| Preliminary pages | As needed |
| Chapter 1 — Introduction and Problem Definition | 3–5 pages |
| Chapter 2 — Literature Review and Foundation | 5–8 pages |
| Chapter 3 — Solution Design and Implementation | 6–9 pages |
| Chapter 4 — Evaluation Methodology | 4–6 pages |
| Chapter 5 — Results and Analysis | 5–8 pages |
| Chapter 6 — Discussion and Validity | 3–5 pages |
| Chapter 7 — Conclusions and Future Work | 2–3 pages |
| References and appendices | As needed |

**Suggested main-text total:** 28–44 pages.

The page ranges are planning guidance, not guaranteed grading criteria.

## A.3 Writing and Evidence Rules

- Use formal academic writing and consistent technical terminology.
- Support literature claims with verified academic or authoritative sources.
- Support implementation claims with actual source code, tests, or execution records.
- Support numerical findings with original experimental data and checked calculations.
- Separate observations from interpretations.
- Explain unsuccessful experiments and deviations.
- Use consistent numbered citations and complete reference entries.
- Define abbreviations when first introduced.
- Number and caption every figure and table.
- Refer to figures and tables in the surrounding text.
- Include units, denominators, and experimental conditions when reporting metrics.
- Do not invent instructor approvals, protocol decisions, test outcomes, or references.
- Preserve the original Capstone I proposal as an unchanged historical document.

---

# B. Preliminary Pages

## Title Page

Include:

- Full research project title.
- Student name.
- Degree program and specialization.
- University.
- CISC 699 course.
- Faculty advisor or instructor, as required.
- Submission date.
- Software artifact version or repository location.

Verify exact institutional formatting before finalization.

## Abstract — 200–300 Words

Write after completing and verifying the main report.

The abstract should cover:

1. Research context and problem.
2. Research question or primary objective.
3. Structured semantic-contract approach.
4. Implemented computational artifact.
5. Controlled comparison methodology.
6. Principal observed result with its denominator.
7. Execution overhead and major limitations.
8. Research contribution.

The abstract must not overstate generalizability.

## AI-Use Disclosure and Contribution Statement

Describe the actual use of AI tools in:

- Research planning.
- Code development or debugging.
- Documentation and writing.
- Editing and formatting.
- Data analysis support.

Clarify the student's responsibility for verifying technical claims, calculations, references, code, and final content.

Do not reuse the Capstone I disclosure without updating it.

## Other Preliminary Material

- Acknowledgments, if appropriate.
- Table of contents.
- List of figures.
- List of tables.
- List of abbreviations and acronyms.

Use Word heading styles, automatic captions, and generated navigation in the final DOCX report.

---

# Chapter 1 — Introduction and Problem Definition

**Suggested length:** 3–5 pages.

**Primary source:** Capstone I proposal, Chapter 1.

**Purpose:** Establish the research problem, justify the study, define its objectives, and accurately describe the completed scope.

## 1.1 Background and Application Context

Discuss:

- AI-assisted software engineering.
- Autonomous software-development agents.
- Graph-based workflow orchestration.
- Conditional transitions between workflow stages.
- Natural-language descriptions of workflow conditions.
- The distinction between interpreting a condition and executing a transition.

Explain why routing decisions affect the predictability and auditability of automated development workflows.

Use verified literature for general claims.

## 1.2 Research and Practice Gap

Describe the specific challenge investigated:

Natural-language edge conditions may require probabilistic interpretation, while workflow execution benefits from explicit, reproducible transition rules.

Distinguish:

- General language-model uncertainty.
- Ambiguity in workflow conditions.
- Structural validation of contracts.
- Semantic correctness of interpreted conditions.
- Deterministic execution after interpretation.

Avoid claiming that all existing workflow frameworks lack structured semantics.

Identify precisely what the implemented research evaluates.

## 1.3 Problem Statement and Research Question

Preserve the original Capstone I research question:

**How can a structured natural-language edge semantics framework improve the determinism, repeatability, and auditability of graph-based autonomous software-development workflows?**

Explain that the study evaluates this question through a controlled prototype and comparisons against direct natural-language routing.

## 1.4 Research Objectives

Preserve the five original objectives:

1. To examine how natural-language edge conditions are interpreted within graph-based autonomous software-development workflows.
2. To develop a structured semantic representation of edge conditions, including state variables, operators, expected values, and destination routes.
3. To implement a controlled prototype that separates natural-language interpretation from deterministic workflow-transition evaluation.
4. To evaluate the proposed approach against direct natural-language routing using repeated executions of predefined scenarios.
5. To assess decision consistency, workflow-path repeatability, expected-route accuracy, trace completeness, validation behavior, and execution overhead.

Explain how each objective is evaluated later in the report.

**Evidence:** `docs/proposal_objective_alignment.md`

## 1.5 Purpose and Significance

Explain the intended value of:

- Explicit semantic contracts.
- Deterministic condition evaluation.
- Controlled routing outcomes.
- Structural validation.
- Diagnostic routing statuses.
- Execution trace recording.

Distinguish demonstrated prototype behavior from anticipated benefits in larger systems.

## 1.6 Final Scope, Delimitations, and Constraints

Document the actual scope:

- Small graph-based software-development workflow.
- Boolean test-result state.
- Two principal conditional destinations.
- Local Ollama model.
- Structured contract generation and validation.
- Direct LLM routing baseline.
- Controlled experimental datasets.
- Repeated routing and interpretation tests.
- JSON execution traces.

Identify exclusions:

- Enterprise-scale agent orchestration.
- Arbitrary natural-language logic.
- Production security certification.
- Universal semantic correctness.
- Broad statistical generalization.

Explain any documented changes from the original proposal.

## 1.7 Overview of the Computational Artifact

Briefly introduce:

- Natural-language interpreter.
- Semantic contract.
- Validator.
- Deterministic evaluator.
- Router.
- Workflow graph.
- Trace recorder.
- Experimental scripts.

Keep implementation detail in Chapter 3.

## 1.8 Organization of the Report

Summarize Chapters 2–7 in a short paragraph.

### Required Chapter 1 Table

**Table 1.1 — Research Problem, Objectives, and Evaluation Evidence**

Columns:

- Research issue.
- Original objective.
- Implemented component or experiment.
- Final-report chapter.
- Evidence reference.

### Chapter 1 Completion Checks

- Research question matches the original proposal.
- All five objectives appear accurately.
- Gap claims have verified references.
- Scope matches the implemented prototype.
- No unapproved scope change is described as approved.
- Every objective links to later evidence.

---

# Chapter 2 — Literature Review and Foundation

**Suggested length:** 5–8 pages.

**Primary source:** Capstone I proposal, Chapter 2.

**Purpose:** Establish the scholarly foundation for the architecture and evaluation design.

## 2.1 Introduction and Review Scope

Explain the purpose of the literature review.

Identify the research themes and their relationship to the research question.

## 2.2 Literature Search Strategy

Document:

- Databases or repositories actually searched.
- Search dates.
- Search terms.
- Inclusion and exclusion criteria.
- Types of accepted sources.
- Verification of original publications.
- Focused updates since Capstone I.

Do not describe the review as systematic unless the documented process supports that designation.

## 2.3 Autonomous Software-Engineering Agents

Review relevant work concerning:

- LLM-supported software-development agents.
- Agent-based task execution.
- Autonomous development workflows.
- Reliability challenges in agent decisions.

Explain how these findings motivate controlled routing.

## 2.4 Graph-Based Workflow Orchestration

Review:

- Nodes and edges.
- Conditional transitions.
- Workflow state.
- Directed graph execution.
- Deterministic transition evaluation.
- Handling invalid or ambiguous routes.

Relate the literature to the implemented workflow graph.

## 2.5 Natural-Language Interpretation and LLM Decision Making

Discuss:

- Natural-language conditions.
- Semantic ambiguity.
- Structured model outputs.
- Prompt sensitivity.
- Repeated interpretation behavior.
- Limitations of deterministic generation settings.

Distinguish language-model output stability from semantic correctness.

## 2.6 Structured Semantics and Contract-Based Execution

Review relevant foundations for:

- Explicit condition representations.
- State variables.
- Operators and expected values.
- Schema validation.
- Contract evaluation.
- Separation of interpretation from execution.

Do not claim novelty without comparing relevant prior work.

## 2.7 Workflow Reliability, Observability, and Auditability

Discuss:

- Reproducibility.
- Decision consistency.
- Execution tracing.
- Failure explanations.
- Logging and provenance.
- Validation and controlled failure handling.

Explain how these concepts inform the prototype.

## 2.8 Comparison of Existing Approaches

Compare literature-supported approaches, potentially including:

- Direct LLM routing.
- Rule-based interpretation.
- Structured-output interpretation.
- Contract-based deterministic evaluation.

Only include claims supported by verified sources.

## 2.9 Research Gap Synthesis

Identify what the reviewed literature supports and what remains insufficiently evaluated for this project's bounded research question.

Avoid implying that a small experiment resolves the entire research gap.

## 2.10 Implications for the Implemented Design

Connect literature findings to:

- The semantic-contract schema.
- The interpreter.
- The validator.
- The deterministic router.
- The direct LLM baseline.
- The evaluation metrics.

### Required Chapter 2 Tables

**Table 2.1 — Verified Literature Synthesis Matrix**

Columns:

- Source.
- Research context.
- Method.
- Main finding.
- Limitation.
- Relevance to this project.

**Table 2.2 — Related Approaches and Design Implications**

Columns:

- Approach.
- Supported strengths.
- Supported limitations.
- Implication for the prototype.

### Chapter 2 Completion Checks

- Every major scholarly claim has a verified source.
- Citations match the reference list.
- Sources are discussed critically, not merely summarized.
- The gap follows from evidence.
- Literature findings connect to implementation choices.
- No bibliographic details are invented.

---

# Chapter 3 — Solution Design and Implementation

**Suggested length:** 6–9 pages.

**Primary source:** Capstone I proposal, Chapter 3, updated using actual code.

**Purpose:** Document the implemented computational solution.

## 3.1 Solution Overview and Design Goals

Describe the implemented approach:

Natural-language edge conditions are interpreted into structured semantic contracts. Contracts are validated and evaluated through deterministic logic, and the routing outcome may be recorded in an execution trace.

Explain the intended separation of responsibilities.

## 3.2 Functional and Nonfunctional Requirements

Document requirements for:

- Interpreting supported natural-language conditions.
- Constructing semantic contracts.
- Validating contract structure.
- Evaluating workflow state.
- Selecting a destination.
- Handling no-match and ambiguity.
- Checking permitted graph transitions.
- Recording execution traces.
- Supporting repeated experiments.

Identify actual acceptance criteria and verification evidence.

## 3.3 Implemented System Architecture

Describe component boundaries and data flow.

Components include:

- Ollama interpretation layer.
- Semantic contract representation.
- Contract validator.
- Deterministic evaluator.
- Contract router.
- Graph-transition checker.
- Trace recorder.
- Experimental baseline.

Explain which components use the LLM and which use deterministic Python logic.

## 3.4 Natural-Language Interpretation Layer

**Implementation:** `src/ollama_structured_interpreter.py`

Describe:

- Local Ollama interaction.
- `llama3.2:3b` model.
- Structured JSON output.
- Temperature setting.
- Supported condition fields.
- Interpretation instructions.
- Error handling.
- Known semantic interpretation failures.

Clarify that source and target nodes are supplied by the workflow scenario rather than freely inferred by the model.

## 3.5 Structured Semantic Contract

**Implementation:** `src/semantic_contract.py`

Document:

- Source node.
- Target node.
- Optional edge identifier.
- Condition field.
- Operator.
- Expected Boolean value.

Provide a representative contract example verified against the implementation.

## 3.6 Contract Validation

**Implementation:** `src/contract_validator.py`

Explain:

- Required fields.
- Supported condition schema.
- Boolean value validation.
- Invalid contract outcomes.
- Accepted additional fields.
- Limits of individual contract validation.

Distinguish structural validity from semantic correctness.

## 3.7 Deterministic Condition Evaluation

**Implementation:** `src/contract_evaluator.py`

Explain how a validated condition is evaluated against workflow state.

Show that unchanged supported inputs produce repeatable Boolean results.

Avoid claiming that interpretation itself is deterministic.

## 3.8 Deterministic Contract Routing

**Implementation:** `src/contract_router.py`

Explain the routing outcomes:

- `ROUTED`
- `NO_MATCH`
- `AMBIGUOUS`
- `INVALID_CONTRACT`
- `INVALID_WORKFLOW_DATA`

Describe matched contracts, validation results, and decision explanations.

## 3.9 Workflow Graph and Transition Enforcement

**Implementation:** `src/graph.py`

Explain the supported workflow nodes and transitions.

Describe how permitted transitions are checked separately from individual contract validation.

## 3.10 Execution Trace Architecture

**Implementations:**
- `src/traced_contract_router.py`
- `src/execution_trace.py`

Describe:

- Trace identifiers.
- Timestamps.
- Current workflow node.
- Workflow state.
- Evaluated contracts.
- Validation outcomes.
- Routing status.
- Selected destination.
- Decision explanation.
- JSON trace persistence.

Explain the limitations of tracing and filesystem guarantees.

## 3.11 Direct Natural-Language Routing Baseline

**Implementation:** `src/direct_nl_llm_router.py`

Explain:

- Baseline inputs.
- Available workflow routes.
- Direct LLM decision generation.
- Model configuration.
- Differences from structured routing.
- Prompt-comparability limitations.

## 3.12 Implementation Environment and Dependencies

Document:

- Windows development environment.
- VS Code.
- Python 3.14.10.
- Python virtual environment.
- Local Ollama.
- `llama3.2:3b`.
- Standard-library dependencies.
- Repository layout.
- Reproduction commands.

Verify exact software versions before final submission.

## 3.13 Component Verification and Integration Testing

Summarize:

- Contract evaluation tests.
- Graph evaluator tests.
- Routing safety tests.
- Invalid contract tests.
- Graph-transition checks.
- Trace persistence tests.
- Ollama workflow integration.

Distinguish passing tests from research evidence of comparative superiority.

## 3.14 Actual Versus Proposed Implementation

Compare the Capstone I design against the completed prototype.

Identify:

- Completed components.
- Partially implemented requirements.
- Deferred features.
- Documented design deviations.
- Known defects or limitations.

### Required Chapter 3 Figures

**Figure 3.1 — Implemented Semantic-Contract Architecture**

Show the natural-language input, Ollama interpreter, contract validator, deterministic evaluator, router, graph check, and trace recorder.

**Figure 3.2 — Implemented Workflow State Diagram**

Show the tested workflow and conditional transitions.

**Figure 3.3 — Routing and Failure-Handling Sequence**

Show successful routing, no-match, ambiguity, invalid input, and graph-transition rejection.

### Required Chapter 3 Tables

- Table 3.1 — Functional Requirements and Verification Matrix.
- Table 3.2 — Semantic Contract Schema.
- Table 3.3 — Routing Status Definitions.
- Table 3.4 — Implemented Components and Source Files.
- Table 3.5 — Proposed Versus Actual Implementation.

### Chapter 3 Completion Checks

- All described components exist.
- Code behavior matches the written description.
- Architecture diagrams reflect the implementation.
- Actual test evidence supports verification claims.
- Security-related claims are appropriately limited.
- Known partial features are identified.

---

# Chapter 4 — Evaluation Methodology

**Suggested length:** 4–6 pages.

**Primary source:** Capstone I proposal, Chapter 4, revised using actual experiments.

**Purpose:** Explain how the study was performed so another researcher can understand and reproduce the evaluation.

## 4.1 Evaluation Purpose

Explain how the experiments address the research question and five objectives.

## 4.2 Research Design

Describe the controlled comparative evaluation.

Distinguish component verification from comparative research experiments.

Explain why multiple experimental stages were conducted.

## 4.3 Experimental Workflow and Scenario Design

Describe:

- `Check Tests` decision node.
- `Deploy Code` destination.
- `Fix Code` destination.
- `tests_passed` workflow variable.
- Successful and failed states.
- Independent natural-language paraphrases.

## 4.4 Experimental Datasets

Identify each dataset separately:

1. Initial four-case rule-based interpretation baseline.
2. Original two-state matched routing scenarios.
3. Matched natural-language comparison.
4. Ten-case independent natural-language comparison.
5. Independent interpretation consistency dataset.
6. Oracle-based semantic consistency dataset.
7. Repeated matched independent evaluation.

Explain the sample size and repetition count of each.

## 4.5 Expected-Route Oracle

Explain how expected destinations were defined.

Describe the role of reference labels in measuring accuracy.

Identify any unverified approval or annotation decisions.

Do not claim that oracle correctness was independently approved without evidence.

## 4.6 Direct LLM Baseline

Document:

- Inputs and prompts.
- Available destinations.
- Workflow state.
- Model settings.
- Output interpretation.
- Number of calls.

## 4.7 Structured Semantic-Contract Method

Document:

- Natural-language condition input.
- Contract generation.
- Validation.
- Deterministic evaluation.
- Destination selection.
- Number of model calls.
- Contract reuse or regeneration.

## 4.8 Comparison Fairness and Experimental Controls

Identify shared conditions and differences.

Discuss:

- Same model family.
- Temperature setting.
- Shared workflow states.
- Shared expected destinations.
- Different prompt guidance.
- Different output schemas.
- Different call counts.
- Contract reuse versus fresh interpretation.

State that architectural effects cannot be isolated perfectly under these conditions.

## 4.9 Repetition Protocol

Document the actual repetitions for each experiment.

For the repeated independent comparison:

- Ten independent cases.
- Three repetitions per case.
- Thirty decisions per method.

Explain why this experiment is distinct from separate path-repeatability and trace-repeatability tests.

## 4.10 Evaluation Metrics

Define:

**Expected-route accuracy**

Correct routing decisions divided by total evaluated decisions.

**Decision consistency**

Agreement among repeated routing decisions for the same scenario.

**Interpretation accuracy**

Generated condition interpretations matching reference semantic labels.

**Workflow-path repeatability**

Repeated executions producing the same workflow path.

**Trace completeness**

Required trace fields successfully recorded.

**Validation behavior**

Observed handling of valid and invalid contracts and workflow data.

**Execution overhead**

Measured elapsed time under specified experiment conditions.

Define how each metric was actually calculated.

## 4.11 Data Collection and Storage

Identify:

- Experiment scripts.
- JSON result files.
- Execution traces.
- Test records.
- Timing measurements.
- Configuration details.

Describe how evidence is preserved and referenced.

## 4.12 Analysis Procedure

Explain:

- Accuracy calculations.
- Repetition consistency checks.
- Error classification.
- Timing comparisons.
- Separation of component and end-to-end results.
- Treatment of incorrect but stable decisions.

## 4.13 Methodological Limitations

Document:

- Small dataset.
- Restricted workflow graph.
- Boolean-only conditions.
- Prompt differences.
- Limited model diversity.
- Local execution environment.
- Incomplete unified end-to-end measurement.
- Protocol and approval questions requiring verification.

### Required Chapter 4 Figures and Tables

- Figure 4.1 — Comparative Evaluation Workflow.
- Table 4.1 — Experimental Dataset Inventory.
- Table 4.2 — Baseline and Structured Method Controls.
- Table 4.3 — Evaluation Metric Definitions.
- Table 4.4 — Experimental Protocol and Repetition Counts.
- Table 4.5 — Data Collection and Evidence Locations.

### Chapter 4 Completion Checks

- Every experiment has a defined dataset and denominator.
- Prompts and model settings are documented.
- Timing conditions are comparable only where justified.
- Oracle labels are traceable.
- Protocol deviations are disclosed.
- Reproduction instructions match actual scripts.

---

# Chapter 5 — Results and Analysis

**Suggested length:** 5–8 pages.

**Primary source:** Recorded Capstone II experimental evidence.

**Purpose:** Present actual observations and explain what the data shows.

## 5.1 Results Overview

Introduce the experiments and explain that results are not pooled across different datasets.

## 5.2 Initial Rule-Based Interpretation Results

Report:

- Four evaluated conditions.
- Two correct interpretations.
- 50% accuracy.
- Two abstentions.
- 50% abstention rate.

Explain the limitation of exact-match interpretation.

## 5.3 Deterministic Component Evaluation Results

Report:

- Expected Boolean condition evaluations.
- Ten identical repeated contract evaluations.
- Early graph evaluator tests.
- Routing safety tests.
- No-match and ambiguity handling.

Clarify the narrow scope of these tests.

## 5.4 Original Matched Routing Comparison

Report:

| Metric | Direct LLM | Structured |
|---|---:|---:|
| Correct decisions | 5/10 | 10/10 |
| Expected-route accuracy | 50% | 100% |

Explain contract reuse and timing differences.

## 5.5 Matched Natural-Language Comparison

Report:

| Metric | Direct LLM | Structured |
|---|---:|---:|
| Correct decisions | 5/10 | 10/10 |
| Accuracy | 50% | 100% |
| Total time | 22.4867 s | 9.0886 s |

Explain why reused contracts affect the timing interpretation.

## 5.6 Independent Natural-Language Comparison

Report:

| Metric | Direct LLM | Structured |
|---|---:|---:|
| Correct decisions | 5/10 | 8/10 |
| Accuracy | 50% | 80% |
| Total time | 36.7451 s | 80.9153 s |

Explain why the structured approach required more time.

## 5.7 Independent Interpretation Consistency

Report:

- Thirty interpretation attempts.
- Twenty-five correct.
- 83.3% interpretation accuracy.
- Nine of ten cases with identical normalized predictions.
- IND06 incorrect in all attempts.
- IND10 variable across attempts.

Explain why temperature 0 does not guarantee semantic correctness.

## 5.8 Oracle-Based Semantic Consistency

Report:

- Eight semantic matches out of ten.
- Two mismatches.
- IND06 and IND10 as failure cases.
- Structurally valid but semantically incorrect conditions.

Distinguish retrospective oracle evaluation from automatic production-time semantic verification.

## 5.9 Repeated Matched Independent Evaluation

Report:

| Metric | Direct LLM | Structured |
|---|---:|---:|
| Cases | 10 | 10 |
| Repetitions per case | 3 | 3 |
| Total decisions | 30 | 30 |
| Correct decisions | 15 | 24 |
| Accuracy | 50% | 80% |
| Stable case-level decisions | 10/10 | 10/10 |
| Total time | 89.5295 s | 253.5074 s |

Explain:

- Thirty-percentage-point accuracy difference.
- Stable but incorrect decisions.
- Structured interpretation failures.
- Direct routing bias toward `Deploy Code`.
- Structured overhead from fresh contract generation.

## 5.10 Workflow-Path Repeatability and Tracing

Report the separate 20/20 repeated path and 20/20 trace experiments.

Explain that these were not part of the thirty-decision independent benchmark.

Identify the fixed initial workflow transition.

## 5.11 Validation and Failure-Handling Results

Summarize tested:

- Invalid contracts.
- Missing workflow data.
- No-match routing.
- Ambiguous routing.
- Invalid graph transitions.
- Trace persistence behavior.

Identify remaining validator limitations.

## 5.12 Execution Overhead Analysis

Compare:

- Deterministic routing after contract construction.
- Contract construction and reuse.
- Fresh contract generation for each case.
- Repeated fresh contract generation.

Avoid presenting deterministic evaluation time as equivalent to full structured execution time.

## 5.13 Research Objective Results

For each of the five objectives, provide:

- Relevant experiment or implementation.
- Observed result.
- Supported interpretation.
- Limitation.
- Evidence reference.

### Required Chapter 5 Figures

- Figure 5.1 — Routing Accuracy Across Separate Comparisons.
- Figure 5.2 — Repeated Independent Accuracy Comparison.
- Figure 5.3 — Repeated Independent Execution Time.
- Figure 5.4 — Interpretation Accuracy and Stability.
- Figure 5.5 — Scenario-Level Error Summary.

### Required Chapter 5 Tables

- Table 5.1 — Consolidated Experimental Results.
- Table 5.2 — Repeated Independent Comparison.
- Table 5.3 — Semantic Interpretation Errors.
- Table 5.4 — Validation and Failure Outcomes.
- Table 5.5 — Execution Overhead.
- Table 5.6 — Objective-to-Finding Traceability.

### Chapter 5 Completion Checks

- Every number matches a recorded result.
- Denominators are explicit.
- Figures match the underlying data.
- No different datasets are silently combined.
- Results and interpretations are separated.
- Failure cases are discussed.
- Unsupported statistical claims are avoided.

---

# Chapter 6 — Discussion and Validity

**Suggested length:** 3–5 pages.

**Purpose:** Interpret the findings, explain their contribution, and critically assess their limitations.

## 6.1 Interpretation of the Main Findings

Discuss the observed accuracy improvement within the tested benchmark.

Explain the role of structured conditions and deterministic routing.

## 6.2 Determinism Versus Semantic Correctness

Explain that deterministic execution can consistently evaluate an incorrect contract.

Use the IND06 and IND10 cases as evidence.

## 6.3 Decision Consistency Versus Routing Accuracy

Discuss why both methods showed repeated decision stability even when some decisions were wrong.

Explain why consistency and correctness must be measured separately.

## 6.4 Comparison Fairness

Discuss:

- Unequal prompt guidance.
- Different numbers of model calls.
- Different output constraints.
- Possible effects on accuracy and latency.

Avoid attributing the full accuracy difference solely to architecture.

## 6.5 Internal Validity

Assess whether experimental controls support the proposed interpretation of results.

Discuss confounding variables and uncontrolled differences.

## 6.6 Construct Validity

Assess whether the chosen metrics adequately represent:

- Determinism.
- Repeatability.
- Accuracy.
- Auditability.
- Validation.
- Overhead.

Identify metrics measured only through separate tests.

## 6.7 External Validity

Discuss the limitations of generalizing from:

- Ten independent paraphrases.
- A small graph.
- Boolean conditions.
- One local model.
- One development environment.

## 6.8 Reproducibility and Reliability

Discuss:

- Saved scripts and outputs.
- Model configuration.
- Prompt recording.
- Environment dependencies.
- Repetition limitations.
- Trace and artifact preservation.

## 6.9 Cybersecurity Engineering Relevance

Explain how explicit validation, controlled routing, and traceability may support safer workflow execution.

Do not claim a comprehensive security assessment was completed.

## 6.10 Contribution and Tradeoffs

Identify supported contributions:

- Structured semantic representation.
- Separation of interpretation and execution.
- Controlled routing outcomes.
- Traceable decision records.
- Comparative evaluation methodology.
- Evidence of both benefits and limitations.

Discuss the performance cost of fresh interpretation.

### Required Chapter 6 Table

**Table 6.1 — Threats to Validity and Mitigations**

Columns:

- Validity category.
- Threat.
- Observed relevance.
- Existing mitigation.
- Remaining limitation.

### Chapter 6 Completion Checks

- Conclusions follow from recorded evidence.
- Confounding variables are acknowledged.
- No unsupported causal claim is made.
- Limitations are specific.
- Cybersecurity claims remain within the evaluated scope.

---

# Chapter 7 — Conclusions and Future Work

**Suggested length:** 2–3 pages.

**Purpose:** Answer the research question and state the supported contribution of the completed work.

## 7.1 Research Summary

Briefly summarize the problem, prototype, and evaluation.

## 7.2 Answer to the Research Question

Provide a qualified answer based on the results.

Explain what improved in the tested scenarios and what remains uncertain.

## 7.3 Completion of the Five Research Objectives

Summarize the evidence for each objective.

Avoid declaring objectives universally achieved beyond the tested scope.

## 7.4 Principal Research Contributions

Identify:

- Implemented semantic-contract prototype.
- Deterministic condition and routing evaluation.
- Structured validation and trace recording.
- Comparative direct-versus-structured evaluation.
- Analysis of semantic interpretation errors and overhead.

## 7.5 Limitations

Briefly restate the most important boundaries affecting interpretation.

## 7.6 Future Work

Prioritize:

1. Stronger graph-level contract validation.
2. More expressive semantic schemas.
3. Independent semantic verification.
4. Larger and more diverse benchmarks.
5. Better-controlled prompt-equivalent comparisons.
6. Unified workflow-path and trace experiments.
7. Performance optimization and contract caching.
8. Evaluation across additional models and environments.

## 7.7 Final Conclusion

End with a concise, evidence-supported statement of the project's contribution.

Do not introduce new experimental results.

---

# C. References

Use the citation style required by the instructor or university.

Requirements:

- Verify every bibliographic entry.
- Ensure each in-text citation appears in the reference list.
- Ensure each listed source is actually used.
- Cite original sources when possible.
- Include software and technical documentation where appropriate.
- Do not invent missing publication details.
- Maintain consistent numbering and formatting.

A final citation audit is required.

---

# D. Appendices

The following appendix structure is proposed and may be refined to avoid unnecessary duplication.

## Appendix A — Proposal-to-Implementation Traceability

Include:

- Proposal migration summary.
- Original versus implemented scope.
- Work-package mapping.
- Milestone completion evidence.

## Appendix B — Implemented Architecture and Workflow

Include:

- Full architecture diagram.
- Workflow graph.
- Contract-processing sequence.
- Routing and trace schema.

## Appendix C — Semantic Contract and Validation Specifications

Include:

- Contract examples.
- Field definitions.
- Validation categories.
- Routing statuses.

## Appendix D — Evaluation Datasets and Oracle

Include:

- Scenario identifiers.
- Natural-language conditions.
- Workflow states.
- Expected destinations.
- Reference labels.

## Appendix E — Experimental Protocol and Configurations

Include:

- Model settings.
- Prompts or prompt references.
- Scripts.
- Repetition rules.
- Timing conditions.
- Deviations and approval status.

## Appendix F — Detailed Results and Error Records

Include:

- Extended result tables.
- Scenario-level outcomes.
- Interpretation failures.
- Timing breakdowns.

## Appendix G — Execution Trace Samples

Include:

- Representative successful trace.
- Representative no-match or ambiguous trace.
- Trace field explanations.

## Appendix H — Software Artifact and Reproducibility Guide

Include:

- Repository structure.
- Dependencies.
- Setup instructions.
- Model requirements.
- Commands for selected tests and experiments.
- Expected output locations.
- Known limitations.

## Appendix I — AI-Use Disclosure and Verification Log

Include:

- Actual AI-assisted activities.
- Student verification actions.
- Source and calculation checks.
- Authorship and responsibility statement.

---

# E. Final Figures and Tables Inventory

## Planned Figures

| Figure | Description | Chapter |
|---|---|---|
| 3.1 | Implemented semantic-contract architecture | 3 |
| 3.2 | Workflow state diagram | 3 |
| 3.3 | Routing and failure-handling sequence | 3 |
| 4.1 | Comparative evaluation workflow | 4 |
| 5.1 | Accuracy across separate comparisons | 5 |
| 5.2 | Repeated independent accuracy | 5 |
| 5.3 | Repeated independent execution time | 5 |
| 5.4 | Interpretation accuracy and stability | 5 |
| 5.5 | Scenario-level error summary | 5 |

Figures should be included only when they communicate useful information beyond the text or tables.

## Planned Tables

| Table | Description | Chapter |
|---|---|---|
| 1.1 | Research problem and objective traceability | 1 |
| 2.1 | Literature synthesis matrix | 2 |
| 2.2 | Related approaches | 2 |
| 3.1 | Requirements verification matrix | 3 |
| 3.2 | Semantic contract schema | 3 |
| 3.3 | Routing status definitions | 3 |
| 3.4 | Implemented components | 3 |
| 3.5 | Proposed versus actual implementation | 3 |
| 4.1 | Dataset inventory | 4 |
| 4.2 | Comparison controls | 4 |
| 4.3 | Evaluation metrics | 4 |
| 4.4 | Repetition protocol | 4 |
| 4.5 | Data collection evidence | 4 |
| 5.1 | Consolidated results | 5 |
| 5.2 | Repeated independent comparison | 5 |
| 5.3 | Semantic interpretation errors | 5 |
| 5.4 | Validation outcomes | 5 |
| 5.5 | Execution overhead | 5 |
| 5.6 | Objective-to-finding mapping | 5 |
| 6.1 | Threats to validity | 6 |

---

# F. Research Evidence and Source Mapping

| Research area | Main evidence |
|---|---|
| Original research question and objectives | Capstone I proposal; `docs/proposal_objective_alignment.md` |
| Contract representation | `src/semantic_contract.py` |
| Structural validation | `src/contract_validator.py` |
| Deterministic evaluation | `src/contract_evaluator.py` |
| Routing | `src/contract_router.py` |
| Workflow graph | `src/graph.py` |
| Ollama interpretation | `src/ollama_structured_interpreter.py` |
| Direct baseline | `src/direct_nl_llm_router.py` |
| Trace recording | `src/traced_contract_router.py`; `src/execution_trace.py` |
| Independent dataset | `src/independent_evaluation_dataset.py` |
| Repeated comparison | `src/test_repeated_matched_independent_nl.py` |
| Original matched results | `docs/matched_routing_comparison_results.json` |
| Matched NL results | `docs/fair_nl_comparison_results.json` |
| Independent results | `docs/matched_independent_nl_results.json` |
| Repeated independent results | `docs/repeated_matched_independent_nl_results.json` |
| Interpretation consistency | `docs/independent_interpretation_consistency_results.json` |
| Semantic consistency | `docs/independent_semantic_consistency_results.json` |
| Consolidated results | `docs/final_evaluation_results.md` |
| Reproduction instructions | `README.md`; `requirements.txt` |
| Professor requirements | CISC 699 Final Report Guide |

These paths are evidence references based on the reviewed project records. Final file existence, content, and version checks are still required.

---

# G. Final Quality and Submission Audit

## G.1 Research Alignment

- [ ] Research question preserved.
- [ ] Five objectives addressed.
- [ ] Scope and deviations documented.
- [ ] Contributions supported by evidence.
- [ ] No unsupported novelty claims.

## G.2 Technical Accuracy

- [ ] Architecture matches actual code.
- [ ] Contract schema matches implementation.
- [ ] Validation limitations are stated.
- [ ] Routing behavior is correctly described.
- [ ] Trace behavior is verified.
- [ ] Environment and dependencies are accurate.

## G.3 Experimental Accuracy

- [ ] Dataset sizes verified.
- [ ] Expected-route labels verified.
- [ ] Accuracy calculations independently checked.
- [ ] Repetition counts verified.
- [ ] Timing units and measurement boundaries explained.
- [ ] Prompt differences disclosed.
- [ ] Stable incorrect outcomes discussed.
- [ ] Separate experiments not combined improperly.

## G.4 Academic Quality

- [ ] Literature claims have verified citations.
- [ ] Reference list is complete and consistent.
- [ ] Figures and tables are accurate and captioned.
- [ ] Terminology is consistent.
- [ ] Limitations and validity threats are discussed.
- [ ] AI-use disclosure reflects actual activities.
- [ ] No fabricated results or approvals.

## G.5 Reproducibility

- [ ] Software artifact version recorded.
- [ ] Setup instructions verified.
- [ ] Model requirements documented.
- [ ] Experiment scripts identified.
- [ ] Raw result files preserved.
- [ ] Representative reproduction commands tested.
- [ ] Known errors and limitations documented.

## G.6 Final Presentation and Handoff

- [ ] Final DOCX report prepared.
- [ ] Final PDF report prepared if required.
- [ ] Software package prepared.
- [ ] Evidence archive prepared.
- [ ] Artifact manifest prepared.
- [ ] Final presentation prepared.
- [ ] Demonstration tested.
- [ ] Submission requirements confirmed.
- [ ] Submitted files open correctly.
- [ ] Submission confirmation retained.

---

# H. Report Preparation Sequence

The recommended writing sequence is:

1. Complete the evidence and source audit.
2. Draft Chapter 3 — Solution Design and Implementation.
3. Draft Chapter 4 — Evaluation Methodology.
4. Draft Chapter 5 — Results and Analysis.
5. Draft Chapter 6 — Discussion and Validity.
6. Draft Chapter 1 — Introduction and Problem Definition.
7. Update and draft Chapter 2 — Literature Review.
8. Draft Chapter 7 — Conclusions and Future Work.
9. Verify references and appendices.
10. Write the abstract.
11. Apply final Word formatting.
12. Perform technical, academic, and submission audits.

This sequence prioritizes actual implementation and experimental evidence before finalizing broad research claims.

The report will ultimately be arranged in the required Chapter 1–7 order, regardless of drafting order.

---

# I. Current Readiness Assessment

**Research foundation:** Substantially prepared.

**Implemented prototype:** Substantially developed for the tested workflow.

**Experimental evidence:** Multiple completed experiments with recorded findings.

**Report outline:** Prepared.

**Final literature verification:** Pending.

**Final protocol and reproducibility audit:** Pending.

**Final seven-chapter report:** Not yet written.

**Final software and evidence package:** Not yet finalized.

**Submission readiness:** Not yet established.

**Quality objective:** Produce a technically accurate, evidence-supported, reproducible, professionally formatted final report aligned with the instructor's CISC 699 guide and suitable for rigorous graduate-level assessment.