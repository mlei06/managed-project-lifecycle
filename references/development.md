# Tracked development

## Start

1. Confirm the request authorizes implementation rather than review or ideation only.
2. Search for a suitable work item. Create one only when none covers the scope.
3. Ensure the item meets the ready criteria: value, observable acceptance criteria, failure behavior, documentation impact, dependencies, and test expectations.
4. Check the item's parent against the same criteria. An unshaped parent is discovered work: shape it or record why it stays a placeholder before continuing.
5. Move it to the profile's active state and post the intended plan.
6. Start from the canonical branch and create `<type>/<id>-<slug>`, or verify the current branch names the item and is suitable.

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

## Reassess the parent

Completing an item is not finished until its ancestors still describe reality. In the same session, walk up the parent chain:

- Move a parent still in the initial state to the active state once any child has started.
- Move a parent to the done state only when every child is done or removed and the parent's own acceptance holds. State follows evidence, not arithmetic.
- Leave a parent with no started children in the initial state. Do not advance it to make the board look busy.
- Treat a parent with no description, no acceptance criteria, and no document link as unshaped work, whatever its children look like. Shape it or say in the item that it is a deliberate placeholder.

A parent abandoned in the initial state while its children close is the most common way a board stops describing its project, and the hardest to notice: every individual item was handled correctly.

