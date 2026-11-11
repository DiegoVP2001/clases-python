"""Genera 'Clase 44 - Mini LLM - Clase.ipynb' (estudiantes), '... - Solucionario.ipynb' (profesor) y el JSON del ticket.

Fuente de verdad: este script + la Spec aprobada. No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.
Ejecutar: py -3 -X utf8 generar_clase.py
Reglas de la clase (Diego): se COMPRENDEN conceptos (los estudiantes solo ejecutan celdas ya escritas);
todo es ESTOCÁSTICO (comportamiento que no se puede predecir con total exactitud: hay azar), también el modelo chiquito;
imagen única: la BOLSA DE FICHAS (probabilidad = proporción de fichas; el modelo saca una ficha al azar).
Los resultados esperados del Solucionario se calculan ejecutando el código.
"""
import contextlib
import io
import json
import random
import uuid
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
NOMBRE = "Clase 44 - Mini LLM"
SALIDA_CLASE = AQUI / f"{NOMBRE} - Clase.ipynb"
SALIDA_SOL = AQUI / f"{NOMBRE} - Solucionario.ipynb"
SALIDA_JSON = AQUI / f"{NOMBRE} - Ticket de Salida Respuestas.json"
URL_FORM = "https://forms.gle/sjRpbgmQzrpkEBsH9"
TEMA_FORM = "Mini modelo de lenguaje"
URL_SLIDES = "https://clases-ia-mario-bertero.vercel.app/clase-44/"

# ───────────────────────── utilidades de celdas ─────────────────────────


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {},
            "source": texto.strip("\n").splitlines(keepends=True)}


def codigo(texto: str) -> dict:
    return {"cell_type": "code", "id": uuid.uuid4().hex[:8], "metadata": {}, "execution_count": None,
            "outputs": [], "source": texto.strip("\n").splitlines(keepends=True)}


def pista(n: int, titulo: str, texto: str) -> str:
    return f"<details><summary>💡 Pista {n} — {titulo}</summary>\n\n{texto}\n\n</details>"


def idea(texto: str) -> str:
    return f"> **Idea clave:** {texto}"


def guardar(ruta: Path, celdas: list) -> None:
    nb = {"cells": celdas,
          "metadata": {"colab": {"provenance": []}, "kernelspec": {"display_name": "Python 3", "name": "python3"},
                       "language_info": {"name": "python"}},
          "nbformat": 4, "nbformat_minor": 5}
    ruta.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


# ───────────────────────── textos de la clase (verificados, sin empates) ─────────────────────────

TEXTO_BASE = "nos vemos en el patio . nos vemos en el patio . nos vemos en la plaza . ya llegué al casino ."
TEXTO_TAREA = "hoy toca mate . hoy toca mate . hoy hay prueba . hoy toca inglés ."
TEXTO_TICKET = "voy al kiosco . voy al kiosco . voy al baño . voy a clases ."
TEXTO_CAFETERIA = "pido pan con palta . pido pan con palta . pido pan con queso . pido jugo ."
CHAT_HAZ_AHORA = ["nos vemos en el recreo", "nos vemos en el kiosco", "llego en la micro"]


def siguientes(texto: str) -> dict:
    p = texto.split()
    t: dict = {}
    for a, b in zip(p, p[1:]):
        t.setdefault(a, Counter())[b] += 1
    return t


def pred(texto: str, palabra: str):
    c = siguientes(texto)[palabra]
    orden = c.most_common()
    assert len(orden) == 1 or orden[0][1] != orden[1][1], f"empate tras {palabra}"
    return orden[0][0], orden[0][1], sum(c.values())


assert pred(TEXTO_BASE, "en") == ("el", 2, 3) and pred(TEXTO_BASE, "nos") == ("vemos", 3, 3)
assert pred(TEXTO_BASE, "el") == ("patio", 2, 2) and "biblioteca" not in TEXTO_BASE.split()
assert len(set(TEXTO_BASE.split())) == 12
# Réplica de la Parte D de la Prueba 1: D1 = 2 de 3, D2 = 3 de 4 (proporción), D3 = palabra nunca vista
assert pred(TEXTO_TAREA, "toca") == ("mate", 2, 3) and pred(TEXTO_TAREA, "hoy") == ("toca", 3, 4)
assert "feriado" not in TEXTO_TAREA.split()
assert not ({"perro", "gato", "come", "pan", "hueso", "bebe", "agua", "pescado", "pájaro"} & set(TEXTO_TAREA.split()))
assert pred(TEXTO_TICKET, "voy") == ("al", 3, 4) and pred(TEXTO_TICKET, "al") == ("kiosco", 2, 3)
assert len(TEXTO_TICKET.split()) == 16
assert pred(TEXTO_CAFETERIA, "pido") == ("pan", 3, 4) and pred(TEXTO_CAFETERIA, "con") == ("palta", 2, 3)
assert "empanada" not in TEXTO_CAFETERIA.split()
_chat = siguientes(" . ".join(CHAT_HAZ_AHORA))
assert _chat["nos"] == Counter({"vemos": 2}) and _chat["en"] == Counter({"el": 2, "la": 1})

# ───────────────────────── celda preparada (se ejecuta primero) ─────────────────────────

