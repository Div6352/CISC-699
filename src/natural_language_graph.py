
# CISC 699 - A2 Research Project
# Natural-Language Graph Definition

nodes = [
    "Check Tests",
    "Fix Code",
    "Deploy Code"
]

natural_language_edges = [
    {
        "edge_id": "E01",
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": "If all software tests have passed, proceed to deployment."
    },
    {
        "edge_id": "E02",
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": "If any software test has failed, return to fixing the code."
    }
]

print("A2 Research - Natural-Language Graph")

for edge in natural_language_edges:
    print("Edge ID:", edge["edge_id"])
    print("From:", edge["source"])
    print("To:", edge["target"])
    print("Condition:", edge["condition"])
    print("-----------------------------")
