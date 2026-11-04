"""Genera 'Clase 43 - Neurona - Clase.ipynb' (estudiantes) y '... - Solucionario.ipynb' (profesor).

Fuente de verdad: este script + la Spec aprobada. No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.
Ejecutar: py -3 generar_clase.py
Los resultados esperados se calculan ejecutando las soluciones (así nunca se desfasan del código).

Diseño v2 (2026-11-04): caja lista primero, evaluador preparado (el estudiante programa la neurona, no el recorrido de
errores), set de entrenamiento y set de prueba, recordatorio puente y «el colega del profesor».
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
SALIDA_CLASE = AQUI / "Clase 43 - Neurona - Clase.ipynb"
SALIDA_SOL = AQUI / "Clase 43 - Neurona - Solucionario.ipynb"
URL_PAGINA = "https://clases-ia-mario-bertero.vercel.app/clase-43/"

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


def resumen(texto_salida: str) -> str:
    """Solo las líneas de resumen de aciertos de una salida del evaluador."""
    return "\n".join(l for l in texto_salida.splitlines() if "Aciertos en" in l)


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

# Colmenas: [temperatura, viento, lluvia]. Entrenamiento (8 días) + prueba (4 días nuevos)
DATOS = ("dias = [[24, 5, 0], [28, 10, 0], [19, 3, 0], [30, 20, 0],\n"
         "        [22, 8, 0], [26, 6, 4], [14, 4, 0], [25, 28, 0]]   # ENTRENAMIENTO: [temperatura, viento, lluvia]\n"
         "etiquetas = [1, 1, 1, 0, 1, 0, 0, 0]                        # 1 = las abejas salieron, 0 = se quedaron")
PRUEBA = ("dias_prueba = [[27, 12, 0], [18, 6, 0], [21, 10, 0], [29, 24, 0]]   # PRUEBA: días nuevos\n"
          "etiquetas_prueba = [1, 0, 1, 0]")
NEURONA = ("pesos = [1, -0.5, -2]   # importancia de temperatura, viento y lluvia\n"
           "sesgo = -13")

NEURONA_FUNC = """def neurona(dia):
    z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo
    if z >= 0:
        return 1
    return 0
"""

# Guiada: enjambre [temperatura, humedad, horas_de_sol]
G_DATOS = ("dias = [[22, 40, 8], [18, 70, 3], [25, 35, 9], [20, 80, 5], [27, 50, 10], [15, 60, 4]]   # ENTRENAMIENTO\n"
           "etiquetas = [1, 0, 1, 0, 1, 0]   # 1 = hubo enjambre\n"
           "dias_prueba = [[24, 45, 7], [19, 75, 4], [26, 55, 9]]   # PRUEBA\n"
           "etiquetas_prueba = [1, 0, 1]\n"
           "pesos = [1, -0.2, 0.5]   # importancia de temperatura, humedad y horas de sol\n"
           "sesgo = -29")
# Ej 0a
E0_DATOS = ("pesos = [2, -1]\n"
            "sesgo = -3\n"
            "dato = [4, 2]")
# Ej 1: Naltagua [temperatura, viento, nubosidad]
E1_DATOS = ("pesos = [1, -0.5, -0.25]   # importancia de temperatura, viento y nubosidad\n"
            "sesgo = -12\n"
            "dias_a_probar = [[22, 10, 20], [18, 4, 60], [25, 16, 8], [17, 4, 12], [14, 10, 40]]")
# Ej 2: cerezos [horas_de_frio, horas_de_sol, flores_abiertas]
E2_DATOS = ("pesos = [-0.5, 1, 0.25]   # importancia de horas de frío, horas de sol y flores abiertas\n"
            "sesgo = -8\n"
            "dias_a_probar = [[2, 7, 40], [6, 4, 20], [1, 8, 60], [4, 5, 36]]")
# Ej 3: miel [dias_de_flor, temperatura_media, dias_de_lluvia]
E3_DATOS = ("dias = [[6, 24, 0], [5, 20, 1], [8, 26, 0], [3, 22, 3], [7, 18, 2], [4, 25, 0], [2, 19, 1]]   # ENTRENAMIENTO\n"
            "etiquetas = [1, 0, 1, 0, 0, 1, 0]   # 1 = la cosecha alcanza para la feria\n"
            "dias_prueba = [[7, 23, 1], [3, 21, 2], [5, 26, 0]]   # PRUEBA\n"
            "etiquetas_prueba = [1, 0, 1]\n"
            "pesos = [1, 1, -1]   # importancia de días de flor, temperatura y días de lluvia\n"
            "sesgo = -30")
# Ej 4: desafío — apiario del cerro [temperatura, viento, nubosidad], 12 días con un día raro (el 10)
E4_DATOS = ("dias = [[30, 4, 20], [22, 12, 40], [26, 6, 10], [18, 8, 30], [32, 10, 60], [28, 2, 40],\n"
            "        [20, 4, 0], [15, 6, 20], [31, 8, 10], [24, 16, 50], [27, 12, 20], [29, 5, 36]]   # ENTRENAMIENTO\n"
            "etiquetas = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1]   # 1 = las abejas salieron a buscar polen\n"
            "dias_prueba = [[26, 3, 20], [19, 10, 40], [30, 14, 30], [27, 4, 30]]   # PRUEBA\n"
            "etiquetas_prueba = [1, 0, 0, 1]\n"
            "pesos = [1, -0.5, -0.25]   # importancia de temperatura, viento y nubosidad\n"
            "sesgo = -14")

CENTINELA = "# ── Escribe tu programa desde aquí ──"

# ───────────────────────── evaluador preparado (celda que el estudiante solo ejecuta) ─────────────────────────

EVALUADORES = '''
#@title 🔧 Evaluador listo — ejecuta esta celda primero (no la edites)
_PRUEBAS_VISTAS = {}


def _regla():
    print("Regla actual → pesos:", pesos, "| sesgo:", sesgo)


def _tabla(dias_, etiquetas_, nombre):
    aciertos = 0
    for i in range(len(dias_)):
        salida = neurona(dias_[i])
        error = etiquetas_[i] - salida
        if error == 0:
            aciertos = aciertos + 1
            marca = "✅"
        else:
            marca = "❌"
        print("Día", i + 1, "| datos:", dias_[i], "| salida:", salida, "| etiqueta:", etiquetas_[i], "| error:", error, marca)
    print("\\n" + nombre + ":", aciertos, "de", len(dias_), "días acertados")


def evaluar_entrenamiento():
    """Prueba la neurona con los días de ENTRENAMIENTO (dias, etiquetas). Aquí sí puedes ajustar."""
    _regla()
    _tabla(dias, etiquetas, "Aciertos en ENTRENAMIENTO")


def evaluar_prueba():
    """Prueba la neurona con los días nuevos (dias_prueba, etiquetas_prueba). Se mira UNA sola vez, al final."""
    clave = str(dias_prueba)
    _PRUEBAS_VISTAS[clave] = _PRUEBAS_VISTAS.get(clave, 0) + 1
    if _PRUEBAS_VISTAS[clave] > 1:
        print("⚠️ Ya miraste la prueba antes. Si cambias los pesos mirándola, la prueba deja de ser prueba: ajusta solo con el entrenamiento.\\n")
    _regla()
    _tabla(dias_prueba, etiquetas_prueba, "Aciertos en PRUEBA (días nuevos)")


print("Evaluador listo ✅")
'''

# ───────────────────────── soluciones (se ejecutan para obtener los resultados esperados) ─────────────────────────

SOL_ICN0 = EVALUADORES + "\n" + DATOS + "\n" + PRUEBA + "\n\n" + NEURONA + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()"

SOL_ICN1 = DATOS + "\n" + NEURONA + """

