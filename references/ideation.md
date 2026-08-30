# Ideation and work shaping

Ideation is exploration, not automatically committed work.

## Explore

1. Read the project profile and relevant product, system, quality, and decision context.
2. Search the board read-only for duplicates, dependencies, or previously rejected approaches when access is available.
3. Clarify user value, observable behavior, failure behavior, boundaries, alternatives, risks, and evidence.
4. State whether the idea changes scope, architecture, interfaces, data, dependencies, configuration, tests, or documentation.
5. Draft a proposed work item in chat when useful.

Do not create a work item until the user asks to capture, schedule, or implement the idea, or the request otherwise clearly commits to the work.

## Work-item proposal

Include:

- Problem and user value
- Proposed external behavior
- Independently verifiable acceptance criteria
- Explicit failure cases
- Documentation impact
- Architecture boundaries
- Dependencies and relationships
- Positive and negative test expectations

Use a User Story or Bug for independently acceptable value or behavior. Use a Task for implementation work within an existing story. Do not create cards for trivial substeps.

## Parent tiers

An Epic or Feature is a work item, not a folder. It needs the same problem, user value, and observable closing condition a story needs, because it is what someone reads first when asking what the project is doing.

Creating a parent tier up front as a taxonomy is legitimate. Leaving it empty afterwards is not. When the user asks for a structure before the work under it is shaped, say inside each parent that it is an unshaped placeholder and what would have to be answered to shape it. An acknowledged placeholder is visible debt; an empty description is invisible debt that reads as a real item.

