#!/usr/bin/env python3
"""
generar_simulacro.py — Genera Simulacro.ipynb (estudiantes) y
Solucionario.ipynb (revisión conjunta) para la Clase 26 - Simulacro Ciclos.

Fuente de verdad: los datos embebidos en este script (mismo patrón que
generar_evaluacion.py). No editar los .ipynb generados a mano — si hay que
cambiar algo, se edita este script y se regenera.

Uso:
    python generar_simulacro.py
"""

from pathlib import Path
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

CARPETA = Path(__file__).resolve().parent

# =====================================================================
# DATOS
# =====================================================================

GUIADA = {
    "titulo": "🎮 Torneo de videojuegos — el puntaje más alto",
    "narrativa": (
        "Un torneo de videojuegos registra los puntajes de la ronda de "
        "clasificación. Cada jugador ingresa su puntaje, uno por uno, y el "
        "sistema debe seguir recibiendo puntajes hasta que se ingresa **-1**, "
        "que marca el fin de la ronda. Al terminar, el sistema debe informar "
        "cuál fue el **puntaje más alto** registrado en toda la ronda."
    ),
    "debe": [
        "Pedir puntajes repetidamente con `while`, hasta recibir `-1`.",
        "Ir comparando cada puntaje ingresado con el más alto registrado hasta "
        "el momento, y quedarse con el mayor.",
        "Imprimir el puntaje más alto al terminar.",
        "Si el primer ingreso ya es `-1` (no se registró ningún puntaje), "
        "informar que no hubo puntajes, sin mostrar un máximo.",
    ],
    "pista": (
        "<details><summary>💡 Pista — Cómo partir el máximo</summary>\n\n"
        "Antes de tener ningún puntaje, todavía no existe un \"máximo\". Puedes "
        "usar el primer puntaje válido que se ingrese como punto de partida, y "
        "desde ahí ir comparando los que vengan después.\n\n</details>"
    ),
    "resultado_tabla": (
        "| Ejemplo 1 | Ejemplo 2 |\n"
        "|---|---|\n"
        "| 📥 *El usuario ingresa:*<br>`850`<br>`1200`<br>`690`<br>`-1` "
        "| 📥 *El usuario ingresa:*<br>`-1` |\n"
        "| 📤 *El programa imprime:*<br>`Puntaje más alto: 1200` "
        "| 📤 *El programa imprime:*<br>`No se registró ningún puntaje.` |"
    ),
    "solucion": '''puntaje_ingresado = int(input("Ingresa el puntaje (o -1 para terminar): "))
puntaje_maximo = None

while puntaje_ingresado != -1:
    if puntaje_maximo is None or puntaje_ingresado > puntaje_maximo:
        puntaje_maximo = puntaje_ingresado
    puntaje_ingresado = int(input("Ingresa el puntaje (o -1 para terminar): "))

if puntaje_maximo is None:
    print("No se registró ningún puntaje.")
else:
    print("Puntaje más alto:", puntaje_maximo)
''',
    "que_se_reviso": (
        "Que el máximo se inicialice de forma segura (no en 0, porque un "
        "puntaje podría ser negativo o el primer dato ya podría ser el mayor) "
        "y que el caso \"sin puntajes\" (primer ingreso ya es -1) no intente "
        "mostrar un máximo que nunca existió."
    ),
}