dia = dias[0]
z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2]
print("Suma ponderada z:", z)"""

SOL_ICN2 = SOL_ICN1 + """
z = z + sesgo
print("z con el sesgo:", z)"""

SOL_ICN3 = SOL_ICN2 + """
if z >= 0:
    salida = 1
else:
    salida = 0
print("Salida de la neurona (1 = salen, 0 = se quedan):", salida)"""

SOL_ICN4_ENTRENAMIENTO = EVALUADORES + "\n" + DATOS + "\n" + PRUEBA + "\n\n" + NEURONA + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()"
SOL_ICN4_AJUSTADA = (EVALUADORES + "\n" + DATOS + "\n" + PRUEBA
                     + "\n\npesos = [1, -1, -2]   # el viento ahora pesa más\nsesgo = -13\n\n" + NEURONA_FUNC
                     + "\nevaluar_entrenamiento()\nprint()\nevaluar_prueba()")

SOL_G_INICIAL = EVALUADORES + "\n" + G_DATOS + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()"
SOL_G = (EVALUADORES + "\n" + G_DATOS.replace("pesos = [1, -0.2, 0.5]   # importancia de temperatura, humedad y horas de sol",
                                               "pesos = [1, -0.2, 2]   # horas de sol: de 0.5 a 2")
         + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()\nprint()\nevaluar_prueba()\n\n"
         "# Mi explicación: con horas de sol en 0.5 la neurona casi no las tomaba en cuenta y se quedaba sin enjambre en los\n"
         "# 3 días soleados. Al subir ese peso a 2, el sol empuja z hacia arriba justo en esos días: acierta los 6 del\n"
         "# entrenamiento y también los 3 días nuevos de la prueba.")

SOL_E0 = E0_DATOS + """

z = dato[0] * pesos[0] + dato[1] * pesos[1] + sesgo
if z >= 0:
    salida = 1
else:
    salida = 0
print("Salida de la neurona:", salida)"""

SOL_E1 = E1_DATOS + """

def neurona(dia):
    z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo
    if z >= 0:
        return 1
    return 0

for i in range(len(dias_a_probar)):
    print("Día", i + 1, "→ salida:", neurona(dias_a_probar[i]))"""

SOL_E2 = E2_DATOS + """

def neurona(dia):
    z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo
    if z >= 0:
        return 1
    return 0