HELPERS = '''
#@title 🔧 Ejecuta esta celda primero (deja listas las funciones de hoy; no hace falta editarla)
import random
from collections import Counter

# Nuestra «base de datos» de juguete: el chat del curso
texto_base = "__TEXTO_BASE__"


def _contar_siguientes(texto):
    palabras = texto.split()
    siguientes = {}
    for palabra, siguiente in zip(palabras, palabras[1:]):
        siguientes.setdefault(palabra, Counter())[siguiente] += 1
    return siguientes


def _conocidas(texto):
    return sorted(set(texto.split()))


def _sacar_ficha(tabla, conocidas, palabra):
    # Con bolsa propia: se saca una ficha al azar (más fichas = más probable).
    # Palabra que nunca vio: se saca al azar entre las palabras que sí conoce.
    if palabra in tabla:
        opciones = tabla[palabra]
        return random.choices(list(opciones), weights=list(opciones.values()))[0]
    return random.choice(conocidas)


def ver_tokens(texto):
    tokens = texto.split()
    print("Texto:", texto)
    print("Tokens (en nuestro mini modelo, cada palabra es un token):")
    print(" | ".join(tokens))
    print("Cantidad de tokens:", len(tokens))


def ver_tokens_modelos_reales():
    print("Ilustración: así podría cortar un modelo grande las palabras largas o poco comunes")
    ejemplos = [("casa", ["casa"]), ("inteligencia", ["inteli", "gencia"]), ("murciélago", ["mur", "ciél", "ago"])]
    for palabra, trozos in ejemplos:
        plural = "s" if len(trozos) > 1 else ""
        print(f"  {palabra:14s} → {' | '.join(trozos)}   ({len(trozos)} token{plural})")
    print("(Cada modelo corta a su manera: esto es solo una ilustración.)")


def mostrar_probabilidades(texto, palabra):
    tabla = _contar_siguientes(texto)
    if palabra not in tabla:
        print(f"«{palabra}» nunca apareció en el texto: no tiene bolsa propia.")
        print(f"Si le preguntamos qué viene después, el modelo saca una ficha AL AZAR entre las {len(_conocidas(texto))} palabras que sí conoce.")
        return
    total = sum(tabla[palabra].values())
    print(f"Bolsa de «{palabra}»: {total} fichas")
    for siguiente, veces in tabla[palabra].most_common():
        print(f"  «{siguiente}»: {veces} de {total} = {veces / total:.0%}")


def sacar_fichas(texto, palabra, cantidad=1):
    tabla = _contar_siguientes(texto)
    conocidas = _conocidas(texto)
    sacadas = [_sacar_ficha(tabla, conocidas, palabra) for _ in range(cantidad)]
    if palabra in tabla:
        print(f"Saqué {cantidad} ficha(s) de la bolsa de «{palabra}»:")
    else:
        print(f"«{palabra}» nunca apareció: saqué {cantidad} ficha(s) AL AZAR entre las {len(conocidas)} palabras que sí conoce:")
    print("  " + " ".join(sacadas))
    if cantidad > 1:
        conteo = Counter(sacadas)
        print("  Conteo: " + ", ".join(f"«{p}» {n}" for p, n in conteo.most_common()))


def _frase(texto, inicio, largo):
    tabla = _contar_siguientes(texto)
    conocidas = _conocidas(texto)
    frase = [inicio]
    while len(frase) < largo:
        frase.append(_sacar_ficha(tabla, conocidas, frase[-1]))
    return " ".join(frase)


def generar_frase(texto, inicio, largo=10):
    print(_frase(texto, inicio, largo))


def generar_varias(texto, inicio, largo=10, cantidad=5):
    for numero in range(1, cantidad + 1):
        print(f"{numero}: {_frase(texto, inicio, largo)}")


print("Funciones listas ✅")
'''.replace("__TEXTO_BASE__", TEXTO_BASE)


def ejecutar(texto: str, semilla: int = None) -> str:
    """Ejecuta HELPERS + el código y devuelve lo impreso (con semilla fija solo para el ejemplo del Solucionario)."""
    g: dict = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(HELPERS, g)
    salida = io.StringIO()
    if semilla is not None:
        random.seed(semilla)
    with contextlib.redirect_stdout(salida):
        exec(texto, g)
    return salida.getvalue().rstrip("\n")


# ───────────────────────── contenido compartido ─────────────────────────

OBJETIVO = ("Comprender con curiosidad cómo funciona ChatGPT: qué es un modelo de lenguaje, qué son los tokens y por qué lo que responde "
            "depende del azar y de las probabilidades con las que se entrenó.")

HAZ_AHORA = [
    "Si alguien escribe «nos», ¿qué palabra le sugerirías a continuación, y por qué?",
    "En ese chat, ¿cuántas veces aparece la palabra «en»?",
    "De esas veces, ¿cuántas veces la palabra que viene justo después es «el»?",
    "Una calculadora, ¿te da siempre el mismo resultado para 7 × 8? Y un amigo al que le pides que te recomiende una película, "
    "¿te recomienda siempre la misma? ¿Qué diferencia hay?",
]


def _bloque(*lineas: str) -> str:
    return "```text\n" + "\n".join(lineas) + "\n```\n\n"