SECCION_1 = [
    {
        "id": "1A.1",
        "tipo": "Arma el código",
        "titulo": "Radio escolar",
        "narrativa": (
            "La radio escolar transmite un anuncio publicitario cada 3 minutos, "
            "desde el minuto 0 hasta el minuto 21 de un bloque de transmisión. "
            "El programa debe imprimir en qué minutos se transmite un anuncio."
        ),
        "codigo_estudiante": '''for minuto in    # completar
    print("Anuncio en el minuto", minuto)
''',
        "pista": (
            "<details><summary>💡 Pista</summary>\n\n"
            "Un `range()` de tres números es `range(inicio, fin, paso)` — "
            "recuerda que el fin queda excluido, así que debe ser un número más "
            "que el último minuto que quieres incluir.\n\n</details>"
        ),
        "esperado": (
            "Anuncio en el minuto 0\nAnuncio en el minuto 3\n"
            "Anuncio en el minuto 6\n...\nAnuncio en el minuto 21"
        ),
        "codigo_solucion": '''for minuto in range(0, 22, 3):
    print("Anuncio en el minuto", minuto)
''',
        "que_se_reviso": "Que el `range()` use los 3 parámetros (inicio, fin, paso) y que el fin quede uno más allá del minuto 21 para no perderlo.",
    },
    {
        "id": "1A.2",
        "tipo": "Arma el código",
        "titulo": "Parque de diversiones",
        "narrativa": (
            "El sistema de un parque de diversiones revisa las atracciones "
            "numeradas del 1 al 12, buscando la primera que tiene mantenimiento "
            "programado: la atracción N°9. Apenas la encuentra, debe avisar cuál "
            "es y **detener la búsqueda de inmediato**, sin seguir revisando las "
            "que quedan."
        ),
        "codigo_estudiante": '''for atraccion in range(1, 13):
    if atraccion == 9:
        print("Atracción en mantenimiento: N°", atraccion)
        # completar: detener la búsqueda
''',
        "pista": (
            "<details><summary>💡 Pista</summary>\n\n"
            "Piensa en la instrucción que corta un ciclo de inmediato, sin "
            "esperar a que termine de recorrer los valores que quedan.\n\n</details>"
        ),
        "esperado": "Atracción en mantenimiento: N° 9",
        "codigo_solucion": '''for atraccion in range(1, 13):
    if atraccion == 9:
        print("Atracción en mantenimiento: N°", atraccion)
        break
''',
        "que_se_reviso": "Que el `break` quede dentro del `if` (para cortar justo al encontrar la atracción) y no fuera de él.",
    },
    {
        "id": "1B.1",
        "tipo": "Arregla el bug",
        "titulo": "Campamento de verano",
        "narrativa": (
            "Un campamento de verano organiza 3 cabañas con 4 actividades cada "
            "una. El sistema debe imprimir cada actividad de cada cabaña, pero "
            "algo salió mal: solo se imprime la última actividad de cada cabaña."
        ),
        "codigo_estudiante": '''for cabana in range(1, 4):
    for actividad in range(1, 5):
        numero_actividad = actividad
    print("Cabaña", cabana, "- Actividad", numero_actividad)
''',
        "pista": (
            "<details><summary>💡 Pista</summary>\n\n"
            "Cuenta cuántas veces se ejecuta el `print()` tal como está escrito, "
            "y compáralo con cuántas veces debería ejecutarse según el "
            "enunciado.\n\n</details>"
        ),
        "esperado": (
            "Cabaña 1 - Actividad 1\nCabaña 1 - Actividad 2\n"
            "Cabaña 1 - Actividad 3\nCabaña 1 - Actividad 4\n...\n"
            "Cabaña 3 - Actividad 4  (12 líneas en total)"
        ),
        "codigo_solucion": '''for cabana in range(1, 4):
    for actividad in range(1, 5):
        numero_actividad = actividad
        print("Cabaña", cabana, "- Actividad", numero_actividad)
''',
        "que_se_reviso": "Que el `print()` quede indentado dentro del ciclo interno — el bug lo dejaba a la altura del ciclo externo, así que solo corría una vez por cabaña.",
    },
    {
        "id": "1B.2",
        "tipo": "Arregla el bug",
        "titulo": "App de estudio",
        "narrativa": (
            "Una app de estudio revisa 8 flashcards numeradas del 1 al 8 y debe "
            "contar cuántas son de **repaso rápido**: las de número **par**. Las "
            "impares se saltan con `continue`. Pero el contador de repaso rápido "
            "nunca sube como corresponde — siempre termina en 8."
        ),
        "codigo_estudiante": '''contador_repaso_rapido = 0

for numero_flashcard in range(1, 9):
    contador_repaso_rapido = contador_repaso_rapido + 1
    if numero_flashcard % 2 != 0:
        continue

print("Repaso rápido:", contador_repaso_rapido)
''',
        "pista": (
            "<details><summary>💡 Pista</summary>\n\n"
            "Revisa el orden: ¿la línea que suma el contador se ejecuta antes o "
            "después de que el programa decida si esa flashcard se salta?\n\n</details>"
        ),
        "esperado": "Repaso rápido: 4",
        "codigo_solucion": '''contador_repaso_rapido = 0

for numero_flashcard in range(1, 9):
    if numero_flashcard % 2 != 0:
        continue
    contador_repaso_rapido = contador_repaso_rapido + 1

print("Repaso rápido:", contador_repaso_rapido)
''',
        "que_se_reviso": "Que el incremento del contador quede después del `if`/`continue`, para que el `continue` sí lo proteja de contar las flashcards impares.",
    },
]

