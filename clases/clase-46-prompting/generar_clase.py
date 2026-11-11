"""Genera 'Clase 46 - Prompting - Clase.ipynb' (estudiantes), '... - Solucionario.ipynb' (profesor) y el JSON del ticket.

Fuente de verdad: este script + contenido.py + la Spec aprobada. No editar los .ipynb a mano: edita aquí y vuelve a ejecutar.
Ejecutar: py -3 -X utf8 generar_clase.py
Reglas de la clase (Diego): hay ChatGPT en vivo y mucha interactividad (laboratorio + constructor de prompt + duelo);
actitud Flexibilidad; escenario «estudiar para una prueba»; SIN instrucciones personalizadas de ChatGPT (regla permanente).
El único código es el verificador check_evidencia() (solo revisa la forma: links y citas; no juzga calidad).
"""
import contextlib
import io
import json
import uuid
from pathlib import Path

from contenido import (DEBIL_1, DEBIL_2, DEBIL_3, DEBIL_4, DEFINICION, EJEMPLOS, GUIAS, ITEMS_A2, ITEMS_A3, MEJORADOS, OBJETIVO,
                       PARTES, RESPUESTA_HAZ_AHORA, TEMA_FORM, URL_FORM, URL_SLIDES, armar)

URL_PAGINA = URL_SLIDES  # LA página de la clase (guion + actividades); el Colab es solo para escribir

AQUI = Path(__file__).resolve().parent
NOMBRE = "Clase 46 - Prompting"
SALIDA_CLASE = AQUI / f"{NOMBRE} - Clase.ipynb"
SALIDA_SOL = AQUI / f"{NOMBRE} - Solucionario.ipynb"
SALIDA_JSON = AQUI / f"{NOMBRE} - Ticket de Salida Respuestas.json"

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


def _bloque(*lineas: str) -> str:
    return "```text\n" + "\n".join(lineas) + "\n```\n\n"


# ───────────────────────── celda preparada (se ejecuta primero) ─────────────────────────

HELPERS = '''
#@title 🔧 Ejecuta esta celda primero (deja listo el verificador de hoy; no hace falta editarla)
import re

PROMPTS_DEBILES = [
    "Explícame la fotosíntesis",
    "¿Es mejor estudiar de noche o de día? Dame una recomendación.",
    "Hazme preguntas para la prueba de historia",
]


def check_evidencia(link_1, diagnostico, prompt_mejorado, link_2, analisis):
    """Revisa solo la FORMA de tu entrega (links y citas). No juzga si tu diagnóstico o tu mejora son buenos."""
    problemas = []
    prefijos = ("https://chatgpt.com/share/", "https://chat.openai.com/share/")
    for nombre, link in (("link_1", link_1), ("link_2", link_2)):
        if not link.strip().startswith(prefijos):
            problemas.append(f"{nombre}: debe empezar con https://chatgpt.com/share/ (el link sale del botón Compartir de ChatGPT).")
    if link_1.strip() and link_1.strip() == link_2.strip():
        problemas.append("link_1 y link_2 son iguales: cada link debe ser de una conversación distinta.")
    cita = r'[«"“][^«»"“”]{8,}[»"”]'
    for nombre, texto in (("diagnostico", diagnostico), ("analisis", analisis)):
        if not re.search(cita, texto):
            problemas.append(f"{nombre}: falta al menos una cita textual entre comillas, por ejemplo «...» (copia la frase tal cual).")
    if not prompt_mejorado.strip():
        problemas.append("prompt_mejorado: está vacío. Copia aquí tu prompt completo.")
    elif prompt_mejorado.strip() in PROMPTS_DEBILES:
        problemas.append("prompt_mejorado: es igual al prompt débil. Agrégale las 4 partes (Rol, Contexto, Formato, Restricción).")
    if problemas:
        print("⚠️ Revisa estos puntos:")
        for p in problemas:
            print("  -", p)
        print("(Este verificador solo revisa la forma de la entrega, no la calidad de tu análisis.)")
    else:
        print("✅ Entrega completa en su forma: 2 links válidos y citas en el diagnóstico y el análisis.")
        print("(Este verificador solo revisa la forma: que tu análisis sea bueno se revisa en la clase.)")


print("Verificador listo ✅")
'''


def ejecutar(texto: str) -> str:
    """Ejecuta HELPERS + el código y devuelve lo impreso."""
    g: dict = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(HELPERS, g)
    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        exec(texto, g)
    return salida.getvalue().rstrip("\n")


# Autoverificación del verificador (casos buenos y malos)
_LINK_OK = "https://chatgpt.com/share/abc-123"
_DIAG_OK = 'Le falta el Contexto; por eso la respuesta dice «Estudiar de día es siempre mejor».'
_ok = ejecutar(f'check_evidencia("{_LINK_OK}", """{_DIAG_OK}""", "Actúa como orientadora de estudio. Tengo prueba el jueves.", "{_LINK_OK}2", """{_DIAG_OK}""")')
assert _ok.startswith("✅"), _ok
_mal = ejecutar(f'check_evidencia("hola", "sin cita", "{DEBIL_2}", "hola", "sin cita")')
assert _mal.startswith("⚠️") and "link_1" in _mal and "diagnostico" in _mal and "igual al prompt débil" in _mal, _mal
_igual = ejecutar(f'check_evidencia("{_LINK_OK}", """{_DIAG_OK}""", "x y z", "{_LINK_OK}", """{_DIAG_OK}""")')
assert "iguales" in _igual, _igual
assert [sorted(x[1]) for x in ITEMS_A2][-1] == []

