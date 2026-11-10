"""Genera 'Clase 43 - Neurona v2 - Clase.ipynb' (estudiantes), '... - Solucionario.ipynb' (profesor) y el JSON del ticket.

Fuente de verdad: este script + la Spec v2 aprobada + clase-42b-tabla-a-listas/datos_wifi_verificados.json.
No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.   Ejecutar: py -3 -X utf8 generar_clase_v2.py
Los resultados esperados se calculan ejecutando las soluciones (así nunca se desfasan del código).
"""
import base64
import contextlib
import hashlib  # noqa: F401  (reservado)
import html
import io
import json
import textwrap
import uuid
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
NOMBRE = "Clase 43 - Neurona v2"
SALIDA_CLASE = AQUI / f"{NOMBRE} - Clase.ipynb"
SALIDA_SOL = AQUI / f"{NOMBRE} - Solucionario.ipynb"
SALIDA_JSON = AQUI / f"{NOMBRE} - Ticket de Salida Respuestas.json"
URL_FORM = "https://forms.gle/sjRpbgmQzrpkEBsH9"
TEMA_FORM = "La neurona aprende sola"
URL_SLIDES = "https://clases-ia-mario-bertero.vercel.app/clase-43-v2/"

# ───────────────────────── utilidades de celdas ─────────────────────────


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {},
            "source": texto.strip("\n").splitlines(keepends=True)}


def codigo(texto: str) -> dict:
    return {"cell_type": "code", "id": uuid.uuid4().hex[:8], "metadata": {}, "execution_count": None,
            "outputs": [], "source": texto.strip("\n").splitlines(keepends=True)}


def ejecutar(texto: str) -> str:
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


def guardar(ruta: Path, celdas: list) -> None:
    nb = {"cells": celdas,
          "metadata": {"colab": {"provenance": []}, "kernelspec": {"display_name": "Python 3", "name": "python3"},
                       "language_info": {"name": "python"}},
          "nbformat": 4, "nbformat_minor": 5}
    ruta.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


# ───────────────────────── datos (los mismos de la 42b) ─────────────────────────

WIFI = json.loads((AQUI.parent / "clase-42b-tabla-a-listas" / "datos_wifi_verificados.json").read_text(encoding="utf-8"))
COLS, TABLA, ETIQ = WIFI["cols"], WIFI["X"], WIFI["y"]
TRIO = [0, 1, 2]       # dispositivos, video, horas desde el reinicio
OTRO = [3, 4, 5]       # temperatura, hora del bloque, día del mes (trío «flojo», solo para el extra)
CENTINELA = "# ── Escribe tu programa desde aquí ──"


def cols_de(filas, cols):
    return [[f[c] for c in cols] for f in filas]


def lista(filas, sangria=4):
    return "[" + (",\n" + " " * sangria).join(str(f) for f in filas) + "]"


X3 = cols_de(TABLA, TRIO)
TR_X, TR_Y, TE_X, TE_Y = X3[:16], ETIQ[:16], X3[16:], ETIQ[16:]
XO = cols_de(TABLA, OTRO)
OTR_X, OTE_X = XO[:16], XO[16:]
FILA_NUEVA = [88, 17, 4]

IMPORTS = ("from sklearn.tree import DecisionTreeClassifier\n"
           "from sklearn.neural_network import MLPClassifier\n"
           "from sklearn.metrics import accuracy_score")

DATOS = (f"entradas_train = {lista(TR_X)}\n\n"
         f"etiquetas_train = {TR_Y}\n\n"
         f"entradas_test = {lista(TE_X)}\n\n"
         f"etiquetas_test = {TE_Y}")
DATOS_OTRO = (f"entradas_train_otro = {lista(OTR_X)}\n\n"
              f"entradas_test_otro = {lista(OTE_X)}")

NEURONA = "MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=0)"

# ───────────────────────── soluciones (se ejecutan para calcular los resultados esperados) ─────────────────────────

SOL_C3 = (IMPORTS + "\n\n" + DATOS + "\n\n"
          f"modelo = {NEURONA}\n"
          "modelo.fit(entradas_train, etiquetas_train)\n"
          "predicciones = modelo.predict(entradas_test)\n"
          "exactitud = accuracy_score(etiquetas_test, predicciones)\n"
          "print(\"Predicciones de la neurona:\", predicciones)\n"
          "print(\"Accuracy de la neurona:\", exactitud)")

SOL_C4A = (SOL_C3 + "\n\n"
           "print(\"Pesos (dispositivos, video, horas):\", modelo.coefs_)\n"
           "print(\"Sesgo:\", modelo.intercepts_)")

DEMO_SEMILLA = ("semilla = {S}   # cambia este número (0, 1, 2…) y ejecuta de nuevo\n"
                "modelo_semilla = MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=semilla)\n"
                "modelo_semilla.fit(entradas_train, etiquetas_train)\n"
                "print(\"Semilla:\", semilla)\n"
                "print(\"Pesos:\", modelo_semilla.coefs_)\n"
                "print(\"Accuracy en train:\", accuracy_score(etiquetas_train, modelo_semilla.predict(entradas_train)))\n"
                "print(\"Accuracy en test:\", accuracy_score(etiquetas_test, modelo_semilla.predict(entradas_test)))")
SOL_C4B = [IMPORTS + "\n\n" + DATOS + "\n\n" + DEMO_SEMILLA.replace("{S}", str(s)) for s in (0, 1)]

SOL_C5 = (SOL_C3 + "\n\n"
          "# El árbol de ayer, con los mismos datos\n"
          "arbol = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
          "arbol.fit(entradas_train, etiquetas_train)\n"
          "predicciones_arbol = arbol.predict(entradas_test)\n\n"
          "# 1. Leer el resultado\n"
          "print(\"Etiquetas reales:          \", etiquetas_test)\n"
          "print(\"Predicciones de la neurona:\", predicciones)\n\n"
          "# 2. Comparar la precisión\n"
          "exactitud_arbol = accuracy_score(etiquetas_test, predicciones_arbol)\n"
          "print(\"Accuracy del árbol:  \", exactitud_arbol)\n"
          "print(\"Accuracy de la neurona:\", exactitud)")

