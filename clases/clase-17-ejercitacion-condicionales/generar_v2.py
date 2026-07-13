#!/usr/bin/env python3
"""
generar_v2.py — Genera los notebooks de Clase 17 - Ejercitación Evaluación.

Salida (en esta misma carpeta):
  Clase 17 - Ejercitación Evaluación - Clase.ipynb        (estudiantes)
  Clase 17 - Ejercitación Evaluación - Solucionario.ipynb (profesor)

Uso:
  python generar_v2.py
"""

import uuid


def _cell_id() -> str:
    return str(uuid.uuid4())[:8]


def md_cell(source: str) -> dict:
    lines = source.split("\n")
    source_list = [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
    return {"cell_type": "markdown", "id": _cell_id(), "metadata": {}, "source": source_list}


def code_cell(source: str = "", form: bool = False) -> dict:
    if source:
        lines = source.split("\n")
        source_list = [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
    else:
        source_list = []
    return {
        "cell_type": "code",
        "id": _cell_id(),
        "execution_count": None,
        "metadata": {"cellView": "form"} if form else {},
        "outputs": [],
        "source": source_list,
    }


def fn_name(item_id: str) -> str:
    return "verificar_" + item_id.replace(".", "_")


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


# ── Práctica Guiada (recuperada de la Clase 17 original, sin cambios) ────────

GUIADA_MD = (
    "---\n\n## 🧭 Práctica Guiada — repaso del patrón `elif` con `if` anidado\n\n"
    "**Situación:** Un local registra el monto de una compra y si la persona "
    "tiene tarjeta de fidelización, para decidir qué descuento aplicar.\n\n"
    "```python\n"
    "monto_compra = 12000\n"
    "tiene_tarjeta = True\n"
    "```\n\n"
    "<table>\n"
    "<tr>\n  <th>Qué debe hacer tu programa</th>\n  <th>Resultado esperado</th>\n</tr>\n"
    "<tr>\n"
    "  <td>Paso 1: Crea las variables del monto y la tarjeta, y escribe el "
    "<code>if</code> para compras muy bajas (menos de \\$5.000)</td>\n"
    "  <td><pre>(no se ejecuta con este monto — sigue evaluando)</pre></td>\n"
    "</tr>\n"
    "<tr>\n"
    "  <td>Paso 2: Agrega el <code>elif</code> para el rango medio (entre "
    "\\$5.000 y \\$19.999), y dentro de él anida un <code>if</code>/<code>else</code> "
    "según si tiene tarjeta</td>\n"
    "  <td><pre>Tienes 10% de descuento por ser socio.</pre></td>\n"
    "</tr>\n"
    "<tr>\n"
    "  <td>Paso 3: Cierra con el <code>else</code> final para compras de "
    "\\$20.000 o más</td>\n"
    "  <td><pre>(no se ejecuta con este monto)</pre></td>\n"
    "</tr>\n"
    "</table>"
)

GUIADA_CODE = "# Tu programa\n"


# ── Datos de los ítems de la Sección 1A — Arma la condición ──────────────────

ITEMS_1A = [
    dict(
        id="1A.1", patron="`and` simple",
        narrativa=(
            "En el taller de música del liceo, puede sumarse al ensayo de hoy "
            "quien traiga su **instrumento** Y haya **confirmado asistencia** con anticipación."
        ),
        setup='tiene_instrumento = True\nconfirmo_asistencia = False',
        var="puede_ensayar", print_label="¿Puede ensayar hoy?",
        expr="tiene_instrumento and confirmo_asistencia",
        expected=False,
    ),
    dict(
        id="1A.2", patron="`or` simple",
        narrativa=(
            "La feria de emprendedores de Isla de Maipo da **descuento** a quien "
            "sea **vecino de la comuna** O tenga **carnet de estudiante** vigente."
        ),
        setup='es_vecino_isla_maipo = False\ntiene_carnet_estudiante = True',
        var="tiene_descuento", print_label="¿Tiene descuento en la feria?",
        expr="es_vecino_isla_maipo or tiene_carnet_estudiante",
        expected=True,
    ),
    dict(
        id="1A.3", patron="`var1 and (var2 or var3)`",
        narrativa=(
            "En el torneo de fútbol escolar, juega el partido quien esté "
            "**inscrito en el equipo** Y además (tenga la **camiseta oficial** "
            "O haya **pagado la cuota** del torneo)."
        ),
        setup=(
            "esta_inscrito_equipo = True\n"
            "tiene_camiseta_oficial = False\n"
            "pago_cuota_torneo = False"
        ),
        var="puede_jugar", print_label="¿Puede jugar el partido?",
        expr="esta_inscrito_equipo and (tiene_camiseta_oficial or pago_cuota_torneo)",
        expected=False,
    ),
    dict(
        id="1A.4", patron="`(var1 and var2) or var3`",
        narrativa=(
            "La biblioteca del liceo presta libros a quien (sea **alumno regular** "
            "Y no tenga **multas pendientes**) O sea **profesor** del establecimiento."
        ),
        setup=(
            "es_alumno_regular = False\n"
            "sin_multas_pendientes = True\n"
            "es_profesor = True"
        ),
        var="puede_retirar_libro", print_label="¿Puede retirar el libro?",
        expr="(es_alumno_regular and sin_multas_pendientes) or es_profesor",
        expected=True,
    ),
    dict(
        id="1A.5", patron="`not(var1) and (var2 and var3)`",
        narrativa=(
            "El campeonato escolar de e-sports abre un cupo tardío para quien "
            "**NO** haya **seleccionado equipo** todavía, Y además (tenga una "
            "**cuenta válida** Y haya **aceptado el reglamento**)."
        ),
        setup=(
            "ya_selecciono_equipo = False\n"
            "tiene_cuenta_valida = True\n"
            "acepto_reglamento = False"
        ),
        var="puede_inscribirse_tarde", print_label="¿Puede inscribirse en el cupo tardío?",
        expr="not(ya_selecciono_equipo) and (tiene_cuenta_valida and acepto_reglamento)",
        expected=False,
    ),
]


# ── Datos de los ítems de la Sección 1B — Arregla el bug ─────────────────────

ITEMS_1B = [
    dict(
        id="1B.1", bloque="Bloque 3 — Análisis de condiciones (caso límite)",
        narrativa=(
            "El cine escolar considera la sala **llena** cuando se **alcanza** "
            "la capacidad máxima (no solo cuando la supera)."
        ),
        buggy=(
            "entradas_vendidas = 120\n"
            "capacidad_maxima = 120\n"
            "\n"
            "if entradas_vendidas > capacidad_maxima:\n"
            "    mensaje_cine = \"Sala llena, no se puede vender más.\"\n"
            "else:\n"
            "    mensaje_cine = \"Aún quedan entradas disponibles.\"\n"
            "\n"
            "print(mensaje_cine)"
        ),
        var="mensaje_cine",
        expected="Sala llena, no se puede vender más.",
    ),
    dict(
        id="1B.2", bloque="Bloque 1 — Booleanos y comparaciones",
        narrativa=(
            "El sistema de acceso al laboratorio de computación compara la clave "
            "ingresada con la clave correcta."
        ),
        buggy=(
            "clave_correcta = 4821\n"
            "clave_ingresada = 4821\n"
            "\n"
            "if clave_ingresada = clave_correcta:\n"
            "    mensaje_lab = \"Acceso concedido al laboratorio.\"\n"
            "else:\n"
            "    mensaje_lab = \"Clave incorrecta.\"\n"
            "\n"
            "print(mensaje_lab)"
        ),
        var="mensaje_lab",
        expected="Acceso concedido al laboratorio.",
    ),
    dict(
        id="1B.3", bloque="Bloque 4 — if / else",
        narrativa=(
            "El sistema de reservas de la sala de ensayo confirma la reserva "
            "si hay sala disponible."
        ),
        buggy=(
            "hay_sala_disponible = True\n"
            "\n"
            "if hay_sala_disponible\n"
            "    mensaje_sala = \"Sala reservada con éxito.\"\n"
            "else:\n"
            "    mensaje_sala = \"No hay salas disponibles hoy.\"\n"
            "\n"
            "print(mensaje_sala)"
        ),
        var="mensaje_sala",
        expected="Sala reservada con éxito.",
    ),
    dict(
        id="1B.4", bloque="Bloque 5 — if anidados",
        narrativa=(
            "El taller de robótica revisa primero si estás inscrito, y solo "
            "entonces si ya tienes equipo de trabajo asignado."
        ),
        buggy=(
            "esta_inscrito_taller = True\n"
            "tiene_equipo_asignado = False\n"
            "\n"
            "if esta_inscrito_taller:\n"
            "    if tiene_equipo_asignado:\n"
            "    mensaje_robotica = \"Puedes comenzar tu proyecto de robótica.\"\n"
            "    else:\n"
            "        mensaje_robotica = \"Debes esperar la asignación de equipo.\"\n"
            "else:\n"
            "    mensaje_robotica = \"Primero debes inscribirte en el taller.\"\n"
            "\n"
            "print(mensaje_robotica)"
        ),
        var="mensaje_robotica",
        expected="Debes esperar la asignación de equipo.",
    ),
    dict(
        id="1B.5", bloque="Bloque 6 — elif",
        narrativa=(
            "El maratón de baile clasifica el puntaje en categorías. Recuerda: "
            "las condiciones deben ir ordenadas de la más específica a la más general."
        ),
        buggy=(
            "puntaje_participante = 72\n"
            "\n"
            "if puntaje_participante >= 40:\n"
            "    mensaje_talento = \"Categoría: Bronce\"\n"
            "elif puntaje_participante >= 60:\n"
            "    mensaje_talento = \"Categoría: Plata\"\n"
            "elif puntaje_participante >= 80:\n"
            "    mensaje_talento = \"Categoría: Oro\"\n"
            "else:\n"
            "    mensaje_talento = \"Categoría: Sin clasificar\"\n"
            "\n"
            "print(mensaje_talento)"
        ),
        var="mensaje_talento",
        expected="Categoría: Plata",
    ),
]


# ── Datos de la Sección 2 — Programas completos ──────────────────────────────

EJERCICIOS_2 = [
    dict(
        num=1, titulo="Kiosco escolar", decimas=1,
        narrativa=(
            "El kiosco del colegio hace una promoción en el recreo: si el monto de la "
            "compra supera cierto mínimo, la persona se lleva una bebida de regalo. "
            "Escribe el programa que, dado el monto de la compra, informe si obtiene "
            "el regalo o no."
        ),
        debe=[
            "Registrar el **monto de la compra** como variable al inicio",
            "Verificar si el monto **alcanza el mínimo** para el regalo (\\$1.500)",
            "Mostrar un **mensaje distinto** según corresponda",
        ],
        ej1_in="monto_compra_kiosko = 1200", ej1_out="Aún no alcanzas el monto para el regalo.",
        ej2_in="monto_compra_kiosko = 1800", ej2_out="¡Compra premiada! Llévate una bebida de regalo.",
        solucion=(
            "monto_compra_kiosko = 1200\n"
            "minimo_para_regalo = 1500\n"
            "\n"
            "if monto_compra_kiosko >= minimo_para_regalo:\n"
            "    print(\"¡Compra premiada! Llévate una bebida de regalo.\")\n"
            "else:\n"
            "    print(\"Aún no alcanzas el monto para el regalo.\")"
        ),
    ),
    dict(
        num=2, titulo="Audiciones del taller de teatro", decimas=1,
        narrativa=(
            "El taller de teatro hace audiciones para la obra de fin de año. El sistema "
            "revisa dos cosas en orden: primero si la persona se inscribió a tiempo, y "
            "solo si lo hizo, si preparó un monólogo. Escribe el programa que informe el "
            "resultado según ambas condiciones."
        ),
        debe=[
            "Registrar si **se inscribió a tiempo** y si **preparó un monólogo**",
            "Verificar primero si se **inscribió a tiempo**",
            "Solo si se inscribió, verificar si **preparó el monólogo**",
            "Mostrar un **mensaje distinto** para cada uno de los tres caminos posibles",
        ],
        ej1_in="se_inscribio_a_tiempo = True\npreparo_monologo = False",
        ej1_out="Inscrito, pero debes preparar un monólogo antes de audicionar.",
        ej2_in="se_inscribio_a_tiempo = False\npreparo_monologo = False",
        ej2_out="Las inscripciones para la audición ya cerraron.",
        solucion=(
            "se_inscribio_a_tiempo = True\n"
            "preparo_monologo = False\n"
            "\n"
            "if se_inscribio_a_tiempo:\n"
            "    if preparo_monologo:\n"
            "        print(\"Pasas a la audición final.\")\n"
            "    else:\n"
            "        print(\"Inscrito, pero debes preparar un monólogo antes de audicionar.\")\n"
            "else:\n"
            "    print(\"Las inscripciones para la audición ya cerraron.\")"
        ),
    ),
    dict(
        num=3, titulo="Reloj del torneo de ajedrez", decimas=1,
        narrativa=(
            "En un torneo de ajedrez escolar, el reloj de cada jugador clasifica su "
            "situación según los minutos restantes. Escribe el programa que, dados los "
            "minutos restantes, muestre la categoría correspondiente."
        ),
        debe=[
            "Registrar los **minutos restantes** del reloj como variable al inicio",
            "Clasificar el estado usando **cuatro categorías** según el tiempo",
            "Mostrar un **mensaje claro** con la categoría obtenida",
        ],
        ej1_in="minutos_restantes_reloj = 3", ej1_out="Zeitnot: quedan menos de 5 minutos.",
        ej2_in="minutos_restantes_reloj = 0", ej2_out="Tiempo agotado: partida perdida por tiempo.",
        solucion=(
            "minutos_restantes_reloj = 3\n"
            "\n"
            "if minutos_restantes_reloj <= 0:\n"
            "    print(\"Tiempo agotado: partida perdida por tiempo.\")\n"
            "elif minutos_restantes_reloj <= 5:\n"
            "    print(\"Zeitnot: quedan menos de 5 minutos.\")\n"
            "elif minutos_restantes_reloj <= 15:\n"
            "    print(\"Tiempo ajustado: administra bien tus jugadas.\")\n"
            "else:\n"
            "    print(\"Tiempo cómodo: aún te queda bastante reloj.\")"
        ),
    ),
    dict(
        num=4, titulo="Transporte compartido al concierto (desafío)", decimas=2,
        narrativa=(
            "Un grupo del liceo organiza transporte compartido en van para ir a un "
            "concierto, según cuántos cupos quedan disponibles. Cuando quedan pocos "
            "cupos, el sistema revisa además si la persona ya pagó la reserva, porque "
            "eso le da prioridad frente al resto. Escribe el programa que, dados los "
            "cupos restantes y si la persona pagó la reserva, muestre el resultado "
            "correspondiente."
        ),
        debe=[
            "Registrar los **cupos restantes** de la van y si **pagó la reserva**",
            "Verificar primero si los cupos **se agotaron**",
            "Si quedan **pocos cupos** (5 o menos), verificar además el **pago de la reserva**",
            "Si quedan **muchos cupos**, mostrar que hay disponibilidad sin restricciones",
        ],
        ej1_in="cupos_restantes_van = 4\npago_reserva = True",
        ej1_out="Tienes prioridad de cupo por tu reserva pagada.",
        ej2_in="cupos_restantes_van = 4\npago_reserva = False",
        ej2_out="Quedan pocos cupos — sin reserva pagada debes esperar confirmación.",
        solucion=(
            "cupos_restantes_van = 4\n"
            "pago_reserva = True\n"
            "\n"
            "if cupos_restantes_van == 0:\n"
            "    print(\"Cupos agotados en la van.\")\n"
            "elif cupos_restantes_van <= 5:\n"
            "    if pago_reserva:\n"
            "        print(\"Tienes prioridad de cupo por tu reserva pagada.\")\n"
            "    else:\n"
            "        print(\"Quedan pocos cupos — sin reserva pagada debes esperar confirmación.\")\n"
            "else:\n"
            "    print(\"Hay cupos disponibles sin restricciones.\")"
        ),
    ),
]


def tabla_html(ej1_in, ej1_out, ej2_in, ej2_out) -> str:
    return (
        "<table>\n"
        "<tr>\n  <th>Ejemplo 1</th>\n  <th>Ejemplo 2</th>\n</tr>\n"
        "<tr>\n"
        f"  <td>📥 <em>El usuario escribe</em><pre>{ej1_in}</pre></td>\n"
        f"  <td>📥 <em>El usuario escribe</em><pre>{ej2_in}</pre></td>\n"
        "</tr>\n"
        "<tr>\n"
        f"  <td>📤 <em>El programa imprime</em><pre>{ej1_out}</pre></td>\n"
        f"  <td>📤 <em>El programa imprime</em><pre>{ej2_out}</pre></td>\n"
        "</tr>\n"
        "</table>"
    )


# ── Notebook de estudiantes ───────────────────────────────────────────────────

def build_student_notebook() -> dict:
    cells = [
        md_cell(
            "# 🎯 Ejercitación Evaluación — Repaso para la Evaluación de Condicionales\n\n"
            "📅 **Fecha:** ___________________________  \n"
            "👤 **Nombre:** ___________________________  \n"
            "📌 **Curso:** ___________________________\n\n"
            "**Vale hasta +6 décimas en total:** +1 décima por completar la Sección 1 "
            "(Calentamiento) y hasta +5 décimas en la Sección 2 (Programas completos)."
        ),
        md_cell(
            "---\n\n"
            "## 📋 Instrucciones\n\n"
            "- Escribe tu código en las celdas grises debajo de cada enunciado.\n"
            "- En la **Sección 1**, las variables ya están definidas — completa solo la "
            "línea que falta (o corrige el error, según corresponda).\n"
            "- Cada ítem de la Sección 1 ya trae su propia verificación al final de la "
            "misma celda: al ejecutarla (**Shift + Enter**) vas a ver de inmediato si "
            "tu respuesta está correcta.\n"
            "- **No modifiques los enunciados.**\n"
            "- Al terminar, comparte el Colab con el profesor desde el botón **Compartir**."
        ),
        md_cell(GUIADA_MD),
        code_cell(GUIADA_CODE),
        md_cell(
            "---\n\n**🔧 Configuración** — ejecuta esta celda primero (Shift + Enter). "
            "No necesitas entender ni editar su contenido."
        ),
        code_cell(_build_setup_cell_source(), form=True),
        md_cell(
            "---\n\n"
            "## 🔥 Sección 1 — Calentamiento rápido\n\n"
            "Ítems cortos para repasar antes de los programas completos. "
            "Vale **+1 décima en bloque** si completas y pasas la verificación de "
            "los 10 ítems (1A + 1B)."
        ),
        md_cell(
            "### 1A — Arma la condición\n\n"
            "Las variables ya están definidas. Escribe **solo la línea que falta** "
            "con la condición pedida y ejecuta para ver el resultado y la verificación."
        ),
    ]

    for item in ITEMS_1A:
        cells.append(md_cell(
            f"---\n\n**Ítem {item['id']}** — {item['patron']}\n\n{item['narrativa']}"
        ))
        cells.append(code_cell(
            f"{item['setup']}\n\n"
            f"{item['var']} = \n\n"
            f"print(\"{item['print_label']}\", {item['var']})\n"
            f"{fn_name(item['id'])}({item['var']})"
        ))

    cells.append(md_cell(
        "### 1B — Arregla el bug\n\n"
        "Cada fragmento tiene un solo error. Corrígelo directamente en la misma "
        "celda y ejecuta para comprobar (la verificación ya está al final del código)."
    ))

    for item in ITEMS_1B:
        cells.append(md_cell(
            f"---\n\n**Ítem {item['id']}** — {item['bloque']}\n\n{item['narrativa']}"
        ))
        cells.append(code_cell(item["buggy"] + f"\n{fn_name(item['id'])}({item['var']})"))

    cells.append(md_cell(
        "---\n\n## 💻 Sección 2 — Programas completos\n\n"
        "Ahora sí: programas completos desde una narrativa, igual que en la "
        "Clase 17 original. Aquí se juega el resto de las décimas."
    ))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"---\n\n## 🎯 Ejercicio {ej['num']} — {ej['titulo']} "
            f"(+{ej['decimas']} décima{'s' if ej['decimas'] > 1 else ''})\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + "\n\n"
            + tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        ))
        cells.append(code_cell(f"# Tu solución del Ejercicio {ej['num']}\n"))

    cells.append(md_cell(
        "---\n\n## 🏁 Cierre\n\n"
        "Con esto repasaste los 7 bloques de la evaluación: booleanos, operadores "
        "lógicos, análisis de condiciones, if/else, if anidados, elif, y criterio "
        "de selección. Si te quedó algún bloque incómodo, repásalo antes del "
        "martes 21 de julio."
    ))

    return notebook(cells, "Clase 17 - Ejercitación Evaluación - Clase")