# ───────────────────────── ticket ─────────────────────────

TICKET_PREGUNTAS = [
    ("Qué parte falta (paso 3)",
     _bloque("«Eres una profesora de Lenguaje de 3ro medio. Mañana tengo una prueba de",
             "comprensión lectora. Hazme 5 preguntas de alternativas sobre un cuento.»")
     + "Este prompt tiene Rol, Contexto y Formato. ¿Qué parte le falta?",
     ["Rol: no dice quién es la IA.",
      "Contexto: no dice para qué lo necesita.",
      "Formato: no dice cómo quiere la respuesta.",
      "Restricción: no dice qué debe respetar o evitar."]),
    ("Qué cita prueba la consecuencia (paso 3)",
     _bloque("Prompt: «¿Es mejor estudiar de noche o de día?»", "",
             "Respuesta: «Estudiar de día es siempre mejor. Recuerda tomar agua mientras",
             "estudias y descansar un poco entre materias.»")
     + "El diagnóstico dice: «Le falta Contexto; por eso la respuesta toma una postura sin matices». ¿Qué cita de la respuesta lo prueba?",
     ["«Recuerda tomar agua mientras estudias».",
      "«descansar un poco entre materias».",
      "«Estudiar de día es siempre mejor».",
      "«¿Es mejor estudiar de noche o de día?»."]),
    ("Qué evidencia es válida (guiada)",
     _bloque("Mi diagnóstico: «Le falta el Formato; por eso la respuesta es muy larga».")
     + "Vas a entregar la evidencia de tu prompt. ¿Cuál entrega es la válida?",
     ["El link de la conversación, que abre sin pedir permiso, y una frase copiada entre comillas de la respuesta.",
      "Solo un resumen con tus propias palabras de lo que respondió ChatGPT.",
      "Una captura de pantalla de la conversación, sin el link.",
      "Un link que pide permiso para abrirse, más una frase entre comillas."]),
]
TICKET_CORRECTAS = ["D", "C", "A"]
TICKET_JUSTIFICACION = [
    "El prompt tiene Rol (profesora de Lenguaje), Contexto (prueba de comprensión lectora mañana) y Formato (5 preguntas de alternativas). "
    "Falta la **Restricción**: algo que deba respetar o evitar (por ejemplo, «no uses cuentos muy largos» o «nivel de 3ro medio»).",
    "La consecuencia del diagnóstico es la postura sin matices. La frase que la muestra es «Estudiar de día es siempre mejor»: es absoluta y no considera la situación de quien pregunta. "
    "Las otras citas son consejos sueltos o el propio prompt, no la respuesta.",
    "La evidencia válida combina el **link que abre sin pedir permiso** y una **cita textual entre comillas**. Un resumen propio, una captura sin link o un link que pide permiso no permiten comprobar lo que dijo la IA.",
]

# ───────────────────────── cuaderno de estudiantes ─────────────────────────

VERIF = "#### ✅ Verificamos lo aprendido\n\nEl colega le pregunta a dos personas del curso:\n\n"


def _partes_md(n: int) -> str:
    m = MEJORADOS[n]
    return "\n".join(f"- **{p}:** {m[p]}" for p in PARTES)


