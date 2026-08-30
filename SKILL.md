---
name: managed-project-lifecycle
description: Onboard, scaffold, document, ideate, develop, and deliver software projects through a work-item-first Azure DevOps and Git lifecycle. Use for new-project setup, existing-project orientation, product or architecture documentation, work planning, implementation, pull requests, and completion audits. Do not use for read-only questions that do not benefit from project lifecycle context.
---

# Managed Project Lifecycle

Apply one traceable lifecycle without replacing project-specific facts or the user's authority.

## Establish context

1. Find the repository root and read its `AGENTS.md` or equivalent host instruction file.
2. Read `.agents/project.json` when present. It is the canonical project profile.
3. Read the orientation documents listed by the profile before meaningful repository changes.
4. Inspect Git status and preserve unrelated or pre-existing changes.
5. Distinguish current behavior from planned behavior. Never present plans as implemented facts.

If the profile is absent, use onboarding or scaffolding mode. Do not guess Azure coordinates, the canonical branch, project purpose, commands, or sensitive-data rules.

## Choose the mode

- Existing-project orientation or documentation bootstrap: read [references/onboarding.md](references/onboarding.md).
- New repository or standards scaffold: read [references/scaffolding.md](references/scaffolding.md).
- Brainstorming, shaping, or capturing a possible change: read [references/ideation.md](references/ideation.md).
- Implementing, reviewing, or completing tracked work: read [references/development.md](references/development.md).
- Azure Boards, Repos, work items, or PR operations: also read [references/azure-devops.md](references/azure-devops.md).
- Creating or changing project documentation: also read [references/documentation.md](references/documentation.md).
- Creating or validating `.agents/project.json`: read [references/project-profile.md](references/project-profile.md).

Load only the references required for the active mode.

## Invariants

- Meaningful repository changes require a real work item before implementation. Never invent an ID.
- Read-only review, diagnosis, explanation, and ideation do not require a work item.
- Creating a work item marks an idea as committed work; do not create one merely because it was discussed.
- Development occurs on a work-item branch, not the canonical branch, except for the one-time empty-repository genesis procedure.
- Every commit and PR names the authorizing work item.
- Discovered out-of-scope work becomes a separate work item or remains untouched.
- Parent items are shaped and stated like their children. Closing a child never leaves its parent's state or intent unreviewed.
- Tests and documentation ship with the behavior they describe.
- A work item is complete only after its acceptance criteria pass, its PR is merged, documentation is current, and a closing summary is posted.
- When Azure DevOps is unreachable, provide a proposed work item in chat and stop before implementation. Never create pending-work-item files.
- External mutations such as project creation, repository creation, pushes, PR completion, and deletion require authorization appropriate to the user's request.

## Repository assets

Use `scripts/scaffold_project.py` for deterministic scaffolding and `scripts/validate_project.py` for structural checks. Templates live under `assets/repository/`. Use `scripts/install.py` to expose this same skill directory to Codex, Claude Code, and OpenCode without maintaining divergent skill bodies.
