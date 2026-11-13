# CISC 699 Capstone II — Proposal Migration Audit

**Project:** A2 — Natural-Language Edge Semantics and Deterministic Agent Execution

**Original proposal:** *Designing Structured Natural-Language Edge Semantics for Deterministic Agent Execution in Graph-Based Autonomous Software Development Workflows*

**Course transition:** GRAD 695 Capstone I to CISC 699 Capstone II

**Primary guidance:** CISC 699 Final Report Guide, Section 2, “Reuse the approved proposal”

**Audit status:** Initial migration plan. Final source verification, code audit, approval checks, and report review remain pending.

## 1. Purpose

This audit maps the original Capstone I proposal to the seven-chapter Capstone II final report required by the instructor's guide.

It identifies which proposal sections should be retained, updated, relocated, replaced, or removed, and specifies the evidence required before the final report can make claims about completed work.

The submitted Capstone I proposal must remain unchanged as an archived source document.

## 2. Migration Classification

- **Retain:** Preserve content whose claims and citations remain accurate.
- **Update:** Revise content to reflect actual implementation, research findings, and verified sources.
- **Relocate:** Move relevant material to a different final-report chapter or appendix.
- **Replace:** Substitute proposed or expected content with observed implementation or evaluation evidence.
- **Remove:** Exclude duplicated, unsupported, obsolete, or unnecessary content from the final narrative while retaining the original proposal in the archive.

A classification does not authorize copying text without reviewing its accuracy and citations.

## 3. Final Report Structure

The final report will follow the instructor's seven-chapter structure:

1. Introduction and Problem Definition
2. Literature Review and Foundation
3. Solution Design and Implementation
4. Evaluation Methodology
5. Results and Analysis
6. Discussion and Validity
7. Conclusions and Future Work

The instructor's suggested main-text range is 28–44 pages, excluding preliminary pages, references, and appendices. This is guidance rather than a fixed quality threshold.

## 4. Preliminary Pages Migration

| Proposal material | Final destination | Action | Required change |
|---|---|---|---|
| Title page | Final title page | Update | Change course, submission details, and artifact information |
| AI-use disclosure | Final preliminary pages or appendix | Update | Accurately describe assistance used during Capstone II |
| Proposal abstract | Final abstract | Replace | Summarize actual implementation, results, limitations, and contribution |
| Table of contents | Final contents | Replace | Generate from final seven-chapter structure |
| Lists of figures and tables | Final preliminary pages | Update | Include actual final-report visuals and captions |
| Abbreviations | Final preliminary pages | Update | Retain relevant terms and remove unused entries |

The final abstract should be 200–300 words and written after the main chapters have been verified.

## 5. Chapter 1 Migration — Introduction and Problem Definition

**Original source:** Capstone I Chapter 1, Sections 1.1–1.20.

**Final destination:** Capstone II Chapter 1.

| Original sections | Action | Migration decision |
|---|---|---|
| 1.1–1.5 Background, software engineering, workflows, graph execution, and natural-language edges | Retain and update | Preserve relevant technical context with verified citations |
| 1.6 Problem Statement | Retain and update | Keep the specific problem and align its wording with the completed study |
| 1.7 Research and Practice Gap | Update | Check that literature supports each gap claim |
| 1.8 Research Question | Retain | Preserve the original question unless an approved change is documented |
| 1.9 Research Objectives | Retain | Preserve the five original objectives and connect them to evidence |
| 1.10–1.13 Purpose, significance, conceptual framework, cybersecurity relevance | Update | Explain the completed study without exaggerating general applicability |
| 1.14–1.17 Scope, delimitations, assumptions, constraints | Update | Distinguish original plans from actual experimental scope |
| 1.18–1.19 Expected artifact and workflow | Relocate and replace | Summarize the implemented artifact in Chapter 1 and explain it fully in Chapter 3 |
| 1.20 Chapter Summary | Replace | Summarize the final Chapter 1 |

### Evidence Required

- Original proposal Chapter 1.
- `docs/proposal_objective_alignment.md`
- Implemented workflow and contract source files.
- Verified literature supporting the research gap.
- Documented scope changes and their approval status, if any.

### Status

**Ready for drafting with source verification.**

The research question and objectives are documented. Final literature support and scope wording still require review.

## 6. Chapter 2 Migration — Literature Review and Foundation

**Original source:** Capstone I Chapter 2.

**Final destination:** Capstone II Chapter 2.

