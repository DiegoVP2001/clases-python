"""Genera 'Clase 43 - Neurona v2 - Ticket de Salida.pptx' con el generador estándar del ticket.

Las preguntas salen de generar_clase_v2.py (fuente de verdad). El PPT NO se sube a GitHub antes de proyectarlo
(el repo es público): se commitea solo después de dictar la clase.

Uso: py -3 -X utf8 crear_ticket_ppt_v2.py
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / ".claude" / "skills" / "generar-ppt-clase"))
sys.path.insert(0, str(AQUI))

import crear_ppt_ticket as t  # noqa: E402
import generar_clase_v2 as g  # noqa: E402
from pptx import Presentation  # noqa: E402
from pptx.util import Inches  # noqa: E402

SALIDA = AQUI / "Clase 43 - Neurona v2 - Ticket de Salida.pptx"


def construir_datos():
    preguntas = []
    for i, (_titulo, enunciado, alternativas) in enumerate(g.TICKET_PREGUNTAS):
        m = re.search(r"```(?:python|text)?\n(.*?)```", enunciado, re.DOTALL)
        codigo = m.group(1).rstrip("\n") if m else ""
        texto = (enunciado[:m.start()] + " " + enunciado[m.end():]) if m else enunciado
        texto = " ".join(texto.split())
        preguntas.append({"enunciado": texto, "codigo": codigo, "alternativas": list(zip("ABCD", alternativas)),
                          "correcta": g.TICKET_CORRECTAS[i], "justificacion": g.TICKET_JUSTIFICACION[i]})
    return {"numero": "43 v2", "tema": "La neurona aprende sola", "tema_breve_form": g.TEMA_FORM, "preguntas": preguntas}


def main():
    datos = construir_datos()
    prs = Presentation()
    prs.slide_width = Inches(t._W)
    prs.slide_height = Inches(t._H)
    t.slide_portada(prs, datos)
    for i in range(len(datos["preguntas"])):
        t.slide_pregunta(prs, datos, i)
    t.slide_formulario(prs, datos)
    for i in range(len(datos["preguntas"])):
        t.slide_revision(prs, datos, i)
    prs.save(str(SALIDA))
    print("OK", SALIDA.name, len(prs.slides), "slides")


if __name__ == "__main__":
    main()
