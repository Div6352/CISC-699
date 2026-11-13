# Week 3 - Research Progress Record

**Course:** CISC 699 - Capstone II
**Project:** A2 - Natural-Language Edge Semantics and Deterministic Agent Execution
**Week:** November 9-15, 2026
**Work Packages:** WP01, WP02, WP05
**Status:** Week 3 technical milestones verified; documentation review pending

## Objective
Verify the development environment, runtime, model access, safety checks, execution logging, and controlled comparison protocol.

## Activities and Results
Verified Python 3.14.1, the project virtual environment, and the standard-library dependency manifest. Ollama 0.40.14 and locally installed llama3.2 models were checked; llama3.2:3b successfully returned READY during a smoke test.

Individually executed research scripts verified contract evaluation, validation, routing, graph restrictions, and execution tracing. Recorded results include 7/7 permitted-transition checks, 4/4 duplicate-edge checks, 4/4 node-membership checks, 12/12 extended-validation checks, and 8/8 missing-workflow-data checks. These results apply to the tested scenarios, not the entire test collection.

Initialized local Git version control and created commits 6a5bcdb and b3947db. Prepared docs/W03_Controlled_Comparison_Protocol_Draft.md to define matched comparison conditions, recorded outcomes, fairness considerations, and timing boundaries.

## Evidence and Limitations
Detailed checks are preserved in docs/W03_Detailed_Verification_Log.md. Existing experiment results remain preliminary; formal controlled evaluation is scheduled for Week 9. Not all standalone test scripts were executed, and the comparison protocol has not received independent approval.

## AI Assistance and Next Steps
ChatGPT assisted with terminal guidance and documentation drafting; the researcher checked reported outputs. Week 4 will address system architecture and requirements traceability.
