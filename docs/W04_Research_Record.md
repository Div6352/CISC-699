# Week 04 â€” Design and requirements traceability Research Record

**Course:** CISC 699 â€” Capstone II
**Project:** A2 â€” Natural-Language Edge Semantics and Deterministic Agent Execution
**Scheduled week:** November 16â€“22, 2026
**Work packages:** WP03, WP02
**Status:** IN PROGRESS - early preparation began November 13, 2026

## Objective and planned work
Refine natural-language input, workflow context, LLM interpretation, semantic contract, validation, deterministic evaluation, routing and trace interfaces. Map requirements to components and tests.

## Actual work performed
**November 13, 2026:** Reviewed implementation source code and existing tests; prepared architecture, interface, and requirements traceability drafts. Created a design decisions and open issues record. No new Week 4 runtime tests were executed.

## Evidence and deliverables to retain
**Planned:** Architecture diagram; schema/interface draft; requirements-to-tests traceability matrix; design decisions and unresolved semantics.
**Actual paths:** docs/W04_System_Architecture_Draft.md; docs/W04_System_Architecture_Diagram.md; docs/W04_Requirements_Traceability_Draft.md; docs/W04_Interface_Specification_Draft.md; docs/W04_Design_Decisions.md. All five drafts were verified to exist.

## Verification and observations
**Planned check:** Review requirements against proposal Chapters 1â€“4 and record M2/M3 status with supporting files.
**Observed results and blockers:** Reviewed implementation source and existing test files; no new Week 4 runtime tests executed. Test coverage and proposal Chapters 1–4 alignment still require verification. M2/M3 definitions and completion evidence remain unverified.

## Methodological caution
Do not mark design ready until interfaces and routing responsibilities are explicit.

## AI assistance and independent verification
**AI assistance:** ChatGPT assisted with documentation drafts and source-code review. The student inspected source files and verified the saved drafts. No new Week 4 runtime tests were executed.

## Next action and report contribution
W05: implement and pilot the minimum end-to-end path. **Report linkage:** PENDING â€” record chapter/section and supported claims after verification.
**Draft deliverables:** docs/W04_System_Architecture_Draft.md; docs/W04_System_Architecture_Diagram.md; docs/W04_Requirements_Traceability_Draft.md; docs/W04_Interface_Specification_Draft.md.
**Remaining:** Verify test coverage, review design decisions, check proposal alignment, and confirm M2/M3 status. Week 4 is not yet complete.
**AI assistance:** ChatGPT helped draft documentation and review code. The student verified saved files and inspected source code; no new Week 4 tests were run.
**Design review:** Created and verified docs/W04_Design_Decisions.md with three decisions and three unresolved issues.
**M2/M3 review:** Milestone definitions and completion evidence not yet verified; status remains pending.
**O2 test review:** Inspected test_contract_validator.py and test_contract_evaluator.py; confirmed four validation scenarios and ten repeated evaluation checks in source code. Tests not executed during Week 4.
**O3 test review:** Inspected test_ollama_workflow_integration.py; verified source-code assertions for Ollama contract generation, validation, both routing outcomes, ten repeated decisions, and twelve unique saved traces. Not executed during Week 4.
**O3 graph review:** Inspected seven graph-transition test scenarios. The test uses a separate example graph and local permission function; production graph enforcement is not directly tested here. Not executed during Week 4.
**O4 review:** Inspected repeated comparison code for accuracy, timing, interpretation correctness, and repeated-decision consistency. Prompt guidance and model-call counts differ. No new experiment executed.
**O5 repeatability review:** Inspected two workflow scenarios with ten repetitions each. Initial transition is fixed; contracts are manually defined. Test not executed during Week 4.
**O5 trace review:** Inspected nine trace-field checks, routing outcome, matched contract, validation results, and explanation. This test does not verify file persistence or repeated traces. Not executed during Week 4.
**O5 timing review:** Inspected timing code for Ollama contract construction, two deterministic routing scenarios, and combined elapsed time. No direct LLM baseline or trace-saving measurement. Not executed during Week 4.
**Proposal alignment review:** Reviewed O1-O5 limitations in docs/proposal_objective_alignment.md. All five objectives have identified implementation and evidence; schema scope, prompt comparability, and separate evaluation datasets remain qualifications. Final report alignment remains pending.
**M2/M3 verification:** Week 2 record reports the 13-week schedule and work-plan submission (95/100), but the original planning documents were not found in the project PDF/DOCX search. Exact M2/M3 definitions and completion remain unverified.
**Report linkage:** Chapter 3 Sections 3.2-3.9 and 3.12 cover requirements, architecture, contracts, routing, and traces; Chapter 4 Sections 4.5-4.11 cover evaluation methods and limitations. Section headings verified; detailed consistency review remains pending.
**M2/M3 source verification:** Original 13-week schedule and individual work plan reviewed. M2 = Requirements reviewed; M3 = Design documented; both target Week 4. Existing architecture, interface, traceability, and design-decision drafts provide supporting evidence. Final acceptance review remains pending.
