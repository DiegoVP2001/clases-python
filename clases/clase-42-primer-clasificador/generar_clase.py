"""Genera 'Clase 42 - Primer Clasificador - Clase.ipynb' (estudiantes) y '... - Solucionario.ipynb' (profesor).

Fuente de verdad: este script + la Spec aprobada. No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.
Ejecutar: py -3 generar_clase.py
Los resultados esperados se calculan ejecutando las soluciones (así nunca se desfasan del código).
"""
import base64
import contextlib
import hashlib
import html
import io
import json
import textwrap
import uuid
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA_CLASE = AQUI / "Clase 42 - Primer Clasificador - Clase.ipynb"
SALIDA_SOL = AQUI / "Clase 42 - Primer Clasificador - Solucionario.ipynb"

# ───────────────────────── utilidades de celdas ─────────────────────────


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {},
            "source": texto.strip("\n").splitlines(keepends=True)}


def codigo(texto: str) -> dict:
    return {"cell_type": "code", "id": uuid.uuid4().hex[:8], "metadata": {}, "execution_count": None,
            "outputs": [], "source": texto.strip("\n").splitlines(keepends=True)}


def ejecutar(texto: str) -> str:
    """Ejecuta un trozo de código y devuelve lo que imprime (para armar los resultados esperados)."""
    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        exec(textwrap.dedent(texto), {})
    return salida.getvalue().rstrip("\n")


def esperado(texto_salida: str, nota: str = "") -> str:
    bloque = "📤 <em>El programa imprime:</em>\n\n<pre>" + html.escape(texto_salida) + "</pre>"
    return bloque + (f"\n\n{nota}" if nota else "")


def pista(n: int, titulo: str, texto: str) -> str:
    return f"<details><summary>💡 Pista {n} — {titulo}</summary>\n\n{texto}\n\n</details>"


def idea(texto: str) -> str:
    return f"> **Idea clave:** {texto}"


def escribelo(instruccion: str) -> str:
    return f"✍️ **Escríbelo tú:** {instruccion}"


def cuaderno(celdas: list) -> dict:
    return {"cells": celdas,
            "metadata": {"colab": {"provenance": []},
                         "kernelspec": {"display_name": "Python 3", "name": "python3"},
                         "language_info": {"name": "python"}},
            "nbformat": 4, "nbformat_minor": 5}


def guardar(ruta: Path, celdas: list) -> None:
    ruta.write_text(json.dumps(cuaderno(celdas), ensure_ascii=False, indent=1), encoding="utf-8")


# ───────────────────────── datos de la clase ─────────────────────────

ENTRADAS = ("entradas = [[0, 1, 10], [0, 2, 25], [1, 0, 15], [0, 3, 30], [2, 1, 20], [0, 0, 8],\n"
            "            [12, 6, 22], [15, 8, 30], [8, 7, 12], [20, 9, 18], [10, 2, 28], [18, 5, 9],\n"
            "            [3, 8, 14], [0, 9, 26], [6, 1, 35], [14, 3, 20]]\n"
            "etiquetas = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]")

# Guiada: micro de las 18:30 que vuelve de Santiago
G_DATOS = ("entradas = [[0, 2, 5], [3, 6, 8], [0, 9, 6], [5, 1, 4], [0, 3, 20], [2, 4, 25], [12, 5, 18], [1, 8, 30]]\n"
           "etiquetas = [0, 0, 0, 0, 1, 1, 1, 1]\n"
           "dias_nuevos = [[0, 5, 7], [10, 2, 22], [4, 9, 12]]")
# Ej 1: Naltagua, ¿conviene el colectivo? (1 = conviene el colectivo)
E1_DATOS = ("entradas = [[0, 2, 5], [1, 6, 8], [0, 3, 10], [2, 7, 6], [0, 1, 25],\n"
            "            [3, 2, 30], [15, 2, 8], [10, 6, 12], [18, 3, 20], [9, 1, 9]]\n"
            "etiquetas = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]\n"
            "dias_nuevos = [[0, 4, 9], [2, 8, 22]]")
# Ej 2: furgón de las 7:30 (1 = llegó después del timbre)
E2_DATOS = ("entradas = [[0, 0, 8], [2, 0, 12], [0, 3, 10], [3, 5, 9], [10, 0, 14],\n"
            "            [8, 2, 6], [12, 0, 11], [15, 6, 13], [6, 5, 7], [9, 1, 12]]\n"
            "etiquetas = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]\n"
            "dias_nuevos = [[1, 0, 10], [8, 0, 5]]")
# Ej 3: feria de la Casona del Maipo (1 = llegó tarde al montaje)
E3_DATOS = ("entradas = [[0, 10, 20], [0, 25, 30], [2, 5, 15], [1, 20, 40], [0, 15, 25], [4, 30, 18], [0, 50, 22],\n"
            "            [3, 55, 35], [12, 20, 45], [15, 10, 50], [10, 35, 48], [20, 40, 30], [14, 5, 55], [0, 45, 12]]\n"
            "etiquetas = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]\n"
            "dias_nuevos = [[0, 20, 30], [16, 15, 52], [5, 45, 20]]")
# Ej 0a: calentamiento
E0_DATOS = ("entradas = [[1, 2], [2, 1], [8, 9], [9, 8], [7, 9], [2, 2]]\n"
            "etiquetas = [0, 0, 1, 1, 1, 0]\n"
            "dia_nuevo = [3, 2]")

CENTINELA = "# ── Escribe tu programa desde aquí ──"

# ───────────────────────── soluciones (se ejecutan para obtener los resultados esperados) ─────────────────────────

SOL_ICN1 = """from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
print("Modelo creado:", modelo)"""

