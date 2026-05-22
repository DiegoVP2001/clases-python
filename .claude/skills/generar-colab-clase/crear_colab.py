#!/usr/bin/env python3
"""
crear_colab.py — Generador de Colab de clase a partir de 00-spec.md

Uso:
    python crear_colab.py <ruta_a_00-spec.md> <ruta_salida_01-clase.ipynb>

Ejemplo:
    python crear_colab.py clases/clase-07-input/00-spec.md clases/clase-07-input/01-clase.ipynb

Lee la especificación de una clase, parsea sus secciones, y produce un
Jupyter notebook (.ipynb) con la estructura estándar de las clases de Python
4to medio, listo para abrir en Google Colab.

Requiere: nbformat (instalar con: pip install nbformat)
"""

import sys
import re
import json
import textwrap
from pathlib import Path

try:
    import nbformat
    from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
except ImportError:
    print("ERROR: nbformat no está instalado. Instálalo con:")
    print("    pip install nbformat")
    sys.exit(1)


# =====================================================================
# PARSER DEL SPEC
# =====================================================================

def parsear_spec(ruta_spec: Path) -> dict:
    """Parsea 00-spec.md y devuelve un diccionario con todas las secciones."""
    contenido = ruta_spec.read_text(encoding="utf-8")

    spec = {
        "numero_clase": None,
        "tema": None,
        "fecha_aprobacion": None,
        "url_picuino": None,
        "contexto": {},
        "objetivo": None,
        "proposito": None,
        "haz_ahora": None,
        "icn": {"conceptos": [], "ejemplos": [], "errores": []},
        "guiada": {"situacion": None, "variables": None, "pasos": [], "resultado": None},
        "independiente": [],
        "ticket": {"tipo": None, "tarea": None, "entrega": None},
        "cierre": [],
        "decisiones": None,
    }

    # Encabezado: "# Clase 07 — La función input()" o "# Clase 8a — ..."
    match_titulo = re.search(r"^#\s+Clase\s+(\w+)\s*[—\-–]\s*(.+)$", contenido, re.MULTILINE)
    if match_titulo:
        raw = match_titulo.group(1)
        spec["numero_clase"] = int(raw) if raw.isdigit() else raw
        spec["tema"] = match_titulo.group(2).strip()

    # Estado
    match_estado = re.search(r"\*\*Estado:\*\*\s*Spec aprobada\s*[—\-–]\s*(\S+)", contenido)
    if match_estado:
        spec["fecha_aprobacion"] = match_estado.group(1)

    # URL Picuino
    match_url = re.search(r"\*\*URL Picuino:\*\*\s*(\S+)", contenido)
    if match_url:
        spec["url_picuino"] = match_url.group(1)

    # Contexto (lista de campos clave-valor)
    seccion_contexto = extraer_seccion(contenido, "## Contexto", "## Objetivo")
    if seccion_contexto:
        for linea in seccion_contexto.split("\n"):
            match_kv = re.match(r"^-\s+\*\*([^:]+):\*\*\s+(.+)$", linea.strip())
            if match_kv:
                clave = match_kv.group(1).strip()
                valor = match_kv.group(2).strip()
                spec["contexto"][clave] = valor

    # Objetivo
    spec["objetivo"] = extraer_seccion(contenido, "## Objetivo", "## Propósito", limpiar=True)

    # Propósito
    proposito_raw = extraer_seccion(contenido, "## Propósito", "## Estructura de la clase", limpiar=True)
    if proposito_raw:
        # Quita los ">" iniciales si el propósito viene como blockquote
        spec["proposito"] = "\n".join(
            l.lstrip("> ").rstrip() for l in proposito_raw.split("\n")
        ).strip()

    # Haz Ahora (strip marcador de tiempo como "(10 min)")
    haz_raw = extraer_seccion(contenido, "### 1. Haz Ahora", "### 2.", limpiar=True)
    spec["haz_ahora"] = re.sub(r"^\s*\(\d+\s*min\)\s*", "", haz_raw or "").strip()

    # ICN
    icn_raw = extraer_seccion(contenido, "### 2. Introducción al Contenido Nuevo", "### 3.", limpiar=True)
    if icn_raw:
        spec["icn"] = parsear_icn(icn_raw)

    # Práctica Guiada
    guiada_raw = extraer_seccion(contenido, "### 3. Práctica Guiada", "### 4.", limpiar=True)
    if guiada_raw:
        spec["guiada"] = parsear_guiada(guiada_raw)

    # Práctica Independiente
    indep_raw = extraer_seccion(contenido, "### 4. Práctica Independiente", "### 5.", limpiar=True)
    if indep_raw:
        spec["independiente"] = parsear_independiente(indep_raw)

    # Ticket
    ticket_raw = extraer_seccion(contenido, "### 5. Ticket de Salida", "### Cierre", limpiar=True)
    if ticket_raw:
        spec["ticket"] = parsear_ticket(ticket_raw)

    # Cierre (acepta "### Cierre y metacognición" o "### Cierre (N min)" o "### Cierre")
    cierre_raw = extraer_seccion(contenido, "### Cierre", "## Decisiones", limpiar=True)
    if cierre_raw:
        spec["cierre"] = [
            re.sub(r"^\d+\.\s*", "", l.strip())
            for l in cierre_raw.split("\n")
            if re.match(r"^\d+\.", l.strip())
        ]

    # Decisiones
    spec["decisiones"] = extraer_seccion(contenido, "## Decisiones de diseño relevantes", None, limpiar=True)

    return spec


