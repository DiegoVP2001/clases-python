#!/usr/bin/env python3
"""
crear_ppt.py — Generador del PPT de clase desde el spec enriquecido. (v4)

Mejoras v4:
- Nuevo slide tipo 9 "Código + Resultado apilado" (layout estrella compacto):
  hasta 3 filas etiqueta + código(izq) + resultado(der) en una sola diapositiva.
  Se dispara con bloques "**Demostración: ...**" en el ICN del spec.
- Regla mixta de fuente para código: mide la línea más larga y baja 20->18->16pt
  solo si hace falta, evitando el desborde de las cajas.
- Ocultado de filas no usadas en el slide apilado (por rango vertical exacto).

Mejoras v3:
- Haz Ahora: separa texto narrativo de bloques de código y los renderiza en
  zonas distintas (texto en bloque oscuro, código en bloque terminal verdoso).
- Tabla de errores: aplica formato inline a backticks `código` para que se
  vean en Consolas verdosa dentro de las celdas.
- Fondo oscuro garantizado por el rectángulo de la plantilla.

Uso:
    python crear_ppt.py <ruta_spec.md> <ruta_salida.pptx>

Requiere: pip install python-pptx
"""

import sys
import re
import copy
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Pt, Inches, Emu
    from pptx.dml.color import RGBColor
except ImportError:
    print("ERROR: python-pptx no está instalado. Instálalo con:")
    print("    pip install python-pptx")
    sys.exit(1)


CARPETA_SKILL = Path(__file__).resolve().parent
RUTA_PLANTILLA = CARPETA_SKILL / "plantilla_marca.pptx"

M_BIENVENIDA = 0
M_OBJETIVO = 1
M_STOCK_TITULO = 2
M_CONCEPTO = 3
M_CODIGO_RESULTADO = 4
M_TABLA = 5
M_EJERCICIO = 6
M_TICKET = 7
M_CIERRE = 8
M_CODIGO_RESULTADO_MULTI = 9  # apilado (layout estrella)

# Ancho útil (in) de las cajas del slide apilado, para la regla mixta de fuente.
# Debe coincidir con COD_W / RES_W de construir_plantilla.py.
ANCHO_CAJA_CODIGO_MULTI = 6.85
ANCHO_CAJA_RESULTADO_MULTI = 13.333 - 0.6 - (0.6 + 6.85 + 0.30)

# Color verdoso para código inline (mismo que el de los bloques terminal)
COLOR_CODIGO_INLINE = RGBColor(0x4A, 0xDF, 0xCB)


# =====================================================================
# PARSER DEL SPEC
# =====================================================================

def parsear_spec(ruta_spec: Path) -> dict:
    contenido = ruta_spec.read_text(encoding="utf-8")
    spec = {
        "numero_clase": None, "tema": None, "contexto": {},
        "objetivo": None, "proposito": None,
        "haz_ahora": None,
        "icn": {"conceptos": [], "errores_tabla": [], "demos_apiladas": []},
        "guiada": {"situacion": None, "variables": None, "resultado": None},
        "independiente": [],
        "ticket": {"tarea": None, "entrega": None},
        "cierre": [],
    }
    m = re.search(r"^#\s+Clase\s+(\w+)\s*[—\-–]\s*(.+)$", contenido, re.MULTILINE)
    if m:
        raw = m.group(1)
        spec["numero_clase"] = int(raw) if raw.isdigit() else raw
        spec["tema"] = m.group(2).strip()
    seccion_ctx = extraer(contenido, "## Contexto", "## Objetivo")
    if seccion_ctx:
        for linea in seccion_ctx.split("\n"):
            mkv = re.match(r"^-\s+\*\*([^:]+):\*\*\s+(.+)$", linea.strip())
            if mkv:
                spec["contexto"][mkv.group(1).strip()] = mkv.group(2).strip()
    spec["objetivo"] = limpiar(extraer(contenido, "## Objetivo", "## Propósito"))
    prop = limpiar(extraer(contenido, "## Propósito", "## Estructura de la clase"))
    if prop:
        spec["proposito"] = "\n".join(
            l.lstrip("> ").rstrip() for l in prop.split("\n")
        ).strip()
    spec["haz_ahora"] = limpiar(extraer(contenido, "### 1. Haz Ahora", "### 2."))
    icn_raw = limpiar(extraer(contenido, "### 2. Introducción al Contenido Nuevo", "### 3."))
    if icn_raw:
        spec["icn"] = parsear_icn_enriquecido(icn_raw)
    g_raw = limpiar(extraer(contenido, "### 3. Práctica Guiada", "### 4."))
    if g_raw:
        spec["guiada"] = parsear_guiada(g_raw)
    i_raw = limpiar(extraer(contenido, "### 4. Práctica Independiente", "### 5."))
    if i_raw:
        spec["independiente"] = parsear_independiente(i_raw)
    t_raw = limpiar(extraer(contenido, "### 5. Ticket de Salida", "### Cierre"))
    if t_raw:
        m_tarea = re.search(r"\*\*Tarea:\*\*\s*(.+?)(?=\*\*Entrega|\Z)", t_raw, re.DOTALL)
        if m_tarea:
            spec["ticket"]["tarea"] = m_tarea.group(1).strip().strip("*").strip()
        m_ent = re.search(r"\*\*Entrega:\*\*\s*(.+)", t_raw)
        if m_ent:
            spec["ticket"]["entrega"] = m_ent.group(1).strip()
    c_raw = limpiar(extraer(contenido, "### Cierre y metacognición", "## Decisiones"))
    if c_raw:
        spec["cierre"] = [
            re.sub(r"^\d+\.\s*", "", l.strip())
            for l in c_raw.split("\n")
            if re.match(r"^\d+\.", l.strip())
        ]
    return spec