TICKET_PREGUNTAS = [
    ("Qué es un modelo de lenguaje (concepto 1)",
     _bloque("Teclado del celular:  escribes «nos vemos en el»  →  sugiere «patio»",
             "ChatGPT:  escribes «Cuéntame un cuento sobre»  →  continúa palabra por palabra")
     + "Los dos de arriba son modelos de lenguaje (LLM). ¿Qué es un LLM?",
     ["Una base de datos con todas las respuestas escritas de antemano.",
      "Un buscador que encuentra páginas de internet con la respuesta.",
      "Un modelo que aprendió de textos a predecir la siguiente palabra y que tiene azar (es estocástico).",
      "Un programa que entiende lo que sentimos y por eso responde."]),
    ("Qué es un token (concepto 2)",
     _bloque("inteligencia  →  inteli | gencia", "murciélago    →  mur | ciél | ago")
     + "Un modelo de lenguaje parte las palabras en trozos como los de arriba. ¿Qué es un token?",
     ["Una palabra que el modelo nunca vio.",
      "Un número que mide qué tan seguro está el modelo.",
      "El texto completo con el que se entrenó el modelo.",
      "Un trozo de texto, a veces una palabra completa y a veces parte de ella, que el modelo lee como una sola pieza."]),
    ("Predecir y proporción (concepto 3)",
     _bloque(TEXTO_TICKET)
     + "Un mini modelo de lenguaje aprendió de este texto (cada `.` termina una oración). Su regla: después de una palabra, "
       "predice la que más veces la siguió. ¿Qué predice después de `voy` y con qué proporción?",
     ["`kiosco`, 2 de 4 veces.",
      "`al`, 3 de 4 veces.",
      "`a`, 1 de 4 veces.",
      "`al`, 3 de 16 veces (las 16 palabras del texto)."]),
    ("Por qué cambia la respuesta (concepto 4)",
     _bloque("Pregunta (enviada 2 veces, en conversaciones nuevas):",
             "«Recomiéndame un panorama para el fin de semana»", "",
             "Respuesta 1: «Te recomiendo ir al cine...»",
             "Respuesta 2: «Te recomiendo caminar por el parque...»")
     + "Con exactamente la misma pregunta, ChatGPT dio respuestas distintas. ¿Por qué?",
     ["Porque un modelo de lenguaje es estocástico: lo que responde depende del azar y de las probabilidades con que se entrenó.",
      "Porque ChatGPT se equivocó y una de las dos respuestas es incorrecta.",
      "Porque ChatGPT cambia de modelo cada vez que se le escribe.",
      "Porque no entendió la pregunta la primera vez."]),
]
TICKET_CORRECTAS = ["C", "D", "B", "A"]
TICKET_JUSTIFICACION = [
    "LLM significa Large Language Model: aprendió, leyendo textos, a predecir la siguiente palabra, y es estocástico (su comportamiento no se puede predecir con total exactitud: tiene azar). El teclado del celular es uno chiquito y ChatGPT uno gigante.",
    "Un token es un trozo de texto (a veces una palabra entera, a veces parte de una) que el modelo trata como una sola pieza.",
    "`voy` apareció 4 veces con algo después: `al` 3 veces y `a` 1. La proporción es 3 de 4 (el total es de las veces que apareció `voy`, no del largo del texto).",
    "Un LLM es estocástico: lo que responde es azaroso y depende de las probabilidades con que se entrenó. En cada paso saca una ficha al azar de su bolsa: la más probable sale más seguido, pero no siempre; con la misma entrada el camino puede cambiar.",
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────

VERIF = "#### ✅ Verificamos lo aprendido\n\nEl colega le pregunta a dos personas del curso:\n\n"


def celdas_inicio() -> list:
    chat = "\n".join(f"> {i}. {m}" for i, m in enumerate(CHAT_HAZ_AHORA, start=1))
    return [
        md("# 🐍 Clase 44 — Cómo funciona ChatGPT: modelo de lenguaje, tokens y azar\n\n"
           "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab\n\n---"),
        md("## 🎯 Objetivo de la clase\n\n" + OBJETIVO + "\n\n"
           "## 🔎 ¿Por qué lo veremos?\n\n"
           "> El teclado que te sugiere la siguiente palabra en WhatsApp y ChatGPT hacen lo mismo en el fondo: predecir qué palabra viene. "
           "Entender cómo lo hacen explica por qué ChatGPT puede responder distinto a la misma pregunta.\n\n---\n\n"
           "**Lo que ya sabes:** que un modelo aprende patrones de los datos (el árbol y la neurona de las clases anteriores).\n\n"
           "**Lo que aprenderás hoy:** qué es un modelo de lenguaje, qué son los tokens y cómo el azar y las probabilidades deciden lo que responde. "
           "**Hoy no programas:** solo ejecutas celdas que ya vienen escritas y lees lo que muestran. Se ejecuta **de arriba hacia abajo**."),
        md("## 🔧 Ejecuta esta celda primero\n\n"
           "Deja listas las funciones de hoy y el texto con el que trabajaremos. No necesitas entenderla ni editarla."),
        codigo(HELPERS),
        md("---\n\n## 1️⃣ Haz Ahora\n\n"
           "Quien programa el **teclado del celular** quiere que sugiera la siguiente palabra mientras escribes. "
           "Para aprender, mira este chat cortito del curso (3 mensajes):\n\n" + chat + "\n\n"
           + "\n".join(f"{i}. {p}" for i, p in enumerate(HAZ_AHORA, start=1))
           + "\n\nSabiendo que programamos, quien hace el teclado nos pide ayuda — pero antes quiere que tengamos clara la lógica."),
        md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "),
        md("---\n\n### 🔁 Ayer → 🔀 Hoy → ➡️ La próxima clase\n\n"
           "| | Qué hacemos |\n|---|---|\n"
           "| 🔁 **Ayer** | La neurona ponderaba columnas con números. |\n"
           "| 🔀 **Hoy es distinto** | Ya no hay columnas ni números: hay **texto**, y el modelo dice **la siguiente palabra** con ayuda del azar. |\n"
           "| ➡️ **La próxima clase (lunes 23, después de la Prueba 1 del jueves 19)** | Prompting: cómo pedirle bien las cosas a ChatGPT. |"),
    ]


def icn() -> list:
    c = [md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
            "Hoy trabajamos con **4 conceptos**. Cada concepto usa lo anterior, así que **ejecuta las celdas en orden**. "
            "No escribes código: **solo ejecutas y lees**. Nuestra imagen de la clase: una **bolsa de fichas**.")]

    # ── Concepto 1 ──
    c.append(md("### 💡 1. ¿Qué es un modelo de lenguaje (LLM)?\n\n"
                "- **LLM** viene del inglés **L**arge **L**anguage **M**odel: *large* = grande · *language* = lenguaje · *model* = modelo.\n"
                "- Es un modelo que aprendió, leyendo textos, a **predecir la siguiente palabra**.\n"
                "- Es **estocástico**: su comportamiento **no se puede predecir con total exactitud**; o sea, tiene **azar** 🎲.\n"
                "- El teclado del celular es un LLM **chiquito**; **ChatGPT** es uno **gigante**. **Los dos tienen azar**: "
                "lo que responden depende del azar y de las probabilidades con las que se entrenaron.\n"
                "- Hoy usamos uno de juguete que aprende de un texto cortito: nuestra **«base de datos»**.\n\n"
                + idea("un LLM (Large Language Model) aprende de textos a predecir la siguiente palabra y es estocástico: lo que responde tiene azar.") + "\n\n"
                "▶️ **Solo ejecuta** la celda: es nuestra «base de datos», el chat del curso (cada `.` termina una oración)."))
    c.append(codigo('print("Nuestra base de datos:")\nprint(texto_base)\nprint("Palabras en el texto:", len(texto_base.split()))'))
    c.append(md(VERIF + "- ¿Qué significa la sigla **LLM** y por qué decimos que es **estocástico**?\n"
                "- ¿En qué se parece el teclado del celular a ChatGPT?"))

    # ── Concepto 2 ──
    c.append(md("### 💡 2. Tokens\n\n"
                "- El modelo no lee letras ni siempre palabras completas: **parte el texto en trozos** llamados **tokens**.\n"
                "- Piensa en cada token como una **ficha**.\n"
                "- En nuestro mini modelo: **cada palabra es un token** (y el `.` también).\n"
                "- En los modelos grandes: las palabras largas o poco comunes se **cortan en varios trozos**.\n\n"
                + idea("un token es un trozo de texto (una ficha) que el modelo lee como una sola pieza.") + "\n\n"
                "▶️ **Solo ejecuta** las dos celdas."))
    c.append(codigo("ver_tokens(texto_base)"))
    c.append(codigo("ver_tokens_modelos_reales()"))
    c.append(md(VERIF + "- ¿Qué es un **token**? ¿Cuántos tokens tiene nuestra base de datos en el mini modelo?\n"
                "- En los modelos grandes, ¿un token es siempre una palabra completa?"))

    # ── Concepto 3: probabilidad y azar (bolsa de fichas) ──
    c.append(md("### 💡 3. Probabilidad y azar: la bolsa de fichas\n\n"
                "> **Las respuestas de un LLM son azarosas.** El proceso para verlo es este: el modelo guarda, para cada palabra, "
                "una **bolsa de fichas** con lo que le siguió; con esas bolsas calcula **probabilidades**; y para responder **saca una ficha al azar**. "
                "Lo vemos paso a paso con nuestro mini modelo.\n\n"
                "**① Aprender = contar**\n"
                "- Por cada palabra, el modelo arma una **bolsa**.\n"
                "- Cada vez que una palabra siguió a otra, mete una **ficha**.\n"
                "- La bolsa de `en` tiene **2 fichas `el`** y **1 ficha `la`**.\n\n"
                "**② Probabilidad = proporción de fichas**\n"
                "- `el`: 2 de 3 ≈ **67 %** · `la`: 1 de 3 ≈ **33 %**.\n"
                "- Si cambia el texto con el que se entrenó, cambian las proporciones.\n\n"
                "**③ Azar = sacar una ficha sin mirar**\n"
                "- El modelo **saca una ficha al azar** de la bolsa: `el` tiene más chances, pero **cualquiera puede salir** (`la` también).\n"
                "- Por eso es **estocástico**: lo que responde es **azaroso** y depende de las **probabilidades con las que se entrenó**.\n\n"
                "**④ Una palabra que nunca vio**\n"
                "- No tiene bolsa propia (por ejemplo `biblioteca`).\n"
                "- No se queda callado: **saca una ficha al azar entre las palabras que sí conoce**.\n"
                "- Responde cualquier cosa de lo que sí sabe decir, sin ninguna base.\n\n"
                + idea("la probabilidad es la proporción de fichas de cada palabra en la bolsa; el modelo saca una ficha al azar, así que lo que responde "
                       "depende del azar y de las probabilidades con que se entrenó (estocástico). Si nunca vio la palabra, saca al azar entre las que sí conoce.") + "\n\n"
                "▶️ **Solo ejecuta** las celdas y repite varias veces las de «sacar fichas» y «frases»: verás que **el resultado cambia**."))
    c.append(codigo('mostrar_probabilidades(texto_base, "en")'))
    c.append(md("Ahora **sacamos 10 fichas** de esa bolsa (ejecútala varias veces):"))
    c.append(codigo('sacar_fichas(texto_base, "en", 10)'))
    c.append(md("Una palabra que el modelo **nunca vio** en su texto:"))
    c.append(codigo('mostrar_probabilidades(texto_base, "biblioteca")\nsacar_fichas(texto_base, "biblioteca", 5)'))
    c.append(md("Y ahora una **frase entera**, sacando una ficha tras otra (ejecútala varias veces):"))
    c.append(codigo('generar_varias(texto_base, "nos", 10, 5)'))
    c.append(md("🤔 **Para pensar:** ¿en qué palabra se separan los caminos? ¿Por qué `en` puede llevar a `el` o a `la`, y cuál sale más seguido?"))
    c.append(md(VERIF + "- En la bolsa de `en` (2 fichas `el` y 1 ficha `la`): ¿qué probabilidad tiene cada una? ¿Por qué puede salir `la` aunque `el` sea más probable?\n"
                "- Si preguntamos por una palabra que el modelo nunca vio, ¿qué hace? ¿De qué depende lo que responde un modelo?"))

    # ── Concepto 4: evidenciarlo en la práctica ──
    c.append(md("### 💡 4. Evidenciarlo en la práctica: ChatGPT también es azaroso\n\n"
                "- Si un LLM es **estocástico**, la **misma pregunta** puede dar **respuestas distintas**.\n"
                "- Lo comprobamos con ChatGPT de verdad: lo hace el profesor en vivo.\n\n"
                "**Cómo lo evidenciamos:**\n"
                "1. El profesor envía **dos veces**, en conversaciones nuevas, este prompt: **«Explica las diferencias entre ChatGPT, Claude y Gemini.»**\n"
                "2. Observa las dos respuestas.\n"
                "3. Completa abajo qué **cambió**, qué se **mantuvo** y **por qué**, con **citas textuales** (copia la frase entre comillas) y usando la palabra «estocástico».\n\n"
                "*(Ojo: estas respuestas pueden traer datos desactualizados o erróneos sobre cada producto; no las des por verdaderas sin revisarlas.)*\n\n"
                + idea("la misma pregunta puede dar respuestas distintas porque un LLM es estocástico: lo evidenciamos comparando dos respuestas reales.")))
    c.append(md("**Cita de la respuesta 1:** \n\n**Cita de la respuesta 2:** \n\n"
                "**¿Qué cambió entre las dos respuestas?** \n\n**¿Qué se mantuvo?** \n\n"
                "**¿Por qué cambia?** *(usa la palabra «estocástico»)* "))
    c.append(md(VERIF + "- ¿Qué cambió y qué se mantuvo entre las dos respuestas de ChatGPT? ¿Cómo lo explica que sea **estocástico**?\n"
                "- ¿Por qué dos respuestas de ChatGPT a la misma pregunta pueden ser distintas?"))

    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Qué significa |\n|---|---|\n"
                "| LLM (*Large Language Model*) | modelo de lenguaje que aprendió de textos a predecir la siguiente palabra y que es **estocástico** (tiene azar) |\n"
                "| Token | un trozo de texto (una ficha) que el modelo lee como una sola pieza |\n"
                "| Bolsa y probabilidad | por cada palabra, una bolsa con fichas de lo que le siguió; probabilidad = proporción de fichas (2 de 3 ≈ 67 %) |\n"
                "| Estocástico | sistema cuyo comportamiento **no se puede predecir con total exactitud**: el modelo saca una ficha **al azar**, así que lo que responde depende del azar y de las probabilidades con que se entrenó |\n"
                "| Palabra nunca vista | no tiene bolsa propia: saca al azar entre las palabras que sí conoce |\n"
                "| Evidencia en la práctica | la misma pregunta a ChatGPT dos veces da respuestas distintas |\n"
                "| Determinístico | lo contrario: misma entrada, **siempre** la misma salida (como una calculadora) |"))
    c.append(md("#### 🎞️ Resumen animado\n\n"
                f"Para repasar los conceptos con animaciones, mira las slides: [{URL_SLIDES}]({URL_SLIDES})"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| Olvidar que el `.` también es una palabra | Se cuenta mal lo que sigue | Contar el `.` igual que cualquier palabra |\n"
                "| Dar la palabra sin la proporción | La respuesta queda incompleta | Escribir «`el`, 2 de 3 veces» |\n"
                "| Usar el largo del texto como total | La proporción sale demasiado chica | El total son las veces que apareció **esa** palabra |\n"
                "| Creer que ante una palabra nueva el modelo «no responde» | Se olvida el azar | Saca una ficha al azar entre las palabras que sí conoce |\n"
                "| Creer que ChatGPT siempre dice la palabra más probable | No se explica por qué cambia | La más probable sale más seguido, pero no siempre: es estocástico |\n"
                "| Creer que el modelo chiquito es «exacto» porque solo cuenta | Se separa «chiquito = seguro» de «gigante = azar» | Los dos son estocásticos |"))
    return c