SOL_G = (IMPORTS + "\n\n" + DATOS + "\n\n"
         "modelo_arbol = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
         f"modelo_neurona = {NEURONA}\n\n"
         "modelo_arbol.fit(entradas_train, etiquetas_train)\n"
         "modelo_neurona.fit(entradas_train, etiquetas_train)\n\n"
         "predicciones_arbol = modelo_arbol.predict(entradas_test)\n"
         "predicciones_neurona = modelo_neurona.predict(entradas_test)\n\n"
         "exactitud_arbol = accuracy_score(etiquetas_test, predicciones_arbol)\n"
         "exactitud_neurona = accuracy_score(etiquetas_test, predicciones_neurona)\n\n"
         "print(\"Accuracy del árbol:\", exactitud_arbol)\n"
         "print(\"Accuracy de la neurona:\", exactitud_neurona)\n\n"
         "# Usaríamos el árbol: acertó 4 de 4 y la neurona 3 de 4 con los mismos datos.\n"
         "# Pero con solo 4 filas de prueba cada fila vale 25 %, así que esa diferencia prueba poco:\n"
         "# conviene probar con más filas antes de confiar.")

E0A_BASE = (IMPORTS + "\n\n" + DATOS + "\n\n"
            f"modelo = {NEURONA}\nmodelo.fit(entradas_train, etiquetas_train)")
E0A_SOL = E0A_BASE + (f"\n\nprediccion = modelo.predict([{FILA_NUEVA}])\n"
                      "print(\"Predicción para la fila nueva (1 = se cae, 0 = aguanta):\", prediccion)")

E1_SOL = (IMPORTS + "\n\n" + DATOS_OTRO + "\n\n"
          f"etiquetas_train = {TR_Y}\netiquetas_test = {TE_Y}\n\n"
          "arbol = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
          f"neurona = {NEURONA}\n"
          "arbol.fit(entradas_train_otro, etiquetas_train)\n"
          "neurona.fit(entradas_train_otro, etiquetas_train)\n"
          "exactitud_arbol_otro = accuracy_score(etiquetas_test, arbol.predict(entradas_test_otro))\n"
          "exactitud_neurona_otro = accuracy_score(etiquetas_test, neurona.predict(entradas_test_otro))\n"
          "print(\"Accuracy del árbol con las otras columnas:\", exactitud_arbol_otro)\n"
          "print(\"Accuracy de la neurona con las otras columnas:\", exactitud_neurona_otro)")

E2_SOL = (IMPORTS + "\n\n" + DATOS + "\n\n"
          "exactitudes_train = []\nexactitudes_test = []\n"
          "for semilla in [0, 1, 2, 3, 4]:\n"
          "    modelo = MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=semilla)\n"
          "    modelo.fit(entradas_train, etiquetas_train)\n"
          "    exactitudes_train.append(accuracy_score(etiquetas_train, modelo.predict(entradas_train)))\n"
          "    exactitudes_test.append(accuracy_score(etiquetas_test, modelo.predict(entradas_test)))\n"
          "print(\"Accuracy en train por semilla:\", exactitudes_train)\n"
          "print(\"Accuracy en test por semilla: \", exactitudes_test)")


def valores(codigo_sol: str) -> dict:
    g: dict = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(codigo_sol, g)
    return g


_g5 = valores(SOL_C5)
_ge1 = valores(E1_SOL)
_ge2 = valores(E2_SOL)
EXACT_NEURONA, EXACT_ARBOL = float(_g5["exactitud"]), float(_g5["exactitud_arbol"])
PRED_NEURONA = [int(p) for p in _g5["predicciones"]]
assert (EXACT_ARBOL, EXACT_NEURONA, PRED_NEURONA) == (1.0, 0.75, [0, 0, 1, 0]), (EXACT_ARBOL, EXACT_NEURONA, PRED_NEURONA)
E1_ARBOL, E1_NEURONA = float(_ge1["exactitud_arbol_otro"]), float(_ge1["exactitud_neurona_otro"])
E2_TRAIN, E2_TEST = [float(v) for v in _ge2["exactitudes_train"]], [float(v) for v in _ge2["exactitudes_test"]]
E0A_PRED = [int(p) for p in valores(E0A_SOL)["prediccion"]]

# ───────────────────────── verificador (celda preparada) ─────────────────────────