def extraer(texto: str, ini: str, fin):
    i = texto.find(ini)
    if i == -1:
        return None
    i += len(ini)
    if fin:
        f = texto.find(fin, i)
        return texto[i:] if f == -1 else texto[i:f]
    return texto[i:]


def limpiar(s):
    if not s:
        return None
    s = re.sub(r"\n\s*---\s*\n", "\n", s)
    return s.strip()


def parsear_icn_enriquecido(texto: str) -> dict:
    icn = {"conceptos": [], "errores_tabla": [], "demos_apiladas": []}
    bloques = re.split(r"\*\*Concepto\s+(\d+)\s*:\s*([^*]+)\*\*", texto)
    if len(bloques) > 1:
        for i in range(1, len(bloques), 3):
            if i + 2 >= len(bloques):
                break
            num = bloques[i].strip()
            nombre = bloques[i + 1].strip()
            cuerpo = bloques[i + 2]
            concepto = {"numero": num, "nombre": nombre,
                        "definicion": "", "ejemplo": "", "idea_clave": ""}
            m = re.search(r"[-•]\s*\*?\*?Definici[óo]n\*?\*?\s*:\s*(.+?)(?=\n\s*[-•]|\n\s*\*\*|\Z)",
                          cuerpo, re.DOTALL)
            if m:
                concepto["definicion"] = m.group(1).strip()
            m = re.search(r"[-•]\s*\*?\*?Ejemplo\*?\*?\s*:?\s*\n?\s*```python\n(.*?)```",
                          cuerpo, re.DOTALL)
            if m:
                concepto["ejemplo"] = m.group(1).rstrip()
            m = re.search(r"[-•]\s*\*?\*?Idea clave\*?\*?\s*:\s*(.+?)(?=\n\s*[-•]|\n\s*\*\*|\Z)",
                          cuerpo, re.DOTALL)
            if m:
                concepto["idea_clave"] = m.group(1).strip()
            icn["conceptos"].append(concepto)

    if not icn["conceptos"]:
        m = re.search(r"\*\*Conceptos:\*\*\s*\n(.*?)(?=\*\*|\Z)", texto, re.DOTALL)
        if m:
            for j, l in enumerate(m.group(1).split("\n"), start=1):
                l = l.strip()
                if re.match(r"^\d+\.", l):
                    icn["conceptos"].append({
                        "numero": str(j), "nombre": f"Concepto {j}",
                        "definicion": re.sub(r"^\d+\.\s*", "", l),
                        "ejemplo": "", "idea_clave": "",
                    })
        m = re.search(r"\*\*Ejemplos a usar:\*\*\s*\n```python\n(.*?)```",
                      texto, re.DOTALL)
        if m and icn["conceptos"]:
            lineas = [l for l in m.group(1).split("\n") if l.strip()]
            for c, lin in zip(icn["conceptos"], lineas):
                c["ejemplo"] = lin

    m = re.search(r"\*\*Errores típicos:\*\*\s*\n(\|.*?)(?=\n\n|\Z)", texto, re.DOTALL)
    if m:
        filas = []
        for linea in m.group(1).strip().split("\n"):
            linea = linea.strip()
            if not linea.startswith("|"):
                continue
            celdas = [c.strip() for c in linea.split("|")[1:-1]]
            if all(re.match(r"^[-:]+$", c) for c in celdas):
                continue
            if celdas:
                filas.append(celdas)
        if filas:
            filas = filas[1:]
        icn["errores_tabla"] = filas

    # Demostraciones apiladas (slide tipo 9). Sintaxis opcional en el spec:
    #
    #   **Demostración: [título corto del slide]**
    #   - Fila: [etiqueta] | `código en una o varias líneas con \n` | resultado
    #   ... (hasta 3 filas)
    #
    # También admite código multilínea con bloque ```python```:
    #   - Fila: [etiqueta]
    #     ```python
    #     línea1
    #     línea2
    #     ```
    #     Resultado: salida esperada
    icn["demos_apiladas"] = parsear_demos_apiladas(texto)
    return icn