for dia in dias_a_probar:
    z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo
    print("Día", dia, "| z:", z, "| salida:", neurona(dia))"""

SOL_E3_INICIAL = EVALUADORES + "\n" + E3_DATOS + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()"
SOL_E3_PASO1 = (EVALUADORES + "\n" + E3_DATOS.replace("pesos = [1, 1, -1]", "pesos = [2, 1, -1]")
                + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()")
SOL_E3 = (EVALUADORES + "\n" + E3_DATOS.replace("pesos = [1, 1, -1]", "pesos = [2, 1, -3]")
          + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()\nprint()\nevaluar_prueba()")

SOL_E4_INICIAL = EVALUADORES + "\n" + E4_DATOS + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()\nprint()\nevaluar_prueba()"
SOL_E4 = (EVALUADORES + "\n" + E4_DATOS.replace("pesos = [1, -0.5, -0.25]", "pesos = [1, -1, -0.25]")
          + "\n\n" + NEURONA_FUNC + "\nevaluar_entrenamiento()\nprint()\nevaluar_prueba()")

# ───────────────────────── ticket y autochequeos ─────────────────────────

TICKET_CORRECTAS = ["B", "D", "A", "C"]
TICKET_JUSTIFICACION = [
    "z = 20·1 + 6·(−0,5) + 1·(−2) + (−13) = 20 − 3 − 2 − 13 = 2. Quien olvida el sesgo obtiene 15, y quien suma los datos sin pesos obtiene 14.",
    "Con z = −0,5 la condición z >= 0 es falsa, así que sale 0; con z = 0 la condición es verdadera (incluye el 0), así que sale 1.",
    "Con un peso más negativo, cada km/h de viento resta más: z baja en los días ventosos y es más probable que las abejas se queden.",
    "Acertar en el entrenamiento no garantiza acertar con días que la neurona nunca vio: por eso se evalúa en una prueba aparte y no se ajustan los pesos mirándola.",
]
TICKET_PISTAS = [
    "Calcula paso a paso: multiplica cada dato por SU peso, súmalos y recién al final suma el sesgo.",
    "Lee la condición del if con atención: ¿incluye el caso en que z vale exactamente 0?",
    "Piensa qué ocurre con z cuando el viento es alto y su peso es negativo: ¿cuánto resta ahora?",
    "Pregúntate para qué existen los días de prueba y qué pasaría si ajustaras los pesos mirándolos.",
]


def huella(i: int, letra: str) -> str:
    return hashlib.sha256(f"c43|{i}|{letra}".encode()).hexdigest()[:16]


def b64(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


CELDA_AUTOCHEQUEOS = '''
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)
import base64
import hashlib


def _referencia(dia, w, b):
    z = sum(x * p for x, p in zip(dia, w)) + b
    return 1 if z >= 0 else 0


def _probar_funcion(dias_prueba_chequeo, w, b):
    f = globals().get("neurona")
    if f is None or not callable(f):
        print("⚠️ Todavía no hay una función llamada neurona.")
        print("   Pista: defínela con def neurona(dia): y ejecuta la celda de tu solución antes del autochequeo.")
        return
    for i, dia in enumerate(dias_prueba_chequeo, start=1):
        try:
            r = f(dia)
        except Exception as e:
            print(f"⚠️ Tu función falló con el día {i} ({type(e).__name__}).")
            print("   Pista: revisa que uses los 3 datos del día y los 3 pesos.")
            return
        if r is None:
            print("⚠️ Tu función no devuelve nada.")
            print("   Pista: debe devolver (return) un 1 o un 0; no basta con imprimirlo.")
            return
        esperado_dia = _referencia(dia, w, b)
        if r != esperado_dia:
            print(f"⚠️ Con el día {i} tu neurona da {r}, pero la neurona de este ejercicio daría {esperado_dia}.")
            print("   Pista: revisa que cada dato se multiplique por SU peso, que sumes el sesgo y que el 0 cuente como «sale» (>=).")
            return
    print(f"✅ Tu neurona calcula bien los {len(dias_prueba_chequeo)} días de prueba.")
    print("   Ahora compara lo que imprimiste con el resultado esperado de arriba.")


def check_ej1():
    _probar_funcion([[22, 10, 20], [18, 4, 60], [25, 16, 8], [17, 4, 12], [14, 10, 40], [30, 2, 4], [10, 0, 0]],
                    [1, -0.5, -0.25], -12)


def check_ej2():
    _probar_funcion([[2, 7, 40], [6, 4, 20], [1, 8, 60], [4, 5, 36], [0, 3, 80], [8, 9, 10]],
                    [-0.5, 1, 0.25], -8)


def _aciertos_entrenamiento(dias_e, et_e):
    p = globals().get("pesos")
    s = globals().get("sesgo")
    if p is None or s is None or len(p) != 3:
        print("⚠️ No encuentro tus pesos ni tu sesgo.")
        print("   Pista: ejecuta primero la celda de tu solución; ahí viven pesos y sesgo.")
        return None
    return sum(_referencia(d, p, s) == e for d, e in zip(dias_e, et_e))


def check_ej3():
    dias_e3 = [[6, 24, 0], [5, 20, 1], [8, 26, 0], [3, 22, 3], [7, 18, 2], [4, 25, 0], [2, 19, 1]]
    et_e3 = [1, 0, 1, 0, 0, 1, 0]
    aciertos = _aciertos_entrenamiento(dias_e3, et_e3)
    if aciertos is None:
        return
    if aciertos == len(et_e3):
        print("✅ Tu neurona acierta los 7 días del entrenamiento con los pesos que dejaste.")
        print("   Mira la prueba UNA sola vez y escribe en la celda de abajo qué cambiaste y por qué.")
    else:
        print(f"⚠️ Con los pesos que dejaste, tu neurona acierta {aciertos} de {len(et_e3)} días del entrenamiento.")
        print("   Pista: cambia UN peso a la vez, ejecuta y mira qué día se arregla… y qué día se rompe.")


def check_ej4():
    dias_e4 = [[30, 4, 20], [22, 12, 40], [26, 6, 10], [18, 8, 30], [32, 10, 60], [28, 2, 40],
               [20, 4, 0], [15, 6, 20], [31, 8, 10], [24, 16, 50], [27, 12, 20], [29, 5, 36]]
    et_e4 = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
    aciertos = _aciertos_entrenamiento(dias_e4, et_e4)
    if aciertos is None:
        return
    if aciertos >= 11:
        print(f"✅ Tu neurona acierta {aciertos} de 12 días del entrenamiento: es la mejor combinación que existe para estos datos.")
        print("   Ahora mira la prueba UNA vez y justifica en la celda de abajo.")
    else:
        print(f"⚠️ Con los pesos que dejaste, tu neurona acierta {aciertos} de 12 días del entrenamiento.")
        print("   Pista: existe una combinación que acierta más. Mira qué días fallan y qué dato tienen en común.")


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
        elif hashlib.sha256(f"c43|{i}|{letra}".encode()).hexdigest()[:16] == _HUELLAS[i - 1]:
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

OBJETIVO = "Crear nuestra primera inteligencia artificial: una neurona, con asombro."

HAZ_AHORA = [
    "Tú no sabes nada de abejas. ¿Qué le pedirías al apicultor para empezar a descubrir cuándo salen?",
    "Con esos registros, ¿qué patrón buscarías primero entre los días en que salen y los días en que se quedan?",
    "Si ves que «con mucho viento casi nunca salen», ¿cómo convertirías eso en un número que un programa pueda usar?",
    "¿Cómo comprobarías que tu regla funciona antes de dársela al apicultor?",
]

TICKET_PREGUNTAS = [
    ("Suma ponderada y sesgo",
     "```python\npesos = [1, -0.5, -2]\nsesgo = -13\ndia = [20, 6, 1]   # temperatura, viento, lluvia\n"
     "z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo\nprint(\"z =\", z)\n```\n\n"
     "¿Qué imprime este programa?",
     ["z = 15.0", "z = 2.0", "z = 14", "z = 28.0"]),
    ("La activación escalón",
     "```python\nif z >= 0:\n    salida = 1\nelse:\n    salida = 0\n```\n\n"
     "¿Qué salida da esta neurona con `z = -0.5` y qué salida da con `z = 0`?",
     ["Con −0,5 sale 1 y con 0 sale 1.", "Con −0,5 sale 0 y con 0 sale 0.",
      "Con −0,5 sale 1 y con 0 sale 0.", "Con −0,5 sale 0 y con 0 sale 1."]),
    ("Un peso negativo",
     "```python\npesos = [1, -0.5, -2]   # antes\npesos = [1, -2, -2]     # después (el peso del viento pasó de -0.5 a -2)\n```\n\n"
     "Con el cambio, en un día muy ventoso, ¿qué le pasa a `z`?",
     ["Baja más, así que es más probable que las abejas se queden.",
      "Sube, así que es más probable que las abejas salgan.",
      "No cambia, porque solo el sesgo mueve a `z`.",
      "La neurona deja de mirar el viento."]),
    ("Entrenamiento y prueba",
     "```text\nAciertos en ENTRENAMIENTO: 8 de 8 días acertados\nAciertos en PRUEBA (días nuevos): 2 de 4 días acertados\n```\n\n"
     "Ajustaste los pesos hasta acertar todo el entrenamiento, pero en la prueba acertó 2 de 4. ¿Qué conviene concluir?",
     ["La neurona está rota y hay que borrarla.",
      "La prueba está mal: solo cuenta el entrenamiento.",
      "Acertar en el entrenamiento no garantiza acertar con días nuevos; por eso se evalúa en una prueba aparte.",
      "Hay que seguir cambiando los pesos mirando la prueba hasta que acierte los 4."]),
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────


def imagen_diagrama() -> str:
    datos = base64.b64encode((AQUI / "diagramas" / "Diagrama - Una neurona.png").read_bytes()).decode("ascii")
    return f"![Cómo decide una neurona](data:image/png;base64,{datos})"


ARRANQUE_C1 = ("# Datos de las colmenas y neurona de partida (ya escritos)\n" + DATOS + "\n\n" + NEURONA
               + "\n\ndia = dias[0]   # [temperatura, viento, lluvia] del primer día")
ARRANQUE_C2 = ARRANQUE_C1 + ("\nz = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2]\n"
                             "print(\"Suma ponderada z:\", z)")
ARRANQUE_C3 = ARRANQUE_C2 + "\nz = z + sesgo\nprint(\"z con el sesgo:\", z)"

CELDA_DATOS = "# Datos de las colmenas (ya escritos)\n" + DATOS + "\n" + PRUEBA

CELDA_JUEGA = ("# 🎛️ Cambia los números de pesos y sesgo, ejecuta y mira cuántos días acierta\n"
               + NEURONA + "\n\n# La neurona ya viene escrita (adentro de la caja):\n" + NEURONA_FUNC
               + "\nevaluar_entrenamiento()")

CELDA_AJUSTE = ("# 🎛️ Cambia UN peso a la vez (o el sesgo), ejecuta y observa\n"
                + NEURONA + "\n\n# Tu neurona, empaquetada en una función:\n" + NEURONA_FUNC
                + "\nevaluar_entrenamiento()")

CELDA_PRUEBA = ("# Mira la prueba UNA sola vez, con los pesos que dejaste arriba\n"
                "evaluar_prueba()")


def celdas_comunes_clase() -> list:
    c = []
    c.append(md("# 🐍 Clase 43 — Construir una neurona\n\n"
                "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab\n\n---"))
    c.append(md(f"## 🎯 Objetivo de la clase\n\n{OBJETIVO}\n\n"
                "## 🔎 ¿Por qué lo veremos?\n\n"
                "🎙️ *Lo dice el colega del profesor:*\n\n"
                "> «Yo estoy hecha de miles de millones de piezas pequeñas llamadas neuronas. Hoy ustedes van a construir "
                "la primera, desde cero. Con ella van a poner los cimientos de lo que yo soy.»\n\n---\n\n"
                "**Lo que ya sabes:** todo lo dictado hasta N°42 (las entradas y las etiquetas, `fit()` y `predict()`) y Python hasta listas, `for` y funciones.\n\n"
                "**Lo que aprenderás hoy:** calcular la salida de una neurona con una **suma ponderada**, un **sesgo** y una **activación escalón**, "
                "y ajustar sus pesos a mano mirando el **entrenamiento** y comprobando después en una **prueba**. "
                "**Todos los datos vienen escritos en este cuaderno** (sin archivos ni descargas) y se ejecuta de arriba hacia abajo."))
    c.append(md("---\n\n## 1️⃣ Haz Ahora\n\n"
                "Un apicultor de Isla de Maipo quiere automatizar algo: que un programa le diga cada mañana si sus abejas saldrán a buscar néctar. "
                "Pero tú no sabes nada de abejas, y él tampoco sabe programar. Ayúdalo a pensar cómo lo harías:\n\n"
                + "\n".join(f"{i}. {p}" for i, p in enumerate(HAZ_AHORA, start=1))
                + "\n\nEl apicultor, sabiendo que programamos, nos pide ayuda — pero antes quiere que tengamos clara la lógica."))
    c.append(md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "))
    c.append(md("---\n\n### 🔁 Ayer → 🔀 Hoy → ➡️ Después\n\n"
                "- 🔁 **Ayer:** el árbol de decisión **aprendió solo** una cadena de preguntas sí/no. Nosotros solo le dimos datos.\n"
                "- 🔀 **Hoy es distinto:** la neurona no hace preguntas, hace una **suma de datos × importancia** y decide al final. "
                "Y esta vez **la regla la armamos nosotros**, moviendo pesos y sesgo para ver cómo piensa.\n"
                "- ➡️ **La próxima clase:** la computadora **aprenderá sola** esos mismos números, y compararemos con los nuestros.\n\n"
                "| | Árbol (clase 42) | Neurona (hoy) |\n|---|---|---|\n"
                "| Cómo decide | Cadena de preguntas sí/no | Suma de datos × pesos + sesgo, y un sí/no al final |\n"
                "| Quién armó la regla | La computadora (`fit`) | Nosotros, a mano |\n"
                "| Qué se puede mover | Nada a mano | Perillas: pesos y sesgo |\n\n"
                "**Árbol = preguntas · neurona = suma de importancias · la próxima clase = la computadora ajusta los números.**"))
    return c


def icn_clase() -> list:
    c = []
    c.append(md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
                "Hoy partimos al revés: **primero usamos una neurona ya armada** (una «caja lista») y moviendo sus números vemos cómo cambia. "
                "Después **abrimos la caja** y escribimos tú las piezas que tiene adentro."))
    c.append(md("### 🧰 Paso 0 · Los datos y la caja lista\n\n"
                "El apicultor anotó **12 días** de sus colmenas. Cada día es una lista `[temperatura, viento, lluvia]` y su etiqueta dice si las abejas salieron (`1`) o se quedaron (`0`).\n\n"
                "| Dato | Qué es | Ejemplo |\n|---|---|---|\n"
                "| `temperatura` | grados a las 9:00 | 24 |\n"
                "| `viento` | km/h | 5 |\n"
                "| `lluvia` | milímetros | 0 |\n"
                "| etiqueta | `1` = las abejas salieron · `0` = se quedaron (**lo definimos nosotros**) | 1 |\n\n"
                "Los 12 días se separan en dos grupos, y esta separación vale para **toda IA que se entrena**:\n\n"
                "- **8 días de ENTRENAMIENTO** — «aquí ajustamos»: podemos mirarlos todas las veces que queramos.\n"
                "- **4 días de PRUEBA** — «aquí vemos si es capaz de predecir» días que nunca vio. **Se miran una sola vez, al final.** "
                "Si ajustáramos los pesos mirándola, dejaría de ser una prueba.\n\n"
                + imagen_diagrama() + "\n\n"
                "Este es el esquema general de lo que vamos a construir: los datos entran, cada línea trae un **peso** (la importancia de ese dato) "
                "y la neurona decide si se **activa** (sale 1) o no (sale 0). Los números concretos los iremos viendo paso a paso."))
    c.append(codigo(CELDA_DATOS))
    c.append(codigo(EVALUADORES))
    c.append(md("🎛️ **Juega con la caja lista (3 minutos):** cambia los números de `pesos` y `sesgo`, ejecuta y mira cuántos días del **entrenamiento** acierta la neurona. "
                "Todavía no hace falta entender cómo funciona por dentro. ¿Puedes llegar a 8 de 8?\n\n"
                "> Mientras tanto, también puedes jugar en la página: "
                f"[{URL_PAGINA}]({URL_PAGINA})"))
    c.append(codigo(CELDA_JUEGA))
    c.append(md("### 💡 Ahora abrimos la caja · Suma ponderada\n\n"
                "La neurona de partida tiene un **peso** por cada dato: `pesos = [1, -0.5, -2]`. El calor suma, el viento y la lluvia restan.\n\n"
                "La suma ponderada se escribe así (con $x$ los datos y $w$ los pesos):\n\n"
                "$$z = w_1 x_1 + w_2 x_2 + w_3 x_3$$\n\n"
                + idea("cada dato se multiplica por su peso (su importancia) y se suman los resultados; un peso negativo frena.") + "\n\n"
                + escribelo("calcula `z` para el primer día multiplicando cada dato por su peso y sumando los tres resultados; muéstralo con una etiqueta clara.")))
    c.append(codigo(ARRANQUE_C1))
    c.append(md("### 💡 El sesgo\n\n"
                "Además de los pesos, una neurona tiene un **sesgo**: un número que se suma al final y que empuja a la neurona a activarse más fácil o más difícil. "
                "Aquí el sesgo es `-13`: es como una «exigencia mínima» de ánimo para que las abejas salgan.\n\n"
                "$$z = w_1 x_1 + w_2 x_2 + w_3 x_3 + b$$\n\n"
                + idea("el sesgo es el empujón inicial: un sesgo muy negativo vuelve a la neurona exigente.") + "\n\n"
                + escribelo("suma el sesgo al valor de `z` y muestra el nuevo `z`.")))
    c.append(codigo(ARRANQUE_C2))
    c.append(md("#### 🗣️ Reto del colega\n\n"
                "Escuchamos el reto. Pistas del problema: un día con **10 °C**, sin viento ni lluvia; los demás datos valen 0.\n\n"
                "✍️ *¿Qué número tendría que ser el sesgo para que las abejas igual salgan?* ..."))
    c.append(md("### 💡 La activación escalón\n\n"
                "Falta lo más importante: **decidir**. La neurona convierte `z` en una salida de 0 o 1 con una regla sencilla llamada **escalón**:\n\n"
                "$$\\text{salida} = \\begin{cases} 1 & \\text{si } z \\ge 0 \\\\ 0 & \\text{si } z < 0 \\end{cases}$$\n\n"
                + idea("la salida es una decisión: 1 si `z` llega a 0 o más, 0 si no; el 0 cuenta como «se activa».") + "\n\n"
                + escribelo("convierte `z` en la salida de la neurona (1 o 0) y muéstrala con una etiqueta clara.")))
    c.append(codigo(ARRANQUE_C3))
    c.append(md("#### 🎞️ Lo que acabamos de hacer, paso a paso\n\n"
                "Mira cómo entra un día, cómo se multiplica por cada peso, se suma el sesgo y se activa (o no) la salida: "
                f"[{URL_PAGINA}]({URL_PAGINA})"))
    c.append(md("#### 🗣️ Reto del colega\n\n"
                "Escuchamos el reto. Pista: puedes probarlo en el laboratorio de la página o cambiando `pesos` en la caja lista.\n\n"
                "✍️ *Si el peso del viento pasa a 0, ¿qué días cambian de salida?* ..."))
    c.append(md("### 🎛️ Ajusta tú: encuentra tu mejor neurona\n\n"
                "Ya sabes lo que hay adentro de la caja. Ahora la neurona viene empaquetada en una función `neurona(dia)` y el evaluador compara su salida con la etiqueta:\n\n"
                "$$\\text{error} = \\text{etiqueta} - \\text{salida}$$\n\n"
                "Error 0 es acierto (✅); error 1 o −1 es fallo (❌). **Cambia UN peso (o el sesgo) a la vez**, ejecuta de nuevo y mira si mejora: así «aprende» una neurona.\n\n"
                + idea("error 0 es acierto; si falla, cambiamos un peso, probamos otra vez y vemos si mejora.") + "\n\n"
                "🎯 **Tu meta:** el mejor resultado que logres en el **entrenamiento**, sin mirar la prueba todavía."))
    c.append(codigo(CELDA_AJUSTE))
    c.append(md("✍️ **Justifica tu mejor resultado** *(completa con tus datos)*:\n\n"
                "*Cambié ___ de ___ a ___. Con eso, la neurona acertó ___ de 8 días del entrenamiento. Lo hizo porque ___.*\n\n"
                "...\n\n"
                "#### 🗣️ Reto del colega\n\n"
                "Escuchamos el último reto sobre cuál peso hizo el trabajo.\n\n"
                "✍️ *¿Cómo puedo saber cuál de dos cambios fue el que ayudó?* ..."))
    c.append(md("### 🧪 Ahora sí: la prueba (una sola vez)\n\n"
                "Con los pesos que dejaste, mira cómo le va a tu neurona con **4 días que nunca vio**. No cambies los pesos después de mirarla."))
    c.append(codigo(CELDA_PRUEBA))
    c.append(md("✍️ **Compara entrenamiento y prueba:** *¿Acertó igual en los días nuevos que en el entrenamiento? ¿Por qué crees que pasó eso?* ..."))
    c.append(md(f"#### 🧪 Laboratorio en vivo\n\n"
                f"Juega con la misma neurona (con entrenamiento y prueba separados) en la página: [{URL_PAGINA}]({URL_PAGINA})"))
    c.append(md("#### ✅ Verificamos lo aprendido\n\n"
                "El colega le pregunta a dos personas del curso:\n\n"
                "- ¿Qué hace el sesgo en una neurona?\n"
                "- ¿Para qué sirven los días de prueba, y por qué no hay que mirarlos mientras ajustamos?"))
    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Ejemplo |\n|---|---|\n"
                "| Suma ponderada | `z = dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2]` |\n"
                "| Sesgo | `z = z + sesgo` |\n"
                "| Activación escalón | `if z >= 0: salida = 1  else: salida = 0` |\n"
                "| Error y ajuste | `error = etiqueta - salida`; cambiar **un** peso a la vez mirando el **entrenamiento** |\n"
                "| Prueba | Se mira **una sola vez**, al final, con días que la neurona no vio |"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| Olvidar el sesgo | `z` queda más alto de lo que debería y la neurona se activa de más | Sumar `sesgo` antes de decidir |\n"
                "| Cambiar el signo de un peso (el viento sumando) | La neurona piensa que más viento ayuda a que salgan | El calor suma; el viento y la lluvia restan |\n"
                "| Usar `>` en lugar de `>=` | Un día con `z` exactamente 0 se apaga | Si 0 debe activarse, usar `z >= 0` |\n"
                "| Cambiar varios pesos a la vez | No se sabe cuál cambio ayudó | Cambiar **un** peso, ejecutar, observar y recién ahí el siguiente |\n"
                "| Ajustar los pesos mirando la prueba | La prueba deja de medir días nuevos y el resultado engaña | Ajustar solo con el entrenamiento; mirar la prueba una vez al final |"))
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
    ini = resumen(ejecutar(SOL_G_INICIAL))
    fin = resumen(ejecutar(SOL_G))
    c = [md("---\n\n## 3️⃣ Práctica Guiada")]
    c += ejercicio(
        "guiada", "¿Habrá enjambre?",
        "Cuando una colmena se llena, parte de las abejas se va a formar un enjambre nuevo, y el apicultor quiere anticiparse para no perderlas. "
        "Anotó 6 días de entrenamiento con la temperatura, la humedad y las horas de sol, y 3 días nuevos de prueba; marcó 1 si hubo enjambre. "
        "Armó una neurona con unos pesos de partida, pero sospecha que le está dando poca importancia a algo. Quiere que la pongan a prueba y la corrijan.",
        ["**Escribir** la función `neurona(dia)` (suma ponderada, sesgo y escalón) y **evaluarla** con el entrenamiento.",
         "**Cambiar un peso a la vez** en los datos de partida hasta acertar los 6 días del entrenamiento.",
         "**Mirar la prueba una sola vez**, con los pesos que dejaste.",
         "**Escribir**, en un comentario, qué peso cambiaste, por qué arregló la neurona y si acertó igual en la prueba."],
        [pista(1, "la función", "Es la misma neurona de la clase: `dia[0] * pesos[0] + dia[1] * pesos[1] + dia[2] * pesos[2] + sesgo` y un `if z >= 0`."),
         pista(2, "qué peso cambiar", "Fíjate en qué días falla: ¿tienen algo en común? Los días que se le escapan, ¿qué dato tienen alto?")],
        esperado(ini + "\n…tras ajustar un peso…\n" + fin,
                 "*(Las primeras líneas son lo que imprime con los pesos de partida; las siguientes, después de ajustar el peso correcto.)*"),
        G_DATOS)
    return c


def independiente() -> list:
    c = [md("---\n\n## 4️⃣ Práctica Independiente\n\n"
            "Resuelve los siguientes ejercicios. Cada uno trae sus propios datos escritos y pistas. "
            "Después de cada uno hay un autochequeo que dice ✅ si tu neurona calcula bien; "
            "**ejecuta primero la celda de tu solución** y luego el autochequeo. Busca tu función en el nombre `neurona`. "
            "Recuerda: el evaluador de la caja lista (`evaluar_entrenamiento()` y `evaluar_prueba()`) sirve en los ejercicios con entrenamiento y prueba."),
         codigo(CELDA_AUTOCHEQUEOS)]
    c.append(md("### 🎯 Ejercicio 0a — Práctica directa: una neurona de 2 entradas\n\n"
                "Aplica la neurona completa con solo dos datos:\n\n"
                "**El programa debe:**\n\n"
                "- Calcular `z` como la suma ponderada de `dato` y `pesos`, más el `sesgo`.\n"
                "- Convertir `z` en la salida de la neurona con la activación escalón (1 si `z >= 0`, si no 0) y guardarla en una variable.\n"
                "- Imprimir la salida con una etiqueta.\n\n"
                + esperado(ejecutar(SOL_E0))))
    c.append(codigo(f"# Tu solución del Ejercicio 0a\n{E0_DATOS}\n\n{CENTINELA}\n"))

    c += ejercicio(
        "1", "Naltagua: ¿sale hoy el otro apiario?",
        "Una vecina de Naltagua tiene su propio apiario y quiere la misma ayuda que el apicultor de Isla de Maipo. "
        "Sus datos son la temperatura, el viento y el porcentaje de cielo nublado, y ya tiene unos pesos que le funcionan. "
        "Quiere saber qué dirá la neurona en cinco mañanas que anotó.",
        ["**Escribir** una función `neurona(dia)` que devuelva 1 o 0 con la suma ponderada, el sesgo y el escalón.",
         "**Probarla** con los 5 días y mostrar la salida de cada uno con su número de día."],
        [pista(1, "devolver, no imprimir", "La función termina con `return 1` o `return 0`; lo que se imprime es el resultado de llamarla."),
         pista(2, "el día que vale cero", "Hay días en que `z` queda exactamente en 0; en ese caso la neurona debe activarse.")],
        esperado(ejecutar(SOL_E1)), E1_DATOS, check="check_ej1()")

    c += ejercicio(
        "2", "Cerezos en flor: ¿conviene llevar las colmenas?",
        "Un productor de cerezos de Isla de Maipo arrienda colmenas para polinizar. Quiere llevarlas solo los días en que valga la pena, "
        "según las horas de frío de la noche, las horas de sol y el porcentaje de flores abiertas. "
        "Tiene los pesos y quiere ver, para cuatro días, el valor de `z` y la decisión de la neurona.",
        ["**Escribir** la función `neurona(dia)` con estos tres datos.",
         "**Recorrer** los 4 días con un `for` y mostrar para cada uno su `z` y la salida de la neurona."],
        [pista(1, "dos usos del mismo cálculo", "Para mostrar `z` hay que calcularlo en el `for`; la función te da solo el 1 o el 0."),
         pista(2, "pesos con decimales", "Un peso puede ser `0.25` o `-0.5`: se multiplica igual que cualquier otro número.")],
        esperado(ejecutar(SOL_E2)), E2_DATOS, check="check_ej2()")

    ini = resumen(ejecutar(SOL_E3_INICIAL))
    fin = resumen(ejecutar(SOL_E3))
    c += ejercicio(
        "3", "Miel para la feria de la Casona del Maipo",
        "Una apicultora vende miel en la feria de la Casona del Maipo y quiere saber si la cosecha le alcanzará. "
        "Anotó 7 semanas de entrenamiento y 3 semanas nuevas de prueba, con los días de flor, la temperatura media y los días de lluvia, y marcó 1 si la cosecha alcanzó. "
        "Su neurona de partida se equivoca en alguna semana: tiene que ajustarla, de a un peso a la vez, y explicar qué descubrió.",
        ["**Escribir** la función de la neurona y **evaluarla** con el entrenamiento.",
         "**Cambiar un peso a la vez**, ejecutando cada vez, hasta que la neurona acierte las 7 semanas del entrenamiento.",
         "**Mirar la prueba una sola vez**, con los pesos que dejaste.",
         "**Explicar por escrito**, en la celda de abajo, qué pesos cambiaste, en qué orden, qué pasó con cada cambio y cómo le fue en la prueba."],
        [pista(1, "el primer fallo", "Revisa qué semana falla y qué dato tiene alto; ¿qué peso lo estaba subestimando?"),
         pista(2, "un arreglo que rompe otro día", "A veces arreglar una semana hace fallar otra: eso es normal. Mira qué semana se rompió y qué otro peso la protege.")],
        esperado(ini + "\n…tras ajustar los pesos…\n" + fin,
                 "*(Ajustes razonables pueden ser otros: lo importante es el resultado final y tu explicación.)*"),
        E3_DATOS, check="check_ej3()",
        extra_md="✍️ **Mi explicación:** *¿Qué pesos cambié y en qué orden? ¿Qué día se arregló y cuál se rompió? ¿Por qué creo que pasó eso? ¿Cómo me fue en la prueba?* ...")

    ini4 = resumen(ejecutar(SOL_E4_INICIAL))
    fin4 = resumen(ejecutar(SOL_E4))
    c += [md("### 🎯 Ejercicio 4 — Desafío: la mejor neurona del apiario del cerro\n\n"
             "En un apiario del cerro, un apicultor anotó 12 días de entrenamiento (temperatura, viento y nubosidad) y 4 días nuevos de prueba, "
             "y marcó 1 si las abejas salieron a buscar polen. Hay un día **raro**: las abejas salieron aunque todo indicaba lo contrario. "
             "Tu desafío es encontrar **la mejor combinación de pesos y sesgo** que puedas con el entrenamiento, y después ver cómo le va en la prueba.\n\n"
             "**El programa debe:**\n\n"
             "- **Cambiar** los pesos y el sesgo (de a uno) hasta lograr la mejor cantidad de aciertos en el **entrenamiento**.\n"
             "- **Mirar la prueba una sola vez**, con la combinación final.\n"
             "- **Escribir**, en la celda de abajo, qué combinación elegiste, si crees que se puede acertar los 12 días y cómo te fue en la prueba.\n\n"
             + pista(1, "el día raro", "Si un día no calza con ninguna combinación, quizás no vale la pena forzar la neurona por él: ¿cuántos aciertos es razonable esperar?")
             + "\n\n" + esperado(ini4 + "\n…con una buena combinación…\n" + fin4)),
          codigo(f"# Tu solución del Ejercicio 4\n{E4_DATOS}\n\n# La neurona ya viene escrita (no la cambies):\n{NEURONA_FUNC}\n"
                 f"evaluar_entrenamiento()\n"),
          md("✍️ **Mi combinación:** *¿Qué pesos y sesgo elegí? ¿Se puede acertar los 12 días? ¿Cómo me fue en la prueba y por qué creo que pasó eso?* ..."),
          codigo("check_ej4()\n# Cuando termines el entrenamiento, mira la prueba UNA vez:\n# evaluar_prueba()")]
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
               f"**Objetivo de la clase**\n\n{OBJETIVO}\n\n"
               "---\n\n**Reflexiona antes de irte** (las comentamos a viva voz):\n\n"
               "1. ¿Qué tan seguro/a te sientes calculando la salida de una neurona y ajustando sus pesos, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. Una neurona es una suma, un número y un `if`, y el colega que nos acompañó está hecho de piezas así. ¿Qué fue lo que más te sorprendió de que algo tan simple esté detrás de una IA?\n\n"
               "3. ¿En qué se nos notó hoy el asombro?\n\n"
               "👀 **La próxima clase:** la computadora **aprenderá sola** esos números, y veremos cómo le va comparada con tu neurona."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. \n\n3. "),
            md("---")]


def clase() -> list:
    return celdas_comunes_clase() + icn_clase() + guiada() + independiente() + ticket() + cierre()


# ───────────────────────── solucionario ─────────────────────────


def bloque_sol(titulo: str, cod: str, nota: str = "") -> list:
    """Solución: celda de código ejecutable + salida real incrustada como texto."""
    salida = ejecutar(cod)
    out = "\n\n**Salida:**\n\n```text\n" + salida + "\n```"
    return [md(f"### {titulo}{out}" + (f"\n\n{nota}" if nota else "")), codigo(cod)]


def solucionario() -> list:
    c = [md("# Clase 43 — Construir una neurona · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Todas las celdas de este cuaderno se ejecutan de arriba hacia abajo (Python puro, sin librerías ni archivos)."),
         md("## ⚙️ Celdas preparadas\n\nLas mismas que ven los estudiantes; los `check_*()` de abajo se ejecutan con las soluciones para comprobar que dan ✅."),
         codigo(CELDA_AUTOCHEQUEOS)]

    c.append(md("## 🧠 Haz Ahora\n\nSin código ni respuesta única: el colega hace de apicultor y el curso piensa en voz alta cómo automatizar algo que no conoce. "
                "Ideas esperables: pedir **registros de días pasados** con lo que pasó (si salieron o no) y con datos del clima; buscar patrones (los días que salen vs. los que no: "
                "calor, poco viento, sin lluvia); convertir «con mucho viento casi nunca salen» en un **número** (una importancia o peso: negativo si frena); "
                "comprobar la regla con **días que no se usaron para armarla** (anticipa el set de prueba)."))

    c.append(md("## 📘 ICN — código completo (cada ejemplo es autocontenido)"))
    for nombre, cod, nota in [
        ("Paso 0 · La caja lista (pesos de partida)", SOL_ICN0,
         "Con los pesos de partida acierta 6 de 8 días del entrenamiento: falla el **día 4** (30 °C, 20 km/h de viento) y el **día 6** (26 °C, 6 km/h, 4 mm); en ambos dice «salen» y se quedaron."),
        ("Concepto 1 · Suma ponderada", SOL_ICN1, "z = 24·1 + 5·(−0,5) + 0·(−2) = 21,5."),
        ("Concepto 2 · El sesgo", SOL_ICN2, "21,5 − 13 = 8,5."),
        ("Concepto 3 · Activación escalón", SOL_ICN3, "8,5 ≥ 0, así que sale 1: las abejas salen."),
        ("Ajusta tú · después de cambiar el peso del viento a −1 (entrenamiento y prueba)", SOL_ICN4_AJUSTADA,
         "Cambiar **solo** el peso del viento (de −0,5 a −1) arregla **los dos** días que fallaban: **8 de 8 en el entrenamiento**. "
         "En la **prueba** acierta **3 de 4**: falla el día 3 (21 °C, 10 km/h), que tenía etiqueta 1. Buen momento para la conversación: "
         "acertar todo el entrenamiento no garantiza acertar días nuevos. "
         "Cambiar solo el peso de la lluvia a −3 arregla el día 6 pero no el 4 (7 de 8). "
         "Con los pesos de partida la prueba da 2 de 4."),
    ]:
        c += bloque_sol(nombre, cod, nota)

    c.append(md("### 🗣️ Retos del colega — respuestas verificadas\n\n"
                "| Reto | Respuesta |\n|---|---|\n"
                "| 1 · Sesgo para que salgan con 10 °C (sin viento ni lluvia) | Cualquier sesgo **≥ −10** (con −10, z = 0 y sale 1; con −11, z = −1 y se quedan). |\n"
                "| 2 · Peso del viento en 0 | En el entrenamiento cambian los **días 7 y 8** (pasan de 0 a 1: ahora salen con 4 km/h y 28 km/h); el día 4 ya decía «salen». |\n"
                "| 3 · ¿Cuál de dos cambios hizo el trabajo? | Cambiar **uno a la vez**: solo el viento (−1) ya acierta los 8; el de la lluvia a −3 arregla solo el día 6. |\n"))
    c.append(codigo(DATOS + """

