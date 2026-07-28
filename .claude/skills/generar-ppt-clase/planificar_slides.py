"""
planificar_slides.py — Capa de planificación pedagógica de ICN.

Recibe los conceptos y demos del spec parseado y produce una lista de SlidePlan:
objetos que describen QUÉ va en cada slide, sin decidir el render todavía.
El planificador usa el presupuesto de densidad (filas visuales) para decidir
cuántos slides generar y qué composición usar.
"""

import re
from dataclasses import dataclass, field

# =====================================================================
# PRESUPUESTO DE DENSIDAD (filas visuales a 18-22pt en área útil)
# =====================================================================

PRESUPUESTO_OBJETIVO   = 14   # cabe cómodo
PRESUPUESTO_REFERENCIA = 16   # umbral de alerta — puede superarse si hay justificación pedagógica

# Costos base en filas por tipo de elemento
_COSTO = {
    "bullet_item":    1.0,
    "bullets_header": 0.5,
    "tabla_fila":     1.2,
    "tabla_header":   1.0,
    "codigo_linea":   1.0,
    "codigo_header":  1.0,
    "idea_clave":     2.0,
    "pregunta":       1.5,
    "advertencia":    1.5,
    "separador":      0.5,
}


def _extraer_tabla_md(texto: str):
    """Extrae la primera tabla markdown del texto.
    Devuelve (texto_sin_tabla, filas) o (texto_original, None).
    La fila separadora (---) se omite. La primera fila es el header.
    """
    if not texto or "|" not in texto:
        return texto, None
    patron = r"((?:[ \t]*\|.+\|\s*\n?)+)"
    m = re.search(patron, texto)
    if not m:
        return texto, None
    tabla_texto = m.group(1)
    texto_limpio = (texto[:m.start()] + texto[m.end():]).strip()
    filas = []
    for linea in tabla_texto.strip().split("\n"):
        linea_s = linea.strip()
        if re.match(r"^\|[\s\-:|]+\|$", linea_s):
            continue  # fila separadora
        celdas = [c.strip() for c in linea_s.strip("|").split("|")]
        if any(c for c in celdas):
            filas.append(celdas)
    return texto_limpio, filas if filas else None