def parsear_demos_apiladas(texto: str) -> list:
    """Parsea bloques '**Demostración: ...**' en una lista de demos.

    Cada demo = {"titulo": str, "subtitulo": str, "filas": [ {label, codigo, resultado} ]}
    Soporta dos formatos de fila:
      A) en línea:  - Fila: etiqueta | codigo | resultado    (codigo admite \\n literal)
      B) con bloque de código:
         - Fila: etiqueta
           ```python
           ...
           ```
           Resultado: ...
    """
    demos = []
    bloques = re.split(r"\*\*Demostración\s*:\s*([^*]+)\*\*", texto)
    if len(bloques) < 2:
        return demos
    for i in range(1, len(bloques), 2):
        titulo = bloques[i].strip()
        cuerpo = bloques[i + 1] if i + 1 < len(bloques) else ""
        demo = {"titulo": titulo, "subtitulo": "", "filas": []}

        # Subtítulo opcional: primera línea que empieza con "Subtítulo:"
        m_sub = re.search(r"Subt[íi]tulo\s*:\s*(.+)", cuerpo)
        if m_sub:
            demo["subtitulo"] = m_sub.group(1).strip()

        # Formato B: filas con bloque ```python```
        patron_b = re.compile(
            r"[-•]\s*Fila\s*:\s*([^\n]*?)\s*\n\s*```python\s*\n(.*?)```"
            r"(?:\s*Resultado\s*:\s*([^\n]+))?",
            re.DOTALL)
        encontrados_b = list(patron_b.finditer(cuerpo))
        if encontrados_b:
            for mb in encontrados_b:
                label = mb.group(1).strip()
                codigo = mb.group(2).rstrip()
                resultado = (mb.group(3) or "").strip()
                demo["filas"].append({"label": label, "codigo": codigo,
                                      "resultado": resultado})
        else:
            # Formato A: una línea por fila con separador |
            for linea in cuerpo.split("\n"):
                linea = linea.strip()
                m_fila = re.match(r"[-•]\s*Fila\s*:\s*(.+)", linea)
                if not m_fila:
                    continue
                partes = [p.strip() for p in m_fila.group(1).split("|")]
                label = partes[0] if len(partes) > 0 else ""
                codigo = partes[1].replace("\\n", "\n") if len(partes) > 1 else ""
                resultado = partes[2].replace("\\n", "\n") if len(partes) > 2 else ""
                demo["filas"].append({"label": label, "codigo": codigo,
                                      "resultado": resultado})

        if demo["filas"]:
            demos.append(demo)
    return demos


def parsear_guiada(texto: str) -> dict:
    g = {"situacion": None, "variables": None, "resultado": None}
    m = re.search(r"\*\*Situación:\*\*\s*(.+?)(?=\*\*|\Z)", texto, re.DOTALL)
    if m:
        g["situacion"] = m.group(1).strip()
    m = re.search(r"\*\*Variables:\*\*\s*\n```python\n(.*?)```", texto, re.DOTALL)
    if m:
        g["variables"] = m.group(1).rstrip()
    m = re.search(r"\*\*Resultado esperado:\*\*\s*\n```\n?(.*?)```", texto, re.DOTALL)
    if m:
        g["resultado"] = m.group(1).rstrip()
    return g


def parsear_independiente(texto: str) -> list:
    ejercicios = []
    bloques = re.split(r"\*\*Ejercicio\s+(\d+)\s*[—\-–]\s*([^*]+)\*\*", texto)
    for i in range(1, len(bloques), 3):
        if i + 2 >= len(bloques):
            break
        num = bloques[i].strip()
        titulo = bloques[i + 1].strip()
        cuerpo = bloques[i + 2].strip()
        ej = {"numero": num, "titulo": titulo, "enunciado": None, "resultado": None}
        m = re.search(r"Resultado esperado:\s*\n```\n?(.*?)```", cuerpo, re.DOTALL)
        if m:
            ej["resultado"] = m.group(1).rstrip()
            ej["enunciado"] = cuerpo[:m.start()].strip()
        else:
            ej["enunciado"] = cuerpo
        ejercicios.append(ej)
    return ejercicios


def separar_haz_ahora(texto: str) -> dict:
    """Separa el Haz Ahora en texto narrativo + bloque de código (si existe)."""
    partes = {"intro": "", "texto": "", "codigo": ""}
    if not texto:
        return partes

    # Quitar "**Propósito:**" si está
    texto = re.sub(r"\*\*Propósito:\*\*[^\n]*\n?", "", texto)
    # Quitar línea sola con "(N min)" que es metadata
    texto = re.sub(r"^\s*\(\s*\d+\s*min\s*\)\s*$", "", texto, flags=re.MULTILINE)

    # Capturar intro desde "**Actividad:**" hasta el final del párrafo
    m_act = re.search(r"\*\*Actividad:\*\*\s*(.+?)(?=\n|\Z)", texto)
    if m_act:
        partes["intro"] = m_act.group(1).strip()

    # Capturar el bloque de código markdown
    m_code = re.search(r"```python\s*\n(.*?)```", texto, re.DOTALL)
    if m_code:
        partes["codigo"] = m_code.group(1).rstrip()
        sin_codigo = re.sub(r"```python\s*\n.*?```", "", texto, flags=re.DOTALL)
        sin_codigo = re.sub(r"\*\*Actividad:\*\*[^\n]*\n?", "", sin_codigo)
        # Compactar líneas en blanco múltiples
        sin_codigo = re.sub(r"\n\s*\n", "\n\n", sin_codigo)
        partes["texto"] = sin_codigo.strip()
    else:
        sin_actividad = re.sub(r"\*\*Actividad:\*\*[^\n]*\n?", "", texto)
        sin_actividad = re.sub(r"\n\s*\n", "\n\n", sin_actividad)
        partes["texto"] = sin_actividad.strip()

    if not partes["intro"]:
        partes["intro"] = "Activa lo que ya sabes antes de empezar."
    if not partes["texto"]:
        partes["texto"] = "Observa con atención y prepárate para discutir."
    return partes


# =====================================================================
# DUPLICACIÓN Y REEMPLAZO
# =====================================================================

def duplicar_slide(prs, slide_modelo):
    blank_layout = slide_modelo.slide_layout
    nueva = prs.slides.add_slide(blank_layout)
    for shp in list(nueva.shapes):
        sp = shp._element
        sp.getparent().remove(sp)
    for shp in slide_modelo.shapes:
        nuevo_el = copy.deepcopy(shp._element)
        nueva.shapes._spTree.insert_element_before(nuevo_el, "p:extLst")
    return nueva


