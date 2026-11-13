# CISC 699 — Capstone II A2 Research

## Natural-Language Edge Semantics and Deterministic Agent Execution

### Project Overview

This research investigates the use of structured semantic contracts to represent natural-language workflow edge conditions and support deterministic routing in graph-based autonomous software development workflows.

The prototype separates two operations:

1. **Natural-language interpretation:** A local language model converts an edge condition into a structured Boolean condition.
2. **Deterministic execution:** A Python routing component validates and evaluates structured contracts against workflow state to select a permitted next node.

The project evaluates expected-route accuracy, decision consistency, workflow-path repeatability, contract validation, execution tracing, and execution overhead.

This is a controlled research prototype rather than a production-ready autonomous software development platform.

## 1. Research Objectives

The project addresses five objectives developed in the Capstone I proposal:

1. Examine natural-language edge interpretation in graph-based autonomous development workflows.
2. Develop a structured semantic representation for workflow conditions and transitions.
3. Implement a prototype separating natural-language interpretation from deterministic transition evaluation.
4. Compare structured routing against direct natural-language LLM routing using predefined and repeated scenarios.
5. Evaluate consistency, repeatability, expected-route accuracy, validation behavior, trace completeness, and execution overhead.

## 2. Prototype Architecture

The prototype uses the following conceptual pipeline:

```text
Natural-Language Edge Description
              |
              v
      Ollama Interpretation
              |
              v
     Structured Semantic Contract
              |
              v
       Contract Validation
              |
              v
      Deterministic Evaluation
              |
              v
      Graph Transition Check
              |
              v
       Routing Decision
              |
              v
      JSON Execution Trace
```

The tested graph contains the following workflow nodes:

- `Check Tests`
- `Deploy Code`
- `Fix Code`

Two directed transitions are used:

- `Check Tests` → `Deploy Code`
- `Check Tests` → `Fix Code`

The routing condition is represented using the Boolean workflow variable `tests_passed`.

A generated condition has the following form:

```json
{
  "field": "tests_passed",
  "operator": "equals",
  "value": true
}
```

The structured representation is intentionally limited to the tested Boolean condition format.

## 3. Software Requirements

The development and experimental environment uses:

- Windows and Visual Studio Code
- Python 3.14.10
- A Python virtual environment (`.venv`)
- Ollama
- Local model: `llama3.2:3b`

The current Python environment uses standard-library modules and does not require additional third-party Python packages.

Ollama must be installed separately and accessible through its local API.

## 4. Environment Setup

Open a PowerShell terminal in the project root folder.

### Create a virtual environment

```powershell
python -m venv .venv
```

### Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Check the Python version

```powershell
python --version
```

The recorded research environment used Python 3.14.10.

### Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

The requirements file currently contains no third-party Python dependencies.

### Install and prepare Ollama

Install Ollama using its official installation instructions.

Download the model:

```powershell
ollama pull llama3.2:3b
```

Verify the available models:

```powershell
ollama list
```

Ensure the Ollama service is running before executing experiments that require language-model inference.

## 5. Main Implementation Files

The `src` directory contains the implementation and experiment scripts.

| File | Purpose |
|---|---|
| `semantic_contract.py` | Structured semantic contract representation |
| `contract_validator.py` | Individual contract structure validation |
| `contract_evaluator.py` | Evaluation of structured contract conditions |
| `contract_router.py` | Deterministic contract-based routing |
| `graph.py` | Workflow graph and permitted-transition checks |
| `ollama_structured_interpreter.py` | Ollama-based structured condition generation |
| `direct_nl_llm_router.py` | Direct natural-language LLM routing baseline |
| `traced_contract_router.py` | Routing wrapper with graph enforcement and automatic tracing |
| `execution_trace.py` | Execution trace creation and JSON persistence |
| `independent_evaluation_dataset.py` | Independent natural-language evaluation cases |

Additional test scripts are included in `src`.

## 6. Running the Experiments

Run the following commands from the project root while the virtual environment is active.

### Integrated Ollama workflow test

```powershell
python src/test_ollama_workflow_integration.py
```

