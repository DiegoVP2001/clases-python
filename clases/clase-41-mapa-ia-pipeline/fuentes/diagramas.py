"""Builds the projectable diagrams of Clase 41 as standalone SVG strings.

Used by construir.py (inlines them in the interactive HTML and exports PNGs) and by
diapositivas.py (step-by-step slides). Edit the texts here, never the generated files.
"""
from xml.sax.saxutils import escape

FONT = "'Segoe UI', Roboto, Arial, sans-serif"
INK = "#0f172a"
SLATE = "#334155"
AZUL, AZUL_BG = "#1d4ed8", "#dbeafe"
TEAL, TEAL_BG = "#0f766e", "#ccfbf1"
MORADO, MORADO_BG = "#6d28d9", "#ede9fe"
NARANJA, NARANJA_BG = "#c2410c", "#ffedd5"


def text(x, y, content, size=30, weight="normal", anchor="start", fill=INK):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{escape(content)}</text>')


def lines(x, y, rows, size=30, step=40, weight="normal", anchor="start", fill=INK):
    return "".join(text(x, y + i * step, row, size, weight, anchor, fill) for i, row in enumerate(rows))


def box(x, y, w, h, fill, stroke, dashed=False, radius=22, sw=4):
    dash = ' stroke-dasharray="14 10"' if dashed else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{dash}/>')


def flecha(x1, y1, x2, y2, color=INK, grosor=5):
    """Straight arrow (horizontal or vertical) with a triangular head at (x2, y2)."""
    if x1 == x2:  # vertical
        s = 1 if y2 > y1 else -1
        cabeza = f"{x2 - 11},{y2 - 16 * s} {x2 + 11},{y2 - 16 * s} {x2},{y2}"
    else:
        s = 1 if x2 > x1 else -1
        cabeza = f"{x2 - 16 * s},{y2 - 11} {x2 - 16 * s},{y2 + 11} {x2},{y2}"
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - (16 if x1 != x2 else 0) * (1 if x2 > x1 else -1)}" '
            f'y2="{y2 - (16 if x1 == x2 else 0) * (1 if y2 > y1 else -1)}" stroke="{color}" stroke-width="{grosor}"/>'
            f'<polygon points="{cabeza}" fill="{color}"/>')


def wrap_svg(body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" role="img" '
            f'aria-labelledby="t d" width="1920" height="1080">'
            f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
            f'<rect width="1920" height="1080" fill="#f8fafc"/>{body}</svg>')


# ───────────────────────── Diagrama 1 · El mapa de la IA ─────────────────────────
def diagrama_mapa():
    b = [text(60, 82, "El mapa de la IA", 54, "bold")]
    b.append('<circle cx="470" cy="470" r="350" fill="#dbeafe" stroke="#1d4ed8" stroke-width="5"/>')
    b.append('<circle cx="470" cy="565" r="240" fill="#ccfbf1" stroke="#0f766e" stroke-width="5"/>')
    b.append('<circle cx="470" cy="640" r="130" fill="#ede9fe" stroke="#6d28d9" stroke-width="5"/>')
    b.append(text(470, 195, "IA", 52, "bold", "middle", "#1e3a8a"))
    b.append(text(470, 455, "Machine Learning (ML)", 32, "bold", "middle", "#115e59"))
    b.append(text(470, 632, "Deep Learning", 30, "bold", "middle", "#4c1d95"))
    b.append(text(470, 670, "(DL)", 30, "bold", "middle", "#4c1d95"))
    b.append('<path d="M692 200 L900 185" stroke="#1d4ed8" stroke-width="4" fill="none"/>')
    b.append('<path d="M644 400 L900 365" stroke="#0f766e" stroke-width="4" fill="none"/>')
    b.append('<path d="M600 640 L900 545" stroke="#6d28d9" stroke-width="4" fill="none"/>')
    b.append('<path d="M585 700 L900 745" stroke="#c2410c" stroke-width="4" stroke-dasharray="14 10" fill="none"/>')
    b.append(box(900, 110, 960, 150, "#eff6ff", "#1d4ed8"))
    b.append(text(930, 160, "IA · Inteligencia artificial", 34, "bold", fill="#1e3a8a"))
    b.append(lines(930, 205, ["Máquinas que hacen tareas que normalmente requieren",
                              "inteligencia humana: aprender, razonar y decidir."], 30, 40))
    b.append(box(900, 290, 960, 150, "#f0fdfa", "#0f766e"))
    b.append(text(930, 340, "ML · Machine Learning", 34, "bold", fill="#115e59"))
    b.append(lines(930, 385, ["La computadora descubre patrones en los datos",
                              "y decide sin que le indiquen cómo."], 30, 40))
    b.append(box(900, 470, 960, 150, "#f5f3ff", "#6d28d9"))
    b.append(text(930, 520, "DL · Deep Learning", 34, "bold", fill="#4c1d95"))
    b.append(lines(930, 565, ["ML con redes neuronales de muchas capas;",
                              "sirve para imágenes, voz y texto."], 30, 40))
    b.append(box(900, 650, 960, 190, "#fff7ed", "#c2410c", dashed=True))
    b.append(text(930, 700, "IA generativa · se define por lo que produce", 34, "bold", fill="#9a3412"))
    b.append(lines(930, 745, ["Produce contenido nuevo (texto, imágenes, música) a",
                              "partir de lo que aprendió. Hoy se construye sobre todo",
                              "con DL (por ejemplo, ChatGPT)."], 30, 38))
    b.append(box(60, 880, 870, 160, "#ffffff", SLATE))
    b.append(text(90, 932, "REGLA", 36, "bold", fill=SLATE))
    b.append(lines(90, 980, ["Instrucción que escribe una persona y que le dice",
                             "a la máquina qué hacer en cada caso. No cambia sola."], 30, 40))
    b.append(box(990, 880, 870, 160, "#ffffff", SLATE))
    b.append(text(1020, 932, "PATRÓN", 36, "bold", fill=SLATE))
    b.append(lines(1020, 980, ["Algo que se repite en los datos y que la máquina",
                               "descubre sola, mirando muchos ejemplos."], 30, 40))
    return wrap_svg("".join(b), "El mapa de la IA",
                    "Tres círculos anidados: IA contiene a Machine Learning y este a Deep Learning. "
                    "La IA generativa se define por lo que produce. Abajo, las definiciones de regla y patrón.")


