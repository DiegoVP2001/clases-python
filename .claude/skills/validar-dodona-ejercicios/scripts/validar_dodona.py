#!/usr/bin/env python3
"""Validate local Dodona/TESTed exercise folders."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def is_exercise_dir(path: Path) -> bool:
    return (path / "config.json").is_file()


def find_exercises(root: Path) -> list[Path]:
    if is_exercise_dir(root):
        return [root]
    return sorted(path for path in root.rglob("*") if path.is_dir() and is_exercise_dir(path))


def validate_config(path: Path, errors: list[str], warnings: list[str]) -> dict:
    config_path = path / "config.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{config_path}: invalid JSON ({exc})")
        return {}

    if config.get("evaluation", {}).get("handler") != "tested":
        errors.append(f"{config_path}: evaluation.handler must be 'tested'")

    suite = config.get("evaluation", {}).get("test_suite")
    if not suite:
        errors.append(f"{config_path}: missing evaluation.test_suite")
    elif not (path / "evaluation" / suite).is_file():
        errors.append(f"{config_path}: evaluation.test_suite points to missing file {suite!r}")

    if config.get("programming_language") != "python":
        warnings.append(f"{config_path}: programming_language is not 'python'")

    if config.get("access") not in {"private", "public"}:
        errors.append(f"{config_path}: access must be 'private' or 'public'")

    names = config.get("description", {}).get("names", {})
    if not names:
        warnings.append(f"{config_path}: description.names is empty")

    return config


def validate_suite(path: Path, suite_name: str | None, errors: list[str], warnings: list[str]) -> None:
    if not suite_name:
        return
    suite_path = path / "evaluation" / suite_name
    if not suite_path.is_file():
        return
    text = suite_path.read_text(encoding="utf-8")
    if "- tab:" not in text:
        errors.append(f"{suite_path}: missing TESTed tab")
    if "testcases:" not in text:
        errors.append(f"{suite_path}: missing testcases")
    if ("stdin:" not in text and "expression:" not in text and "statement:" not in text):
        errors.append(f"{suite_path}: no stdin/expression/statement test found")
    if 'stdout: ""' not in text:
        for match in re.finditer(r'^\s*stdout:\s*"((?:\\.|[^"])*)"', text, re.MULTILINE):
            value = match.group(1)
            if value and not value.endswith(r"\n"):
                warnings.append(f"{suite_path}: stdout should end with escaped newline")


def validate_exercise(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SLUG_RE.match(path.name):
        errors.append(f"{path}: folder name must be kebab-case ASCII")

    config = validate_config(path, errors, warnings)
    suite_name = config.get("evaluation", {}).get("test_suite") if config else None
    validate_suite(path, suite_name, errors, warnings)

    has_description = any(
        (path / "description" / filename).is_file()
        for filename in ("description.es.md", "description.en.md", "description.md")
    )
    if not has_description:
        errors.append(f"{path}: missing description/description.es.md or description.en.md")

    solution_path = path / "solution" / "solution.py"
    if not solution_path.is_file():
        warnings.append(f"{path}: missing solution/solution.py")
    elif not solution_path.read_text(encoding="utf-8").strip():
        errors.append(f"{solution_path}: empty solution")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("dodona"))
    args = parser.parse_args()

    root = args.root
    if not root.exists():
        print(f"ERROR: {root} does not exist")
        return 1

    exercises = find_exercises(root)
    if not exercises:
        print(f"ERROR: no Dodona exercises found under {root}")
        return 1

    all_errors: list[str] = []
    all_warnings: list[str] = []
    for exercise in exercises:
        errors, warnings = validate_exercise(exercise)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    print(f"Checked {len(exercises)} exercise(s).")
    for warning in all_warnings:
        print(f"WARNING: {warning}")
    for error in all_errors:
        print(f"ERROR: {error}")

    if all_errors:
        print("Validation failed.")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
