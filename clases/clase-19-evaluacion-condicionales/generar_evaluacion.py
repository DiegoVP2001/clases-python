#!/usr/bin/env python3
"""
generar_evaluacion.py — Genera los notebooks de Clase 19 - Evaluación Condicionales.

Salida (en esta misma carpeta):
  Clase 19 - Evaluación Condicionales - Evaluación.ipynb    (estudiantes)
  Clase 19 - Evaluación Condicionales - Solucionario.ipynb  (profesor)

Uso:
  python generar_evaluacion.py
"""

import uuid


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


# ── Sección 1 — Ítems cortos (sin input, sin autocheck) ──────────────────────

ITEMS_1 = [
    dict(
        id="1.1", bloque="Bloque 1 — Booleanos y comparaciones", tipo="bug", pts=4,
        narrativa=(
            "El servidor privado de Discord del club de videojuegos del liceo "
            "solo deja entrar a quien escribe el **código de invitación** correcto."
        ),
        buggy=(
            "codigo_correcto = 4821\n"
            "codigo_ingresado = 4821\n"
            "\n"
            "if codigo_ingresado = codigo_correcto:\n"
            "    mensaje_discord = \"Acceso concedido al servidor.\"\n"
            "else:\n"
            "    mensaje_discord = \"Código incorrecto.\"\n"
            "\n"
            "print(mensaje_discord)"
        ),
        fixed=(
            "codigo_correcto = 4821\n"
            "codigo_ingresado = 4821\n"
            "\n"
            "if codigo_ingresado == codigo_correcto:\n"
            "    mensaje_discord = \"Acceso concedido al servidor.\"\n"
            "else:\n"
            "    mensaje_discord = \"Código incorrecto.\"\n"
            "\n"
            "print(mensaje_discord)"
        ),
        expected="Acceso concedido al servidor.",
    ),
    dict(
        id="1.2", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`and` simple",
        narrativa=(
            "En la Feria de la Vendimia de Isla de Maipo, puede instalar su "
            "stand de comida quien tenga **permiso municipal** Y haya "
            "**pagado el arriendo** del espacio."
        ),
        setup="tiene_permiso_municipal = True\npago_arriendo_stand = False",
        var="puede_instalar_stand", print_label="¿Puede instalar el stand?",
        expr="tiene_permiso_municipal and pago_arriendo_stand",
        expected=False,
    ),
    dict(
        id="1.3", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`var1 and (var2 or var3)`",
        narrativa=(
            "En el modo clasificatorio de un videojuego, puede entrar a la "
            "partida quien tenga la **cuenta verificada** Y además (haya "
            "alcanzado el **rango mínimo** O tenga una **invitación** de un "
            "jugador de rango alto)."
        ),
        setup=(
            "cuenta_verificada = True\n"
            "alcanzo_rango_minimo = False\n"
            "tiene_invitacion_rango_alto = True"
        ),
        var="puede_entrar_clasificatoria", print_label="¿Puede entrar a la clasificatoria?",
        expr="cuenta_verificada and (alcanzo_rango_minimo or tiene_invitacion_rango_alto)",
        expected=True,
    ),
    dict(
        id="1.4", bloque="Bloque 3 — Análisis de condiciones (caso límite)", tipo="bug", pts=5,
        narrativa=(
            "En el torneo de básquetbol del liceo, un equipo clasifica a "
            "semifinales cuando su puntaje **alcanza** el mínimo de la fase "
            "de grupos (no solo cuando lo supera)."
        ),
        buggy=(
            "puntaje_equipo = 18\n"
            "puntaje_minimo_clasificacion = 18\n"
            "\n"
            "if puntaje_equipo > puntaje_minimo_clasificacion:\n"
            "    mensaje_torneo = \"El equipo clasifica a semifinales.\"\n"
            "else:\n"
            "    mensaje_torneo = \"El equipo queda eliminado.\"\n"
            "\n"
            "print(mensaje_torneo)"
        ),
        fixed=(
            "puntaje_equipo = 18\n"
            "puntaje_minimo_clasificacion = 18\n"
            "\n"
            "if puntaje_equipo >= puntaje_minimo_clasificacion:\n"
            "    mensaje_torneo = \"El equipo clasifica a semifinales.\"\n"
            "else:\n"
            "    mensaje_torneo = \"El equipo queda eliminado.\"\n"
            "\n"
            "print(mensaje_torneo)"
        ),
        expected="El equipo clasifica a semifinales.",
    ),
    dict(
        id="1.5", bloque="Bloque 4 — if / else", tipo="bug", pts=4,
        narrativa=(
            "Antes de publicar un video en TikTok, el sistema revisa si "
            "pasó la verificación de **derechos de autor**."
        ),
        buggy=(
            "paso_revision_derechos = True\n"
            "\n"
            "if paso_revision_derechos\n"
            "    mensaje_tiktok = \"Video publicado con éxito.\"\n"
            "else:\n"
            "    mensaje_tiktok = \"Video retenido por derechos de autor.\"\n"
            "\n"
            "print(mensaje_tiktok)"
        ),
        fixed=(
            "paso_revision_derechos = True\n"
            "\n"
            "if paso_revision_derechos:\n"
            "    mensaje_tiktok = \"Video publicado con éxito.\"\n"
            "else:\n"
            "    mensaje_tiktok = \"Video retenido por derechos de autor.\"\n"
            "\n"
            "print(mensaje_tiktok)"
        ),
        expected="Video publicado con éxito.",
    ),
    dict(
        id="1.6", bloque="Bloque 5 — if anidados", tipo="bug", pts=4,
        narrativa=(
            "Un robot aspirador doméstico revisa primero si está "
            "**encendido**, y solo entonces si **detecta un obstáculo** en "
            "el camino."
        ),
        buggy=(
            "robot_encendido = True\n"
            "detecto_obstaculo = False\n"
            "\n"
            "if robot_encendido:\n"
            "    if detecto_obstaculo:\n"
            "    mensaje_robot = \"El robot esquiva el obstáculo.\"\n"
            "    else:\n"
            "        mensaje_robot = \"El robot sigue limpiando.\"\n"
            "else:\n"
            "    mensaje_robot = \"El robot está apagado.\"\n"
            "\n"
            "print(mensaje_robot)"
        ),
        fixed=(
            "robot_encendido = True\n"
            "detecto_obstaculo = False\n"
            "\n"
            "if robot_encendido:\n"
            "    if detecto_obstaculo:\n"
            "        mensaje_robot = \"El robot esquiva el obstáculo.\"\n"
            "    else:\n"
            "        mensaje_robot = \"El robot sigue limpiando.\"\n"
            "else:\n"
            "    mensaje_robot = \"El robot está apagado.\"\n"
            "\n"
            "print(mensaje_robot)"
        ),
        expected="El robot sigue limpiando.",
    ),
    dict(
        id="1.7", bloque="Bloque 6 — elif", tipo="bug", pts=5,
        narrativa=(
            "Una app de hábitos de estudio clasifica la racha de días "
            "seguidos estudiando en categorías, de la más exigente a la "
            "más básica."
        ),
        buggy=(
            "racha_dias_estudio = 12\n"
            "\n"
            "if racha_dias_estudio >= 3:\n"
            "    mensaje_racha = \"Racha en marcha: no la cortes.\"\n"
            "elif racha_dias_estudio >= 7:\n"
            "    mensaje_racha = \"Buena constancia.\"\n"
            "elif racha_dias_estudio >= 14:\n"
            "    mensaje_racha = \"Racha de élite.\"\n"
            "else:\n"
            "    mensaje_racha = \"Recién empezando.\"\n"
            "\n"
            "print(mensaje_racha)"
        ),
        fixed=(
            "racha_dias_estudio = 12\n"
            "\n"
            "if racha_dias_estudio >= 14:\n"
            "    mensaje_racha = \"Racha de élite.\"\n"
            "elif racha_dias_estudio >= 7:\n"
            "    mensaje_racha = \"Buena constancia.\"\n"
            "elif racha_dias_estudio >= 3:\n"
            "    mensaje_racha = \"Racha en marcha: no la cortes.\"\n"
            "else:\n"
            "    mensaje_racha = \"Recién empezando.\"\n"
            "\n"
            "print(mensaje_racha)"
        ),
        expected="Buena constancia.",
    ),
]


