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
# Orden: primero los 1A (Arma la condición), luego los 1B (Arregla el bug).
# "bloque" y "patron" son metadatos internos para el profesor (Solucionario);
# nunca se muestran en el notebook de estudiante.

ITEMS_1 = [
    dict(
        id="1A.1", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`and` simple",
        narrativa=(
            "El concurso de fotografía de Instagram del liceo solo acepta la "
            "publicación de quien tenga la **cuenta pública** Y haya usado el "
            "**hashtag oficial** del concurso."
        ),
        setup="cuenta_publica = True\nuso_hashtag_oficial = False",
        var="participa_concurso", print_label="¿Participa en el concurso?",
        expr="cuenta_publica and uso_hashtag_oficial",
        expected=False,
    ),
    dict(
        id="1A.2", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`var1 and (var2 or var3)`",
        narrativa=(
            "Para entrar al backstage de un festival de música, se necesita "
            "la **pulsera VIP** Y además (tener **acreditación de prensa** O "
            "**invitación del staff**)."
        ),
        setup=(
            "tiene_pulsera_vip = True\n"
            "tiene_acreditacion_prensa = False\n"
            "tiene_invitacion_staff = True"
        ),
        var="puede_entrar_backstage", print_label="¿Puede entrar al backstage?",
        expr="tiene_pulsera_vip and (tiene_acreditacion_prensa or tiene_invitacion_staff)",
        expected=True,
    ),
    dict(
        id="1B.1", bloque="Bloque 1 — Booleanos y comparaciones", tipo="bug", pts=4,
        narrativa=(
            "La máquina expendedora de bebidas del liceo solo entrega el "
            "producto cuando el monto insertado es **exactamente igual** al "
            "precio (no da vuelto)."
        ),
        buggy=(
            "precio_bebida = 900\n"
            "monto_insertado = 900\n"
            "\n"
            "if monto_insertado = precio_bebida:\n"
            "    mensaje_maquina = \"Bebida entregada.\"\n"
            "else:\n"
            "    mensaje_maquina = \"Monto incorrecto, no se entrega vuelto.\"\n"
            "\n"
            "print(mensaje_maquina)"
        ),
        fixed=(
            "precio_bebida = 900\n"
            "monto_insertado = 900\n"
            "\n"
            "if monto_insertado == precio_bebida:\n"
            "    mensaje_maquina = \"Bebida entregada.\"\n"
            "else:\n"
            "    mensaje_maquina = \"Monto incorrecto, no se entrega vuelto.\"\n"
            "\n"
            "print(mensaje_maquina)"
        ),
        expected="Bebida entregada.",
    ),
    dict(
        id="1B.2", bloque="Bloque 3 — Análisis de condiciones (caso límite)", tipo="bug", pts=5,
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
        id="1B.3", bloque="Bloque 4 — if / else", tipo="bug", pts=4,
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
        id="1B.4", bloque="Bloque 5 — if anidados", tipo="bug", pts=4,
        narrativa=(
            "Un parlante inteligente revisa primero si está **conectado a "
            "internet**, y solo entonces si **reconoció el comando de voz**."
        ),
        buggy=(
            "conectado_internet = True\n"
            "reconocio_comando = False\n"
            "\n"
            "if conectado_internet:\n"
            "    if reconocio_comando:\n"
            "    mensaje_parlante = \"El parlante ejecuta la acción pedida.\"\n"
            "    else:\n"
            "        mensaje_parlante = \"El parlante no entendió el comando.\"\n"
            "else:\n"
            "    mensaje_parlante = \"El parlante está desconectado.\"\n"
            "\n"
            "print(mensaje_parlante)"
        ),
        fixed=(
            "conectado_internet = True\n"
            "reconocio_comando = False\n"
            "\n"
            "if conectado_internet:\n"
            "    if reconocio_comando:\n"
            "        mensaje_parlante = \"El parlante ejecuta la acción pedida.\"\n"
            "    else:\n"
            "        mensaje_parlante = \"El parlante no entendió el comando.\"\n"
            "else:\n"
            "    mensaje_parlante = \"El parlante está desconectado.\"\n"
            "\n"
            "print(mensaje_parlante)"
        ),
        expected="El parlante no entendió el comando.",
    ),
    dict(
        id="1B.5", bloque="Bloque 6 — elif", tipo="bug", pts=5,
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
# Sin estrellas ni etiquetas de dificultad — solo título y puntaje.

EJERCICIOS_2 = [
    dict(
        num=1, titulo="Modo Fiesta de una playlist", pts=12,
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
        num=2, titulo="Micro a Talagante", pts=16,
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
            "la tarjeta bip** (un **número entero**, en pesos)",
            "Verificar primero el pase escolar; solo si no lo tiene, "
            "verificar si el saldo **alcanza** el costo del pasaje (\\$800)",
            "Mostrar el mensaje que corresponda a cada uno de estos tres "
            "caminos:\n"
            "  - Tiene pase escolar vigente → `\"Sube gratis con su pase escolar.\"`\n"
            "  - No tiene pase Y el saldo alcanza el pasaje → `\"Paga el pasaje con la tarjeta bip.\"`\n"
            "  - No tiene pase Y el saldo no alcanza → `\"No le alcanza el saldo para el pasaje.\"`",
        ],
        ej1_in="si", ej1_out="Sube gratis con su pase escolar.",
        ej2_in="no<br>500", ej2_out="No le alcanza el saldo para el pasaje.",
        solucion=(
            "tiene_pase_escolar = input(\"¿Tiene pase escolar vigente? (si/no): \")\n"
            "\n"
            "if tiene_pase_escolar == \"si\":\n"
            "    print(\"Sube gratis con su pase escolar.\")\n"
            "else:\n"
            "    saldo_tarjeta_bip = int(input(\"Ingresa el saldo de la tarjeta bip: \"))\n"
            "    if saldo_tarjeta_bip >= 800:\n"
            "        print(\"Paga el pasaje con la tarjeta bip.\")\n"
            "    else:\n"
            "        print(\"No le alcanza el saldo para el pasaje.\")"
        ),
    ),
    dict(
        num=3, titulo="Ahorro semanal en dólares", pts=18,
        narrativa=(
            "Una alcancía digital lleva el registro de cuánto ahorras en "
            "dólares cada semana — varias personas en Chile prefieren "
            "ahorrar en esta moneda para protegerse de la fluctuación del "
            "peso. Escribe el programa que, dado el monto ahorrado, "
            "muestre el nivel correspondiente."
        ),
        debe=[
            "Pedir con `input()` el **monto ahorrado esta semana, en "
            "dólares** (**puede tener decimales**)",
            "Clasificar el monto en estos 4 niveles:\n"
            "  - Menos de 10 dólares → `\"Nivel: Recién empezando.\"`\n"
            "  - Entre 10 y 29,99 dólares → `\"Nivel: En camino.\"`\n"
            "  - Entre 30 y 59,99 dólares → `\"Nivel: Buen ahorro.\"`\n"
            "  - 60 dólares o más → `\"Nivel: ¡Excelente semana!\"`",
        ],
        ej1_in="15", ej1_out="Nivel: En camino.",
        ej2_in="62.5", ej2_out="Nivel: ¡Excelente semana!",
        solucion=(
            "monto_ahorrado_semana = float(input(\"Ingresa cuántos dólares ahorraste esta semana: \"))\n"
            "\n"
            "if monto_ahorrado_semana < 10:\n"
            "    print(\"Nivel: Recién empezando.\")\n"
            "elif monto_ahorrado_semana < 30:\n"
            "    print(\"Nivel: En camino.\")\n"
            "elif monto_ahorrado_semana < 60:\n"
            "    print(\"Nivel: Buen ahorro.\")\n"
            "else:\n"
            "    print(\"Nivel: ¡Excelente semana!\")"
        ),
    ),
    dict(
        num=4, titulo="Sala de juego según tu rango", pts=24,
        narrativa=(
            "El sistema de un videojuego arma la sala de partida según el "
            "rango del jugador. Para el rango más alto, además revisa si "
            "el jugador tiene una racha de victorias activa, porque eso le "
            "da una sala especial. Escribe el programa que, dado el rango "
            "del jugador y —cuando corresponda— si tiene racha activa, "
            "muestre en qué sala queda."
        ),
        debe=[
            "Pedir con `input()` el **rango del jugador** (la persona "
            "responde **exactamente** una de estas palabras: \"bronce\", "
            "\"plata\" u \"oro\")",
            "Si el rango es **\"oro\"**, pedir además con `input()` si "
            "tiene **racha de victorias activa** (responde **exactamente** "
            "\"si\" o \"no\") — esta pregunta no se hace para los otros rangos",
            "Mostrar el mensaje que corresponda a cada uno de estos casos:\n"
            "  - rango \"bronce\" → `\"Sala de nivel bronce.\"`\n"
            "  - rango \"plata\" → `\"Sala de nivel plata.\"`\n"
            "  - rango \"oro\" sin racha activa → `\"Sala de nivel oro.\"`\n"
            "  - rango \"oro\" con racha activa → `\"Sala especial de racha activa.\"`",
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


def tipo_label(item) -> str:
    return "Arma la condición" if item["tipo"] == "arma" else "Arregla el bug"


# ── Notebook de estudiantes ───────────────────────────────────────────────────

def build_student_notebook() -> dict:
    puntaje_rows = [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_1]
    puntaje_rows += [
        (f"2.{ej['num']}", ej["titulo"], ej["pts"])
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
            "Repaso rápido de condicionales, dividido en dos partes."
        ),
    ]

    last_tipo = None
    for item in ITEMS_1:
        if item["tipo"] != last_tipo:
            if item["tipo"] == "arma":
                cells.append(md_cell(
                    "### 1A — Arma la condición\n\n"
                    "Las variables ya están definidas. Escribe **solo la "
                    "línea que falta** con la condición pedida."
                ))
            else:
                cells.append(md_cell(
                    "### 1B — Arregla el bug\n\n"
                    "Cada fragmento tiene un solo error. Corrígelo "
                    "directamente en la misma celda."
                ))
            last_tipo = item["tipo"]

        header = f"**Ítem {item['id']}** ({item['pts']} pts)"
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
            f"({ej['pts']} pts)\n\n"
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
        "compartir el Colab."
    ))

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Evaluación")


# ── Solucionario ──────────────────────────────────────────────────────────────

CRITERIOS_CORRECCION_MD = (
    "---\n\n## 🎯 Criterios de corrección\n\n"
    "**Enfoque de esta pauta: se evalúa la lógica de las condiciones, no la "
    "forma exacta del código.**\n\n"
    "- Acepta cualquier redacción de `print()` que distinga correctamente "
    "los casos — no exijas el mensaje literal del ejemplo.\n"
    "- Acepta nombres de variable distintos a los del ejemplo, siempre que "
    "sean coherentes, en español y se usen bien.\n"
    "- Acepta estructuras equivalentes (por ejemplo `if/elif/else` en vez "
    "de `if` anidados) si logran la misma partición de casos, salvo que el "
    "enunciado pida explícitamente una técnica.\n"
    "- Resta puntos solo por errores de lógica: operador de comparación "
    "incorrecto, caso límite mal manejado, rama faltante, tipo de dato mal "
    "leído desde `input()`, o código que no ejecuta.\n"
    "- No restes puntos por estilo de `print()` (comas vs. f-string), "
    "mensajes distintos si igual distinguen los casos, o el orden en que "
    "se definen variables antes del bloque condicional.\n\n"
    "*Nota: esto es un punto de partida. Al corregir, sigue calibrando la "
    "rúbrica en conjunto con Diego caso a caso — no asumas criterios de "
    "evaluaciones anteriores.*"
)


def build_solucionario_notebook() -> dict:
    puntaje_rows = [(item["id"], item["bloque"], item["pts"]) for item in ITEMS_1]
    puntaje_rows += [
        (f"2.{ej['num']}", ej["titulo"], ej["pts"])
        for ej in EJERCICIOS_2
    ]

    cells = [
        md_cell(
            "# ✅ Solucionario — Evaluación Individual Condicionales\n\n"
            "Solo para el profesor. Incluye soluciones y pauta de puntaje."
        ),
        md_cell(CRITERIOS_CORRECCION_MD),
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
        cells.append(md_cell(
            f"**Ítem {item['id']}** — {item['bloque']} — {tipo_label(item)} "
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
            f"### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)"
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
