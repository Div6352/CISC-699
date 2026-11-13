# Week 4 - Interface Specification
## Semantic Contract: edge_id, source, target, condition (field, operator, value).
## Validation: source and target must be nonempty strings; condition must use tests_passed, equals, and a Boolean value.
## Evaluation: compare workflow_data.tests_passed with the contract Boolean value; return True or False.
## Routing: select the target only when exactly one outgoing contract matches; otherwise return no match or ambiguity.
## Routing statuses: ROUTED, NO_MATCH, AMBIGUOUS, INVALID_CONTRACT, INVALID_WORKFLOW_DATA; traced routing can also return INVALID_GRAPH_TRANSITION.
## Execution tracing: record routing status, selected node, matched contracts, validation results, explanation, timestamp, and unique trace ID in JSON.