def eliminar_slides(prs, indices):
    xml_slides = prs.slides._sldIdLst
    slides_xml = list(xml_slides)
    for idx in sorted(indices, reverse=True):
        rId = slides_xml[idx].rId
        prs.part.drop_rel(rId)
        xml_slides.remove(slides_xml[idx])


def reemplazar_placeholders(slide, mapping: dict, mapping_inline_code=None):
    """Reemplaza placeholders {{KEY}} en todos los textos y tablas.

    Si el valor del placeholder contiene backticks `código`, automáticamente
    se aplica formato Consolas verdoso a esa parte. Esto aplica a TODOS los
    placeholders por defecto. El parámetro mapping_inline_code se mantiene
    por compatibilidad pero ya no es necesario.
    """
    for shape in slide.shapes:
        if shape.has_text_frame:
            reemplazar_en_text_frame(shape.text_frame, mapping)
        if shape.has_table:
            for row in shape.table.rows:
                for cell in row.cells:
                    reemplazar_en_text_frame(cell.text_frame, mapping)


def reemplazar_en_text_frame(tf, mapping: dict):
    """Para cada run del TextFrame, busca placeholders y los reemplaza.

    Si el valor de un placeholder contiene backticks, el texto se reconstruye
    en múltiples runs para aplicar formato Consolas verdoso al código inline.
    Si el valor contiene saltos de línea \\n, se crean párrafos adicionales.
    """
    for para in tf.paragraphs:
        for run in list(para.runs):
            texto_original = run.text
            placeholders_encontrados = re.findall(r"\{\{([A-Z_0-9]+)\}\}", texto_original)
            if not placeholders_encontrados:
                continue

            # ¿Algún placeholder tiene backticks en su valor?
            necesita_split_backticks = any(
                "`" in str(mapping.get(k, "")) for k in placeholders_encontrados
            )
            # ¿Algún placeholder tiene saltos de línea?
            necesita_split_lineas = any(
                "\n" in str(mapping.get(k, "")) for k in placeholders_encontrados
            )

            if not necesita_split_backticks and not necesita_split_lineas:
                nuevo = texto_original
                for key, valor in mapping.items():
                    nuevo = nuevo.replace("{{" + key + "}}",
                                          str(valor) if valor is not None else "")
                run.text = nuevo
            elif necesita_split_lineas and not necesita_split_backticks:
                aplicar_reemplazo_con_saltos_linea(tf, para, run, mapping)
            else:
                # Tiene backticks (con o sin saltos de línea)
                aplicar_reemplazo_con_inline_code(para, run, mapping)


def aplicar_reemplazo_con_saltos_linea(tf, para, run, mapping):
    """Maneja placeholders cuyo valor contiene saltos de línea.

    En XML de PowerPoint, los párrafos son elementos <a:p>. Un \\n debe
    convertirse en un nuevo elemento <a:p> hermano. Esta función reescribe
    el run actual para que su texto sea solo la primera línea, y agrega
    párrafos adicionales después con el resto del contenido.
    """
    texto_original = run.text

    # Conservar formato base del run original
    base_font_name = run.font.name
    base_font_size = run.font.size
    base_font_bold = run.font.bold
    base_color = None
    try:
        if run.font.color and run.font.color.type:
            base_color = run.font.color.rgb
    except Exception:
        pass

    # Expandir placeholders
    texto_expandido = texto_original
    for key, valor in mapping.items():
        texto_expandido = texto_expandido.replace(
            "{{" + key + "}}", str(valor) if valor is not None else ""
        )

    lineas = texto_expandido.split("\n")
    if not lineas:
        return

    # Primera línea va en el run actual
    run.text = lineas[0]

    # Líneas adicionales como párrafos nuevos después del párrafo actual
    if len(lineas) > 1:
        from copy import deepcopy
        p_xml = para._p
        parent = p_xml.getparent()
        idx_actual = list(parent).index(p_xml)

        for offset, linea in enumerate(lineas[1:], start=1):
            # Clonar el párrafo actual como base (mantiene formato)
            nuevo_p = deepcopy(p_xml)
            # Limpiar runs dentro del nuevo párrafo
            ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
            for r_xml in list(nuevo_p.findall(f"{ns}r")):
                nuevo_p.remove(r_xml)
            # Insertar el nuevo párrafo después del actual
            parent.insert(idx_actual + offset, nuevo_p)

        # Ahora poblar las líneas en los nuevos párrafos
        # Re-leer paragraphs después de la mutación XML
        nuevos_paras = list(tf.paragraphs)
        idx_para_actual = None
        for i, p in enumerate(nuevos_paras):
            if p._p is p_xml:
                idx_para_actual = i
                break
        if idx_para_actual is not None:
            for offset, linea in enumerate(lineas[1:], start=1):
                p_nuevo = nuevos_paras[idx_para_actual + offset]
                r_nuevo = p_nuevo.add_run()
                r_nuevo.text = linea
                r_nuevo.font.name = base_font_name or "Calibri"
                if base_font_size:
                    r_nuevo.font.size = base_font_size
                r_nuevo.font.bold = base_font_bold
                if base_color:
                    r_nuevo.font.color.rgb = base_color


