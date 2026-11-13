
# CISC 699 - A2 Research Project
# Natural-Language Contract Builder Test

from nl_contract_builder import build_contract
from natural_language_graph import natural_language_edges

print("\nA2 Research - NL Contract Builder Test")

# Build contracts from natural-language edges
contracts = []

for edge in natural_language_edges:
    contract = build_contract(edge)

    print("Edge:", edge["edge_id"])
    print("Generated contract:", contract)

    assert contract is not None

    contracts.append(contract)

# Verify the generated conditions
assert contracts[0]["condition"] == {
    "field": "tests_passed",
    "operator": "equals",
    "value": True
}

assert contracts[1]["condition"] == {
    "field": "tests_passed",
    "operator": "equals",
    "value": False
}

print("Both natural-language contracts created successfully!")
