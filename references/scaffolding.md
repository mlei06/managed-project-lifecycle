# New-project scaffolding

Use this mode for a new repository or for adding the managed structure to an existing repository.

## Before scaffold writes

Establish with the user or existing systems:

- project name, purpose, maturity, and owners;
- Azure organization, project, team, repository, area path, process, states, and work-item types;
- canonical branch and allowed branch types;
- setup, test, lint, build, and run commands that actually exist;
- documentation paths, architectural boundaries, and sensitive paths.

Record these in a profile conforming to [project-profile.md](project-profile.md). Preview `scripts/scaffold_project.py` with `--dry-run`, review collisions, then scaffold. Do not overwrite an existing file unless the user explicitly authorizes replacement.

## Empty-repository genesis

An empty remote cannot receive a PR until its canonical branch exists. Use this exception only when no branch exists:

1. Obtain authorization to create or configure the Azure project and repository.
2. Create the bootstrap work item.
3. Create and push one empty commit named `#<id> Initialize canonical branch` to establish the canonical branch.
4. Create `chore/<id>-project-bootstrap` from it.
5. Scaffold and document the project on that branch.
6. Merge through a linked PR, then close the work item.

If a canonical branch already exists, do not use the exception.

## Documentation collaboration

Draft from evidence and the user's stated intent. Ask for confirmation of goals, non-goals, scope, users, and unresolved product decisions. Architecture may be documented as planned, but must be labeled planned until implemented. Quality documentation begins with actual commands and known gaps, not fictional metrics.

