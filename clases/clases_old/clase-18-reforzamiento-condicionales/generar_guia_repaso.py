#!/usr/bin/env python3
"""
generar_guia_repaso.py — Genera "Clase 18 - Reforzamiento Condicionales - Guía de Repaso.ipynb"

Repaso express, enfocado en Bloque 6 (elif) y Bloque 7 (elif + if anidado) —
lo último que se vio en Clase 17 y a lo que la mayoría de las parejas no
alcanzó a llegar (Ejercicios 3 y 4). No repite teoría completa: la Dinámica
de la misma clase ya recicla los 4 ejercicios de Clase 17.

Sin autocorrección: las soluciones de todos los ítems (incluidos los tres
primeros) viven plegadas en una sección final sin encabezado markdown, para
que no aparezca en el índice de Colab.

Uso:
  python generar_guia_repaso.py
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


def build_notebook() -> dict:
    cells = [
        md_cell(
            "# 🔁 Repaso Express — elif y combinaciones\n\n"
            "Guía corta antes de la evaluación del **martes 21 de julio**. Se "
            "enfoca solo en `elif` y en combinarlo con `if` anidados — lo "
            "último que se vio en Clase 17 y a lo que menos parejas "
            "llegaron.\n\n"
            "**Cómo usarla:**\n"
            "1. Resuelve los **Ítems 1 a 3**, el **Desafío final** y los "
            "**Propuestos** por tu cuenta.\n"
            "2. Revisa tus respuestas con la sección de soluciones al final "
            "del documento — ábrelas recién después de intentarlo. No hay "
            "corrección automática: lo importante es que la **lógica** y el "
            "**resultado** calcen, aunque el texto exacto de tu `print` sea "
            "distinto."
        ),
        md_cell(
            "---\n\n## 🧩 Ítem 1\n\n"
            "Recuerda: solo se ejecuta la **primera** condición que sea "
            "`True`, de arriba hacia abajo — el orden importa.\n\n"
            "Una app de clima clasifica la temperatura de hoy en un nivel de "
            "alerta, para sugerir cómo vestirse antes de salir.\n\n"
            "**El programa debe:**\n"
            "- Clasificar `temperatura_grados` en **4 niveles**: helada "
            "(menor a 0°), fría (menor a 15°), templada (menor a 25°) y "
            "calurosa (25° o más)\n"
            "- Mostrar el mensaje correspondiente al nivel"
        ),
        code_cell("temperatura_grados = 3\n\n# Tu solución del Ítem 1\n"),
        md_cell(
            "---\n\n## 🧩 Ítem 2\n\n"
            "Recuerda: el `if` anidado va **dentro** de una sola rama del "
            "`elif`, no reemplaza a las demás.\n\n"
            "Una plataforma de streaming musical arma el mensaje de "
            "bienvenida según el plan de la persona. Si el plan es "
            "**premium**, revisa además si activó el audio en alta "
            "calidad (HD), porque eso cambia el mensaje.\n\n"
            "**El programa debe:**\n"
            "- Distinguir entre plan `\"basico\"`, `\"estandar\"` y `\"premium\"`\n"
            "- Si el plan es `\"premium\"`, verificar además si "
            "`audio_hd_activado` es `True`\n"
            "- Mostrar el mensaje correspondiente"
        ),
        code_cell(
            "plan_streaming = \"premium\"\naudio_hd_activado = True\n\n"
            "# Tu solución del Ítem 2\n"
        ),
        md_cell(
            "---\n\n## 🐛 Ítem 3\n\n"
            "Una veterinaria clasifica la urgencia de una mascota según sus "
            "síntomas, y si es **urgente**, revisa además si hay un turno "
            "disponible ahora mismo. El fragmento de abajo tiene **un solo "
            "error** — corrígelo directamente en la celda."
        ),
        code_cell(
            "nivel_sintomas = \"urgente\"\n"
            "turno_disponible = False\n"
            "\n"
            "if nivel_sintomas == \"leve\":\n"
            "    mensaje_veterinaria = \"Puede esperar a una hora normal.\"\n"
            "elif nivel_sintomas == \"moderado\":\n"
            "    mensaje_veterinaria = \"Se recomienda ver hoy mismo.\"\n"
            "elif nivel_sintomas == \"urgente\":\n"
            "    if turno_disponible:\n"
            "    mensaje_veterinaria = \"Atención inmediata: hay turno disponible ahora.\"\n"
            "    else:\n"
            "        mensaje_veterinaria = \"Urgencia: dirígete a la clínica de emergencia.\"\n"
            "\n"
            "print(\"Mensaje de la veterinaria:\", mensaje_veterinaria)"
        ),
        md_cell(
            "---\n\n## 🏁 Desafío final\n\n"
            "El sistema de notas del liceo entrega un mensaje según el "
            "promedio semestral. Si el promedio cae en el tramo más alto, "
            "revisa además si la asistencia es completa, porque eso habilita "
            "el ingreso al cuadro de honor.\n\n"
            "**El programa debe:**\n"
            "- Clasificar `promedio_semestral` en 4 tramos: insuficiente "
            "(menor a 4.0), aprobado (menor a 5.5), muy bueno (menor a 6.5) "
            "y destacado (6.5 o más)\n"
            "- Si el promedio es destacado, verificar además si "
            "`asistencia_completa` es `True` para el cuadro de honor\n"
            "- Mostrar el mensaje correspondiente\n\n"
            "Después de que te funcione con `promedio_semestral = 6.7` y "
            "`asistencia_completa = True`, cambia `asistencia_completa` a "
            "`False` y vuelve a ejecutar — el mensaje debería cambiar."
        ),
        code_cell("promedio_semestral = 6.7\nasistencia_completa = True\n\n# Tu solución del Desafío final\n"),
        md_cell(
            "---\n\n## 🌟 Propuestos\n\n"
            "Dos ejercicios opcionales, un poco más largos, para quien "
            "quiera seguir practicando."
        ),
        md_cell(
            "**Propuesto 1.** El celular avisa sobre el nivel de batería, y "
            "si está en nivel **crítico** revisa si el modo ahorro está "
            "activado, porque eso cambia cuánto tiempo más durará.\n\n"
            "**El programa debe:**\n"
            "- Clasificar `nivel_bateria` en 3 tramos: bueno (50% o más), "
            "medio (20% o más) y crítico (menos de 20%)\n"
            "- Si es crítico, verificar además si `modo_ahorro_activado` es "
            "`True`\n"
            "- Mostrar el mensaje correspondiente"
        ),
        code_cell("nivel_bateria = 15\nmodo_ahorro_activado = True\n\n# Tu solución del Propuesto 1\n"),
        md_cell(
            "**Propuesto 2.** Una tienda de streaming de películas aplica "
            "descuentos según el tipo de cuenta. Si la cuenta es **nueva**, "
            "revisa si la persona ingresó un código promocional válido, "
            "porque eso le da un descuento extra el primer mes.\n\n"
            "**El programa debe:**\n"
            "- Distinguir entre cuenta `\"nueva\"` y `\"antigua\"` (cualquier "
            "otro valor es \"no reconocida\")\n"
            "- Si la cuenta es `\"nueva\"`, verificar además si "
            "`codigo_promocional_valido` es `True`\n"
            "- Mostrar el mensaje correspondiente"
        ),
        code_cell(
            "tipo_cuenta = \"nueva\"\ncodigo_promocional_valido = False\n\n"
            "# Tu solución del Propuesto 2\n"
        ),
        md_cell(
            "---\n\n**✅ Soluciones**\n\n"
            "Ábrelas recién después de intentar cada una tú mismo/a. Los "
            "mensajes pueden estar redactados distinto a los tuyos — lo que "
            "importa es que la lógica y el resultado calcen.\n\n"
            "<details>\n<summary>💡 Solución Ítem 1</summary>\n\n"
            "```python\n"
            "temperatura_grados = 3\n"
            "\n"
            "if temperatura_grados < 0:\n"
            "    print(\"Alerta: ¡Abrígate mucho, viene helada!\")\n"
            "elif temperatura_grados < 15:\n"
            "    print(\"Frío: lleva chaqueta.\")\n"
            "elif temperatura_grados < 25:\n"
            "    print(\"Templado: con polerón basta.\")\n"
            "else:\n"
            "    print(\"Calor: usa ropa liviana.\")\n"
            ">> Frío: lleva chaqueta.\n"
            "```\n</details>\n\n"
            "<details>\n<summary>💡 Solución Ítem 2</summary>\n\n"
            "```python\n"
            "plan_streaming = \"premium\"\n"
            "audio_hd_activado = True\n"
            "\n"
            "if plan_streaming == \"basico\":\n"
            "    print(\"Plan básico: audio estándar.\")\n"
            "elif plan_streaming == \"estandar\":\n"
            "    print(\"Plan estándar: sin anuncios.\")\n"
            "elif plan_streaming == \"premium\":\n"
            "    if audio_hd_activado:\n"
            "        print(\"Premium HD: la mejor calidad disponible.\")\n"
            "    else:\n"
            "        print(\"Premium: audio estándar, activa el HD cuando quieras.\")\n"
            ">> Premium HD: la mejor calidad disponible.\n"
            "```\n</details>\n\n"
            "<details>\n<summary>💡 Solución Ítem 3</summary>\n\n"
            "```python\n"
            "nivel_sintomas = \"urgente\"\n"
            "turno_disponible = False\n"
            "\n"
            "if nivel_sintomas == \"leve\":\n"
            "    mensaje_veterinaria = \"Puede esperar a una hora normal.\"\n"
            "elif nivel_sintomas == \"moderado\":\n"
            "    mensaje_veterinaria = \"Se recomienda ver hoy mismo.\"\n"
            "elif nivel_sintomas == \"urgente\":\n"
            "    if turno_disponible:\n"
            "        mensaje_veterinaria = \"Atención inmediata: hay turno disponible ahora.\"\n"
            "    else:\n"
            "        mensaje_veterinaria = \"Urgencia: dirígete a la clínica de emergencia.\"\n"
            "\n"
            "print(\"Mensaje de la veterinaria:\", mensaje_veterinaria)\n"
            ">> Mensaje de la veterinaria: Urgencia: dirígete a la clínica de emergencia.\n"
            "```\n\n"
            "El error era de indentación: la línea "
            "`mensaje_veterinaria = \"Atención inmediata...\"` debía ir "
            "**dentro** del `if turno_disponible:`, con un nivel más de "
            "sangría.\n</details>\n\n"
            "<details>\n<summary>💡 Solución Desafío final</summary>\n\n"
            "```python\n"
            "promedio_semestral = 6.7\n"
            "asistencia_completa = True\n"
            "\n"
            "if promedio_semestral < 4.0:\n"
            "    print(\"Promedio insuficiente: exigencia mínima 4.0.\")\n"
            "elif promedio_semestral < 5.5:\n"
            "    print(\"Promedio aprobado: sigue así.\")\n"
            "elif promedio_semestral < 6.5:\n"
            "    print(\"Muy buen promedio: ¡felicitaciones!\")\n"
            "else:\n"
            "    if asistencia_completa:\n"
            "        print(\"¡Cuadro de honor! Promedio destacado y asistencia perfecta.\")\n"
            "    else:\n"
            "        print(\"Promedio destacado, pero te faltó asistencia perfecta para el cuadro de honor.\")\n"
            ">> ¡Cuadro de honor! Promedio destacado y asistencia perfecta.\n"
            "```\n\n"
            "Con `asistencia_completa = False`, el mensaje cambia a "
            "\"Promedio destacado, pero te faltó asistencia perfecta...\" — "
            "aunque el promedio sea el mismo.\n"
            "</details>\n\n"
            "<details>\n<summary>💡 Solución Propuesto 1</summary>\n\n"
            "```python\n"
            "nivel_bateria = 15\n"
            "modo_ahorro_activado = True\n"
            "\n"
            "if nivel_bateria >= 50:\n"
            "    print(\"Batería en buen nivel.\")\n"
            "elif nivel_bateria >= 20:\n"
            "    print(\"Batería media: considera cargar pronto.\")\n"
            "else:\n"
            "    if modo_ahorro_activado:\n"
            "        print(\"Batería crítica, pero el modo ahorro está activo: aguanta más tiempo.\")\n"
            "    else:\n"
            "        print(\"Batería crítica: carga el celular ahora.\")\n"
            ">> Batería crítica, pero el modo ahorro está activo: aguanta más tiempo.\n"
            "```\n</details>\n\n"
            "<details>\n<summary>💡 Solución Propuesto 2</summary>\n\n"
            "```python\n"
            "tipo_cuenta = \"nueva\"\n"
            "codigo_promocional_valido = False\n"
            "\n"
            "if tipo_cuenta == \"nueva\":\n"
            "    if codigo_promocional_valido:\n"
            "        print(\"Bienvenida con 50% de descuento el primer mes.\")\n"
            "    else:\n"
            "        print(\"Bienvenida con 20% de descuento el primer mes.\")\n"
            "elif tipo_cuenta == \"antigua\":\n"
            "    print(\"Sin descuento por renovación.\")\n"
            "else:\n"
            "    print(\"Tipo de cuenta no reconocida.\")\n"
            ">> Bienvenida con 20% de descuento el primer mes.\n"
            "```\n</details>"
        ),
        md_cell(
            "---\n\n## 🏁 Cierre\n\n"
            "Repasando y ejercitando así, te va a ir increíble en la "
            "evaluación del martes 21. ¡Confía en tu proceso y nos vemos "
            "ese día! 💪"
        ),
    ]

    return notebook(cells, "Clase 18 - Reforzamiento Condicionales - Guía de Repaso")


if __name__ == "__main__":
    import json
    import os

    base = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(base, "Clase 18 - Reforzamiento Condicionales - Guía de Repaso.ipynb")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(build_notebook(), f, ensure_ascii=False, indent=1)

    print("Generado:", out_path)