DESARROLLO = [
    {
        "id": "2.1",
        "titulo": "Feria de talentos",
        "narrativa": (
            "La feria de talentos del liceo tiene 4 bloques de presentaciones. "
            "El bloque *i* tiene *i* presentaciones, y cada presentación dura 8 "
            "minutos. El programa debe calcular el **total de minutos** de "
            "presentaciones en toda la feria, y además contar en **cuántos "
            "bloques se superaron los 24 minutos** de duración."
        ),
        "debe": [
            "Usar `bloques_totales = 4`.",
            "Para cada bloque (empezando en 1), calcular los minutos de ese "
            "bloque sumando 8 minutos por cada presentación que le "
            "corresponde, y acumular ese subtotal en el total general de la "
            "feria.",
            "Contar en cuántos bloques la duración del bloque superó los 24 "
            "minutos (estrictamente mayor).",
            "Imprimir el total de minutos de toda la feria y la cantidad de "
            "bloques que superaron los 24 minutos, cada uno con su etiqueta.",
        ],
        "pistas": [
            "<details><summary>💡 Pista 1 — Reinicia el contador de minutos en cada bloque</summary>\n\n"
            "Antes de empezar a contar las presentaciones de un bloque nuevo, la "
            "variable que acumula los minutos de ese bloque debe volver a partir "
            "en 0.\n\n</details>",
            "<details><summary>💡 Pista 2 — El contador de bloques se revisa después del ciclo interno</summary>\n\n"
            "Recién cuando terminaste de sumar todas las presentaciones de un "
            "bloque sabes si ese bloque superó los 24 minutos.\n\n</details>",
        ],
        "esperado": (
            "Total de minutos de la feria: 80\nBloques que superaron los 24 minutos: 1"
        ),
        "codigo_solucion": '''bloques_totales = 4
total_minutos_feria = 0
bloques_sobre_24 = 0

for bloque in range(1, bloques_totales + 1):
    minutos_bloque = 0
    for presentacion in range(1, bloque + 1):
        minutos_bloque = minutos_bloque + 8
    total_minutos_feria = total_minutos_feria + minutos_bloque
    if minutos_bloque > 24:
        bloques_sobre_24 = bloques_sobre_24 + 1

print("Total de minutos de la feria:", total_minutos_feria)
print("Bloques que superaron los 24 minutos:", bloques_sobre_24)
''',
        "que_se_reviso": "Que el acumulador de minutos del bloque se reinicie en cada vuelta del ciclo externo, y que el contador de bloques se evalúe recién después de cerrar el ciclo interno.",
    },
    {
        "id": "2.2",
        "titulo": "Invernadero escolar",
        "narrativa": (
            "Un invernadero escolar registra la temperatura de sus primeros 6 "
            "sensores del día, ingresada manualmente uno por uno. El programa "
            "debe contar cuántas lecturas fueron **\"normales\"** (entre 18 y 28 "
            "grados, ambos límites incluidos) y cuántas fueron **\"de alerta\"** "
            "(fuera de ese rango)."
        ),
        "debe": [
            "Usar un `for` con `range(6)` para repetir exactamente 6 veces.",
            "Por cada vuelta, pedir la temperatura del sensor correspondiente "
            "con `input()` (puede tener decimales).",
            "Clasificar cada lectura como normal o de alerta, según el rango "
            "indicado.",
            "Imprimir ambos conteos al terminar, cada uno con su etiqueta.",
        ],
        "pistas": [
            "<details><summary>💡 Pista 1 — Dos contadores, uno por categoría</summary>\n\n"
            "Necesitas una variable que cuente las lecturas normales y otra "
            "distinta que cuente las de alerta — cada lectura suma a una sola "
            "de las dos.\n\n</details>",
            "<details><summary>💡 Pista 2 — Ambos límites incluidos</summary>\n\n"
            "Una lectura de exactamente 18 o exactamente 28 grados cuenta como "
            "normal, no como de alerta.\n\n</details>",
        ],
        "resultado_tabla": (
            "| Ejemplo 1 | Ejemplo 2 |\n"
            "|---|---|\n"
            "| 📥 *El usuario ingresa:*<br>`20`<br>`30`<br>`18`<br>`28`<br>`15`<br>`22` "
            "| 📥 *El usuario ingresa:*<br>`15`<br>`35`<br>`20`<br>`25`<br>`10`<br>`40` |\n"
            "| 📤 *El programa imprime:*<br>`Lecturas normales: 4`<br>`Lecturas de alerta: 2` "
            "| 📤 *El programa imprime:*<br>`Lecturas normales: 2`<br>`Lecturas de alerta: 4` |"
        ),
        "codigo_solucion": '''normales = 0
alerta = 0

for sensor in range(6):
    temperatura = float(input("Temperatura del sensor (°C): "))
    if temperatura >= 18 and temperatura <= 28:
        normales = normales + 1
    else:
        alerta = alerta + 1

print("Lecturas normales:", normales)
print("Lecturas de alerta:", alerta)
''',
        "que_se_reviso": "Que cada lectura sume a una sola de las dos categorías (no a un acumulador de suma) y que los límites 18 y 28 cuenten como normales.",
    },
]

