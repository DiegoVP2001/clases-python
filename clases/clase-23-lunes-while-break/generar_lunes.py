"""Genera los notebooks del lunes estandar N°23 (While y Break).

Fuente de verdad: "Clase 23 - Lunes While y Break - Propuesta.json".
Nunca editar los .ipynb a mano: cambiar el JSON y volver a correr este script.

Produce:
  - Clase 23 - Lunes While y Break - Ejercitación.ipynb       (estudiantes, Colab)
  - Clase 23 - Lunes While y Break - Control.ipynb            (estudiantes, Classroom)
  - Clase 23 - Lunes While y Break - Control Solucionario.ipynb (profesor + agente corrector)

Uso:
    python generar_lunes.py            # genera los tres notebooks
    python generar_lunes.py --check    # solo verifica las soluciones contra los casos
"""

import argparse
import builtins
import contextlib
import io
import json
import sys
import uuid
from pathlib import Path

BASE = Path(__file__).resolve().parent
PROPUESTA = BASE / "Clase 23 - Lunes While y Break - Propuesta.json"


# ── Helpers de notebook ───────────────────────────────────────────────────────

def _cell_id() -> str:
    return uuid.uuid4().hex[:8]


def _source(text: str) -> list:
    lines = text.split("\n")
    return [line + "\n" for line in lines[:-1]] + [lines[-1]]


def md_cell(text: str) -> dict:
    return {"cell_type": "markdown", "id": _cell_id(), "metadata": {}, "source": _source(text)}


def code_cell(text: str = "") -> dict:
    return {
        "cell_type": "code",
        "id": _cell_id(),
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": _source(text) if text else [],
    }


def notebook(cells: list, colab_name: str) -> dict:
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


def bloque_ejemplo(test: dict) -> str:
    """Formato visual de caso de prueba: mismo lenguaje que las evaluaciones."""
    entradas = "\n".join(test["stdin"])
    return (
        "<p>📥 <em>El usuario ingresa:</em></p>\n"
        f"<pre>{entradas}</pre>\n"
        "<p>📤 <em>El programa imprime:</em></p>\n"
        f"<pre>{test['stdout']}</pre>"
    )


# ── Notebook 1: Ejercitación ──────────────────────────────────────────────────

def build_ejercitacion(data: dict) -> dict:
    ej = data["ejercitacion"]
    actitud = data["actitud"]
    cells = [
        md_cell(
            f"# 🔁 Clase {data['class_number']} — Ejercitación: While, continue y break\n\n"
            f"**Fecha:** {data['fecha']}  \n"
            "**Nombre:** _______________________  \n"
            "**Curso:** _______________________\n\n"
            "---"
        ),
        md_cell(
            f"## 🎯 Objetivo\n\n{data['objetivo']}\n\n"
            f"## 💡 Propósito\n\n> {actitud['proposito_md']}\n\n"
            f"{ej['modalidad_nota']}"
        ),
        md_cell(ej["recordatorio_md"]),
        md_cell("---\n\n## 🤝 Ejercicio guiado — lo resolvemos juntos"),
        md_cell(f"### {ej['guided_exercise']['title']}\n\n{ej['guided_exercise']['statement_md']}"),
        code_cell("# Tu programa"),
        md_cell("---\n\n## 🎯 Serie de ejercicios\n\nEscribe cada programa en su celda."),
    ]

    for numero, ex in enumerate(ej["exercises"], start=1):
        visible = next((t for t in ex["tests"] if not t["hidden"]), ex["tests"][0])
        cells.append(md_cell(
            f"### Ejercicio {numero} — {ex['title']}\n\n"
            f"{ex['statement_md']}\n\n"
            f"**Resultado esperado:**\n\n{bloque_ejemplo(visible)}"
        ))
        cells.append(code_cell(f"# Tu solución del Ejercicio {numero}"))

    # Sección final de soluciones colapsadas (excepción a la Restricción 5 del CLAUDE.md,
    # exclusiva del Colab de Ejercitación de los lunes estándar).
    cells.append(md_cell(
        "---\n\n## 🔓 Soluciones\n\n"
        "Ábrelas **después** de intentar el ejercicio: comparar tu programa con una "
        "solución posible es parte del entrenamiento. Ojo, es *una* solución, no *la* "
        "solución — si el tuyo hace lo mismo con otra estructura, también está bien."
    ))

    guiado = ej["guided_exercise"]
    cells.append(md_cell(
        f"<details>\n<summary>✅ Solución — Ejercicio guiado: {guiado['title']}</summary>\n\n"
        f"```python\n{guiado['solution_py']}\n```\n\n</details>"
    ))
    for numero, ex in enumerate(ej["exercises"], start=1):
        cells.append(md_cell(
            f"<details>\n<summary>✅ Solución — Ejercicio {numero}: {ex['title']}</summary>\n\n"
            f"```python\n{ex['solution_py']}\n```\n\n</details>"
        ))

    return notebook(cells, f"Clase {data['class_number']} - {data['class_topic']} - Ejercitación")