def aplicar_reemplazo_con_inline_code(para, run, mapping):
    """Toma un run que contiene placeholders con backticks y lo reemplaza por
    múltiples runs: texto normal y código (Consolas verdoso) alternados."""
    texto_original = run.text

    # Conservar el formato del run original como base
    base_font_name = run.font.name
    base_font_size = run.font.size
    base_font_bold = run.font.bold
    base_font_color_rgb = None
    try:
        if run.font.color and run.font.color.type:
            base_font_color_rgb = run.font.color.rgb
    except Exception:
        pass

    # Primero, sustituir placeholders por su valor literal
    texto_expandido = texto_original
    for key, valor in mapping.items():
        texto_expandido = texto_expandido.replace(
            "{{" + key + "}}", str(valor) if valor is not None else ""
        )

    # Limpiar el run original (lo vamos a reescribir como secuencia de runs)
    run.text = ""

    # Dividir por backticks: alternar texto plano y código
    partes = re.split(r"(`[^`]+`)", texto_expandido)

    # El primer run ya existe; rellenamos su texto con la primera parte
    primera = True
    para_xml = para._p
    # Limpiar a partir del run original todos los runs siguientes que estaban en este párrafo
    # (estamos dentro del bucle paraventana sobre runs, pero como ya consumimos los
    # placeholders del original solo, esto está OK)

    for parte in partes:
        if not parte:
            continue
        if parte.startswith("`") and parte.endswith("`"):
            # Código inline
            contenido = parte[1:-1]
            if primera:
                r = run
                primera = False
            else:
                r = para.add_run()
            r.text = contenido
            r.font.name = "Consolas"
            if base_font_size:
                r.font.size = base_font_size
            r.font.bold = base_font_bold
            r.font.color.rgb = COLOR_CODIGO_INLINE
        else:
            # Texto normal
            if primera:
                r = run
                primera = False
            else:
                r = para.add_run()
            r.text = parte
            r.font.name = base_font_name or "Calibri"
            if base_font_size:
                r.font.size = base_font_size
            r.font.bold = base_font_bold
            if base_font_color_rgb:
                r.font.color.rgb = base_font_color_rgb


# =====================================================================
# REGLA MIXTA DE FUENTE PARA CÓDIGO (ajuste sobre contenido real)
# =====================================================================

def calcular_tamano_codigo(texto, ancho_caja_in, tam_max=20, tam_min=16):
    """Elige el mayor tamaño (20 -> 18 -> 16) con que la línea más larga cabe.

    Consolas es monoespaciada (~0.60 * pt de ancho por glifo). ancho_caja_in
    es el ancho útil de la caja en pulgadas. Devuelve un entero de tamaño en pt.
    """
    lineas = (texto or "").split("\n")
    max_chars = max((len(l) for l in lineas), default=0)
    if max_chars == 0:
        return tam_max
    ancho_util_pt = (ancho_caja_in - 0.30) * 72.0  # ~0.15" de padding por lado
    for tam in sorted({tam_max, 18, tam_min}, reverse=True):
        if max_chars * (0.60 * tam) <= ancho_util_pt:
            return tam
    return tam_min


def ajustar_fuente_codigo_en_shape(slide, placeholder_key, ancho_caja_in,
                                   texto_real, tam_max=20, tam_min=16):
    """Tras reemplazar un placeholder de código, reajusta el tamaño de fuente
    de los runs Consolas del shape que contenía ese placeholder.

    Se llama ANTES del reemplazo: localiza el shape cuyo text_frame todavía
    contiene "{{KEY}}", calcula el tamaño según texto_real y lo aplica a todos
    sus runs. Devuelve el tamaño aplicado (o None si no encontró el shape).
    """
    tam = calcular_tamano_codigo(texto_real, ancho_caja_in, tam_max, tam_min)
    objetivo = "{{" + placeholder_key + "}}"
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        if objetivo in shape.text_frame.text:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(tam)
            return tam
    return None


def buscar_shape_por_key(slide, key):
    """Encuentra la shape que contiene {{KEY}} en su texto (antes de reemplazar)."""
    token = "{{" + key + "}}"
    for shape in slide.shapes:
        if shape.has_text_frame:
            texto = " ".join(r.text for p in shape.text_frame.paragraphs for r in p.runs)
            if token in texto:
                return shape
    return None


def eliminar_shape_de_slide(slide, shape):
    """Elimina una shape del XML del slide."""
    sp = shape._element
    sp.getparent().remove(sp)


def extraer_tabla_md(texto):
    """Extrae una tabla markdown del texto.
    Devuelve (texto_sin_tabla, lista_de_filas) o (texto_original, None).
    Cada fila es una lista de strings (celdas). La fila separadora (---) se omite.
    """
    if not texto or "|" not in texto:
        return texto, None
    patron = r"((?:\|.+\|\n?)+)"
    m = re.search(patron, texto)
    if not m:
        return texto, None
    tabla_texto = m.group(1)
    texto_limpio = (texto[:m.start()] + texto[m.end():]).strip()
    filas = []
    for linea in tabla_texto.strip().split("\n"):
        if re.match(r"^\|[\s\-|]+\|$", linea.strip()):
            continue  # fila separadora
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if any(c for c in celdas):
            filas.append(celdas)
    return texto_limpio, filas if filas else None