def celdas_inicio() -> list:
    haz = "\n".join(f"> {r}\n>" for r in RESPUESTA_HAZ_AHORA).rstrip("\n>").rstrip()
    return [
        md("# 🐍 Clase 46 — Prompting: guiar a la IA y evaluar bien su respuesta\n\n"
           "**Curso:** 3ro medio  |  **Duración:** 80 min  |  **Plataforma:** Google Colab + ChatGPT\n\n---"),
        md("## 🎯 Objetivo de la clase\n\n" + OBJETIVO + "\n\n"
           "## 🔎 ¿Por qué lo veremos?\n\n"
           "> Pedirle a ChatGPT que te ayude a estudiar sirve o no según cómo se lo pidas. "
           "Como ChatGPT responde con azar (lo vimos en la clase anterior), **tu prompt es lo que guía el camino**.\n\n---\n\n"
           "**Lo que ya sabes:** que ChatGPT predice la siguiente palabra y es **estocástico**: la misma pregunta puede dar respuestas distintas.\n\n"
           "**Lo que aprenderás hoy:** qué es un prompt, las 4 partes de un buen prompt, cómo **diagnosticar** uno débil y cómo **mejorarlo y comprobar con evidencia** "
           "(un link y citas textuales) que la respuesta mejoró. **Hoy usas ChatGPT en vivo.**"),
        md("## 🧭 Hoja de ruta: dónde se hace cada cosa\n\n"
           f"**La página de la clase es el guion:** [{URL_PAGINA}]({URL_PAGINA}) (el profesor la proyecta y tú haces ahí las actividades). "
           "Este cuaderno es **solo para escribir** tus respuestas.\n\n"
           "| Paso | Qué hacemos | 🧪 Página | 💬 ChatGPT | 📝 Este Colab |\n|---|---|:-:|:-:|:-:|\n"
           "| **Haz Ahora** | Miramos la respuesta de una estudiante | ✔️ | | respuestas |\n"
           "| **1** | ¿Qué es un prompt? Mismo prompt, dos veces | ✔️ | ✔️ | qué cambió, qué se mantuvo, por qué |\n"
           "| **2** | Armamos entre todos las 4 partes | ✔️ | ✔️ | el prompt y qué cambió |\n"
           "| **3** | ¿Qué le falta a un prompt? | ✔️ | | tu diagnóstico con cita |\n"
           "| **4** | Otra situación: armas tu prompt | ✔️ | ✔️ | antes / ahora / qué falta |\n"
           "| **Guiada** | El ciclo completo con evidencia | ✔️ | ✔️ | celda de código |\n"
           "| **Ticket** | Preguntas en la tele | | | link al Form |\n\n"
           "🔒 **Cuidado con tus datos:** no escribas en ChatGPT tu nombre completo, RUT, dirección ni datos de otras personas. "
           "El link que compartes muestra todo lo que escribiste."),
        md("## 🔧 Ejecuta esta celda primero\n\n"
           "Deja listo el verificador que usarás en la práctica guiada. No necesitas entenderla ni editarla."),
        codigo(HELPERS),
        md("---\n\n## 1️⃣ Haz Ahora\n\n"
           "Una estudiante de tu curso prepara la **prueba de Biología del jueves** y le pidió ayuda a ChatGPT con este prompt:\n\n"
           f"> **«{DEBIL_1}»**\n\n"
           "Esto fue lo que respondió *(respuesta de ejemplo preparada para la clase)*:\n\n"
           + haz + "\n\n"
           "Responde mirando la respuesta:\n\n"
           "1. ¿La respuesta dice para qué curso o nivel es?\n"
           "2. ¿Menciona para cuándo es la prueba?\n"
           "3. ¿Cuántos párrafos tiene?\n"
           "4. ¿La entenderías en 5 minutos de estudio?\n\n"
           "Sabiendo que dominas ChatGPT, la estudiante te pide ayuda — pero antes quiere que tengamos clara la lógica."),
        md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. "),
        md("---\n\n### 🔁 Ayer → 🔀 Hoy → ➡️ La próxima clase\n\n"
           "| | Qué hacemos |\n|---|---|\n"
           "| 🔁 **Ayer** | ChatGPT predice la siguiente palabra y es **estocástico**: la misma pregunta puede dar respuestas distintas. |\n"
           "| 🔀 **Hoy es distinto** | Como tiene azar, **el prompt guía el camino**: aprendemos a pedirle bien las cosas y a comprobar si respondió bien. |\n"
           "| ➡️ **La próxima clase (martes 24)** | Ética y las 4D: cómo revisar con criterio lo que responde una IA. |"),
    ]