# ── Sección 2 — Programas completos (con input()) ────────────────────────────

EJERCICIOS_2 = [
    dict(
        num=1, titulo="Modo Fiesta de una playlist", estrellas="⭐ Fácil", pts=12,
        narrativa=(
            "Una playlist compartida arma automáticamente el \"Modo Fiesta\": "
            "cualquier canción con un nivel de energía alto entra a la lista; "
            "el resto se guarda para otro momento. Escribe el programa que, "
            "dado el nivel de energía de una canción, informe si entra o no "
            "al Modo Fiesta."
        ),
        debe=[
            "Pedir con `input()` el **nivel de energía de la canción** "
            "(**un número entero** entre 0 y 100)",
            "Verificar si la energía **alcanza el mínimo** para el Modo Fiesta (70)",
            "Mostrar un **mensaje distinto** según corresponda",
        ],
        ej1_in="70", ej1_out="¡Entra al Modo Fiesta! 🎉",
        ej2_in="45", ej2_out="Se guarda para otro momento.",
        solucion=(
            "nivel_energia_cancion = int(input(\"Ingresa el nivel de energía de la canción (0 a 100): \"))\n"
            "\n"
            "if nivel_energia_cancion >= 70:\n"
            "    print(\"¡Entra al Modo Fiesta! 🎉\")\n"
            "else:\n"
            "    print(\"Se guarda para otro momento.\")"
        ),
    ),
    dict(
        num=2, titulo="Micro a Talagante", estrellas="⭐⭐ Media", pts=16,
        narrativa=(
            "Para subir al micro que va desde Isla de Maipo hasta Talagante, "
            "el sistema revisa primero si la persona tiene pase escolar "
            "vigente; si no lo tiene, revisa si el saldo de su tarjeta bip "
            "alcanza para pagar el pasaje. Escribe el programa que, según "
            "esos datos, muestre cómo puede subir la persona."
        ),
        debe=[
            "Pedir con `input()` si tiene **pase escolar vigente** (la "
            "persona responde **exactamente** \"si\" o \"no\")",
            "Si **no** tiene pase, pedir además con `input()` el **saldo de "
            "la tarjeta bip** (**puede tener decimales**, en pesos)",
            "Verificar primero el pase escolar; solo si no lo tiene, "
            "verificar si el saldo **alcanza** el costo del pasaje (\\$800)",
            "Mostrar un **mensaje distinto** para cada uno de los tres "
            "caminos posibles",
        ],
        ej1_in="si", ej1_out="Sube gratis con su pase escolar.",
        ej2_in="no<br>500", ej2_out="No le alcanza el saldo para el pasaje.",
        solucion=(
            "tiene_pase_escolar = input(\"¿Tiene pase escolar vigente? (si/no): \")\n"
            "\n"
            "if tiene_pase_escolar == \"si\":\n"
            "    print(\"Sube gratis con su pase escolar.\")\n"
            "else:\n"
            "    saldo_tarjeta_bip = float(input(\"Ingresa el saldo de la tarjeta bip: \"))\n"
            "    if saldo_tarjeta_bip >= 800:\n"
            "        print(\"Paga el pasaje con la tarjeta bip.\")\n"
            "    else:\n"
            "        print(\"No le alcanza el saldo para el pasaje.\")"
        ),
    ),
    dict(
        num=3, titulo="Ahorro semanal", estrellas="⭐⭐ Media-alta", pts=18,
        narrativa=(
            "Una app ficticia de ahorro semanal clasifica cuánto guardaste "
            "esta semana en cuatro niveles, para motivarte a seguir "
            "ahorrando. Escribe el programa que, dado el monto ahorrado, "
            "muestre el nivel correspondiente."
        ),
        debe=[
            "Pedir con `input()` el **monto ahorrado esta semana** (**puede "
            "tener decimales**, en pesos)",
            "Clasificar el monto en **cuatro niveles**, del más bajo al más alto",
            "Mostrar un **mensaje claro** con el nivel obtenido",
        ],
        ej1_in="8000", ej1_out="Nivel: En camino.",
        ej2_in="31000.50", ej2_out="Nivel: ¡Excelente semana!",
        solucion=(
            "monto_ahorrado_semana = float(input(\"Ingresa el monto ahorrado esta semana: \"))\n"
            "\n"
            "if monto_ahorrado_semana < 5000:\n"
            "    print(\"Nivel: Recién empezando.\")\n"
            "elif monto_ahorrado_semana < 15000:\n"
            "    print(\"Nivel: En camino.\")\n"
            "elif monto_ahorrado_semana < 30000:\n"
            "    print(\"Nivel: Buen ahorro.\")\n"
            "else:\n"
            "    print(\"Nivel: ¡Excelente semana!\")"
        ),
    ),
    dict(
        num=4, titulo="Salas de matchmaking (desafío)", estrellas="⭐⭐⭐ Difícil", pts=24,
        narrativa=(
            "El sistema de emparejamiento de un videojuego arma las salas "
            "según el rango del jugador. Para el rango más alto, además "
            "revisa si el jugador tiene una racha de victorias activa, "
            "porque eso le da una sala especial. Escribe el programa que, "
            "dado el rango del jugador y —cuando corresponda— si tiene "
            "racha activa, muestre en qué sala queda."
        ),
        debe=[
            "Pedir con `input()` el **rango del jugador** (la persona "
            "responde **exactamente** una de estas palabras: \"bronce\", "
            "\"plata\" u \"oro\")",
            "Si el rango es **\"oro\"**, pedir además con `input()` si "
            "tiene **racha de victorias activa** (responde **exactamente** "
            "\"si\" o \"no\")",
            "Asignar la sala usando `elif` para los tres rangos, y anidar "
            "la pregunta de la racha solo dentro de la rama \"oro\"",
            "Mostrar un **mensaje distinto** con la sala asignada para "
            "cada camino posible",
        ],
        ej1_in="oro<br>si", ej1_out="Sala especial de racha activa.",
        ej2_in="plata", ej2_out="Sala de nivel plata.",
        solucion=(
            "rango_jugador = input(\"Ingresa tu rango (bronce/plata/oro): \")\n"
            "\n"
            "if rango_jugador == \"oro\":\n"
            "    tiene_racha_activa = input(\"¿Tienes racha de victorias activa? (si/no): \")\n"
            "    if tiene_racha_activa == \"si\":\n"
            "        print(\"Sala especial de racha activa.\")\n"
            "    else:\n"
            "        print(\"Sala de nivel oro.\")\n"
            "elif rango_jugador == \"plata\":\n"
            "    print(\"Sala de nivel plata.\")\n"
            "else:\n"
            "    print(\"Sala de nivel bronce.\")"
        ),
    ),
]