CELDA_VERIFICADOR = '''
#@title 🔧 Verificador automático — ejecútala después de la celda de los import (no la edites)
_ETQ_TRAIN = __ETQ_TRAIN__
_ETQ_TEST = __ETQ_TEST__
_PRED = __PRED__
_ACC_NEURONA = __ACC_N__
_ACC_ARBOL = __ACC_A__
_E0A = __E0A__
_E1 = __E1__
_E2 = __E2__


def _es_neurona(m):
    return isinstance(m, MLPClassifier) and tuple(m.hidden_layer_sizes) == () and m.max_iter == 2000 and m.random_state == 0


def _es_arbol(m):
    return isinstance(m, DecisionTreeClassifier) and m.max_depth == 3 and m.random_state == 0


def _igual(a, b):
    return a is not None and abs(float(a) - b) < 1e-9


def _datos_ok():
    g = globals()
    for n in ("entradas_train", "etiquetas_train", "entradas_test", "etiquetas_test"):
        if g.get(n) is None:
            print("⏳ Falta ejecutar la celda de los datos (las 4 listas).")
            return False
    return True


def check_icn():
    g = globals()
    if not _datos_ok():
        return
    m = g.get("modelo")
    if m is None:
        print("⏳ Falta crear la neurona y guardarla en una variable llamada modelo.")
        return
    if not isinstance(m, MLPClassifier):
        print("⚠️ modelo no es una neurona (MLPClassifier).")
        print("   Pista: la línea que crea el modelo es lo único que cambia respecto del árbol.")
        return
    if not _es_neurona(m):
        print("⚠️ Tu neurona no tiene los argumentos pedidos.")
        print("   Pista: hidden_layer_sizes=() (una sola neurona), max_iter=2000 y random_state=0.")
        return
    if not hasattr(m, "coefs_"):
        print("⏳ La neurona todavía no aprendió. Falta modelo.fit(entradas_train, etiquetas_train).")
        return
    p = g.get("predicciones")
    if p is None:
        print("⏳ Falta guardar en predicciones lo que predice la neurona para entradas_test.")
        return
    if [int(v) for v in p] != _PRED:
        print("⚠️ Tus predicciones no son las esperadas.")
        print("   Pista: entrena con train y predice con entradas_test, no con entradas_train.")
        return
    print("✅ La neurona aprendió y sus predicciones son las esperadas.")
    ex = g.get("exactitud")
    if ex is None:
        print("⏳ Falta calcular el accuracy de la neurona y guardarlo en una variable llamada exactitud.")
    elif _igual(ex, _ACC_NEURONA):
        print("✅ Tu accuracy de la neurona es el esperado.")
    else:
        print("⚠️ Tu accuracy de la neurona no coincide con el esperado.")
        print("   Pista: accuracy_score(etiquetas_test, predicciones): primero las reales, después las predichas.")


def check_comparar():
    g = globals()
    check_icn()
    ea = g.get("exactitud_arbol")
    if ea is None:
        print("⏳ Falta calcular el accuracy del árbol y guardarlo en exactitud_arbol.")
    elif _igual(ea, _ACC_ARBOL):
        print("✅ Tu accuracy del árbol es el esperado.")
        print("   Y ahora: ¿cuál de los dos usarían, y por qué?")
    else:
        print("⚠️ Tu accuracy del árbol no coincide con el esperado.")
        print("   Pista: usa predicciones_arbol (las del árbol) con etiquetas_test.")


def check_guiada():
    g = globals()
    if not _datos_ok():
        return
    ma, mn = g.get("modelo_arbol"), g.get("modelo_neurona")
    if ma is None or mn is None:
        print("⏳ Faltan los dos modelos: modelo_arbol y modelo_neurona.")
        return
    if not _es_arbol(ma):
        print("⚠️ modelo_arbol debe ser un árbol de profundidad máxima 3 y semilla 0.")
        return
    if not _es_neurona(mn):
        print("⚠️ modelo_neurona debe ser la neurona pedida (hidden_layer_sizes=(), max_iter=2000, random_state=0).")
        return
    if not hasattr(ma, "tree_") or not hasattr(mn, "coefs_"):
        print("⏳ Falta entrenar los dos modelos con fit(entradas_train, etiquetas_train).")
        return
    ea, en = g.get("exactitud_arbol"), g.get("exactitud_neurona")
    if ea is None or en is None:
        print("⏳ Faltan los accuracy: guárdalos en exactitud_arbol y exactitud_neurona.")
        return
    if not _igual(ea, _ACC_ARBOL):
        print("⚠️ El accuracy del árbol no es el esperado.")
        print("   Pista: predice con entradas_test y compara con etiquetas_test.")
    elif not _igual(en, _ACC_NEURONA):
        print("⚠️ El accuracy de la neurona no es el esperado.")
        print("   Pista: misma receta que el árbol; solo cambia la línea que crea el modelo.")
    else:
        print("✅ Tus dos modelos y sus accuracy son los esperados.")
        print("   Falta tu decisión escrita en un comentario: ¿cuál usarías y por qué? ¿Alcanzan 4 filas de prueba?")


def check_ej0a():
    p, m = globals().get("prediccion"), globals().get("modelo")
    if p is None or m is None:
        print("⏳ Falta guardar la predicción en una variable llamada prediccion.")
    elif [int(v) for v in p] != _E0A:
        print("⚠️ Tu predicción no corresponde a la fila nueva (88, 17, 4).")
        print("   Pista: una sola fila nueva va dentro de otra lista: [[...]].")
    else:
        print("✅ Predijiste la fila nueva con la forma correcta.")


def check_ej1():
    g = globals()
    ea, en = g.get("exactitud_arbol_otro"), g.get("exactitud_neurona_otro")
    if ea is None or en is None:
        print("⏳ Faltan exactitud_arbol_otro y exactitud_neurona_otro.")
    elif not _igual(ea, _E1[0]):
        print("⚠️ El accuracy del árbol con las otras columnas no es el esperado.")
        print("   Pista: entrena con entradas_train_otro y predice con entradas_test_otro.")
    elif not _igual(en, _E1[1]):
        print("⚠️ El accuracy de la neurona con las otras columnas no es el esperado.")
        print("   Pista: misma receta, solo cambia la línea que crea el modelo.")
    else:
        print("✅ Tus dos accuracy son los esperados. Compáralos con los de las columnas de la clase.")


def check_ej2():
    g = globals()
    tr, te = g.get("exactitudes_train"), g.get("exactitudes_test")
    if not tr or not te:
        print("⏳ Faltan las listas exactitudes_train y exactitudes_test.")
    elif len(tr) != 5 or len(te) != 5:
        print("⚠️ Cada lista debe tener 5 valores, uno por semilla (0, 1, 2, 3 y 4).")
    elif any(abs(float(a) - b) > 1e-9 for a, b in zip(tr, _E2[0])) or any(abs(float(a) - b) > 1e-9 for a, b in zip(te, _E2[1])):
        print("⚠️ Alguno de tus valores no coincide con el esperado.")
        print("   Pista: en cada vuelta crea la neurona con random_state=semilla, entrénala con train y mide train y test.")
    else:
        print("✅ Tus resultados son los esperados. ¿Cambian con la semilla? ¿Qué dice eso de confiar en una sola?")


print("Verificador listo ✅")
'''
CELDA_VERIFICADOR = (CELDA_VERIFICADOR
                     .replace("__ETQ_TRAIN__", json.dumps(TR_Y)).replace("__ETQ_TEST__", json.dumps(TE_Y))
                     .replace("__PRED__", json.dumps(PRED_NEURONA)).replace("__ACC_N__", repr(EXACT_NEURONA))
                     .replace("__ACC_A__", repr(EXACT_ARBOL)).replace("__E0A__", json.dumps(E0A_PRED))
                     .replace("__E1__", json.dumps([E1_ARBOL, E1_NEURONA]))
                     .replace("__E2__", json.dumps([E2_TRAIN, E2_TEST])))