def leer_y_responder() -> list:
    c = [md("---\n\n## 3️⃣ Práctica guiada: la siguiente palabra\n\n"
            "**No programas:** respondes **a mano**, por escrito, y después ejecutas celdas ya escritas para **comprobar** tus respuestas. "
            "Al final revisamos una respuesta entre todos.")]
    c.append(md("### 🎯 El teclado aprende del chat del horario\n\n"
                "Quien programa el teclado le mostró un chat donde el curso anota qué toca cada día. Un mini modelo de lenguaje aprendió de este texto "
                "(cada `.` termina una oración):\n\n"
                f"`{TEXTO_TAREA}`\n\n"
                "Su regla es: *después de una palabra, predice la palabra que más veces la siguió en el texto* (la ficha más grande de su bolsa).\n\n"
                "**D1.** Después de `toca`, ¿qué palabra predice y en cuántas de las veces que apareció `toca` fue esa la siguiente?\n\n"
                "**D2.** Después de `hoy`, ¿qué palabra predice y con qué **proporción**?\n\n"
                "**D3.** La palabra `feriado` **no aparece** en el texto. Si le pedimos al modelo qué viene después de `feriado`, "
                "¿puede responder usando su regla? Responde **sí** o **no** y explica en una frase por qué.\n\n"
                "**D4.** Si el modelo igual tuviera que decir una palabra después de `feriado`, ¿qué haría? ¿Sería predecible?\n\n"
                + pista(1, "contar a mano", "Subraya cada vez que aparece la palabra y anota la que viene justo después; luego cuenta cuántas veces salió cada una.") + "\n\n"
                + pista(2, "el total", "El total es cuántas veces apareció la palabra que estás mirando, **no** cuántas palabras tiene el texto.")))
    c.append(md("**Mis respuestas:**\n\nD1: \n\nD2: \n\nD3: \n\nD4: "))
    c.append(md("#### 🔍 Comprueba tus respuestas\n\nAhora **ejecuta** las celdas y compara con lo que escribiste "
                "(«N de total» es la proporción). La última saca fichas: ejecútala varias veces."))
    c.append(codigo(f'texto_tarea = "{TEXTO_TAREA}"\nprint(texto_tarea)'))
    c.append(codigo('mostrar_probabilidades(texto_tarea, "toca")'))
    c.append(codigo('mostrar_probabilidades(texto_tarea, "hoy")'))
    c.append(codigo('mostrar_probabilidades(texto_tarea, "feriado")\nsacar_fichas(texto_tarea, "feriado", 3)'))
    return c