This test checks contract generation, validation, routing for both workflow states, repeated deterministic routing, and execution trace persistence.

### Independent end-to-end evaluation

```powershell
python src/test_independent_end_to_end.py
```

This evaluates generated structured conditions and routing behavior using the independent benchmark.

### Independent interpretation consistency

```powershell
python src/test_contract_generation_consistency.py
```

This evaluates repeated structured interpretation across independent natural-language cases.

### Original matched independent comparison

```powershell
python src/test_matched_independent_nl.py
```

This compares direct LLM routing and structured routing once per independent case.

**Caution:** This original script writes to `docs/matched_independent_nl_results.json` and may overwrite its existing results. Preserve the original evidence before rerunning.

### Repeated matched independent comparison

```powershell
python src/test_repeated_matched_independent_nl.py
```

This performs three repetitions for each of ten independent cases.

The experiment generates 30 paired routing decisions and makes approximately 90 Ollama calls.

It writes to:

`docs/repeated_matched_independent_nl_results.json`

The script uses exclusive file creation. If that output file already exists, the script will refuse to overwrite it after completing the model calls. To reproduce the experiment without disturbing existing evidence, run it in a separate project copy with a fresh output location.

**Do not run all experiment scripts through automatic test discovery.** Some scripts execute model calls or experiments when imported. Run the intended scripts individually.

### Additional verified evaluation experiments

The following three experiments provide the main comparative and
workflow-tracing evidence for the current report.

**Prompt-controlled routing comparison**

```powershell
python src/test_prompt_controlled_comparison.py
```

This experiment evaluates ten natural-language cases with three repetitions
per case under original direct routing, prompt-controlled direct routing,
and fresh structured-contract routing. The recorded accuracies were
15/30 (50%), 15/30 (50%), and 24/30 (80%), respectively. All three methods
produced stable decisions for 10/10 cases. The corresponding model-call
counts were 30, 30, and 60.

Evidence: `docs/prompt_controlled_comparison_results.json`.

**Contract-reuse experiment**

```powershell
python src/test_contract_reuse_experiment.py
```

This experiment generates two structured contracts once per case and
reuses them for three routing decisions. The recorded result was
27/30 correct decisions (90%), with 10/10 cases stable. Contract
construction required 20 total model calls; the subsequent deterministic
routing decisions required no additional model calls. The recorded
total construction time was approximately 92.4455 seconds, and the
combined routing time for 30 decisions was approximately 0.0004541 seconds.
These results should not be interpreted as a causal comparison with
fresh generation because the runs were separate.

Evidence: `docs/contract_reuse_experiment_results.json`.

**Workflow-path and execution-trace experiment**

```powershell
python src/test_workflow_path_trace_experiment.py
```

This experiment evaluates two Boolean workflow states, each repeated
ten times, using manually authored reference contracts. All 20/20
tested workflow paths matched their expected destinations, and all
20/20 saved trace files passed the implemented trace checks with
20 unique trace identifiers. Each complete tested path contains one
routed transition to a terminal node. This experiment does not
evaluate language-model interpretation or a complex multi-step
agent workflow.

Evidence: `docs/workflow_path_trace_experiment_results.json` and
`docs/workflow_path_trace_experiment_traces/`.

**Reproduction safety:** Preserve the original `docs` evidence. The
prompt-controlled and contract-reuse scripts use exclusive result-file
creation, but they can perform model calls before reaching the save
operation. The workflow-path script checks for existing result and
trace destinations before execution. Run these experiments in a
separate project copy with fresh output destinations rather than
rerunning them over the original research records.

## 7. Verified Experimental Findings

### Repeated matched independent natural-language comparison

Ten independent natural-language cases were evaluated three times each.

| Metric | Direct LLM | Structured Contracts |
|---|---:|---:|
| Decisions | 30 | 30 |
| Correct decisions | 15 | 24 |
| Expected-route accuracy | 50.0% | 80.0% |
| Cases with stable repeated decisions | 10/10 | 10/10 |
| Total measured time | 89.5295 seconds | 253.5074 seconds |

The structured method achieved 30 percentage points higher expected-route accuracy in this benchmark.