TICKET = [
    {
        "numero": 1,
        "codigo": 'for numero in range(2, 10, 2):\n    print(numero)',
        "enunciado": "¿Qué imprime este programa?",
        "alternativas": {
            "A": "2, 4, 6, 8",
            "B": "2, 4, 6, 8, 10",
            "C": "2, 3, 4, 5, 6, 7, 8, 9",
            "D": "10, 8, 6, 4, 2",
        },
        "correcta": "A",
        "justificacion": (
            "`range(2, 10, 2)` empieza en 2, avanza de 2 en 2, y se detiene "
            "antes de llegar a 10 — el límite superior queda excluido."
        ),
    },
    {
        "numero": 2,
        "codigo": (
            'total = 0\nfor fila in range(1, 4):\n'
            '    for columna in range(1, 3):\n        total = total + 1\n'
            'print("Total:", total)'
        ),
        "enunciado": "¿Qué imprime este programa?",
        "alternativas": {
            "A": "Total: 3",
            "B": "Total: 6",
            "C": "Total: 2",
            "D": "Total: 9",
        },
        "correcta": "B",
        "justificacion": (
            "El ciclo interno se ejecuta 2 veces por cada una de las 3 vueltas "
            "del ciclo externo, así que el contador suma 1 un total de 3×2 = 6 "
            "veces."
        ),
    },
    {
        "numero": 3,
        "codigo": (
            'numero = 0\nwhile numero < 6:\n    numero = numero + 1\n'
            '    if numero % 2 == 0:\n        continue\n'
            '    if numero == 5:\n        break\n    print(numero)'
        ),
        "enunciado": "¿Qué imprime este programa?",
        "alternativas": {
            "A": "1, 3, 5",
            "B": "1, 2, 3, 4, 5",
            "C": "1, 3",
            "D": "1",
        },
        "correcta": "C",
        "justificacion": (
            "`continue` salta el `print()` de los pares (2 y 4) pero no termina "
            "el ciclo; `break` sí lo termina, y ocurre en `numero == 5` antes de "
            "llegar a su `print()`, así que el 5 nunca se imprime. Solo se "
            "imprimen 1 y 3."
        ),
    },
]

FORM_URL = "https://forms.gle/sjRpbgmQzrpkEBsH9"


# =====================================================================
# HELPERS DE FORMATO
# =====================================================================

def bullets(items):
    return "\n".join(f"- {i}" for i in items) + "\n"


def pre(texto):
    return f"<pre>\n{texto}\n</pre>\n"


# =====================================================================
# SIMULACRO.IPYNB (estudiantes)
# =====================================================================

