# Project profile

`.agents/project.json` is the canonical machine-readable source for project-specific lifecycle configuration. `AGENTS.md` points agents to it; reusable skill instructions must not duplicate its values.

## Required shape

```json
{
  "schema_version": 1,
  "standards": {"skill": "managed-project-lifecycle", "version": 1},
  "project": {"name": "Example", "summary": "One truthful sentence.", "maturity": "prototype"},
  "orientation": {"required": ["README.md", "docs/product.md", "docs/system.md", "docs/quality.md"], "decisions": "relevant"},
  "azure_devops": {
    "organization": "https://dev.azure.com/example",
    "project": "Example",
    "team": "Example Team",
    "repository": "Example",
    "area_path": "Example",
    "process": "Agile",
    "states": {"new": "New", "active": "Active", "review": "Resolved", "done": "Closed"},
    "work_item_types": ["Epic", "Feature", "User Story", "Task", "Bug"]
  },
  "git": {"canonical_branch": "main", "branch_types": ["feature", "bugfix", "hotfix", "docs", "refactor", "chore"], "commit_reference": "#<id>"},
  "commands": {"setup": ["command"], "test": ["command"], "lint": [], "build": [], "run": []},
  "documentation": {"readme": "README.md", "product": "docs/product.md", "system": "docs/system.md", "quality": "docs/quality.md", "decisions": "docs/decisions", "pr_template": ".azuredevops/pull_request_template.md"},
  "boundaries": [],
  "meaningful_change_paths": [],
  "sensitive_paths": []
}
```

Use real values only. Empty optional lists are preferable to invented commands, boundaries, owners, metrics, or paths. Changing the profile is itself a meaningful workflow/configuration change.