def tabla_html(ej1_in, ej1_out, ej2_in, ej2_out) -> str:
    return (
        "<table>\n"
        "<tr>\n  <th>Ejemplo 1</th>\n  <th>Ejemplo 2</th>\n</tr>\n"
        "<tr>\n"
        f"  <td>📥 <em>El usuario ingresa</em><pre>{ej1_in}</pre></td>\n"
        f"  <td>📥 <em>El usuario ingresa</em><pre>{ej2_in}</pre></td>\n"
        "</tr>\n"
        "<tr>\n"
        f"  <td>📤 <em>El programa imprime</em><pre>{ej1_out}</pre></td>\n"
        f"  <td>📤 <em>El programa imprime</em><pre>{ej2_out}</pre></td>\n"
        "</tr>\n"
        "</table>"
    )


def puntaje_tabla_md(rows, total_label="Total") -> str:
    lines = ["| Ítem | Contenido | Puntaje |", "|---|---|---|"]
    total = 0
    for label, contenido, pts in rows:
        lines.append(f"| {label} | {contenido} | {pts} pts |")
        total += pts
    lines.append(f"| **{total_label}** | | **{total} pts** |")
    return "\n".join(lines)


# ── Notebook de estudiantes ───────────────────────────────────────────────────

def build_student_notebook() -> dict:
    puntaje_rows = [(item["id"], item["bloque"], item["pts"]) for item in ITEMS_1]
    puntaje_rows += [
        (f"2.{ej['num']}", f"{ej['titulo']} ({ej['estrellas']})", ej["pts"])
        for ej in EJERCICIOS_2
    ]

    cells = [
        md_cell(
            "# 📝 Evaluación Individual — Condicionales\n\n"
            "**Fecha:** martes 21 de julio, 2026  |  **75 minutos**\n\n"
            "📅 **Fecha:** ___________________________  \n"
            "👤 **Nombre:** ___________________________  \n"
            "📌 **Curso:** ___________________________"
        ),
        md_cell(
            "---\n\n"
            "## 📋 Instrucciones generales\n\n"
            "- Esta evaluación tiene **2 secciones** y dura **75 minutos**.\n"
            "- Trabaja en orden y administra tu tiempo.\n"
            "- Entrega este notebook a través de **Google Classroom** antes "
            "de que termine la clase.\n"
            "- El código debe ejecutarse sin errores. Si no terminas un "
            "ejercicio, deja lo que alcanzaste.\n"
            "- Usa nombres de variables en **snake_case en español**.\n"
            "- Cuando un ejercicio pida un dato con `input()`, el enunciado "
            "siempre aclara si es un **número entero**, un **número con "
            "decimales**, o una **palabra exacta**.\n"
            "- **Prohibido** copiar código de compañeros."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts)\n\n"
            + puntaje_tabla_md(puntaje_rows)
        ),
        md_cell(
            "---\n\n## 🔥 Sección 1 — Ítems cortos (30 pts)\n\n"
            "Las variables ya están definidas. En **Arma la condición**, "
            "completa solo la línea que falta. En **Arregla el bug**, "
            "corrige el único error del fragmento."
        ),
    ]

    for item in ITEMS_1:
        tipo_label = "Arma la condición" if item["tipo"] == "arma" else "Arregla el bug"
        header = f"**Ítem {item['id']}** — {item['bloque']} — {tipo_label} ({item['pts']} pts)"
        if item["tipo"] == "arma":
            header += f"\n\n*{item['patron']}*"
        cells.append(md_cell(f"---\n\n{header}\n\n{item['narrativa']}"))
        if item["tipo"] == "arma":
            cells.append(code_cell(
                f"{item['setup']}\n\n"
                f"{item['var']} = \n\n"
                f"print(\"{item['print_label']}\", {item['var']})"
            ))
        else:
            cells.append(code_cell(item["buggy"]))

    cells.append(md_cell(
        "---\n\n## 💻 Sección 2 — Programas completos (70 pts)\n\n"
        "Programas completos desde una narrativa. Cada uno pide sus datos "
        "con `input()` — lee bien el tipo de dato que se espera antes de "
        "escribir tu código."
    ))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"---\n\n## 🎯 Ejercicio {ej['num']} — {ej['titulo']} "
            f"{ej['estrellas']} ({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + "\n\n"
            + tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        ))
        cells.append(code_cell(f"# Tu solución del Ejercicio {ej['num']}\n"))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin de la evaluación\n\n"
        "Revisa que todas las celdas se ejecuten sin errores antes de "
        "compartir el Colab con el profesor."
    ))

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Evaluación")