def extraer_seccion(texto: str, encabezado_inicio: str, encabezado_fin: str | None, limpiar: bool = False) -> str | None:
    """Extrae el contenido entre dos encabezados de markdown."""
    inicio_idx = texto.find(encabezado_inicio)
    if inicio_idx == -1:
        return None
    inicio_idx += len(encabezado_inicio)

    if encabezado_fin:
        fin_idx = texto.find(encabezado_fin, inicio_idx)
        if fin_idx == -1:
            seccion = texto[inicio_idx:]
        else:
            seccion = texto[inicio_idx:fin_idx]
    else:
        seccion = texto[inicio_idx:]

    if limpiar:
        # Quita separadores --- al final y espacios sobrantes
        seccion = re.sub(r"\n\s*---\s*\n", "\n", seccion)
        seccion = seccion.strip()
    return seccion


def parsear_icn(texto: str) -> dict:
    """Parsea la sección de Introducción al Contenido Nuevo.
    Soporta formato enriquecido (**Concepto N: nombre**) y formato antiguo (**Conceptos:**).
    Mantiene el orden de conceptos y demostraciones tal como aparecen en el spec.
    """
    icn = {"items": [], "conceptos": [], "ejemplos": [], "errores": "", "demostraciones": []}

    if re.search(r"\*\*Concepto\s+\d+:", texto):
        # Formato enriquecido: split por Concepto o Demostración, manteniendo orden
        patron = r"(\*\*(?:Concepto\s+\d+|Demostración):\s*[^*\n]+\*\*)"
        partes = re.split(patron, texto)

        for i in range(1, len(partes), 2):
            header = partes[i]
            content = partes[i + 1] if i + 1 < len(partes) else ""

            if re.match(r"\*\*Concepto\s+\d+:", header):
                m_titulo = re.search(r"\*\*Concepto\s+\d+:\s*([^*\n]+)\*\*", header)
                titulo = m_titulo.group(1).strip() if m_titulo else header
                concepto = {"tipo": "concepto", "titulo": titulo, "definicion": None, "ejemplo": None, "idea_clave": None}

                m_def = re.search(r"- Definición:\s*(.+?)(?=- Ejemplo:|- Idea clave:|\Z)", content, re.DOTALL)
                if m_def:
                    concepto["definicion"] = m_def.group(1).strip()

                m_ej = re.search(r"- Ejemplo:\s*\n\s*```python\n(.*?)```", content, re.DOTALL)
                if m_ej:
                    concepto["ejemplo"] = textwrap.dedent(m_ej.group(1)).strip()

                m_ik = re.search(r"- Idea clave:\s*(.+?)(?=\*\*|\Z)", content, re.DOTALL)
                if m_ik:
                    concepto["idea_clave"] = m_ik.group(1).strip()

                icn["items"].append(concepto)
                icn["conceptos"].append(concepto)

            elif "Demostración" in header:
                m_titulo = re.search(r"\*\*Demostración:\s*([^*\n]+)\*\*", header)
                titulo = m_titulo.group(1).strip() if m_titulo else header
                demo = {"tipo": "demo", "titulo": titulo, "subtitulo": None, "filas": []}

                m_sub = re.match(r"Subtítulo:\s*(.+)", content.strip())
                if m_sub:
                    demo["subtitulo"] = m_sub.group(1).strip()

                for fila_m in re.finditer(r"- Fila:\s*(.+)", content):
                    campos = [p.strip() for p in fila_m.group(1).split("|")]
                    demo["filas"].append({
                        "etiqueta": campos[0] if len(campos) > 0 else "",
                        "codigo": campos[1] if len(campos) > 1 else "",
                        "resultado": campos[2] if len(campos) > 2 else "",
                    })

                icn["items"].append(demo)
                icn["demostraciones"].append(demo)
    else:
        # Formato antiguo: **Conceptos:** lista numerada + **Ejemplos a usar:**
        match_conceptos = re.search(r"\*\*Conceptos:\*\*\s*\n(.*?)(?=\*\*|\Z)", texto, re.DOTALL)
        if match_conceptos:
            bloque = match_conceptos.group(1)
            icn["conceptos"] = [
                re.sub(r"^\d+\.\s*", "", l.strip())
                for l in bloque.split("\n")
                if re.match(r"^\d+\.", l.strip())
            ]
        match_ejemplos = re.search(r"\*\*Ejemplos a usar:\*\*\s*\n```python\n(.*?)```", texto, re.DOTALL)
        if match_ejemplos:
            icn["ejemplos"].append(match_ejemplos.group(1).rstrip())

    # Errores típicos: tabla markdown
    match_errores = re.search(r"\*\*Errores típicos:\*\*\s*\n(\|.*?)(?=\n\n|\Z)", texto, re.DOTALL)
    if match_errores:
        icn["errores"] = match_errores.group(1).strip()

    return icn