def insertar_tabla_pptx(slide, filas, left, top, width, height):
    """Agrega una tabla estilizada (marca oscura) al slide en la posición dada."""
    from pptx.util import Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN

    if not filas:
        return
    n_rows = len(filas)
    n_cols = max(len(f) for f in filas)

    tbl = slide.shapes.add_table(n_rows, n_cols, left, top, width, height).table

    COLOR_HEADER_BG = RGBColor(0x0D, 0x2B, 0x3E)
    COLOR_ROW_BG    = RGBColor(0x12, 0x22, 0x32)
    COLOR_ROW_ALT   = RGBColor(0x0A, 0x1A, 0x28)
    COLOR_TEXTO     = RGBColor(0xFF, 0xFF, 0xFF)
    COLOR_CODIGO    = RGBColor(0x4A, 0xDF, 0xCB)

    for r_idx, fila in enumerate(filas):
        for c_idx in range(n_cols):
            cell = tbl.cell(r_idx, c_idx)
            cell.margin_left  = Emu(91440)
            cell.margin_right = Emu(91440)
            cell.margin_top   = Emu(45720)
            cell.margin_bottom= Emu(45720)
            cell.fill.solid()
            if r_idx == 0:
                cell.fill.fore_color.rgb = COLOR_HEADER_BG
            elif r_idx % 2 == 1:
                cell.fill.fore_color.rgb = COLOR_ROW_BG
            else:
                cell.fill.fore_color.rgb = COLOR_ROW_ALT

            texto_celda = fila[c_idx] if c_idx < len(fila) else ""
            tf = cell.text_frame
            tf.word_wrap = True
            para = tf.paragraphs[0]
            # Detectar si hay backticks (código inline)
            partes = re.split(r"`([^`]+)`", texto_celda)
            for k, parte in enumerate(partes):
                if not parte:
                    continue
                run = para.add_run()
                run.text = parte
                run.font.size = Pt(14) if r_idx == 0 else Pt(13)
                run.font.bold = r_idx == 0
                if k % 2 == 1:  # estaba entre backticks
                    run.font.name = "Consolas"
                    run.font.color.rgb = COLOR_CODIGO
                else:
                    run.font.color.rgb = COLOR_TEXTO


def adaptar_layout_concepto(slide, concepto):
    """Post-procesa un slide de concepto para adaptar el layout al contenido real.
    Debe llamarse DESPUÉS de reemplazar_placeholders.
    Recibe las shape references guardadas antes del reemplazo.
    """
    pass  # lógica delegada a las referencias guardadas en generar_ppt


def ocultar_filas_vacias_multi(slide, filas_vacias):
    """Elimina las cajas, etiquetas y textos de las filas no usadas del slide
    apilado, identificándolas por su rango vertical EXACTO (no por proximidad).

    filas_vacias: lista de números de fila (1..3) que deben ocultarse.

    La geometría debe coincidir con construir_slide_codigo_resultado_multi:
      FILA_Y0 = 2.25, FILA_PASO = 1.62, LABEL_H = 0.34, FILA_H = 1.42
    Una fila i ocupa verticalmente desde y_label hasta el fondo de la caja.
    """
    FILA_Y0 = 2.25
    FILA_PASO = 1.62
    LABEL_H = 0.34
    FILA_H = 1.42
    MARGEN = 0.05  # tolerancia

    rangos = []
    for i in filas_vacias:
        y_top = FILA_Y0 + (i - 1) * FILA_PASO - MARGEN
        y_bottom = y_top + LABEL_H + FILA_H + 2 * MARGEN
        rangos.append((Inches(y_top), Inches(y_bottom)))

    for shape in list(slide.shapes):
        try:
            top = shape.top
            bottom = shape.top + shape.height
        except Exception:
            continue
        for (y0, y1) in rangos:
            # El shape pertenece a la fila si su centro cae dentro del rango
            centro = (top + bottom) // 2
            if y0 <= centro <= y1:
                shape._element.getparent().remove(shape._element)
                break


# =====================================================================
# CONSTRUCCIÓN DEL PPT
# =====================================================================

