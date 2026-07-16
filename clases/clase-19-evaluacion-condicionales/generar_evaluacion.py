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
        rubrica=dict(
            acepta=[
                "Orden invertido: `uso_hashtag_oficial and cuenta_publica` (mismo resultado, `and` es conmutativo).",
                "Comparaciones redundantes que no cambian el resultado, ej. `cuenta_publica == True and uso_hashtag_oficial == True`.",
            ],
            parcial=[],
            full=[
                "Usa `or` en vez de `and` (basta con que se cumpla una de las dos condiciones, no ambas).",
                "Solo evalúa una de las dos variables, ignorando la otra.",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Reescribe con la distribución equivalente: `(tiene_pulsera_vip and tiene_acreditacion_prensa) or (tiene_pulsera_vip and tiene_invitacion_staff)` — matemáticamente igual, aunque menos elegante.",
                "Paréntesis de más que no cambian la precedencia real.",
            ],
            parcial=[
                "Omite los paréntesis (`tiene_pulsera_vip and tiene_acreditacion_prensa or tiene_invitacion_staff`): por la precedencia real de Python (`and` liga más fuerte que `or`) el resultado da igual en este ejemplo puntual, pero la lógica no generaliza a otros valores — no fue una decisión consciente del estudiante. Descuenta 1 pt.",
            ],
            full=[
                "Exige solo la pulsera VIP sin revisar prensa/staff, o exige las tres condiciones juntas con `and`.",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Usa `!=` invirtiendo las ramas (`if monto_insertado != precio_bebida:` mensaje de error, `else:` entregada) — misma partición de casos.",
            ],
            parcial=[
                "Usa `>=` en vez de `==`: en el ejemplo dado (900 == 900) da el mismo resultado, pero no respeta \"exactamente igual\" del enunciado — un monto mayor debería fallar y con `>=` no falla. El estudiante sí entendió que había que cambiar el operador de comparación, solo eligió el operador equivocado. Descuenta 2 de 4 pts.",
            ],
            full=[
                "No corrige el `=` (error de sintaxis, el código no ejecuta).",
                "Quita la comparación por completo (siempre entrega la bebida, sin condición).",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Reescribe como `not (puntaje_equipo < puntaje_minimo_clasificacion)` — equivalente lógico.",
            ],
            parcial=[],
            full=[
                "Deja `>` sin corregir, o cambia a `==` (deja fuera del rango a los puntajes mayores al mínimo, que también deben clasificar) — es exactamente el error de caso límite que este ítem evalúa, no hay término medio.",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Cualquier corrección que agregue los dos puntos y mantenga la lógica intacta.",
            ],
            parcial=[],
            full=[
                "No agrega el `:` (el código no ejecuta).",
                "Agrega el `:` pero además invierte la condición o los mensajes sin necesidad, cambiando el resultado.",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Cualquier indentación consistente que preserve el anidamiento correcto (4 espacios, tabs, etc. — no importa el estilo, solo que sea consistente).",
            ],
            parcial=[],
            full=[
                "No corrige la indentación (`IndentationError`, el código no ejecuta).",
                "Corrige la indentación pero aplana el anidado (`if conectado_internet` y `if reconocio_comando` al mismo nivel, con `elif`), perdiendo la dependencia \"solo revisa el comando si hay internet\" — cambia el resultado cuando no hay internet.",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Cualquier orden de `if/elif` siempre que vaya de mayor a menor umbral (>=14, >=7, >=3, else) — lo que importa es el orden de evaluación, no la redacción exacta de los mensajes.",
            ],
            parcial=[
                "Con racha_dias_estudio = 12, un orden intermedio (ej. compara primero >=7, luego >=14) también da \"Buena constancia\" en este ejemplo puntual, pero no generaliza (para racha=15 fallaría). Descuenta 1-2 pts si el resto de la lógica está bien.",
            ],
            full=[
                "Deja el orden ascendente original (bug sin corregir) — entrega \"Racha en marcha\" en vez de \"Buena constancia\".",
            ],
        ),
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
        rubrica=dict(
            acepta=[
                "Cualquier mensaje del `input()` y cualquier nombre de variable.",
                "Usar `if/else` como en la solución, o un `if` seguido de otro `if` con condición negada — misma partición de casos.",
            ],
            parcial=[
                "Usa `float()` en vez de `int()` para leer la energía: el enunciado pide entero, pero numéricamente 70 sigue siendo 70.0 y no cambia el resultado en la práctica. Descuenta 1 pt por no seguir el tipo de dato pedido.",
            ],
            full=[
                "Usa `>` en vez de `>=` (cambia el resultado justo para energía = 70, el caso límite mostrado en el Ejemplo 1).",
                "No convierte el input a número y compara contra el texto \"70\" tal cual (no ejecuta o el resultado es incorrecto).",
            ],
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
        rubrica=dict(
            acepta=[
                "Compara la respuesta con `.lower()` u otra variante que además acepte \"Si\"/\"SI\" — mejora robustez, no se exige pero tampoco se penaliza.",
                "Usa `if/elif/else` al mismo nivel en vez de anidar el segundo `if` dentro del `else` — igual de válido si logra la misma partición de 3 casos.",
            ],
            parcial=[
                "Usa `>` en vez de `>=` para el saldo de la bip (\\$800 exactos no alcanzaría) — cambia un caso límite que no aparece en los ejemplos. Si el resto del ejercicio (las 2 ramas del pase escolar) está bien resuelto, descuenta 1-2 pts, no el ejercicio completo.",
                "Un desliz aislado en el mensaje de una sola rama (ej. cambia \"Paga el pasaje con la tarjeta bip.\" por una redacción que igual deja claro que sí pagó) — no es el mismo texto pero distingue el caso correctamente.",
            ],
            full=[
                "No hace la verificación anidada del saldo cuando no hay pase (falta por completo uno de los 3 caminos posibles).",
                "Compara mal la respuesta \"si\"/\"no\" (ej. contra un booleano) y el programa no distingue los casos.",
            ],
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
        rubrica=dict(
            acepta=[
                "Cualquier orden de las comparaciones (de menor a mayor o de mayor a menor) siempre que las 4 franjas queden bien delimitadas.",
                "Usa `<=` en los límites en vez de `<` siempre que sea consistente en las 4 franjas y no deje huecos ni duplique un valor límite en dos categorías a la vez.",
            ],
            parcial=[
                "Deja un pequeño hueco o superposición en un límite exacto (ej. 30.0 justo) que no se prueba en los ejemplos dados, pero rompe la partición para ese valor puntual. Descuenta 1-2 pts si el resto de las 4 franjas está bien.",
            ],
            full=[
                "Confunde el orden de los niveles (los mensajes no corresponden a su franja).",
                "Le faltan niveles (usa solo `if/else` de 2 casos en vez de las 4 franjas pedidas).",
            ],
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
        rubrica=dict(
            acepta=[
                "Usa `if/elif/elif/else` de 3 ramas para bronce/plata/oro anidando la pregunta de racha solo dentro de la rama oro (como la solución), o reordena el orden de los rangos (oro/plata/bronce en cualquier orden) siempre que las 4 combinaciones finales queden bien cubiertas.",
            ],
            parcial=[
                "Pregunta por la racha de victorias siempre (a todos los rangos) pero solo usa la respuesta cuando el rango es oro — la pregunta de más no cambia el resultado, solo sobra un `input()`. Descuenta 1 pt por no seguir la instrucción \"esta pregunta no se hace para los otros rangos\", aunque el resultado final sea correcto.",
            ],
            full=[
                "No anida la pregunta de racha dentro de \"oro\" (muestra \"Sala de nivel oro\" sin revisar la racha) — falta una de las 4 combinaciones posibles.",
                "Confunde a qué rango corresponde cada mensaje.",
            ],
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
    "---\n\n## 🎯 Criterios de corrección — instrucciones para el agente que revisa\n\n"
    "**Si estás revisando esta evaluación (skill `revisar-evaluacion`), lee esto "
    "antes de calificar el primer ítem.**\n\n"
    "**Enfoque general: se evalúa la lógica de las condiciones y que el programa "
    "funcione, no la forma exacta del código.** Los estudiantes de 4to medio no "
    "van a escribir exactamente lo mismo que la solución de referencia — eso es "
    "normal y no es un error. Cada ítem y ejercicio de abajo trae su propia "
    "sub-sección **🔍 Rúbrica flexible** con 3 niveles de descuento. Aplícalos "
    "así:\n\n"
    "1. **✅ Acepta sin descuento** — variantes que logran lo mismo que la "
    "solución, aunque se vean distintas: nombres de variable, redacción del "
    "`print()`, orden de definición de variables, estructuras equivalentes "
    "(`if/elif/else` en vez de `if` anidados si logran la misma partición de "
    "casos), forma de leer el `input()`, uso de comas vs. f-string, paréntesis "
    "de más que no cambian la precedencia real, etc.\n"
    "2. **⚠️ Descuenta 1-2 pts (detalle menor)** — el estudiante entendió el "
    "problema y su lógica central está bien, pero algo quedó impreciso: no "
    "siguió el tipo de dato exacto pedido, un caso límite no probado en los "
    "ejemplos queda mal cubierto, sobra un `input()` que no se pidió, o un "
    "acierto en el ejemplo dado que no generalizaría a otros valores. **Este es "
    "el nivel por defecto cuando algo no calza exactamente pero la esencia del "
    "programa es correcta — nunca descuentes más de 2 pts por un detalle así, y "
    "ante la duda entre 0 y 1-2, prefiere 0.**\n"
    "3. **❌ Descuenta la mayoría o todo el puntaje del ítem** — reservado para "
    "errores de lógica reales: operador de comparación incorrecto que cambia el "
    "resultado, caso límite mal manejado, rama faltante, tipo de dato mal leído "
    "desde `input()` que rompe el programa, o código que no ejecuta.\n\n"
    "**Regla de oro: si dudas si algo es un error, no lo es.** Solo desciende de "
    "nivel 1 cuando puedas señalar con precisión qué caso de entrada distinto "
    "produciría un resultado equivocado. La forma exacta del código nunca es, "
    "por sí sola, motivo de descuento.\n\n"
    "*Nota: esto es un punto de partida ya calibrado a este solucionario. Al "
    "corregir, sigue afinando con Diego caso a caso si aparece un patrón nuevo "
    "no cubierto aquí — no asumas criterios de evaluaciones anteriores.*"
)


def rubrica_md(rubrica: dict, pts: int) -> str:
    bloques = []
    if rubrica.get("acepta"):
        bloques.append(
            "**✅ Acepta sin descuento:**\n"
            + "\n".join(f"- {x}" for x in rubrica["acepta"])
        )
    if rubrica.get("parcial"):
        bloques.append(
            "**⚠️ Descuenta 1-2 pts (detalle menor):**\n"
            + "\n".join(f"- {x}" for x in rubrica["parcial"])
        )
    if rubrica.get("full"):
        bloques.append(
            f"**❌ Descuenta la mayoría o todo el puntaje ({pts} pts) — error real:**\n"
            + "\n".join(f"- {x}" for x in rubrica["full"])
        )
    return "🔍 **Rúbrica flexible para este ítem:**\n\n" + "\n\n".join(bloques)


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
        cells.append(md_cell(rubrica_md(item["rubrica"], item["pts"])))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos"))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)"
        ))
        cells.append(code_cell(ej["solucion"]))
        cells.append(md_cell(rubrica_md(ej["rubrica"], ej["pts"])))

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Solucionario")


# ── Solucionario para publicar a estudiantes (sin rúbrica de corrección) ──────

def build_solucionario_estudiantes_notebook() -> dict:
    puntaje_rows = [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_1]
    puntaje_rows += [
        (f"2.{ej['num']}", ej["titulo"], ej["pts"])
        for ej in EJERCICIOS_2
    ]

    cells = [
        md_cell(
            "# ✅ Solucionario — Evaluación Individual Condicionales\n\n"
            "Revisa aquí la solución de cada ítem y ejercicio, con el "
            "resultado esperado. Si tu código llegaba a un resultado "
            "distinto por otro camino (otros nombres de variable, otra "
            "forma de escribir la condición), no significa necesariamente "
            "que estuviera mal — conversa cualquier duda puntual con el "
            "profesor."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts, exigencia 50%)\n\n"
            + puntaje_tabla_md(puntaje_rows)
        ),
        md_cell("---\n\n## 🔥 Sección 1 — Ítems cortos (30 pts)"),
    ]

    last_tipo = None
    for item in ITEMS_1:
        if item["tipo"] != last_tipo:
            cells.append(md_cell(
                "### 1A — Arma la condición" if item["tipo"] == "arma"
                else "### 1B — Arregla el bug"
            ))
            last_tipo = item["tipo"]

        cells.append(md_cell(
            f"---\n\n**Ítem {item['id']}** ({item['pts']} pts)\n\n"
            f"{item['narrativa']}"
        ))
        if item["tipo"] == "arma":
            cells.append(code_cell(
                f"{item['setup']}\n\n"
                f"{item['var']} = {item['expr']}\n\n"
                f"print(\"{item['print_label']}\", {item['var']})  "
                f"# Esperado: {item['expected']}"
            ))
        else:
            cells.append(code_cell(item["fixed"] + f"\n# Esperado: {item['expected']}"))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos (70 pts)"))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"---\n\n### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + "\n\n"
            + tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        ))
        cells.append(code_cell(ej["solucion"]))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin del solucionario\n\n"
        "¿Alguna respuesta no te calzó? Pregúntale al profesor antes de la "
        "próxima clase."
    ))

    return notebook(
        cells, "Clase 19 - Evaluación Condicionales - Solucionario Estudiantes"
    )


if __name__ == "__main__":
    import json
    import os

    base = os.path.dirname(os.path.abspath(__file__))

    student_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Evaluación.ipynb")
    sol_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Solucionario.ipynb")
    sol_estudiantes_path = os.path.join(
        base, "Clase 19 - Evaluación Condicionales - Solucionario Estudiantes.ipynb"
    )

    with open(student_path, "w", encoding="utf-8") as f:
        json.dump(build_student_notebook(), f, ensure_ascii=False, indent=1)

    with open(sol_path, "w", encoding="utf-8") as f:
        json.dump(build_solucionario_notebook(), f, ensure_ascii=False, indent=1)

    with open(sol_estudiantes_path, "w", encoding="utf-8") as f:
        json.dump(build_solucionario_estudiantes_notebook(), f, ensure_ascii=False, indent=1)

    print("Generado:", student_path)
    print("Generado:", sol_path)
    print("Generado:", sol_estudiantes_path)