for pesos_prueba, nombre in [([1, 0, -2], "viento = 0"), ([1, -1, -2], "viento = -1"), ([1, -0.5, -3], "lluvia = -3")]:
    salidas = []
    for d in dias:
        z = d[0] * pesos_prueba[0] + d[1] * pesos_prueba[1] + d[2] * pesos_prueba[2] - 13
        salidas.append(1 if z >= 0 else 0)
    print(nombre, "→", salidas, "| etiquetas:", etiquetas)"""))

    c.append(md("## 🧩 Práctica guiada — solución"))
    c += bloque_sol("Guiada · ¿Habrá enjambre? (peso de horas de sol: 0,5 → 2)", SOL_G,
                    "Con los pesos de partida acierta 3 de 6 del entrenamiento (se queda sin enjambre en los 3 días soleados) y 1 de 3 en la prueba. "
                    "Con horas de sol en 1,5 acierta 5 de 6; con 2 acierta los 6 y los 3 de la prueba. Un ajuste razonable puede ser otro mientras acierte los 6.")
    c.append(md("**Referencia de partida:** " + resumen(ejecutar(SOL_G_INICIAL))))

    c.append(md("## 🚀 Práctica independiente — soluciones"))
    c += bloque_sol("Ejercicio 0a", SOL_E0, "z = 4·2 + 2·(−1) − 3 = 3, así que sale 1.")
    c += bloque_sol("Ejercicio 1 · Naltagua", SOL_E1, "Dos de los días tienen `z` exactamente 0 (días 1 y 4): con `>` en lugar de `>=` fallarían.")
    c.append(codigo("check_ej1()"))
    c += bloque_sol("Ejercicio 2 · Cerezos", SOL_E2)
    c.append(codigo("check_ej2()"))
    c += bloque_sol("Ejercicio 3 · Miel (pesos finales [2, 1, −3])", SOL_E3,
                    "**Recorrido típico de ajuste:** con los pesos de partida acierta 6 de 7 del entrenamiento (falla la semana 6, con pocos días de flor) y 2 de 3 en la prueba. "
                    "Subir los días de flor a 2 arregla la semana 6 pero **rompe la semana 5** (queda en 6 de 7), porque su `z` queda justo en 0 y la neurona se activa; "
                    "bajar el peso de la lluvia a −3 corrige esa semana y deja los 7 aciertos (y 3 de 3 en la prueba). "
                    "**Criterio:** el estudiante nombra qué pesos cambió, en qué orden, reconoce que un arreglo puede romper otro día y compara entrenamiento con prueba.")
    c.append(md("**Pasos intermedios:** con `pesos = [2, 1, -1]` → " + resumen(ejecutar(SOL_E3_PASO1))))
    c.append(codigo("check_ej3()"))
    c += bloque_sol("Ejercicio 4 · Desafío (apiario del cerro) — combinación [1, −1, −0,25], sesgo −14", SOL_E4,
                    "Con los datos de partida (`[1, -0.5, -0.25]`, `-14`) acierta 10 de 12 en el entrenamiento y 3 de 4 en la prueba. "
                    "Cambiar el peso del viento a −1 llega a **11 de 12**, que es la **mejor combinación posible** en una búsqueda amplia (el día 10, raro, no se puede acertar sin romper otros), "
                    "y acierta **4 de 4** en la prueba. **Criterio:** el estudiante elige una combinación, reconoce que no se pueden acertar los 12 y justifica el resultado de la prueba. "
                    "Conversación útil: ¿lo hará mejor la computadora la próxima clase?")
    c.append(codigo("check_ej4()"))

    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                "Respuestas correctas: **B, D, A, C**. El Colab de estudiantes guarda las letras como huellas (no como texto) y la justificación codificada."))
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
