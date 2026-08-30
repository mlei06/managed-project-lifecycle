#!/usr/bin/env python3
"""Expose this canonical skill to Codex, Claude Code, and OpenCode."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


SKILL_NAME = "managed-project-lifecycle"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--hosts",
        nargs="+",
        choices=("codex", "claude", "opencode"),
        default=("codex", "claude", "opencode"),
        help="Hosts to install for. Codex and OpenCode share .agents/skills.",
    )
    parser.add_argument("--method", choices=("link", "copy"), default="link")
    parser.add_argument("--replace", action="store_true", help="Replace an existing copied installation or link.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--home", type=Path, default=Path.home(), help=argparse.SUPPRESS)
    return parser.parse_args()


def destinations(home: Path, hosts: list[str]) -> list[Path]:
    result: list[Path] = []
    if {"codex", "opencode"}.intersection(hosts):
        result.append(home / ".agents" / "skills" / SKILL_NAME)
    if "claude" in hosts:
        result.append(home / ".claude" / "skills" / SKILL_NAME)
    return result


def remove_existing(path: Path) -> None:
    if path.is_symlink():
        path.unlink()
        return
    if os.name == "nt" and path.exists():
        # rmdir removes a junction itself without traversing its target.
        result = subprocess.run(["cmd", "/c", "rmdir", str(path)], capture_output=True, text=True)
        if result.returncode == 0:
            return
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def create_link(source: Path, destination: Path) -> None:
    try:
        destination.symlink_to(source, target_is_directory=True)
    except OSError:
        if os.name != "nt":
            raise
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(destination), str(source)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip())


def main() -> int:
    args = parse_args()
    source = Path(__file__).resolve().parent.parent
    home = args.home.resolve()

    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"SKILL.md not found at {source}")

    for destination in destinations(home, list(args.hosts)):
        action = f"{args.method} {source} -> {destination}"
        if args.dry_run:
            print(f"WOULD {action}")
            continue

        if destination.exists() or destination.is_symlink():
            try:
                same_target = destination.resolve() == source.resolve()
            except OSError:
                same_target = False
            if same_target and args.method == "link":
                print(f"OK already linked: {destination}")
                continue
            if not args.replace:
                raise SystemExit(f"Refusing to replace {destination}; rerun with --replace.")
            remove_existing(destination)

        destination.parent.mkdir(parents=True, exist_ok=True)
        if args.method == "copy":
            shutil.copytree(source, destination, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        else:
            create_link(source, destination)
        print(f"OK {action}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