| Original material | Action | Migration decision |
|---|---|---|
| Literature search strategy | Update | Record actual search sources, dates, terms, and selection criteria |
| Autonomous software-engineering agents | Retain and update | Preserve supported background and relevant research |
| Graph-based workflow orchestration | Retain and update | Connect prior work to the implemented workflow |
| Natural-language reasoning and decision making | Retain and update | Explain interpretation uncertainty and related research |
| Reliability, observability, and explainability | Retain and update | Connect literature to routing and tracing decisions |
| Structured edge semantics and deterministic execution | Retain and update | Explain the technical foundation of the project |
| Existing approach comparisons | Update | Relate prior approaches to the direct-routing baseline and structured prototype |
| Research gap synthesis | Update | State only gaps supported by the verified literature |

### Evidence Required

- Original proposal references.
- Original publications or authoritative technical documentation.
- Updated literature search record.
- Source-to-claim verification.
- Design decisions linked to literature findings.

### Status

**Requires citation and literature-update audit before finalization.**

The proposal provides a foundation, but citations must not be accepted without verification.

## 7. Chapter 3 Migration — Solution Design and Implementation

**Original source:** Capstone I Chapter 3 and relevant portions of Chapter 5.

**Final destination:** Capstone II Chapter 3.

| Original sections or topics | Action | Migration decision |
|---|---|---|
| 3.1–3.3 Solution overview and design goals | Update | Describe the implemented solution |
| 3.4 Natural-Language Edge Model | Update | Describe actual supported edge conditions |
| 3.5 Structured Semantic Contract | Update | Document the implemented contract fields and schema limitations |
| 3.6 Semantic Interpretation Layer | Replace proposed details | Explain the actual Ollama interpreter, model configuration, inputs, and outputs |
| 3.7 Semantic Validation Layer | Update | Separate implemented structural validation from oracle-based semantic checks |
| 3.8–3.10 Deterministic evaluation and evaluator architecture | Consolidate and update | Explain actual evaluator and router behavior without duplicated sections |
| 3.11 Workflow Execution Model | Update | Describe implemented transitions and tested integration |
| 3.12 Execution Trace Design | Update | Describe actual JSON trace fields and persistence behavior |
| 3.13 Baseline Architecture | Update | Describe the implemented direct LLM baseline |
| 3.14–3.15 Prototype and requirements | Update | Connect actual requirements to components and tests |
| 3.16 Failure Traceability | Update | Report tested no-match, ambiguity, validation, and graph-transition outcomes |
| 3.17 Cybersecurity Considerations | Update | Describe supported controls and clearly state untested security properties |
| 3.18–3.20 Data model and execution sequence | Replace proposed diagrams | Use implemented data structures and verified architecture diagrams |
| 3.21–3.27 Implementation strategy, decisions, advantages, limitations, summary | Update and consolidate | Explain actual implementation choices, deviations, tradeoffs, and limitations |
| Capstone I Chapter 5 implementation work packages | Relocate | Summarize actual-versus-planned work; preserve detailed plan in an appendix |

### Implementation Evidence

- `src/semantic_contract.py`
- `src/contract_validator.py`
- `src/contract_evaluator.py`
- `src/contract_router.py`
- `src/graph.py`
- `src/ollama_structured_interpreter.py`
- `src/direct_nl_llm_router.py`
- `src/traced_contract_router.py`
- `src/execution_trace.py`
- `src/test_ollama_workflow_integration.py`
- `README.md`
- `requirements.txt`
- Relevant component test records.

### Known Boundaries

The contract schema is limited to supported Boolean conditions.

The individual validator does not enforce every graph-level constraint.

A structurally valid contract can still contain a semantically incorrect interpretation.

Graph-transition enforcement is performed separately in the traced routing wrapper.

The prototype is not a production-scale autonomous software-development system.

### Status

**Substantial implementation evidence exists; final source-code and architecture audit remain pending.**

## 8. Chapter 4 Migration — Evaluation Methodology

**Original source:** Capstone I Chapter 4.

**Final destination:** Capstone II Chapter 4.

| Original sections | Action | Migration decision |
|---|---|---|
| 4.1–4.3 Evaluation purpose, design, and experimental context | Update | Describe the actual study and its boundaries |
| 4.4 Experimental workflow and architecture | Update | Explain the implemented comparison process |
| 4.5 Scenario Construction | Update | Describe original states and independent paraphrase cases |
| 4.6 Expected-Route Oracle | Update | Explain expected-route labels and their validation status |
| 4.7 Baseline, proposed system, and fair comparison | Update | Document actual prompts, model calls, and comparability limitations |
| 4.8 Data sources, collection, and metrics | Update | Define actual datasets, repetitions, calculations, and timing measurements |
| 4.9 Analysis and methodological limitations | Update | Explain interpretation of results and threats to validity |
| 4.10 Chapter Summary | Replace | Summarize the completed methodology |

