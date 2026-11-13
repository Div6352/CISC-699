
# CISC 699 - A2 Research Project
# End-to-End Natural-Language Workflow Test

from natural_language_graph import natural_language_edges
from nl_contract_builder import build_contract
from contract_router import select_next_node_from_contracts

# Convert English-language edges into contracts
contracts = []

for edge in natural_language_edges:
    contract = build_contract(edge)

    assert contract is not None
    contracts.append(contract)

print("\nA2 Research - End-to-End Workflow Test")

# Scenario 1: All tests passed
result1 = select_next_node_from_contracts(
    contracts,
    "Check Tests",
    {"tests_passed": True}
)

print("Tests passed ->", result1)

# Scenario 2: Tests failed
result2 = select_next_node_from_contracts(
    contracts,
    "Check Tests",
    {"tests_passed": False}
)

print("Tests failed ->", result2)

# Verify both routing decisions
assert result1 == "Deploy Code"
assert result2 == "Fix Code"

print("End-to-end workflow test passed!")