def extras() -> list:
    c = [md("---\n\n## 4️⃣ Ejercicios extra\n\nPara seguir practicando en casa o si terminas antes. Son opcionales y no tienen nota.")]
    c.append(md("### 🎯 Ejercicio 0a — Cambia una palabra del chat\n\n"
                "Un compañero cambió el chat: en el primer mensaje escribió «en **la plaza**» en vez de «en **el patio**». "
                "Haz ese cambio en la primera oración y, **antes de ejecutar**, escribe cómo crees que cambia la bolsa de `en`.\n\n"
                + pista(1, "qué cambia", "Cuenta de nuevo lo que viene después de cada `en` en el texto modificado.") + "\n\n"
                + pista(2, "qué mirar", "Compara cuántas fichas `el` y cuántas `la` quedan en la bolsa de `en`.")))
    c.append(codigo(f'texto_modificado = "{TEXTO_BASE}"   # cambia aquí «en el patio» por «en la plaza» en la primera oración\nmostrar_probabilidades(texto_modificado, "en")'))
    c.append(md("**Mi predicción antes de ejecutar:** "))
    c.append(md("### 🎯 Ejercicio 1 — Otro chat, las mismas preguntas\n\n"
                "En la cafetería del liceo anotan los pedidos del recreo. Ejecuta las celdas y responde: "
                "(a) ¿qué predice después de `pido` y en cuántas veces?, (b) ¿con qué proporción predice después de `con`?, "
                "(c) ¿qué hace el modelo con `empanada`?\n\n"
                + pista(1, "lee la salida", "Mira «N de total» en cada celda.") + "\n\n"
                + pista(2, "palabra nueva", "Si la palabra nunca apareció, mira qué dice la salida: ¿tiene bolsa propia?")))
    c.append(codigo(f'texto_cafeteria = "{TEXTO_CAFETERIA}"\nmostrar_probabilidades(texto_cafeteria, "pido")\n'
                    'mostrar_probabilidades(texto_cafeteria, "con")\nmostrar_probabilidades(texto_cafeteria, "empanada")'))
    c.append(md("**Mis respuestas:**\n\n(a) \n\n(b) \n\n(c) "))
    c.append(md("### 🎯 Ejercicio 2 — Desafío: ¿cuántas frases distintas salen?\n\n"
                "Ejecuta la celda **3 veces**. Cada vez genera 5 frases desde `nos`. Anota **cuántas frases distintas** salieron en cada ejecución "
                "y responde: ¿es posible que salgan las 5 iguales? ¿qué te dice eso de un sistema estocástico?\n\n"
                + pista(1, "cómo contar", "Compara las frases una a una: si dos son idénticas, cuentan como una sola.") + "\n\n"
                + pista(2, "pensar en probabilidades", "Cada frase se sortea de nuevo; que las 5 coincidan es posible, pero muy poco probable.")))
    c.append(codigo('generar_varias(texto_base, "nos", 10, 5)'))
    c.append(md("**Mis respuestas:**\n\nEjecución 1: \n\nEjecución 2: \n\nEjecución 3: \n\nConclusión: "))
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
               "1. ¿Qué tan bien entendiste cómo funciona ChatGPT, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. ¿Qué te dio curiosidad de cómo funciona ChatGPT por dentro?\n\n"
               "📢 **Aviso:** el **jueves 19** es la **Prueba 1** y antes habrá un repaso.\n\n"
               "👀 **Lo que viene (lunes 23):** prompting, cómo pedirle bien las cosas a ChatGPT."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. "),
            md("---")]