# ───────────────────── Piezas del pipeline (compartidas con las diapositivas) ─────────────────────
BANDAS = [("PREPARAR", 0, 2, AZUL_BG, AZUL), ("ENTRENAR", 3, 3, TEAL_BG, TEAL),
          ("EVALUAR", 4, 5, MORADO_BG, MORADO), ("USAR", 6, 6, NARANJA_BG, NARANJA)]
PASOS = [["Definir el", "problema"], ["Reunir datos:", "variables y", "etiqueta"],
         ["Separar en dos", "sets de datos"], ["Entrenar", "el modelo"],
         ["Predecir sobre", "el set de", "prueba"], ["Evaluar:", "¿cuántas", "acertó?"],
         ["Usar en casos", "nuevos y", "revisar"]]
COLORES = [AZUL, AZUL, AZUL, TEAL, MORADO, MORADO, NARANJA]


def tira(activo=None, y_banda=165, y_card=228, alto=200):
    """The 7-step strip. With `activo`, every other step is faded so the current one stands out."""
    b = []
    for nombre, a, z, fill, stroke in BANDAS:
        x0, x1 = 95 + a * 250, 95 + z * 250 + 230
        op = 1 if activo is None or a <= activo <= z else 0.3
        b.append(f'<g opacity="{op}">' + box(x0, y_banda, x1 - x0, 50, fill, stroke, radius=14)
                 + text((x0 + x1) // 2, y_banda + 36, nombre, 28, "bold", "middle") + "</g>")
    for i, titulo in enumerate(PASOS):
        x = 95 + i * 250
        on = activo is None or i == activo
        g = [box(x, y_card, 230, alto, "#ffffff", COLORES[i], sw=9 if activo == i else 4),
             f'<circle cx="{x + 42}" cy="{y_card + 46}" r="26" fill="{COLORES[i]}"/>',
             text(x + 42, y_card + 56, str(i + 1), 30, "bold", "middle", "#ffffff"),
             lines(x + 18, y_card + 120, titulo, 26, 33, "bold")]
        b.append(f'<g opacity="{1 if on else 0.3}">' + "".join(g) + "</g>")
        if i < 6:
            b.append(f'<g opacity="{1 if activo is None or activo in (i, i + 1) else 0.3}">'
                     + flecha(x + 233, y_card + alto // 2, x + 248, y_card + alto // 2) + "</g>")
    return b


def tabla(x, y, anchos, cab, filas, idx_etq=3, oculta_etq=False, alto=40, size=21):
    """Mini data table; the label column is orange and can hide its values with '?'."""
    b, cx = [], x
    for j, w in enumerate(anchos):
        col = NARANJA if j == idx_etq else AZUL
        b.append(box(cx, y, w - 8, alto, NARANJA_BG if j == idx_etq else AZUL_BG, col, radius=6, sw=3))
        b.append(text(cx + (w - 8) // 2, y + alto - 11, cab[j], size - 1, "bold", "middle"))
        for r, fila in enumerate(filas):
            yy = y + (r + 1) * (alto + 6)
            b.append(box(cx, yy, w - 8, alto, "#ffffff", col, radius=6, sw=3))
            val = "?" if (oculta_etq and j == idx_etq) else fila[j]
            b.append(text(cx + (w - 8) // 2, yy + alto - 11, val, size + 1, "bold", "middle"))
        cx += w
    return b


CAB_RIEGO = ["Humedad", "Temperatura", "Días sin lluvia", "¿Se regó?"]
ANCHOS = [150, 150, 170, 170]


def bloque_entrenamiento(x=95, y=570, w=700, h=335, titulo_fila="SET DE ENTRENAMIENTO · 48 filas"):
    b = [box(x, y, w, h, TEAL_BG if False else "#f0fdfa", TEAL),
         text(x + 30, y + 44, titulo_fila, 30, "bold", fill="#115e59"),
         box(x + 20, y + 58, w - 40, 52, TEAL, TEAL, radius=12),
         text(x + w // 2, y + 94, "AQUÍ LA COMPUTADORA APRENDE", 28, "bold", "middle", "#ffffff")]
    b += tabla(x + 30, y + 132, ANCHOS, CAB_RIEGO, [["32 %", "27 °C", "5", "Sí"], ["58 %", "19 °C", "1", "No"]])
    b.append(text(x + 30, y + 310, "Ve las variables Y la etiqueta (la respuesta)", 24, fill="#115e59"))
    return b


def bloque_prueba(x=1125, y=570, w=700, h=335, titulo_fila="SET DE PRUEBA · 12 filas"):
    b = [box(x, y, w, h, "#f5f3ff", MORADO),
         text(x + 30, y + 44, titulo_fila, 30, "bold", fill="#4c1d95"),
         box(x + 20, y + 58, w - 40, 52, MORADO, MORADO, radius=12),
         text(x + w // 2, y + 94, "AQUÍ VEMOS SI ES CAPAZ DE PREDECIR", 26, "bold", "middle", "#ffffff")]
    b += tabla(x + 30, y + 132, ANCHOS, CAB_RIEGO, [["41 %", "24 °C", "3", "?"], ["22 %", "30 °C", "8", "?"]],
               oculta_etq=True)
    b.append(text(x + 30, y + 310, "Se guarda aparte: el modelo no lo ve al entrenar", 24, fill="#4c1d95"))
    return b


def bloque_modelo(x=835, y=655, w=250, h=170):
    return [box(x, y, w, h, "#fffbeb", "#b45309"),
            text(x + w // 2, y + 80, "MODELO", 34, "bold", "middle"),
            text(x + w // 2, y + 120, "(ya entrenado)", 24, anchor="middle", fill=SLATE)]


# ───────────────────────── Diagrama 2 · El pipeline ─────────────────────────
def diagrama_pipeline():
    b = [text(60, 82, "El recorrido de los datos: el pipeline", 54, "bold"),
         text(60, 128, "Caso: ¿hay que regar mañana? Riego automatizado de una viña de Isla de Maipo, "
                       "como Santa Ema (datos ficticios)", 28, fill=SLATE)]
    b += tira()
    # One data set, split in two: where the computer learns and where we test it
    b.append(box(95, 462, 1730, 54, "#e2e8f0", SLATE, radius=12))
    b.append(text(960, 498, "SET DE DATOS · 60 filas (una fila = un día de riego)", 28, "bold", "middle"))
    b.append(flecha(445, 518, 445, 566, TEAL))
    b.append(flecha(1475, 518, 1475, 566, MORADO))
    b.append(text(470, 552, "la mayoría → para entrenar", 22, fill="#115e59"))
    b.append(text(1500, 552, "una parte → para probar", 22, fill="#4c1d95"))
    b += bloque_entrenamiento() + bloque_modelo() + bloque_prueba()
    b.append(flecha(797, 740, 833, 740, TEAL))
    b.append(flecha(1087, 740, 1123, 740, MORADO))
    b.append(box(95, 935, 1730, 100, NARANJA_BG, NARANJA))
    b.append(text(960, 982, "EVALUAR: comparamos lo que predijo con lo que realmente pasó", 31, "bold", "middle"))
    b.append(text(960, 1019, "→ ¿cuántas veces acertó?", 27, anchor="middle", fill="#9a3412"))
    return wrap_svg("".join(b), "El recorrido de los datos: el pipeline",
                    "Siete pasos agrupados en preparar, entrenar, evaluar y usar. Un set de datos se separa en set de "
                    "entrenamiento, donde la computadora aprende, y set de prueba, donde vemos si es capaz de predecir.")