# ── Solucionario ──────────────────────────────────────────────────────────────

def build_solucionario_notebook() -> dict:
    puntaje_rows = [(item["id"], item["bloque"], item["pts"]) for item in ITEMS_1]
    puntaje_rows += [
        (f"2.{ej['num']}", f"{ej['titulo']} ({ej['estrellas']})", ej["pts"])
        for ej in EJERCICIOS_2
    ]

    cells = [
        md_cell(
            "# ✅ Solucionario — Evaluación Individual Condicionales\n\n"
            "Solo para el profesor. Incluye soluciones y pauta de puntaje."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts, exigencia 50%)\n\n"
            + puntaje_tabla_md(puntaje_rows)
            + "\n\nEscala: 50% de logro = nota 4.0 (nota = 1 + (pct/50)*3 si "
            "pct < 50%; nota = 4 + ((pct-50)/50)*3 si pct >= 50%, con pct "
            "= puntaje obtenido / 100 * 100)."
        ),
        md_cell("---\n\n## 🔥 Sección 1 — Ítems cortos"),
    ]

    for item in ITEMS_1:
        tipo_label = "Arma la condición" if item["tipo"] == "arma" else "Arregla el bug"
        cells.append(md_cell(
            f"**Ítem {item['id']}** — {item['bloque']} — {tipo_label} "
            f"({item['pts']} pts) — solución esperada:"
        ))
        if item["tipo"] == "arma":
            cells.append(code_cell(
                f"{item['setup']}\n\n"
                f"{item['var']} = {item['expr']}\n\n"
                f"print(\"{item['print_label']}\", {item['var']})  # Esperado: {item['expected']}"
            ))
        else:
            cells.append(code_cell(item["fixed"] + f"\n# Esperado: {item['expected']}"))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos"))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"### Ejercicio {ej['num']} — {ej['titulo']} {ej['estrellas']} "
            f"({ej['pts']} pts)"
        ))
        cells.append(code_cell(ej["solucion"]))

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Solucionario")


if __name__ == "__main__":
    import json
    import os

    base = os.path.dirname(os.path.abspath(__file__))

    student_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Evaluación.ipynb")
    sol_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Solucionario.ipynb")

    with open(student_path, "w", encoding="utf-8") as f:
        json.dump(build_student_notebook(), f, ensure_ascii=False, indent=1)

    with open(sol_path, "w", encoding="utf-8") as f:
        json.dump(build_solucionario_notebook(), f, ensure_ascii=False, indent=1)

    print("Generado:", student_path)
    print("Generado:", sol_path)
