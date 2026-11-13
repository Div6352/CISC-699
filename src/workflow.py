
# CISC 699 - A2 Research Project
# First deterministic graph-based workflow

def execute_workflow(tests_passed):
    print("Starting workflow...")
    print("Node: Check Tests")

    if tests_passed:
        print("Edge: Tests passed")
        print("Next Node: Deploy Code")
    else:
        print("Edge: Tests failed")
        print("Next Node: Fix Code")

    print("Workflow completed.")


# Example workflow execution
execute_workflow(False)