Both methods produced stable decisions for all ten cases. However, decision stability does not imply correctness.

The structured method was slower when fresh contract generation was included for every repetition.

### Interpretation correctness

Across the repeated matched comparison, 24 of 30 target paraphrase interpretations were correct.

The structured interpreter repeatedly misinterpreted two failure-related cases, IND06 and IND10.

In those cases, the structured router produced no matching route rather than select the expected repair transition.

### Workflow repeatability and tracing

Separate experiments previously demonstrated:

- 20/20 repeated workflow paths matched the expected tested path.
- 20/20 repeated automatic tracing runs passed.
- 20/20 repeated trace runs produced unique trace identifiers and files.

The workflow-path experiment included a fixed initial transition that was not selected through semantic contract evaluation.

### Earlier independent interpretation consistency

A separate experiment using ten independent paraphrases with three interpretations per case recorded:

- 25/30 correct interpretations.
- 9/10 cases with stable interpreted conditions.

These are separate experimental results and should not be combined with the matched routing comparison as though they were the same trial.

## 8. Validation and Execution Traces

The prototype evaluates contract structure, workflow state, routing conditions, and selected graph transitions.

The traced routing wrapper can save JSON records containing information such as:

- Current workflow node
- Workflow state
- Evaluated contracts
- Routing status
- Selected next node
- Matched contracts
- Validation results
- Decision explanation
- Unique trace identifier

The traced routing wrapper rejects selected transitions that are not permitted by the configured workflow graph.

Individual contract validation does not independently enforce all graph constraints or contract-set uniqueness requirements.

## 9. Research Limitations

The findings should be interpreted within the following boundaries:

1. The prototype uses a small workflow graph and a Boolean condition representation.
2. The independent benchmark contains ten paraphrase cases.
3. Each independent case tests one workflow state.
4. The benchmark oracle determines which edge is substituted and the expected destination; it is not supplied as an answer to either routing model.
5. The structured interpreter receives explicit Boolean interpretation guidance that the direct routing method does not receive.
6. The structured approach makes two LLM interpretation calls per repetition, while the direct method makes one routing call.
7. Repeated matched comparison timing includes fresh structured contract generation.
8. Stable routing decisions can still be incorrect.
9. Structural validation cannot guarantee the semantic correctness of generated conditions.
10. Oracle-based semantic consistency checks require an independently annotated expected condition and do not constitute automatic production-time semantic verification.
11. The repeated matched comparison does not measure full workflow execution or execution-trace persistence.
12. The prototype does not establish general performance across different models, larger graphs, or production environments.

The observed accuracy difference cannot be attributed exclusively to the structured semantic-contract architecture because the two methods also differ in prompt guidance and output constraints.

## 10. Research Evidence and Results

Experimental outputs and research documentation are stored in the `docs` directory.

Important files include:

- `matched_routing_research_findings.md`
- `research_completion_checklist.txt`
- `matched_independent_nl_results.json`
- `repeated_matched_independent_nl_results.json`
- `independent_interpretation_consistency_results.json`
- `independent_end_to_end_results.json`
- `independent_semantic_consistency_results.json`

These files preserve the experimental records used to support the reported findings.

## 11. Research Conclusion

The prototype demonstrates that natural-language workflow edge conditions can be translated into structured semantic contracts and evaluated through a deterministic routing component.

Within the tested benchmark, structured routing achieved higher expected-route accuracy than the direct natural-language LLM baseline, while requiring more end-to-end execution time when contracts were regenerated for each repetition.

The results distinguish three separate properties: consistency of decisions, correctness of semantic interpretation, and correctness of selected workflow routes.

The research supports structured contracts as a useful approach for controlled and explainable workflow routing, while also showing that deterministic execution cannot eliminate errors introduced during natural-language interpretation.

## 12. Project Status

The core prototype and major experimental comparisons have been implemented.

Remaining work includes final proposal-to-implementation review, consolidation of research results, preparation of the final Capstone II report, verification of references and university submission requirements, and final reproducibility checks.

This README describes the research prototype and the verified experimental evidence available at the time of preparation.