SOL_ICN2 = ENTRADAS + """

from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo.fit(entradas, etiquetas)
print("El modelo ya aprendió de", len(entradas), "días")"""

SOL_ICN3 = ENTRADAS + """

from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo.fit(entradas, etiquetas)

dia_nuevo = [0, 2, 12]
prediccion = modelo.predict([dia_nuevo])
print("Predicción para el día nuevo (0 = puntual, 1 = atrasada):", prediccion)"""

SOL_ICN4 = ENTRADAS + """

from sklearn.tree import DecisionTreeClassifier, export_text

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo.fit(entradas, etiquetas)

nombres_variables = ["lluvia_mm", "km_taco", "pasajeros"]
print(export_text(modelo, feature_names=nombres_variables))"""

SOL_G = """from sklearn.tree import DecisionTreeClassifier

""" + G_DATOS + """

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo.fit(entradas, etiquetas)

prediccion = modelo.predict(dias_nuevos)
print("Predicciones de los días nuevos (0 = puntual, 1 = atrasada):", prediccion)

# Día 1 (0 mm, 5 km de taco, 7 min de espera): puntual. Cuadra: en los datos, con poca espera la micro salió puntual.
# Día 2 (10 mm, 2 km de taco, 22 min de espera): atrasada. Cuadra: con mucha espera, los datos la muestran atrasada.
# Día 3 (4 mm, 9 km de taco, 12 min de espera): puntual. Llama la atención con 9 km de taco, pero en los datos hay
#   un día con 9 km de taco y poca espera que salió puntual: el árbol sólo miró la espera, así que conviene revisarlo."""

SOL_E0 = """from sklearn.tree import DecisionTreeClassifier

""" + E0_DATOS + """

modelo = DecisionTreeClassifier(max_depth=2, random_state=0)
modelo.fit(entradas, etiquetas)
prediccion = modelo.predict([dia_nuevo])
print("Predicción del caso nuevo:", prediccion)"""

SOL_E1 = """from sklearn.tree import DecisionTreeClassifier

""" + E1_DATOS + """

modelo = DecisionTreeClassifier(max_depth=2, random_state=0)
modelo.fit(entradas, etiquetas)
prediccion = modelo.predict(dias_nuevos)
print("Predicciones de los 2 días nuevos (0 = micro, 1 = colectivo):", prediccion)"""

SOL_E2 = """from sklearn.tree import DecisionTreeClassifier

""" + E2_DATOS + """

modelo = DecisionTreeClassifier(max_depth=2, random_state=0)
modelo.fit(entradas, etiquetas)
prediccion = modelo.predict(dias_nuevos)
print("Predicciones de las 2 mañanas nuevas (0 = a tiempo, 1 = después del timbre):", prediccion)"""

SOL_E3 = """from sklearn.tree import DecisionTreeClassifier, export_text

""" + E3_DATOS + """

modelo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo.fit(entradas, etiquetas)
prediccion = modelo.predict(dias_nuevos)
print("Predicciones de los 3 días nuevos (0 = a tiempo, 1 = tarde):", prediccion)

dia_cambiado = [0, 20, 46]
prediccion_cambiada = modelo.predict([dia_cambiado])
print("Primer día con 46 cajas en vez de 30:", prediccion_cambiada)

print(export_text(modelo, feature_names=["lluvia_mm", "minutos_salida", "cajas"]))"""

SOL_E4 = """from sklearn.tree import DecisionTreeClassifier, export_text

""" + E3_DATOS + """

nombres_variables = ["lluvia_mm", "minutos_salida", "cajas"]

modelo_corto = DecisionTreeClassifier(max_depth=1, random_state=0)
modelo_corto.fit(entradas, etiquetas)
modelo_largo = DecisionTreeClassifier(max_depth=3, random_state=0)
modelo_largo.fit(entradas, etiquetas)

print("Árbol con max_depth=1:")
print(export_text(modelo_corto, feature_names=nombres_variables))
print("Árbol con max_depth=3:")
print(export_text(modelo_largo, feature_names=nombres_variables))"""

# ───────────────────────── autochequeos (celda preparada) ─────────────────────────

# Ticket: letras correctas C, A, D, B (guardadas como huellas; la justificación va codificada)
TICKET_CORRECTAS = ["C", "A", "D", "B"]
TICKET_JUSTIFICACION = [
    "fit() entrena el modelo con los días anteriores; predict() usa lo aprendido para responder por un día nuevo.",
    "predict() espera una lista de días (una lista de listas); [0, 2, 12] es un solo día suelto, sin la lista que lo contiene.",
    "El primer día se mide con la pregunta lluvia_mm <= 5.00; con 9 mm la respuesta es «no», y esa rama dice class: 1 (atrasada). El km_taco no aparece en este árbol.",
    "El árbol no usó pasajeros y sus datos no tenían días con tanta gente; la conclusión prudente es pedir más datos, no decir que los pasajeros no importan.",
]
TICKET_PISTAS = [
    "Piensa qué recibe cada línea: una recibe los días anteriores con sus etiquetas y la otra, un día que aún no ocurrió.",
    "Mira cuántos corchetes tiene lo que se le entrega a predict() y compáralo con lo que usamos en clase.",
    "Parte por la primera pregunta del árbol y sigue la rama que corresponde a los datos del día; usa solo lo que el árbol mira.",
    "Pregúntate si el modelo ya comprobó algo sobre esa variable o si simplemente no la usó.",
]


def huella(i: int, letra: str) -> str:
    return hashlib.sha256(f"c42|{i}|{letra}".encode()).hexdigest()[:16]