# ───────────────────────── contenido compartido ─────────────────────────

OBJETIVO = "Crear, entrenar y evaluar una neurona con la misma receta del árbol y comparar ambos resultados con sorpresa."

HAZ_AHORA = [
    "Para saber si el wifi se cae, no todas las columnas pesan igual. Si tuvieran que ponerle una **importancia de 0 a 10** a cada una de estas 3 columnas, ¿qué nota le pondrían a cada una y por qué?",
    "Ayer el árbol acertó los 4 días de prueba: ¿qué porcentaje de aciertos es eso?",
    "Con 4 filas de prueba, ¿cuántos puntos porcentuales vale cada fila?",
    "Si un modelo tuviera una precisión de 0,75 con esas 4 filas, ¿cuántas filas acertó?",
]

_NEURONA_CAJA = (
    "```text\n"
    "dispositivos_conectados   × peso 1 ──┐\n"
    "estudiantes_viendo_video  × peso 2 ──┼──► suma ──► ¿pasa el umbral? ──► 1 (se cae) / 0 (aguanta)\n"
    "horas_desde_reinicio      × peso 3 ──┘\n"
    "```")

TICKET_PREGUNTAS = [
    ("Qué cambia entre árbol y neurona",
     "```python\n# Ayer (árbol)\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n\n"
     "# Hoy (neurona)\nmodelo = MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=0)\n```\n\n"
     "Con los mismos datos, ¿qué líneas del programa cambian al pasar del árbol a la neurona?",
     ["Todas: también cambian `fit`, `predict` y `accuracy_score`.",
      "Solo la línea que crea el modelo; el resto de la receta es igual.",
      "Solo la línea de `accuracy_score`.",
      "Hay que volver a escribir las listas de entradas y etiquetas."]),
    ("Qué son los pesos",
     "```python\nprint(modelo.coefs_)\n```\n\n"
     "Ese `print` muestra tres números, uno por columna. ¿Qué representan?",
     ["Las predicciones del test.",
      "Los aciertos de cada columna.",
      "Las filas más importantes de la tabla.",
      "La importancia que la computadora ajustó sola para cada columna."]),
    ("Leer el resultado",
     "```text\nárbol:   accuracy = 1,00  (4 de 4)\nneurona: accuracy = 0,75  (3 de 4)\n```\n\n"
     "Los dos modelos se probaron con las mismas 4 filas de prueba. ¿Qué conviene concluir?",
     ["El árbol acertó una fila más, pero con solo 4 filas esa diferencia prueba poco: conviene probar con más filas.",
      "La neurona es peor y hay que descartarla para siempre.",
      "El árbol es perfecto y no hace falta volver a probarlo.",
      "La neurona falló porque la semilla estaba mal: con otra semilla acertaría las 4."]),
]
TICKET_CORRECTAS = ["B", "D", "A"]
TICKET_JUSTIFICACION = [
    "Solo cambia la línea que crea el modelo: después siguen igual `fit`, `predict` y `accuracy_score`.",
    "`coefs_` son los pesos: la importancia que la computadora ajustó sola para cada columna.",
    "Con 4 filas de prueba cada fila vale 25 %, así que una fila de diferencia prueba poco; conviene probar con más filas.",
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────


def imagen(nombre: str, alt: str) -> str:
    datos = base64.b64encode((AQUI / "diagramas" / nombre).read_bytes()).decode("ascii")
    return f"![{alt}](data:image/png;base64,{datos})"


def celdas_inicio() -> list:
    c = [md("# 🐍 Clase 43 v2 — La neurona aprende sola\n\n"
            "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab\n\n---"),
         md("## 🎯 Objetivo de la clase\n\n" + OBJETIVO + "\n\n"
            "## 🔎 ¿Por qué lo veremos?\n\n"
            "> Las redes que reconocen voz o rostros están hechas de millones de estas neuronas que ponderan datos; hoy creamos una sola "
            "y vemos si le gana al árbol en los datos del wifi.\n\n---\n\n"
            "**Lo que ya sabes:** la receta de la N°42 y la N°42b (`crear → fit → predict → accuracy_score`) y cómo pasar una tabla a listas.\n\n"
            "**Lo que aprenderás hoy:** qué es una neurona, cómo crearla con la misma receta del árbol, mirar los pesos que la computadora ajusta sola "
            "y comparar los dos modelos con los mismos datos. Se ejecuta **de arriba hacia abajo**."),
         md("## 🔧 Ejecuta esta celda primero\n\n"
            "Los `import` raros van **SIEMPRE en la primera celda, ejecutada primero**: así no tienes que escribir `from sklearn... import ...` cada vez. "
            "Hoy traen el árbol (`DecisionTreeClassifier`), la neurona (`MLPClassifier`) y `accuracy_score`."),
         codigo(IMPORTS),
         md("Ahora ejecuta esta segunda celda (deja listos los verificadores automáticos; no hace falta entenderla ni editarla)."),
         codigo(CELDA_VERIFICADOR),
         md("---\n\n## 1️⃣ Haz Ahora\n\n"
            "El encargado de informática del liceo sigue con su problema: **el cuaderno tenía 6 columnas, pero nos pide trabajar con estas 3**, "
            "las mismas de ayer:\n\n"
            "- `dispositivos_conectados`: cuántos aparatos hay conectados al wifi\n"
            "- `estudiantes_viendo_video`: cuántos estudiantes están viendo videos\n"
            "- `horas_desde_reinicio`: cuántas horas lleva el router sin reiniciarse\n\n"
            + "\n".join(f"{i}. {p}" for i, p in enumerate(HAZ_AHORA, start=1))
            + "\n\nSabiendo que programamos, el encargado quiere probar un modelo nuevo — pero antes quiere que tengamos clara la lógica."),
         md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "),
         md("---\n\n### 🔁 Ayer → 🔀 Hoy → ➡️ La próxima clase\n\n"
            "| | Qué hacemos |\n|---|---|\n"
            "| 🔁 **Ayer** | El árbol aprendió solo una cadena de preguntas sí/no con las listas que tipeamos. |\n"
            "| 🔀 **Hoy es distinto** | Los mismos datos, otro modelo: una **neurona** que *pondera* cada columna (le da más o menos importancia). |\n"
            "| ➡️ **La próxima clase (lunes 16)** | Mini-LLM: cómo una IA de lenguaje predice la siguiente palabra. |\n\n"
            "| | Árbol | Neurona |\n|---|---|---|\n"
            "| Cómo decide | Cadena de preguntas sí/no | Suma de datos × importancia |\n"
            "| Quién lo arma | La computadora, con `fit` | La computadora, con `fit` |\n"
            "| La receta | crear → `fit` → `predict` → `accuracy_score` | **la misma** |")]
    return c


def icn() -> list:
    c = [md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
            "Hoy **no tipeamos los datos**: las listas ya vienen escritas (lo hiciste a mano en la N°42b). "
            "Cada concepto usa lo anterior, así que **ejecuta las celdas en orden**.")]

    c.append(md("### 💡 1. Datos listos\n\n"
                "Son los mismos 20 días del wifi: las **primeras 16 filas** para que la computadora **aprenda** (`train`) y las **últimas 4** para **probarla** (`test`). "
                "La etiqueta es `1` = el wifi se cayó, `0` = aguantó.\n\n"
                + idea("las listas `entradas_train`, `etiquetas_train`, `entradas_test` y `etiquetas_test` son el material con el que aprende y se prueba cualquier modelo.") + "\n\n"
                "▶️ **Solo ejecuta** la celda."))
    c.append(codigo(DATOS))

    c.append(md("### 💡 2. ¿Qué es una neurona?\n\n"
                "Una **neurona** es el modelo más pequeño de una red neuronal. Recibe las 3 columnas, **pondera** cada una (le da más o menos importancia), "
                "las **suma** y **decide** 0 o 1. Esos números de importancia se llaman **pesos** y **no los escribimos nosotros: los ajusta sola la computadora al entrenar**.\n\n"
                + imagen("neurona.png", "Diagrama de la neurona: tres columnas, cada una por su peso, una suma, el nivel de activación y la decisión 1 o 0") + "\n\n"
                "La flecha más gruesa es el dato con más peso. Después de sumar, la neurona calcula su **nivel de activación**: un número entre **0 y 1**. "
                "Si pasa de **0,5**, decide **1** (se cae); si no, decide **0** (aguanta).\n\n"
                + imagen("activacion.png", "Curva del nivel de activación con el umbral 0,5 y las cuatro filas de prueba") + "\n\n"
                "Cada punto es una de las 4 filas de prueba: mientras más a la derecha, mayor la suma y más se acerca el nivel de activación a 1.\n\n"
                + idea("una neurona recibe datos, pondera cada uno (peso), suma, calcula su nivel de activación (de 0 a 1) y decide: más de 0,5 → 1; si no → 0. Los pesos los ajusta sola la computadora.")))

    c.append(md("### 💡 3. La receta, cambiando una sola línea\n\n"
                "Es la receta de ayer: **crear → `fit` → `predict` → `accuracy_score`**. Lo único que cambia es la línea que crea el modelo. "
                "La neurona se crea así: `" + NEURONA + "`.\n\n"
                + idea("para usar otro modelo solo cambia la línea que lo crea; `fit`, `predict` y `accuracy_score` quedan igual.") + "\n\n"
                + escribelo("crea la neurona en `modelo`, entrénala con `train`, guarda en `predicciones` lo que predice para `entradas_test` y calcula su accuracy en `exactitud`.")))
    c.append(codigo("# Ayer (árbol):  modelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
                    "# Hoy (neurona): escribe la línea que crea la neurona\n"
                    "modelo = None   # ← reemplaza None\n\n"
                    "# Entrena con train, predice el test y calcula el accuracy\n"
                    "# Muestra las predicciones y el accuracy con una etiqueta clara\n"))
    c.append(md("<details><summary>❓ ¿Qué significa <code>hidden_layer_sizes=()</code>?</summary>\n\n"
                "Es el argumento que dice cuántas neuronas más se agregan en medio. Con `()` no hay ninguna: es **una sola neurona**. "
                "Cuántas poner se decide por prueba y error (hoy hay sistemas que automatizan esa búsqueda); nosotros seguimos con una sola.\n\n</details>"))
    c.append(md("#### 🔍 Revisa tu trabajo\n\nEjecuta la celda para comprobar tu neurona."))
    c.append(codigo("check_icn()"))

    c.append(md("### 💡 4. Abrir la caja: los pesos\n\n"
                "Después de `fit`, la neurona guarda los **pesos** que la computadora ajustó sola: `modelo.coefs_` (uno por columna, en el orden de las listas) "
                "y el **sesgo** (un pequeño ajuste extra): `modelo.intercepts_`.\n\n"
                + idea("`coefs_` e `intercepts_` son los pesos que la computadora ajustó sola; existen, pero no los leemos como verdad absoluta.") + "\n\n"
                + escribelo("muestra los pesos y el sesgo de tu `modelo`, cada uno con una etiqueta clara.")))
    c.append(codigo("# Muestra los pesos (coefs_) y el sesgo (intercepts_)\n"))
    c.append(md("🎲 **La semilla importa:** `random_state` es el número que fija el **punto de partida aleatorio** del entrenamiento. "
                "Con otra semilla los pesos (y a veces el accuracy) **salen distintos**. Cambia `semilla` a 1, ejecuta, y vuelve a 0:\n\n"
                "> **Siempre dejamos `random_state=0`** en las pruebas para que todos obtengamos lo mismo.\n\n"
                "*(Los números también pueden variar por otras razones técnicas, por ejemplo cómo termina de procesar el entrenamiento; no las veremos en este curso. "
                "Y los pesos no dicen por sí solos qué columna «es la importante»: quédate con que **existen y los ajusta la computadora**.)*"))
    c.append(codigo(DEMO_SEMILLA.replace("{S}", "0")))
    c.append(md("#### ✅ Verificamos lo aprendido\n\nEl colega le pregunta a dos personas del curso:\n\n"
                "- ¿Por qué cambian los pesos si usamos otra semilla?\n- ¿Los pesos los escribimos nosotros o los ajustó la computadora?"))

    c.append(md("### 💡 5. Revisar y comparar\n\n"
                "Al revisar hacemos dos cosas:\n\n"
                "1. **Leer el resultado:** mira las `predicciones` de la neurona junto a las `etiquetas_test`: ¿en qué fila falló?\n"
                "2. **Comparar la precisión:** el `accuracy_score` de la neurona frente al del árbol de ayer, **con los mismos datos**. "
                "Con 4 filas de prueba, cada fila vale 25 %.\n\n"
                + idea("para comparar dos modelos se usan los mismos datos y el mismo `accuracy_score`; con 4 filas de prueba cada fila vale 25 %.") + "\n\n"
                + escribelo("muestra las etiquetas reales y las predicciones de la neurona; calcula el accuracy del árbol en `exactitud_arbol` y muestra ambos accuracy con etiqueta.")))
    c.append(codigo("# El árbol de ayer, con los mismos datos (ya escrito)\n"
                    "arbol = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
                    "arbol.fit(entradas_train, etiquetas_train)\n"
                    "predicciones_arbol = arbol.predict(entradas_test)\n\n"
                    "# 1. Leer el resultado: etiquetas reales y predicciones de la neurona\n\n"
                    "# 2. Comparar la precisión: exactitud_arbol y exactitud (la de la neurona)\n"))
    c.append(codigo("check_comparar()"))
    c.append(md("🤔 **Para pensar:** ¿cuál de los dos usarían, y por qué? ¿Qué cambia si la diferencia es de una sola fila?"))

    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Cómo se escribe |\n|---|---|\n"
                "| Los `import` | siempre en la primera celda, ejecutada primero |\n"
                "| Neurona | recibe datos, pondera (pesos), suma, calcula su nivel de activación (0 a 1) y decide: más de 0,5 → 1 |\n"
                f"| Crearla | `modelo = {NEURONA}` |\n"
                "| La receta | `fit` → `predict` → `accuracy_score`: igual que el árbol |\n"
                "| Los pesos | `modelo.coefs_` e `modelo.intercepts_`: los ajustó sola la computadora |\n"
                "| `random_state` | fija el punto de partida; en las pruebas siempre `0` |\n"
                "| Comparar | mismos datos, mismo `accuracy_score`; con 4 filas cada fila vale 25 % |"))
    c.append(md("#### 🎞️ Resumen animado\n\n"
                f"Para repasar cada concepto con animaciones, mira las slides: [{URL_SLIDES}]({URL_SLIDES})"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| No ejecutar la celda de los `import` | `NameError: name 'MLPClassifier' is not defined` | Ejecutar siempre primero la celda de los `import` |\n"
                "| Cambiar `random_state` y creer que es otro modelo | Los pesos y a veces el accuracy cambian | Dejar `random_state=0` en las pruebas |\n"
                "| Leer los pesos como verdad absoluta | Concluir qué columna «importa» con una sola corrida | Recordar que existen y los ajusta la computadora |\n"
                "| Concluir con solo 4 filas de prueba | Se confía en una diferencia de una fila | Cada fila vale 25 %: probar con más filas |"))
    return c


