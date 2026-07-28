#!/usr/bin/env python3
"""
generar_ayudantia.py — Genera dos notebooks Jupyter desde una propuesta JSON.

Salida (dentro de clases/, con numeración real — vigente desde 2026-07-28):
  clases/clase-<class_number>-ayudantia-<slug>/Clase <class_number> - Ayudantia <class_topic> - Ejercicios.ipynb
  clases/clase-<class_number>-ayudantia-<slug>/Clase <class_number> - Ayudantia <class_topic> - Solucionario.ipynb

Uso:
  python generar_ayudantia.py "clases/clase-NN-ayudantia-tema/Clase NN - Ayudantia Tema - Ejercicios propuesta.json" [--force]
"""

import argparse
import json
import uuid
from datetime import date
from pathlib import Path


# ── Helpers de celda ──────────────────────────────────────────────────────────

def _cell_id() -> str:
    return str(uuid.uuid4())[:8]


def md_cell(source: str) -> dict:
    lines = source.split("\n")
    source_list = [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
    return {"cell_type": "markdown", "id": _cell_id(), "metadata": {}, "source": source_list}


def code_cell(source: str = "") -> dict:
    if source:
        lines = source.split("\n")
        source_list = [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
    else:
        source_list = []
    return {
        "cell_type": "code",
        "id": _cell_id(),
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source_list,
    }


def _notebook(cells: list, colab_name: str) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"},
            "colab": {"name": colab_name + ".ipynb"},
        },
        "cells": cells,
    }


# ── Notebook de estudiantes ───────────────────────────────────────────────────

def build_student_notebook(proposal: dict) -> dict:
    slug = proposal["set_slug"]
    title = proposal["set_title"]
    today = date.today().strftime("%d/%m/%Y")

    cells = [
        md_cell(
            f"# 🏋️ {title}\n\n"
            f"📅 **Fecha:** {today}  \n"
            f"👤 **Nombre:** ___________________________  \n"
            f"📌 **Curso:** ___________________________"
        ),
        md_cell(
            "---\n\n"
            "## 📋 Instrucciones\n\n"
            "- Escribe tu código en las celdas grises debajo de cada enunciado.\n"
            "- Para ejecutar una celda, presiona **Shift + Enter**.\n"
            "- **No modifiques los enunciados.**\n"
            "- Si quedas trabado, avanza al siguiente y vuelve después.\n"
            "- Al terminar, comparte el Colab con el profesor desde el botón **Compartir**."
        ),
    ]

    if proposal.get("objetivo"):
        cells.append(md_cell(f"---\n\n## 🎯 Objetivo\n\n{proposal['objetivo']}"))

    guided = proposal.get("guided_exercise")
    if guided:
        topic = proposal.get("class_topic", "lo visto")
        cells.append(md_cell(
            f"---\n\n## 🔁 Ejercicio guiado — recordemos {topic}\n\n"
            f"{guided['statement_md']}"
        ))
        cells.append(code_cell("# Trabajemos este ejercicio en conjunto\n"))

    cells.append(md_cell("---\n\n## 🎯 Serie de ejercicios"))

    ex_num = 1
    for ex in proposal["exercises"]:
        if ex.get("difficulty") == "trivial":
            continue
        cells.append(md_cell(
            f"---\n\n### Ejercicio {ex_num} — {ex['title']}\n\n{ex['statement_md']}"
        ))
        cells.append(code_cell("# Tu código aquí\n"))
        ex_num += 1

    return _notebook(cells, f"{slug}-ejercicios")


# ── Solucionario ──────────────────────────────────────────────────────────────