def b64(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


CELDA_AUTOCHEQUEOS = '''
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)
import base64
import hashlib
from sklearn.tree import DecisionTreeClassifier


def _revisar(entradas, etiquetas):
    modelo_alumno = globals().get("modelo")
    if modelo_alumno is None:
        print("⚠️ Todavía no hay un modelo llamado modelo.")
        print("   Pista: crea el árbol y guárdalo en una variable con ese nombre.")
        return
    if not isinstance(modelo_alumno, DecisionTreeClassifier):
        print("⚠️ La variable modelo existe, pero no es un árbol de decisión.")
        print("   Pista: ¿con qué instrucción se crea el árbol?")
        return
    if not hasattr(modelo_alumno, "tree_"):
        print("⚠️ El árbol está creado, pero todavía no aprendió nada.")
        print("   Pista: falta el paso que le entrega los días anteriores y sus etiquetas.")
        return
    if modelo_alumno.n_features_in_ != len(entradas[0]) or modelo_alumno.tree_.n_node_samples[0] != len(entradas):
        print("⚠️ Tu modelo se entrenó con otros datos, no con los de este ejercicio.")
        print("   Pista: revisa qué le entregas al entrenar. Si volviste atrás, ejecuta de nuevo la celda de tu solución.")
        return
    if list(modelo_alumno.predict(entradas)) != list(etiquetas):
        print("⚠️ Tu árbol no logra acertar ni con los días de entrenamiento.")
        print("   Pista: revisa la profundidad máxima del árbol y el orden de lo que le entregas al entrenar.")
        return
    print("✅ Tu modelo está bien entrenado con los datos de este ejercicio.")
    print("   Ahora compara lo que imprimiste con el resultado esperado de arriba.")


def check_ej1():
    _revisar([[0, 2, 5], [1, 6, 8], [0, 3, 10], [2, 7, 6], [0, 1, 25],
              [3, 2, 30], [15, 2, 8], [10, 6, 12], [18, 3, 20], [9, 1, 9]],
             [0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


def check_ej2():
    _revisar([[0, 0, 8], [2, 0, 12], [0, 3, 10], [3, 5, 9], [10, 0, 14],
              [8, 2, 6], [12, 0, 11], [15, 6, 13], [6, 5, 7], [9, 1, 12]],
             [0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


def check_ej3():
    _revisar([[0, 10, 20], [0, 25, 30], [2, 5, 15], [1, 20, 40], [0, 15, 25], [4, 30, 18], [0, 50, 22],
              [3, 55, 35], [12, 20, 45], [15, 10, 50], [10, 35, 48], [20, 40, 30], [14, 5, 55], [0, 45, 12]],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])


_HUELLAS = __HUELLAS__
_RAZONES = __RAZONES__
_PISTAS = __PISTAS__


def check_ticket(respuestas):
    aciertos = 0
    for i, letra in enumerate(respuestas, start=1):
        letra = str(letra).strip().upper()
        if letra == "":
            print(f"⏳ Pregunta {i}: todavía sin responder.")
        elif letra not in ("A", "B", "C", "D"):
            print(f"⚠️ Pregunta {i}: escribe solo una letra (A, B, C o D).")
        elif hashlib.sha256(f"c42|{i}|{letra}".encode()).hexdigest()[:16] == _HUELLAS[i - 1]:
            aciertos += 1
            print(f"✅ Pregunta {i}: correcto. " + base64.b64decode(_RAZONES[i - 1]).decode("utf-8"))
        else:
            print(f"⚠️ Pregunta {i}: revísala otra vez. Pista: " + _PISTAS[i - 1])
    print(f"\\nAciertos: {aciertos} de {len(_HUELLAS)} (sin nota: es para que revises tu propia comprensión).")


print("Autochequeos listos ✅")
'''.replace("__HUELLAS__", json.dumps([huella(i, l) for i, l in enumerate(TICKET_CORRECTAS, start=1)])) \
   .replace("__RAZONES__", json.dumps([b64(t) for t in TICKET_JUSTIFICACION])) \
   .replace("__PISTAS__", json.dumps(TICKET_PISTAS, ensure_ascii=False))

# ───────────────────────── contenido compartido ─────────────────────────

HAZ_AHORA = [
    "¿Qué cosas del día, antes de las 7:00, podrían influir en que la micro se atrase?",
    "De esas cosas, ¿cuáles podríamos medir con un número?",
    "¿Qué dato tendríamos que anotar cada día para saber si la micro sí se atrasó?",
    "¿Cuántos días de datos pediríamos, más o menos, antes de confiar en el sistema?",
]

TICKET_PREGUNTAS = [
    ("`fit` y `predict`",
     "```python\nmodelo.fit(entradas, etiquetas)\nresultado = modelo.predict([[0, 2, 12]])\n```\n\n"
     "¿Qué hace cada línea?",
     ["`fit` predice el día nuevo y `predict` aprende de los días anteriores.",
      "Las dos líneas entrenan el modelo; la segunda con un día más.",
      "`fit` entrena con los días anteriores y `predict` usa lo aprendido para el día nuevo.",
      "`fit` crea el modelo y `predict` lo borra para empezar de cero."]),
    ("La forma de la entrada",
     "```python\nmodelo.fit(entradas, etiquetas)\nresultado = modelo.predict([0, 2, 12])   # <- esta línea\n```\n\n"
     "Esta línea falla. ¿Por qué?",
     ["`predict` espera una lista de días y se le entregó un solo día suelto, sin la lista que lo contiene.",
      "Falta entrenar el modelo antes de usar `predict`.",
      "12 pasajeros es un número demasiado grande para `predict`.",
      "`predict` solo funciona con días que ya estaban en los datos de entrenamiento."]),
    ("Leer el árbol",
     "```text\n|--- lluvia_mm <= 5.00\n|   |--- class: 0\n|--- lluvia_mm >  5.00\n|   |--- class: 1\n```\n\n"
     "Un día tiene 9 mm de lluvia y 1 km de taco (0 = puntual, 1 = atrasada). ¿Qué predice este árbol?",
     ["Puntual (0), porque el taco es bajo.",
      "No se puede saber, porque faltan los pasajeros.",
      "Puntual (0), porque 9 es mayor que 5 y eso significa «sin problemas».",
      "Atrasada (1), porque 9 mm de lluvia es más que 5 mm."]),
    ("Pensamiento crítico",
     "El árbol de la clase predice **puntual** para un día con 40 pasajeros esperando.\n\n"
     "¿Qué conviene concluir?",
     ["Que los pasajeros no influyen nunca en el atraso de la micro.",
      "Que el árbol no usó esa variable y sus datos no tenían días con tanta gente; conviene revisar con más datos.",
      "Que el árbol está mal construido, porque no debería predecir puntual.",
      "Que la predicción es segura, porque el árbol es un cálculo matemático."]),
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────


def imagen_diagrama() -> str:
    datos = base64.b64encode((AQUI / "diagramas" / "Diagrama - Un arbol de decision.png").read_bytes()).decode("ascii")
    return f"![Cómo decide un árbol de decisión](data:image/png;base64,{datos})"


DATOS_ICN = "# Datos de la micro de las 7:00 (ya escritos)\n" + ENTRADAS
CREAR = "\n\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=0)"
ENTRENAR = "\nmodelo.fit(entradas, etiquetas)"
PREDECIR = ("\n\ndia_nuevo = [0, 2, 12]\nprediccion = modelo.predict([dia_nuevo])\n"
            "print(\"Predicción para el día nuevo (0 = puntual, 1 = atrasada):\", prediccion)")

# Punto de partida de cada concepto = el código ya construido del concepto anterior (patrón de la Clase 37)
ARRANQUE_C1 = DATOS_ICN
ARRANQUE_C2 = "from sklearn.tree import DecisionTreeClassifier\n\n" + DATOS_ICN + CREAR
ARRANQUE_C3 = "from sklearn.tree import DecisionTreeClassifier\n\n" + DATOS_ICN + CREAR + ENTRENAR + "\n\ndia_nuevo = [0, 2, 12]"
ARRANQUE_C4 = ("from sklearn.tree import DecisionTreeClassifier\n\n" + DATOS_ICN + CREAR + ENTRENAR + PREDECIR
               + "\n\nnombres_variables = [\"lluvia_mm\", \"km_taco\", \"pasajeros\"]")
ARRANQUE_COMPARAR = ("from sklearn.tree import DecisionTreeClassifier\n\n" + DATOS_ICN + CREAR + ENTRENAR + PREDECIR
                     + "\n\ndia_a_comparar = [7, 4, 15]")


def celdas_comunes_clase() -> list:
    c = []
    c.append(md("# 🐍 Clase 42 — Primer clasificador ML\n\n"
                "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab\n\n---"))
    c.append(md("## 🎯 Objetivo de la clase\n\n"
                "Entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico.\n\n"
                "## 🔎 ¿Por qué lo veremos?\n\n"
                "> Cuando una app nos dice «tu micro llegará atrasada», alguien la entrenó con datos de días anteriores, y saber "
                "cómo se hace nos permite revisar si su respuesta tiene sentido. Hoy entrenamos un primer modelo con los datos "
                "de la micro de La Islita y lo usamos con días nuevos.\n\n---\n\n"
                "**Lo que ya sabes:** todo lo dictado hasta N°41 (el mapa de la IA, variables, etiqueta, entrenar ≠ predecir) y Python hasta listas.\n\n"
                "**Lo que aprenderás hoy:** crear un `DecisionTreeClassifier`, entrenarlo con `fit()`, predecir con `predict()` y leer sus preguntas con `export_text`. "
                "**Todos los datos vienen escritos en este cuaderno** (sin archivos ni descargas) y se ejecuta de arriba hacia abajo."))
    c.append(md("---\n\n## 1️⃣ Haz Ahora\n\n"
                "La junta de vecinos de La Islita quiere un sistema que le avise si la micro de las 7:00 hacia Santiago llegará atrasada, "
                "para decidir si salir antes o tomar colectivo. Todavía no sabe qué datos mirar ni cuántos necesita.\n\n"
                + "\n".join(f"{i}. {p}" for i, p in enumerate(HAZ_AHORA, start=1))
                + "\n\nLa junta, sabiendo que programamos, nos pide ayuda para armar ese sistema — pero antes quiere que tengamos clara la lógica."))
    c.append(md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "))
    c.append(md("---\n\n### 🔁 Recordemos la clase 41\n\n"
                "- **Variables:** lo que el modelo recibe para decidir.\n"
                "- **Etiqueta:** lo que queremos que el modelo prediga.\n"
                "- **Entrenar** es aprender de ejemplos; **predecir** es usar lo aprendido en un caso nuevo.\n\n"
                "Para la micro de La Islita:\n\n"
                "| Dato | Qué es | Ejemplo |\n|---|---|---|\n"
                "| `lluvia_mm` | variable: lluvia de la madrugada | 12 |\n"
                "| `km_taco` | variable: km de taco en la Ruta 78 a las 6:45 | 6 |\n"
                "| `pasajeros` | variable: personas esperando en el paradero | 22 |\n"
                "| etiqueta | `1` = la micro llegó atrasada · `0` = llegó puntual | 1 |"))
    return c


def icn_clase() -> list:
    c = []
    c.append(md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
                "Estudia cada concepto y escribe tú el código que falta en cada celda, siguiendo la instrucción. "
                "Cada celda ya trae **lo que construimos en el concepto anterior**: tú solo agregas lo nuevo."))
    c.append(md("### 💡 ¿Cómo se ve un árbol de decisión?\n\n"
                "Un **árbol de decisión** es una lista de **preguntas de sí/no** encadenadas. Para decidir, se parte desde la pregunta de arriba, "
                "se sigue la rama que corresponde a los datos del día y se repite hasta llegar a una **respuesta final**.\n\n"
                + imagen_diagrama() + "\n\n"
                "**Cómo leerlo:**\n\n"
                "1. Parte siempre desde la pregunta de arriba.\n"
                "2. Responde «sí» o «no» con los datos de tu día y sigue esa flecha.\n"
                "3. Si llegas a otra pregunta, vuelve al paso 2; si llegas a una caja de color, esa es la respuesta.\n\n"
                "> *Este árbol es un ejemplo inventado, para aprender a leerlo. El árbol de la micro lo va a encontrar el modelo solo, a partir de los datos.*"))
    c.append(md("### 💡 Crear el modelo\n\n"
                "Antes de usar un árbol hay que crearlo. Recién creado está vacío: todavía no sabe ninguna pregunta ni ninguna respuesta. "
                "Los **16 días** que anotó la junta de vecinos ya vienen escritos: cada día es una lista `[lluvia_mm, km_taco, pasajeros]` "
                "y su etiqueta está en la misma posición de `etiquetas`.\n\n"
                + idea("El modelo es un árbol de preguntas sí/no; al crearlo todavía no sabe nada.") + "\n\n"
                + escribelo("importa `DecisionTreeClassifier` y crea el modelo con `max_depth=3` y `random_state=0` en una variable llamada `modelo`.")))
    c.append(codigo(ARRANQUE_C1))
    c.append(md("### 💡 Entrenar con `fit()`\n\n"
                "Entrenar es mostrarle al modelo los días anteriores **con sus etiquetas**, para que descubra qué preguntas separan los días atrasados de los puntuales.\n\n"
                + idea("`modelo.fit(entradas, etiquetas)` es entrenar: el árbol busca las preguntas que mejor separan los días atrasados de los puntuales.") + "\n\n"
                + escribelo("entrena el modelo con las entradas y las etiquetas.")))
    c.append(codigo(ARRANQUE_C2))
    c.append(md("### 💡 Predecir con `predict()`\n\n"
                "Ahora el modelo ya aprendió. Predecir es preguntarle por un día que **no** estaba en los datos. "
                "Como `predict()` trabaja con una lista de días, un solo día va dentro de otra lista.\n\n"
                + idea("`modelo.predict([[...]])` es predecir: recibe una lista con los datos de un día nuevo y devuelve 1 (atrasada) o 0 (puntual).") + "\n\n"
                + escribelo("pregunta al modelo por el día nuevo (0 mm de lluvia, 2 km de taco y 12 pasajeros) y muestra el resultado con una etiqueta clara.")))
    c.append(codigo(ARRANQUE_C3))
    c.append(md("#### 🗣️ ¿Quién acierta más? Humano vs. voz vs. modelo\n\n"
                "Un día nuevo: **7 mm de lluvia, 4 km de taco y 15 pasajeros**. Antes de preguntarle al modelo:\n\n"
                "1. Cada uno decide **a ojo**: ¿atrasada o puntual?\n"
                "2. Escuchamos qué predice la voz.\n"
                "3. Recién entonces le preguntamos al modelo y comparamos los tres resultados.\n\n"
                + escribelo("pregunta al modelo por `dia_a_comparar` y muestra el resultado con una etiqueta clara.")
                + "\n\n✍️ *Mi predicción a ojo:* ..."))
    c.append(codigo(ARRANQUE_COMPARAR))
    c.append(md("### 💡 Leer el árbol\n\n"
                "El modelo no es una caja cerrada: podemos mirar las preguntas que encontró, igual que en el diagrama del comienzo. "
                "Eso nos permite **revisar si tiene sentido**.\n\n"
                + idea("`export_text` muestra las preguntas que el árbol encontró: es el **patrón** que descubrió solo.") + "\n\n"
                + escribelo("importa `export_text` y muestra el árbol, indicando los nombres de las variables.")))
    c.append(codigo(ARRANQUE_C4))
    c.append(md("#### 🕵️ Explicar un error\n\n"
                "Un día nuevo tiene **5 mm de lluvia, 1 km de taco y 40 pasajeros**, y el árbol predice **puntual**. "
                "Escuchamos cómo la voz explica por qué, y **juzgamos entre todos si su explicación cuadra con las preguntas del árbol** que acabamos de leer.\n\n"
                "✍️ *¿La explicación cuadra con el árbol? ¿Por qué sí o por qué no?* ..."))
    c.append(md("#### ✅ Verificamos lo aprendido\n\n"
                "La voz le pregunta a dos personas del curso:\n\n"
                "- ¿Qué diferencia hay entre `fit()` y `predict()`?\n"
                "- ¿Por qué el árbol ignoró los pasajeros?"))
    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Ejemplo |\n|---|---|\n"
                "| Crear el modelo | `modelo = DecisionTreeClassifier(max_depth=3, random_state=0)` |\n"
                "| Entrenar | `modelo.fit(entradas, etiquetas)` |\n"
                "| Predecir un día nuevo | `modelo.predict([dia_nuevo])` |\n"
                "| Leer el árbol | `export_text(modelo, feature_names=nombres_variables)` |"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| Pasar un solo día suelto: `modelo.predict([0, 2, 12])` | `ValueError`: `predict()` espera una lista de días | Poner el día dentro de otra lista: `modelo.predict([[0, 2, 12]])` |\n"
                "| Llamar a `predict()` antes de `fit()` | `NotFittedError`: el modelo todavía no sabe nada | Entrenar primero con `modelo.fit(entradas, etiquetas)` |\n"
                "| Invertir el orden: `modelo.fit(etiquetas, entradas)` | `ValueError` o un árbol sin sentido | Primero van las entradas y después las etiquetas |\n"
                "| Creer que el modelo «sabe» algo que no está en sus datos | Se acepta una predicción sin revisarla | Leer el árbol con `export_text` y preguntarse qué días vio realmente |"))
    return c


