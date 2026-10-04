#!/usr/bin/env python3
"""Copy the complete Chrys Epic skill into an explicitly chosen host scope."""

import argparse
from pathlib import Path
import shutil
import sys


SKILL_NAME = "chrys-epic"
SOURCE = Path(__file__).resolve().parents[1] / "skills" / SKILL_NAME


def inventory(directory):
    """Compare contents, including extra files, without following symlinks."""
    entries = {}
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Refusing to compare a symlink in an installation: {path}")
        key = path.relative_to(directory).as_posix()
        entries[key] = path.read_bytes() if path.is_file() else None
    return entries


def install(source, destination):
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Skill source is incomplete: {source}")
    if destination.is_symlink():
        raise ValueError(f"Existing installation is a symlink; leave it intact: {destination}")
    if destination.exists():
        if destination.is_dir() and inventory(source) == inventory(destination):
            return "Already installed"
        raise ValueError(
            f"Existing installation differs: {destination}. "
            "Move it to a backup outside the skills folder before installing this version."
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return "Installed"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("claude", "codex"), required=True)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=Path, help="Existing project directory")
    scope.add_argument("--user", action="store_true", help="Install for the current account")
    args = parser.parse_args(argv)
    root = Path.home() if args.user else args.project.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Directory does not exist: {root}")
    host_dir = ".claude" if args.host == "claude" else ".agents"
    destination = root / host_dir / "skills" / SKILL_NAME
    try:
        outcome = install(SOURCE, destination)
    except (OSError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    print(f"{outcome}: {destination}")
    print("Open the target project in a new agent session and ask to use chrys-epic.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
