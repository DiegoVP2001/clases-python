#!/usr/bin/env python3
"""
generar_evaluacion.py — Genera los notebooks de Clase 27 - Evaluación Ciclos.

Salida (en esta misma carpeta):
  Clase 27 - Evaluación Ciclos - Evaluación.ipynb    (estudiantes)

El Solucionario (rúbrica parcelada + criterios de corrección) se agrega en una
iteración posterior, una vez calibrado con Diego — este script hoy solo
construye el notebook de estudiante para preview.

Uso:
  python "generar_evaluacion.py"
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


def salida_fija(texto: str) -> str:
    return f"📤 <em>El programa imprime:</em>\n<pre>{texto}</pre>"


def pistas_md(pistas: list) -> str:
    if not pistas:
        return ""
    bloques = [
        f"<details><summary>💡 Pista {i} — {subtitulo}</summary>\n\n{texto}\n\n</details>"
        for i, (subtitulo, texto) in enumerate(pistas, start=1)
    ]
    return "\n\n".join(bloques)


def rubrica_md(rubrica: dict, pts: int) -> str:
    bloques = []
    if rubrica.get("acepta"):
        bloques.append(
            "**✅ Acepta sin descuento:**\n"
            + "\n".join(f"- {x}" for x in rubrica["acepta"])
        )
    if rubrica.get("parcial"):
        bloques.append(
            "**⚠️ Descuenta 1-3 pts (detalle menor):**\n"
            + "\n".join(f"- {x}" for x in rubrica["parcial"])
        )
    if rubrica.get("full"):
        bloques.append(
            f"**❌ Descuenta la mayoría o todo el puntaje ({pts} pts) — error real:**\n"
            + "\n".join(f"- {x}" for x in rubrica["full"])
        )
    return "🔍 **Rúbrica flexible para este ítem:**\n\n" + "\n\n".join(bloques)


# ── Criterios de corrección — instrucciones para el agente que revisa ────────

CRITERIOS_CORRECCION_MD = (
    "---\n\n## 🎯 Criterios de corrección — instrucciones para el agente que revisa\n\n"
    "**Si estás revisando esta evaluación (skill `revisar-evaluacion`), lee esto "
    "antes de calificar el primer ítem.**\n\n"
    "**Enfoque general: se evalúa la lógica de los ciclos y que el programa "
    "funcione, no la forma exacta del código.** Los estudiantes de 4to medio no "
    "van a escribir exactamente lo mismo que la solución de referencia — eso es "
    "normal y no es un error. Cada ítem y ejercicio de abajo trae su propia "
    "sub-sección **🔍 Rúbrica flexible** con 3 niveles de descuento. Aplícalos "
    "así:\n\n"
    "1. **✅ Acepta sin descuento** — variantes que logran lo mismo que la "
    "solución, aunque se vean distintas: nombres de variable, redacción del "
    "`print()`, orden de definición de variables, usar `for` con `range(N)` sin "
    "nombrar la variable de control cuando no se usa, estructuras equivalentes "
    "(un `while` con la condición reescrita, un `for` en vez de un `while` con "
    "límite conocido de antemano), fórmulas cerradas que reemplazan un "
    "acumulador (ej. suma de Gauss en vez de sumar dentro del ciclo) si llegan "
    "al mismo resultado, etc.\n"
    "2. **⚠️ Descuenta 1-3 pts (detalle menor)** — el estudiante entendió el "
    "problema y su lógica central está bien, pero algo quedó impreciso: un "
    "operador de comparación por uno equivalente que en los casos de prueba "
    "dados da igual pero no generaliza (ej. `!=` en vez de `<`), un caso límite "
    "no probado en los ejemplos que queda mal cubierto, o un acierto que no "
    "generalizaría a otro rango de valores. **Este es el nivel por defecto "
    "cuando algo no calza exactamente pero la esencia del programa es "
    "correcta — nunca descuentes más de 3 pts por un detalle así, y ante la "
    "duda entre 0 y 1-3, prefiere 0.**\n"
    "3. **❌ Descuenta la mayoría o todo el puntaje del ítem** — reservado para "
    "errores de lógica reales: condición de corte incorrecta que cambia cuántas "
    "veces se repite el ciclo, `break`/`continue` mal ubicados que cambian el "
    "resultado, variable acumuladora que no se actualiza, `ZeroDivisionError` u "
    "otro error de ejecución, o código que no ejecuta.\n\n"
    "**Regla de oro: si dudas si algo es un error, no lo es.** Solo desciende de "
    "nivel 1 cuando puedas señalar con precisión qué caso de entrada distinto "
    "produciría un resultado equivocado. La forma exacta del código nunca es, "
    "por sí sola, motivo de descuento.\n\n"
    "**No se evalúa eficiencia ni elegancia del código, solo lo que hace.** "
    "Ciclos con más vueltas de las estrictamente necesarias, condiciones "
    "redundantes, nombres de variable raros o pasos innecesarios NO "
    "descuentan. Solo descuenta lo que produce un resultado equivocado. Antes "
    "de escribir cualquier comentario de descuento, revísalo: si estás "
    "señalando algo que no cambia lo que el programa entrega, sácalo. Por lo "
    "mismo, se califica el COMPORTAMIENTO y no la forma: una estructura "
    "reescrita, aplanada o distinta a la solución de referencia que produce el "
    "resultado correcto en todos los casos vale el puntaje completo.\n\n"
    "**Da crédito parcial por componentes.** No califiques cada ítem como todo "
    "o nada: divídelo en las decisiones independientes que lo componen (leer "
    "el dato y su tipo, la condición de corte del ciclo, la actualización de "
    "la variable de control, la ubicación del `break`/`continue`, los mensajes "
    "por caso) y puntúa cada una por separado. Un estudiante puede fallar una "
    "pieza y conservar el puntaje de las demás. Nunca descuentes el mismo "
    "error en dos componentes. En los ítems de Sección 1 tipo \"arregla el "
    "bug\" aplica la **regla de portazo**: si el estudiante entregó el "
    "fragmento tal como venía, sin tocar el error, el ítem completo es 0 — no "
    "hay crédito parcial por \"intentarlo\" sin cambiar nada. Ver la skill "
    "`revisar-evaluacion` para el método completo.\n\n"
    "**Verifica ejecutando el código, no leyendo el output pegado en la "
    "celda.** Colab no re-ejecuta al editar, así que el resultado visible "
    "puede estar desactualizado. Si el estudiante cambió valores que venían "
    "fijos en el enunciado (ej. `codigo_correcto`, `filas`), repón los "
    "originales y califica la lógica que escribió.\n\n"
    "*Nota: esto es un punto de partida ya calibrado a este solucionario. Al "
    "corregir, sigue afinando con Diego caso a caso si aparece un patrón "
    "nuevo no cubierto aquí — no asumas criterios de evaluaciones "
    "anteriores.*"
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
    return "Arma el código" if item["tipo"] == "arma" else "Arregla el bug"


# ── Sección 1 — Ítems cortos (sin input, sin autocheck) ──────────────────────
# "bloque"/"patron" son metadatos internos para el futuro Solucionario;
# nunca se muestran en el notebook de estudiante.

ITEMS_1 = [
    dict(
        id="1A.1", bloque="range() con 3 argumentos (conteo regresivo)", tipo="arma", pts=4,
        narrativa=(
            "Para la feria científica del liceo, un grupo programó la cuenta "
            "regresiva del lanzamiento de su cohete a escala: debe imprimir "
            "los números del 10 al 1, uno por línea, terminando con "
            "\"¡Despegue!\"."
        ),
        codigo=(
            "for numero in    # completar\n"
            "    print(numero)\n"
            "\n"
            "print(\"¡Despegue!\")"
        ),
        esperado="10\n9\n8\n...\n1\n¡Despegue!",
        solucion=(
            "for numero in range(10, 0, -1):\n"
            "    print(numero)\n"
            "\n"
            "print(\"¡Despegue!\")"
        ),
        criterio="Que el rango contara hacia atrás exactamente del 10 al 1, sin saltarse ningún número.",
        rubrica=dict(
            acepta=[
                "Cualquier forma de `range()` con paso negativo que genere exactamente 10, 9, ..., 1 (ej. escrito con distinto espaciado).",
                "Un enfoque distinto que logre el mismo resultado (ej. recorrer `range(1, 11)` y usar el valor invertido), siempre que el output impreso sea idéntico.",
            ],
            parcial=[],
            full=[
                "El rango no incluye el paso negativo (queda vacío o lanza error), o los límites están mal puestos y falta/sobra un número en la secuencia.",
            ],
        ),
    ),
    dict(
        id="1A.2", bloque="for + range() + condición + contador (sin listas)", tipo="arma", pts=4,
        narrativa=(
            "En el club de atletismo, un corredor entrena dando 10 vueltas a "
            "la pista, numeradas del 1 al 10. Cada vuelta múltiplo de 3, el "
            "entrenador le toma el tiempo con cronómetro. El programa debe "
            "contar cuántas veces le tomó el tiempo en total."
        ),
        codigo=(
            "tomas_de_tiempo = 0\n"
            "\n"
            "for vuelta in range(1, 11):\n"
            "        # completar: sumar 1 a tomas_de_tiempo si la vuelta es múltiplo de 3\n"
            "\n"
            "print(\"Tomas de tiempo:\", tomas_de_tiempo)"
        ),
        esperado="Tomas de tiempo: 3",
        solucion=(
            "tomas_de_tiempo = 0\n"
            "\n"
            "for vuelta in range(1, 11):\n"
            "    if vuelta % 3 == 0:\n"
            "        tomas_de_tiempo = tomas_de_tiempo + 1\n"
            "\n"
            "print(\"Tomas de tiempo:\", tomas_de_tiempo)"
        ),
        criterio="Que la condición usara el resto de la división (múltiplos de 3) y que el contador se actualizara solo cuando correspondía.",
        rubrica=dict(
            acepta=[
                "Usa `vuelta % 3 == 0` o una expresión equivalente como `not vuelta % 3` (misma partición de casos).",
            ],
            parcial=[
                "Cuenta comparando contra valores fijos hardcodeados (ej. `vuelta == 3 or vuelta == 6 or vuelta == 9`) sin usar el módulo — llega al resultado correcto en este ejemplo puntual, pero no generaliza a otro rango. Descuenta 1-2 pts.",
            ],
            full=[
                "El contador no se actualiza dentro del `if`, o la condición no tiene relación con ser múltiplo de 3 (ej. cuenta vueltas pares).",
            ],
        ),
    ),
    dict(
        id="1A.3", bloque="for anidado — completar el rango interno (sin listas)", tipo="arma", pts=4,
        narrativa=(
            "En el taller de robótica se arma una cuadrícula de prueba de "
            "sensores de 3 filas por 3 columnas: el sistema debe imprimir en "
            "qué fila y columna está cada sensor."
        ),
        codigo=(
            "for fila in range(3):\n"
            "    for columna in    # completar\n"
            "        print(\"Sensor en fila\", fila, \"columna\", columna)"
        ),
        esperado=(
            "Sensor en fila 0 columna 0\nSensor en fila 0 columna 1\n"
            "Sensor en fila 0 columna 2\nSensor en fila 1 columna 0\n"
            "Sensor en fila 1 columna 1\nSensor en fila 1 columna 2\n"
            "Sensor en fila 2 columna 0\nSensor en fila 2 columna 1\n"
            "Sensor en fila 2 columna 2"
        ),
        solucion=(
            "for fila in range(3):\n"
            "    for columna in range(3):\n"
            "        print(\"Sensor en fila\", fila, \"columna\", columna)"
        ),
        criterio="Que el ciclo interno recorriera las 3 columnas completas, no solo 2.",
        rubrica=dict(
            acepta=[
                "Usa `range(3)` o cualquier forma equivalente que recorra exactamente 3 columnas (ej. `range(0, 3)`).",
            ],
            parcial=[],
            full=[
                "El rango interno no cubre las 3 columnas (deja `range(2)` u otro número distinto de 3).",
            ],
        ),
    ),
    dict(
        id="1A.4", bloque="while — completar la condición de corte", tipo="arma", pts=4,
        narrativa=(
            "El estacionamiento del liceo tiene 5 cupos, numerados del 1 al "
            "5. El sistema debe registrar la entrada de vehículos "
            "exactamente hasta llenar el estacionamiento, sin registrar "
            "ninguno de más."
        ),
        codigo=(
            "cupos_ocupados = 0\n"
            "cupos_totales = 5\n"
            "\n"
            "while    # completar\n"
            "    cupos_ocupados = cupos_ocupados + 1\n"
            "    print(\"Vehículo N°\", cupos_ocupados, \"estacionado.\")"
        ),
        esperado=(
            "Vehículo N° 1 estacionado.\nVehículo N° 2 estacionado.\n"
            "Vehículo N° 3 estacionado.\nVehículo N° 4 estacionado.\n"
            "Vehículo N° 5 estacionado."
        ),
        solucion=(
            "cupos_ocupados = 0\n"
            "cupos_totales = 5\n"
            "\n"
            "while cupos_ocupados < cupos_totales:\n"
            "    cupos_ocupados = cupos_ocupados + 1\n"
            "    print(\"Vehículo N°\", cupos_ocupados, \"estacionado.\")"
        ),
        criterio="Que la condición del `while` cortara exactamente al llenar los 5 cupos, sin registrar uno de más.",
        rubrica=dict(
            acepta=[
                "Usa `cupos_ocupados < cupos_totales` o una forma equivalente (ej. `cupos_totales > cupos_ocupados`).",
            ],
            parcial=[
                "Usa `cupos_ocupados != cupos_totales` — funciona porque parte en 0 y sube de a uno, pero no es robusto ante otros valores iniciales. Descuenta 1 pt.",
            ],
            full=[
                "Usa `<=` (permite un vehículo de más) o cualquier condición que no corte exactamente en 5.",
            ],
        ),
    ),
    dict(
        id="1B.1", bloque="range() — límite incorrecto (off-by-one)", tipo="bug", pts=4,
        narrativa=(
            "El encargado de turnos de la feria de emprendimiento del liceo "
            "necesita atender exactamente a los primeros **5** puestos "
            "inscritos, numerados del 1 al 5."
        ),
        codigo=(
            "for puesto in range(1, 5):\n"
            "    print(\"Atendiendo puesto N°\", puesto)"
        ),
        esperado="Atendiendo puesto N° 1\nAtendiendo puesto N° 2\nAtendiendo puesto N° 3\nAtendiendo puesto N° 4\nAtendiendo puesto N° 5",
        solucion=(
            "for puesto in range(1, 6):\n"
            "    print(\"Atendiendo puesto N°\", puesto)"
        ),
        criterio="Que el rango incluyera el puesto N°5, el último de los cinco.",
        rubrica=dict(
            acepta=[
                "Cambia a `range(1, 6)` o reescribe como `range(1, 5 + 1)`, mismo resultado.",
            ],
            parcial=[],
            full=[
                "No corrige el límite (deja `range(1, 5)`), o lo cambia a un número que no cubre los 5 puestos.",
                "No tocó la línea con el error (portazo: 0 pts).",
            ],
        ),
    ),
    dict(
        id="1B.2", bloque="while — falta actualizar la variable de corte", tipo="bug", pts=4,
        narrativa=(
            "Un dron de fotografía aérea debe avisar cada vez que su "
            "batería baja un 10%, partiendo de 100%, hasta llegar a 0%."
        ),
        codigo=(
            "bateria = 100\n"
            "\n"
            "while bateria > 0:\n"
            "    print(\"Batería:\", bateria, \"%\")\n"
            "    bateria - 10"
        ),
        esperado="Batería: 100 %\nBatería: 90 %\n...\nBatería: 10 %",
        solucion=(
            "bateria = 100\n"
            "\n"
            "while bateria > 0:\n"
            "    print(\"Batería:\", bateria, \"%\")\n"
            "    bateria = bateria - 10"
        ),
        criterio="Que la variable de la batería se actualizara dentro del ciclo, para que el `while` terminara.",
        rubrica=dict(
            acepta=[
                "Agrega `bateria = bateria - 10` o `bateria -= 10` dentro del `while`, en cualquier posición que logre el mismo resultado.",
            ],
            parcial=[],
            full=[
                "No agrega ninguna actualización de `bateria` (el ciclo queda infinito), o la actualización queda fuera del `while`.",
                "No tocó la línea con el error (portazo: 0 pts).",
            ],
        ),
    ),
    dict(
        id="1B.3", bloque="break fuera del if (búsqueda con range, sin listas)", tipo="bug", pts=4,
        narrativa=(
            "El sistema del karaoke escolar recorre la cola de canciones "
            "numeradas del 1 al 6, buscando la canción número 4 (la primera "
            "disponible), y debe detenerse apenas la encuentra."
        ),
        codigo=(
            "for numero_cancion in range(1, 7):\n"
            "    if numero_cancion == 4:\n"
            "        print(\"Canción encontrada: N°\", numero_cancion)\n"
            "    break"
        ),
        esperado="Canción encontrada: N° 4",
        solucion=(
            "for numero_cancion in range(1, 7):\n"
            "    if numero_cancion == 4:\n"
            "        print(\"Canción encontrada: N°\", numero_cancion)\n"
            "        break"
        ),
        criterio="Que el `break` estuviera dentro del `if`, cortando solo al encontrar la canción correcta.",
        rubrica=dict(
            acepta=[
                "Indenta el `break` dentro del `if`, o logra el mismo efecto con una condición equivalente que solo corte al llegar a la canción N°4.",
            ],
            parcial=[],
            full=[
                "Deja el `break` fuera del `if` (corta en la primera vuelta sin buscar), o lo elimina por completo.",
                "No tocó la línea con el error (portazo: 0 pts).",
            ],
        ),
    ),
    dict(
        id="1B.4", bloque="continue con condición invertida (range + módulo, sin listas)", tipo="bug", pts=4,
        narrativa=(
            "En el campeonato de ajedrez cronometrado, los jugadores llegan "
            "numerados del 1 al 6 a la mesa de resultados. Los jugadores con "
            "número **par** fueron descalificados por tiempo y no deben "
            "mostrarse; el sistema debe imprimir solo a los jugadores con "
            "número **impar**, que siguen en competencia."
        ),
        codigo=(
            "for numero_jugador in range(1, 7):\n"
            "    if numero_jugador % 2 != 0:\n"
            "        continue\n"
            "    print(\"Jugador N°\", numero_jugador, \"sigue en competencia.\")"
        ),
        esperado="Jugador N° 1 sigue en competencia.\nJugador N° 3 sigue en competencia.\nJugador N° 5 sigue en competencia.",
        solucion=(
            "for numero_jugador in range(1, 7):\n"
            "    if numero_jugador % 2 == 0:\n"
            "        continue\n"
            "    print(\"Jugador N°\", numero_jugador, \"sigue en competencia.\")"
        ),
        criterio="Que el `continue` saltara a los jugadores descalificados (pares), no a los que siguen en competencia.",
        rubrica=dict(
            acepta=[
                "Cambia la condición a `numero_jugador % 2 == 0`, o reescribe la lógica sin `continue` (ej. un `if numero_jugador % 2 != 0: print(...)`) logrando el mismo resultado.",
            ],
            parcial=[],
            full=[
                "Deja la condición igual (`!= 0`), o la invierte de forma incorrecta (ej. `numero_jugador == 2`).",
                "No tocó la línea con el error (portazo: 0 pts).",
            ],
        ),
    ),
]


# ── Sección 2 — Programas completos ──────────────────────────────────────────

EJERCICIOS_2 = [
    dict(
        num=1, titulo="Ventas del almacén", pts=15, usa_input=True,
        narrativa=(
            "El almacén de barrio de Isla de Maipo va a registrar las ventas "
            "de sus primeras 5 transacciones del día. El programa debe pedir "
            "cada venta y, al terminar, informar el total vendido y cuántas "
            "ventas individuales superaron los \\$5.000."
        ),
        debe=[
            "Usar un `for` con `range(5)` para repetir exactamente 5 veces.",
            "Por cada vuelta del `for`, pedir la venta correspondiente con "
            "`input()` (número entero).",
            "Acumular el **total vendido** en el día.",
            "Contar cuántas ventas fueron **superiores a \\$5.000**.",
            "Imprimir ambos resultados con etiqueta al terminar.",
        ],
        pistas=[
            (
                "Reutiliza la variable",
                "No necesitas crear una variable distinta para cada venta "
                "que pides — puedes usar el mismo nombre de variable en cada "
                "vuelta del ciclo, porque solo te interesa el valor que "
                "acabas de ingresar para sumarlo y compararlo, no guardarlos "
                "todos por separado.",
            ),
        ],
        ej1_in="3000<br>5500<br>12000<br>4200<br>8000",
        ej1_out="Total vendido: 32700\nVentas sobre $5.000: 3",
        ej2_in="1000<br>2000<br>3000<br>1500<br>900",
        ej2_out="Total vendido: 8400\nVentas sobre $5.000: 0",
        solucion=(
            "total_vendido = 0\n"
            "ventas_sobre_umbral = 0\n"
            "\n"
            "for numero_venta in range(5):\n"
            "    venta = int(input(\"Ingresa el monto de la venta: \"))\n"
            "    total_vendido = total_vendido + venta\n"
            "    if venta > 5000:\n"
            "        ventas_sobre_umbral = ventas_sobre_umbral + 1\n"
            "\n"
            "print(\"Total vendido:\", total_vendido)\n"
            "print(\"Ventas sobre $5.000:\", ventas_sobre_umbral)"
        ),
        criterio="Que se pidiera exactamente 5 ventas con `input()`, y que el total y el conteo sobre el umbral se acumularan correctamente vuelta a vuelta.",
        rubrica=dict(
            acepta=[
                "Cualquier forma de leer el `input()` y convertirlo (ej. `int(input(...))` en una línea o en dos), variantes de nombre de variable, orden distinto entre acumular el total y verificar el umbral.",
                "Usa `for _ in range(5)` en vez de nombrar la variable de control — es válido, no se usa dentro del ciclo.",
            ],
            parcial=[
                "Compara con `>=` en vez de `>` contra los \\$5.000 — cambia el resultado solo si algún caso está exactamente en el umbral. Descuenta 2-3 pts si afecta el resultado en los casos de prueba.",
            ],
            full=[
                "No repite exactamente 5 veces (usa otro número o un `while` sin límite claro).",
                "No acumula el total, o no cuenta las ventas sobre el umbral.",
                "Lee el dato fuera del ciclo (pide un solo input y lo reutiliza), sin pedir las 5 ventas reales.",
            ],
        ),
    ),
    dict(
        num=2, titulo="Formación del baile de Aniversario", pts=17, usa_input=False,
        narrativa=(
            "Para el número de baile del Aniversario, cada integrante de una "
            "fila debe gritar el número de su fila: la fila 1 tiene 1 "
            "integrante, la fila 2 tiene 2, y así sucesivamente hasta la "
            "fila indicada. Además, la profesora a cargo quiere saber "
            "cuántos integrantes participan en total en el número completo."
        ),
        debe=[
            "Usar `filas = 4`.",
            "Para cada fila (empezando en 1), imprimir el número de esa "
            "fila una vez por cada integrante que le corresponde (una "
            "impresión por línea).",
            "Contar el **total de integrantes** que participan en el "
            "número completo (la suma de todas las filas) e imprimirlo al "
            "final, con etiqueta.",
        ],
        esperado="1\n2\n2\n3\n3\n3\n4\n4\n4\n4\nTotal de integrantes: 10",
        datos="filas = 4",
        solucion=(
            "filas = 4\n"
            "total_integrantes = 0\n"
            "\n"
            "for fila in range(1, filas + 1):\n"
            "    for integrante in range(fila):\n"
            "        print(fila)\n"
            "        total_integrantes = total_integrantes + 1\n"
            "\n"
            "print(\"Total de integrantes:\", total_integrantes)"
        ),
        criterio="Que el ciclo anidado repitiera cada fila la cantidad correcta de veces, y que el acumulador de integrantes sumara en cada impresión, no solo al final.",
        rubrica=dict(
            acepta=[
                "Cualquier forma de recorrer las filas y repeticiones (ej. `range(1, filas+1)` con distinto nombre de variable), siempre que el patrón impreso sea idéntico.",
                "Calcula `total_integrantes` con la fórmula de suma de Gauss (`filas * (filas + 1) // 2`) en vez de acumularlo dentro del ciclo — llega al mismo resultado.",
            ],
            parcial=[],
            full=[
                "El ciclo interno no repite exactamente `fila` veces (ej. usa un número fijo).",
                "El acumulador de integrantes no se actualiza, se actualiza fuera del ciclo interno, o no se imprime al final.",
            ],
        ),
    ),
    dict(
        num=3, titulo="Estación meteorológica", pts=18, usa_input=True,
        narrativa=(
            "Una estación meteorológica escolar recibe temperaturas "
            "ingresadas manualmente durante el día. El programa debe "
            "seguir pidiendo temperaturas (números que pueden tener "
            "decimales) hasta que se ingrese **-999**, que marca el fin "
            "del registro, y luego mostrar el promedio del día."
        ),
        debe=[
            "Pedir temperaturas repetidamente con `while`, hasta recibir `-999`.",
            "Acumular la suma y contar cuántas temperaturas válidas se "
            "ingresaron (sin contar el -999).",
            "Imprimir el **promedio** al terminar.",
            "Si no se ingresó ninguna temperatura válida antes del -999, "
            "imprimir un mensaje indicando que no hay datos, sin calcular "
            "el promedio.",
        ],
        pistas=[
            (
                "Cómo se calcula un promedio",
                "El promedio de un conjunto de datos es la suma de todos "
                "los valores dividida por la cantidad de valores que "
                "sumaste — asegúrate de tener ambos datos disponibles al "
                "momento de calcularlo.",
            ),
            (
                "No olvides contar cuántas veces registraste",
                "Además de ir sumando las temperaturas, necesitas otra "
                "variable que vaya guardando cuántas temperaturas válidas "
                "se han ingresado hasta el momento — ese conteo es "
                "justamente lo que necesitas para calcular el promedio y "
                "para saber si hubo o no datos.",
            ),
        ],
        ej1_in="18.5<br>20.0<br>19.2<br>-999",
        ej1_out="Promedio del día: 19.23",
        ej2_in="-999",
        ej2_out="No se registraron temperaturas.",
        solucion=(
            "suma_temperaturas = 0\n"
            "cantidad_temperaturas = 0\n"
            "\n"
            "temperatura = float(input(\"Ingresa una temperatura (o -999 para terminar): \"))\n"
            "\n"
            "while temperatura != -999:\n"
            "    suma_temperaturas = suma_temperaturas + temperatura\n"
            "    cantidad_temperaturas = cantidad_temperaturas + 1\n"
            "    temperatura = float(input(\"Ingresa una temperatura (o -999 para terminar): \"))\n"
            "\n"
            "if cantidad_temperaturas > 0:\n"
            "    promedio = suma_temperaturas / cantidad_temperaturas\n"
            "    print(\"Promedio del día:\", promedio)\n"
            "else:\n"
            "    print(\"No se registraron temperaturas.\")"
        ),
        criterio="Que el promedio se calculara con la suma y el conteo correctos, y que el caso sin ninguna temperatura ingresada no intentara dividir por cero.",
        rubrica=dict(
            acepta=[
                "Cualquier estructura de `while` que lea el primer dato antes del ciclo y vuelva a leer al final de cada vuelta (patrón \"leer antes, leer al final\"), con nombres de variable distintos.",
                "Imprime el promedio con más o menos decimales que el ejemplo (no se exige redondeo específico salvo que el enunciado lo pida).",
            ],
            parcial=[
                "Calcula el promedio pero cuenta el `-999` como un dato más (divide por uno de más) — descuenta 2-3 pts si afecta el resultado.",
            ],
            full=[
                "No maneja el caso de cero temperaturas (el programa falla con `ZeroDivisionError` o imprime un promedio incorrecto como 0).",
                "No usa una variable contadora separada de la suma, o el promedio no se calcula como suma/cantidad.",
            ],
        ),
    ),
    dict(
        num=4, titulo="Caja fuerte del escape room", pts=18, usa_input=True,
        narrativa=(
            "En el escape room del liceo, una caja fuerte tiene un código "
            "de 4 dígitos. Cada equipo dispone de **como máximo 5 "
            "intentos**; el programa debe cortar apenas alguien acierte el "
            "código, o informar que se acabaron los intentos si nadie lo "
            "logra."
        ),
        debe=[
            "Usar `codigo_correcto = 4271` y `intentos_maximos = 5`.",
            "Pedir un intento (número entero) repetidamente, contando "
            "cuántos van.",
            "Si el intento es correcto, felicitar y **cortar el ciclo** de "
            "inmediato (sin seguir pidiendo intentos).",
            "Si se agotan los 5 intentos sin acertar, informar que la caja "
            "quedó bloqueada.",
        ],
        pistas=[
            (
                "Qué es un contador",
                "Un contador es una variable que va sumando de a uno cada "
                "vez que ocurre algo (por ejemplo, cada intento que se "
                "realiza), para saber cuántas veces ha pasado ese algo.",
            ),
            (
                "Qué es un flag (bandera)",
                "Un flag o bandera es una variable que solo guarda "
                "Verdadero o Falso, y sirve para recordar si algo ya "
                "ocurrió (por ejemplo, si ya se acertó el código) para "
                "poder usar esa información más adelante en el programa, "
                "incluso fuera del ciclo.",
            ),
        ],
        ej1_in="1234<br>4321<br>4271",
        ej1_out="¡Código correcto! Caja abierta en el intento 3",
        ej2_in="1111<br>2222<br>3333<br>4444<br>5555",
        ej2_out="Caja bloqueada: se agotaron los 5 intentos.",
        solucion=(
            "codigo_correcto = 4271\n"
            "intentos_maximos = 5\n"
            "intento_actual = 0\n"
            "acerto = False\n"
            "\n"
            "while intento_actual < intentos_maximos:\n"
            "    intento_actual = intento_actual + 1\n"
            "    intento = int(input(\"Ingresa el código: \"))\n"
            "    if intento == codigo_correcto:\n"
            "        acerto = True\n"
            "        break\n"
            "\n"
            "if acerto:\n"
            "    print(\"¡Código correcto! Caja abierta en el intento\", intento_actual)\n"
            "else:\n"
            "    print(\"Caja bloqueada: se agotaron los 5 intentos.\")"
        ),
        criterio="Que el ciclo cortara apenas se acertara el código, y que el mensaje final distinguiera correctamente entre acierto y agotamiento de intentos.",
        rubrica=dict(
            acepta=[
                "Cualquier forma de contar los intentos (ej. `for` con `range(intentos_maximos)` en vez de `while`, siempre que corte igual con `break` al acertar).",
                "Usa un `return`/estructura distinta para salir del ciclo si el resultado final es idéntico.",
            ],
            parcial=[
                "El mensaje final no incluye el número de intento en el que acertó, pero sí distingue correctamente acierto de agotamiento — descuenta 1-2 pts.",
            ],
            full=[
                "No corta con `break` al acertar (sigue pidiendo intentos de más).",
                "No usa una variable tipo flag para recordar el acierto y termina imprimiendo el mensaje equivocado (ej. dice \"bloqueada\" habiendo acertado).",
                "Permite más de 5 intentos, o corta antes de los 5 sin haber acertado.",
            ],
        ),
    ),
]


# ── Notebook de estudiante ────────────────────────────────────────────────────

def build_student_notebook() -> dict:
    puntaje_rows = [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_1]
    puntaje_rows += [(f"2.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_2]

    cells = [
        md_cell(
            "# 📝 Evaluación Individual — Ciclos\n\n"
            "**Fecha:** jueves 27 de agosto, 2026\n\n"
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
            "ítem, deja lo que alcanzaste.\n"
            "- Usa nombres de variables en **snake_case en español**.\n"
            "- Cuando un ítem pida un dato con `input()`, el enunciado "
            "siempre aclara si es un **número entero**, un **número con "
            "decimales**, o una **palabra exacta**.\n"
            "- **Prohibido** copiar código de compañeros."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts)\n\n"
            + puntaje_tabla_md(puntaje_rows)
        ),
        md_cell(
            "---\n\n## 🔥 Sección 1 — Ítems cortos (32 pts)\n\n"
            "Repaso rápido de ciclos, dividido en dos partes."
        ),
    ]

    last_tipo = None
    for item in ITEMS_1:
        if item["tipo"] != last_tipo:
            if item["tipo"] == "arma":
                cells.append(md_cell(
                    "### 1A — Arma el código\n\n"
                    "Completa la línea marcada para que el programa haga lo "
                    "que pide la narrativa."
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
        cells.append(code_cell(item["codigo"]))

    cells.append(md_cell(
        "---\n\n## 💻 Sección 2 — Programas completos (68 pts)\n\n"
        "Programas completos desde una narrativa. Los ejercicios 1, 3 y 4 "
        "piden sus datos con `input()` — lee bien el tipo de dato que se "
        "espera antes de escribir tu código."
    ))

    for ej in EJERCICIOS_2:
        if ej["usa_input"]:
            resultado_md = tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        else:
            resultado_md = salida_fija(ej["esperado"])

        pistas_bloque = pistas_md(ej.get("pistas", []))

        cells.append(md_cell(
            f"---\n\n## 🎯 Ejercicio {ej['num']} — {ej['titulo']} "
            f"({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + ("\n\n" + pistas_bloque if pistas_bloque else "")
            + "\n\n"
            + resultado_md
        ))
        starter = f"# Ejercicio {ej['num']}\n{ej['datos']}\n\n" if not ej["usa_input"] else f"# Ejercicio {ej['num']}\n"
        cells.append(code_cell(starter))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin de la evaluación\n\n"
        "Revisa que todas las celdas se ejecuten sin errores antes de "
        "compartir el Colab."
    ))

    cells.append(md_cell(
        "---\n\n## 💪 Antes de cerrar\n\n"
        "Cuenta un momento en que aplicaste **rigurosidad** durante la "
        "evaluación. ¿Qué habría pasado con tu resultado si no lo hacías "
        "justo ahí?\n\n"
        "*(Esta pregunta no lleva nota — respóndela con confianza.)*"
    ))
    cells.append(md_cell("**Mi respuesta:**\n\n_______________________________________________"))

    return notebook(cells, "Clase 27 - Evaluación Ciclos - Evaluación")


# ── Preview con respuestas (uso interno, no es el Solucionario formal) ───────
# Mismo notebook de estudiante, pero con la respuesta esperada agregada justo
# debajo de cada celda de código. No tiene rúbrica ni criterios de corrección
# — eso llega con el Solucionario Docente/Estudiantes cuando se calibre.

def build_preview_notebook() -> dict:
    puntaje_rows = [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_1]
    puntaje_rows += [(f"2.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_2]

    cells = [
        md_cell(
            "# 📝 Evaluación Individual — Ciclos — 🔎 Preview con respuestas\n\n"
            "**Fecha:** jueves 27 de agosto, 2026\n\n"
            "*(Este cuaderno es solo para revisión interna de Diego — no se "
            "sube a Classroom ni a GitHub. La respuesta esperada aparece en "
            "una celda de código justo debajo de cada ítem, marcada con "
            "`# ✅ Respuesta esperada`.)*"
        ),
        md_cell(
            "---\n\n"
            "## 📋 Instrucciones generales\n\n"
            "- Esta evaluación tiene **2 secciones** y dura **75 minutos**.\n"
            "- Trabaja en orden y administra tu tiempo.\n"
            "- Entrega este notebook a través de **Google Classroom** antes "
            "de que termine la clase.\n"
            "- El código debe ejecutarse sin errores. Si no terminas un "
            "ítem, deja lo que alcanzaste.\n"
            "- Usa nombres de variables en **snake_case en español**.\n"
            "- Cuando un ítem pida un dato con `input()`, el enunciado "
            "siempre aclara si es un **número entero**, un **número con "
            "decimales**, o una **palabra exacta**.\n"
            "- **Prohibido** copiar código de compañeros."
        ),
        md_cell(
            "---\n\n## 📊 Distribución de puntaje (total 100 pts)\n\n"
            + puntaje_tabla_md(puntaje_rows)
        ),
        md_cell(
            "---\n\n## 🔥 Sección 1 — Ítems cortos (32 pts)\n\n"
            "Repaso rápido de ciclos, dividido en dos partes."
        ),
    ]

    last_tipo = None
    for item in ITEMS_1:
        if item["tipo"] != last_tipo:
            if item["tipo"] == "arma":
                cells.append(md_cell(
                    "### 1A — Arma el código\n\n"
                    "Completa la línea marcada para que el programa haga lo "
                    "que pide la narrativa."
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
        cells.append(code_cell(item["codigo"]))
        cells.append(code_cell(
            "# ✅ Respuesta esperada\n" + item["solucion"]
            + f"\n\n# Salida esperada:\n# {item['esperado'].replace(chr(10), chr(10) + '# ')}"
        ))

    cells.append(md_cell(
        "---\n\n## 💻 Sección 2 — Programas completos (68 pts)\n\n"
        "Programas completos desde una narrativa. Los ejercicios 1, 3 y 4 "
        "piden sus datos con `input()` — lee bien el tipo de dato que se "
        "espera antes de escribir tu código."
    ))

    for ej in EJERCICIOS_2:
        if ej["usa_input"]:
            resultado_md = tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        else:
            resultado_md = salida_fija(ej["esperado"])

        pistas_bloque = pistas_md(ej.get("pistas", []))

        cells.append(md_cell(
            f"---\n\n## 🎯 Ejercicio {ej['num']} — {ej['titulo']} "
            f"({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + ("\n\n" + pistas_bloque if pistas_bloque else "")
            + "\n\n"
            + resultado_md
        ))
        starter = f"# Ejercicio {ej['num']}\n{ej['datos']}\n\n" if not ej["usa_input"] else f"# Ejercicio {ej['num']}\n"
        cells.append(code_cell(starter))
        cells.append(code_cell(f"# ✅ Respuesta esperada — Ejercicio {ej['num']}\n" + ej["solucion"]))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin de la evaluación\n\n"
        "Revisa que todas las celdas se ejecuten sin errores antes de "
        "compartir el Colab."
    ))

    cells.append(md_cell(
        "---\n\n## 💪 Antes de cerrar\n\n"
        "Cuenta un momento en que aplicaste **rigurosidad** durante la "
        "evaluación. ¿Qué habría pasado con tu resultado si no lo hacías "
        "justo ahí?\n\n"
        "*(Esta pregunta no lleva nota — respóndela con confianza. Sin "
        "respuesta correcta que registrar aquí.)*"
    ))

    return notebook(cells, "Clase 27 - Evaluación Ciclos - Preview con Respuestas")


# ── Solucionario Docente (rúbrica parcelada + criterios de corrección) ───────

def build_solucionario_notebook() -> dict:
    puntaje_rows = [(item["id"], item["bloque"], item["pts"]) for item in ITEMS_1]
    puntaje_rows += [(f"2.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_2]

    cells = [
        md_cell(
            "# ✅ Solucionario — Evaluación Individual Ciclos\n\n"
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
        md_cell("---\n\n## 🔥 Sección 1 — Ítems cortos (32 pts)"),
    ]

    for item in ITEMS_1:
        cells.append(md_cell(
            f"**Ítem {item['id']}** — {item['bloque']} — {tipo_label(item)} "
            f"({item['pts']} pts) — solución esperada:"
        ))
        cells.append(code_cell(item["solucion"] + f"\n\n# Esperado:\n# {item['esperado'].replace(chr(10), chr(10) + '# ')}"))
        cells.append(md_cell(rubrica_md(item["rubrica"], item["pts"])))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos (68 pts)"))

    for ej in EJERCICIOS_2:
        cells.append(md_cell(
            f"### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)"
        ))
        cells.append(code_cell(ej["solucion"]))
        cells.append(md_cell(rubrica_md(ej["rubrica"], ej["pts"])))

    return notebook(cells, "Clase 27 - Evaluación Ciclos - Solucionario")


# ── Solucionario para publicar a estudiantes (sin rúbrica de corrección) ─────

def build_solucionario_estudiantes_notebook() -> dict:
    puntaje_rows = [(item["id"], tipo_label(item), item["pts"]) for item in ITEMS_1]
    puntaje_rows += [(f"2.{ej['num']}", ej["titulo"], ej["pts"]) for ej in EJERCICIOS_2]

    cells = [
        md_cell(
            "# ✅ Solucionario — Evaluación Individual Ciclos\n\n"
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
        md_cell("---\n\n## 🔥 Sección 1 — Ítems cortos (32 pts)"),
    ]

    last_tipo = None
    for item in ITEMS_1:
        if item["tipo"] != last_tipo:
            cells.append(md_cell(
                "### 1A — Arma el código" if item["tipo"] == "arma"
                else "### 1B — Arregla el bug"
            ))
            last_tipo = item["tipo"]

        cells.append(md_cell(
            f"---\n\n**Ítem {item['id']}** ({item['pts']} pts)\n\n"
            f"{item['narrativa']}"
        ))
        cells.append(code_cell(item["solucion"] + f"\n\n# Esperado:\n# {item['esperado'].replace(chr(10), chr(10) + '# ')}"))
        cells.append(md_cell(f"🔎 **Qué se revisó:** {item['criterio']}"))

    cells.append(md_cell("---\n\n## 💻 Sección 2 — Programas completos (68 pts)"))

    for ej in EJERCICIOS_2:
        if ej["usa_input"]:
            resultado_md = tabla_html(ej["ej1_in"], ej["ej1_out"], ej["ej2_in"], ej["ej2_out"])
        else:
            resultado_md = salida_fija(ej["esperado"])

        cells.append(md_cell(
            f"---\n\n### Ejercicio {ej['num']} — {ej['titulo']} ({ej['pts']} pts)\n\n"
            f"{ej['narrativa']}\n\n"
            "**El programa debe:**\n"
            + "\n".join(f"- {d}" for d in ej["debe"])
            + "\n\n"
            + resultado_md
        ))
        cells.append(code_cell(ej["solucion"]))
        cells.append(md_cell(f"🔎 **Qué se revisó:** {ej['criterio']}"))

    cells.append(md_cell(
        "---\n\n## 🏁 Fin del solucionario\n\n"
        "¿Alguna respuesta no te calzó? Pregúntale al profesor antes de la "
        "próxima clase."
    ))

    return notebook(
        cells, "Clase 27 - Evaluación Ciclos - Solucionario Estudiantes"
    )


if __name__ == "__main__":
    import json

    def _guardar(nb: dict, nombre: str) -> None:
        with open(nombre, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"Generado: {nombre}")

    _guardar(build_student_notebook(), "Clase 27 - Evaluación Ciclos - Evaluación.ipynb")
    _guardar(build_preview_notebook(), "Clase 27 - Evaluación Ciclos - Preview con Respuestas.ipynb")
    _guardar(build_solucionario_notebook(), "Clase 27 - Evaluación Ciclos - Solucionario.ipynb")
    _guardar(build_solucionario_estudiantes_notebook(), "Clase 27 - Evaluación Ciclos - Solucionario Estudiantes.ipynb")