def ejercicio(num: str, titulo: str, narrativa: str, debe: list, pistas: list, esp: str, datos: str,
              check: str = "", extra_md: str = "") -> list:
    rotulo = titulo if num == "guiada" else f"Ejercicio {num} — {titulo}"
    cuerpo = f"### 🎯 {rotulo}\n\n{narrativa}\n\n**El programa debe:**\n\n" \
             + "\n".join(f"- {b}" for b in debe) + "\n\n" + "\n\n".join(pistas) + "\n\n" + esp
    c = [md(cuerpo)]
    marca = "# Tu programa" if num == "guiada" else f"# Tu solución del Ejercicio {num}"
    c.append(codigo(f"{marca}\n{datos}\n\n{CENTINELA}\n"))
    if extra_md:
        c.append(md(extra_md))
    if check:
        c.append(codigo(check))
    return c


def guiada() -> list:
    sal = ejecutar(SOL_G)
    c = [md("---\n\n## 3️⃣ Práctica Guiada")]
    c += ejercicio(
        "guiada", "¿Se atrasará la micro de vuelta?",
        "La junta de vecinos de La Islita ahora quiere saber lo mismo, pero para la micro de las 18:30 que vuelve desde Santiago. "
        "Anotó 8 días con la lluvia, los kilómetros de taco en la Autopista del Sol y los minutos que la micro esperó en el terminal antes de salir. "
        "Antes de confiar en el sistema, quieren que ustedes revisen si cada respuesta tiene sentido con lo que se vio en los datos.",
        ["**Entrenar** un árbol de decisión con los 8 días (profundidad máxima 3, semilla 0).",
         "**Predecir** los 3 días nuevos de una sola vez.",
         "**Mostrar** las predicciones con una etiqueta clara (0 = puntual, 1 = atrasada).",
         "**Escribir**, en un comentario, una frase por día: ¿esa predicción cuadra con lo que se ve en los datos?"],
        [pista(1, "varios días a la vez", "`predict()` acepta varios días si se los entregas como una lista de listas; justo así viene `dias_nuevos`."),
         pista(2, "para la frase", "Mira en tus datos qué días se parecen al día nuevo y qué etiqueta tenían. Puedes leer el árbol con `export_text`.")],
        esperado(sal), G_DATOS)
    return c


