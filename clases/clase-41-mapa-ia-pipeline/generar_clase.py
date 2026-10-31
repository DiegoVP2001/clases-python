"""Generates 'Clase 41 - Mapa IA - Clase.ipynb' (guide notebook; the practice lives in the web page).

Source of truth: this script + the approved Spec. Never edit the .ipynb by hand; edit here and rerun.
Run: py -3 generar_clase.py   (after fuentes/construir.py has exported the diagram PNGs)
"""
import base64
import json
import uuid
from pathlib import Path

AQUI = Path(__file__).resolve().parent
URL_PAGINA = "https://clases-ia-mario-bertero.vercel.app/clase-41/"
SALIDA = AQUI / "Clase 41 - Mapa IA - Clase.ipynb"


def imagen(nombre: str, alt: str) -> str:
    datos = base64.b64encode((AQUI / "diagramas" / nombre).read_bytes()).decode("ascii")
    return f"![{alt}](data:image/png;base64,{datos})"


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {},
            "source": texto.strip("\n").splitlines(keepends=True)}


def ir_a(actividad: str) -> str:
    return f"👉 **Vamos a la actividad {actividad} de la página.**"


def ir_a_pagina(pagina: int, destino: str) -> str:
    return f"👉 **Vamos {destino} de la página** (cambiamos a la **página {pagina}**: nos piden el código)."


def idea(titulo: str, texto: str) -> str:
    return f"> **Idea clave — {titulo}:** {texto}"


HAZ_AHORA = [
    "¿Dónde han escuchado hablar de IA?",
    "¿Qué creen que hace una IA?",
    "¿Qué han probado ustedes?",
    "¿Cómo creen que aprende?",
    "¿Qué dudas o riesgos les genera?",
]

celdas = [
    md("# Clase 41 — Mapa de la IA + pipeline\n\n**3ro medio · Inteligencia artificial · lunes 2 de noviembre**"),
    md("## 🎯 Objetivo de la clase\n\n"
       "Ubicar ejemplos de IA en el mapa (reglas, ML, DL e IA generativa) y ordenar el recorrido de los datos "
       "hasta la evaluación de un modelo, con curiosidad."),
    md("## 🔎 ¿Por qué lo veremos?\n\n"
       "> La IA ya decide cosas a nuestro alrededor —el filtro de spam, las canciones que nos recomiendan, las "
       "respuestas de ChatGPT— y saber cómo funciona cada una nos dice cuánto confiar. Además, el recorrido "
       "datos → entrenar → evaluar es el que seguiremos todo noviembre para entrenar nuestros propios modelos, "
       "empezando por predecir si hay que regar una viña."),
    md("## 🌐 La página de la clase\n\n"
       "Las actividades viven en una página. Cuando este Colab diga **«vamos a la actividad X de la página»**, la "
       "abrimos y entramos con el código que nos entregan en la sala.\n\n"
       f"👉 **[Abrir la página de la clase]({URL_PAGINA})**"),
    md("---\n\n## 🧠 Haz Ahora — ¿Qué sabemos de la IA?\n\n"
       "Escuchamos cada pregunta y respondemos en voz alta. Si queremos, anotamos nuestra idea (no se revisa)."),
]
for i, pregunta in enumerate(HAZ_AHORA, start=1):
    celdas.append(md(f"**{i}. {pregunta}**\n\n✍️ *Mi idea:* ..."))