def ejercicio(num: str, titulo: str, narrativa: str, debe: list, pistas: list, esp: str, arranque: str,
              check: str = "") -> list:
    rotulo = titulo if num == "guiada" else f"Ejercicio {num} — {titulo}"
    cuerpo = (f"### 🎯 {rotulo}\n\n{narrativa}\n\n**El programa debe:**\n\n" + "\n".join(f"- {b}" for b in debe)
              + "\n\n" + "\n\n".join(pistas) + "\n\n" + esp)
    c = [md(cuerpo), codigo(arranque)]
    if check:
        c.append(codigo(check))
    return c


def guiada() -> list:
    c = [md("---\n\n## 3️⃣ Práctica Guiada\n\nEste es **el ejercicio de la clase**: lo hacemos todos y al final revisamos uno entre todos.")]
    c += ejercicio(
        "guiada", "El encargado quiere decidir con qué modelo quedarse",
        "El encargado de informática del liceo tiene los mismos 20 días de wifi y dos modelos que probar: el **árbol** de ayer y la **neurona** de hoy. "
        "Las listas ya están escritas. Quiere ver los dos accuracy y que le cuentes, con tus propios números, cuál usarías. "
        "Antes de decidir, le preocupa que la prueba tenga muy pocas filas.",
        ["**Crear** el árbol (profundidad máxima 3, semilla 0) en `modelo_arbol` y la neurona en `modelo_neurona`, y **entrenar** los dos con `train`.",
         "**Predecir** el test con cada uno y **calcular** sus accuracy en `exactitud_arbol` y `exactitud_neurona`.",
         "**Mostrar** ambos accuracy con una etiqueta clara.",
         "**Escribir**, en un comentario, 2 líneas: cuál usarías y por qué (con tus números), y por qué 4 filas de prueba dan poca seguridad."],
        [pista(1, "la misma receta", "Los dos modelos se entrenan y se evalúan igual; solo cambia la línea que crea cada uno."),
         pista(2, "cada fila vale 25 %", "Con 4 filas de prueba, una fila de diferencia mueve el accuracy 0,25 puntos: piensa si eso alcanza para estar seguros.")],
        esperado(ejecutar(SOL_G)),
        "# Tu programa\n\n" + CENTINELA + "\n", check="check_guiada()")
    return c