def generar_ppt(spec: dict, ruta_salida: Path):
    if not RUTA_PLANTILLA.exists():
        raise FileNotFoundError(f"No se encontró la plantilla en {RUTA_PLANTILLA}")

    prs = Presentation(str(RUTA_PLANTILLA))
    n = spec["numero_clase"]
    num = f"{n:02d}" if isinstance(n, int) else (str(n) if n is not None else "??")
    tema = spec["tema"] or "Clase de Python"

    # === Bienvenida ===
    sl = duplicar_slide(prs, prs.slides[M_BIENVENIDA])
    reemplazar_placeholders(sl, {
        "TITULO_CLASE": tema,
        "SUBTITULO": generar_subtitulo(spec),
        "NUMERO_CLASE": num,
        "MENSAJE_HOY": generar_mensaje_hoy(spec),
    })

    # === Objetivo ===
    sl = duplicar_slide(prs, prs.slides[M_OBJETIVO])
    reemplazar_placeholders(sl, {
        "NUMERO_CLASE": num,
        "TITULO_CLASE": tema,
        "OBJETIVO": spec["objetivo"] or "",
        "PROPOSITO": spec["proposito"] or "",
        "REGLAS": generar_reglas(),
    })

    # === Haz Ahora ===
    if spec["haz_ahora"]:
        sl = duplicar_slide(prs, prs.slides[M_STOCK_TITULO])
        ha = separar_haz_ahora(spec["haz_ahora"])
        tiene_codigo_ha = bool(ha["codigo"])
        shape_cod_ha = buscar_shape_por_key(sl, "CONTENIDO_CODIGO")
        shape_txt_ha = buscar_shape_por_key(sl, "CONTENIDO_TEXTO")
        reemplazar_placeholders(sl, {
            "NUMERO_CLASE": num,
            "SECCION": "Haz Ahora",
            "TITULO_SLIDE": "⚡ Haz Ahora",
            "SUBTITULO_SLIDE": ha["intro"],
            "CONTENIDO_TEXTO": ha["texto"],
            "CONTENIDO_CODIGO": ha["codigo"] or "",
            "NOTA_INFERIOR": "💡 Idea clave: lo que ya sabes te ayuda a entender lo nuevo.",
        })
        if not tiene_codigo_ha and shape_cod_ha and shape_txt_ha:
            extra = shape_cod_ha.height
            eliminar_shape_de_slide(sl, shape_cod_ha)
            shape_txt_ha.height += extra

    # === ICN: un slide por concepto (layout adaptativo) ===
    for concepto in spec["icn"]["conceptos"]:
        sl = duplicar_slide(prs, prs.slides[M_CONCEPTO])

        tiene_codigo = bool(concepto["ejemplo"])
        texto_def = concepto["definicion"] or ""
        texto_sin_tabla, filas_tabla = extraer_tabla_md(texto_def)
        tiene_tabla = filas_tabla is not None

        # Guardar referencias ANTES de reemplazar
        shape_def  = buscar_shape_por_key(sl, "DEFINICION")
        shape_cod  = buscar_shape_por_key(sl, "EJEMPLO_CODIGO")
        shape_idea = buscar_shape_por_key(sl, "IDEA_CLAVE")

        reemplazar_placeholders(sl, {
            "NUMERO_CLASE": num,
            "SECCION": "Contenido nuevo",
            "TITULO_CONCEPTO": f"📘 {concepto['numero']}. {concepto['nombre']}",
            "DEFINICION": texto_sin_tabla if tiene_tabla else texto_def,
            "EJEMPLO_CODIGO": concepto["ejemplo"] or "",
            "IDEA_CLAVE": concepto["idea_clave"] or "",
        })

        # Post-proceso: adaptar layout según contenido
        if tiene_tabla and shape_cod:
            left, top = shape_cod.left, shape_cod.top
            width, height = shape_cod.width, shape_cod.height
            eliminar_shape_de_slide(sl, shape_cod)
            insertar_tabla_pptx(sl, filas_tabla, left, top, width, height)
        elif not tiene_codigo and shape_cod and shape_def:
            cod_height = shape_cod.height
            eliminar_shape_de_slide(sl, shape_cod)
            if shape_idea:
                shape_def.height  += cod_height * 2 // 3
                shape_idea.top    -= cod_height // 3
                shape_idea.height += cod_height // 3
            else:
                shape_def.height += cod_height

    # === Tabla de errores ===
    if spec["icn"]["errores_tabla"]:
        sl = duplicar_slide(prs, prs.slides[M_TABLA])
        mapping = {
            "NUMERO_CLASE": num,
            "SECCION": "Errores típicos",
            "TITULO_SLIDE": "⚠️ Errores típicos a evitar",
            "NOTA_INFERIOR": "💡 Si te aparece uno de estos errores, vuelve a esta tabla antes de pedir ayuda.",
        }
        for i, fila in enumerate(spec["icn"]["errores_tabla"][:3], start=1):
            for j, valor in enumerate(fila[:3], start=1):
                mapping[f"FILA_{i}_COL_{j}"] = valor
        for i in range(1, 4):
            for j in range(1, 4):
                k = f"FILA_{i}_COL_{j}"
                if k not in mapping:
                    mapping[k] = ""
        reemplazar_placeholders(sl, mapping)

    # === Demostraciones apiladas (slide tipo 9, layout estrella) ===
    for demo in spec["icn"].get("demos_apiladas", []):
        sl = duplicar_slide(prs, prs.slides[M_CODIGO_RESULTADO_MULTI])
        filas = demo["filas"][:3]  # máximo 3 filas por slide

        mapping = {
            "NUMERO_CLASE": num,
            "SECCION": "Contenido nuevo",
            "TITULO_SLIDE": demo["titulo"],
            "SUBTITULO_SLIDE": demo.get("subtitulo", ""),
        }
        for idx in range(1, 4):
            if idx <= len(filas):
                fila = filas[idx - 1]
                mapping[f"FILA_{idx}_LABEL"] = fila.get("label", "")
                mapping[f"FILA_{idx}_CODIGO"] = fila.get("codigo", "")
                mapping[f"FILA_{idx}_RESULTADO"] = fila.get("resultado", "")
            else:
                mapping[f"FILA_{idx}_LABEL"] = ""
                mapping[f"FILA_{idx}_CODIGO"] = ""
                mapping[f"FILA_{idx}_RESULTADO"] = ""

        # Regla mixta de fuente: ANTES de reemplazar, ajustar el tamaño de los
        # runs de cada caja de código/resultado según su contenido real.
        for idx in range(1, len(filas) + 1):
            fila = filas[idx - 1]
            ajustar_fuente_codigo_en_shape(
                sl, f"FILA_{idx}_CODIGO", ANCHO_CAJA_CODIGO_MULTI,
                fila.get("codigo", ""))
            ajustar_fuente_codigo_en_shape(
                sl, f"FILA_{idx}_RESULTADO", ANCHO_CAJA_RESULTADO_MULTI,
                fila.get("resultado", ""))

        reemplazar_placeholders(sl, mapping)

        # Ocultar las filas que no se usaron
        filas_vacias = [i for i in range(1, 4) if i > len(filas)]
        if filas_vacias:
            ocultar_filas_vacias_multi(sl, filas_vacias)

    # === Práctica Guiada ===
    if spec["guiada"]["situacion"]:
        sl = duplicar_slide(prs, prs.slides[M_CODIGO_RESULTADO])
        reemplazar_placeholders(sl, {
            "NUMERO_CLASE": num,
            "SECCION": "Práctica guiada",
            "TITULO_SLIDE": "🛠️ Práctica guiada",
            "SUBTITULO_SLIDE": spec["guiada"]["situacion"],
            "CODIGO": spec["guiada"]["variables"] or "",
            "RESULTADO": spec["guiada"]["resultado"] or "",
            "NOTA_INFERIOR": "👥 Construyan el programa paso a paso junto al profe.",
        })

    # === Ejercicios independientes ===
    for ej in spec["independiente"]:
        sl = duplicar_slide(prs, prs.slides[M_EJERCICIO])
        reemplazar_placeholders(sl, {
            "NUMERO_CLASE": num,
            "SECCION": "Práctica independiente",
            "TITULO_SLIDE": f"💻 Ejercicio {ej['numero']} — {ej['titulo']}",
            "ENUNCIADO": ej["enunciado"] or "",
            "RESULTADO_ESPERADO": ej["resultado"] or "",
            "NOTA_INFERIOR": "⏱️ Si te atascas más de 10 minutos, pregunta al profe.",
        })

    # === Ticket de salida ===
    if spec["ticket"]["tarea"]:
        sl = duplicar_slide(prs, prs.slides[M_TICKET])
        reemplazar_placeholders(sl, {
            "NUMERO_CLASE": num,
            "SECCION": "Ticket de salida",
            "TAREA": spec["ticket"]["tarea"],
            "ENTREGA": spec["ticket"]["entrega"] or "Subir evidencia a Google Classroom.",
        })

    # === Cierre ===
    if spec["cierre"]:
        sl = duplicar_slide(prs, prs.slides[M_CIERRE])
        mapping = {
            "NUMERO_CLASE": num,
            "SECCION": "Cierre",
        }
        for i in range(1, 4):
            mapping[f"PREGUNTA_{i}"] = spec["cierre"][i - 1] if i - 1 < len(spec["cierre"]) else ""
        reemplazar_placeholders(sl, mapping)

    eliminar_slides(prs, list(range(10)))
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(ruta_salida))