def icn() -> list:
    c = [md("---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
            "Hoy trabajamos en **4 pasos**. En cada uno: el profesor muestra en la página, tú haces la actividad (con **ChatGPT en otra pestaña**) y respondes **aquí**. "
            "Cada vez que pidas algo nuevo, abre una **conversación nueva**.\n\n"
            f"🧭 Página de la clase: [{URL_PAGINA}]({URL_PAGINA})")]

    # ── Paso 1 ──
    c.append(md("### 💡 Paso 1 — ¿Qué es un prompt?\n\n"
                f"- **{DEFINICION}**\n"
                "- Lo que escribas **guía el camino** de la respuesta.\n"
                "- Ayer vimos que ChatGPT es **estocástico**: con el mismo prompt la respuesta puede cambiar. Hoy lo comprobamos.\n\n"
                + idea("un prompt es el texto que le escribes a una IA para pedirle algo, y como la IA es estocástica, el mismo prompt puede dar respuestas distintas.") + "\n\n"
                f"🧭 **Dónde:** página [paso 1]({URL_PAGINA}#p1) + ChatGPT + aquí.\n\n"
                f"✍️ **Escríbelo tú:** envía **exactamente** «{DEBIL_1}» en **dos conversaciones nuevas** y compara las dos respuestas."))
    c.append(md("**Qué cambió:** \n\n**Qué se mantuvo:** \n\n**Por qué (usa la palabra «estocástico»):** "))
    c.append(md(VERIF + "- ¿Qué es un prompt?\n- ¿Qué quiere decir que ChatGPT sea estocástico?"))

    # ── Paso 2 ──
    c.append(md("### 💡 Paso 2 — Las 4 partes de un buen prompt\n\n"
                "| Parte | Qué es | La pregunta que nos hacemos |\n|---|---|---|\n"
                + "\n".join(f"| **{p}** | {d} | {GUIAS[p]} |" for p, d in zip(PARTES, [
                    "quién es la IA", "la situación, para qué, a quién", "lista, tabla, extensión, tono", "qué debe respetar o evitar"])) + "\n\n"
                "**Lo armamos entre todos en la página:** el profesor pregunta al curso por cada parte y escribe lo que decidan.\n\n"
                + idea("un buen prompt dice quién es la IA (Rol), para qué lo necesitas (Contexto), cómo quieres la respuesta (Formato) y qué debe evitar (Restricción).") + "\n\n"
                f"🧭 **Dónde:** página [paso 2]({URL_PAGINA}#p2) + ChatGPT + aquí.\n\n"
                f"✍️ **Escríbelo tú:** con el mismo pedido («{MEJORADOS[1]['pedido']}»), copia el prompt que armamos entre todos y envíalo en una conversación nueva."))
    c.append(md("**El prompt que armamos entre todos:** \n\n**Qué cambió en la respuesta frente a la primera:** "))
    c.append(md(VERIF + "- ¿Qué parte le falta a «Eres profesor de Biología. Explícame la fotosíntesis»?\n"
                "- Da un ejemplo de **Formato** y uno de **Restricción** para un prompt sobre estudiar para una prueba."))

    # ── Paso 3 ──
    c.append(md("### 💡 Paso 3 — ¿Qué le falta a este prompt? (diagnosticar)\n\n"
                "Diagnosticar es explicar **qué parte falta** y **qué consecuencia se nota** en la respuesta, **citando una frase** de ella.\n\n"
                "**Marco para escribirlo:** «Le falta ___; por eso la respuesta ___, por ejemplo: “___”».\n\n"
                "**Ejemplo con la respuesta del Haz Ahora:** «Le falta el **Contexto** y el **Formato**; por eso la respuesta es demasiado técnica y larga, "
                "por ejemplo: “autótrofos fototrofos transforman la energía lumínica”».\n\n"
                + idea("un diagnóstico dice qué parte falta, qué consecuencia se nota en la respuesta y cita una frase que lo prueba.") + "\n\n"
                f"🧭 **Dónde:** página [paso 3]({URL_PAGINA}#p3) (marcas lo que falta: una parte, varias o ninguna) + aquí.\n\n"
                "✍️ **Escríbelo tú:** escribe tu **diagnóstico de la respuesta del Paso 1** usando el marco."))
    c.append(md("**Mi diagnóstico:** "))
    c.append(md(VERIF + "- ¿Qué tres cosas tiene un buen diagnóstico?\n"
                "- ¿Por qué una cita sirve más que decir «la respuesta es mala»?"))

    # ── Paso 4 ──
    c.append(md("### 💡 Paso 4 — Otra situación: mejorar y comprobar\n\n"
                "**Situación:** el curso tiene **tres pruebas el mismo jueves** y quiere pedirle al **profesor jefe** que cambie una. "
                f"Un compañero le escribió a ChatGPT: **«{DEBIL_4}»**.\n\n"
                "**Flexibilidad:** si la primera forma de pedir no sirvió, **cámbiala**.\n\n"
                "**El ciclo:**\n"
                "1. **Envía** el prompt débil y mira la respuesta.\n"
                "2. **Arma tu prompt** con las 4 partes en el constructor de la página.\n"
                "3. **Envíalo** en otra conversación nueva.\n"
                "4. **Compara**: una cita de antes y una de ahora; di **qué mejoró** y **qué falta aún**.\n\n"
                "**Marco para comprobar:** «Mejoró ___: antes decía “___”, ahora dice “___”. Todavía falta ___.»\n\n"
                + idea("mejorar un prompt es cambiarlo con las 4 partes, volver a probar y comprobar con una cita que el problema mejoró, diciendo qué falta aún.") + "\n\n"
                f"🧭 **Dónde:** página [paso 4]({URL_PAGINA}#p4) (constructor con botón Copiar) + ChatGPT + aquí.\n\n"
                "✍️ **Escríbelo tú:** arma tu prompt, pruébalo y completa el marco."))
    c.append(md("**Una cita de la respuesta al prompt débil:** \n\n**Mi prompt con las 4 partes:** \n\n"
                "**Una cita de la respuesta ahora:** \n\n**Qué mejoró:** \n\n**Qué falta aún:** "))
    c.append(md(VERIF + "- ¿Qué haces si la primera respuesta no sirvió? ¿Por qué es mejor cambiar solo lo que diagnosticaste?\n"
                "- ¿Qué dos cosas necesita tu evidencia para ser válida?"))

    c.append(md("### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?\n\n"
                "| Concepto | Qué significa |\n|---|---|\n"
                "| Prompt | el texto que le escribes a una IA para pedirle algo; guía el camino de la respuesta |\n"
                "| Rol / Contexto / Formato / Restricción | quién es la IA · para qué y a quién · cómo quieres la respuesta · qué debe evitar |\n"
                "| Diagnóstico | qué parte falta + qué consecuencia se nota + una cita de la respuesta |\n"
                "| Mejora y comprobación | reescribir con las 4 partes, volver a probar, citar lo que mejoró y decir qué falta aún |\n"
                "| Evidencia | el link de la conversación (que abre sin pedir permiso) + frases copiadas entre comillas |"))
    c.append(md("#### ⚠️ Errores típicos a evitar\n\n"
                "| Error | Qué ocurre | Cómo corregirlo |\n|---|---|---|\n"
                "| Decir «es mala» sin nombrar la parte | No se sabe qué cambiar | Nombra la parte que falta y la consecuencia |\n"
                "| Citar algo que no prueba nada | El diagnóstico no se sostiene | Elige la frase que muestra la consecuencia |\n"
                "| Cambiar todo el prompt a la vez | No sabes qué mejoró la respuesta | Cambia primero la parte que diagnosticaste |\n"
                "| Compartir un link que pide permiso | Nadie puede comprobar tu evidencia | Ábrelo en una ventana de incógnito antes de entregarlo |\n"
                "| Parafrasear en vez de citar | No se puede verificar | Copia la frase tal cual, entre comillas |"))
    return c


