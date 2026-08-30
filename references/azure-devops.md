# Azure DevOps operations

Read all coordinates and state names from `.agents/project.json`. Never reuse values remembered from another project. Prefer explicit `--organization` and `--project` arguments for mutating commands; machine-wide CLI defaults may point at a different project.

## Access check

Verify `az`, the `azure-devops` extension, authentication, and read access before promising board operations. Read-only discovery may proceed without a work item. If mutation fails for access or authentication reasons, show the proposed change in chat and stop; do not create pending files or invent IDs.

## Board lifecycle

- Search before creating.
- Use the project process's real work-item types and states.
- Put product value and observable behavior in the item, not an implementation-only description.
- Shape every tier. An Epic or Feature with an empty description is unshaped work no matter how many children it has.
- Include failure cases, documentation impact, boundaries, dependencies, and tests.
- Post a start-plan comment before implementation.
- Link parent, blocking, related, document, branch, commit, and PR relationships explicitly when supported.
- Move to review when the PR is open, not when local implementation ends.
- Move to done only after merge and a closing summary.
- Keep parent state consistent with its children: active once a child starts, done only when every child is done or removed and the parent's own acceptance holds.

## Hygiene queries

A query that exists to find neglected work must not filter on the condition that defines the neglect. A query for unshaped parents that excludes the initial state cannot see a parent that never left it, so it reports zero while the debt grows behind it.

Before trusting a hygiene query, run it against an item it is supposed to catch and confirm the item appears. A query that has never returned a row has not been verified, it has only been written.

## CLI safety

- Inspect command output and returned IDs rather than assuming success.
- Pass the work item explicitly when creating a PR; commit references alone may not create the desired Development link.
- Do not auto-complete a PR unless the user's request authorizes end-to-end completion and branch policies pass.
- Do not change organization-wide process fields or policies as a side effect of project work.

Use the locally installed Azure CLI's help for exact syntax because extension versions change. Never hard-code an example project's organization, project, repository, team, area path, branch, or item ID in reusable commands.

