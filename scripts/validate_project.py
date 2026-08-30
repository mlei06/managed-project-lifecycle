#!/usr/bin/env python3
"""Validate a repository scaffolded for the managed project lifecycle."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TOKEN = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path, default=Path.cwd())
    return parser.parse_args()


def nested(profile: dict[str, Any], *keys: str) -> Any:
    current: Any = profile
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(".".join(keys))
        current = current[key]
    return current


def main() -> int:
    root = parse_args().target.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    profile_path = root / ".agents" / "project.json"

    if not profile_path.is_file():
        print("ERROR missing .agents/project.json")
        return 1

    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR invalid .agents/project.json: {exc}")
        return 1

    required_fields = (
        ("schema_version",),
        ("standards", "skill"),
        ("standards", "version"),
        ("project", "name"),
        ("project", "summary"),
        ("orientation", "required"),
        ("azure_devops", "organization"),
        ("azure_devops", "project"),
        ("azure_devops", "repository"),
        ("git", "canonical_branch"),
        ("git", "branch_types"),
        ("commands", "test"),
        ("documentation", "readme"),
        ("documentation", "product"),
        ("documentation", "system"),
        ("documentation", "quality"),
        ("documentation", "decisions"),
    )
    for field in required_fields:
        try:
            value = nested(profile, *field)
            if value is None or value == "":
                errors.append(f"empty profile field {'.'.join(field)}")
        except KeyError:
            errors.append(f"missing profile field {'.'.join(field)}")

    if profile.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if profile.get("standards", {}).get("skill") != "managed-project-lifecycle":
        errors.append("standards.skill must be managed-project-lifecycle")

    expected = {
        Path("AGENTS.md"),
        Path("README.md"),
        Path("CONTRIBUTING.md"),
        Path("docs/product.md"),
        Path("docs/system.md"),
        Path("docs/quality.md"),
        Path("docs/decisions/template.md"),
        Path(".azuredevops/pull_request_template.md"),
        Path(".githooks/commit-msg"),
        Path(".githooks/pre-commit"),
        Path(".githooks/pre-push"),
        Path("scripts/setup_hooks.py"),
    }
    for relative in sorted(expected):
        if not (root / relative).is_file():
            errors.append(f"missing {relative.as_posix()}")

    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        agents = agents_path.read_text(encoding="utf-8")
        if "managed-project-lifecycle" not in agents:
            errors.append("AGENTS.md does not name managed-project-lifecycle")
        if ".agents/project.json" not in agents:
            errors.append("AGENTS.md does not direct agents to .agents/project.json")

    pending = root / "docs" / "_devops" / "pending"
    if pending.exists():
        errors.append("pending work-item directory exists; proposals must stay in chat")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if TOKEN.search(text):
            errors.append(f"unresolved template token in {path.relative_to(root).as_posix()}")

    if not profile.get("commands", {}).get("test"):
        warnings.append("commands.test is empty; quality verification is not yet reproducible")

    for warning in warnings:
        print(f"WARNING {warning}")
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"FAILED with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1
    print(f"OK managed project profile and scaffold are valid ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

