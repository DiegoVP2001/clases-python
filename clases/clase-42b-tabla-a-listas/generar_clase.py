"""Genera 'Clase 42b - De la Tabla a las Listas - Clase.ipynb' (estudiantes) y '... - Solucionario.ipynb' (profesor).

Fuente de verdad: este script + la Spec aprobada + datos_wifi_verificados.json + datos_extras_verificados.json.
No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.   Ejecutar: py -3 generar_clase.py
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
NOMBRE = "Clase 42b - De la Tabla a las Listas"
SALIDA_CLASE = AQUI / f"{NOMBRE} - Clase.ipynb"
SALIDA_SOL = AQUI / f"{NOMBRE} - Solucionario.ipynb"

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


def b64(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


# ───────────────────────── datos (verificados con scikit-learn, ver los .json) ─────────────────────────

WIFI = json.loads((AQUI / "datos_wifi_verificados.json").read_text(encoding="utf-8"))
EXTRAS = json.loads((AQUI / "datos_extras_verificados.json").read_text(encoding="utf-8"))
COLS = WIFI["cols"]                      # 6 columnas
TABLA, ETIQ = WIFI["X"], WIFI["y"]       # 20 filas
SENSATO = [0, 1, 2]                      # dispositivos, video, horas desde el reinicio (las 3 columnas elegidas por la clase)
NOMBRES3 = [COLS[c] for c in SENSATO]
QUE_MIDE = {"dispositivos_conectados": "cuántos aparatos hay conectados al wifi",
            "estudiantes_viendo_video": "cuántos estudiantes están viendo videos",
            "horas_desde_reinicio": "cuántas horas lleva el router sin reiniciarse",
            "temperatura_sala": "temperatura de la sala (°C)",
            "hora_del_bloque": "bloque horario del día en que se anotó (del 1 al 8)",
            "dia_del_mes": "día del mes (del 1 al 31)"}
CENTINELA = "# ── Escribe tu programa desde aquí ──"


def lista(filas, sangria=4):
    """Una fila por línea: [[a, b, c],\n [d, e, f]]"""
    sp = " " * sangria
    return "[" + (",\n" + sp).join(str(f) for f in filas) + "]"


def columnas(filas, cols):
    return [[f[c] for c in cols] for f in filas]


def tabla_md(nombres, filas, etiquetas, desde=1, ocultar=()):
    """Tabla markdown con numeración de filas; 'ocultar' = columnas que no se muestran."""
    idx = [i for i in range(len(nombres)) if i not in ocultar]
    cab = "| Fila | " + " | ".join(f"`{nombres[i]}`" for i in idx) + " | `cae` |"
    sep = "|---|" + "---|" * (len(idx) + 1)
    cuerpo = "\n".join(f"| {desde + k} | " + " | ".join(str(f[i]) for i in idx) + f" | {etiquetas[k]} |"
                       for k, f in enumerate(filas))
    return "\n".join([cab, sep, cuerpo])


# Datos de cada pieza
ICN_TRAIN_X, ICN_TRAIN_Y = columnas(TABLA[:16], SENSATO), ETIQ[:16]
ICN_TEST_X, ICN_TEST_Y = columnas(TABLA[16:], SENSATO), ETIQ[16:]

G = EXTRAS["guiada"]; G_NOMBRES = ["computadores_en_uso", "estudiantes_viendo_video", "horas_desde_reinicio",
                                   "ancho_de_banda_contratado", "dia_del_mes"]
E1 = EXTRAS["ej1"]; E1_NOMBRES = ["usuarios_conectados", "notebooks_en_mesas", "horas_desde_reinicio", "dia_del_mes"]
E2 = EXTRAS["ej2"]; E2_NOMBRES = ["equipos_encendidos", "estudiantes_viendo_video", "horas_desde_reinicio"]
E3 = EXTRAS["ej3"]; E3_NOMBRES = E3["cols"]

E0A_TABLA = [[60, 5, 3], [95, 20, 14], [40, 0, 22]]
E0A_ETIQ = [0, 1, 0]
E0B_ENTRADAS = [[60, 5, 3], [95, 20, 14], [40, 0, 22], [110, 2, 8], [30, 12, 5], [85, 0, 18]]
E0B_ETIQ = [0, 1, 0, 1, 1, 0]

# ───────────────────────── soluciones (se ejecutan para obtener los resultados esperados) ─────────────────────────

RECETA_IMPORTS = ("from sklearn.tree import DecisionTreeClassifier\n"
                  "from sklearn.metrics import accuracy_score\n\n")


def datos_split(x_tr, y_tr, x_te, y_te, sufijo=""):
    return (f"entradas_train{sufijo} = {lista(x_tr, 4 + 0)}\n"
            f"etiquetas_train{sufijo} = {y_tr}\n\n"
            f"entradas_test{sufijo} = {lista(x_te)}\n"
            f"etiquetas_test{sufijo} = {y_te}\n")


SOL_C1 = ("# Justificación de ejemplo:\n"
          "# Elegimos dispositivos_conectados y estudiantes_viendo_video porque son los que más cargan la red;\n"
          "# y horas_desde_reinicio porque un router que lleva muchas horas sin reiniciarse se degrada.\n"
          "# Dejamos fuera temperatura_sala, hora_del_bloque y dia_del_mes porque no cargan la red por sí solas.")

SOL_C2 = f"fila_2 = {columnas(TABLA[1:2], SENSATO)[0]}\nprint(\"Fila 2:\", fila_2)"

SOL_C3 = ("fila_2 = " + str(ICN_TRAIN_X[1]) + "\n\n"
          "entradas_train = " + lista(ICN_TRAIN_X) + "\n"
          "etiquetas_train = " + str(ICN_TRAIN_Y) + "\n"
          "print(\"Filas de entrenamiento:\", len(entradas_train), \"· etiquetas:\", len(etiquetas_train))")

SOL_C4 = (datos_split(ICN_TRAIN_X, ICN_TRAIN_Y, ICN_TEST_X, ICN_TEST_Y)
          + "\nprint(\"Filas de prueba:\", len(entradas_test), \"· etiquetas:\", len(etiquetas_test))")

SOL_C5 = (RECETA_IMPORTS + datos_split(ICN_TRAIN_X, ICN_TRAIN_Y, ICN_TEST_X, ICN_TEST_Y)
          + "\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
          "modelo.fit(entradas_train, etiquetas_train)\n"
          "predicciones = modelo.predict(entradas_test)\n"
          "print(\"Predicciones del test:\", predicciones)\n"
          "print(\"Etiquetas reales:      \", etiquetas_test)")

SOL_C6 = ("from sklearn.tree import export_text\n" + SOL_C5 +
          "\n\n# Revisar 1: leer el árbol (los nombres van en el MISMO orden que las columnas de mis listas)\n"
          "nombres_variables = " + str(NOMBRES3) + "\n"
          "print(export_text(modelo, feature_names=nombres_variables))\n\n"
          "# Revisar 2: precisión (accuracy)\n"
          "exactitud = accuracy_score(etiquetas_test, predicciones)\n"
          "print(\"Accuracy en el test:\", exactitud)")

# Guiada
G_X = columnas(G["X"], [0, 1, 2]); G_Y = G["y"]
SOL_G = (RECETA_IMPORTS + datos_split(G_X[:8], G_Y[:8], G_X[8:], G_Y[8:]) +
         "\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
         "modelo.fit(entradas_train, etiquetas_train)\n"
         "predicciones = modelo.predict(entradas_test)\n"
         "exactitud = accuracy_score(etiquetas_test, predicciones)\n\n"
         "print(\"Predicciones de las 2 filas de prueba:\", predicciones)\n"
         "print(\"Etiquetas reales:\", etiquetas_test)\n"
         "print(\"Accuracy en el test:\", exactitud)\n\n"
         "# Con solo 2 filas de prueba, acertar los 2 no basta para confiar: conviene probar con más filas.")

# Ejercicios extra
E0A_SOL = f"entradas = {E0A_TABLA}\netiquetas = {E0A_ETIQ}\nprint(\"entradas:\", entradas)\nprint(\"etiquetas:\", etiquetas)"

E0B_BASE = ("from sklearn.tree import DecisionTreeClassifier\n\n"
            f"entradas = {lista(E0B_ENTRADAS)}\n"
            f"etiquetas = {E0B_ETIQ}\n\n"
            "modelo = DecisionTreeClassifier(max_depth=2, random_state=0)\n"
            "modelo.fit(entradas, etiquetas)")
E0B_SOL = E0B_BASE + "\n\nprediccion = modelo.predict([[88, 17, 4]])\nprint(\"Predicción para la fila nueva (1 = se cae, 0 = aguanta):\", prediccion)"

E1_X = columnas(E1["X"], [0, 1, 2]); E1_Y = E1["y"]
E1_SOL = (RECETA_IMPORTS + datos_split(E1_X[:8], E1_Y[:8], E1_X[8:], E1_Y[8:]) +
          "\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
          "modelo.fit(entradas_train, etiquetas_train)\n"
          "predicciones = modelo.predict(entradas_test)\n"
          "exactitud = accuracy_score(etiquetas_test, predicciones)\n"
          "print(\"Predicciones del test:\", predicciones)\n"
          "print(\"Accuracy en el test:\", exactitud)")

E2_X, E2_Y = E2["X"], E2["y"]
E2_FALLA = E2_Y[:4] + E2_Y[5:]          # se omitió la 5ª etiqueta
E2_BASE = ("from sklearn.tree import DecisionTreeClassifier\n\n"
           f"entradas = {lista(E2_X)}\n"
           "etiquetas = {ETQ}\n\n"
           "modelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
           "modelo.fit(entradas, etiquetas)\n"
           "print(\"El modelo ya aprendió de\", len(entradas), \"filas\")")
E2_SOL = E2_BASE.replace("{ETQ}", str(E2_Y))

E3_X, E3_Y = E3["X"], E3["y"]
E3_FLOJO = [3, 4, 5]
E3_FLOJO_X, E3_CMP = columnas(E3_X, E3_FLOJO), "_companero"
E3_SOL = (RECETA_IMPORTS + "# Mi trío: dispositivos_conectados, estudiantes_viendo_video, horas_desde_reinicio\n"
          + datos_split(columnas(E3_X[:8], SENSATO), E3_Y[:8], columnas(E3_X[8:], SENSATO), E3_Y[8:]) + "\n"
          + "def evaluar(e_tr, y_tr, e_te, y_te):\n"
            "    m = DecisionTreeClassifier(max_depth=3, random_state=0)\n"
            "    m.fit(e_tr, y_tr)\n"
            "    return accuracy_score(y_te, m.predict(e_te))\n\n"
          + "# Trío del compañero: temperatura_sala, hora_del_bloque, dia_del_mes\n"
          + datos_split(E3_FLOJO_X[:8], E3_Y[:8], E3_FLOJO_X[8:], E3_Y[8:], E3_CMP) + "\n"
          + "mi_accuracy = evaluar(entradas_train, etiquetas_train, entradas_test, etiquetas_test)\n"
            "su_accuracy = evaluar(entradas_train_companero, etiquetas_train_companero, entradas_test_companero, etiquetas_test_companero)\n"
            "print(\"Accuracy de mi trío:\", mi_accuracy)\n"
            "print(\"Accuracy del trío del compañero:\", su_accuracy)")

E4_SOL = (E3_SOL + "\n\n# Cambio: el primer dato de la primera fila de prueba quedó mal anotado y pasa a valer 100\n"
          "entradas_test[0][0] = 100\n"
          "print(\"Accuracy de mi trío con el dato mal anotado:\", evaluar(entradas_train, etiquetas_train, entradas_test, etiquetas_test))")

# ───────────────────────── verificador (celda preparada) ─────────────────────────

TICKET_CORRECTAS = ["D", "B", "C", "A"]
TICKET_JUSTIFICACION = [
    "Cada fila va en su propia lista, las filas se separan con coma y todo va dentro de otro par de corchetes.",
    "Cada etiqueta está en la misma posición que su fila: la fila 3 se empareja con la tercera etiqueta, que es 0.",
    "predict() espera una tabla (una lista de filas); una sola fila nueva va dentro de otra lista: [[88, 17, 4]].",
    "Acertó esas 4 filas, pero con tan pocos no basta para confiar: conviene probar el modelo con más filas.",
]
TICKET_PISTAS = [
    "Piensa qué debe quedar junto: los tres datos de una fila, y qué separa una fila de otra.",
    "Mira qué posición ocupa la fila 3 y qué hay en esa misma posición de la otra lista.",
    "Recuerda cuántos corchetes necesita predict() para recibir una tabla, aunque tenga una sola fila.",
    "Pregúntate cuántos filas de prueba hay y si eso alcanza para estar seguros.",
]


def huella(i: int, letra: str) -> str:
    return hashlib.sha256(f"c42b|{i}|{letra}".encode()).hexdigest()[:16]


CELDA_VERIFICADOR = '''
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)
import base64
import hashlib
import itertools
from sklearn.tree import DecisionTreeClassifier

_NOMBRES = __NOMBRES__
_TABLA = __TABLA__
_ETIQ = __ETIQ__
_G_TABLA, _G_ETIQ, _G_ACIERTOS = __G__
_E1_TABLA, _E1_ETIQ, _E1_ACIERTOS = __E1__
_E2_ETIQ = __E2__
_E3_TABLA, _E3_ETIQ = __E3__
_E0A = __E0A__


def _columnas_usadas(filas, tabla, inicio):
    """Busca qué columnas (y en qué orden) usó el estudiante: devuelve (columnas, filas que coinciden)."""
    k = len(filas[0])
    mejor, mejor_n = None, -1
    for cols in itertools.permutations(range(len(tabla[0])), k):
        n = sum(1 for i, f in enumerate(filas) if [tabla[inicio + i][c] for c in cols] == list(f))
        if n > mejor_n:
            mejor, mejor_n = cols, n
    return mejor, mejor_n


def _revisar(tabla, etiquetas, n_train, cols_esperadas=None, nombres=None):
    g = globals()
    nombres = nombres or _NOMBRES
    claves = ("entradas_train", "etiquetas_train", "entradas_test", "etiquetas_test")
    valores = [g.get(c) for c in claves]
    faltan = [c for c, v in zip(claves, valores) if not v]
    if faltan:
        print("⏳ Todavía faltan estas listas:", ", ".join(faltan))
        return None
    e_tr, y_tr, e_te, y_te = valores
    n_test = len(tabla) - n_train
    for nombre, v, n in (("entradas_train", e_tr, n_train), ("etiquetas_train", y_tr, n_train),
                         ("entradas_test", e_te, n_test), ("etiquetas_test", y_te, n_test)):
        if len(v) != n:
            print(f"⚠️ {nombre} tiene {len(v)} elementos y debería tener {n} (uno por fila).")
            print("   Pista: cuenta las filas de la tabla y revisa que no falte ninguno ni sobre uno.")
            return None
    for nombre, v in (("entradas_train", e_tr), ("entradas_test", e_te)):
        if not all(isinstance(f, (list, tuple)) and len(f) == len(e_tr[0]) for f in v):
            print(f"⚠️ En {nombre} cada fila debe ser una lista con la misma cantidad de datos.")
            print("   Pista: cada fila va entre corchetes y con una coma entre sus datos.")
            return None
    for nombre, mios, reales, inicio in (("etiquetas_train", y_tr, etiquetas[:n_train], 0),
                                         ("etiquetas_test", y_te, etiquetas[n_train:], n_train)):
        for i, (a, b) in enumerate(zip(mios, reales)):
            if a != b:
                print(f"⚠️ La etiqueta de la posición {i + 1} de {nombre} no coincide con la de la fila {inicio + i + 1} de la tabla.")
                print("   Pista: cada etiqueta debe estar en la misma posición que su fila.")
                return None
    cols, ok = _columnas_usadas(e_tr, tabla, 0)
    if ok < len(e_tr):
        i = next(j for j, f in enumerate(e_tr) if [tabla[j][c] for c in cols] != list(f))
        print(f"⚠️ El fila {i + 1} de entradas_train no coincide con la tabla.")
        print("   Pista: revisa que cada dato esté en la columna correcta y que el orden de las columnas sea el mismo en todas las filas.")
        return None
    cols_te, ok_te = _columnas_usadas(e_te, tabla, n_train)
    if cols_te != cols or ok_te < len(e_te):
        print("⚠️ entradas_test no usa las mismas columnas, en el mismo orden, que entradas_train.")
        print("   Pista: las filas de prueba deben escribirse igual que los de entrenamiento.")
        return None
    if cols_esperadas is not None and tuple(cols) != tuple(cols_esperadas):
        print("⚠️ Tus listas coinciden con la tabla, pero usaste otras columnas: ", ", ".join(nombres[c] for c in cols))
        print("   Pista: las columnas pedidas son:", ", ".join(nombres[c] for c in cols_esperadas), "(en ese orden)")
        return None
    return cols


def _aciertos(cols, tabla, etiquetas, n_train):
    m = DecisionTreeClassifier(max_depth=3, random_state=0)
    m.fit([[f[c] for c in cols] for f in tabla[:n_train]], etiquetas[:n_train])
    pred = m.predict([[f[c] for c in cols] for f in tabla[n_train:]])
    return int(sum(1 for p, y in zip(pred, etiquetas[n_train:]) if p == y))


def _cierre_accuracy(aciertos, n_test):
    ex = globals().get("exactitud")
    if ex is None:
        print("⏳ Falta calcular el accuracy y guardarlo en una variable llamada exactitud.")
    elif abs(ex - aciertos / n_test) < 1e-9:
        print("✅ Tu accuracy es el esperado.")
    else:
        print("⚠️ Tu accuracy no coincide con el esperado.")
        print("   Pista: entrena con profundidad máxima 3 y semilla 0, y compara las predicciones con etiquetas_test.")


def check_icn():
    cols = _revisar(_TABLA, _ETIQ, 16, (0, 1, 2))
    if cols is None:
        return
    print("✅ Tus listas coinciden con la tabla, fila por fila y etiqueta por etiqueta.")
    esperados = [_NOMBRES[c] for c in (0, 1, 2)]
    nv = globals().get("nombres_variables")
    if nv is None:
        print("⏳ Falta escribir nombres_variables con los nombres de tus 3 columnas.")
    elif list(nv) != esperados:
        print("⚠️ Los nombres de nombres_variables no coinciden con tus columnas, o están en otro orden.")
        print("   Pista: deben ir en el mismo orden que las columnas de tus listas:", ", ".join(esperados))
    else:
        print("✅ nombres_variables coincide con tus columnas y con su orden.")
    _cierre_accuracy(_aciertos(cols, _TABLA, _ETIQ, 16), 4)
    print("   Con solo 4 filas de test, ¿alcanza con acertar los 4 para confiar en el modelo?")


def check_guiada():
    cols = _revisar(_G_TABLA, _G_ETIQ, 8, (0, 1, 2), ["computadores_en_uso", "estudiantes_viendo_video",
                                                      "horas_desde_reinicio", "ancho_de_banda_contratado", "dia_del_mes"])
    if cols is None:
        return
    print("✅ Tus listas coinciden con la tabla del liceo vecino.")
    _cierre_accuracy(_G_ACIERTOS, 2)


def check_ej0a():
    e, y = globals().get("entradas"), globals().get("etiquetas")
    if not e or not y:
        print("⏳ Todavía faltan las listas entradas y etiquetas.")
    elif [list(f) for f in e] != _E0A[0]:
        print("⚠️ entradas no coincide con la tabla.")
        print("   Pista: una lista por fila, con los tres datos en el mismo orden de las columnas, todas dentro de otra lista.")
    elif list(y) != _E0A[1]:
        print("⚠️ etiquetas no coincide con la columna cae de la tabla.")
        print("   Pista: una etiqueta por fila, en el mismo orden de las filas.")
    else:
        print("✅ Tus listas coinciden con la tabla.")


def check_ej0b():
    p = globals().get("prediccion")
    m = globals().get("modelo")
    if p is None or m is None:
        print("⏳ Falta guardar la predicción en una variable llamada prediccion.")
    elif list(p) != list(m.predict([[88, 17, 4]])):
        print("⚠️ Tu predicción no corresponde a la fila nueva (88, 17, 4).")
        print("   Pista: una sola fila nueva va dentro de otra lista: [[...]].")
    else:
        print("✅ Predijiste la fila nueva con la forma correcta.")


def check_ej1():
    cols = _revisar(_E1_TABLA, _E1_ETIQ, 8, (0, 1, 2), ["usuarios_conectados", "notebooks_en_mesas",
                                                        "horas_desde_reinicio", "dia_del_mes"])
    if cols is None:
        return
    print("✅ Tus listas coinciden con la tabla de la biblioteca.")
    _cierre_accuracy(_E1_ACIERTOS, 2)


def check_ej2():
    et = globals().get("etiquetas")
    m = globals().get("modelo")
    if et is None:
        print("⏳ Falta la lista etiquetas.")
    elif len(et) != len(_E2_ETIQ):
        print(f"⚠️ etiquetas tiene {len(et)} elementos y hay {len(_E2_ETIQ)} filas.")
        print("   Pista: compara la tabla con tu lista, fila por fila, hasta encontrar la que falta.")
    elif list(et) != _E2_ETIQ:
        print("⚠️ Ya hay una etiqueta por fila, pero alguna quedó en una posición equivocada.")
        print("   Pista: la etiqueta que agregaste debe quedar justo en la posición de su fila, no al final.")
    elif m is None or not hasattr(m, "tree_"):
        print("⏳ Las etiquetas ya están bien. Ejecuta de nuevo la celda completa para que el modelo aprenda.")
    else:
        print("✅ Corregiste la lista: cada etiqueta está en la misma posición que su fila.")


def evaluar(e_tr, y_tr, e_te, y_te):
    """Entrena un árbol (profundidad 3, semilla 0) con train y devuelve el accuracy en test."""
    m = DecisionTreeClassifier(max_depth=3, random_state=0)
    m.fit(e_tr, y_tr)
    pred = m.predict(e_te)
    return sum(1 for p, y in zip(pred, y_te) if p == y) / len(y_te)


def check_ej3():
    cols = _revisar(_E3_TABLA, _E3_ETIQ, 8, None, ["dispositivos_conectados", "estudiantes_viendo_video",
                                                   "horas_desde_reinicio", "temperatura_sala", "hora_del_bloque", "dia_del_mes"])
    if cols is None:
        return
    print("✅ Tus listas coinciden con la tabla. Columnas que usaste:", ", ".join(
        ["dispositivos_conectados", "estudiantes_viendo_video", "horas_desde_reinicio", "temperatura_sala",
         "hora_del_bloque", "dia_del_mes"][c] for c in cols))
    print("   Ahora calcula tu accuracy y el del compañero con evaluar(...) y explica cuál conviene.")


print("Verificador listo ✅")
'''

# aciertos reales de guiada y ej1 (accuracy * 2, porque el test tiene 2 filas)
_acc_g = float(ejecutar(SOL_G).split("Accuracy en el test: ")[1].splitlines()[0])
_acc_1 = float(ejecutar(E1_SOL).split("Accuracy en el test: ")[1].splitlines()[0])
G_ACIERTOS, E1_ACIERTOS = int(round(_acc_g * 2)), int(round(_acc_1 * 2))

CELDA_VERIFICADOR = (CELDA_VERIFICADOR
                     .replace("__NOMBRES__", json.dumps(COLS))
                     .replace("__TABLA__", json.dumps(TABLA))
                     .replace("__ETIQ__", json.dumps(ETIQ))
                     .replace("__G__", json.dumps([G["X"], G["y"], G_ACIERTOS]))
                     .replace("__E1__", json.dumps([E1["X"], E1["y"], E1_ACIERTOS]))
                     .replace("__E2__", json.dumps(E2_Y))
                     .replace("__E3__", json.dumps([E3["X"], E3["y"]]))
                     .replace("__E0A__", json.dumps([E0A_TABLA, E0A_ETIQ])))

# ───────────────────────── contenido compartido ─────────────────────────

HAZ_AHORA = [
    "Mirando los nombres de las 6 columnas, ¿cuáles 3 creen que más ayudan a saber si el wifi se cae?",
    "¿Cuáles son las 3 que descartaron y por qué?",
    "Al final de cada registro, el encargado tiene otra columna que se llama **«¿Se cayó el wifi?»**. ¿Cómo representarían esa respuesta con una **etiqueta** binaria, en código?",
    "Si el cuaderno tiene **20 filas de datos**, ¿cuántas filas de datos dejarían para entrenar el modelo y cuántas para probarlo (testearlo)?",
]

TICKET_PREGUNTAS = [
    ("La forma de la tabla",
     "Tres filas del wifi, con tres datos cada uno (dispositivos, estudiantes viendo video, horas desde el reinicio):\n\n"
     "```text\nFila 1: 71, 0, 20\nFila 2: 62, 2, 12\nFila 3: 79, 2, 2\n```\n\n"
     "¿Cuál de estas opciones escribe correctamente la tabla de entradas?",
     ["`[71, 0, 20, 62, 2, 12, 79, 2, 2]`",
      "`[[71, 62, 79], [0, 2, 2], [20, 12, 2]]`",
      "`[[71, 0, 20] [62, 2, 12] [79, 2, 2]]`",
      "`[[71, 0, 20], [62, 2, 12], [79, 2, 2]]`"]),
    ("Cada etiqueta con su fila",
     "```python\nentradas = [[71, 0, 20], [62, 2, 12], [79, 2, 2], [73, 0, 15]]\netiquetas = [1, 1, 0, 1]\n```\n\n"
     "¿Qué etiqueta le corresponde a la fila 3, `[79, 2, 2]`?",
     ["`1`, la de la última fila.",
      "`0`, la que está en la misma posición que la fila 3.",
      "`1`, la de la fila 2.",
      "No se puede saber, porque las etiquetas están en otra lista."]),
    ("Predecir una sola fila",
     "```python\nmodelo.fit(entradas_train, etiquetas_train)\nresultado = modelo.predict(...)   # <- completa esta línea\n```\n\n"
     "Queremos preguntar por **una sola** fila nueva: 88 dispositivos, 17 estudiantes viendo video y 4 horas desde el reinicio. "
     "¿Cómo se escribe?",
     ["`modelo.predict([88, 17, 4])`",
      "`modelo.predict(88, 17, 4)`",
      "`modelo.predict([[88, 17, 4]])`",
      "`modelo.predict([[88], [17], [4]])`"]),
    ("Pensar sobre el test",
     "Un modelo se prueba con las 4 filas que guardamos aparte y acierta los 4 (accuracy = 1,0).\n\n"
     "¿Qué conviene concluir?",
     ["Que acertó esas 4 filas; con tan pocos no basta para confiar, conviene probarlo con más.",
      "Que el modelo es perfecto y se puede usar sin revisar.",
      "Que el test estaba mal elegido, porque un modelo nunca debería acertar todo.",
      "Que el modelo se aprendió de memoria las 4 filas del test."]),
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────

OBJETIVO = "Convertir una tabla de datos en listas de entradas y etiquetas para entrenar y evaluar un modelo con atención."


def imagen_80_20() -> str:
    datos = base64.b64encode((AQUI / "diagramas" / "split_80_20.png").read_bytes()).decode("ascii")
    return f"![Diagrama del 80 / 20: 16 filas para aprender y 4 para probar](data:image/png;base64,{datos})"


def celdas_inicio() -> list:
    c = []
    c.append(md("# 🐍 Clase 42b — De la tabla a las listas\n\n"
                "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab\n\n---"))
    c.append(md("## 🎯 Objetivo de la clase\n\n" + OBJETIVO + "\n\n"
                "## 🔎 ¿Por qué lo veremos?\n\n"
                "> Antes de que un modelo aprenda algo, alguien tiene que ordenar los datos para dárselos, y un dato en el lugar "
                "equivocado le enseña algo falso sin que nadie lo note. Hoy ordenamos los registros del wifi del liceo y medimos "
                "qué tan bien predice la red.\n\n---\n\n"
                "**Lo que ya sabes:** todo lo dictado hasta N°42 (variables, etiqueta, `DecisionTreeClassifier`, `fit()` y `predict()`) "
                "y Python hasta listas.\n\n"
                "**Lo que aprenderás hoy:** escribir una tabla como listas, elegir qué columnas usar, separar filas para aprender y para probar, "
                "y medir qué tan bien acierta el modelo con `accuracy_score`. "
                "**Todos los datos vienen en este cuaderno** (sin archivos ni descargas) y se ejecuta de arriba hacia abajo."))
    c.append(md("### 🔧 Antes de empezar\n\n"
                "Ejecuta la celda de abajo una sola vez: deja listos los **verificadores automáticos** que usaremos para revisar tus listas "
                "(no hace falta entenderla ni editarla)."))
    c.append(codigo(CELDA_VERIFICADOR))
    c.append(md("---\n\n## 1️⃣ Haz Ahora\n\n"
                "El encargado de informática del liceo quiere un sistema que le avise si el wifi se va a caer durante las clases. "
                "Registró varios datos en una tabla, donde las distintas columnas son:\n\n"
                + "\n".join(f"- `{c}`: {QUE_MIDE[c]}" for c in COLS) + "\n\n"
                "y no sabe cuáles le podrían servir para resolver el problema.\n\n"
                + "\n".join(f"{i}. {p}" for i, p in enumerate(HAZ_AHORA, start=1))
                + "\n\nEl encargado, sabiendo que programamos, nos pide ayuda para armar ese sistema — pero antes quiere que tengamos clara la lógica."))
    c.append(md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "))
    c.append(md("---\n\n### 🔁 Ayer → 🔀 Hoy → ➡️ Mañana\n\n"
                "| | Qué hacíamos |\n|---|---|\n"
                "| 🔁 **Ayer (N°42)** | El árbol encontró solo las preguntas que separan los días atrasados de los puntuales. **Los datos ya venían escritos.** |\n"
                "| 🔀 **Hoy** | **Nosotros** escribimos los datos: pasamos la tabla del cuaderno a las listas que recibe el modelo, y probamos qué tan bien aprendió. |\n"
                "| ➡️ **Mañana** | La misma receta con otro modelo: una neurona. |\n\n"
                "**Recordemos la receta de ayer:** `modelo = DecisionTreeClassifier(...)` → `modelo.fit(entradas, etiquetas)` → `modelo.predict([[...]])`."))
    return c


def icn_clase() -> list:
    c = []
    c.append(md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
                "Esta es la tabla de registros del liceo: **20 filas de clases**, 6 columnas y la etiqueta `cae`, que responde la pregunta del encargado: "
                "**¿se cayó el wifi?** (`1` = sí, `0` = no; el 1 significa «sí», no «bueno»). Primero, cómo vamos a usarla:\n\n"
                + imagen_80_20() + "\n\n"
                "De las 20 filas, **las primeras 16** son para que la computadora **aprenda** y **las últimas 4** las guardamos para **probarla** con filas que no vio.\n\n"
                + tabla_md(COLS, TABLA, ETIQ)))
    c.append(md("Ahora ve concepto por concepto y escribe tú el código que falta. "
                "Todo lo que escribas queda guardado en las celdas de abajo: cada concepto usa lo que hiciste en el anterior, "
                "así que **ejecuta las celdas en orden**."))

    c.append(md("### 💡 1. Elegir las 3 columnas\n\n"
                "Un modelo no necesita todas las columnas. Quedarnos solo con las que podrían explicar la etiqueta **ahorra procesamiento**: "
                "menos datos que anotar y que escribir, menos ruido y, en bases enormes, menos cómputo. "
                "En este ejemplo casi no se nota, pero igual debemos **justificar** la elección.\n\n"
                "Después de revisar las 6 columnas, estas son las **3 que usaremos**:\n\n"
                "| Columna | Qué mide |\n|---|---|\n"
                + "\n".join(f"| `{COLS[i]}` | {QUE_MIDE[COLS[i]]} |" for i in SENSATO) + "\n\n"
                "Quedan fuera: " + ", ".join(f"`{COLS[i]}`" for i in range(6) if i not in SENSATO) + ".\n\n"
                "Así queda la tabla con las 3 columnas elegidas (de aquí vas a copiar los datos):\n\n"
                + tabla_md(COLS, TABLA, ETIQ, ocultar=tuple(i for i in range(6) if i not in SENSATO)) + "\n\n"
                + idea("el modelo no necesita todas las columnas: usamos las que podrían explicar la etiqueta y dejamos fuera las que no, y lo justificamos.") + "\n\n"
                "✍️ **Escribe tu justificación** (no es código): ¿por qué esas 3 sí y las otras 3 no?"))
    c.append(md("**Mi justificación:**\n\nElegimos ___ porque ...\n\nDejamos fuera ___ porque ..."))

    c.append(md("### 💡 2. Una fila es una lista\n\n"
                "Una fila de la tabla se escribe como una **lista**: los datos van entre corchetes y cada **coma** separa una columna. "
                "Por ejemplo, la **fila 1** (71 dispositivos conectados, 0 estudiantes viendo video y 20 horas desde el reinicio) se escribe `[71, 0, 20]`. "
                "El **orden** importa: la primera posición siempre es `dispositivos_conectados`, la segunda `estudiantes_viendo_video` y la tercera `horas_desde_reinicio`, en todas las filas.\n\n"
                + idea("una fila se escribe `[dato1, dato2, dato3]`: cada coma separa una columna y el **orden** es siempre el mismo.") + "\n\n"
                + escribelo("escribe la **fila 2** como una lista con las 3 columnas, en ese orden, y guárdala en una variable llamada `fila_2`.")))
    c.append(codigo("# Fila 2: dispositivos_conectados, estudiantes_viendo_video, horas_desde_reinicio\nfila_2 = [ ]"))

    c.append(md("### 💡 3. La tabla: filas separadas por coma, dentro de otro corchete\n\n"
                "Para armar la tabla, se **separan las filas con comas** y se **envuelven en otro par de corchetes**: una lista de filas. "
                "Las **etiquetas** van en su propia lista, **en el mismo orden** que las filas: la primera etiqueta responde «¿se cayó el wifi?» para la primera fila "
                "(`1` = sí, `0` = no), y así.\n\n"
                + idea("la tabla es varias filas separadas por coma y envueltas en otro corchete; las etiquetas (1 = sí, 0 = no) van en otra lista, en el mismo orden.") + "\n\n"
                + escribelo("completa `entradas_train` con las **primeras 16 filas** (una fila por línea) y escribe `etiquetas_train` con sus 16 resultados, en el mismo orden.")))
    c.append(codigo("# Las primeras 16 filas, una fila por línea\n"
                    "entradas_train = [\n    [71, 0, 20],   # fila 1\n    fila_2,       # ← la fila 2 ya está lista\n    # escribe aquí las filas 3 a 16\n]\n\n"
                    "# Los 16 resultados, en el mismo orden (1 = sí se cayó, 0 = no)\n"
                    "etiquetas_train = [\n]"))

    c.append(md("### 💡 4. Las 4 filas que guardamos para probar\n\n"
                "El 80 % aprende; el 20 % se guarda aparte para saber si la computadora funciona con filas que **no vio**. "
                "Se escriben igual que las anteriores, con **las mismas 3 columnas y en el mismo orden**.\n\n"
                + idea("con el 80 % la computadora aprende (train); el 20 % lo guardamos aparte para probarla (test).") + "\n\n"
                + escribelo("escribe `entradas_test` y `etiquetas_test` con las **últimas 4 filas** (17 a 20).")))
    c.append(codigo("# Las últimas 4 filas (17 a 20), con las mismas 3 columnas\nentradas_test = [\n]\n\netiquetas_test = [\n]"))

    c.append(md("### 💡 5. La receta: crear → fit → predict\n\n"
                "Es la receta de ayer, pero ahora con **tus listas**: se entrena con `train` y se le pide `predict` sobre el `test`. "
                "Como `entradas_test` ya es una tabla, el modelo entrega **una predicción por fila**.\n\n"
                "**¿Qué es `max_depth`?** Es cuánto le dejamos **«pensar»** al computador: el máximo de preguntas sí/no seguidas que puede hacer el árbol. "
                "Podría ser cualquier número, pero **mientras menos, mejor si los resultados no cambian**, porque es menos procesamiento.\n\n"
                "**¿Y `random_state=0`?** Es una semilla: hace que a todos nos resulte el mismo árbol.\n\n"
                + idea("`max_depth` es cuánto le dejamos pensar al árbol: mientras menos, mejor, siempre que los resultados no cambien.") + "\n\n"
                + escribelo("entrena el árbol con `entradas_train` y `etiquetas_train`, y guarda en `predicciones` lo que predice para `entradas_test`.")))
    c.append(codigo("from sklearn.tree import DecisionTreeClassifier\n\n"
                    "modelo = DecisionTreeClassifier(max_depth=3, random_state=0)\n\n"
                    "# Entrena con train y predice el test\n"))
    c.append(md("<details><summary>❓ ¿Cómo cambian los resultados si variamos <code>max_depth</code>?</summary>\n\n"
                "Cambia `max_depth` a 1, 2 y 4 en la celda de arriba y vuelve a ejecutar. Con nuestras filas de entrenamiento:\n\n"
                "- Con **1** o **2** el árbol todavía se equivoca en el entrenamiento (en 2 y en 1 de las 16 filas).\n"
                "- Con **3** acierta todas las filas de entrenamiento.\n"
                "- Con **4** o más queda **igual que con 3**: no necesita más preguntas. Pensar de más no mejora nada.\n\n"
                "</details>"))

    c.append(md("### 💡 6. Revisar\n\n"
                "Al revisar hacemos dos cosas:\n\n"
                "1. **Leer el árbol:** `export_text(modelo, feature_names=nombres_variables)` muestra las preguntas que aprendió. "
                "`nombres_variables` son los nombres de las columnas (*features*), **en el mismo orden** que en tus listas.\n"
                "2. **Ver la precisión (accuracy):** `accuracy_score(etiquetas_test, predicciones)` compara las predicciones con lo que pasó de verdad: aciertos ÷ total.\n\n"
                + escribelo("escribe `nombres_variables` y muestra el árbol; luego calcula el accuracy en una variable llamada `exactitud` y muéstralo con una etiqueta clara.")))
    c.append(codigo("from sklearn.tree import export_text\nfrom sklearn.metrics import accuracy_score\n\n"
                    "# 1. Leer el árbol: los nombres van en el MISMO orden que las columnas de tus listas\nnombres_variables = [ ]\n\n"
                    "# 2. Ver la precisión: usa predicciones y etiquetas_test\n"))
    c.append(md("#### 🔍 Revisa tu trabajo\n\nEjecuta la celda: revisa que tus listas coincidan con la tabla, que los nombres estén en orden y que tu accuracy sea el esperado."))
    c.append(codigo("check_icn()"))
    c.append(md("#### ✅ Verificamos lo aprendido\n\n"
                "El colega le pregunta a dos personas del curso:\n\n"
                "- ¿Para qué guardamos 4 filas aparte?\n"
                "- ¿Qué cambia si una etiqueta queda en otra posición?"))
    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Cómo se escribe |\n|---|---|\n"
                "| Columnas elegidas | solo las que podrían explicar la etiqueta, y las justificamos |\n"
                "| Una fila | `[dato1, dato2, dato3]` |\n"
                "| La tabla | `[[...], [...], [...]]`: filas separadas por coma, dentro de otro corchete |\n"
                "| Las etiquetas | otra lista (1 = sí, 0 = no), en el mismo orden que las filas |\n"
                "| Train y test | primeras 16 filas → `entradas_train` / `etiquetas_train`; últimas 4 filas → `entradas_test` / `etiquetas_test` |\n"
                "| `max_depth` | cuánto le dejamos pensar al árbol: el menor valor que no empeora los resultados |\n"
                "| La receta | `modelo.fit(entradas_train, etiquetas_train)` → `modelo.predict(entradas_test)` |\n"
                "| Revisar | `export_text(modelo, feature_names=nombres_variables)` y `accuracy_score(etiquetas_test, predicciones)` |"))
    c.append(md("#### 🎞️ Resumen animado\n\n"
                "Para repasar la etiqueta, las columnas elegidas, cómo pasar de la tabla a las listas, el 80 / 20, `max_depth` y el accuracy, mira las slides animadas: "
                "[https://clases-ia-mario-bertero.vercel.app/clase-42b/](https://clases-ia-mario-bertero.vercel.app/clase-42b/)"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| Cambiar el orden de las columnas entre una fila y otra | El modelo aprende algo falso, sin dar error | Usar siempre las mismas columnas en el mismo orden |\n"
                "| Olvidar una etiqueta o repetirla | `ValueError`: distinta cantidad de entradas y etiquetas | Contar: una etiqueta por cada fila |\n"
                "| `modelo.predict([88, 17, 4])` | `ValueError`: `predict()` espera una tabla | Poner la fila dentro de otra lista: `[[88, 17, 4]]` |\n"
                "| `nombres_variables` en otro orden que las columnas | El árbol impreso habla de la columna equivocada | Escribir los nombres en el mismo orden que las columnas de las listas |\n"
                "| Mirar el test mientras se elige el modelo | El accuracy deja de ser una prueba de verdad | Elegir con el train y mirar el test al final |\n"
                "| Creer que 4 de 4 prueba que el modelo es bueno | Se confía con muy poca evidencia | Probar con más filas antes de confiar |"))
    return c


def ejercicio(num: str, titulo: str, narrativa: str, debe: list, pistas: list, esp: str, arranque: str,
              check: str = "", extra_md: str = "") -> list:
    rotulo = titulo if num == "guiada" else f"Ejercicio {num} — {titulo}"
    cuerpo = f"### 🎯 {rotulo}\n\n{narrativa}\n\n**El programa debe:**\n\n" \
             + "\n".join(f"- {b}" for b in debe) + "\n\n" + "\n\n".join(pistas) + "\n\n" + esp
    c = [md(cuerpo)]
    c.append(codigo(arranque))
    if extra_md:
        c.append(md(extra_md))
    if check:
        c.append(codigo(check))
    return c


def guiada() -> list:
    sal = ejecutar(SOL_G)
    tabla = tabla_md(G_NOMBRES, G["X"], G["y"])
    c = [md("---\n\n## 3️⃣ Práctica Guiada\n\n"
            "Este es **el ejercicio de la clase**: lo hacemos todos, y al final revisamos uno entre todos.")]
    c += ejercicio(
        "guiada", "El liceo vecino: ¿se caerá su wifi?",
        "El liceo vecino también quiere anticipar si su wifi se cae. Su encargada de informática anotó **10 filas** en una tabla de 5 columnas "
        "y nos pide trabajar solo con **las tres primeras**. Como son 10 filas, la computadora aprende con las **primeras 8 filas** y se prueba con las **últimas 2**. "
        "Antes de confiar, quiere que revisemos si ese resultado alcanza.\n\n" + tabla,
        ["**Escribir** las listas `entradas_train` y `etiquetas_train` (8 filas) y `entradas_test` y `etiquetas_test` (2 filas), con las tres columnas pedidas.",
         "**Entrenar** un árbol (profundidad máxima 3, semilla 0) con las 8 filas y **predecir** los 2 de prueba.",
         "**Calcular** el accuracy en una variable llamada `exactitud` y **mostrar** las predicciones, las etiquetas reales y el accuracy con una etiqueta clara.",
         "**Escribir**, en un comentario, si con solo 2 filas de prueba basta para confiar."],
        [pista(1, "una fila, una lista", "Cada fila son **tres** datos entre corchetes, en el mismo orden de las columnas; las filas van separadas por coma, dentro de otro corchete."),
         pista(2, "cada etiqueta con su fila", "La primera etiqueta es la de la primera fila. Revisa que `entradas_train` y `etiquetas_train` tengan la misma cantidad de elementos.")],
        esperado(sal), "# Tu programa\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score\n\n",
        check="check_guiada()")
    return c


def extras() -> list:
    c = [md("---\n\n## 4️⃣ Ejercicios extra\n\n"
            "Para seguir practicando en casa o si terminas antes. Cada uno trae pistas y, después, un verificador que te dice ✅ si vas bien. "
            "No tienen nota.")]
    c.append(md("### 🎯 Ejercicio 0a — Práctica directa: de la tabla a las listas\n\n"
                "Esta es la tabla de 3 filas del wifi:\n\n"
                + tabla_md(COLS[:3], E0A_TABLA, E0A_ETIQ) + "\n\n"
                "**El programa debe:**\n\n"
                "- Escribir `entradas` con las 3 filas (una lista por fila, con los tres datos en el orden de las columnas, todas dentro de otra lista).\n"
                "- Escribir `etiquetas` con sus 3 resultados, en el mismo orden.\n"
                "- Imprimir ambas listas con una etiqueta.\n\n" + esperado(ejecutar(E0A_SOL))))
    c.append(codigo("# Tu solución del Ejercicio 0a\n\n" + CENTINELA + "\n"))
    c.append(codigo("check_ej0a()"))

    c.append(md("### 🎯 Ejercicio 0b — Práctica directa: predecir una sola fila\n\n"
                "La celda de abajo ya trae un modelo entrenado.\n\n**El programa debe:**\n\n"
                "- Preguntar al modelo por **una sola** fila nueva: 88 dispositivos, 17 estudiantes viendo video y 4 horas desde el reinicio.\n"
                "- Guardar la predicción en una variable llamada `prediccion` e imprimirla con una etiqueta.\n\n"
                + esperado(ejecutar(E0B_SOL))))
    c.append(codigo("# Tu solución del Ejercicio 0b\n" + E0B_BASE + "\n\n" + CENTINELA + "\n"))
    c.append(codigo("check_ej0b()"))

    sal1 = ejecutar(E1_SOL)
    c += ejercicio(
        "1", "Biblioteca del liceo: ¿se cae la red en la biblioteca?",
        "En la biblioteca del liceo, el encargado anotó 10 filas de datos en una tabla de 4 columnas y nos pide trabajar con **las tres primeras**. "
        "Quiere saber qué tan bien un árbol predice si la red se cae, aprendiendo con las primeras 8 filas y probando con las últimas 2.\n\n"
        + tabla_md(E1_NOMBRES, E1["X"], E1["y"]),
        ["**Escribir** las cuatro listas (train de 8 filas y test de 2) con las tres columnas pedidas.",
         "**Entrenar** un árbol (profundidad máxima 3, semilla 0), **predecir** el test y guardar el accuracy en `exactitud`.",
         "**Mostrar** las predicciones y el accuracy con etiquetas claras."],
        [pista(1, "las columnas", "Son tres datos por fila: usuarios conectados, notebooks en mesas y horas desde el reinicio. La cuarta columna se deja fuera."),
         pista(2, "el orden de las filas", "Las primeras 8 filas van en `train` y las últimas 2 en `test`, en el mismo orden de la tabla.")],
        esperado(sal1), "# Tu solución del Ejercicio 1\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score\n\n" + CENTINELA + "\n",
        check="check_ej1()")

    c += ejercicio(
        "2", "Sala de computación: la etiqueta que falta",
        "El profesor de computación anotó 8 filas y escribió las listas a mano, pero al entrenar el programa se cae con un error. "
        "Alguien se saltó una etiqueta. Hay que encontrar cuál falta y arreglar la lista, sin tocar las entradas.\n\n"
        + tabla_md(E2_NOMBRES, E2_X, E2_Y),
        ["**Comparar** la tabla con la lista `etiquetas` hasta encontrar qué etiqueta falta.",
         "**Corregir** `etiquetas` para que cada etiqueta quede en la misma posición que su fila.",
         "**Ejecutar** de nuevo la celda: el modelo debe aprender sin errores."],
        [pista(1, "cuántas son", "Hay 8 filas: cuenta cuántas etiquetas tiene la lista."),
         pista(2, "dónde falta", "Recorre la tabla y tu lista a la vez; la primera posición donde no coinciden marca la etiqueta que falta.")],
        esperado("El modelo ya aprendió de 8 filas"),
        "# Tu solución del Ejercicio 2\n" + E2_BASE.replace("{ETQ}", str(E2_FALLA) + "   # ← a esta lista le falta una etiqueta"),
        check="check_ej2()")

    c += ejercicio(
        "3", "Sala de actos: ¿qué columnas conviene usar?",
        "El liceo prepara un evento en la sala de actos y quiere saber si el wifi se caerá. La tabla trae **6 columnas** y 10 filas. "
        "Un compañero ya probó con tres columnas (`temperatura_sala`, `hora_del_bloque` y `dia_del_mes`). "
        "Hay que elegir **tu propio trío con criterio**, compararlo con el de tu compañero y decidir cuál conviene.\n\n"
        + tabla_md(E3_NOMBRES, E3_X, E3_Y),
        ["**Escribir** las listas train (8 filas) y test (2 filas) con tus 3 columnas.",
         "**Calcular** tu accuracy y el del compañero con la función `evaluar(...)`, que ya viene preparada.",
         "**Explicar por escrito** cuál trío conviene y por qué; recuerda que con solo 2 filas de prueba una diferencia pequeña prueba poco."],
        [pista(1, "elegir", "Mira los nombres de las columnas: ¿cuáles podrían explicar que el wifi se caiga?"),
         pista(2, "evaluar", "`evaluar(entradas_train, etiquetas_train, entradas_test, etiquetas_test)` devuelve el accuracy; úsala con tus listas y con las del compañero.")],
        esperado("Accuracy de mi trío: …\nAccuracy del trío del compañero: …",
                 "*(Tus números dependen de las columnas que elijas.)*"),
        "# Tu solución del Ejercicio 3\n"
        "# Las listas del compañero (temperatura_sala, hora_del_bloque, dia_del_mes) ya están escritas:\n"
        + datos_split(E3_FLOJO_X[:8], E3_Y[:8], E3_FLOJO_X[8:], E3_Y[8:], E3_CMP) + "\n" + CENTINELA + "\n",
        check="check_ej3()",
        extra_md="✍️ **Mi explicación:** *¿Qué trío elegí y por qué? ¿Cuál conviene, el mío o el del compañero? ¿Alcanza el test para estar seguros?* ...")

    c += [md("### 🎯 Ejercicio 4 — Desafío: un dato mal anotado\n\n"
             "Imagina que, al pasar la tabla a listas, **un solo dato** del test se anotó mal: el primer dato de la primera fila de `entradas_test` "
             "quedó valiendo **100** en vez de su valor real. Con tu trío del Ejercicio 3, vuelve a calcular el accuracy con `evaluar` y compara.\n\n"
             "**El programa debe:**\n\n"
             "- **Cambiar** ese dato en `entradas_test`.\n"
             "- **Calcular** de nuevo tu accuracy y mostrarlo con una etiqueta.\n"
             "- **Escribir** si cambió tu conclusión y qué dice eso de probar con tan pocos filas y de revisar bien los datos.\n\n"
             + pista(1, "cambiar un dato de una lista", "`entradas_test[0][0] = 100` cambia el primer dato de la primera fila.")
             + "\n\n📤 <em>El programa imprime:</em> el accuracy de tu trío con el dato mal anotado."),
          codigo("# Tu solución del Ejercicio 4\n\n" + CENTINELA + "\n"),
          md("✍️ **Mi conclusión:** ...")]
    return c


URL_FORM = "https://forms.gle/sjRpbgmQzrpkEBsH9"
TEMA_FORM = "De la tabla a las listas"


def ticket() -> list:
    """El Colab NO trae las preguntas (se proyectan en el PPT del ticket): solo el aviso y el link al Form."""
    return [md("---\n\n## 🎫 Ticket de Salida\n\n"
               "Las preguntas **se proyectan en la tele**: no están en este cuaderno. Mira cada pregunta y **decide tu respuesta en silencio**; "
               "cuando termine la última, abre el formulario, escribe tu nombre y marca tus alternativas.\n\n"
               f"👉 **Formulario del Ticket de Salida:** [{URL_FORM}]({URL_FORM})\n\n"
               f"En «Tema de la clase de hoy» escribe: **{TEMA_FORM}**.")]


def cierre() -> list:
    return [md("---\n\n## 🎯 Cierre\n\n**Objetivo de la clase**\n\n" + OBJETIVO + "\n\n"
               "---\n\n**Reflexiona antes de irte** (las comentamos a viva voz):\n\n"
               "1. ¿Qué tan seguro/a te sientes pasando una tabla a listas y entrenando y evaluando un modelo, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. ¿En qué momento de hoy tuvimos que **poner atención** para no cambiar un dato de lugar?\n\n"
               "3. ¿Qué parte del orden de los datos revisamos con cuidado y cuál habríamos dejado pasar?\n\n"
               "👀 **Lo que viene:** mañana usamos la misma receta con otro modelo: una **neurona**."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. \n\n3. "),
            md("---")]


def clase() -> list:
    return celdas_inicio() + icn_clase() + guiada() + ticket() + cierre() + extras()


# ───────────────────────── solucionario ─────────────────────────


def bloque_sol(titulo: str, cod: str, nota: str = "") -> list:
    salida = ejecutar(cod)
    out = "\n\n**Salida:**\n\n```text\n" + salida + "\n```"
    return [md(f"### {titulo}{out}" + (f"\n\n{nota}" if nota else "")), codigo(cod)]


def solucionario() -> list:
    c = [md("# Clase 42b — De la tabla a las listas · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Todas las celdas se ejecutan de arriba hacia abajo (scikit-learn, sin archivos)."),
         md("## ⚙️ Celda preparada del verificador\n\nLa misma que ven los estudiantes; los `check_*()` de abajo se ejecutan con las soluciones para comprobar que dan ✅."),
         codigo(CELDA_VERIFICADOR)]

    c.append(md("## 🧠 Haz Ahora\n\nSin código ni respuesta única: el colega hace de encargado de informática y el curso piensa en voz alta. "
                "Esperable: dispositivos conectados, estudiantes viendo video y horas desde el reinicio como las claras; "
                "temperatura de la sala y hora del bloque como posibles; el día del mes como la que no tiene nada que ver (se puede comprobar viendo si "
                "cambiarla cambia el resultado). **Etiqueta (pregunta 3):** el encargado pregunta «¿se cayó el wifi?» y la respuesta se presenta como un número: "
                "**1 = sí, 0 = no** (el 1 significa «sí», no «bueno»). Si el curso propone otra codificación, se aclara que da lo mismo mientras sea binaria y consistente. "
                "Filas a guardar para probar: la idea es llegar a «unos pocos, sin mostrarlos al modelo»; el diagrama fija 4 de 20 (20 %). "
                "**Tras el Haz Ahora, la clase fija las 3 columnas** (dispositivos, video, horas) y se compara con lo que propuso el curso; si eligieron otras (p. ej. temperatura), "
                "se dice que la tabla de comparación de más abajo muestra por qué conviene este trío."))

    c.append(md("## 📘 ICN — código completo (cada ejemplo es autocontenido)\n\n"
                "Trío sensato: `dispositivos_conectados`, `estudiantes_viendo_video`, `horas_desde_reinicio`. "
                "Con ese trío el árbol acierta **4 de 4** en el test; ver la tabla comparativa más abajo."))
    for nombre, cod, nota in [
        ("Concepto 1 · Elegir las 3 columnas (justificación modelo)", SOL_C1,
         "La clase ya trae las 3 columnas elegidas; el estudiante solo escribe la justificación. Criterio: nombra las 3 columnas y da una razón para cada grupo "
         "(las 3 que sí cargan o desgastan la red; las otras 3 no). Ahorro de procesamiento: menos datos que anotar y escribir, menos ruido y, en bases enormes, menos cómputo."),
        ("Concepto 2 · Una fila es una lista (fila 2)", SOL_C2, ""),
        ("Concepto 3 · La tabla de entrenamiento (16 filas)", SOL_C3, ""),
        ("Concepto 4 · Los 4 filas de prueba", SOL_C4, ""),
        ("Concepto 5 · La receta: crear → fit → predict", SOL_C5,
         "`max_depth` = cuánto le dejamos «pensar» al árbol. Verificado con estos datos (entrenamiento): profundidad 1 → se equivoca en 2 de 16; 2 → 1 de 16; "
         "3 → 0 de 16; 4 o más → el árbol queda igual que con 3 (profundidad real 3). Por eso 3 es el menor valor que acierta todo el entrenamiento."),
        ("Concepto 6 · Revisar: leer el árbol y accuracy", SOL_C6,
         "Lectura del árbol: la primera pregunta es `estudiantes_viendo_video <= 4,5`; si no (más de 4,5 estudiantes viendo video), predice 1 (sí se cae). "
         "Si sí, mira `horas_desde_reinicio <= 15,5`: con pocas horas desde el reinicio predice 0; con más, mira `dispositivos_conectados <= 65` (0) o más (1). "
         "Las **features** son las 3 columnas que le dimos; los nombres deben ir en el mismo orden que las columnas de las listas. "
         "Accuracy 4 de 4 = 1,0: el colega puede preguntar si eso basta para confiar (no basta: son solo 4 filas)."),
    ]:
        c += bloque_sol(nombre, cod, nota)
    c.append(codigo("check_icn()"))

    c.append(md("### 📊 Comparación de tríos (verificado con scikit-learn 1.9, profundidad 3, semilla 0)\n\n"
                "| Trío | Aciertos en test (de 4) | Validación cruzada |\n|---|---|---|\n"
                "| **Sensato** (dispositivos, video, horas reinicio) | **4** | **0,90** (el mejor de los 20 tríos) |\n"
                "| dispositivos, video, temperatura | 4 | 0,70 |\n"
                "| dispositivos, video, día del mes (con la columna sin relación) | 2 | 0,80 |\n"
                "| dispositivos, temperatura, día del mes | 1 | 0,55 |\n"
                "| temperatura, hora del bloque, día del mes (los tres «flojos») | 1 | 0,55 |\n\n"
                "Lectura honesta: con solo 4 filas de test, un trío con una columna floja puede sacar 4/4 igual que el sensato; lo que lo delata es la validación cruzada (que no se enseña). "
                "El árbol con las 6 columnas usa solo las 3 claras."))

    c.append(md("## 🧩 Práctica guiada — solución"))
    c += bloque_sol("Guiada · El liceo vecino", SOL_G,
                    "Columnas pedidas: las tres primeras. Con 2 filas de prueba, acertar los 2 no basta para confiar; ese es el comentario esperado. "
                    "**Revisión en vivo:** una pareja explica al frente cómo pasó cada fila de la tabla a su lista y por qué cada etiqueta queda en su posición.")
    c.append(codigo("check_guiada()"))

    c.append(md("## 🚀 Ejercicios extra — soluciones"))
    c += bloque_sol("Ejercicio 0a", E0A_SOL)
    c.append(codigo("check_ej0a()"))
    c += bloque_sol("Ejercicio 0b", E0B_SOL)
    c.append(codigo("check_ej0b()"))
    c += bloque_sol("Ejercicio 1 · Biblioteca", E1_SOL)
    c.append(codigo("check_ej1()"))
    c += bloque_sol("Ejercicio 2 · Sala de computación (la etiqueta que falta)", E2_SOL,
                    f"La lista del enunciado traía `{E2_FALLA}` (falta la 5ª etiqueta, que es `{E2_Y[4]}`). "
                    "El error al entrenar es un `ValueError` por distinta cantidad de entradas y etiquetas.")
    c.append(codigo("check_ej2()"))
    c += bloque_sol("Ejercicio 3 · Sala de actos (comparar tríos)", E3_SOL,
                    "Criterio: elige tres columnas con razones, calcula los dos accuracy y argumenta; debe notar que con 2 filas de prueba una diferencia pequeña prueba poco. "
                    "El trío sensato acierta 2 de 2 y el del compañero (`temperatura_sala`, `hora_del_bloque`, `dia_del_mes`) 0 de 2.")
    c.append(codigo("check_ej3()"))
    c += bloque_sol("Ejercicio 4 · Desafío", E4_SOL,
                    "Con el trío sensato, un solo dato mal anotado (dispositivos = 100 en la primera fila de prueba) baja el accuracy de 1,0 a 0,5. "
                    "Criterio: nota que cambió, y lo relaciona con que el test es muy chico (una sola fila pesa la mitad) y con la importancia de revisar los datos con atención.")

    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                "Respuestas correctas: **D, B, C, A**. Las preguntas **no están en el Colab de estudiantes**: se proyectan en `Ticket de Salida.pptx` y se responden en el Google Form (`" + URL_FORM + "`). Las respuestas correctas viven también en `Ticket de Salida Respuestas.json`."))
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        letras = "ABCD"
        alts = "\n".join(f"- **{letras[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}\n\n**Respuesta correcta: {TICKET_CORRECTAS[i - 1]}.** {TICKET_JUSTIFICACION[i - 1]}"))
    return c


if __name__ == "__main__":
    (AQUI / f"{NOMBRE} - Ticket de Salida Respuestas.json").write_text(json.dumps({"clase": "42b", "tema": TEMA_FORM, "respuestas": {**{f"Respuestas a ticket [{i}]": l for i, l in enumerate(TICKET_CORRECTAS, start=1)}}}, ensure_ascii=False, indent=2), encoding="utf-8")
    guardar(SALIDA_CLASE, clase())
    guardar(SALIDA_SOL, solucionario())
    print("Listo:", SALIDA_CLASE.name, "·", SALIDA_SOL.name)
