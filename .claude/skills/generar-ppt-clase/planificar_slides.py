"""
planificar_slides.py — Capa de planificación pedagógica de ICN.

Recibe los conceptos y demos del spec parseado y produce una lista de SlidePlan:
objetos que describen QUÉ va en cada slide, sin decidir el render todavía.
El planificador usa el presupuesto de densidad (filas visuales) para decidir
cuántos slides generar y qué composición usar.
"""

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
    - anatomia, analogia, antes_despues, frase_clave → slide propio con
      constructor existente (ya funcionan bien).
    - Concepto clásico (definición + código + idea clave opcional) → slide
      ICN flexible con composición dinámica de bloques.
    - Dos conceptos clásicos adyacentes con densidad combinada ≤ 14 → fusión
      en un único slide.
    - Demos → cada una mantiene su slide apilado al final.
    """
    # Intercalar demos al final (v1: no inferimos posición relativa)
    items = _intercalar_demos(conceptos, demos)

    planes = []
    i = 0
    while i < len(items):
        item = items[i]

        # — Demo —
        if item.get("_es_demo"):
            planes.append(SlidePlan(
                tipo_slide="tabla_demos",
                titulo=item.get("titulo", "Demostración"),
                seccion="Contenido nuevo",
                concepto=item,
            ))
            i += 1
            continue

        concepto = item
        tipo = _tipo_layout(concepto)

        # — Layouts especiales: slide propio, constructor existente —
        if tipo in ("anatomia", "analogia", "antes_despues", "frase_clave"):
            planes.append(SlidePlan(
                tipo_slide=tipo,
                titulo=f"📘 {concepto['numero']}. {concepto['nombre']}",
                seccion="Contenido nuevo",
                concepto=concepto,
            ))
            i += 1
            continue

        # — Concepto clásico → slide flexible —
        bloques_actual = _bloques_clasico(concepto)
        densidad_actual = sum(b.filas for b in bloques_actual)

        # Intentar fusionar con el siguiente si también es clásico y cabe
        siguiente = items[i + 1] if i + 1 < len(items) else None
        puede_fusionar = (
            siguiente is not None
            and not siguiente.get("_es_demo")
            and _tipo_layout(siguiente) == "concepto"
        )

        if puede_fusionar:
            bloques_sig = _bloques_clasico(siguiente)
            densidad_combinada = (
                densidad_actual
                + _COSTO["separador"]
                + sum(b.filas for b in bloques_sig)
            )
            if densidad_combinada <= PRESUPUESTO_OBJETIVO:
                todos = (bloques_actual
                         + [BloquePlan("separador", "", _COSTO["separador"])]
                         + bloques_sig)
                titulo_fusionado = (
                    f"📘 {concepto['numero']}–{siguiente['numero']}. "
                    f"{concepto['nombre']} y {siguiente['nombre']}"
                )
                planes.append(SlidePlan(
                    tipo_slide="icn_flexible",
                    titulo=titulo_fusionado,
                    bloques=todos,
                    densidad=densidad_combinada,
                    concepto=concepto,
                    justificacion=f"Fusionados: densidad {densidad_combinada:.1f} ≤ {PRESUPUESTO_OBJETIVO}",
                ))
                i += 2
                continue

        # Sin fusión
        justificacion = ""
        if densidad_actual > PRESUPUESTO_REFERENCIA:
            justificacion = (
                f"⚠ Densidad {densidad_actual:.1f} > {PRESUPUESTO_REFERENCIA} "
                f"(referencia) — contenido pedagógicamente necesario"
            )

        planes.append(SlidePlan(
            tipo_slide="icn_flexible",
            titulo=f"📘 {concepto['numero']}. {concepto['nombre']}",
            bloques=bloques_actual,
            densidad=densidad_actual,
            concepto=concepto,
            justificacion=justificacion,
        ))
        i += 1

    return planes


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

    if concepto.get("definicion"):
        filas = _costo_definicion(concepto["definicion"])
        bloques.append(BloquePlan(
            tipo="definicion",
            contenido=concepto["definicion"],
            filas=filas,
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

    Identifica tres partes:
    - intro: instrucción principal (todo lo que aparece antes de los ítems numerados)
    - situaciones: lista de strings con los ítems numerados (ej. "1. El PIN...")
    - cierre: texto de cierre (lo que aparece después de los ítems)

    Retorna dict con:
      tipo: "situaciones" | "libre"
      intro: str
      situaciones: list[str]
      cierre: str
    """
    import re

    if not texto:
        return {"tipo": "libre", "intro": "", "situaciones": [], "cierre": ""}

    lineas = texto.strip().split("\n")
    intro_lineas = []
    situaciones = []
    cierre_lineas = []
    en_situaciones = False

    for linea in lineas:
        linea_stripped = linea.strip()
        if not linea_stripped:
            continue
        m = re.match(r"^(\d+)\.\s+(.+)$", linea_stripped)
        if m:
            en_situaciones = True
            situaciones.append(f"{m.group(1)}. {m.group(2)}")
        elif en_situaciones:
            cierre_lineas.append(linea_stripped)
        else:
            intro_lineas.append(linea_stripped)

    intro = " ".join(intro_lineas).strip()
    cierre = " ".join(cierre_lineas).strip()
    tipo = "situaciones" if situaciones else "libre"

    # TODO (caso futuro): algunos Haz Ahora pueden tener un bloque de código Python
    # (ej. "ejecuta esto y observa qué devuelve") seguido de preguntas asociadas.
    # En ese caso, "tipo" debería ser "codigo_preguntas" y el plan debería incluir
    # una caja terminal + una caja de preguntas debajo, respetando el presupuesto
    # de densidad. Por ahora se caen en "libre" (texto sin parsear), que funciona
    # razonablemente bien aunque sin el estilo visual de terminal.

    return {
        "tipo": tipo,
        "intro": intro,
        "situaciones": situaciones,
        "cierre": cierre,
    }