def guiada() -> list:
    c = [md("---\n\n## 3️⃣ Práctica guiada: el ciclo completo\n\n"
            f"🧭 Las instrucciones paso a paso están en la página: [guiada]({URL_PAGINA}#guiada). **Aquí escribes tus respuestas.**\n\n"
            "Son **5 preguntas, en orden**. Cada una tiene **su propio cuadro** (una celda de código): escribe tu respuesta **entre las comillas** y ejecuta la celda con ▶️. "
            "Al final, un verificador revisa **solo la forma** de tu entrega (links y citas). Después revisamos una entrega entre todos."),
         md("### 🎯 ¿De noche o de día?\n\n"
            "La estudiante de Biología también quiere saber cómo organizar su tiempo de estudio para el jueves, y le pregunta a ChatGPT: "
            f"**«{DEBIL_2}»** Sabes que ese prompt es débil: ahora te toca diagnosticarlo, mejorarlo y comprobar con evidencia que resultó mejor.\n\n"
            "**Cómo escribir en los cuadros:** los **links** van entre comillas simples `\"...\"`; los **textos largos** van entre triples comillas `\"\"\"` "
            "(puedes usar varias líneas) y las citas se escriben entre `«»`.")]
    c.append(md("#### Pregunta 1 — Envía el prompt débil y comparte el link\n\n"
                f"Abre ChatGPT, crea una **conversación nueva** y envía **exactamente**: **«{DEBIL_2}»**. "
                "Cuando responda, usa el botón *Compartir*, copia el link y ábrelo en una ventana de incógnito: si abre sin pedir permiso, sirve.\n\n"
                + pista(1, "el link", "Debe empezar con `https://chatgpt.com/share/`. Si pide permiso para abrirse, vuelve a compartir.") + "\n\n"
                "👇 **Pega tu link entre las comillas:**"))
    c.append(codigo('# Pregunta 1\nlink_1 = ""'))
    c.append(md("#### Pregunta 2 — Escribe tu diagnóstico\n\n"
                "Mira la respuesta y completa: «Le falta ___; por eso la respuesta ___, por ejemplo: “___”». La cita se copia **tal cual** de la respuesta.\n\n"
                + pista(2, "qué mirar", "Revisa si la respuesta tiene en cuenta tu situación y si da matices. Cita la frase que lo muestra.") + "\n\n"
                "👇 **Escribe tu diagnóstico entre las triples comillas:**"))
    c.append(codigo('# Pregunta 2\ndiagnostico = """\n"""'))
    c.append(md("#### Pregunta 3 — Escribe tu prompt mejorado\n\n"
                "Arma el prompt con las **4 partes** (Rol, Contexto, Formato y Restricción). Puedes usar el constructor de la página (en la guiada) y copiar el resultado.\n\n"
                "👇 **Pega tu prompt completo entre las triples comillas:**"))
    c.append(codigo('# Pregunta 3\nprompt_mejorado = """\n"""'))
    c.append(md("#### Pregunta 4 — Envía tu prompt mejorado y comparte el link\n\n"
                "Pega tu prompt en **otra conversación nueva**, espera la respuesta y comparte el link como en la Pregunta 1. Debe ser un link **distinto** al anterior.\n\n"
                "👇 **Pega el segundo link entre las comillas:**"))
    c.append(codigo('# Pregunta 4\nlink_2 = ""'))
    c.append(md("#### Pregunta 5 — ¿Funcionó?\n\n"
                "Compara las dos respuestas y completa: «Mejoró ___: antes decía “___”, ahora dice “___”. Todavía falta ___.» "
                "Incluye una **cita de cada respuesta** y **una cosa que todavía falta**.\n\n"
                "👇 **Escribe tu análisis entre las triples comillas:**"))
    c.append(codigo('# Pregunta 5\nanalisis = """\n"""'))
    c.append(md("#### ✅ Al final — Ejecuta el verificador\n\n"
                "Revisa **solo la forma** de tu entrega (links y citas), no si tu análisis es bueno. Si falta algo, te dice qué corregir.\n\n"
                "📤 <em>El verificador imprime, cuando tu entrega está completa:</em>\n\n"
                "<pre>✅ Entrega completa en su forma: 2 links válidos y citas en el diagnóstico y el análisis.</pre>"))
    c.append(codigo('# Verificador\ncheck_evidencia(link_1, diagnostico, prompt_mejorado, link_2, analisis)'))
    return c


def duelo() -> list:
    return [md("---\n\n## ⚔️ Duelo de prompts en vivo *(opcional: solo si sobra tiempo)*\n\n"
               f"Prompt débil: **«{DEBIL_3}»**. Dos estudiantes lo mejoran **por separado** con las 4 partes. "
               "Proyectamos las dos respuestas y el curso vota cuál resolvió mejor el problema, **justificando con una cita**.\n\n"
               "**Mi voto y mi cita:** \n\n"
               + pista(1, "qué mirar", "Compara qué tan útiles, claras y ajustadas al nivel son las respuestas, y cita la frase que más pesó en tu voto.")),
            md("**Mi voto:** \n\n**Mi cita:** ")]


