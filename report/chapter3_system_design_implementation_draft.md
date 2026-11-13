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