def _build_setup_cell_source() -> str:
    parts = []
    for item in ITEMS_1A:
        parts.append(
            f"def {fn_name(item['id'])}(valor):\n"
            "    try:\n"
            f"        assert valor == {item['expected']}, \"Revisa tu condición: "
            "el resultado no es el esperado para este caso.\"\n"
            f"        print(\"✅ ¡Muy bien! El ítem {item['id']} está correcto.\")\n"
            "    except AssertionError as e:\n"
            "        print(\"❌\", e)\n"
        )
    for item in ITEMS_1B:
        parts.append(
            f"def {fn_name(item['id'])}(valor):\n"
            "    try:\n"
            f"        assert valor == \"{item['expected']}\", \"El mensaje no "
            "coincide con el esperado para este caso — revisa el bug de nuevo.\"\n"
            f"        print(\"✅ ¡Muy bien! El ítem {item['id']} está correcto.\")\n"
            "    except AssertionError as e:\n"
            "        print(\"❌\", e)\n"
        )
    return "#@title 🔧 Configuración automática (no la edites)\n\n" + "\n".join(parts)


# ── Solucionario ──────────────────────────────────────────────────────────────

def build_solucionario_notebook() -> dict:
    cells = [
        md_cell(
            "# ✅ Solucionario — Ejercitación Evaluación\n\n"
            "Solo para el profesor. Incluye soluciones y pauta de décimas."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de décimas (total +6)\n\n"
            "| Sección | Décimas | Cómo se otorgan |\n"
            "|---|---|---|\n"
            "| 1 — Calentamiento (1A + 1B, 10 ítems) | +1 | En bloque: se otorga si "
            "el notebook entregado muestra los 10 \"✅ ¡Muy bien!\" impresos "
            "(revisión visual al recibir en Classroom) |\n"
            "| 2 — Ej. 1, 2, 3 | +1 cada uno | Corrección en vivo o revisión de "
            "Classroom |\n"
            "| 2 — Ej. 4 (desafío) | +2 | Corrección en vivo o revisión de "
            "Classroom |\n\n"
            "Estas +6 décimas son independientes de las +5 décimas ya otorgadas en "
            "la Clase 17 original (archivada en `old/`) — no se suman entre sí."
        ),
        md_cell("---\n\n## 🧭 Práctica Guiada — descuentos por compra"),
        code_cell(
            "monto_compra = 12000\n"
            "tiene_tarjeta = True\n"
            "\n"
            "if monto_compra < 5000:\n"
            "    print(\"Compra muy baja: sin descuento por ahora.\")\n"
            "elif monto_compra < 20000:\n"
            "    if tiene_tarjeta:\n"
            "        print(\"Tienes 10% de descuento por ser socio.\")\n"
            "    else:\n"
            "        print(\"Sin descuento — hazte socio para la próxima.\")\n"
            "else:\n"
            "    print(\"Compra alta: 15% de descuento automático.\")"
        ),
        md_cell("---\n\n## 🔥 Sección 1A — Arma la condición"),
    ]

    for item in ITEMS_1A:
        cells.append(md_cell(f"**Ítem {item['id']}** — solución esperada:"))
        cells.append(code_cell(
            f"{item['setup']}\n\n"
            f"{item['var']} = {item['expr']}\n\n"
            f"print(\"{item['print_label']}\", {item['var']})  # Esperado: {item['expected']}"
        ))

    cells.append(md_cell("---\n\n## 🐛 Sección 1B — Arregla el bug"))

    for item in ITEMS_1B:
        fixed = {
            "1B.1": item["buggy"].replace(
                "entradas_vendidas > capacidad_maxima",
                "entradas_vendidas >= capacidad_maxima",
            ),
            "1B.2": item["buggy"].replace(
                "if clave_ingresada = clave_correcta:",
                "if clave_ingresada == clave_correcta:",
            ),
            "1B.3": item["buggy"].replace(
                "if hay_sala_disponible\n",
                "if hay_sala_disponible:\n",
            ),
            "1B.4": item["buggy"].replace(
                "    if tiene_equipo_asignado:\n    mensaje_robotica",
                "    if tiene_equipo_asignado:\n        mensaje_robotica",
            ),
            "1B.5": (
                "puntaje_participante = 72\n\n"
                "if puntaje_participante >= 80:\n"
                "    mensaje_talento = \"Categoría: Oro\"\n"
                "elif puntaje_participante >= 60:\n"
                "    mensaje_talento = \"Categoría: Plata\"\n"
                "elif puntaje_participante >= 40:\n"
                "    mensaje_talento = \"Categoría: Bronce\"\n"
                "else:\n"
                "    mensaje_talento = \"Categoría: Sin clasificar\"\n\n"
                "print(mensaje_talento)"
            ),
        }[item["id"]]
        cells.append(md_cell(f"**Ítem {item['id']}** — bug y corrección:"))
        cells.append(code_cell(fixed))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos"))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"### Ejercicio {ej['num']} — {ej['titulo']} (+{ej['decimas']} décimas)"
        ))
        cells.append(code_cell(ej["solucion"]))

    return notebook(cells, "Clase 17 - Ejercitación Evaluación - Solucionario")


if __name__ == "__main__":
    import json
    import os

    base = os.path.dirname(os.path.abspath(__file__))

    student_path = os.path.join(base, "Clase 17 - Ejercitación Evaluación - Clase.ipynb")
    sol_path = os.path.join(base, "Clase 17 - Ejercitación Evaluación - Solucionario.ipynb")

    with open(student_path, "w", encoding="utf-8") as f:
        json.dump(build_student_notebook(), f, ensure_ascii=False, indent=1)

    with open(sol_path, "w", encoding="utf-8") as f:
        json.dump(build_solucionario_notebook(), f, ensure_ascii=False, indent=1)

    print("Generado:", student_path)
    print("Generado:", sol_path)
