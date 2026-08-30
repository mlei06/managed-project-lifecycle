# Existing-project onboarding

Use this mode to make an existing repository understandable without inventing a cleaner project than the one that exists.

## Discover before writing

1. Inspect repository structure, manifests, configuration examples, test configuration, automation, deployment files, history, and existing instructions.
2. Run safe discovery commands and the documented tests when practical.
3. Classify statements as implemented, planned, inferred, or unknown.
4. Ask the user only for product intent, ownership, or material choices that repository evidence cannot answer.
5. Identify contradictions instead of silently choosing one source as true.

## Produce the baseline

Create or update:

- `.agents/project.json` with project-specific workflow facts.
- `AGENTS.md` as the small host bootstrap.
- `README.md` as the front door.
- `docs/product.md`, `docs/system.md`, and `docs/quality.md`.
- ADRs only for accepted decisions with live alternatives.
- Hooks and the PR template when the user adopts the full standard.

Repository-writing onboarding is meaningful work. Find or create its work item and branch before edits. If the board cannot be reached, return the proposed item in chat and stop.

## Accuracy rules

- Never infer a passing test suite from test files alone.
- Never claim an integration, deployment, database, interface, or workflow exists because it is planned.
- Preserve known gaps and uncomfortable measurements.
- Put unresolved product choices in product open questions; put implementation shortcomings in quality limitations or debt.