# =====================================================================
# HELPERS DE CONTENIDO
# =====================================================================

def generar_subtitulo(spec: dict) -> str:
    contenidos_nuevos = spec["contexto"].get("Contenidos nuevos", "")
    if contenidos_nuevos:
        return f"Hoy: {contenidos_nuevos}"
    return ""


def generar_mensaje_hoy(spec: dict) -> str:
    """Mensaje motivador para la portada.

    Combina el tema de la clase con un mensaje inspirador relacionado.
    Si el propósito tiene una analogía o ejemplo concreto (Steam, juegos,
    apps, etc.), lo usa. Si no, genera uno genérico pero específico al tema.
    """
    tema = spec.get("tema") or "programar"
    proposito = spec.get("proposito") or ""

    # Intentar extraer la frase con la analogía/ejemplo concreto del propósito
    # (típicamente después de "—" o que mencione una app/juego/situación real)
    if proposito:
        # Buscar oración que tenga una analogía concreta (después de — o que mencione "como")
        match_analogia = re.search(
            r"(?:—|—|como )\s*([^.—]+(?:Steam|juego|app|aplicación|YouTube|Spotify|Instagram|TikTok|servicio|sitio|red social|programa)[^.]*)",
            proposito, re.IGNORECASE
        )
        if match_analogia:
            analogia = match_analogia.group(1).strip().rstrip(",;:")
            if len(analogia) < 130:
                return f"Hoy darás un salto: pasarás de ver código a controlarlo {analogia} 🚀"

        # Si no hay analogía clara, usar la primera oración del propósito pero con marco motivador
        primera = proposito.split(".")[0].strip()
        if len(primera) > 0 and len(primera) < 130:
            # Si la primera oración suena descriptiva, le agregamos un marco motivador
            return f"{primera}. Hoy desbloqueas una herramienta nueva ⚡"

    # Fallback: mensaje genérico pero específico al tema
    return f"Hoy aprenderás {tema} — un paso más para que tu código haga cosas reales 🚀"


def generar_reglas() -> str:
    return ("📓 Todo comando nuevo va al cuaderno.\n"
            "🚫 NO hagan copiar-pegar de los comandos.\n"
            "✨ En toda evaluación podrán usar sus apuntes.")


# =====================================================================
# MAIN
# =====================================================================

def main():
    if len(sys.argv) != 3:
        print("Uso: python crear_ppt.py <ruta_spec.md> <ruta_salida.pptx>")
        sys.exit(1)
    ruta_spec = Path(sys.argv[1])
    ruta_salida = Path(sys.argv[2])
    if not ruta_spec.exists():
        print(f"ERROR: no existe {ruta_spec}")
        sys.exit(1)
    if not RUTA_PLANTILLA.exists():
        print(f"ERROR: falta plantilla en {RUTA_PLANTILLA}")
        sys.exit(1)
    print(f"📖 Leyendo spec: {ruta_spec}")
    spec = parsear_spec(ruta_spec)
    print(f"✅ Parseado: Clase {spec['numero_clase']} — {spec['tema']}")
    print(f"   - {len(spec['icn']['conceptos'])} conceptos")
    print(f"   - {len(spec['icn']['errores_tabla'])} errores típicos")
    print(f"   - {len(spec['independiente'])} ejercicios")
    print("🛠️  Generando presentación...")
    generar_ppt(spec, ruta_salida)
    print(f"💾 PPT guardado en: {ruta_salida}")


if __name__ == "__main__":
    main()
