#!/usr/bin/env python3
"""Generate Dodona/TESTed exercise folders from an approved JSON proposal."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
from pathlib import Path
from typing import Any


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def ensure_slug(value: str, field: str) -> None:
    if not SLUG_RE.match(value):
        raise ValueError(f"{field} must be kebab-case ASCII: {value!r}")


def ensure_trailing_newline(value: str) -> str:
    if value and not value.endswith("\n"):
        return value + "\n"
    return value


def yaml_scalar(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_lines_for_test(test: dict[str, Any], indent: int = 8) -> list[str]:
    prefix = " " * indent
    lines: list[str] = []
    first = True
    for key in ("stdin", "stdout", "stderr", "expression", "statement", "return", "exit_code"):
        if key not in test:
            continue
        value = ensure_trailing_newline(test[key]) if key in {"stdout", "stderr"} else test[key]
        marker = "-" if first else " "
        lines.append(f"{prefix}{marker} {key}: {yaml_scalar(value)}")
        first = False
    if first:
        raise ValueError("Each test must include at least one TESTed field")
    return lines


def build_suite(exercise: dict[str, Any]) -> str:
    tests = exercise.get("tests")
    if not isinstance(tests, list) or not tests:
        raise ValueError(f"{exercise['slug']}: tests must be a non-empty list")

    exercise_type = exercise.get("type", "io")
    visible_tests = [test for test in tests if not test.get("hidden")]
    hidden_tests = [test for test in tests if test.get("hidden")]
    groups: list[tuple[str, bool, list[dict[str, Any]]]] = []
    if visible_tests:
        groups.append(("Casos visibles", False, visible_tests))
    if hidden_tests:
        groups.append(("Casos ocultos", True, hidden_tests))

    lines: list[str] = []

    for title, hidden, grouped_tests in groups:
        lines.append(f"- tab: {yaml_scalar(title)}")
        if hidden:
            lines.append("  hidden: true")

        if exercise_type == "io":
            lines.append("  contexts:")
            for test in grouped_tests:
                if "stdin" not in test or "stdout" not in test:
                    raise ValueError(f"{exercise['slug']}: io tests need stdin and stdout")
                lines.append("    - testcases:")
                lines.extend(yaml_lines_for_test(test, indent=8))
        elif exercise_type == "function":
            lines.append("  testcases:")
            for test in grouped_tests:
                if "expression" not in test or "return" not in test:
                    raise ValueError(f"{exercise['slug']}: function tests need expression and return")
                lines.extend(yaml_lines_for_test(test, indent=4))
        else:
            raise ValueError(f"{exercise['slug']}: unknown type {exercise_type!r}")

    return "\n".join(lines) + "\n"


def build_description(exercise: dict[str, Any]) -> str:
    """Build the Dodona description Markdown. Only title + statement — no metadata.

    Dodona renders the sample I/O natively from the exercise config, so it must
    NOT be duplicated here. Pedagogical metadata (topics, focus_class, source)
    belongs in the JSON proposal, not in the student-facing description.
    """
    statement = exercise["statement_md"].strip()
    parts = [
        f"# {exercise['title']}",
        "",
        statement,
    ]
    return "\n".join(parts).strip() + "\n"


def build_notebook(proposal: dict[str, Any]) -> dict[str, Any]:
    """Build a Jupyter notebook with one exercise per section.

    For each exercise: a markdown cell with the statement (+ sample if not
    already inlined in statement_md) and an empty code cell for the student.
    Solutions are grouped at the end in collapsible <details> blocks.
    """
    set_title = proposal.get("set_title", proposal["set_slug"])
    exercises = proposal["exercises"]

    def md_cell(source: str) -> dict[str, Any]:
        return {"cell_type": "markdown", "metadata": {}, "source": source}

    def code_cell() -> dict[str, Any]:
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": "",
        }

    cells: list[dict[str, Any]] = [
        md_cell(
            f"# {set_title}\n\n"
            "Completa cada ejercicio en la celda de código correspondiente."
        )
    ]

    for i, exercise in enumerate(exercises, 1):
        statement = exercise["statement_md"].strip()
        sample = exercise.get("sample") or {}

        header = f"## Ejercicio {i} — {exercise['title']}\n\n{statement}"

        # Append sample block only when statement_md doesn't already include it
        # (new-style proposals keep statement_md clean; Dodona shows sample natively)
        if sample and "**Ejemplo" not in statement and "## Ejemplo" not in statement:
            example_parts: list[str] = []
            if "stdin" in sample:
                example_parts += [
                    "",
                    "**Entrada de ejemplo:**",
                    "```",
                    sample["stdin"].rstrip("\n"),
                    "```",
                ]
            if "stdout" in sample:
                example_parts += [
                    "",
                    "**Salida esperada:**",
                    "```",
                    sample["stdout"].rstrip("\n"),
                    "```",
                ]
            if example_parts:
                header += "\n" + "\n".join(example_parts)

        cells.append(md_cell(header))
        cells.append(code_cell())

    solution_parts = ["## 📋 Soluciones\n"]
    for i, exercise in enumerate(exercises, 1):
        sol = exercise["solution_py"].strip()
        solution_parts.append(
            f"\n<details>\n<summary>Ejercicio {i} — {exercise['title']}</summary>\n\n"
            f"```python\n{sol}\n```\n\n</details>"
        )
    cells.append(md_cell("".join(solution_parts)))

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0",
            },
        },
        "cells": cells,
    }


def build_config(exercise: dict[str, Any]) -> dict[str, Any]:
    title = exercise["title"]
    return {
        "description": {
            "names": {
                "es": title,
                "en": title,
            }
        },
        "evaluation": {
            "handler": "tested",
            "test_suite": "suite.yaml",
        },
        "programming_language": exercise.get("programming_language", "python"),
        "access": exercise.get("access", "private"),
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def generate(
    proposal_path: Path,
    output_root: Path,
    force: bool,
    jupyter_root: Path | None = None,
) -> list[Path]:
    proposal = json.loads(proposal_path.read_text(encoding="utf-8-sig"))
    set_slug = proposal["set_slug"]
    ensure_slug(set_slug, "set_slug")

    exercises = proposal.get("exercises")
    if not isinstance(exercises, list) or not exercises:
        raise ValueError("Proposal must contain a non-empty exercises list")

    output_root.mkdir(parents=True, exist_ok=True)
    root_dirconfig = output_root / "dirconfig.json"
    if not root_dirconfig.exists():
        write_text(
            root_dirconfig,
            json.dumps(
                {
                    "programming_language": "python",
                    "access": "private",
                    "evaluation": {"handler": "tested"},
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )

    set_dir = output_root / set_slug
    if set_dir.exists() and force:
        def _force_remove(func, path, _exc_info):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        shutil.rmtree(set_dir, onerror=_force_remove)
    elif set_dir.exists():
        raise FileExistsError(f"{set_dir} already exists. Use --force to overwrite.")

    set_dir.mkdir(parents=True)
    write_text(
        set_dir / "dirconfig.json",
        json.dumps(
            {
                "description": {
                    "names": {
                        "es": proposal.get("set_title", set_slug),
                        "en": proposal.get("set_title", set_slug),
                    }
                }
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )

    created: list[Path] = []
    for exercise in exercises:
        for required in ("slug", "title", "statement_md", "solution_py"):
            if required not in exercise:
                raise ValueError(f"Exercise missing {required}: {exercise}")

        slug = exercise["slug"]
        ensure_slug(slug, "exercise.slug")
        exercise_dir = set_dir / slug
        description = build_description(exercise)

        write_text(exercise_dir / "config.json", json.dumps(build_config(exercise), ensure_ascii=False, indent=2) + "\n")
        write_text(exercise_dir / "description" / "description.es.md", description)
        write_text(exercise_dir / "description" / "description.en.md", description)
        write_text(exercise_dir / "evaluation" / "suite.yaml", build_suite(exercise))
        write_text(exercise_dir / "solution" / "solution.py", ensure_trailing_newline(exercise["solution_py"]))
        created.append(exercise_dir)

    if jupyter_root is not None:
        notebook = build_notebook(proposal)
        nb_path = jupyter_root / set_slug / f"{set_slug}-ejercicios.ipynb"
        write_text(nb_path, json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
        created.append(nb_path)

    return created


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposal_json", type=Path)
    parser.add_argument("--output-root", type=Path, default=Path("dodona-ejercicios-profesor"))
    parser.add_argument("--jupyter-root", type=Path, default=Path("dodona"),
                        help="Root dir for generated Jupyter notebook (default: dodona/)")
    parser.add_argument("--no-jupyter", action="store_true", help="Skip Jupyter notebook generation")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    jupyter_root = None if args.no_jupyter else args.jupyter_root
    created = generate(args.proposal_json, args.output_root, args.force, jupyter_root)
    print(f"Generated {len(created)} items:")
    for path in created:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
