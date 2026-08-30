#!/usr/bin/env python3
"""Create the managed project structure from a verified project profile."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any


TOKEN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_profile(path: Path) -> dict[str, Any]:
    profile = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "schema_version",
        "standards",
        "project",
        "orientation",
        "azure_devops",
        "git",
        "commands",
        "documentation",
    }
    missing = sorted(required.difference(profile))
    if missing:
        raise ValueError(f"Profile is missing top-level fields: {', '.join(missing)}")
    if profile["schema_version"] != 1:
        raise ValueError("Only project profile schema_version 1 is supported.")
    if profile["standards"].get("skill") != "managed-project-lifecycle":
        raise ValueError("standards.skill must be managed-project-lifecycle.")
    return profile


def first_command(profile: dict[str, Any], name: str) -> str:
    commands = profile.get("commands", {}).get(name, [])
    return commands[0] if commands else "Not configured yet"


def substitutions(profile: dict[str, Any]) -> dict[str, str]:
    project = profile["project"]
    return {
        "PROJECT_NAME": str(project["name"]),
        "PROJECT_SUMMARY": str(project["summary"]),
        "PROJECT_MATURITY": str(project.get("maturity", "unspecified")),
        "SETUP_COMMAND": first_command(profile, "setup"),
        "TEST_COMMAND": first_command(profile, "test"),
    }


def render(text: str, values: dict[str, str], source: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise ValueError(f"Unknown template token {key} in {source}")
        return values[key]

    return TOKEN.sub(replace, text)


def output_path(relative: Path) -> Path:
    name = relative.name.removesuffix(".template")
    return relative.with_name(name)


def main() -> int:
    args = parse_args()
    profile = load_profile(args.profile.resolve())
    target = args.target.resolve()
    templates = Path(__file__).resolve().parent.parent / "assets" / "repository"
    values = substitutions(profile)

    operations: list[tuple[Path, str | bytes]] = []
    profile_output = target / ".agents" / "project.json"
    operations.append((profile_output, json.dumps(profile, indent=2, ensure_ascii=False) + "\n"))

    for source in sorted(
        path
        for path in templates.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    ):
        relative = output_path(source.relative_to(templates))
        destination = target / relative
        try:
            content: str | bytes = render(source.read_text(encoding="utf-8"), values, source)
        except UnicodeDecodeError:
            content = source.read_bytes()
        operations.append((destination, content))

    collisions = [path for path, _ in operations if path.exists() and not args.replace]
    if collisions:
        listed = "\n".join(f"  {path}" for path in collisions)
        raise SystemExit(f"Refusing to overwrite existing files:\n{listed}\nUse --replace only after review.")

    for destination, content in operations:
        verb = "WOULD WRITE" if args.dry_run else "WRITE"
        print(f"{verb} {destination}")
        if args.dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            destination.write_bytes(content)
        else:
            destination.write_text(content, encoding="utf-8", newline="\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