def _build_rubric(ex: dict) -> str:
    sol = ex.get("solution_py", "")
    criteria = []

    if "int(input())" in sol or "float(input())" in sol:
        criteria.append("Convierte la entrada al tipo numérico correcto con `int()` o `float()`.")
    if 'input() == "si"' in sol:
        criteria.append('Compara el texto con `"si"` (sin mayúsculas ni espacios extra).')
    if " and " in sol:
        criteria.append("Usa `and` correctamente: ambas condiciones deben cumplirse.")
    if " or " in sol:
        criteria.append("Usa `or` correctamente: basta con que una condición se cumpla.")
    if "if " in sol and "else" in sol:
        criteria.append("La estructura `if/else` cubre exactamente los dos casos posibles.")
    if "print(" in sol:
        criteria.append(
            "El texto impreso coincide exactamente con la salida esperada "
            "(mayúsculas, puntuación, tildes y formato)."
        )

    if not criteria:
        criteria.append("El programa produce la salida esperada para todos los casos de prueba.")

    lines = ["### ✅ Criterios de corrección\n"]
    for c in criteria:
        lines.append(f"- {c}")

    visible = [t for t in ex.get("tests", []) if not t.get("hidden")]
    if visible:
        lines.append("\n**Casos visibles:**")
        for t in visible:
            stdin = t["stdin"].strip().replace("\n", " → ")
            stdout = t["stdout"].strip()
            lines.append(f"- Entrada: `{stdin}` | Salida esperada: `{stdout}`")

    hidden = [t for t in ex.get("tests", []) if t.get("hidden")]
    if hidden:
        lines.append("\n**Casos ocultos:**")
        for t in hidden:
            stdin = t["stdin"].strip().replace("\n", " → ")
            stdout = t["stdout"].strip()
            lines.append(f"- Entrada: `{stdin}` | Salida esperada: `{stdout}`")

    return "\n".join(lines)


def build_solucionario(proposal: dict) -> dict:
    slug = proposal["set_slug"]
    title = proposal["set_title"]
    today = date.today().strftime("%d/%m/%Y")

    cells = [
        md_cell(
            f"# 📋 Solucionario — {title}\n\n"
            f"📅 **Fecha:** {today}  \n"
            f"🔒 **Uso exclusivo del profesor.**  \n"
            f"> Subir a Classroom después de la ayudantía para que los estudiantes lo revisen."
        ),
    ]

    guided = proposal.get("guided_exercise")
    if guided:
        cells.append(md_cell(
            f"---\n\n## 🔁 Ejercicio guiado — {guided['title']}\n\n{guided['statement_md']}"
        ))
        cells.append(code_cell(f"# ✅ Solución esperada\n{guided.get('solution_py', '')}"))

    ex_num = 1
    for ex in proposal["exercises"]:
        if ex.get("difficulty") == "trivial":
            continue
        rubric = _build_rubric(ex)
        cells.append(md_cell(
            f"---\n\n## 📝 Ejercicio {ex_num} — {ex['title']}\n\n"
            f"{ex['statement_md']}\n\n"
            f"{rubric}"
        ))
        cells.append(code_cell(f"# ✅ Solución esperada\n{ex.get('solution_py', '')}"))
        ex_num += 1

    return _notebook(cells, f"{slug}-solucionario")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Genera notebooks de ayudantía (estudiantes + solucionario).")
    ap.add_argument("proposal", type=Path, help="Ruta al JSON de propuesta")
    ap.add_argument("--root", type=Path, default=Path("clases"), help="Carpeta raíz de salida")
    ap.add_argument("--force", action="store_true", help="Sobreescribir si ya existe")
    args = ap.parse_args()

    proposal = json.loads(args.proposal.read_text(encoding="utf-8"))
    slug = proposal["set_slug"]
    class_number = str(proposal["class_number"])
    class_topic = proposal["class_topic"]

    folder_name = f"clase-{class_number}-ayudantia-{slug}"
    file_prefix = f"Clase {class_number} - Ayudantía {class_topic}"
    out_dir = args.root / folder_name

    student_path = out_dir / f"{file_prefix} - Ejercicios.ipynb"
    sol_path = out_dir / f"{file_prefix} - Solucionario.ipynb"

    # La carpeta puede existir de antemano (ej. con un Prompt.md de planificación);
    # solo bloqueamos si los notebooks ya fueron generados antes.
    if (student_path.exists() or sol_path.exists()) and not args.force:
        print(f"Ya existen notebooks en {out_dir}. Usa --force para sobreescribir.")
        return
    out_dir.mkdir(parents=True, exist_ok=True)

    student_path.write_text(
        json.dumps(build_student_notebook(proposal), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    sol_path.write_text(
        json.dumps(build_solucionario(proposal), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Generado:")
    print(f"  {student_path}  (subir a Colab)")
    print(f"  {sol_path}  (subir a Classroom despues)")


if __name__ == "__main__":
    main()