def clase() -> list:
    return celdas_inicio() + icn() + leer_y_responder() + ticket() + cierre() + extras()


# ───────────────────────── solucionario ─────────────────────────

PREFIJO_TAREA = f'texto_tarea = "{TEXTO_TAREA}"\n'


def bloque_sol(titulo: str, cod: str, nota: str = "", semilla: int = None) -> list:
    out = "\n\n**Salida:**\n\n```text\n" + ejecutar(cod, semilla) + "\n```"
    return [md(f"### {titulo}{out}" + (f"\n\n{nota}" if nota else "")), codigo(cod)]


def solucionario() -> list:
    c = [md("# Clase 44 — Cómo funciona ChatGPT · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Cada bloque usa las funciones de la primera celda (sin librerías externas). "
            "Las salidas con sorteo se muestran con una semilla fija **solo como ejemplo**: en clase cada ejecución cambia."),
         md("## ⚙️ Celda preparada\n\nLa misma celda inicial que ven los estudiantes."),
         codigo(HELPERS),
         md("## 🧠 Haz Ahora\n\n"
            "Chat: «nos vemos en el recreo / nos vemos en el kiosco / llego en la micro».\n\n"
            "1. Sugeriría **`vemos`**: las dos veces que aparece «nos» la palabra siguiente es «vemos».\n"
            "2. «en» aparece **3 veces**.\n"
            "3. De esas 3 veces, **2** vienen seguidas de «el» (y 1 de «la»).\n"
            "4. La calculadora **sí** da siempre 56 (determinística); el amigo **no** recomienda siempre lo mismo (varía). Respuesta válida: «la calculadora es siempre igual; con la persona/amigo la respuesta puede cambiar». "
            "Aún no se nombran los términos: **estocástico** ya está en la definición de LLM (concepto 1) y se desarrolla en el concepto 3.\n\n"
            "**Línea de toda la clase (Diego):** el modelo chiquito y el gigante son **estocásticos** (comportamiento que no se puede predecir con total exactitud: hay azar). "
            "Lo que responde un modelo es **azaroso** y depende de las **probabilidades con que se entrenó**. Imagen única: la **bolsa de fichas** (se saca una ficha al azar; más fichas = más probable, sin garantía). "
            "«Determinístico» solo aparece como contraste con la calculadora.")]
    c.append(md("## 📘 ICN — código completo y salidas"))
    c += bloque_sol("Concepto 1 · Nuestra «base de datos»", 'print("Nuestra base de datos:")\nprint(texto_base)\nprint("Palabras en el texto:", len(texto_base.split()))',
                    "Lo esencial: **LLM = Large Language Model** (modelo de lenguaje grande): aprendió de textos a predecir la siguiente palabra y es **estocástico** (tiene azar). "
                    "El teclado es uno chiquito y ChatGPT uno gigante; los dos tienen azar.")
    c += bloque_sol("Concepto 2 · Tokens (mini modelo)", "ver_tokens(texto_base)")
    c += bloque_sol("Concepto 2 · Tokens (modelos reales, ilustración)", "ver_tokens_modelos_reales()",
                    "Es una **ilustración**: cada modelo corta a su manera y no se afirma cómo lo hace ningún producto concreto. En el mini modelo, 1 palabra = 1 token (y el `.` también).")
    c += bloque_sol("Concepto 3 · La bolsa de `en`", 'mostrar_probabilidades(texto_base, "en")',
                    "Bolsa de `en`: 2 fichas `el` y 1 ficha `la` → `el` 2 de 3 (≈ 67 %), `la` 1 de 3 (≈ 33 %). Probabilidad = proporción de fichas.")
    c += bloque_sol("Concepto 3 · Sacar 10 fichas (azar)", 'sacar_fichas(texto_base, "en", 10)',
                    "**Ejemplo con semilla fija; en clase cada ejecución varía.** `el` sale más seguido, pero `la` también puede salir, y el conteo cambia de una ejecución a otra (puede ser 7 y 3, 5 y 5, 9 y 1…): es **estocástico**. "
                    "Frase a evitar: «siempre elige la más probable».", semilla=4)
    c += bloque_sol("Concepto 3 · Palabra que nunca vio", 'mostrar_probabilidades(texto_base, "biblioteca")\nsacar_fichas(texto_base, "biblioteca", 5)',
                    "No tiene bolsa propia, pero **responde igual**: saca una ficha **al azar entre las 12 palabras que sí conoce**, sin ninguna base. "
                    "Lo que responde un modelo es azaroso y depende de con qué se entrenó (ejemplo con semilla fija).", semilla=2)
    c += bloque_sol("Concepto 3 · Generar 5 frases", 'generar_varias(texto_base, "nos", 10, 5)',
                    "**Ejemplo con semilla fija; en clase cada ejecución varía.** Los caminos se separan tras `en` (`el` 2/3 o `la` 1/3) y tras `.` (`nos` 2/3 o `ya` 1/3). "
                    "Es la misma bolsa de fichas, usada una y otra vez.", semilla=3)
    c.append(md("### 🌐 Concepto 4 · Evidenciarlo en la práctica (prompt real en vivo) — qué esperar\n\n"
                "Prompt (2 veces, conversaciones nuevas): «Explica las diferencias entre ChatGPT, Claude y Gemini». "
                "**Las respuestas las genera ChatGPT y varían**, así que no hay respuesta única. Rúbrica orientadora para las celdas de los estudiantes:\n\n"
                "| Componente | ✅ completo | ⚠️ parcial | ❌ cero |\n|---|---|---|---|\n"
                "| Qué cambió / qué se mantuvo | nombra al menos un cambio y una constante, **con cita de ambas respuestas** | nombra sin cita, o cita solo una | sin evidencia |\n"
                "| Por qué | dice que el modelo es **estocástico** (su comportamiento no se puede predecir con total exactitud, hay azar): en cada paso saca una ficha al azar según probabilidades y no siempre la misma, y el camino se acumula | «es aleatorio» sin ligarlo a la siguiente palabra | explicación incorrecta |\n\n"
                "**Aprovecha para decir:** las respuestas sobre cada producto pueden estar desactualizadas o ser erróneas; «revisar si algo es confiable» (sin nombrar las 4D). "
                "Típicamente se mantiene la estructura/idea general y cambian la redacción, el orden y los ejemplos. *(Referencia B2 de la Prueba 2.)*"))
    c.append(md("## ✅ Verificamos lo aprendido — respuestas esperadas (el colega pregunta a dos personas por concepto; 4 conceptos)\n\n"
                "| Concepto | Pregunta | Respuesta esperada |\n|---|---|---|\n"
                "| 1 · LLM | ¿Qué significa LLM y por qué es estocástico? | *Large Language Model* (modelo de lenguaje grande): aprendió de textos a predecir la siguiente palabra; es estocástico porque su comportamiento no se puede predecir con total exactitud (tiene azar). |\n"
                "| 1 · LLM | ¿En qué se parece el teclado a ChatGPT? | Los dos predicen la siguiente palabra y tienen azar; el teclado es uno chiquito y ChatGPT uno gigante. |\n"
                "| 2 · Tokens | ¿Qué es un token? ¿Cuántos tiene la base de datos? | Un trozo de texto (una ficha) que el modelo lee como una sola pieza; en el mini modelo, **23** (cada palabra y cada `.`). |\n"
                "| 2 · Tokens | En los modelos grandes, ¿un token es siempre una palabra? | No: las palabras largas o poco comunes se cortan en varios trozos. |\n"
                "| 3 · Bolsa y azar | En la bolsa de `en` (2 `el`, 1 `la`): ¿probabilidad de cada una? ¿Por qué puede salir `la`? | `el` 2 de 3 ≈ 67 %; `la` 1 de 3 ≈ 33 %. Puede salir `la` porque el modelo saca una ficha **al azar**: la más probable sale más seguido, pero no está garantizada. |\n"
                "| 3 · Bolsa y azar | Palabra nunca vista: ¿qué hace? ¿De qué depende lo que responde? | Saca una ficha al azar entre las palabras que sí conoce. Lo que responde depende del azar y de las probabilidades con que se entrenó. |\n"
                "| 4 · Evidencia | ¿Qué cambió y qué se mantuvo entre las dos respuestas? ¿Cómo lo explica que sea estocástico? | Cambian redacción, orden y ejemplos; se mantiene la idea general/estructura. Se explica porque en cada paso se saca una ficha al azar según probabilidades y un camino distinto se va acumulando. |\n"
                "| 4 · Evidencia | ¿Por qué dos respuestas de ChatGPT a la misma pregunta pueden ser distintas? | Porque es estocástico: lo que responde es azaroso y depende de las probabilidades con que se entrenó. |\n\n"
                "**Conteo de 2 minutos en la pizarra (concepto 3):** escribir el texto del patio, subrayar cada `en`, anotar lo que viene después (`el`, `el`, `la`), contar y dividir: 2 de 3 ≈ 67 %. "
                "La práctica guiada (réplica de la Parte D de la Prueba 1) se responde **a mano** antes de ejecutar las celdas de comprobación."))
    c.append(md("## 🧩 Práctica guiada (réplica de la Parte D) — solución"))
    c += bloque_sol("Texto del horario", f'texto_tarea = "{TEXTO_TAREA}"\nprint(texto_tarea)')
    c += bloque_sol("D1 · tras `toca`", PREFIJO_TAREA + 'mostrar_probabilidades(texto_tarea, "toca")',
                    "**`mate`, 2 de 3 veces** (`inglés`, 1 de 3). ✅ palabra + cuántas veces · ⚠️ solo la palabra · ❌ sin respuesta.")
    c += bloque_sol("D2 · tras `hoy`", PREFIJO_TAREA + 'mostrar_probabilidades(texto_tarea, "hoy")',
                    "**`toca`, 3 de 4 = 75 %** (`hay`, 1 de 4). El total es 4 (las veces que apareció `hoy`), no las 12 palabras del texto. ✅ palabra + proporción · ⚠️ solo la palabra · ❌ sin respuesta.")
    c += bloque_sol("D3 y D4 · `feriado`", PREFIJO_TAREA + 'mostrar_probabilidades(texto_tarea, "feriado")\nsacar_fichas(texto_tarea, "feriado", 3)',
                    "**D3:** **no** puede usar su regla: no hay nada que contar, `feriado` no tiene bolsa propia. ✅ «no» + razón (nunca la vio) · ⚠️ «no» sin razón · ❌ «sí» sin más. "
                    "*(Se acepta «sí, pero al azar» si aclara que no tiene base: es consistente con D4.)*\n\n"
                    "**D4:** igual tendría que decir algo: **saca una ficha al azar entre las palabras que sí conoce**; la respuesta es **azarosa** (no predecible), depende de con qué se entrenó (ejemplo con semilla fija).\n\n"
                    "**Revisión en vivo:** una pareja explica al frente cómo contó a mano. Es una réplica de la Parte D de la Prueba 1 (mismo formato, otro texto).", semilla=5)
    c.append(md("## 🚀 Ejercicios extra — soluciones"))
    modificado = TEXTO_BASE.replace("en el patio", "en la plaza", 1)
    c += bloque_sol("Ejercicio 0a · Cambiar una palabra",
                    f'texto_modificado = "{modificado}"\nmostrar_probabilidades(texto_modificado, "en")',
                    "Con «en la plaza» en la primera oración, la bolsa de `en` queda con 1 ficha `el` y 2 fichas `la`: ahora `la` es la más probable (2 de 3). "
                    "Cualquier cambio equivalente vale; lo importante es que anticipen que un cambio pequeño en la «base de datos» cambia las probabilidades.")
    c += bloque_sol("Ejercicio 1 · Cafetería", f'texto_cafeteria = "{TEXTO_CAFETERIA}"\nmostrar_probabilidades(texto_cafeteria, "pido")\n'
                    'mostrar_probabilidades(texto_cafeteria, "con")\nmostrar_probabilidades(texto_cafeteria, "empanada")',
                    "(a) `pan`, 3 de 4. (b) tras `con`: `palta`, 2 de 3 ≈ 67 %. (c) `empanada` nunca apareció: no tiene bolsa propia, el modelo saca una ficha al azar entre las palabras que sí conoce.")
    c += bloque_sol("Ejercicio 2 · Frases distintas (desafío)", 'generar_varias(texto_base, "nos", 10, 5)',
                    "**Ejemplo con semilla fija.** Casi siempre salen 4-5 frases distintas; que las 5 coincidan es posible pero muy poco probable. "
                    "Conclusión esperada: en un sistema estocástico cada sorteo es nuevo (hay azar), por eso los resultados cambian de una ejecución a otra.", semilla=11)
    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                f"Respuestas correctas: **{', '.join(TICKET_CORRECTAS)}**. Las preguntas **no están en el Colab de estudiantes**: se proyectan en `Ticket de Salida.pptx` "
                f"y se responden en el Google Form (`{URL_FORM}`). Respuestas también en `Ticket de Salida Respuestas.json`."))
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        alts = "\n".join(f"- **{'ABCD'[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}\n\n**Respuesta correcta: {TICKET_CORRECTAS[i - 1]}.** {TICKET_JUSTIFICACION[i - 1]}"))
    return c


if __name__ == "__main__":
    SALIDA_JSON.write_text(json.dumps(
        {"clase": "44", "tema": TEMA_FORM,
         "respuestas": {f"Respuestas a ticket [{i}]": l for i, l in enumerate(TICKET_CORRECTAS, start=1)}},
        ensure_ascii=False, indent=2), encoding="utf-8")
    guardar(SALIDA_CLASE, clase())
    guardar(SALIDA_SOL, solucionario())
    print("Listo:", SALIDA_CLASE.name, "·", SALIDA_SOL.name)