def independiente() -> list:
    c = [md("---\n\n## 4️⃣ Práctica Independiente\n\n"
            "Resuelve los siguientes ejercicios. Cada uno trae sus propios datos escritos y pistas. "
            "Después de cada uno hay un autochequeo que dice ✅ si tu modelo quedó bien entrenado; "
            "**busca tu árbol en la variable `modelo`**, así que usa ese nombre."),
         codigo(CELDA_AUTOCHEQUEOS)]
    c.append(md("### 🎯 Ejercicio 0a — Práctica directa: crear, entrenar y predecir\n\n"
                "Aplica el patrón base de un árbol de decisión:\n\n"
                "**El programa debe:**\n\n"
                "- Importar `DecisionTreeClassifier` y crear un árbol con `max_depth=2` y `random_state=0`.\n"
                "- Entrenarlo con las entradas y las etiquetas.\n"
                "- Predecir el caso nuevo, guardar la predicción en una variable e imprimirla con una etiqueta.\n\n"
                + esperado(ejecutar(SOL_E0))))
    c.append(codigo(f"# Tu solución del Ejercicio 0a\n{E0_DATOS}\n\n{CENTINELA}\n"))

    c += ejercicio(
        "1", "Naltagua: ¿conviene el colectivo?",
        "Los vecinos de Naltagua se preguntan si les conviene tomar el colectivo en vez de esperar la micro. "
        "Anotaron 10 días con la lluvia, los kilómetros de taco y los minutos que esperaron en el paradero. "
        "Marcaron 1 si ese día convino el colectivo y 0 si la micro sirvió bien. Quieren saber qué conviene en dos días nuevos.",
        ["**Entrenar** un árbol con los 10 días (profundidad máxima 2, semilla 0).",
         "**Predecir** los 2 días nuevos de una sola vez.",
         "**Mostrar** las predicciones con una etiqueta clara (0 = micro, 1 = colectivo)."],
        [pista(1, "dos días a la vez", "Los días nuevos son una lista que contiene dos listas: así se entregan al modelo."),
         pista(2, "el orden importa", "El modelo primero tiene que aprender de los días anteriores y recién después puede predecir.")],
        esperado(ejecutar(SOL_E1)), E1_DATOS, check="check_ej1()")

    c += ejercicio(
        "2", "Liceo Mario Bertero: ¿llegará el furgón antes del timbre?",
        "Una apoderada del Liceo Mario Bertero anotó 10 mañanas del furgón de las 7:30: los minutos que se atrasó en salir, "
        "los milímetros de lluvia y cuántos estudiantes subieron. Marcó 1 si el furgón llegó después del timbre de las 8:00 y 0 si llegó a tiempo. "
        "Quiere saber qué pasará en dos mañanas nuevas.",
        ["**Entrenar** un árbol con las 10 mañanas (profundidad máxima 2, semilla 0).",
         "**Predecir** las 2 mañanas nuevas.",
         "**Mostrar** las predicciones con una etiqueta clara (0 = a tiempo, 1 = después del timbre)."],
        [pista(1, "cuántos datos por día", "Cada día tiene tres datos, siempre en el mismo orden que en los datos de entrenamiento."),
         pista(2, "si algo se cae", "Si `predict()` da error, revisa si le entregaste una lista de días o un solo día suelto.")],
        esperado(ejecutar(SOL_E2)), E2_DATOS, check="check_ej2()")

    lineas = ejecutar(SOL_E3).splitlines()
    c += ejercicio(
        "3", "Casona del Maipo: ¿llega a tiempo a montar su puesto?",
        "Doña Marta vende verduras en la feria de la Casona del Maipo y tiene que montar su puesto antes de las 8:00. "
        "Anotó 14 días: la lluvia, los minutos pasados de las 6:00 a los que salió de su casa y las cajas que cargó. "
        "Marcó 1 si llegó tarde al montaje. Quiere predecir tres días nuevos y saber qué pasa si cambia un dato del primero de ellos.",
        ["**Entrenar** un árbol con los 14 días (profundidad máxima 3, semilla 0).",
         "**Predecir** los 3 días nuevos y mostrar las predicciones (0 = a tiempo, 1 = tarde).",
         "**Cambiar un solo dato** del primer día nuevo, volver a predecir y mostrar el resultado.",
         "**Explicar por escrito**, en la celda de abajo, qué cambió y por qué."],
        [pista(1, "cambiar un dato", "Crea una copia del primer día con un solo número distinto y pregúntale al modelo por ella."),
         pista(2, "elegir qué cambiar", "No todos los datos pesan igual en el árbol: míralo con `export_text` antes de decidir cuál cambiar.")],
        esperado("\n".join(lineas[:2]), "*(La segunda línea es un ejemplo, con 46 cajas en vez de 30: tu dato cambiado puede ser otro.)*"),
        E3_DATOS, check="check_ej3()",
        extra_md="✍️ **Mi explicación:** *¿Qué dato cambié? ¿Cambió la predicción? ¿Por qué creo que pasó eso, según el árbol?* ...")

    c += [md("### 🎯 Ejercicio 4 — Desafío: ¿árbol corto o árbol largo?\n\n"
             "Con los datos de doña Marta, entrena **dos** árboles: uno con profundidad máxima 1 y otro con profundidad máxima 3. "
             "Muestra los dos como preguntas de sí/no y compara.\n\n"
             "**El programa debe:**\n\n"
             "- **Entrenar** los dos árboles con los mismos 14 días.\n"
             "- **Mostrar** las preguntas de cada árbol, con los nombres de las variables.\n"
             "- **Escribir**, en la celda de abajo, cuál de los dos es más fácil de revisar y cuál se equivoca más con los datos de entrenamiento.\n\n"
             + pista(1, "mostrar las preguntas", "Ya mostraste las preguntas de un árbol en la clase: repite ese paso para cada modelo.")
             + "\n\n📤 <em>El programa imprime:</em> las preguntas de los dos árboles, uno debajo del otro."),
          codigo(f"# Tu solución del Ejercicio 4\n{E3_DATOS}\n\n{CENTINELA}\n"),
          md("✍️ **Mi comparación:** ...")]
    return c


