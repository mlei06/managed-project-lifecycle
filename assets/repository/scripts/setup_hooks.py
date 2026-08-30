#!/usr/bin/env python3
"""Configure versioned Git hooks from the project profile."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    profile = json.loads((root / ".agents" / "project.json").read_text(encoding="utf-8"))
    trunk = profile["git"]["canonical_branch"]
    branch_types = "|".join(profile["git"]["branch_types"])

    def configure(*args: str) -> None:
        subprocess.run(["git", "config", *args], cwd=root, check=True)

    configure("core.hooksPath", ".githooks")
    configure("managed.trunk", trunk)
    configure("managed.branchTypes", branch_types)
    configure("--unset-all", "managed.sensitivePath") if _has_key(root, "managed.sensitivePath") else None
    for path in profile.get("sensitive_paths", []):
        configure("--add", "managed.sensitivePath", path.rstrip("/"))

    print(f"Configured .githooks; canonical branch is {trunk}.")
    return 0


def _has_key(root: Path, key: str) -> bool:
    result = subprocess.run(["git", "config", "--get-all", key], cwd=root, capture_output=True)
    return result.returncode == 0


if __name__ == "__main__":
    raise SystemExit(main())