### Evidence Required

- `src/independent_evaluation_dataset.py`
- `src/test_repeated_matched_independent_nl.py`
- `docs/matched_routing_comparison_results.json`
- `docs/fair_nl_comparison_results.json`
- `docs/matched_independent_nl_results.json`
- `docs/repeated_matched_independent_nl_results.json`
- `docs/independent_interpretation_consistency_results.json`
- `docs/independent_semantic_consistency_results.json`
- Exact model configuration, prompts, scripts, and environment details.
- Documented expected-route oracle.
- Any protocol approvals, deviations, and version records.

### Methodological Qualifications

The structured interpreter received additional Boolean interpretation guidance compared with the direct baseline.

The methods used different numbers of LLM calls.

Experiments that reused contracts must be distinguished from experiments that regenerated contracts.

Repeated decision stability must not be described as proof of correctness.

The repeated independent routing experiment did not measure complete workflow paths or persisted execution traces.

The individual research plan schedules formal evaluation for January 2027. Earlier recorded experiments must not be labeled as the formally approved evaluation without checking the protocol and instructor decisions.

### Status

**Experimental procedures and data exist; final protocol, oracle, and reproducibility audit remain pending.**

## 9. Chapter 5 Migration — Results and Analysis

**Original source:** No completed results chapter in the Capstone I proposal.

**Final destination:** New Capstone II Chapter 5.

**Action:** Create new content from recorded experimental evidence.

### Planned Sections

- 5.1 Evaluation overview and reporting conventions.
- 5.2 Component verification results.
- 5.3 Initial natural-language interpretation baseline.
- 5.4 Original matched routing comparisons.
- 5.5 Independent natural-language comparison.
- 5.6 Interpretation consistency and semantic correctness.
- 5.7 Repeated matched independent comparison.
- 5.8 Workflow-path repeatability, validation, and tracing.
- 5.9 Execution overhead and timing interpretation.
- 5.10 Error analysis and objective-level findings.

### Principal Recorded Result

The repeated matched independent experiment contains ten cases repeated three times.

- Direct LLM routing: 15 correct decisions out of 30, or 50%.
- Structured contract routing: 24 correct decisions out of 30, or 80%.
- Both methods produced identical repeated decisions within all ten cases.
- Direct total measured time: approximately 89.53 seconds.
- Structured total measured time: approximately 253.51 seconds.
- The structured method took approximately 2.83 times as long when fresh contracts were generated for each repetition.

These results must be reported with the correct experimental denominator and conditions.

### Evidence Required

- `docs/final_evaluation_results.md`
- Original experiment JSON files.
- Experiment scripts and model configurations.
- Raw-run records and calculation checks.
- Graphs or tables generated from verified data.
- Scenario-level error analysis.

### Status

**Ready for an evidence-based draft, subject to final verification of raw data and calculations.**

## 10. Chapter 6 Migration — Discussion and Validity

**Original sources:** Capstone I Chapters 3, 4, and 6.

**Final destination:** Capstone II Chapter 6.

**Action:** Update and replace expected advantages with supported interpretations.

### Planned Sections

- 6.1 Interpretation of findings.
- 6.2 Relationship to the original research question.
- 6.3 Structured routing benefits within the tested scope.
- 6.4 Interpretation errors and limitations of deterministic evaluation.
- 6.5 Fairness and construct validity.
- 6.6 Internal, external, and reproducibility validity.
- 6.7 Execution overhead and design tradeoffs.
- 6.8 Cybersecurity engineering implications and boundaries.

### Required Distinctions

Higher expected-route accuracy does not establish universal superiority.

Stable decisions can be incorrect.

Deterministic evaluation does not correct semantically incorrect contracts.

The recorded benchmark does not prove general production reliability, safety, or security.

### Status

**Can be drafted from recorded findings after methodological verification.**

## 11. Chapter 7 Migration — Conclusions and Future Work

**Original source:** Capstone I Chapter 6, Expected Contributions and Conclusion.

**Final destination:** Capstone II Chapter 7.

| Original material | Action | Migration decision |
|---|---|---|
| 6.1 Proposal Summary | Update | Summarize the completed study |
| 6.2 Expected Artifact or Research Outcome | Replace | Describe the actual implemented artifact |
| 6.3 Expected Contribution to Practice | Update | State supported practical contributions |
| 6.4 Expected Contribution to Knowledge | Update | State supported research contributions |
| 6.5 Anticipated Limitations | Replace | Report observed limitations |
| 6.6 Readiness for Capstone II | Remove from final narrative | This was a proposal-stage statement |
| 6.7 Conclusions | Replace | Answer the original research question using actual findings |