def construir_simulacro():
    nb = new_notebook()
    cells = []

    cells.append(new_markdown_cell(
        "# 📝 Simulacro — Ciclos\n\n"
        "**Fecha:** martes 25 de agosto, 2026\n\n"
        "📅 **Fecha:** ___________________________  \n"
        "👤 **Nombre:** ___________________________  \n"
        "📌 **Curso:** ___________________________"
    ))

    cells.append(new_markdown_cell(
        "## 🎯 Objetivo de la sesión\n\n"
        "Aplicar `for`+`range()`, `for` anidado, `while` y `continue`/`break` "
        "en problemas estilo evaluación, para llegar con seguridad a la "
        "Evaluación de Ciclos del jueves.\n\n"
        "## 💡 Propósito\n\n"
        "> Hoy simulamos las condiciones de la evaluación del jueves: mismos "
        "tipos de problemas, mismo trabajo individual, pero sin nota. "
        "Practicar bajo esa presión controlada, y revisar juntos los errores "
        "al final, es lo que te permite llegar con más confianza al día real."
    ))

    cells.append(new_markdown_cell(
        "---\n\n## 📋 Instrucciones generales\n\n"
        "- Esta sesión tiene 3 partes: una **Práctica Guiada** (se resuelve en "
        "conjunto), 4 **ítems cortos**, y 2 **programas de desarrollo**.\n"
        "- **No lleva nota.** Al terminar, revisamos juntos los errores más "
        "comunes.\n"
        "- El código debe ejecutarse sin errores. Si no terminas un ítem, "
        "deja lo que alcanzaste.\n"
        "- Usa nombres de variables en **snake_case en español**.\n"
        "- Cuando un ítem pida un dato con `input()`, el enunciado siempre "
        "aclara si es un número entero, un número con decimales, o una "
        "palabra exacta."
    ))

    # Práctica Guiada
    g = GUIADA
    md = f"---\n\n## 🧭 Práctica Guiada — se resuelve en conjunto\n\n### {g['titulo']}\n\n"
    md += g["narrativa"] + "\n\n"
    md += "**El programa debe:**\n\n" + bullets(g["debe"]) + "\n"
    md += g["pista"] + "\n\n"
    md += "**Resultado esperado:**\n\n" + g["resultado_tabla"] + "\n"
    cells.append(new_markdown_cell(md))
    cells.append(new_code_cell("# Tu programa\n"))

    # Sección 1
    cells.append(new_markdown_cell(
        "---\n\n## 🔥 Sección 1 — Ítems cortos\n\n"
        "Dos ítems de armar código + dos de arreglar un bug. Completa "
        "directamente en la misma celda de código."
    ))
    for item in SECCION_1:
        md = f"---\n\n**Ítem {item['id']}** — {item['tipo']}\n\n{item['narrativa']}\n"
        cells.append(new_markdown_cell(md))
        cells.append(new_code_cell(item["codigo_estudiante"].rstrip() + "\n"))
        md2 = item["pista"] + "\n\n"
        md2 += "📤 <em>El programa imprime:</em>\n\n" + pre(item["esperado"])
        cells.append(new_markdown_cell(md2))

    # Sección 2
    cells.append(new_markdown_cell(
        "---\n\n## 💻 Sección 2 — Desarrollo\n\n"
        "Programas completos desde una narrativa. El Ejercicio 2 pide datos "
        "con `input()` — lee bien el tipo de dato que se espera antes de "
        "escribir tu código."
    ))
    for i, ej in enumerate(DESARROLLO, 1):
        md = f"---\n\n## 🎯 Ejercicio {i} — {ej['titulo']}\n\n{ej['narrativa']}\n\n"
        md += "**El programa debe:**\n\n" + bullets(ej["debe"]) + "\n"
        for p in ej["pistas"]:
            md += p + "\n\n"
        if ej.get("esperado"):
            md += "📤 <em>El programa imprime:</em>\n\n" + pre(ej["esperado"])
        elif ej.get("resultado_tabla"):
            md += ej["resultado_tabla"] + "\n"
        cells.append(new_markdown_cell(md))
        cells.append(new_code_cell(f"# Ejercicio {i}\n\n\n"))

    # Ticket de Salida — solo el aviso, nunca las preguntas
    cells.append(new_markdown_cell(
        "---\n\n## 🎫 Ticket de Salida\n\n"
        "Ahora proyectamos 3 preguntas en la tele, una por una. Decide tu "
        "respuesta en silencio y anótala — recién al terminar la última "
        "completamos juntos el Formulario:\n\n"
        f"[{FORM_URL}]({FORM_URL})\n\n"
        "En \"Tema de la clase de hoy\" escribe: `simulacro ciclos`."
    ))

    # Cierre
    cells.append(new_markdown_cell(
        "---\n\n## 🏁 Cierre\n\n"
        "Revisa que todas tus celdas se ejecuten sin errores. Ahora vamos a "
        "revisar juntos, en el `Solucionario`, los errores más comunes de "
        "cada ítem — antes de la Evaluación del jueves."
    ))

    nb.cells = cells
    return nb