# ── Notebook 2: Control (estudiantes) ─────────────────────────────────────────

def build_control(data: dict) -> dict:
    ctrl = data["control"]
    actitud = data["actitud"]
    cells = [
        md_cell(
            # Título deliberadamente neutro: nombrar las tres estructuras acá delataría
            # qué usar en cada ítem, y la gracia del control es que eso lo decidan ellos.
            f"# ⚡ Clase {data['class_number']} — Control de Ciclos\n\n"
            f"**Fecha:** {data['fecha']}  \n"
            "**Nombre:** _______________________  \n"
            "**Curso:** _______________________\n\n"
            "---"
        ),
        md_cell(
            f"## 💪 Actitud del control: {actitud['nombre']}\n\n"
            f"{actitud['frase_control_md']}"
        ),
        md_cell(
            f"## 📋 Antes de partir\n\n{ctrl['modalidad_md']}\n\n"
            f"**Tiempo:** {ctrl['duracion_min']} minutos · **Puntaje total:** {ctrl['puntaje_total']} puntos"
        ),
    ]

    for item in ctrl["items"]:
        visible = next((t for t in item["tests"] if not t["hidden"]), item["tests"][0])
        cells.append(md_cell(
            f"---\n\n## Ítem {item['id']} — {item['title']} ({item['pts']} pts)\n\n"
            f"{item['statement_md']}\n\n"
            f"**Ejemplo válido:**\n\n{bloque_ejemplo(visible)}"
        ))
        cells.append(code_cell(f"# Tu solución del Ítem {item['id']}"))

    cierre = ctrl.get("cierre_actitud")
    if not cierre:
        raise ValueError(
            "Falta 'control.cierre_actitud' en la Propuesta — el CLAUDE.md exige preguntarle "
            "a Diego qué actitud y qué pregunta del banco usar antes de generar el Control."
        )
    cells.append(md_cell(
        "---\n\n## 🎯 Cierre — reflexión individual\n\n"
        f"{cierre['pregunta_md']}\n\n"
        "*(Esta pregunta no lleva nota — respóndela con confianza.)*"
    ))
    cells.append(md_cell("### 📝 Mi respuesta\n\n*(haz doble click para editar y escribir tu respuesta)*\n\n"))

    cells.append(md_cell(
        "---\n\n## ✅ Antes de entregar\n\n"
        "- Ejecuta cada celda una última vez para confirmar que tu programa corre.\n"
        "- Sube este mismo archivo a Classroom."
    ))

    return notebook(cells, f"Clase {data['class_number']} - {data['class_topic']} - Control")


# ── Notebook 3: Control Solucionario (profesor + agente corrector) ────────────

