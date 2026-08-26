#!/usr/bin/env python3
"""
generar_evaluacion_atrasada.py — Genera los notebooks de la versión "Atrasada"
(reposición) de Clase 19 - Evaluación Condicionales.

Réplica de la evaluación original para estudiantes que la rinden después de
la fecha regular (evaluación ya publicada en el repo público). Mismo puntaje,
misma dificultad y mismos patrones lógicos que el original — cambia el orden
de las secciones (Programas completos primero, Ítems cortos al final), el
orden de los ítems dentro de cada sección, y el contexto narrativo de cada
uno, para que no sea posible copiar directamente las respuestas.

Salida (en esta misma carpeta):
  Clase 19 - Evaluación Condicionales - Evaluación (Atrasada).ipynb
  Clase 19 - Evaluación Condicionales - Solucionario (Atrasada).ipynb
  Clase 19 - Evaluación Condicionales - Solucionario Estudiantes (Atrasada).ipynb

Uso:
  python generar_evaluacion_atrasada.py
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


# ── Sección 1 (atrasada) — Programas completos (con input()) ─────────────────
# Orden nuevo (derangement del original): Ahorro→Natación, Modo Fiesta→Batería
# PS5, Sala de juego→Fiesta Vendimia, Micro a Talagante→Convención.

EJERCICIOS_1 = [
    dict(
        num=1, titulo="Kilometraje semanal de natación", pts=18,
        narrativa=(
            "El club de natación de la piscina municipal registra cuántos "
            "kilómetros nada cada estudiante en la semana, para reconocer la "
            "constancia de cada nadador. Escribe el programa que, dado el "
            "kilometraje nadado, muestre el nivel correspondiente."
        ),
        debe=[
            "Pedir con `input()` los **kilómetros nadados esta semana** "
            "(**puede tener decimales**)",
            "Clasificar el kilometraje en estos 4 niveles:\n"
            "  - Menos de 5 km → `\"Nivel: Recién empezando.\"`\n"
            "  - Entre 5 y menos de 15 km → `\"Nivel: En camino.\"`\n"
            "  - Entre 15 y menos de 25 km → `\"Nivel: Buen ritmo.\"`\n"
            "  - 25 km o más → `\"Nivel: ¡Semana destacada!\"`",
        ],
        ej1_in="8", ej1_out="Nivel: En camino.",
        ej2_in="27.5", ej2_out="Nivel: ¡Semana destacada!",
        solucion=(
            "km_nadados_semana = float(input(\"Ingresa cuántos kilómetros nadaste esta semana: \"))\n"
            "\n"
            "if km_nadados_semana < 5:\n"
            "    print(\"Nivel: Recién empezando.\")\n"
            "elif km_nadados_semana < 15:\n"
            "    print(\"Nivel: En camino.\")\n"
            "elif km_nadados_semana < 25:\n"
            "    print(\"Nivel: Buen ritmo.\")\n"
            "else:\n"
            "    print(\"Nivel: ¡Semana destacada!\")"
        ),
        criterio=(
            "Que las **4 categorías** quedaran bien delimitadas, sin huecos ni "
            "superposiciones en los límites entre un nivel y el siguiente."
        ),
        rubrica=dict(
            acepta=[
                "Cualquier orden de las comparaciones (de menor a mayor o de mayor a menor) siempre que las 4 franjas queden bien delimitadas.",
                "Usa `<=` en los límites en vez de `<` siempre que sea consistente en las 4 franjas y no deje huecos ni duplique un valor límite en dos categorías a la vez.",
            ],
            parcial=[
                "Deja un pequeño hueco o superposición en un límite exacto (ej. 15.0 justo) que no se prueba en los ejemplos dados, pero rompe la partición para ese valor puntual. Descuenta 1-2 pts si el resto de las 4 franjas está bien.",
            ],
            full=[
                "Confunde el orden de los niveles (los mensajes no corresponden a su franja).",
                "Le faltan niveles (usa solo `if/else` de 2 casos en vez de las 4 franjas pedidas).",
            ],
        ),
    ),
    dict(
        num=2, titulo="Batería del control de PS5", pts=12,
        narrativa=(
            "La app de un control de PlayStation revisa el nivel de batería "
            "antes de cada partida: si queda suficiente carga, activa el "
            "Modo Turbo con vibración avanzada; si no, deja el control en "
            "modo ahorro de energía. Escribe el programa que, dado el "
            "porcentaje de batería, informe en qué modo queda el control."
        ),
        debe=[
            "Pedir con `input()` el **porcentaje de batería del control** "
            "(**un número entero** entre 0 y 100)",
            "Verificar si la batería **alcanza el mínimo** para el Modo Turbo (70)",
            "Mostrar un **mensaje distinto** según corresponda",
        ],
        ej1_in="70", ej1_out="¡Modo Turbo activado! 🎮",
        ej2_in="45", ej2_out="Modo ahorro de energía.",
        solucion=(
            "porcentaje_bateria_control = int(input(\"Ingresa el porcentaje de batería del control (0 a 100): \"))\n"
            "\n"
            "if porcentaje_bateria_control >= 70:\n"
            "    print(\"¡Modo Turbo activado! 🎮\")\n"
            "else:\n"
            "    print(\"Modo ahorro de energía.\")"
        ),
        criterio=(
            "Que el dato pedido con `input()` se leyera como número, que el "
            "umbral (70) quedara incluido como \"alcanza\" (no solo \"supera\"), "
            "y que cada camino mostrara su mensaje correspondiente."
        ),
        rubrica=dict(
            acepta=[
                "Cualquier mensaje del `input()` y cualquier nombre de variable.",
                "Usar `if/else` como en la solución, o un `if` seguido de otro `if` con condición negada — misma partición de casos.",
            ],
            parcial=[
                "Usa `float()` en vez de `int()` para leer la batería: el enunciado pide entero, pero numéricamente 70 sigue siendo 70.0 y no cambia el resultado en la práctica. Descuenta 1 pt por no seguir el tipo de dato pedido.",
            ],
            full=[
                "Usa `>` en vez de `>=` (cambia el resultado justo para batería = 70, el caso límite mostrado en el Ejemplo 1).",
                "No convierte el input a número y compara contra el texto \"70\" tal cual (no ejecuta o el resultado es incorrecto).",
            ],
        ),
    ),
    dict(
        num=3, titulo="Entrada a la Fiesta de la Vendimia", pts=24,
        narrativa=(
            "La boletería de la Fiesta de la Vendimia de Isla de Maipo arma "
            "el acceso según el tipo de entrada. Para la entrada VIP, además "
            "revisa si la persona lleva un acompañante, porque eso cambia el "
            "acceso que recibe. Escribe el programa que, dado el tipo de "
            "entrada y —cuando corresponda— si lleva acompañante, muestre a "
            "qué acceso queda."
        ),
        debe=[
            "Pedir con `input()` el **tipo de entrada** (la persona responde "
            "**exactamente** una de estas palabras: \"general\", "
            "\"preferencial\" o \"vip\")",
            "Si el tipo es **\"vip\"**, pedir además con `input()` si "
            "**lleva acompañante** (responde **exactamente** \"si\" o "
            "\"no\") — esta pregunta no se hace para los otros tipos",
            "Mostrar el mensaje que corresponda a cada uno de estos casos:\n"
            "  - tipo \"general\" → `\"Acceso por la fila general.\"`\n"
            "  - tipo \"preferencial\" → `\"Acceso por la fila preferencial.\"`\n"
            "  - tipo \"vip\" sin acompañante → `\"Acceso VIP directo.\"`\n"
            "  - tipo \"vip\" con acompañante → `\"Acceso VIP directo con acompañante.\"`",
        ],
        ej1_in="vip<br>si", ej1_out="Acceso VIP directo con acompañante.",
        ej2_in="preferencial", ej2_out="Acceso por la fila preferencial.",
        solucion=(
            "tipo_entrada = input(\"Ingresa tu tipo de entrada (general/preferencial/vip): \")\n"
            "\n"
            "if tipo_entrada == \"vip\":\n"
            "    lleva_acompanante = input(\"¿Llevas acompañante? (si/no): \")\n"
            "    if lleva_acompanante == \"si\":\n"
            "        print(\"Acceso VIP directo con acompañante.\")\n"
            "    else:\n"
            "        print(\"Acceso VIP directo.\")\n"
            "elif tipo_entrada == \"preferencial\":\n"
            "    print(\"Acceso por la fila preferencial.\")\n"
            "else:\n"
            "    print(\"Acceso por la fila general.\")"
        ),
        criterio=(
            "Que la pregunta por el acompañante solo se hiciera para el tipo "
            "\"vip\", y que las **cuatro** combinaciones posibles (general, "
            "preferencial, vip sin acompañante, vip con acompañante) "
            "mostraran su mensaje correcto."
        ),
        rubrica=dict(
            acepta=[
                "Usa `if/elif/elif/else` de 3 ramas para general/preferencial/vip anidando la pregunta del acompañante solo dentro de la rama vip (como la solución), o reordena el orden de los tipos (vip/preferencial/general en cualquier orden) siempre que las 4 combinaciones finales queden bien cubiertas.",
            ],
            parcial=[
                "Pregunta por el acompañante siempre (a todos los tipos) pero solo usa la respuesta cuando el tipo es vip — la pregunta de más no cambia el resultado, solo sobra un `input()`. Descuenta 1 pt por no seguir la instrucción \"esta pregunta no se hace para los otros tipos\", aunque el resultado final sea correcto.",
            ],
            full=[
                "No anida la pregunta del acompañante dentro de \"vip\" (muestra \"Acceso VIP directo\" sin revisar si lleva acompañante) — falta una de las 4 combinaciones posibles.",
                "Confunde a qué tipo de entrada corresponde cada mensaje.",
            ],
        ),
    ),
    dict(
        num=4, titulo="Convención de videojuegos y anime", pts=16,
        narrativa=(
            "Para entrar a una convención de videojuegos y anime, el sistema "
            "revisa primero si la persona ya compró su entrada digital; si "
            "no la compró, revisa si el efectivo que lleva alcanza para "
            "pagar la entrada en la puerta. Escribe el programa que, según "
            "esos datos, muestre cómo puede entrar la persona."
        ),
        debe=[
            "Pedir con `input()` si ya tiene **entrada digital comprada** "
            "(la persona responde **exactamente** \"si\" o \"no\")",
            "Si **no** tiene entrada digital, pedir además con `input()` "
            "**cuánto efectivo lleva** (un **número entero**, en pesos)",
            "Verificar primero la entrada digital; solo si no la tiene, "
            "verificar si el efectivo **alcanza** el costo de la entrada en "
            "la puerta (\\$6.000)",
            "Mostrar el mensaje que corresponda a cada uno de estos tres "
            "caminos:\n"
            "  - Tiene entrada digital → `\"Ingresa directo mostrando su entrada digital.\"`\n"
            "  - No tiene entrada Y el efectivo alcanza → `\"Paga la entrada en la puerta.\"`\n"
            "  - No tiene entrada Y el efectivo no alcanza → `\"No le alcanza el efectivo para entrar.\"`",
        ],
        ej1_in="si", ej1_out="Ingresa directo mostrando su entrada digital.",
        ej2_in="no<br>4000", ej2_out="No le alcanza el efectivo para entrar.",
        solucion=(
            "tiene_entrada_digital = input(\"¿Ya tienes tu entrada digital comprada? (si/no): \")\n"
            "\n"
            "if tiene_entrada_digital == \"si\":\n"
            "    print(\"Ingresa directo mostrando su entrada digital.\")\n"
            "else:\n"
            "    efectivo_disponible = int(input(\"Ingresa cuánto efectivo llevas: \"))\n"
            "    if efectivo_disponible >= 6000:\n"
            "        print(\"Paga la entrada en la puerta.\")\n"
            "    else:\n"
            "        print(\"No le alcanza el efectivo para entrar.\")"
        ),
        criterio=(
            "Que se verificara **primero** la entrada digital, que la "
            "pregunta por el efectivo solo apareciera cuando correspondía "
            "(sin entrada), y que los **tres** caminos posibles mostraran "
            "su mensaje exacto."
        ),
        rubrica=dict(
            acepta=[
                "Compara la respuesta con `.lower()` u otra variante que además acepte \"Si\"/\"SI\" — mejora robustez, no se exige pero tampoco se penaliza.",
                "Usa `if/elif/else` al mismo nivel en vez de anidar el segundo `if` dentro del `else` — igual de válido si logra la misma partición de 3 casos.",
            ],
            parcial=[
                "Usa `>` en vez de `>=` para el efectivo (\\$6.000 exactos no alcanzaría) — cambia un caso límite que no aparece en los ejemplos. Si el resto del ejercicio (las 2 ramas de la entrada digital) está bien resuelto, descuenta 1-2 pts, no el ejercicio completo.",
                "Un desliz aislado en el mensaje de una sola rama (ej. cambia \"Paga la entrada en la puerta.\" por una redacción que igual deja claro que sí pagó) — no es el mismo texto pero distingue el caso correctamente.",
            ],
            full=[
                "No hace la verificación anidada del efectivo cuando no hay entrada digital (falta por completo uno de los 3 caminos posibles).",
                "Compara mal la respuesta \"si\"/\"no\" (ej. contra un booleano) y el programa no distingue los casos.",
            ],
        ),
    ),
]


# ── Sección 2 (atrasada) — Ítems cortos (sin input, sin autocheck) ───────────
# Orden nuevo: 2A (swap) + 2B (corrimiento cíclico de 2 sobre el original).

ITEMS_2 = [
    dict(
        id="2A.1", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`and` simple",
        narrativa=(
            "Un sistema de riego automático en una parcela de Isla de Maipo "
            "solo abre la **válvula de riego por goteo** cuando el sensor "
            "detecta que la **tierra está seca** Y además hay **agua "
            "disponible en el canal**."
        ),
        setup="tierra_esta_seca = True\nhay_agua_en_canal = False",
        var="abre_valvula_riego", print_label="¿Abre la válvula de riego?",
        expr="tierra_esta_seca and hay_agua_en_canal",
        expected=False,
        criterio=(
            "Que la condición exigiera **ambas** variables a la vez (no bastaba "
            "con que se cumpliera solo una de las dos)."
        ),
        rubrica=dict(
            acepta=[
                "Orden invertido: `hay_agua_en_canal and tierra_esta_seca` (mismo resultado, `and` es conmutativo).",
                "Comparaciones redundantes que no cambian el resultado, ej. `tierra_esta_seca == True and hay_agua_en_canal == True`.",
            ],
            parcial=[],
            full=[
                "Usa `or` en vez de `and` (basta con que se cumpla una de las dos condiciones, no ambas).",
                "Solo evalúa una de las dos variables, ignorando la otra.",
            ],
        ),
    ),
    dict(
        id="2A.2", bloque="Bloque 2 — Operadores lógicos", tipo="arma", pts=4,
        patron="`var1 and (var2 or var3)`",
        narrativa=(
            "Para desbloquear el **modo cooperativo secreto** de un "
            "videojuego, se necesita tener el **nivel mínimo de cuenta** Y "
            "además (haber **completado el modo historia** O tener un "
            "**código de invitación** de un amigo)."
        ),
        setup=(
            "tiene_nivel_minimo_cuenta = True\n"
            "completo_modo_historia = False\n"
            "tiene_codigo_invitacion = True"
        ),
        var="desbloquea_modo_cooperativo", print_label="¿Desbloquea el modo cooperativo secreto?",
        expr="tiene_nivel_minimo_cuenta and (completo_modo_historia or tiene_codigo_invitacion)",
        expected=True,
        criterio=(
            "Que el nivel mínimo de cuenta fuera **obligatorio** y que, además, "
            "bastara con **una** de las otras dos condiciones (modo historia o "
            "código de invitación) — no las dos juntas."
        ),
        rubrica=dict(
            acepta=[
                "Reescribe con la distribución equivalente: `(tiene_nivel_minimo_cuenta and completo_modo_historia) or (tiene_nivel_minimo_cuenta and tiene_codigo_invitacion)` — matemáticamente igual, aunque menos elegante.",
                "Paréntesis de más que no cambian la precedencia real.",
            ],
            parcial=[
                "Omite los paréntesis (`tiene_nivel_minimo_cuenta and completo_modo_historia or tiene_codigo_invitacion`): por la precedencia real de Python (`and` liga más fuerte que `or`) el resultado da igual en este ejemplo puntual, pero la lógica no generaliza a otros valores — no fue una decisión consciente del estudiante. Descuenta 1 pt.",
            ],
            full=[
                "Exige solo el nivel mínimo de cuenta sin revisar historia/invitación, o exige las tres condiciones juntas con `and`.",
            ],
        ),
    ),
    dict(
        id="2B.1", bloque="Bloque 1 — Booleanos y comparaciones", tipo="bug", pts=4,
        narrativa=(
            "El **casillero inteligente** del gimnasio del liceo solo se "
            "abre cuando el **código ingresado** es exactamente igual al "
            "**código asignado** al estudiante."
        ),
        buggy=(
            "codigo_asignado = 4821\n"
            "codigo_ingresado = 4821\n"
            "\n"
            "if codigo_ingresado = codigo_asignado:\n"
            "    mensaje_casillero = \"Casillero abierto.\"\n"
            "else:\n"
            "    mensaje_casillero = \"Código incorrecto, casillero bloqueado.\"\n"
            "\n"
            "print(mensaje_casillero)"
        ),
        fixed=(
            "codigo_asignado = 4821\n"
            "codigo_ingresado = 4821\n"
            "\n"
            "if codigo_ingresado == codigo_asignado:\n"
            "    mensaje_casillero = \"Casillero abierto.\"\n"
            "else:\n"
            "    mensaje_casillero = \"Código incorrecto, casillero bloqueado.\"\n"
            "\n"
            "print(mensaje_casillero)"
        ),
        expected="Casillero abierto.",
        criterio=(
            "Que la comparación fuera de **igualdad exacta** (no un rango), ya "
            "que el casillero exige el código preciso."
        ),
        rubrica=dict(
            acepta=[
                "Usa `!=` invirtiendo las ramas (`if codigo_ingresado != codigo_asignado:` mensaje de error, `else:` abierto) — misma partición de casos.",
            ],
            parcial=[
                "Usa `>=` en vez de `==`: en el ejemplo dado (4821 == 4821) da el mismo resultado, pero no respeta \"exactamente igual\" del enunciado — un código mayor no debería abrir y con `>=` sí abre. El estudiante sí entendió que había que cambiar el operador de comparación, solo eligió el operador equivocado. Descuenta 2 de 4 pts.",
            ],
            full=[
                "No corrige el `=` (error de sintaxis, el código no ejecuta).",
                "Quita la comparación por completo (siempre abre el casillero, sin condición).",
            ],
        ),
    ),
    dict(
        id="2B.2", bloque="Bloque 3 — Análisis de condiciones (caso límite)", tipo="bug", pts=5,
        narrativa=(
            "En un juego de estrategia online, una alianza declara la "
            "**victoria** en la batalla cuando su cantidad de **tropas** "
            "**alcanza** el mínimo necesario para ganar (no solo cuando lo "
            "supera)."
        ),
        buggy=(
            "tropas_alianza = 500\n"
            "tropas_minimas_victoria = 500\n"
            "\n"
            "if tropas_alianza > tropas_minimas_victoria:\n"
            "    mensaje_batalla = \"La alianza gana la batalla.\"\n"
            "else:\n"
            "    mensaje_batalla = \"La alianza pierde la batalla.\"\n"
            "\n"
            "print(mensaje_batalla)"
        ),
        fixed=(
            "tropas_alianza = 500\n"
            "tropas_minimas_victoria = 500\n"
            "\n"
            "if tropas_alianza >= tropas_minimas_victoria:\n"
            "    mensaje_batalla = \"La alianza gana la batalla.\"\n"
            "else:\n"
            "    mensaje_batalla = \"La alianza pierde la batalla.\"\n"
            "\n"
            "print(mensaje_batalla)"
        ),
        expected="La alianza gana la batalla.",
        criterio=(
            "Que el caso límite (tropas **igual** al mínimo) quedara incluido "
            "en la victoria, no solo las cantidades que lo superan."
        ),
        rubrica=dict(
            acepta=[
                "Reescribe como `not (tropas_alianza < tropas_minimas_victoria)` — equivalente lógico.",
            ],
            parcial=[],
            full=[
                "Deja `>` sin corregir, o cambia a `==` (deja fuera de la victoria a las tropas mayores al mínimo, que también deben ganar) — es exactamente el error de caso límite que este ítem evalúa, no hay término medio.",
            ],
        ),
    ),
    dict(
        id="2B.3", bloque="Bloque 4 — if / else", tipo="bug", pts=4,
        narrativa=(
            "Antes de enviar una tarea en la **plataforma de estudio en "
            "línea**, el sistema revisa si el **archivo fue adjuntado** "
            "correctamente."
        ),
        buggy=(
            "archivo_adjuntado = True\n"
            "\n"
            "if archivo_adjuntado\n"
            "    mensaje_plataforma = \"Tarea enviada con éxito.\"\n"
            "else:\n"
            "    mensaje_plataforma = \"Falta adjuntar el archivo.\"\n"
            "\n"
            "print(mensaje_plataforma)"
        ),
        fixed=(
            "archivo_adjuntado = True\n"
            "\n"
            "if archivo_adjuntado:\n"
            "    mensaje_plataforma = \"Tarea enviada con éxito.\"\n"
            "else:\n"
            "    mensaje_plataforma = \"Falta adjuntar el archivo.\"\n"
            "\n"
            "print(mensaje_plataforma)"
        ),
        expected="Tarea enviada con éxito.",
        criterio=(
            "Que la sintaxis del `if` quedara completa (con `:` al final) y que "
            "el resultado no cambiara respecto al esperado."
        ),
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
        id="2B.4", bloque="Bloque 5 — if anidados", tipo="bug", pts=4,
        narrativa=(
            "Un **dron de reparto** revisa primero si tiene **batería "
            "suficiente** para volar, y solo entonces si **detectó la "
            "dirección de entrega**."
        ),
        buggy=(
            "bateria_suficiente = True\n"
            "detecto_direccion_entrega = False\n"
            "\n"
            "if bateria_suficiente:\n"
            "    if detecto_direccion_entrega:\n"
            "    mensaje_dron = \"El dron entrega el paquete.\"\n"
            "    else:\n"
            "        mensaje_dron = \"El dron no encontró la dirección.\"\n"
            "else:\n"
            "    mensaje_dron = \"El dron no puede despegar por batería baja.\"\n"
            "\n"
            "print(mensaje_dron)"
        ),
        fixed=(
            "bateria_suficiente = True\n"
            "detecto_direccion_entrega = False\n"
            "\n"
            "if bateria_suficiente:\n"
            "    if detecto_direccion_entrega:\n"
            "        mensaje_dron = \"El dron entrega el paquete.\"\n"
            "    else:\n"
            "        mensaje_dron = \"El dron no encontró la dirección.\"\n"
            "else:\n"
            "    mensaje_dron = \"El dron no puede despegar por batería baja.\"\n"
            "\n"
            "print(mensaje_dron)"
        ),
        expected="El dron no encontró la dirección.",
        criterio=(
            "Que se mantuviera la **dependencia** entre las dos condiciones: la "
            "pregunta por la dirección solo se hace si hay batería suficiente."
        ),
        rubrica=dict(
            acepta=[
                "Cualquier indentación consistente que preserve el anidamiento correcto (4 espacios, tabs, etc. — no importa el estilo, solo que sea consistente).",
            ],
            parcial=[],
            full=[
                "No corrige la indentación (`IndentationError`, el código no ejecuta).",
                "Corrige la indentación pero aplana el anidado (`if bateria_suficiente` y `if detecto_direccion_entrega` al mismo nivel, con `elif`), perdiendo la dependencia \"solo revisa la dirección si hay batería\" — cambia el resultado cuando no hay batería.",
            ],
        ),
    ),
    dict(
        id="2B.5", bloque="Bloque 6 — elif", tipo="bug", pts=5,
        narrativa=(
            "Una **tienda de artículos de skate** clasifica el nivel de "
            "**fidelidad** de un cliente según la cantidad de **compras "
            "acumuladas en el año**, de la categoría más exigente a la más "
            "básica."
        ),
        buggy=(
            "compras_acumuladas_anio = 12\n"
            "\n"
            "if compras_acumuladas_anio >= 3:\n"
            "    mensaje_fidelidad = \"Cliente ocasional.\"\n"
            "elif compras_acumuladas_anio >= 7:\n"
            "    mensaje_fidelidad = \"Cliente frecuente.\"\n"
            "elif compras_acumuladas_anio >= 14:\n"
            "    mensaje_fidelidad = \"Cliente VIP.\"\n"
            "else:\n"
            "    mensaje_fidelidad = \"Nuevo cliente.\"\n"
            "\n"
            "print(mensaje_fidelidad)"
        ),
        fixed=(
            "compras_acumuladas_anio = 12\n"
            "\n"
            "if compras_acumuladas_anio >= 14:\n"
            "    mensaje_fidelidad = \"Cliente VIP.\"\n"
            "elif compras_acumuladas_anio >= 7:\n"
            "    mensaje_fidelidad = \"Cliente frecuente.\"\n"
            "elif compras_acumuladas_anio >= 3:\n"
            "    mensaje_fidelidad = \"Cliente ocasional.\"\n"
            "else:\n"
            "    mensaje_fidelidad = \"Nuevo cliente.\"\n"
            "\n"
            "print(mensaje_fidelidad)"
        ),
        expected="Cliente frecuente.",
        criterio=(
            "Que las condiciones quedaran ordenadas de **mayor a menor** "
            "exigencia, para que ningún caso quedara mal clasificado por una "
            "condición más amplia evaluada antes de tiempo."
        ),
        rubrica=dict(
            acepta=[
                "Cualquier orden de `if/elif` siempre que vaya de mayor a menor umbral (>=14, >=7, >=3, else) — lo que importa es el orden de evaluación, no la redacción exacta de los mensajes.",
            ],
            parcial=[
                "Con compras_acumuladas_anio = 12, un orden intermedio (ej. compara primero >=7, luego >=14) también da \"Cliente frecuente\" en este ejemplo puntual, pero no generaliza (para compras=15 fallaría). Descuenta 1-2 pts si el resto de la lógica está bien.",
            ],
            full=[
                "Deja el orden ascendente original (bug sin corregir) — entrega \"Cliente ocasional\" en vez de \"Cliente frecuente\".",
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
    puntaje_rows = [(f"1.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_1]
    puntaje_rows += [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_2]

    cells = [
        md_cell(
            "# 📝 Evaluación Individual — Condicionales (Reposición)\n\n"
            "**Fecha:** jueves 6 de agosto, 2026\n\n"
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
            "---\n\n## 💻 Sección 1 — Programas completos (70 pts)\n\n"
            "Programas completos desde una narrativa. Cada uno pide sus datos "
            "con `input()` — lee bien el tipo de dato que se espera antes de "
            "escribir tu código."
        ),
    ]

    for ej in EJERCICIOS_1:
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
        "---\n\n## 🔥 Sección 2 — Ítems cortos (30 pts)\n\n"
        "Repaso rápido de condicionales, dividido en dos partes."
    ))

    last_tipo = None
    for item in ITEMS_2:
        if item["tipo"] != last_tipo:
            if item["tipo"] == "arma":
                cells.append(md_cell(
                    "### 2A — Arma la condición\n\n"
                    "Las variables ya están definidas. Escribe **solo la "
                    "línea que falta** con la condición pedida."
                ))
            else:
                cells.append(md_cell(
                    "### 2B — Arregla el bug\n\n"
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
        "---\n\n## 🏁 Fin de la evaluación\n\n"
        "Revisa que todas las celdas se ejecuten sin errores antes de "
        "compartir el Colab."
    ))

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Evaluación (Atrasada)")


# ── Solucionario ──────────────────────────────────────────────────────────────

CRITERIOS_CORRECCION_MD = (
    "---\n\n## 🎯 Criterios de corrección — instrucciones para el agente que revisa\n\n"
    "**Si estás revisando esta evaluación (skill `revisar-evaluacion`), lee esto "
    "antes de calificar el primer ítem.** Esta es la **versión de reposición** "
    "de Clase 19 - Evaluación Condicionales: mismos contenidos, mismo puntaje y "
    "misma dificultad que la evaluación original, con otro orden y otros "
    "contextos narrativos — la pauta se corrige exactamente igual.\n\n"
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
    puntaje_rows = [(f"1.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_1]
    puntaje_rows += [(item["id"], item["bloque"], item["pts"]) for item in ITEMS_2]

    cells = [
        md_cell(
            "# ✅ Solucionario (Reposición) — Evaluación Individual Condicionales\n\n"
            "Solo para el profesor. Incluye soluciones y pauta de puntaje. "
            "Versión de reposición: mismo contenido y puntaje que el "
            "Solucionario original, en el orden de esta versión."
        ),
        md_cell(CRITERIOS_CORRECCION_MD),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts, exigencia 50%)\n\n"
            + puntaje_tabla_md(puntaje_rows)
            + "\n\nEscala: 50% de logro = nota 4.0 (nota = 1 + (pct/50)*3 si "
            "pct < 50%; nota = 4 + ((pct-50)/50)*3 si pct >= 50%, con pct "
            "= puntaje obtenido / 100 * 100)."
        ),
        md_cell("---\n\n## 💻 Sección 1 — Programas completos"),
    ]

    for ej in EJERCICIOS_1:
        cells.append(md_cell(
            f"### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)"
        ))
        cells.append(code_cell(ej["solucion"]))
        cells.append(md_cell(rubrica_md(ej["rubrica"], ej["pts"])))

    cells.append(md_cell("---\n\n## 🔥 Sección 2 — Ítems cortos"))

    for item in ITEMS_2:
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

    return notebook(cells, "Clase 19 - Evaluación Condicionales - Solucionario (Atrasada)")


# ── Solucionario para publicar a estudiantes (sin rúbrica de corrección) ──────

def build_solucionario_estudiantes_notebook() -> dict:
    puntaje_rows = [(f"1.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_1]
    puntaje_rows += [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_2]

    cells = [
        md_cell(
            "# ✅ Solucionario (Reposición) — Evaluación Individual Condicionales\n\n"
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
        md_cell("---\n\n## 💻 Sección 1 — Programas completos (70 pts)"),
    ]

    for ej in EJERCICIOS_1:
        cells.append(md_cell(
            f"---\n\n### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + "\n\n"
            + tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        ))
        cells.append(code_cell(ej["solucion"]))
        cells.append(md_cell(f"🔎 **Qué se revisó:** {ej['criterio']}"))

    cells.append(md_cell("---\n\n## 🔥 Sección 2 — Ítems cortos (30 pts)"))

    last_tipo = None
    for item in ITEMS_2:
        if item["tipo"] != last_tipo:
            cells.append(md_cell(
                "### 2A — Arma la condición" if item["tipo"] == "arma"
                else "### 2B — Arregla el bug"
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
        cells.append(md_cell(f"🔎 **Qué se revisó:** {item['criterio']}"))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin del solucionario\n\n"
        "¿Alguna respuesta no te calzó? Pregúntale al profesor antes de la "
        "próxima clase."
    ))

    return notebook(
        cells, "Clase 19 - Evaluación Condicionales - Solucionario Estudiantes (Atrasada)"
    )


if __name__ == "__main__":
    import json
    import os

    base = os.path.dirname(os.path.abspath(__file__))

    student_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Evaluación (Atrasada).ipynb")
    sol_path = os.path.join(base, "Clase 19 - Evaluación Condicionales - Solucionario (Atrasada).ipynb")
    sol_estudiantes_path = os.path.join(
        base, "Clase 19 - Evaluación Condicionales - Solucionario Estudiantes (Atrasada).ipynb"
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