# =====================================================================
# SOLUCIONARIO.IPYNB (revisión conjunta)
# =====================================================================

def construir_solucionario():
    nb = new_notebook()
    cells = []

    cells.append(new_markdown_cell(
        "# 🔎 Solucionario — Simulacro Ciclos\n\n"
        "**Uso:** documento para la revisión conjunta en clase. Actividad "
        "formativa, sin nota — cada ítem trae una nota breve de **qué se "
        "revisó**, pensada para comentar en voz alta con el curso, no una "
        "rúbrica de puntaje."
    ))

    # Guiada
    g = GUIADA
    cells.append(new_markdown_cell(f"---\n\n## 🧭 Práctica Guiada — {g['titulo']}"))
    cells.append(new_code_cell(g["solucion"].rstrip() + "\n"))
    cells.append(new_markdown_cell(f"🔎 **Qué se revisó:** {g['que_se_reviso']}"))

    # Sección 1
    cells.append(new_markdown_cell("---\n\n## 🔥 Sección 1 — Ítems cortos"))
    for item in SECCION_1:
        cells.append(new_markdown_cell(
            f"**Ítem {item['id']}** — {item['titulo']} ({item['tipo']}) — solución esperada:"
        ))
        cells.append(new_code_cell(item["codigo_solucion"].rstrip() + "\n"))
        cells.append(new_markdown_cell(f"🔎 **Qué se revisó:** {item['que_se_reviso']}"))

    # Sección 2
    cells.append(new_markdown_cell("---\n\n## 💻 Sección 2 — Desarrollo"))
    for i, ej in enumerate(DESARROLLO, 1):
        cells.append(new_markdown_cell(f"### Ejercicio {i} — {ej['titulo']}"))
        cells.append(new_code_cell(ej["codigo_solucion"].rstrip() + "\n"))
        cells.append(new_markdown_cell(f"🔎 **Qué se revisó:** {ej['que_se_reviso']}"))

    # Ticket de Salida
    cells.append(new_markdown_cell("---\n\n## 🎫 Ticket de Salida"))
    for p in TICKET:
        md = f"### Pregunta {p['numero']}\n\n```python\n{p['codigo']}\n```\n\n{p['enunciado']}\n\n"
        for letra, texto in p["alternativas"].items():
            marca = " ✅" if letra == p["correcta"] else ""
            md += f"**{letra}:** {texto}{marca}\n\n"
        md += f"> 💡 {p['justificacion']}\n"
        cells.append(new_markdown_cell(md))

    nb.cells = cells
    return nb


# =====================================================================
# MAIN
# =====================================================================

def main():
    nb_simulacro = construir_simulacro()
    nb_solucionario = construir_solucionario()

    ruta_simulacro = CARPETA / "Clase 26 - Simulacro Ciclos - Simulacro.ipynb"
    ruta_solucionario = CARPETA / "Clase 26 - Simulacro Ciclos - Solucionario.ipynb"

    nbformat.write(nb_simulacro, ruta_simulacro)
    nbformat.write(nb_solucionario, ruta_solucionario)

    print("OK", ruta_simulacro.name, len(nb_simulacro.cells), "celdas")
    print("OK", ruta_solucionario.name, len(nb_solucionario.cells), "celdas")


if __name__ == "__main__":
    main()