def parsear_guiada(texto: str) -> dict:
    """Parsea la sección de Práctica Guiada."""
    guiada = {"situacion": None, "variables": None, "pasos": [], "resultado": None, "solucion": None}

    match_situacion = re.search(r"\*\*Situación:\*\*\s*(.+?)(?=\*\*|\Z)", texto, re.DOTALL)
    if match_situacion:
        guiada["situacion"] = match_situacion.group(1).strip()

    match_variables = re.search(r"\*\*Variables:\*\*\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if match_variables:
        guiada["variables"] = textwrap.dedent(match_variables.group(1)).strip()

    match_pasos = re.search(r"\*\*Pasos guiados:\*\*\s*\n(.*?)(?=\*\*|\Z)", texto, re.DOTALL)
    if match_pasos:
        bloque = match_pasos.group(1)
        guiada["pasos"] = [
            re.sub(r"^\d+\.\s*", "", l.strip())
            for l in bloque.split("\n")
            if re.match(r"^\d+\.", l.strip())
        ]

    match_resultado = re.search(r"\*\*Resultado esperado:\*\*\s*\n```\n(.*?)```", texto, re.DOTALL)
    if match_resultado:
        guiada["resultado"] = match_resultado.group(1).rstrip()

    match_solucion = re.search(r"- Solución:\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if match_solucion:
        guiada["solucion"] = textwrap.dedent(match_solucion.group(1)).strip()

    return guiada


def parsear_independiente(texto: str) -> list:
    """Parsea los ejercicios de Práctica Independiente."""
    ejercicios = []
    # Cada ejercicio empieza con "**Ejercicio N — ...**"
    bloques = re.split(r"\*\*Ejercicio\s+(\d+)\s*[—\-–]\s*([^*]+)\*\*", texto)
    # Después del split, los grupos vienen como: [vacío, num, titulo, contenido, num, titulo, contenido, ...]
    for i in range(1, len(bloques), 3):
        if i + 2 >= len(bloques):
            break
        num = bloques[i].strip()
        titulo = bloques[i + 1].strip()
        contenido = bloques[i + 2].strip()

        ejercicio = {"numero": num, "titulo": titulo, "enunciado": None, "resultado": None, "solucion": None}

        # Extraer solución oculta (- Solución: ```python ... ```)
        match_solucion = re.search(r"- Solución:\s*\n```python\n(.*?)```", contenido, re.DOTALL)
        if match_solucion:
            ejercicio["solucion"] = textwrap.dedent(match_solucion.group(1)).strip()
            contenido = contenido[:match_solucion.start()].strip()

        # Separar enunciado y resultado esperado
        match_resultado = re.search(r"Resultado esperado:\s*\n```\n(.*?)```", contenido, re.DOTALL)
        if match_resultado:
            ejercicio["resultado"] = match_resultado.group(1).rstrip()
            ejercicio["enunciado"] = contenido[:match_resultado.start()].strip()
        else:
            ejercicio["enunciado"] = contenido

        ejercicios.append(ejercicio)

    return ejercicios


def parsear_ticket(texto: str) -> dict:
    """Parsea la sección de Ticket de Salida.
    Acepta formato estructurado (**Tarea:**/**Entrega:**) o texto libre.
    """
    ticket = {"tipo": None, "tarea": None, "entrega": None, "solucion": None}
    match_sol = re.search(r"- Solución:\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if match_sol:
        ticket["solucion"] = textwrap.dedent(match_sol.group(1)).strip()
        texto = texto[:match_sol.start()].strip()

    match_tipo = re.search(r"\*\*Tipo:\*\*\s*(.+)", texto)
    if match_tipo:
        ticket["tipo"] = match_tipo.group(1).strip()

    match_tarea = re.search(r"\*\*Tarea:\*\*\s*(.+?)(?=\*\*Entrega|\Z)", texto, re.DOTALL)
    if match_tarea:
        ticket["tarea"] = match_tarea.group(1).strip().strip("*").strip()

    match_entrega = re.search(r"\*\*Entrega:\*\*\s*(.+)", texto)
    if match_entrega:
        ticket["entrega"] = match_entrega.group(1).strip()

    # Si no hay **Tarea:**, usar el texto completo (sin marcadores de tiempo como "(8 min)")
    if not ticket["tarea"]:
        limpio = re.sub(r"^\s*\(\d+\s*min\)\s*", "", texto.strip())
        ticket["tarea"] = limpio.strip()

    return ticket


# =====================================================================
# CONSTRUCCIÓN DEL NOTEBOOK
# =====================================================================

def construir_notebook(spec: dict) -> nbformat.NotebookNode:
    """Construye el objeto notebook a partir del spec parseado."""
    nb = new_notebook()
    nb.cells = []

    # --- ENCABEZADO ---
    nb.cells.append(new_markdown_cell(generar_encabezado(spec)))

    # --- OBJETIVO Y PROPÓSITO ---
    nb.cells.append(new_markdown_cell(generar_objetivo_proposito(spec)))

    # --- 1. HAZ AHORA ---
    nb.cells.append(new_markdown_cell(generar_seccion_haz_ahora(spec)))
    nb.cells.append(new_markdown_cell("**Mis respuestas:**\n\n1. \n2. \n3. \n4. \n5. \n6. "))

    # --- 2. INTRODUCCIÓN AL CONTENIDO NUEVO ---
    nb.cells.append(new_markdown_cell(generar_seccion_icn_intro(spec)))
    # Formato enriquecido: procesar items en orden (conceptos y demos intercalados)
    if spec["icn"].get("items"):
        for item in spec["icn"]["items"]:
            if item["tipo"] == "concepto":
                nb.cells.append(new_markdown_cell(generar_concepto_markdown(item)))
                if item.get("ejemplo"):
                    nb.cells.append(new_code_cell(item["ejemplo"]))
            elif item["tipo"] == "demo":
                nb.cells.append(new_markdown_cell(generar_demo_markdown(item)))
                nb.cells.append(new_code_cell(generar_demo_codigo(item)))
    elif spec["icn"]["ejemplos"]:
        # Formato antiguo: ejemplos sueltos
        for ejemplo in spec["icn"]["ejemplos"]:
            nb.cells.append(new_code_cell(ejemplo))
    # Tabla de errores como markdown
    if spec["icn"]["errores"]:
        nb.cells.append(new_markdown_cell(
            "#### ⚠️ Errores típicos a evitar\n\n" + spec["icn"]["errores"]
        ))

    # --- 3. PRÁCTICA GUIADA ---
    nb.cells.append(new_markdown_cell(generar_seccion_guiada_intro(spec)))
    nb.cells.append(new_code_cell("# Construye aquí el programa paso a paso siguiendo las indicaciones\n"))

    # --- 4. PRÁCTICA INDEPENDIENTE ---
    nb.cells.append(new_markdown_cell(generar_seccion_independiente_intro(spec)))
    for ejercicio in spec["independiente"]:
        nb.cells.append(new_markdown_cell(generar_ejercicio_independiente(ejercicio)))
        nb.cells.append(new_code_cell(f"# Tu solución del Ejercicio {ejercicio['numero']}\n"))

    # --- 5. TICKET DE SALIDA ---
    nb.cells.append(new_markdown_cell(generar_seccion_ticket(spec)))
    nb.cells.append(new_code_cell("# Tu solución del ticket de salida\n"))

    # --- CIERRE ---
    nb.cells.append(new_markdown_cell(generar_seccion_cierre(spec)))
    nb.cells.append(new_markdown_cell("---\n\n"))

    # --- SOLUCIONES (sección separada al final) ---
    nb.cells.append(new_markdown_cell(generar_seccion_soluciones(spec)))

    return nb


def generar_encabezado(spec: dict) -> str:
    n = spec['numero_clase']
    num = f"{n:02d}" if isinstance(n, int) else (str(n) if n is not None else "??")
    duracion = spec["contexto"].get("Duración", "90 min")
    curso = spec["contexto"].get("Curso", "4to medio")
    return f"""# 🐍 Clase {num} — {spec['tema']}

**Curso:** {curso}  |  **Duración:** {duracion}  |  **Plataforma:** Google Colab

---"""


def generar_objetivo_proposito(spec: dict) -> str:
    contenidos_previos = spec["contexto"].get("Contenidos previos asumidos", "")
    contenidos_nuevos = spec["contexto"].get("Contenidos nuevos", "")
    bloque = "## 🎯 Objetivo de la clase\n\n"
    bloque += f"{spec['objetivo']}\n\n"
    bloque += "## 💡 ¿Para qué te sirve?\n\n"
    bloque += f"> {spec['proposito']}\n\n"
    if contenidos_previos or contenidos_nuevos:
        bloque += "---\n\n"
        if contenidos_previos:
            bloque += f"**Lo que ya sabes:** {contenidos_previos}\n\n"
        if contenidos_nuevos:
            bloque += f"**Lo que aprenderás hoy:** {contenidos_nuevos}\n"
    return bloque


def generar_seccion_haz_ahora(spec: dict) -> str:
    bloque = "---\n\n## 1️⃣ Haz Ahora\n\n"
    if spec["haz_ahora"]:
        bloque += spec["haz_ahora"]
    return bloque


def generar_seccion_icn_intro(spec: dict) -> str:
    bloque = "---\n\n## 2️⃣ Introducción al Contenido Nuevo\n\n"
    if spec["icn"]["conceptos"] and isinstance(spec["icn"]["conceptos"][0], dict):
        bloque += "Estudia cada concepto, ejecuta los ejemplos y observa el resultado:\n"
    else:
        if spec["icn"]["conceptos"]:
            bloque += "### Conceptos clave de hoy\n\n"
            for i, concepto in enumerate(spec["icn"]["conceptos"], 1):
                bloque += f"{i}. {concepto}\n"
            bloque += "\n"
        bloque += "### Ejemplos para ejecutar\n\n"
        bloque += "Ejecuta cada celda (Shift+Enter) y observa qué pasa:\n"
    return bloque


def generar_concepto_markdown(concepto: dict) -> str:
    bloque = f"### 💡 {concepto['titulo']}\n\n"
    if concepto["definicion"]:
        bloque += concepto["definicion"] + "\n\n"
    if concepto["idea_clave"]:
        bloque += f"**Idea clave:** _{concepto['idea_clave']}_\n"
    return bloque


def generar_solucion_oculta(codigo: str, etiqueta: str) -> str:
    return (
        f"<details>\n"
        f"<summary>🔓 Ver solución — {etiqueta} (intenta primero)</summary>\n\n"
        f"```python\n{codigo}\n```\n\n"
        f"</details>"
    )


def generar_demo_markdown(demo: dict) -> str:
    bloque = f"### 🔍 Demostración: {demo['titulo']}\n\n"
    if demo["subtitulo"]:
        bloque += f"_{demo['subtitulo']}_\n\n"
    bloque += "Ejecuta la celda y observa qué devuelve cada operador:\n"
    return bloque


def generar_demo_codigo(demo: dict) -> str:
    lineas = []
    for fila in demo["filas"]:
        etiqueta = fila["etiqueta"]
        codigo = fila["codigo"]
        resultado = fila["resultado"]
        comentario = f"  # {resultado}" if resultado else ""
        lineas.append(f"# {etiqueta}")
        lineas.append(f"print({codigo}){comentario}")
        lineas.append("")
    return "\n".join(lineas).rstrip()


def generar_seccion_guiada_intro(spec: dict) -> str:
    bloque = "---\n\n## 3️⃣ Práctica Guiada\n\n"
    if spec["guiada"]["situacion"]:
        bloque += f"**Situación:** {spec['guiada']['situacion']}\n\n"
    if spec["guiada"]["pasos"]:
        bloque += "**Vamos a construirlo paso a paso:**\n\n"
        for i, paso in enumerate(spec["guiada"]["pasos"], 1):
            bloque += f"{i}. {paso}\n"
        bloque += "\n"
    if spec["guiada"]["resultado"]:
        bloque += "**Resultado esperado al final:**\n\n```\n"
        bloque += spec["guiada"]["resultado"]
        bloque += "\n```\n"
    return bloque


def generar_solucion_guiada(spec: dict) -> str:
    bloque = "<details>\n<summary>🔓 Ver solución de la Práctica Guiada (después de intentarlo)</summary>\n\n"
    if spec["guiada"]["variables"]:
        bloque += "```python\n" + spec["guiada"]["variables"] + "\n"
        bloque += "\nprint(\"=== PERFIL ===\")\n"
        bloque += "# (completar el resumen según el caso)\n```\n\n"
    bloque += "</details>"
    return bloque


def generar_seccion_independiente_intro(spec: dict) -> str:
    return "---\n\n## 4️⃣ Práctica Independiente\n\nResuelve los siguientes ejercicios de forma individual. Si te trabas, pregunta al profe."


def generar_ejercicio_independiente(ejercicio: dict) -> str:
    bloque = f"### Ejercicio {ejercicio['numero']} — {ejercicio['titulo']}\n\n"
    if ejercicio["enunciado"]:
        bloque += ejercicio["enunciado"] + "\n\n"
    if ejercicio["resultado"]:
        bloque += "**Resultado esperado:**\n\n```\n" + ejercicio["resultado"] + "\n```\n"
    return bloque


def generar_seccion_ticket(spec: dict) -> str:
    bloque = "---\n\n## 5️⃣ Ticket de Salida\n\n"
    bloque += "> 🎫 **Esta es tu evidencia individual de la clase de hoy.**\n\n"
    if spec["ticket"]["tarea"]:
        bloque += spec["ticket"]["tarea"] + "\n\n"
    if spec["ticket"]["entrega"]:
        bloque += f"**Entrega:** {spec['ticket']['entrega']}\n"
    return bloque


def generar_seccion_cierre(spec: dict) -> str:
    bloque = "---\n\n## 🧠 Cierre y reflexión\n\n"
    bloque += "Antes de irte, piensa (no hay que entregar):\n\n"
    for i, pregunta in enumerate(spec["cierre"], 1):
        bloque += f"{i}. {pregunta}\n"
    return bloque


def generar_seccion_soluciones(spec: dict) -> str:
    bloque = "---\n\n## 📋 Soluciones\n\n"
    bloque += "> Intenta resolver cada ejercicio antes de mirar aquí.\n\n"

    # Solución de la Práctica Guiada
    if spec["guiada"].get("solucion"):
        bloque += "<details>\n"
        bloque += "<summary>🔓 Práctica Guiada</summary>\n\n"
        bloque += f"```python\n{spec['guiada']['solucion']}\n```\n\n"
        bloque += "</details>\n\n"

    # Soluciones de ejercicios independientes
    for ejercicio in spec["independiente"]:
        if ejercicio.get("solucion"):
            bloque += "<details>\n"
            bloque += f"<summary>🔓 Ejercicio {ejercicio['numero']} — {ejercicio['titulo']}</summary>\n\n"
            bloque += f"```python\n{ejercicio['solucion']}\n```\n\n"
            bloque += "</details>\n\n"

    # Solución del Ticket
    if spec["ticket"].get("solucion"):
        bloque += "<details>\n"
        bloque += "<summary>🔓 Ticket de Salida</summary>\n\n"
        bloque += f"```python\n{spec['ticket']['solucion']}\n```\n\n"
        bloque += "</details>\n"

    return bloque


# =====================================================================
# MAIN
# =====================================================================

def main():
    if len(sys.argv) != 3:
        print("Uso: python crear_colab.py <ruta_spec.md> <ruta_salida.ipynb>")
        sys.exit(1)

    ruta_spec = Path(sys.argv[1])
    ruta_salida = Path(sys.argv[2])

    if not ruta_spec.exists():
        print(f"ERROR: no existe el archivo {ruta_spec}")
        sys.exit(1)

    print(f"📖 Leyendo spec: {ruta_spec}")
    spec = parsear_spec(ruta_spec)

    print(f"✅ Spec parseado: Clase {spec['numero_clase']} — {spec['tema']}")
    print(f"   - {len(spec['icn']['conceptos'])} conceptos en ICN")
    print(f"   - {len(spec['guiada']['pasos'])} pasos en guiada")
    print(f"   - {len(spec['independiente'])} ejercicios independientes")

    print(f"🛠️  Construyendo notebook...")
    nb = construir_notebook(spec)

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    with ruta_salida.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"💾 Notebook guardado en: {ruta_salida}")
    print(f"📤 Súbelo a Colab desde https://colab.research.google.com (Archivo → Subir cuaderno)")


if __name__ == "__main__":
    main()
