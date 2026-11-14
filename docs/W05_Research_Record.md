# Week 5 - Prototype and Pilot Research Record

**Started early:** November 13, 2026
**Scheduled week:** November 30 - December 6, 2026

## Prototype Status
Existing natural-language interpretation, semantic contract validation, deterministic routing, graph permission enforcement, and JSON execution tracing components were reused.

## Pilot Integration Result
**PASS** - Ollama workflow integration test verified both Boolean routing outcomes, repeated deterministic decisions, automatic trace saving, and unique trace identifiers.

## Scope and Limitations
This was an early integration pilot, not the formal Week 9 controlled evaluation. Trace files were saved in a temporary directory and removed when the test completed.

## Remaining Week 5 Work
Review the pilot scenario coverage, baseline readiness, and any implementation limitations before finalizing Week 5.

## Direct-LLM Baseline Readiness
Code review confirmed that original direct-LLM, prompt-controlled direct-LLM, and structured-contract comparison methods are implemented. The existing comparison records accuracy, consistency, timing, and LLM-call counts. No new comparison experiment was executed during this Week 5 review. Formal controlled evaluation remains scheduled for Week 9.

## Known Comparison Limitations
The dataset covers ten paraphrases of one Boolean condition. Direct methods use one LLM call per decision, while the structured method uses two. Structured contracts are regenerated each repetition. Prompt constraints differ, and execution order may affect timing.

## Pilot Scenario Coverage
Source review confirmed ten independent natural-language scenarios: five passing-test conditions and five failing-test conditions. All represent variations of one Boolean workflow rule. The existing Ollama integration pilot passed, but the ten-case dataset was not rerun during this Week 5 checkpoint. Coverage of complex conditions and other workflow types remains unverified.
