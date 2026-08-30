# Managed Project Lifecycle

A portable Agent Skills skill for onboarding, scaffolding, documenting, and delivering software projects with Azure DevOps and Git traceability.

The canonical skill is `SKILL.md`. Codex, Claude Code, and OpenCode all consume that same file and its supporting resources.

## Install

Preview installation:

```powershell
python scripts/install.py --dry-run
```

Install links for all supported hosts:

```powershell
python scripts/install.py
```

The installer exposes this repository at:

- `~/.agents/skills/managed-project-lifecycle` for Codex and OpenCode
- `~/.claude/skills/managed-project-lifecycle` for Claude Code

It prefers directory links so every host reads this repository directly. Use `--method copy` only when links are unavailable; rerun with `--replace` to refresh a copied installation.

## Scaffold a project

Copy `assets/project-profile.example.json`, fill in real project values, then preview:

```powershell
python scripts/scaffold_project.py C:\path\to\project --profile C:\path\to\project-profile.json --dry-run
```

Remove `--dry-run` to create the missing files. Existing files are never overwritten unless `--replace` is explicitly supplied.

Validate the result:

```powershell
python scripts/validate_project.py C:\path\to\project
```

Scaffolding changes files only. It does not create Azure projects or work items, initialize Git, push branches, open PRs, or merge changes.