def extras() -> list:
    c = [md("---\n\n## 4️⃣ Ejercicios extra\n\nPara seguir practicando en casa o si terminas antes. Cada uno trae pistas y un verificador. No tienen nota.")]
    c.append(md("### 🎯 Ejercicio 0a — Práctica directa: predecir una fila nueva\n\n"
                "La celda de abajo ya trae la neurona entrenada.\n\n**El programa debe:**\n\n"
                "- Preguntar a la neurona por **una sola** fila nueva: 88 dispositivos, 17 estudiantes viendo video y 4 horas desde el reinicio.\n"
                "- Guardar la predicción en una variable llamada `prediccion` e imprimirla con una etiqueta.\n\n"
                + esperado(ejecutar(E0A_SOL))))
    c.append(codigo("# Tu solución del Ejercicio 0a\n" + DATOS + f"\n\nmodelo = {NEURONA}\nmodelo.fit(entradas_train, etiquetas_train)\n\n" + CENTINELA + "\n"))
    c.append(codigo("check_ej0a()"))
    c += ejercicio(
        "1", "¿Y si el encargado usa otras columnas?",
        "Un compañero propone usar otras tres columnas del cuaderno del encargado: `temperatura_sala`, `hora_del_bloque` y `dia_del_mes`. "
        "Las listas ya están escritas. Hay que entrenar los dos modelos con ellas y ver cómo les va frente a las columnas de la clase.",
        ["**Entrenar** un árbol (profundidad 3, semilla 0) y la neurona de hoy con `entradas_train_otro` y `etiquetas_train`.",
         "**Calcular** sus accuracy en `exactitud_arbol_otro` y `exactitud_neurona_otro` con `entradas_test_otro` y `etiquetas_test`, y **mostrarlos**.",
         "**Escribir**, en un comentario, si estas columnas funcionan mejor o peor que las de la clase y qué sospechas."],
        [pista(1, "los datos", "`entradas_train_otro` y `entradas_test_otro` reemplazan a las listas de la clase; las etiquetas son las mismas."),
         pista(2, "la receta", "Es la misma receta de hoy; solo cambian las listas de entradas.")],
        esperado(ejecutar(E1_SOL)),
        "# Tu solución del Ejercicio 1\n" + DATOS_OTRO + "\n\n" + CENTINELA + "\n", check="check_ej1()")
    c += ejercicio(
        "2", "Desafío: ¿y si cambiamos la semilla?",
        "El encargado desconfía: «si cambio el número de la semilla, ¿la neurona sigue acertando igual?». Hay que probar cinco semillas y mirar qué pasa "
        "tanto con los días que la neurona usó para aprender como con los de prueba.",
        ["**Entrenar** la neurona de hoy una vez por cada semilla de 0 a 4.",
         "**Guardar** el accuracy en `train` de cada una en `exactitudes_train` y el de `test` en `exactitudes_test`, y **mostrar** ambas listas.",
         "**Escribir**, en un comentario, si los resultados cambian y qué te dice eso sobre confiar en una sola corrida."],
        [pista(1, "repetir cinco veces", "Puedes recorrer las semillas con `for semilla in [0, 1, 2, 3, 4]:` y crear la neurona con `random_state=semilla`."),
         pista(2, "guardar cada resultado", "Parte con una lista vacía y agrega cada accuracy con `.append(...)`.")],
        esperado(ejecutar(E2_SOL)),
        "# Tu solución del Ejercicio 2\n\n" + CENTINELA + "\n", check="check_ej2()")
    return c


