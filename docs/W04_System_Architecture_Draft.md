# Week 4 - A2 System Architecture Draft

**Course:** CISC 699 - Capstone II
**Project:** A2 - Natural-Language Edge Semantics and Deterministic Agent Execution
**Status:** Draft based on source-code inspection

## Architecture Overview
The prototype separates natural-language interpretation, semantic contract construction, contract validation, deterministic evaluation, workflow routing, graph transition enforcement, and execution tracing.

## Components and Interfaces
- natural_language_graph.py: Defines three workflow nodes and two natural-language edges.
- nl_interpreter.py: Recognizes two predefined conditions; returns a structured condition or None.
- nl_contract_builder.py: Builds and validates contracts using the rule-based interpreter.
- ollama_interpreter.py: Uses local llama3.2:3b with JSON-mode output and Python validation.
- ollama_structured_interpreter.py: Uses local llama3.2:3b with schema-constrained output and Python validation.
- contract_validator.py: Validates contract structure and the supported Boolean condition.
- contract_evaluator.py: Evaluates a valid contract against workflow data.
- contract_router.py: Selects a destination only when exactly one outgoing contract matches.
- graph.py: Defines permitted directed transitions and checks node membership.
- traced_contract_router.py: Enforces graph permissions and coordinates trace creation and saving.
- execution_trace.py: Creates structured decision records and saves JSON using temporary-file replacement.

## Verified Execution Responsibilities
Natural-language interpretation produces a condition. A semantic contract contains edge_id, source, target, and condition. The deterministic router validates contracts, evaluates outgoing conditions, and reports routing outcomes. The traced router rejects unauthorized graph transitions and saves an execution record.

## Design Constraints and Open Questions
- The inspected contract builder uses the rule-based interpreter, not the Ollama interpreters.
- Full LLM-to-contract-to-routing integration has not yet been established from the inspected files.
- The current validator supports tests_passed with the equals operator and a Boolean value.
- The contract builder requires an edge_id key, although the validator permits that field to be absent.
- Structural validity does not establish semantic interpretation accuracy.
- Additional requirements traceability and interface review remain pending.

## Evidence
Source files inspected: src/natural_language_graph.py, src/nl_interpreter.py, src/nl_contract_builder.py, src/ollama_interpreter.py, src/ollama_structured_interpreter.py, src/semantic_contract.py, src/contract_validator.py, src/contract_evaluator.py, src/contract_router.py, src/graph.py, src/workflow.py, src/traced_contract_router.py, and src/execution_trace.py.

No new Week 4 runtime tests are claimed in this draft.
