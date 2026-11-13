
# CISC 699 - A2 Research Project
# Structured Workflow Graph and Transition Validation

# Define the workflow nodes.
nodes = [
    "Check Tests",
    "Fix Code",
    "Deploy Code"
]

# Define the permitted workflow connections.
edges = [
    {
        "source": "Check Tests",
        "target": "Deploy Code",
        "condition": "tests_passed == True"
    },
    {
        "source": "Check Tests",
        "target": "Fix Code",
        "condition": "tests_passed == False"
    }
]


def is_permitted_transition(source, target):
    """
    Return True only when both nodes exist
    and the directed transition is in the graph.
    """

    if source not in nodes or target not in nodes:
        return False

    return any(
        edge["source"] == source
        and edge["target"] == target
        for edge in edges
    )


if __name__ == "__main__":
    print("A2 Research - Graph Structure")

    print("\nWorkflow Nodes:")
    for node in nodes:
        print("-", node)

    print("\nWorkflow Edges:")
    for edge in edges:
        print(
            edge["source"],
            "->",
            edge["target"],
            "| Condition:",
            edge["condition"]
        )