CRITERIOS_MD = (
    "---\n\n## 🎯 Criterios de corrección — instrucciones para el agente que revisa\n\n"
    "**Si estás corrigiendo este control, lee esto antes de calificar el primer ítem.**\n\n"
    "**Enfoque general: se evalúa que el programa haga lo que se pidió, no la forma exacta "
    "del código.** Los estudiantes no van a escribir lo mismo que la solución de referencia — "
    "eso es normal y no es un error.\n\n"
    "**Rúbrica parcelada por componentes.** Cada ítem se divide abajo en componentes "
    "independientes, cada uno con su propio presupuesto de puntos y sus tres niveles "
    "(✅ completo / ⚠️ parcial / ❌ cero). Un estudiante puede fallar un componente y "
    "conservar el puntaje de los demás. **Nunca descuentes el mismo error en dos "
    "componentes.**\n\n"
    "**No se evalúa eficiencia ni elegancia del código, solo lo que hace.** Ramas repetidas, "
    "condiciones de más, nombres de variable raros o pasos innecesarios NO descuentan. Solo "
    "descuenta lo que produce un resultado equivocado. Se califica el COMPORTAMIENTO y no la "
    "forma: una estructura reescrita o aplanada que produce el resultado correcto en todos "
    "los casos vale el puntaje completo.\n\n"
    "**Regla de oro: si dudas si algo es un error, no lo es.** Solo desciende de nivel cuando "
    "puedas señalar con precisión qué entrada distinta produciría un resultado equivocado.\n\n"
    "**Verifica ejecutando el código, no leyendo el output pegado en la celda.** Colab no "
    "re-ejecuta al editar, así que el resultado visible puede estar desactualizado. Corre cada "
    "programa contra los casos de prueba de este solucionario (los visibles y los ocultos).\n\n"
    "**Errores de corrección:** los reclaman los estudiantes. Si alguien plantea que un ítem "
    "quedó mal calificado, se revisa ese caso puntual — no hay auditoría entrega por entrega."
)


def build_control_solucionario(data: dict) -> dict:
    ctrl = data["control"]
    filas = "\n".join(
        f"| Ítem {i['id']} | {i['title']} | {i['concepto']} | {i['pts']} |" for i in ctrl["items"]
    )
    cells = [
        md_cell(
            f"# ✅ Solucionario del Control — Clase {data['class_number']}: While y Break\n\n"
            "**Solo para el profesor y para el agente que corrige.** No se sube a Classroom ni "
            "se pushea al repositorio antes de aplicado el control.\n\n"
            f"**Fecha de aplicación:** {data['fecha']} · "
            f"**Puntaje total:** {ctrl['puntaje_total']} pts · "
            f"**Exigencia:** {int(ctrl['exigencia'] * 100)}%"
        ),
        md_cell(
            f"## 📊 Distribución de puntaje (total {ctrl['puntaje_total']} pts)\n\n"
            "| Ítem | Título | Concepto | Pts |\n|---|---|---|---|\n" + filas
        ),
        md_cell(CRITERIOS_MD),
    ]

    for item in ctrl["items"]:
        casos = "\n".join(
            f"| {t['name']} | `{' / '.join(t['stdin'])}` | `{t['stdout']}` | "
            f"{'🔒 oculto' if t['hidden'] else '👁️ visible'} |"
            for t in item["tests"]
        )
        comps = "\n".join(
            f"| {c['nombre']} | {c['pts']} | {c['completo']} | {c['parcial'] or '—'} | {c['cero']} |"
            for c in item["componentes"]
        )
        suma = sum(c["pts"] for c in item["componentes"])
        nota = f"\n\n> **Nota de corrección:** {item['nota_correccion']}" if item.get("nota_correccion") else ""

        cells.append(md_cell(
            f"---\n\n## Ítem {item['id']} — {item['title']} ({item['pts']} pts)\n\n"
            f"**Concepto:** {item['concepto']}\n\n"
            f"**Qué evalúa:** {item['que_evalua']}\n\n"
            f"{item['statement_md']}"
        ))
        cells.append(code_cell(item["solution_py"]))
        cells.append(md_cell(
            f"### 🧪 Casos de prueba — Ítem {item['id']}\n\n"
            "| Caso | Entradas | Salida esperada | |\n|---|---|---|---|\n" + casos
        ))
        cells.append(md_cell(
            f"### 🔍 Rúbrica parcelada — Ítem {item['id']} ({suma} pts)\n\n"
            "| Componente | Pts | ✅ Completo | ⚠️ Parcial | ❌ Cero |\n|---|---|---|---|---|\n"
            + comps + nota
        ))

    return notebook(
        cells, f"Clase {data['class_number']} - {data['class_topic']} - Control Solucionario"
    )