def ticket() -> list:
    return [md("---\n\n## 🎫 Ticket de Salida\n\n"
               "Las preguntas **se proyectan en la tele**: no están en este cuaderno. Mira cada pregunta y **decide tu respuesta en silencio**; "
               "cuando termine la última, abre el formulario, escribe tu nombre y marca tus alternativas.\n\n"
               f"👉 **Formulario del Ticket de Salida:** [{URL_FORM}]({URL_FORM})\n\n"
               f"En «Tema de la clase de hoy» escribe: **{TEMA_FORM}**.")]


def cierre() -> list:
    return [md("---\n\n## 🎯 Cierre\n\n**Objetivo de la clase**\n\n" + OBJETIVO + "\n\n---\n\n"
               "**Reflexiona antes de irte** (las comentamos a viva voz):\n\n"
               "1. ¿Qué tan seguro/a te sientes creando, entrenando y evaluando una neurona, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. ¿Qué te sorprendió hoy de la neurona y por qué?\n\n"
               "3. ¿Dónde crees que se usan neuronas como esta fuera de la clase?\n\n"
               "👀 **Lo que viene (lunes 16):** el mini-LLM: cómo una IA de lenguaje predice la siguiente palabra."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. \n\n3. "),
            md("---")]


def clase() -> list:
    return celdas_inicio() + icn() + guiada() + ticket() + cierre() + extras()


# ───────────────────────── solucionario ─────────────────────────


def bloque_sol(titulo: str, cod: str, nota: str = "") -> list:
    out = "\n\n**Salida:**\n\n```text\n" + ejecutar(cod) + "\n```"
    return [md(f"### {titulo}{out}" + (f"\n\n{nota}" if nota else "")), codigo(cod)]


def solucionario() -> list:
    c = [md("# Clase 43 v2 — La neurona aprende sola · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Cada bloque es autocontenido (scikit-learn 1.9.1, sin archivos)."),
         md("## ⚙️ Celdas preparadas\n\nLas mismas dos celdas iniciales que ven los estudiantes (los `import` y el verificador)."),
         codigo(IMPORTS), codigo(CELDA_VERIFICADOR),
         md("## 🧠 Haz Ahora\n\n1. Es la **ponderación**: cada estudiante asigna una nota a cada columna; no hay una única respuesta, lo importante es que las notas sean distintas y estén justificadas (esperable: más nota al video y a las horas). Ese «dar más o menos importancia» es lo que hará la neurona. "
            "**Dato:** con estos datos la neurona le da más peso al video y casi nada a los dispositivos. "
            "2. 4 de 4 = **100 %**. 3. Cada fila vale **25 puntos porcentuales**. 4. 0,75 × 4 = **3 filas**.")]
    c.append(md("## 📘 ICN — código completo\n\nResultados verificados con scikit-learn 1.9.1: árbol **1,0** (4/4), neurona **0,75** (3/4; falla la fila 18)."))
    c += bloque_sol("Concepto 3 · Crear la neurona y la receta", SOL_C3,
                    "La neurona predice `[0, 0, 1, 0]`; las etiquetas reales son `[0, 1, 1, 0]`: falla la **fila 18** (117 dispositivos, 0 estudiantes viendo video).")
    c.append(codigo("check_icn()"))
    c += bloque_sol("Concepto 4 · Abrir la caja (pesos y sesgo)", SOL_C4A,
                    "Con `random_state=0`: pesos `[-0.035, 0.376, 0.098]` y sesgo `-0.048`. **No leer los pesos como verdad absoluta**: «dispositivos» sale casi en cero aunque sea una columna clara. "
                    "Quedarse en la idea de que existen y los ajusta la computadora.")
    for s, cod in zip((0, 1), SOL_C4B):
        c += bloque_sol(f"Concepto 4 · Demo de semilla (semilla = {s})", cod,
                        "Con semilla 0: pesos `[-0.035, 0.376, 0.098]`, train 0,875, test 0,75. Con semilla 1: pesos `[-0.001, 0.767, -0.099]`, train 0,75, test 0,75. "
                        "Los números también pueden variar por otras razones técnicas (cómo termina de procesar el entrenamiento); no se ven en el curso. "
                        "En las pruebas siempre `random_state=0`." if s == 1 else "")
    c += bloque_sol("Concepto 5 · Revisar y comparar", SOL_C5,
                    "Árbol 1,0 vs. neurona 0,75: con 4 filas cada fila vale 25 %, así que la diferencia es una sola fila. Respuesta esperada a «¿cuál usarían?»: "
                    "cualquiera bien justificada con números y mencionando que 4 filas prueban poco.")
    c.append(codigo("check_comparar()"))
    c.append(md("## 🧩 Práctica guiada — solución"))
    c += bloque_sol("Guiada · ¿Con qué modelo se queda el encargado?", SOL_G,
                    "Criterio de los 2 comentarios: (1) elige un modelo y cita sus números (árbol 1,0, neurona 0,75); (2) explica que con 4 filas cada fila vale 25 % y una fila de diferencia prueba poco. "
                    "**Revisión en vivo:** una pareja explica al frente qué cambió entre crear el árbol y crear la neurona. Alineada con la Prueba 1 (B, C1, C3).")
    c.append(codigo("check_guiada()"))
    c.append(md("## 🚀 Ejercicios extra — soluciones"))
    c += bloque_sol("Ejercicio 0a", E0A_SOL)
    c.append(codigo("check_ej0a()"))
    c += bloque_sol("Ejercicio 1 · Otras columnas", E1_SOL,
                    "Con las columnas `temperatura_sala`, `hora_del_bloque` y `dia_del_mes` los dos modelos rinden peor (árbol 0,25, neurona 0,25): las columnas sin relación con la red no ayudan. "
                    "Criterio: dice que rinden peor y lo atribuye a las columnas.")
    c.append(codigo("check_ej1()"))
    c += bloque_sol("Ejercicio 2 · Semillas (desafío)", E2_SOL,
                    "Los resultados **sí cambian con la semilla** (p. ej. la semilla 4 baja a 0,5 en test). Criterio: nota que cambian y concluye que no conviene confiar en una sola corrida.")
    c.append(codigo("check_ej2()"))
    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                f"Respuestas correctas: **{', '.join(TICKET_CORRECTAS)}**. Las preguntas **no están en el Colab de estudiantes**: se proyectan en `Ticket de Salida.pptx` "
                f"y se responden en el Google Form (`{URL_FORM}`). Respuestas también en `Ticket de Salida Respuestas.json`."))
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        alts = "\n".join(f"- **{'ABCD'[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}\n\n**Respuesta correcta: {TICKET_CORRECTAS[i - 1]}.** {TICKET_JUSTIFICACION[i - 1]}"))
    return c


if __name__ == "__main__":
    SALIDA_JSON.write_text(json.dumps(
        {"clase": "43 v2", "tema": TEMA_FORM,
         "respuestas": {**{f"Respuestas a ticket [{i}]": l for i, l in enumerate(TICKET_CORRECTAS, start=1)}, "Respuestas a ticket [4]": "No se preguntó"}},
        ensure_ascii=False, indent=2), encoding="utf-8")
    guardar(SALIDA_CLASE, clase())
    guardar(SALIDA_SOL, solucionario())
    print("Listo:", SALIDA_CLASE.name, "·", SALIDA_SOL.name)
    print("Árbol", EXACT_ARBOL, "· neurona", EXACT_NEURONA, "· ej1", E1_ARBOL, E1_NEURONA, "· ej2", E2_TRAIN, E2_TEST)