def extras() -> list:
    c = [md("---\n\n## 4️⃣ Ejercicios extra\n\nPara seguir practicando en casa o si terminas antes. Son opcionales y no tienen nota.")]
    c.append(md("### 🎯 Ejercicio 1 — El ciclo completo con otro prompt\n\n"
                f"Repite el ciclo de la guiada con el prompt débil de la prueba de historia: **«{DEBIL_3}»**. **Tu entrega debe:** mostrar los dos links, "
                "el diagnóstico con cita, el prompt mejorado y el análisis de si funcionó.\n\n"
                + pista(1, "el marco", "«Le falta ___; por eso la respuesta ___, por ejemplo: «___»».") + "\n\n"
                + pista(2, "qué falta aún", "Escribe una cosa concreta que todavía podrías pedirle: otro tono, una extensión, un ejemplo.")))
    c.append(codigo('# Tu solución del Ejercicio 1\n'
                    'link_1 = ""\n\n'
                    'diagnostico = """\n"""\n\n'
                    'prompt_mejorado = """\n"""\n\n'
                    'link_2 = ""\n\n'
                    'analisis = """\n"""\n\n'
                    'check_evidencia(link_1, diagnostico, prompt_mejorado, link_2, analisis)'))
    c.append(md("### 🎯 Ejercicio 2 — Flexibilidad: cambia una sola parte\n\n"
                "Toma tu prompt mejorado de la guiada y cambia **una sola parte** (por ejemplo, el Formato: de tabla a lista). Envíalo en una conversación nueva. "
                "**Tu respuesta debe:** decir qué parte cambiaste y qué cambió en la respuesta, con una cita de cada una.\n\n"
                + pista(1, "una sola parte", "Si cambias dos cosas a la vez, no sabrás cuál produjo el cambio.") + "\n\n"
                + pista(2, "compara", "Pon lado a lado una cita de la respuesta anterior y una de la nueva.")))
    c.append(md("**Parte que cambié:** \n\n**Cita antes:** \n\n**Cita ahora:** \n\n**Qué cambió:** "))
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
               "1. ¿Qué tan bien entendiste cómo diagnosticar y mejorar un prompt, donde 1 es \"no entendí nada\" y 5 es \"puedo explicárselo a otro\"?\n\n"
               "2. ¿En qué momento cambiaste tu forma de pedir y qué pasó con la respuesta?\n\n"
               "👀 **Lo que viene (martes 24):** ética y las 4D, cómo revisar con criterio lo que responde una IA."),
            md("### 📝 Mis respuestas\n\n*(haz doble click para editar y escribir tus respuestas)*\n\n1. \n\n2. "),
            md("---")]


def clase() -> list:
    return celdas_inicio() + icn() + guiada() + duelo() + ticket() + cierre() + extras()


# ───────────────────────── solucionario ─────────────────────────


def _tabla_a3() -> str:
    filas = "\n".join(f"| {i} | «{it['prompt']}» | {it['falta']} | {it['oraciones'][it['correcta']]} |" for i, it in enumerate(ITEMS_A3, start=1))
    return "| Ítem | Prompt | Falta | Cita correcta |\n|---|---|---|---|\n" + filas


