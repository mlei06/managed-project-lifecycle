# Tracked development

## Start

1. Confirm the request authorizes implementation rather than review or ideation only.
2. Search for a suitable work item. Create one only when none covers the scope.
3. Ensure the item meets the ready criteria: value, observable acceptance criteria, failure behavior, documentation impact, dependencies, and test expectations.
4. Move it to the profile's active state and post the intended plan.
5. Start from the canonical branch and create `<type>/<id>-<slug>`, or verify the current branch names the item and is suitable.

## Implement

- Make only changes authorized by the item.
- Keep one logical change per commit and start its subject with the configured item reference.
- Add or update tests proportionate to behavior and risk.
- Update documentation in the same branch.
- If a significant choice has live alternatives, stop and write an ADR before hiding the reasoning in code.
- For a blocking discovery, create and link separate tracked work before fixing it, and keep it in its own commit. For a non-blocking discovery, capture it and leave the code alone.

## Complete

Audit before opening the PR:

- Every acceptance criterion is checked individually.
- Focused and full tests pass; actual output is available for the PR.
- The diff contains no unrelated changes.
- Discoveries have IDs or are explicitly absent.
- Product, system, quality, ADR, README, and configuration impacts were assessed.
- No new product-documentation file exists outside the documented structure.
- No debug code, secrets, temporary files, or personal data entered history.
- Hooks were not bypassed, or the bypass is explained.

Create the PR against the canonical branch, link the work item explicitly, and move it to the review state. Merge only when authorized and required checks pass. After merge, verify the canonical branch, post a closing summary with tests/docs/discoveries, and move the item to the done state.