### Possible Future Work

Future work may include:

- More expressive semantic condition schemas.
- Stronger graph-level validation.
- Independent semantic verification.
- Larger and more diverse evaluation datasets.
- Prompt-equivalent baseline comparisons.
- Complete workflow-path and trace evaluation within a unified benchmark.
- Further performance optimization.

These items are future research directions, not completed features.

### Status

**Conclusion can be drafted after Chapters 3–6 are verified.**

## 12. Capstone I Execution Plan Migration

**Original source:** Capstone I Chapter 5.

**Final destination:** Chapter 3 implementation summary and Appendix A.

The original plan should be preserved as historical project documentation.

The final report must compare actual activities against planned work packages WP01–WP11 and milestones M1–M11.

The 13-week individual plan provides the scheduled research stages and expected evidence records.

Completion must be based on verified activities rather than the existence of a planned milestone.

### Required Evidence

- Individual 13-week research schedule.
- Individual research work plan.
- Completed research records.
- Implementation and test evidence.
- Experimental outputs.
- Version or configuration records.
- Presentation and submission confirmation when available.

### Status

**Initial mapping possible; final milestone and approval audit pending.**

## 13. References and Appendices Migration

| Original material | Action | Final treatment |
|---|---|---|
| Capstone I references | Verify and update | Retain only sources actually used and verified |
| Literature synthesis matrix | Update | Include a verified version where useful |
| Proposed architecture diagrams | Replace | Use implemented architecture and workflow diagrams |
| Proposed data instruments | Update | Include instruments and schemas actually used |
| Proposed evaluation protocol | Update | Document actual protocol and deviations |
| Original project schedule | Archive | Preserve as planning evidence |
| Scenario examples | Update | Include actual evaluated scenarios and labels |
| AI-use disclosure | Update | Reflect Capstone II activities accurately |
| Proposal-to-presentation traceability | Update | Link actual results and final presentation |

The final report should also include a software and evidence handoff appropriate to the professor's guide.

## 14. Objective-to-Final-Chapter Traceability

| Original objective | Primary final-report chapters | Required evidence |
|---|---|---|
| Objective 1: Examine natural-language interpretation | Chapters 3, 4, 5, 6 | Interpreter implementation and interpretation experiments |
| Objective 2: Develop structured semantic representation | Chapters 3, 5 | Contract schema, validator, evaluator, component tests |
| Objective 3: Implement controlled prototype | Chapter 3 | Source code, integration tests, architecture |
| Objective 4: Compare against direct natural-language routing | Chapters 4, 5 | Baseline, structured approach, matched comparison results |
| Objective 5: Assess consistency, paths, accuracy, traces, validation, overhead | Chapters 4, 5, 6 | Metric definitions, raw results, trace tests, timing, limitations |

Each objective must be addressed explicitly in the final discussion or conclusion.

## 15. Outstanding Verification Register

| ID | Verification item | Current status |
|---|---|---|
| V01 | Confirm exact professor/institution formatting requirements | Pending final check |
| V02 | Verify all retained literature citations against original sources | Pending |
| V03 | Audit implemented code against Chapter 3 claims | Pending final audit |
| V04 | Verify protocol, oracle, prompts, and comparison fairness | Pending |
| V05 | Recalculate reported experimental results from raw files | Pending final audit |
| V06 | Verify full trace records and component-test evidence | Pending final audit |
| V07 | Confirm approval status of any research scope or protocol changes | Not established |
| V08 | Prepare final artifact and evidence manifest | Pending |
| V09 | Prepare seven-chapter report and final abstract | Pending |
| V10 | Prepare presentation, demonstration, and submission package | Pending |

An item marked pending must not be described as verified or approved.

## 16. Migration Decision Summary

The original Capstone I proposal provides the research foundation for the Capstone II final report.

Its research question, five objectives, and supported literature context should be preserved.

Its proposed architecture, methodology, execution plan, and expected contributions must be transformed into accurate accounts of implemented components, actual experiments, observed results, documented deviations, and limitations.

The Capstone II final report will therefore use seven chapters as required by the instructor's guide, with a new results chapter and separate discussion and conclusion chapters.

**Audit conclusion:** The project has substantial material for drafting the final report. Submission readiness remains conditional on the verification register, complete report preparation, and final software/evidence handoff.