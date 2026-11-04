"""Genera 'Clase 42 - Primer Clasificador - Ticket de Salida.pptx'.

Reutiliza el diseño del generador de la skill generar-ppt-clase, pero con la
dinámica de la clase 42: no hay Google Form; el estudiante anota sus letras y
las escribe en el Colab (`respuestas = [...]` + `check_ticket(respuestas)`).
Las preguntas salen de generar_clase.py (fuente de verdad).

Uso: py -3 -X utf8 crear_ticket_ppt.py
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
SKILL = RAIZ / ".claude" / "skills" / "generar-ppt-clase"
sys.path.insert(0, str(SKILL))
sys.path.insert(0, str(AQUI))

import crear_ppt_ticket as t  # noqa: E402
import generar_clase as g  # noqa: E402
from pptx import Presentation  # noqa: E402
from pptx.util import Inches  # noqa: E402
from pptx.enum.text import PP_ALIGN  # noqa: E402

SALIDA = AQUI / "Clase 42 - Primer Clasificador - Ticket de Salida.pptx"


def construir_datos():
    preguntas = []
    for i, (_titulo, enunciado, alternativas) in enumerate(g.TICKET_PREGUNTAS):
        m = re.search(r"```(?:python|text)?\n(.*?)```", enunciado, re.DOTALL)
        codigo = m.group(1).rstrip("\n") if m else ""
        texto = (enunciado[:m.start()] + " " + enunciado[m.end():]) if m else enunciado
        texto = " ".join(texto.split())
        preguntas.append({
            "enunciado": texto,
            "codigo": codigo,
            "alternativas": list(zip("ABCD", alternativas)),
            "correcta": g.TICKET_CORRECTAS[i],
            "justificacion": g.TICKET_JUSTIFICACION[i],
        })
    return {"numero": "42", "tema": "Primer clasificador ML",
            "tema_breve_form": "", "preguntas": preguntas}


def slide_portada(prs, datos):
    slide = t._slide_base(prs, datos["numero"], "TICKET DE SALIDA")
    t._texto(slide, t._MX, 1.05, t._ANCHO_UTIL, 0.95,
             f"{t._E['ticket']}  Ticket de Salida", tamano=44, color="ambar", negrita=True)
    t._texto(slide, t._MX, 2.00, t._ANCHO_UTIL, 0.50,
             f"Clase {datos['numero']} — {datos['tema']}", tamano=22, color="blanco")
    n = len(datos["preguntas"])
    alto = 3.35
    t._rect(slide, t._MX, 2.80, t._ANCHO_UTIL, alto, t._C["fondo_bloque"])
    t._rect(slide, t._MX, 2.80, 0.08, alto, t._C["turquesa"])
    t._texto(slide, t._MX + 0.28, 2.94, t._ANCHO_UTIL - 0.5, 0.42,
             f"{t._E['idea']}  Cómo lo vamos a hacer", tamano=t._T["titulo_bloque"],
             color="turquesa", negrita=True)
    t._texto_rico(slide, t._MX + 0.28, 3.45, t._ANCHO_UTIL - 0.6, 2.55, [
        f"1.  Son {n} preguntas. Las vemos **una por una**.",
        "2.  Decide tu respuesta **en silencio** y anota la letra (**A**, **B**, **C** o **D**).",
        f"3.  Al terminar la pregunta {n}, abre el Colab: sección **Ticket de Salida**.",
        "4.  Escribe tus letras en `respuestas` y ejecuta `check_ticket(respuestas)`.",
        "5.  Después revisamos juntos las respuestas.",
    ], tamano=22, interlineado=1.05)
    t._texto(slide, t._MX, 6.50, t._ANCHO_UTIL, 0.45,
             "Es práctica sin nota: primero te comprometes con tu respuesta, "
             "después la compruebas.", tamano=17, color="gris_claro")


def slide_colab(prs, datos):
    slide = t._slide_base(prs, datos["numero"], "TICKET DE SALIDA")
    t._texto(slide, t._MX, 0.72, t._ANCHO_UTIL, 0.70,
             "📝  Ahora sí: al Colab", tamano=34, color="menta", negrita=True)
    t._rect(slide, t._MX, 1.65, t._ANCHO_UTIL, 1.60, t._C["terminal_bg"])
    t._rect(slide, t._MX, 1.65, t._ANCHO_UTIL, 0.10, t._C["menta"])
    t._texto(slide, t._MX, 1.95, t._ANCHO_UTIL, 1.2,
             'respuestas = ["B", "D", "A", "C"]\ncheck_ticket(respuestas)',
             tamano=28, color="codigo_color", fuente="Consolas", alineacion=PP_ALIGN.CENTER)
    alto = 3.00
    t._rect(slide, t._MX, 3.55, t._ANCHO_UTIL, alto, t._C["fondo_bloque"])
    t._rect(slide, t._MX, 3.55, 0.08, alto, t._C["menta"])
    t._texto(slide, t._MX + 0.28, 3.69, t._ANCHO_UTIL - 0.5, 0.42,
             f"{t._E['idea']}  Qué hacer", tamano=t._T["titulo_bloque"],
             color="menta", negrita=True)
    t._texto_rico(slide, t._MX + 0.28, 4.23, t._ANCHO_UTIL - 0.6, 2.2, [
        "Reemplaza las letras de ejemplo por **las que anotaste** (una por pregunta).",
        "Ejecuta la celda: verás ✅ o ⚠️ con una pista, sin que te muestre la respuesta.",
        "Si te sale ⚠️, piénsalo de nuevo y cámbiala. Cuando estén todos, revisamos juntos.",
    ], tamano=22, interlineado=1.05)


def main():
    datos = construir_datos()
    prs = Presentation()
    prs.slide_width = Inches(t._W)
    prs.slide_height = Inches(t._H)
    slide_portada(prs, datos)
    for i in range(len(datos["preguntas"])):
        t.slide_pregunta(prs, datos, i)
    slide_colab(prs, datos)
    for i in range(len(datos["preguntas"])):
        t.slide_revision(prs, datos, i)
    prs.save(str(SALIDA))
    print("OK", SALIDA.name, len(prs.slides), "slides")


if __name__ == "__main__":
    main()