def ticket() -> list:
    c = [md("---\n\n## 🎫 Ticket de Salida\n\n"
            "Cuatro preguntas para que revises tu propia comprensión: **no tiene nota ni se entrega**. "
            "Lee cada una, decide en silencio y escribe una letra por pregunta (`A`, `B`, `C` o `D`) en la celda de abajo. "
            "Luego ejecútala: el autochequeo te dice qué va bien y qué conviene revisar 🙌")]
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        letras = "ABCD"
        alts = "\n".join(f"- **{letras[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}"))
    c.append(codigo("# Escribe una letra (A, B, C o D) por pregunta y ejecuta la celda\n"
                    "respuestas = [\"\", \"\", \"\", \"\"]\ncheck_ticket(respuestas)"))
    return c


def cierre() -> list:
    return [md("---\n\n## 🎯 Cierre\n\n"
               "**Objetivo de la clase**\n\n"
               "Entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico.\n\n"
               "---\n\n**Reflexiona antes de irte** (las comentamos a viva voz):\n\n"
               "1. ¿Qué tan seguro/a te sientes entrenando un árbol de decisión y usándolo para predecir, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. ¿Qué parte de las predicciones de hoy revisamos con los datos y cuál habríamos aceptado sin revisar?\n\n"
               "3. ¿En qué se nos notó hoy el pensamiento crítico?\n\n"
               "👀 **Lo que viene:** el jueves construimos una **neurona** para ver cómo decide."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. \n\n3. "),
            md("---")]


def clase() -> list:
    return celdas_comunes_clase() + icn_clase() + guiada() + independiente() + ticket() + cierre()


# ───────────────────────── solucionario ─────────────────────────


def bloque_sol(titulo: str, cod: str, nota: str = "") -> list:
    """Solución: celda de código ejecutable + salida real incrustada como texto."""
    salida = ejecutar(cod)
    out = "\n\n**Salida:**\n\n```text\n" + salida + "\n```"
    c = [md(f"### {titulo}{out}" + (f"\n\n{nota}" if nota else "")), codigo(cod)]
    return c


def solucionario() -> list:
    c = [md("# Clase 42 — Primer clasificador · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Todas las celdas de este cuaderno se ejecutan de arriba hacia abajo (scikit-learn, sin archivos)."),
         md("## ⚙️ Celda preparada de autochequeos\n\nLa misma que ven los estudiantes; los `check_*()` de abajo se ejecutan con las soluciones para comprobar que dan ✅."),
         codigo(CELDA_AUTOCHEQUEOS)]

    c.append(md("## 🧠 Haz Ahora\n\nSin código ni respuesta única: la voz hace de dirigente de la junta de vecinos y el curso piensa en voz alta. "
                "Ideas esperables: lluvia, taco en la Ruta 78, cantidad de pasajeros, hora de salida, día de la semana, accidentes. "
                "Medibles con un número: milímetros de lluvia, kilómetros de taco, cantidad de pasajeros, minutos de espera. "
                "Dato a anotar cada día: si la micro llegó atrasada o puntual (la etiqueta). Cantidad de días: no hay cifra exacta, pero debería aparecer la idea de «muchos y variados»."))

    c.append(md("## 📘 ICN — código completo (cada ejemplo es autocontenido)"))
    for nombre, cod, nota in [
        ("Concepto 1 · Crear el modelo", SOL_ICN1, "El `print` muestra el modelo recién creado: aún no tiene nada aprendido."),
        ("Concepto 2 · `fit()` = entrenar", SOL_ICN2, ""),
        ("Concepto 3 · `predict()` = predecir", SOL_ICN3,
         "Observación: `predict` devuelve una lista (`[0]`) aunque se le pregunte por un solo día."),
        ("Concepto 4 · Leer el árbol", SOL_ICN4,
         "Hallazgos para el pensamiento crítico: el árbol ignora `pasajeros`, y el umbral de 8 mm cae en un hueco "
         "(no hay días con 6–8 mm y poco taco)."),
    ]:
        c += bloque_sol(nombre, cod, nota)

    c.append(md("### 🗣️ Momentos con la voz — casos y predicciones verificadas\n\n"
                "| Caso `[lluvia_mm, km_taco, pasajeros]` | Predicción del árbol |\n|---|---|\n"
                "| `[0, 2, 12]` | puntual (0) |\n| `[16, 6, 20]` | atrasada (1) |\n| `[7, 4, 15]` | puntual (0) |\n"
                "| `[1, 8, 22]` | atrasada (1) |\n| `[5, 1, 40]` | puntual (0) — ignora los 40 pasajeros |\n\n"
                "**Explicar un error:** la voz debe apoyarse en la pregunta `km_taco <= 4.00` y `lluvia_mm <= 8.00`; si dice que «los pasajeros no importan» "
                "o que «con 40 pasajeros igual es puntual», el curso debe notar que el árbol simplemente no usó esa variable."))
    c.append(codigo(ENTRADAS + "\n\nfrom sklearn.tree import DecisionTreeClassifier\n\n"
                    "modelo = DecisionTreeClassifier(max_depth=3, random_state=0)\nmodelo.fit(entradas, etiquetas)\n\n"
                    "for dia in [[0, 2, 12], [16, 6, 20], [7, 4, 15], [1, 8, 22], [5, 1, 40]]:\n"
                    "    print(\"Día\", dia, \"→\", modelo.predict([dia]))"))

    c.append(md("## 🧩 Práctica guiada — solución\n\n" + "Salida: ver abajo."))
    c += bloque_sol("Guiada · La micro de las 18:30", SOL_G,
                    "El árbol resultante usa solo `minutos_espera` (profundidad 1). El día 3 (9 km de taco) se predice puntual porque el árbol no usó el taco: "
                    "es un buen momento para pedir la frase de pensamiento crítico.")

    c.append(md("## 🚀 Práctica independiente — soluciones"))
    c += bloque_sol("Ejercicio 0a", SOL_E0)
    c += bloque_sol("Ejercicio 1 · Naltagua", SOL_E1)
    c.append(codigo("check_ej1()"))
    c += bloque_sol("Ejercicio 2 · Furgón del liceo", SOL_E2)
    c.append(codigo("check_ej2()"))
    c += bloque_sol("Ejercicio 3 · Feria / Casona del Maipo", SOL_E3,
                    "Explicación modelo: el árbol solo usa `minutos_salida` y `cajas`; la lluvia no aparece. "
                    "Subir las cajas del primer día de 30 a 46 cambia la predicción de 0 a 1 (con más de 42,5 cajas se llega tarde); subir la lluvia no cambia nada, "
                    "porque el árbol no la usó. **Criterio:** el estudiante identifica qué dato cambió, si cambió la predicción y lo relaciona con una pregunta del árbol.")
    c.append(codigo("check_ej3()"))
    c += bloque_sol("Ejercicio 4 · Desafío", SOL_E4,
                    "El árbol corto (profundidad 1) usa solo `minutos_salida` y se equivoca con 3 de los 14 días de entrenamiento: los que salieron temprano pero cargaron muchas cajas "
                    "([12, 20, 45], [15, 10, 50] y [14, 5, 55]). El de profundidad 3 acierta con los 14, pero tiene una pregunta más que revisar. "
                    "Respuestas razonables: el corto es más fácil de revisar; el largo se ajusta mejor a los datos.")

    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                "Respuestas correctas: **C, A, D, B**. El Colab de estudiantes guarda las letras como huellas (no como texto) y la justificación codificada."))
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        letras = "ABCD"
        alts = "\n".join(f"- **{letras[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}\n\n**Respuesta correcta: {TICKET_CORRECTAS[i - 1]}.** {TICKET_JUSTIFICACION[i - 1]}"))
    c.append(codigo("respuestas = " + json.dumps(TICKET_CORRECTAS) + "\ncheck_ticket(respuestas)"))
    return c


if __name__ == "__main__":
    guardar(SALIDA_CLASE, clase())
    guardar(SALIDA_SOL, solucionario())
    print("Listo:", SALIDA_CLASE.name, "·", SALIDA_SOL.name)
