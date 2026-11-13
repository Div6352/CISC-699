# Week 4 - Design Decisions and Open Issues
## D1: Separate natural-language interpretation from deterministic contract evaluation and routing.
## D2: Validate semantic contracts before routing; enforce permitted graph transitions separately.
## D3: Save JSON execution traces to support auditability and reproducibility.
## Open Issue 1: A structurally valid contract may still contain an incorrect natural-language interpretation.
## Open Issue 2: The current contract schema supports only Boolean tests_passed conditions; broader condition types remain unverified.
## Open Issue 3: Direct LLM and structured-routing comparisons use different prompt guidance, limiting causal conclusions.
