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

TICKET_SALIDA_FORM_URL = "https://forms.gle/sjRpbgmQzrpkEBsH9"
import base64
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
        "ticket_mcq": [],
        "cierre": [],
        "cierre_estructurado": None,
        "respuestas_haz_ahora": None,
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

    # Propósito — stop at next ## section to avoid capturing intermediate sections
    proposito_raw = extraer_seccion(contenido, "## Propósito", "## Estructura de la clase", limpiar=True)
    if proposito_raw:
        next_h2 = re.search(r"\n## ", proposito_raw)
        if next_h2:
            proposito_raw = proposito_raw[:next_h2.start()]
        spec["proposito"] = "\n".join(
            l.lstrip("> ").rstrip() for l in proposito_raw.split("\n")
        ).strip()

    # Haz Ahora (strip marcador de tiempo como "(10 min)" y extrae respuestas esperadas)
    haz_raw = extraer_seccion(contenido, "### 1. Haz Ahora", "### 2.", limpiar=True)
    if haz_raw:
        match_resp = re.search(
            r"\*\*Respuestas (?:del Haz Ahora|esperadas):\*\*\s*\n(.*)",
            haz_raw, re.DOTALL
        )
        if match_resp:
            spec["respuestas_haz_ahora"] = match_resp.group(1).strip()
            haz_raw = haz_raw[:match_resp.start()].strip()
        spec["haz_ahora"] = re.sub(r"^\s*\(\d+\s*min\)\s*", "", haz_raw).strip()
    else:
        spec["haz_ahora"] = ""

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

    # Ticket (MCQ — 2-3 preguntas de 4 alternativas, solo van al Solucionario)
    ticket_raw = extraer_seccion(contenido, "### 5. Ticket de Salida", "### Cierre", limpiar=True)
    if ticket_raw:
        spec["ticket_mcq"] = parsear_ticket_mcq(ticket_raw)

    # Cierre (acepta "### Cierre y metacognición" o "### Cierre (N min)" o "### Cierre")
    cierre_raw = extraer_seccion(contenido, "### Cierre", "## Decisiones", limpiar=True)
    if cierre_raw:
        if "**Objetivo de la clase" in cierre_raw:
            spec["cierre_estructurado"] = parsear_cierre_estructurado(cierre_raw)
        else:
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

    if re.search(r"\*\*(?:Concepto\s+\d+|Comparación):", texto):
        # Formato enriquecido: split por Concepto, Demostración o Comparación, manteniendo orden
        patron = r"(\*\*(?:Concepto\s+\d+|Demostración|Comparación):\s*[^*\n]+\*\*)"
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
                    raw_ej = textwrap.dedent(m_ej.group(1)).strip()
                    # Convert ">> output" lines to "# >> output" so they are valid Python comments
                    concepto["ejemplo"] = re.sub(r"^>>", "# >>", raw_ej, flags=re.MULTILINE)

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

            elif "Comparación" in header:
                # Tabla lado a lado (ej: comparar dos sintaxis relacionadas, como for y range()).
                # El contenido es la tabla HTML (u otro markdown) tal cual, más un ejemplo
                # ejecutable opcional con el mismo formato "- Ejemplo:" que un concepto.
                m_titulo = re.search(r"\*\*Comparación:\s*([^*\n]+)\*\*", header)
                titulo = m_titulo.group(1).strip() if m_titulo else header
                comparacion = {"tipo": "comparacion", "titulo": titulo, "contenido": None, "ejemplo": None}

                m_ej = re.search(r"- Ejemplo:\s*\n\s*```python\n(.*?)```", content, re.DOTALL)
                if m_ej:
                    raw_ej = textwrap.dedent(m_ej.group(1)).strip()
                    comparacion["ejemplo"] = re.sub(r"^>>", "# >>", raw_ej, flags=re.MULTILINE)
                    content = content[:m_ej.start()].strip()

                comparacion["contenido"] = content.strip()
                icn["items"].append(comparacion)
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
    guiada = {
        "situacion": None, "variables": None, "pasos": [], "pasos_tabla": [],
        "resultado": None, "solucion": None, "codigo_error": None,
    }

    match_situacion = re.search(r"\*\*Situación:\*\*\s*(.+?)(?=\*\*|\Z)", texto, re.DOTALL)
    if match_situacion:
        guiada["situacion"] = match_situacion.group(1).strip()

    match_variables = re.search(r"\*\*Variables:\*\*\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if match_variables:
        guiada["variables"] = textwrap.dedent(match_variables.group(1)).strip()

    match_codigo_error = re.search(r"\*\*Código con error:\*\*\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if match_codigo_error:
        guiada["codigo_error"] = textwrap.dedent(match_codigo_error.group(1)).strip()

    if re.search(r"\*\*Pasos guiados \(tabla\):\*\*", texto):
        # Formato tabla (default actual): cada paso trae su propio resultado esperado,
        # se renderiza como tabla de 2 columnas en vez de lista + bloque de resultado separado.
        for m in re.finditer(
            r"-\s*Paso\s+\d+:\s*(.+?)\n\s*Resultado:\s*\n\s*```\n(.*?)```", texto, re.DOTALL
        ):
            guiada["pasos_tabla"].append({
                "paso": m.group(1).strip(),
                "resultado": textwrap.dedent(m.group(2)).strip(),
            })
    else:
        # Formato antiguo (retrocompatible): lista de pasos + un solo bloque de resultado al final.
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

    match_solucion = re.search(r"- Solución:\s*\n\s*```python\n(.*?)```", texto, re.DOTALL)
    if match_solucion:
        guiada["solucion"] = textwrap.dedent(match_solucion.group(1)).strip()

    return guiada


def parsear_independiente(texto: str) -> list:
    """Parsea los ejercicios de Práctica Independiente. Soporta Parte A/B."""
    ejercicios = []
    bloques = re.split(r"\*\*Ejercicio\s+(\d+)\s*[—\-–]\s*([^*]+)\*\*", texto)
    for i in range(1, len(bloques), 3):
        if i + 2 >= len(bloques):
            break
        num = bloques[i].strip()
        titulo = bloques[i + 1].strip()
        contenido = bloques[i + 2].strip()

        ejercicio = {
            "numero": num, "titulo": titulo,
            "contexto": None, "enunciado": None,
            "parte_a": None, "parte_b": None,
            "resultado": None, "codigo_error": None,
            "solucion": None, "solucion_a": None, "solucion_b": None,
        }

        # Extraer soluciones en orden inverso (B antes que A) para evitar solapamiento
        match_sol_b = re.search(r"- Solución Parte B:\s*\n\s*```python\n(.*?)```", contenido, re.DOTALL)
        if match_sol_b:
            ejercicio["solucion_b"] = textwrap.dedent(match_sol_b.group(1)).strip()
            contenido = (contenido[:match_sol_b.start()] + contenido[match_sol_b.end():]).strip()

        match_sol_a = re.search(r"- Solución Parte A:\s*\n\s*```python\n(.*?)```", contenido, re.DOTALL)
        if match_sol_a:
            ejercicio["solucion_a"] = textwrap.dedent(match_sol_a.group(1)).strip()
            contenido = (contenido[:match_sol_a.start()] + contenido[match_sol_a.end():]).strip()

        match_solucion = re.search(r"- Solución:\s*\n\s*```python\n(.*?)```", contenido, re.DOTALL)
        if match_solucion:
            ejercicio["solucion"] = textwrap.dedent(match_solucion.group(1)).strip()
            contenido = contenido[:match_solucion.start()].strip()

        match_codigo_error = re.search(r"\*\*Código con error:\*\*\s*\n```python\n(.*?)```", contenido, re.DOTALL)
        if match_codigo_error:
            ejercicio["codigo_error"] = textwrap.dedent(match_codigo_error.group(1)).strip()
            contenido = (contenido[:match_codigo_error.start()] + contenido[match_codigo_error.end():]).strip()

        # Extraer Parte B antes que A para no truncar contenido
        match_parte_b = re.search(r"\*\*Parte B[^*]*\*\*\s*\n(.*?)(?=\*\*Parte|\Z)", contenido, re.DOTALL)
        if match_parte_b:
            ejercicio["parte_b"] = match_parte_b.group(1).strip()
            contenido = (contenido[:match_parte_b.start()] + contenido[match_parte_b.end():]).strip()

        match_parte_a = re.search(r"\*\*Parte A[^*]*\*\*\s*\n(.*?)(?=\*\*Parte|\Z)", contenido, re.DOTALL)
        if match_parte_a:
            ejercicio["parte_a"] = match_parte_a.group(1).strip()
            contenido = (contenido[:match_parte_a.start()] + contenido[match_parte_a.end():]).strip()

        ejercicio["contexto"] = contenido.strip()
        ejercicio["enunciado"] = contenido.strip()

        match_resultado = re.search(r"Resultado esperado:\s*\n```\n(.*?)```", contenido, re.DOTALL)
        if match_resultado:
            ejercicio["resultado"] = match_resultado.group(1).rstrip()
            ejercicio["enunciado"] = contenido[:match_resultado.start()].strip()
            ejercicio["contexto"] = ejercicio["enunciado"]

        ejercicios.append(ejercicio)

    return ejercicios


def parsear_ticket_mcq(texto: str) -> list:
    """Parsea el Ticket de Salida en formato MCQ (2-3 preguntas de 4 alternativas).

    Cada pregunta en el spec sigue el formato:
        **Pregunta N:** [enunciado]
        - 1 dedo: [alternativa]
        - 2 dedos: [alternativa]
        - 3 dedos: [alternativa]
        - 4 dedos: [alternativa]
        **Respuesta correcta:** [1/2/3/4 dedos]
        **Justificación:** [texto]

    Las alternativas se rotulan por cantidad de dedos (no A/B/C/D) para mantener
    el mismo vocabulario que se usa en clase; se responden vía el Google Form de
    registro, no en voz alta y no antes de que termine la última pregunta, para
    evitar el efecto arrastre (ver CLAUDE.md regla 17).
    Estas preguntas NO van al Clase.ipynb del estudiante — solo al Solucionario.
    Las respuestas correctas (sin enunciado ni justificación) se replican además
    en un JSON liviano — ver `construir_ticket_respuestas()` — para que el agente
    que cruza las respuestas del Form no tenga que leer este notebook completo.
    """
    preguntas = []
    bloques = re.split(r"\*\*Pregunta\s+(\d+)\s*:\*\*", texto)
    for i in range(1, len(bloques), 2):
        if i + 1 >= len(bloques):
            break
        numero = bloques[i].strip()
        cuerpo = bloques[i + 1]

        match_enunciado = re.search(r"^(.*?)(?=\n\s*-\s*\d\s*dedos?:)", cuerpo, re.DOTALL)
        enunciado = match_enunciado.group(1).strip() if match_enunciado else cuerpo.strip()

        alternativas = {}
        for match_alt in re.finditer(r"-\s*(\d)\s*dedos?:\s*(.+)", cuerpo):
            alternativas[match_alt.group(1)] = match_alt.group(2).strip()

        match_correcta = re.search(r"\*\*Respuesta correcta:\*\*\s*(\d)", cuerpo)
        correcta = match_correcta.group(1).strip() if match_correcta else None

        match_justif = re.search(r"\*\*Justificación:\*\*\s*(.+?)(?=\*\*Pregunta|\Z)", cuerpo, re.DOTALL)
        justificacion = match_justif.group(1).strip() if match_justif else ""

        preguntas.append({
            "numero": numero, "enunciado": enunciado,
            "alternativas": alternativas, "correcta": correcta,
            "justificacion": justificacion,
        })

    return preguntas


def parsear_cierre_estructurado(texto: str) -> dict:
    """Parsea el nuevo formato de cierre con objetivo + pregunta metacognición + pregunta actitud.
    Usa (?=\\n\\*\\*|\\Z) para no cortar en bold (**texto**) dentro de una línea."""
    cierre = {"objetivo": None, "pregunta_meta": None, "pregunta_actitud": None}

    m_obj = re.search(r"\*\*Objetivo de la clase[^*]*\*\*\s*\n(.+?)(?=\n\*\*|\Z)", texto, re.DOTALL)
    if m_obj:
        cierre["objetivo"] = m_obj.group(1).strip()

    m_p1 = re.search(r"\*\*Pregunta 1[^*]*\*\*\s*\n(.+?)(?=\n\*\*Pregunta 2|\Z)", texto, re.DOTALL)
    if m_p1:
        cierre["pregunta_meta"] = m_p1.group(1).strip()

    m_p2 = re.search(r"\*\*Pregunta 2[^*]*\*\*\s*\n(.+?)(?=\n\*\*|\Z)", texto, re.DOTALL)
    if m_p2:
        cierre["pregunta_actitud"] = m_p2.group(1).strip()

    return cierre


def backticks_a_code(texto: str) -> str:
    """Convierte `código` (markdown) a <code>código</code> (HTML).
    Necesario para texto que se inserta dentro de un bloque <table> raw: Jupyter/Colab
    no reprocesa markdown inline dentro de HTML crudo, así que los backticks quedarían
    literales en vez de renderizarse con estilo de código."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", texto)


MIME_POR_EXTENSION = {
    "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
    "gif": "image/gif", "svg": "image/svg+xml", "webp": "image/webp",
}


def incrustar_imagenes_locales(texto: str, carpeta_base: Path) -> str:
    """Convierte referencias markdown a imágenes locales (![alt](ruta/relativa.png))
    en data URIs base64, para que el notebook sea autocontenido y se vea igual
    al subirlo a Colab sin depender de que Diego suba también los archivos de imagen.
    Deja intactas las URLs remotas (http/https) y los data URIs que ya vengan incrustados.
    """
    def reemplazar(m):
        alt, ruta = m.group(1), m.group(2)
        if ruta.startswith(("http://", "https://", "data:")):
            return m.group(0)
        ruta_img = (carpeta_base / ruta).resolve()
        if not ruta_img.exists():
            return m.group(0)
        mime = MIME_POR_EXTENSION.get(ruta_img.suffix.lstrip(".").lower(), "image/png")
        data = base64.b64encode(ruta_img.read_bytes()).decode("ascii")
        return f"![{alt}](data:{mime};base64,{data})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", reemplazar, texto)


# =====================================================================
# CONSTRUCCIÓN DEL NOTEBOOK
# =====================================================================

def construir_notebook(spec: dict, carpeta_spec: Path) -> nbformat.NotebookNode:
    """Construye el objeto notebook a partir del spec parseado.
    carpeta_spec: carpeta que contiene el Spec.md, usada como base para
    resolver referencias a imágenes locales (ej: assets/bloque.png).
    """
    nb = new_notebook()
    nb.cells = []

    # --- ENCABEZADO ---
    nb.cells.append(new_markdown_cell(generar_encabezado(spec)))

    # --- OBJETIVO Y PROPÓSITO ---
    nb.cells.append(new_markdown_cell(generar_objetivo_proposito(spec)))

    # --- 1. HAZ AHORA ---
    nb.cells.append(new_markdown_cell(generar_seccion_haz_ahora(spec)))
    num_items = len(re.findall(r"^\d+\.", spec["haz_ahora"] or "", re.MULTILINE))
    num_items = max(num_items, 3)
    respuestas = "**Mis respuestas:**\n\n" + "\n".join(f"{i}. " for i in range(1, num_items + 1))
    nb.cells.append(new_markdown_cell(respuestas))

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
            elif item["tipo"] == "comparacion":
                nb.cells.append(new_markdown_cell(generar_comparacion_markdown(item)))
                if item.get("ejemplo"):
                    nb.cells.append(new_code_cell(item["ejemplo"]))
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
    # Nunca lleva celda "Mis respuestas": Diego siempre escribe el código
    # directamente en la celda de código, no respuestas de texto aparte.
    nb.cells.append(new_markdown_cell(generar_seccion_guiada_intro(spec)))
    if spec["guiada"].get("codigo_error"):
        nb.cells.append(new_code_cell("# Código a analizar — ejecuta y observa el resultado\n" + spec["guiada"]["codigo_error"]))
    nb.cells.append(new_code_cell("# Tu programa\n"))

    # --- 4. PRÁCTICA INDEPENDIENTE ---
    nb.cells.append(new_markdown_cell(generar_seccion_independiente_intro(spec)))
    for ejercicio in spec["independiente"]:
        nb.cells.append(new_markdown_cell(generar_ejercicio_independiente(ejercicio)))
        if ejercicio.get("parte_a") and ejercicio.get("parte_b"):
            if ejercicio.get("codigo_error"):
                nb.cells.append(new_code_cell("# Código a analizar — ejecuta y observa el resultado\n" + ejercicio["codigo_error"]))
            nb.cells.append(new_markdown_cell("#### Parte A — Análisis\n\n" + ejercicio["parte_a"]))
            nb.cells.append(new_markdown_cell(
                "📝 **Mis respuestas — Parte A** *(haz doble click para editar)*\n\n"
                "1. \n\n2. \n\n3. "
            ))
            nb.cells.append(new_code_cell("# Tu código — Parte A\n"))
            nb.cells.append(new_markdown_cell("#### Parte B — Escritura desde cero\n\n" + ejercicio["parte_b"]))
            nb.cells.append(new_code_cell("# Tu código — Parte B\n"))
        else:
            if ejercicio.get("codigo_error"):
                nb.cells.append(new_code_cell("# Código a analizar — ejecuta y observa el resultado\n" + ejercicio["codigo_error"]))
            nb.cells.append(new_code_cell(f"# Tu solución del Ejercicio {ejercicio['numero']}\n"))

    # --- TICKET DE SALIDA (placeholder) ---
    # Las preguntas y alternativas NUNCA van en este notebook — viven solo en
    # Solucionario.ipynb y se proyectan en la tele. Acá solo queda el anuncio.
    if spec.get("ticket_mcq"):
        nb.cells.append(new_markdown_cell(generar_seccion_ticket_placeholder(spec)))

    # --- CIERRE ---
    nb.cells.append(new_markdown_cell(generar_seccion_cierre(spec)))
    if spec.get("cierre_estructurado"):
        nb.cells.append(new_markdown_cell(
            "### 📝 Mis respuestas\n\n"
            "*(haz doble click para editar y escribir tus respuestas)*\n\n"
            "1. \n\n"
            "2. "
        ))
    nb.cells.append(new_markdown_cell("---\n\n"))

    # NOTA: el notebook de estudiante NO lleva ninguna sección de soluciones,
    # ni siquiera oculta con <details>. Todas las soluciones (Haz Ahora, Guiada,
    # Independiente) van al Solucionario.ipynb — ver construir_solucionario().

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            cell.source = incrustar_imagenes_locales(cell.source, carpeta_spec)

    return nb


def generar_encabezado(spec: dict) -> str:
    n = spec['numero_clase']
    num = f"{n:02d}" if isinstance(n, int) else (str(n) if n is not None else "??")
    duracion = spec["contexto"].get("Duración", "90 min")
    curso = spec["contexto"].get("Curso", "3ro y 4to medio")
    return f"""# 🐍 Clase {num} — {spec['tema']}

**Curso:** {curso}  |  **Duración:** {duracion}  |  **Plataforma:** Google Colab

---"""


def generar_objetivo_proposito(spec: dict) -> str:
    contenidos_previos = spec["contexto"].get("Contenidos previos asumidos", "")
    contenidos_nuevos = spec["contexto"].get("Contenidos nuevos", "")
    bloque = "## 🎯 Objetivo de la clase\n\n"
    bloque += f"{spec['objetivo']}\n\n"
    if spec.get("proposito"):
        bloque += "## 💡 Propósito\n\n"
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
        # Strip internal design notes (Propósito, Objetivo) — not student-facing
        contenido = re.sub(r"\*\*Propósito:\*\*[^\n]*\n?", "", spec["haz_ahora"])
        contenido = re.sub(r"\*\*Objetivo:\*\*[^\n]*\n?", "", contenido).strip()
        bloque += contenido
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


def generar_comparacion_markdown(item: dict) -> str:
    bloque = f"### 💡 {item['titulo']}\n\n" if item.get("titulo") else ""
    bloque += backticks_a_code(item["contenido"]) + "\n"
    return bloque


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

    if spec["guiada"].get("pasos_tabla"):
        # Formato default: tabla de 2 columnas (qué debe hacer el programa | resultado esperado),
        # un paso por fila, agrupando en el spec los pasos que no producen output propio.
        bloque += "**Antes de escribir código, analiza el enunciado:**\n\n"
        bloque += "<table>\n<tr><th>Qué debe hacer tu programa</th><th>Resultado esperado</th></tr>\n"
        for i, fila in enumerate(spec["guiada"]["pasos_tabla"], 1):
            paso = backticks_a_code(fila["paso"])
            resultado = backticks_a_code(fila["resultado"])
            bloque += f"<tr>\n<td>{i}. {paso}</td>\n<td><pre>{resultado}</pre></td>\n</tr>\n"
        bloque += "</table>\n"
    else:
        # Formato antiguo (retrocompatible): lista de pasos + un solo bloque de resultado al final.
        if spec["guiada"]["pasos"]:
            bloque += "**Antes de escribir código, analiza el enunciado:**\n\n"
            for i, paso in enumerate(spec["guiada"]["pasos"], 1):
                bloque += f"{i}. {paso}\n"
            bloque += "\n"
        if spec["guiada"]["resultado"]:
            bloque += "**Resultado esperado al final:**\n\n```\n"
            bloque += spec["guiada"]["resultado"]
            bloque += "\n```\n"

    return bloque


def generar_seccion_independiente_intro(spec: dict) -> str:
    return "---\n\n## 4️⃣ Práctica Independiente\n\nResuelve los siguientes ejercicios en pareja. Si se traban, pregunten al profe."


def generar_ejercicio_independiente(ejercicio: dict) -> str:
    bloque = f"### Ejercicio {ejercicio['numero']} — {ejercicio['titulo']}\n\n"
    contexto = ejercicio.get("contexto") or ejercicio.get("enunciado") or ""

    if "Ejemplo:" in contexto:
        idx = contexto.find("Ejemplo:")
        main_desc = contexto[:idx].strip()
        ejemplo_block = contexto[idx:].strip()
        bloque += main_desc + "\n\n"
        m_code = re.search(r"```\n(.*?)```", ejemplo_block, re.DOTALL)
        if m_code:
            ejemplo_desc = ejemplo_block[:m_code.start()].strip().rstrip(":")
            ejemplo_output = m_code.group(1).strip()
            bloque += f"*{ejemplo_desc}:*\n\n```\n{ejemplo_output}\n```\n\n"
        else:
            bloque += ejemplo_block + "\n\n"
    else:
        bloque += contexto + "\n\n"

    if ejercicio.get("resultado") and not ejercicio.get("parte_a"):
        bloque += "**Resultado esperado:**\n\n```\n"
        for linea in ejercicio["resultado"].split("\n"):
            bloque += f"{linea}\n"
        bloque += "```\n"

    return bloque


def derivar_tema_breve_form(nombre_carpeta: str) -> str:
    """Deriva el nombre breve que los estudiantes escriben en el Form del Ticket
    de Salida (campo "Tema de la clase de hoy") a partir del slug de la carpeta,
    ej. "clase-16-for-range" -> "for range", "clase-20-for-avanzado" -> "for avanzado".
    """
    slug = re.sub(r"^clase-\d+[a-z]?-", "", nombre_carpeta)
    return slug.replace("-", " ")


def construir_ticket_respuestas(spec: dict) -> dict:
    """Arma el JSON liviano con SOLO las respuestas correctas del Ticket de
    Salida (sin enunciado ni justificación), pensado para que un agente lo lea
    rápido al cruzar las respuestas del Google Form sin abrir el Solucionario
    completo. Las llaves replican tal cual el nombre de columna que el Form usa
    en la Sheet de respuestas ("Respuestas a ticket [1]".."[4]") — así el
    cruce hace match directo columna-a-llave, sin traducir. Si la clase tuvo
    menos de 4 preguntas, los espacios sobrantes quedan "No se preguntó".
    """
    llaves = [f"Respuestas a ticket [{n}]" for n in range(1, 5)]
    preguntas = spec.get("ticket_mcq", [])
    respuestas = {}
    for llave, pregunta in zip(llaves, preguntas):
        respuestas[llave] = pregunta.get("correcta") or "No se preguntó"
    for llave in llaves[len(preguntas):]:
        respuestas[llave] = "No se preguntó"
    return {
        "clase": spec.get("numero_clase"),
        "tema": spec.get("tema_breve_form", ""),
        "respuestas": respuestas,
    }


def generar_seccion_ticket_placeholder(spec: dict) -> str:
    nombre_breve = spec.get("tema_breve_form", spec.get("tema", ""))
    return (
        "---\n\n## 🎫 Ticket de Salida\n\n"
        "Las preguntas del Ticket de Salida se van a proyectar en la tele, una por una. "
        "Míralas, decide tu respuesta y espera a que pasen todas — recién al final completas "
        f"y envías [este formulario]({TICKET_SALIDA_FORM_URL}) con tus respuestas.\n\n"
        f"En el campo **\"Tema de la clase de hoy\"** escribe: `{nombre_breve}`\n\n"
        "Cuando todos hayan enviado, revisamos juntos las respuestas correctas 🙌"
    )


def generar_seccion_cierre(spec: dict) -> str:
    if spec.get("cierre_estructurado"):
        c = spec["cierre_estructurado"]
        bloque = "---\n\n## 🎯 Cierre\n\n"
        if c.get("objetivo"):
            bloque += f"**Objetivo de la clase**\n\n{c['objetivo']}\n\n"
        bloque += "---\n\n**Reflexiona antes de irte:**\n\n"
        if c.get("pregunta_meta"):
            bloque += f"1. {c['pregunta_meta']}\n\n"
        if c.get("pregunta_actitud"):
            bloque += f"2. {c['pregunta_actitud']}\n"
        return bloque

    bloque = "---\n\n## 🧠 Cierre y reflexión\n\n"
    bloque += "Antes de irte, piensa (no hay que entregar):\n\n"
    for i, pregunta in enumerate(spec["cierre"], 1):
        bloque += f"{i}. {pregunta}\n"
    return bloque


def hay_soluciones_de_clase(spec: dict) -> bool:
    """True si hay algún contenido de solución de Clase.ipynb para el Solucionario
    (respuestas de Haz Ahora, solución de la Guiada, o soluciones de Independiente)."""
    if spec.get("respuestas_haz_ahora"):
        return True
    if spec["guiada"].get("solucion"):
        return True
    for ejercicio in spec["independiente"]:
        if ejercicio.get("solucion") or ejercicio.get("solucion_a") or ejercicio.get("solucion_b"):
            return True
    return False


def generar_secciones_solucionario_clase(spec: dict) -> str:
    """Genera las secciones del Solucionario correspondientes a Clase.ipynb:
    respuestas del Haz Ahora, solución de la Guiada y soluciones de Independiente.
    Sin <details> — el Solucionario es de uso exclusivo del profesor, no hay
    nada que ocultar dentro de su propio documento."""
    bloque = ""

    if spec.get("respuestas_haz_ahora"):
        bloque += "## 1️⃣ Haz Ahora — Respuestas\n\n"
        bloque += spec["respuestas_haz_ahora"] + "\n\n---\n\n"

    if spec["guiada"].get("solucion"):
        bloque += "## 3️⃣ Práctica Guiada — Solución\n\n"
        bloque += f"```python\n{spec['guiada']['solucion']}\n```\n\n---\n\n"

    ejercicios_con_solucion = [
        e for e in spec["independiente"]
        if e.get("solucion") or e.get("solucion_a") or e.get("solucion_b")
    ]
    if ejercicios_con_solucion:
        bloque += "## 4️⃣ Práctica Independiente — Soluciones\n\n"
        for ejercicio in ejercicios_con_solucion:
            bloque += f"### Ejercicio {ejercicio['numero']} — {ejercicio['titulo']}\n\n"
            if ejercicio.get("solucion_a"):
                bloque += f"**Parte A:**\n\n```python\n{ejercicio['solucion_a']}\n```\n\n"
            if ejercicio.get("solucion_b"):
                bloque += f"**Parte B:**\n\n```python\n{ejercicio['solucion_b']}\n```\n\n"
            if ejercicio.get("solucion"):
                bloque += f"```python\n{ejercicio['solucion']}\n```\n\n"
        bloque += "---\n\n"

    return bloque


# =====================================================================
# CONSTRUCCIÓN DEL SOLUCIONARIO (TODAS las soluciones — solo para el profesor)
# =====================================================================

def construir_solucionario(spec: dict) -> nbformat.NotebookNode:
    """Construye (o inicia) el notebook Solucionario con TODAS las soluciones
    ligadas a Clase.ipynb: respuestas del Haz Ahora, solución de la Guiada,
    soluciones de Práctica Independiente, y las preguntas MCQ del Ticket de Salida.

    generar-colab-ejercicios actualiza después este mismo archivo agregando las
    soluciones de Ejercicios.ipynb — ver ese script.

    Exclusivo para el profesor. Diego lo sube a Classroom recién después de
    dictar la clase, nunca antes — es un solo documento con todas las
    respuestas, no algo para compartir con estudiantes.
    """
    nb = new_notebook()
    nb.cells = []

    n = spec["numero_clase"]
    num = f"{n:02d}" if isinstance(n, int) else (str(n) if n is not None else "??")

    nb.cells.append(new_markdown_cell(
        f"# 🔒 Solucionario — Clase {num}: {spec['tema']}\n\n"
        "**Uso:** documento exclusivo para el profesor. El Ticket de Salida se "
        "proyecta en clase y se responde a viva voz; el resto (Haz Ahora, Guiada, "
        "Independiente) es para revisar en vivo o subir a Classroom recién "
        "**después** de dictar la clase — nunca antes.\n\n"
        "---"
    ))

    secciones_clase = generar_secciones_solucionario_clase(spec)
    if secciones_clase:
        nb.cells.append(new_markdown_cell(secciones_clase))

    ETIQUETAS_DEDOS = {"1": "1 dedo", "2": "2 dedos", "3": "3 dedos", "4": "4 dedos"}
    if spec.get("ticket_mcq"):
        nb.cells.append(new_markdown_cell("## 🎫 Ticket de Salida"))
        for pregunta in spec["ticket_mcq"]:
            bloque = f"### Pregunta {pregunta['numero']}\n\n{pregunta['enunciado']}\n\n"
            for numero_dedo in ["1", "2", "3", "4"]:
                texto_alt = pregunta["alternativas"].get(numero_dedo, "")
                if not texto_alt:
                    continue
                marca = " ✅" if numero_dedo == pregunta.get("correcta") else ""
                bloque += f"**✋ {ETIQUETAS_DEDOS[numero_dedo]}:** {texto_alt}{marca}\n\n"
            if pregunta.get("justificacion"):
                bloque += f"> 💡 {pregunta['justificacion']}\n"
            nb.cells.append(new_markdown_cell(bloque))

    return nb


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
    spec["tema_breve_form"] = derivar_tema_breve_form(ruta_spec.parent.name)

    print(f"✅ Spec parseado: Clase {spec['numero_clase']} — {spec['tema']}")
    print(f"   - {len(spec['icn']['conceptos'])} conceptos en ICN")
    print(f"   - {len(spec['guiada']['pasos']) or len(spec['guiada']['pasos_tabla'])} pasos en guiada")
    print(f"   - {len(spec['independiente'])} ejercicios independientes")

    print(f"🛠️  Construyendo notebook...")
    nb = construir_notebook(spec, ruta_spec.parent)

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    with ruta_salida.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"💾 Notebook guardado en: {ruta_salida}")
    print(f"📤 Súbelo a Colab desde https://colab.research.google.com (Archivo → Subir cuaderno)")

    if spec.get("ticket_mcq") or hay_soluciones_de_clase(spec):
        print(f"🛠️  Construyendo Solucionario "
              f"({len(spec.get('ticket_mcq', []))} preguntas MCQ + soluciones de Clase.ipynb)...")
        nb_solucionario = construir_solucionario(spec)
        ruta_solucionario = ruta_salida.parent / ruta_salida.name.replace(
            " - Clase.ipynb", " - Solucionario.ipynb"
        )
        if ruta_solucionario == ruta_salida:
            print("⚠️  No se pudo derivar el nombre del Solucionario — "
                  "el archivo de salida debe seguir el patrón 'Clase NN - Tema - Clase.ipynb'.")
        else:
            # Si ya existía un Solucionario con soluciones de Ejercicios.ipynb
            # (generadas por generar-colab-ejercicios), preservarlas: esta función
            # solo reconstruye las secciones derivadas de Clase.ipynb.
            if ruta_solucionario.exists():
                marca_ejercicios = "## 💪 Ejercicios adicionales — Soluciones"
                nb_previo = nbformat.read(ruta_solucionario, as_version=4)
                celdas_ejercicios = [
                    c for c in nb_previo.cells if c.get("source", "").startswith(marca_ejercicios)
                ]
                nb_solucionario.cells.extend(celdas_ejercicios)
            with ruta_solucionario.open("w", encoding="utf-8") as f:
                nbformat.write(nb_solucionario, f)
            print(f"💾 Solucionario guardado en: {ruta_solucionario}")
            print("🔒 Solo para el profesor — se sube a Classroom recién después de dictar la clase.")

    if spec.get("ticket_mcq"):
        ruta_respuestas = ruta_salida.parent / ruta_salida.name.replace(
            " - Clase.ipynb", " - Ticket de Salida Respuestas.json"
        )
        if ruta_respuestas == ruta_salida:
            print("⚠️  No se pudo derivar el nombre del JSON de respuestas — "
                  "el archivo de salida debe seguir el patrón 'Clase NN - Tema - Clase.ipynb'.")
        else:
            with ruta_respuestas.open("w", encoding="utf-8") as f:
                json.dump(construir_ticket_respuestas(spec), f, ensure_ascii=False, indent=2)
            print(f"💾 JSON de respuestas del Ticket de Salida guardado en: {ruta_respuestas}")


if __name__ == "__main__":
    main()