def solucionario() -> list:
    c = [md("# Clase 46 — Prompting · Solucionario\n\n"
            "**Solo para el profesor.** No se sube a Classroom ni se proyecta antes de dictar la clase.\n\n"
            "Las respuestas de ChatGPT en vivo **varían**: no hay respuesta única. Aquí van respuestas modelo, criterios y los ejemplos **preparados a mano** "
            "(no generados por ChatGPT) que sirven de **plan B** si a alguien no le funciona ChatGPT. "
            f"La página de la clase ({URL_PAGINA}) **no muestra los prompts modelo**: se construyen con el curso (paso 2) y con cada estudiante (paso 4)."),
         md("## ⚙️ Celda preparada\n\nLa misma celda inicial que ven los estudiantes."),
         codigo(HELPERS),
         md("## 🧠 Haz Ahora\n\n"
            "Respuesta de ejemplo (prompt «Explícame la fotosíntesis»): 3 párrafos técnicos.\n\n"
            "1. **No**, no dice para qué curso o nivel es.\n"
            "2. **No**, no menciona la prueba del jueves.\n"
            "3. **3 párrafos.**\n"
            "4. Respuesta abierta; lo esperado es **no**, por términos como «autótrofos fototrofos», «tilacoidales» o «RuBisCO» sin explicar.\n\n"
            "**Ancla para la clase:** faltan el nivel, la fecha y el formato porque el prompt no los pidió; esa es la intuición del diagnóstico.")]

    c.append(md("## 📘 ICN — respuestas modelo\n\n### Paso 1 · ¿Qué es un prompt? (mismo prompt, dos veces)\n\n"
                f"**Definición:** {DEFINICION}\n\n"
                "No hay respuesta única (las respuestas reales varían). **Sin citas en este paso.** Rúbrica orientadora:\n\n"
                "| Componente | ✅ completo | ⚠️ parcial | ❌ cero |\n|---|---|---|---|\n"
                "| Qué cambió / qué se mantuvo | nombra al menos un cambio (redacción, orden, ejemplos, extensión) y una constante (la idea general) | nombra solo uno de los dos | sin evidencia |\n"
                "| Por qué | dice que ChatGPT es **estocástico** (comportamiento que no se puede predecir con total exactitud: hay azar) y que en cada paso saca una ficha al azar | «es aleatorio» sin más | explicación incorrecta |"))
    c.append(md("### Paso 2 · Las 4 partes: prompt modelo (solo para el profesor)\n\n"
                "En clase **se construye con el curso**, parte por parte (ver preguntas guía abajo). Este es un modelo de referencia, **no se muestra**:\n\n"
                + "\n".join(f"- **{p}** — *{GUIAS[p]}* → «{MEJORADOS[1][p]}»" for p in PARTES)
                + f"\n\n> {armar(1)}\n\n"
                "Cualquier versión del curso que tenga las 4 partes sirve. Lo esperado en el Colab: pegar el prompt armado y describir un cambio concreto frente a la primera respuesta "
                "(más corta, de nivel adecuado, en lista, con ejemplo…)."))
    c.append(md("### Paso 3 · Diagnósticos modelo\n\n"
                "- **«Explícame la fotosíntesis»:** «Le falta el **Contexto** y el **Formato**; por eso la respuesta es demasiado técnica y larga, por ejemplo: “autótrofos fototrofos transforman la energía lumínica”».\n"
                f"- **«{DEBIL_2}»:** «Le falta el **Contexto** y la **Restricción**; por eso la respuesta toma una postura sin matices, por ejemplo: “Estudiar de día es siempre mejor”».\n"
                f"- **«{DEBIL_3}»:** «Le falta el **Contexto** (qué tema) y el **Formato** (cuántas y de qué tipo); por eso las preguntas son de temas sueltos, por ejemplo: “¿Quién fue Napoleón Bonaparte?”».\n\n"
                "**Actividad de la página (clave) · ① qué falta:** " + " · ".join(f"«{p}» → faltan: {', '.join(f) or 'ninguna (está completo)'}" for p, f in ITEMS_A2)
                + "\n\n**② cita que prueba la consecuencia:**\n\n" + _tabla_a3()
                + "\n\n**Criterio (Colab):** ✅ nombra la(s) parte(s) + consecuencia + cita · ⚠️ falta la cita o la consecuencia · ❌ «es mala» sin más."))
    c.append(md("### Paso 4 · Otra situación (correo al profesor jefe): modelo\n\n"
                f"Prompt débil: **«{DEBIL_4}»** → falta **todo**: Rol, Contexto (qué pruebas, cuántas, a quién), Formato (extensión, asunto, tono) y Restricción.\n\n"
                + "\n".join(f"- **{p}:** {MEJORADOS[4][p]}" for p in PARTES)
                + f"\n\n> {armar(4)}\n\n"
                "**Diagnóstico modelo:** «Le falta el **Contexto** y el **Formato**; por eso el correo es genérico y sin datos concretos, por ejemplo: “Le escribo para solicitar el cambio de una prueba”».\n\n"
                "**Comprobación modelo:** «Mejoró **la precisión**: antes decía “Le escribo para solicitar el cambio de una prueba”, ahora dice “nos preocupa no alcanzar a prepararlas bien”. "
                "Todavía falta pedirle que ofrezca fechas concretas dentro del calendario del curso.»\n\n"
                "*(Las citas dependen de la respuesta real de ChatGPT; lo importante es: una cita de antes, una de ahora, qué mejoró y qué falta aún.)*"))
    c.append(md("## ✅ Verificamos lo aprendido — respuestas esperadas\n\n"
                "| Paso | Pregunta | Respuesta esperada |\n|---|---|---|\n"
                f"| 1 | ¿Qué es un prompt? | {DEFINICION} |\n"
                "| 1 | ¿Qué es ser estocástico? | Que el comportamiento no se puede predecir con total exactitud: tiene azar (saca una ficha al azar). |\n"
                "| 2 | ¿Qué parte le falta a «Eres profesor de Biología. Explícame la fotosíntesis»? | Contexto, Formato y Restricción. |\n"
                "| 2 | Ejemplos de Formato y Restricción | Formato: «en una lista de 5 pasos», «tono cercano». Restricción: «no uses términos universitarios», «máximo 150 palabras». |\n"
                "| 3 | ¿Qué tres cosas tiene un buen diagnóstico? | Qué parte falta, qué consecuencia se nota y una cita de la respuesta. |\n"
                "| 3 | ¿Por qué sirve más una cita? | Porque se puede comprobar: muestra la frase real que prueba la consecuencia; «es mala» no. |\n"
                "| 4 | ¿Qué haces si la primera respuesta no sirvió? | Cambiar el prompt (flexibilidad): agregar la parte que falta, cambiando poco para saber qué mejoró. |\n"
                "| 4 | ¿Qué dos cosas necesita la evidencia? | El link que abre sin pedir permiso y citas textuales entre comillas. |"))
    ej_ok = ('link_1 = "https://chatgpt.com/share/ejemplo-1"\n\n'
             'diagnostico = """Le falta el Contexto y la Restricción; por eso la respuesta toma una postura sin matices, '
             'por ejemplo: «Estudiar de día es siempre mejor.»"""\n\n'
             f'prompt_mejorado = """{armar(2)}"""\n\n'
             'link_2 = "https://chatgpt.com/share/ejemplo-2"\n\n'
             'analisis = """Mejoró: antes decía «Estudiar de día es siempre mejor.», ahora dice «Depende de tu rutina». '
             'Todavía falta pedirle cuántas horas de estudio necesito."""\n\n'
             'check_evidencia(link_1, diagnostico, prompt_mejorado, link_2, analisis)')
    ej_mal = ej_ok.replace('"https://chatgpt.com/share/ejemplo-1"', '"mi link"').replace("«Estudiar de día es siempre mejor.»", "que es mala")
    c.append(md("## 🧩 Práctica guiada — solución y rúbrica orientadora\n\n"
                f"Prompt débil: **«{DEBIL_2}»**. Solución modelo (con links de ejemplo) y salida del verificador:\n\n"
                f"**Salida:**\n\n```text\n{ejecutar(ej_ok)}\n```\n\n"
                "| Componente | ✅ completo | ⚠️ parcial | ❌ cero |\n|---|---|---|---|\n"
                "| Pregunta 1 · Link 1 | abre y es del prompt débil exacto | link que pide permiso o prompt distinto | sin link |\n"
                "| Pregunta 2 · Diagnóstico | parte(s) que falta + consecuencia + **cita** | falta la cita o la consecuencia | «es mala» |\n"
                "| Pregunta 3 · Prompt mejorado | tiene Rol, Contexto, Formato y Restricción | le falta una parte | igual al débil |\n"
                "| Pregunta 4 · Link 2 | abre y es del prompt mejorado | link que pide permiso | sin link |\n"
                "| ¿Funcionó? (Pregunta 5) | cita de cada respuesta + una cosa que falta aún | falta la cita o lo que falta | sin análisis |\n\n"
                "**El verificador solo mira la forma** (links y citas). Un ejemplo con errores de forma:"))
    c += [codigo(ej_ok), md("**Salida con errores de forma** (link sin formato y sin cita):\n\n```text\n" + ejecutar(ej_mal) + "\n```")]
    c.append(md("## ⚔️ Duelo de prompts (opcional) — criterios para votar\n\n"
                f"Prompt débil 3: «{DEBIL_3}». Mejor respuesta = la que tiene **tema, cantidad, tipo y respuestas** ajustados al contexto. "
                "El voto vale con **una cita** (ej.: «incluye las respuestas al final con una explicación»). Guía: no premiar la respuesta más larga."))
    c.append(md("## 🚀 Ejercicios extra — soluciones\n\n"
                f"**Ejercicio 1 (prueba de historia):** prompt mejorado modelo: {armar(3)} Diagnóstico: ver paso 3.\n\n"
                "**Ejercicio 2 (flexibilidad):** vale cualquier cambio de **una sola** parte (p. ej., Formato: tabla → lista) con una cita antes y una cita ahora que muestren lo que cambió."))
    c.append(md("## 🛟 Respuestas de ejemplo preparadas (plan B)\n\n"
                "Escritas a mano para la clase, **no generadas por ChatGPT**. Úsalas si a alguien no le funciona ChatGPT (también están en la página, en «Plan B», sin el texto del prompt mejorado)."))
    for n, deb in ((1, DEBIL_1), (2, DEBIL_2), (3, DEBIL_3), (4, DEBIL_4)):
        c.append(md(f"### «{deb}»\n\n**Respuesta al prompt débil:**\n\n" + "\n".join(f"> {s}" for s in EJEMPLOS[n]["debil"])
                    + f"\n\n**Respuesta al prompt mejorado:** *({armar(n)})*\n\n" + "\n".join(f"> {s}" for s in EJEMPLOS[n]["mejorada"])))
    c.append(md("## 🎫 Ticket de salida — preguntas y respuestas\n\n"
                f"Respuestas correctas: **{', '.join(TICKET_CORRECTAS)}**. Las preguntas **no están en el Colab de estudiantes**: se proyectan en `Ticket de Salida.pptx` "
                f"y se responden en el Google Form (`{URL_FORM}`). Respuestas también en `Ticket de Salida Respuestas.json`."))
    for i, (titulo, enunciado, alternativas) in enumerate(TICKET_PREGUNTAS, start=1):
        alts = "\n".join(f"- **{'ABCD'[k]})** {a}" for k, a in enumerate(alternativas))
        c.append(md(f"### Pregunta {i} — {titulo}\n\n{enunciado}\n\n{alts}\n\n**Respuesta correcta: {TICKET_CORRECTAS[i - 1]}.** {TICKET_JUSTIFICACION[i - 1]}"))
    return c


if __name__ == "__main__":
    SALIDA_JSON.write_text(json.dumps(
        {"clase": "46", "tema": TEMA_FORM,
         "respuestas": {**{f"Respuestas a ticket [{i}]": l for i, l in enumerate(TICKET_CORRECTAS, start=1)},
                        "Respuestas a ticket [4]": "No se preguntó"}},
        ensure_ascii=False, indent=2), encoding="utf-8")
    guardar(SALIDA_CLASE, clase())
    guardar(SALIDA_SOL, solucionario())
    print("Listo:", SALIDA_CLASE.name, "·", SALIDA_SOL.name)