def _costo_definicion(texto: str) -> float:
    """Estima filas de una definición: Calibri 22pt, ~50 chars/línea en 12" útil."""
    if not texto:
        return 0.0
    chars = len(texto)
    lineas = max(1, -(-chars // 50))   # ceil division
    return lineas + 0.5                 # +0.5 de respiro antes del siguiente bloque


def _costo_codigo(texto: str) -> float:
    """Filas de un bloque de código: líneas + 1 de header/label."""
    if not texto:
        return 0.0
    lineas = len(texto.strip().split("\n"))
    return lineas + _COSTO["codigo_header"]


# =====================================================================
# ESTRUCTURAS DE DATOS
# =====================================================================

@dataclass
class BloquePlan:
    tipo: str           # "definicion" | "codigo" | "bullets" | "tabla"
                        # "idea_clave" | "advertencia" | "pregunta" | "separador"
    contenido: object   # str, list[str], o list[list[str]] según tipo
    filas: float = 0.0  # costo estimado en filas visuales
    label: str = ""     # etiqueta visible del bloque (ej: "Definición", "Ejemplo")


@dataclass
class SlidePlan:
    tipo_slide: str     # "icn_flexible" | "anatomia" | "analogia"
                        # "antes_despues" | "tabla_demos" | "frase_clave"
    titulo: str
    seccion: str = "Contenido nuevo"
    bloques: list = field(default_factory=list)
    densidad: float = 0.0
    concepto: dict = field(default_factory=dict)   # datos del concepto original
    justificacion: str = ""                        # nota si se superó la referencia


# =====================================================================
# PLANIFICADOR DE ICN
# =====================================================================

def planificar_icn(conceptos: list, demos: list, num_clase: str) -> list:
    """Produce la lista de SlidePlan para toda la sección ICN.

    Estrategia:
    1. Slide individual por cada concepto (icn_flexible para clásicos, slide propio para tipos especiales).
    2. Demos siguen inmediatamente al concepto al que pertenecen.
    3. Al final de todos los slides individuales: UN slide dos_columnas de resumen compacto
       (solo si hay ≥2 conceptos clásicos).
    """
    items = _intercalar_demos(conceptos, demos)
    planes = []
    clasicos_vistos = []   # para el resumen final dos_columnas

    for item in items:
        if item.get("_es_demo"):
            planes.append(SlidePlan(
                tipo_slide="tabla_demos",
                titulo=item.get("titulo", "Demostración"),
                seccion="Contenido nuevo",
                concepto=item,
            ))
            continue

        concepto = item
        tipo = _tipo_layout(concepto)

        if tipo in ("anatomia", "analogia", "antes_despues", "frase_clave"):
            planes.append(SlidePlan(
                tipo_slide=tipo,
                titulo=f"📘 {concepto['numero']}. {concepto['nombre']}",
                seccion="Contenido nuevo",
                concepto=concepto,
            ))
            continue

        # Concepto clásico: slide individual
        bloques = _bloques_clasico(concepto)
        densidad = sum(b.filas for b in bloques)
        justificacion = ""
        if densidad > PRESUPUESTO_REFERENCIA:
            justificacion = (
                f"⚠ Densidad {densidad:.1f} > {PRESUPUESTO_REFERENCIA} "
                f"— contenido pedagógicamente necesario"
            )
        planes.append(SlidePlan(
            tipo_slide="icn_flexible",
            titulo=f"📘 {concepto['numero']}. {concepto['nombre']}",
            bloques=bloques,
            densidad=densidad,
            concepto=concepto,
            justificacion=justificacion,
        ))
        clasicos_vistos.append(concepto)

    # Slide resumen al final: dos_columnas con todos los conceptos clásicos
    if len(clasicos_vistos) >= 2:
        planes.append(_plan_dos_columnas(clasicos_vistos))

    return planes


def _plan_dos_columnas(conceptos: list) -> SlidePlan:
    """Un SlidePlan de tipo dos_columnas para N conceptos clásicos.

    Izquierda: bullets (nombre + definición primera oración) de cada concepto.
    Derecha: código + output del primer concepto que tenga ejemplo.
    """
    nums = [c.get("numero", "?") for c in conceptos]
    if len(nums) == 1:
        titulo = f"📘 {nums[0]}. {conceptos[0].get('nombre', '')}"
    else:
        titulo = f"📘 Conceptos {nums[0]}–{nums[-1]}"

    # Código a mostrar: primer concepto con ejemplo (preferir el más representativo)
    codigo = ""
    output = ""
    for c in conceptos:
        if c.get("ejemplo"):
            codigo = c["ejemplo"]
            output = c.get("output", "")
            break

    codigo_display = codigo
    if output:
        codigo_display = codigo + "\n" + output

    # Bullets: nombre + primera oración completa de la definición (sin truncar)
    bullets = []
    for c in conceptos:
        nombre = c.get("nombre", "")
        defn = c.get("definicion", "") or ""
        primera = re.split(r"(?<=[.!?])\s+", defn)[0].strip() if defn else ""
        bullets.append({
            "numero": c.get("numero", ""),
            "nombre": nombre,
            "definicion": primera,
        })

    return SlidePlan(
        tipo_slide="dos_columnas",
        titulo=titulo,
        seccion="Contenido nuevo",
        bloques=[],
        densidad=0.0,
        concepto={
            "bullets": bullets,
            "codigo": codigo_display,
            "conceptos_originales": conceptos,
        },
        justificacion="",
    )


# =====================================================================
# HELPERS INTERNOS
# =====================================================================

def _tipo_layout(concepto: dict) -> str:
    """Detecta el tipo de layout para un concepto (misma lógica que seleccionar_layout_concepto)."""
    tipo_ex = (concepto.get("tipo") or "").lower()
    if tipo_ex in {"anatomia", "anatomía", "anatomy"}:
        return "anatomia"
    if tipo_ex in {"analogia", "analogía", "analogy"}:
        return "analogia"
    if tipo_ex in {"antes_despues", "antes-despues", "comparison",
                   "comparacion", "comparación"}:
        return "antes_despues"
    if tipo_ex in {"frase_clave", "frase-clave", "pull_quote",
                   "pull-quote", "quote"}:
        return "frase_clave"
    if concepto.get("partes"):
        return "anatomia"
    if concepto.get("analogia_filas"):
        return "analogia"
    if concepto.get("antes_codigo") and concepto.get("despues_codigo"):
        return "antes_despues"
    return "concepto"


def _bloques_clasico(concepto: dict) -> list:
    """Produce los BloquePlan para un concepto tipo clásico."""
    bloques = []

    if concepto.get("tabla_comparacion"):
        filas = concepto["tabla_comparacion"]
        bloques.append(BloquePlan(
            tipo="tabla",
            contenido=filas,
            filas=len(filas) * _COSTO["tabla_fila"],
            label="",
        ))

    if concepto.get("definicion"):
        texto_def = concepto["definicion"]
        texto_sin_tabla, filas_tabla = _extraer_tabla_md(texto_def)
        if filas_tabla:
            if texto_sin_tabla:
                bloques.append(BloquePlan(
                    tipo="definicion",
                    contenido=texto_sin_tabla,
                    filas=_costo_definicion(texto_sin_tabla),
                    label="Definición",
                ))
            costo_tabla = len(filas_tabla) * _COSTO["tabla_fila"]
            bloques.append(BloquePlan(
                tipo="tabla",
                contenido=filas_tabla,
                filas=costo_tabla,
                label="",
            ))
        else:
            bloques.append(BloquePlan(
                tipo="definicion",
                contenido=texto_def,
                filas=_costo_definicion(texto_def),
                label="Definición",
            ))

    if concepto.get("ejemplo"):
        filas = _costo_codigo(concepto["ejemplo"])
        bloques.append(BloquePlan(
            tipo="codigo",
            contenido=concepto["ejemplo"],
            filas=filas,
            label="Ejemplo",
        ))

    if concepto.get("idea_clave"):
        bloques.append(BloquePlan(
            tipo="idea_clave",
            contenido=concepto["idea_clave"],
            filas=_COSTO["idea_clave"],
            label="Idea clave",
        ))

    return bloques


def _intercalar_demos(conceptos: list, demos: list) -> list:
    """Inserta cada demo después del concepto al que pertenece en el spec.

    Si el concepto tiene `demos_inline` (parseadas desde su cuerpo de texto),
    se insertan inmediatamente después de ese concepto. Los demos del parámetro
    `demos` que no aparecen en ningún cuerpo se apilan al final como fallback.
    """
    ya_colocados = set()
    resultado = []

    for concepto in conceptos:
        resultado.append(concepto)
        for demo in concepto.get("demos_inline", []):
            marcado = dict(demo)
            marcado["_es_demo"] = True
            resultado.append(marcado)
            ya_colocados.add(demo.get("titulo", ""))

    # Demos huérfanas (no encontradas en ningún cuerpo de concepto): al final
    for demo in demos:
        if demo.get("titulo", "") not in ya_colocados:
            marcado = dict(demo)
            marcado["_es_demo"] = True
            resultado.append(marcado)

    return resultado


# =====================================================================
# PLANIFICADOR DE HAZ AHORA
# =====================================================================

def planificar_haz_ahora(texto: str) -> dict:
    """Parsea el texto del Haz Ahora y devuelve un plan estructurado.

    Identifica:
    - intro: texto narrativo antes de la tabla/preguntas (sin metadata interna)
    - tabla: filas de una tabla markdown (si existe), como lista de listas de celdas
    - instruccion: línea tipo "Responde en tu cuaderno:" (si existe), separada del intro
    - situaciones: ítems numerados ("1. ...", "2. ...")
    - cierre: texto después de los ítems (generalmente vacío)

    Tipos:
      "situaciones_con_tabla": hay tabla + preguntas numeradas
      "situaciones": solo preguntas numeradas
      "libre": sin ítems numerados
    """
    import re

    if not texto:
        return {"tipo": "libre", "intro": "", "tabla": None,
                "instruccion": "", "situaciones": [], "cierre": ""}

    # Eliminar metadata interna antes de parsear
    texto = re.sub(r"\*\*Propósito:\*\*[^\n]*\n?", "", texto)
    texto = re.sub(r"^\s*\(\s*\d+\s*min\s*\)\s*$", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"\*\*Actividad:\*\*\s*", "", texto)
    texto = re.sub(r"\*\*Respuestas\s+(?:del\s+Haz\s+Ahora|esperadas):\*\*.*", "", texto, flags=re.DOTALL)

    lineas = texto.strip().split("\n")
    intro_lineas = []   # todo lo que va antes de los ítems numerados (preserva vacías para tabla)
    situaciones  = []
    cierre_lineas = []
    en_situaciones = False

    for linea in lineas:
        linea_stripped = linea.strip()
        m = re.match(r"^(\d+)\.\s+(.+)$", linea_stripped)
        if m:
            en_situaciones = True
            situaciones.append(f"{m.group(1)}. {m.group(2)}")
        elif en_situaciones:
            if linea_stripped:
                cierre_lineas.append(linea_stripped)
        else:
            intro_lineas.append(linea)  # incluye líneas vacías (necesario para detectar tabla)

    # Unir con \n para que _extraer_tabla_md pueda encontrar la tabla
    intro_raw = "\n".join(intro_lineas).strip()

    # Extraer tabla markdown si existe
    intro_sin_tabla, tabla_filas = _extraer_tabla_md(intro_raw)
    intro_sin_tabla = intro_sin_tabla.strip()

    # Extraer "instrucción" = línea que introduce las preguntas (ej: "Responde en tu cuaderno:")
    instruccion = ""
    lineas_intro = [ln.strip() for ln in intro_sin_tabla.split("\n") if ln.strip()]
    if lineas_intro:
        ultima = lineas_intro[-1]
        if (ultima.endswith(":") or
                re.match(r"responde|anota|escribe|contesta", ultima, re.IGNORECASE)):
            instruccion = ultima
            lineas_intro = lineas_intro[:-1]

    intro = "\n".join(lineas_intro).strip()
    cierre = " ".join(cierre_lineas).strip()

    if tabla_filas and situaciones:
        tipo = "situaciones_con_tabla"
    elif situaciones:
        tipo = "situaciones"
    else:
        tipo = "libre"

    return {
        "tipo": tipo,
        "intro": intro,
        "tabla": tabla_filas,
        "instruccion": instruccion,
        "situaciones": situaciones,
        "cierre": cierre,
    }