# ── Verificación: corre cada solución contra sus casos ────────────────────────

def _ejecutar(codigo: str, entradas: list) -> str:
    """Ejecuta el código con las entradas dadas y devuelve solo lo impreso.

    Reemplaza input() por una versión que no escribe el prompt en stdout, para
    poder comparar la salida contra el stdout esperado sin ruido.
    """
    pendientes = list(entradas)

    def fake_input(prompt=""):
        if not pendientes:
            raise EOFError("El programa pidió más datos de los que trae el caso de prueba.")
        return pendientes.pop(0)

    salida = io.StringIO()
    original = builtins.input
    builtins.input = fake_input
    try:
        with contextlib.redirect_stdout(salida):
            exec(compile(codigo, "<solucion>", "exec"), {"__name__": "__main__"})
    finally:
        builtins.input = original
    return salida.getvalue().strip()


def verificar(data: dict) -> bool:
    piezas = [("Guiado", data["ejercitacion"]["guided_exercise"])]
    piezas += [(f"Ejercitación {n}", e) for n, e in enumerate(data["ejercitacion"]["exercises"], 1)]
    piezas += [(f"Control ítem {i['id']}", i) for i in data["control"]["items"]]

    ok = True
    for etiqueta, pieza in piezas:
        for test in pieza["tests"]:
            try:
                obtenido = _ejecutar(pieza["solution_py"], test["stdin"])
            except Exception as error:  # noqa: BLE001 — queremos reportar cualquier fallo
                print(f"  ERROR  {etiqueta} / {test['name']}: {type(error).__name__}: {error}")
                ok = False
                continue
            esperado = test["stdout"].strip()
            if obtenido == esperado:
                print(f"  OK     {etiqueta} / {test['name']}")
            else:
                ok = False
                print(f"  FALLA  {etiqueta} / {test['name']}")
                print(f"         esperado: {esperado!r}")
                print(f"         obtenido: {obtenido!r}")
    return ok


# ── Validación de puntajes ────────────────────────────────────────────────────

def validar_puntajes(data: dict) -> bool:
    ctrl = data["control"]
    ok = True
    total = 0
    for item in ctrl["items"]:
        suma = sum(c["pts"] for c in item["componentes"])
        total += item["pts"]
        if suma != item["pts"]:
            print(f"  FALLA  Ítem {item['id']}: componentes suman {suma}, el ítem declara {item['pts']}")
            ok = False
        else:
            print(f"  OK     Ítem {item['id']}: componentes suman {suma} pts")
    if total != ctrl["puntaje_total"]:
        print(f"  FALLA  Los ítems suman {total}, el control declara {ctrl['puntaje_total']}")
        ok = False
    else:
        print(f"  OK     Los ítems suman {total} pts")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="solo verificar, no escribir notebooks")
    args = parser.parse_args()

    data = json.loads(PROPUESTA.read_text(encoding="utf-8"))
    prefijo = f"Clase {data['class_number']} - {data['class_topic']}"

    print("Verificando puntajes de la rúbrica...")
    puntajes_ok = validar_puntajes(data)
    print("\nVerificando soluciones contra sus casos de prueba...")
    soluciones_ok = verificar(data)

    if not (puntajes_ok and soluciones_ok):
        print("\n❌ Hay fallas. No se escribió ningún notebook.")
        return 1

    if args.check:
        print("\n✅ Todo correcto (modo --check, sin escribir archivos).")
        return 0

    salidas = [
        (f"{prefijo} - Ejercitación.ipynb", build_ejercitacion(data)),
        (f"{prefijo} - Control.ipynb", build_control(data)),
        (f"{prefijo} - Control Solucionario.ipynb", build_control_solucionario(data)),
    ]
    print()
    for nombre, nb in salidas:
        destino = BASE / nombre
        destino.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  escrito  {nombre}  ({len(nb['cells'])} celdas)")

    print("\n✅ Listo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