celdas += [
    md("---\n\n## 🗺️ Nuestro recorrido de noviembre\n\n"
       "| Fecha | Qué hacemos |\n|---|---|\n"
       "| Lun 2 | Mapa de la IA + pipeline (hoy) |\n"
       "| Mar 3 | Primer clasificador |\n"
       "| Jue 5 | Construir una neurona |\n"
       "| Lun 9 | Entrenar una red y medir aciertos |\n"
       "| Mar 10 | Mini-LLM: generar texto |\n"
       "| Jue 12 | **Evaluación 1** (E1, 45 min) |\n"
       "| Lun 16 | Usar ChatGPT con instrucciones claras |\n"
       "| Jue 19 | **Evaluación 2** (E2, 45 min) — el mar 17 no hay clase |\n"
       "| Lun 23 | Ética y uso responsable |\n"
       "| Mar 24 | Integración (práctica sin nota) |\n"
       "| Jue 26 | **Evaluación 3** (E3) |\n\n"
       "**Dos notas:** la primera es el promedio de E1 y E2; la segunda es E3.\n\n"
       "En cada clase escribimos y ejecutamos código y explicamos lo que obtenemos: no basta con ejecutarlo todo."),

    md("---\n\n## 📘 Concepto 1 · El mapa de la IA\n\n" + imagen("Diagrama 1 - El mapa de la IA.png", "El mapa de la IA")),
    md("### Regla y patrón\n\n"
       + idea("Regla", "instrucción que escribe una persona y que le dice a la máquina qué hacer en cada caso. No cambia sola.")
       + "\n\n"
       + idea("Patrón", "algo que se repite en los datos y que la máquina descubre sola, mirando muchos ejemplos.")
       + "\n\n" + ir_a("M1")),
    md("### IA, ML, DL e IA generativa\n\n"
       + idea("IA", "máquinas que hacen tareas que normalmente requieren inteligencia humana: aprender, razonar y decidir.")
       + "\n\n"
       + idea("Machine Learning (ML)", "la computadora descubre patrones en los datos y decide sin que le indiquen cómo.")
       + "\n\n"
       + idea("Deep Learning (DL)", "ML con redes neuronales de muchas capas; sirve para imágenes, voz y texto.")
       + "\n\n"
       + idea("IA generativa", "produce contenido nuevo (texto, imágenes, música) a partir de lo que aprendió. "
                              "Hoy se construye sobre todo con DL (por ejemplo, ChatGPT).")
       + "\n\n" + ir_a("M2")),
    md("### Cuando algo no calza\n\n"
       "A veces un ejemplo admite dos lecturas: para ubicarlo en el mapa nos falta saber cómo se construyó.\n\n"
       + ir_a("M3")),

    md("---\n\n## 📘 Concepto 2 · El recorrido de los datos\n\n"
       "Caso del diagrama: riego automatizado de una viña de Isla de Maipo, como Santa Ema (datos ficticios).\n\n"
       + imagen("Diagrama 2 - El pipeline.png", "El recorrido de los datos")),
    md("### Los 7 pasos\n\n"
       "1. Definir el problema (¿hay que regar mañana?).\n"
       "2. Reunir los datos y reconocer variables y etiqueta.\n"
       "3. Separar los datos en dos sets: el set de entrenamiento y el set de prueba.\n"
       "4. Entrenar el modelo con el set de entrenamiento.\n"
       "5. Predecir sobre el set de prueba.\n"
       "6. Evaluar cuántas veces acertó.\n"
       "7. Usar el modelo en casos nuevos y revisar.\n\n"
       "En las actividades de la página cambiamos de ejemplo: el sistema de climatización de una bodega de "
       "fermentación.\n\n"
       + ir_a_pagina(2, "a la actividad P1")),
    md("### Variables y etiqueta\n\n"
       + idea("Variables y etiqueta", "las variables son lo que el modelo recibe; la etiqueta es lo que queremos que prediga.")
       + "\n\n" + ir_a("P2")),
    md("### Entrenar y predecir\n\n"
       + idea("Entrenar y predecir", "entrenar es aprender de ejemplos que traen su respuesta; predecir es usar lo aprendido en un caso.")
       + "\n\n"
       + idea("Set de entrenamiento", "es donde la computadora aprende: ve las variables y la etiqueta.")
       + "\n\n"
       + idea("Set de prueba", "es donde vemos si es capaz de predecir: no ve la etiqueta cuando responde.")
       + "\n\n" + ir_a("P3")),
    md("### El set de prueba se guarda aparte\n\n"
       + idea("Prueba aparte", "si evaluamos con lo mismo que entrenamos, no sabemos cómo le irá con casos nuevos.")
       + "\n\n" + ir_a("P4")),

    md("---\n\n## 🎫 Ticket de salida\n\n"
       "Lo resolvemos en silencio, cada uno por su cuenta, y sin nota.\n\n"
       + ir_a_pagina(3, "al ticket de salida")),
    md("---\n\n## 🏁 Cierre\n\n"
       "**Objetivo de hoy:** ubicar ejemplos de IA en el mapa y ordenar el recorrido de los datos hasta la "
       "evaluación de un modelo, con curiosidad.\n\n"
       "- Del 1 al 5, ¿cuánto entendimos el objetivo de hoy? *(a viva voz)*\n"
       "- Volvemos al diagnóstico del comienzo: ¿qué idea cambiaríamos ahora? *(a viva voz)*\n"
       "- ¿En qué se nos notó hoy la curiosidad? *(a viva voz)*\n\n"
       "**Mañana:** entrenamos nuestro primer clasificador."),
]

cuaderno = {
    "cells": celdas,
    "metadata": {"colab": {"provenance": []}, "kernelspec": {"display_name": "Python 3", "name": "python3"},
                 "language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 5,
}
SALIDA.write_text(json.dumps(cuaderno, ensure_ascii=False, indent=1), encoding="utf-8")
print("Colab guía:", SALIDA.name, f"({len(celdas)} celdas, {SALIDA.stat().st_size // 1024} KB)")
