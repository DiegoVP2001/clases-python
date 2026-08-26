"""
Genera "Clase 17.5 - Evaluacion Condicionales - Temario de Evaluacion.pdf"
a partir del temario aprobado (Clase 17.5 - Evaluacion Condicionales - Temario.md).

Fuente de verdad: los datos de este script (bloques, conocimiento previo).
Para editar el contenido, modifica los diccionarios de abajo y vuelve a
correr el script -- no edites el PDF a mano.
"""

from fpdf import FPDF
from fpdf.fonts import TextStyle

# ---------------------------------------------------------------------------
# Paleta de colores
# ---------------------------------------------------------------------------
PRIMARY_DARK = (35, 46, 96)        # banda superior + banner de portada
BLOCK_COLORS = [
    (47, 98, 181),    # azul
    (109, 76, 178),   # morado
    (23, 138, 122),   # verde azulado
]
CODE_COLOR = (122, 31, 162)        # morado para codigo inline
TEXT_COLOR = (34, 34, 34)
ERROR_COLOR = (179, 38, 30)        # rojo para "Errores tipicos"
HIGHLIGHT_COLOR = (196, 130, 0)    # ambar para cajas de conocimiento previo / formato
WHITE = (255, 255, 255)
GRAY_TEXT = (110, 110, 110)


def tint(color, factor=0.75):
    """Mezcla un color con blanco (factor=1 -> blanco puro)."""
    r, g, b = color
    return (
        round(r + (255 - r) * factor),
        round(g + (255 - g) * factor),
        round(b + (255 - b) * factor),
    )


# ---------------------------------------------------------------------------
# Contenido (fuente de verdad)
# ---------------------------------------------------------------------------
META = {
    "titulo": "Evaluación de Condicionales",
    "subtitulo": "Temario de evaluación",
    "fecha": "Martes 21 de julio, 2026",
    "modalidad": "Individual",
    "oas": "OA1, OA3 | OAd",
}

CONOCIMIENTO_PREVIO = {
    "titulo": "Antes de empezar, ya deberías manejar",
    "items": [
        'Tipos de dato: <code>bool</code>, <code>int</code>, <code>float</code>, <code>str</code>',
        'Captura de datos con <code>input()</code>, convertido con <code>int()</code> o <code>float()</code> según corresponda',
    ],
}

BLOQUES = [
    {
        "titulo": "Booleanos y comparaciones",
        "items": [
            'El tipo <code>bool</code>: <code>True</code> / <code>False</code> como valores de dato',
            'Operadores de comparación: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>',
            'Las comparaciones funcionan tanto con números como con texto (ej: <code>dia == "sabado"</code>)',
            'La función <code>bool()</code> para convertir números a booleano',
        ],
        "errores": 'Usar <code>=</code> en vez de <code>==</code> para comparar.',
    },
    {
        "titulo": "Operadores lógicos",
        "items": [
            '<code>and</code>: verdadero solo si <b>ambas</b> condiciones son verdaderas',
            '<code>or</code>: verdadero si <b>al menos una</b> condición es verdadera',
            '<code>not</code>: invierte el valor booleano',
            'Combinar operadores con paréntesis, en distintos órdenes: <code>var and (var2 or var3)</code>, <code>(var and var2) or var3</code>, <code>not (var) and (var2 and var3)</code>',
        ],
        "errores": "Confundir <code>and</code>/<code>or</code>, mayúsculas, alcance de <code>not</code> sin paréntesis.",
    },
    {
        "titulo": "Análisis de condiciones",
        "items": [
            '"Funciona con mis datos de prueba" no es lo mismo que "funciona siempre"',
            'El <b>caso límite</b>: el valor exacto donde <code>&gt;</code>/<code>&gt;=</code> (o <code>&lt;</code>/<code>&lt;=</code>) dan resultados distintos',
            "Identificar y corregir el operador incorrecto en una condición dada",
        ],
        "errores": None,
    },
    {
        "titulo": "if / else",
        "items": [
            'Sintaxis de <code>if</code> y cláusula <code>else</code>',
            "La indentación como sintaxis obligatoria",
        ],
        "errores": 'Falta de <code>:</code>, falta de indentación, <code>else</code> sin <code>if</code>.',
    },
    {
        "titulo": "if anidados",
        "items": [
            'Un <code>if</code> dentro de otro <code>if</code>; la condición interior solo se evalúa si la exterior fue <code>True</code>',
            '<code>else</code> en cada nivel de anidamiento',
            "La sangría como jerarquía",
            'Criterio: ¿cuándo anidar vs. cuándo basta con <code>and</code>?',
        ],
        "errores": None,
    },
    {
        "titulo": "elif",
        "items": [
            'Sintaxis de <code>elif</code>: condiciones alternativas mutuamente excluyentes',
            'Solo se ejecuta <b>una</b> rama -- la primera que resulte <code>True</code>',
            "El orden de las condiciones importa (de más específica a más general)",
        ],
        "errores": 'Condición demasiado amplia primero, <code>elif</code> después de <code>else</code>, olvidar el <code>else</code> final.',
    },
    {
        "titulo": "Criterio de selección",
        "items": [
            'Reconocer cuál estructura usar: <code>if</code>/<code>else</code> simple, anidados, <code>elif</code>, o combinaciones',
            'Combinar estructuras (ej: <code>elif</code> con un <code>if</code>/<code>else</code> anidado dentro de una rama)',
        ],
        "errores": None,
    },
]

TAG_STYLES = {
    "code": TextStyle(font_family="courier", color=CODE_COLOR, font_size_pt=10),
    "li": TextStyle(color=TEXT_COLOR, font_size_pt=11, t_margin=1, b_margin=1),
    "p": TextStyle(color=TEXT_COLOR, font_size_pt=11, t_margin=1, b_margin=1),
}


class GuiaPDF(FPDF):
    def header(self):
        self.set_fill_color(*PRIMARY_DARK)
        self.rect(0, 0, self.w, 12, "F")
        self.set_font("helvetica", "B", 9)
        self.set_text_color(*WHITE)
        self.set_xy(0, 3.2)
        self.cell(
            self.w, 6,
            "TEMARIO DE EVALUACIÓN - CONDICIONALES",
            align="C",
        )
        self.set_y(18)

    def footer(self):
        self.set_y(-13)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(*GRAY_TEXT)
        self.cell(0, 8, f"Página {self.page_no()}", align="C")


def draw_pill(pdf, x, y, text, fill, text_color):
    pdf.set_font("helvetica", "B", 9.5)
    w = pdf.get_string_width(text) + 8
    pdf.set_fill_color(*fill)
    pdf.rect(x, y, w, 7.5, "F", round_corners=True, corner_radius=1.6)
    pdf.set_text_color(*text_color)
    pdf.set_xy(x, y + 1.1)
    pdf.cell(w, 5.3, text, align="C")
    return w


def draw_hero_banner(pdf):
    y0 = pdf.get_y()
    banner_h = 34
    pdf.set_fill_color(*PRIMARY_DARK)
    pdf.rect(0, y0, pdf.w, banner_h, "F")

    pdf.set_font("helvetica", "B", 22)
    pdf.set_text_color(*WHITE)
    pdf.set_xy(0, y0 + 8)
    pdf.cell(pdf.w, 10, META["titulo"], align="C")

    pdf.set_font("helvetica", "", 13)
    pdf.set_xy(0, y0 + 19)
    pdf.cell(pdf.w, 7, META["subtitulo"], align="C")

    pdf.set_y(y0 + banner_h + 6)

    # Metadata pills, centradas
    pills = [
        ("Fecha: " + META["fecha"], tint(PRIMARY_DARK, 0.85), PRIMARY_DARK),
        ("Modalidad: " + META["modalidad"], tint(PRIMARY_DARK, 0.85), PRIMARY_DARK),
        ("OAs: " + META["oas"], tint(PRIMARY_DARK, 0.85), PRIMARY_DARK),
    ]
    pdf.set_font("helvetica", "B", 9.5)
    widths = [pdf.get_string_width(t) + 8 for t, _, _ in pills]
    gap = 4
    total_w = sum(widths) + gap * (len(widths) - 1)
    x = (pdf.w - total_w) / 2
    y = pdf.get_y()
    for (text, fill, tc), w in zip(pills, widths):
        draw_pill(pdf, x, y, text, fill, tc)
        x += w + gap
    pdf.set_y(y + 7.5 + 8)


def draw_left_strip(pdf, x, y_start, y_end, color, width=1.3):
    if y_end - y_start < 1:
        return
    pdf.set_fill_color(*color)
    pdf.rect(x, y_start, width, y_end - y_start, "F")


def check_space(pdf, min_h):
    if pdf.get_y() + min_h > pdf.page_break_trigger:
        pdf.add_page()


def draw_callout(pdf, titulo, items, accent):
    check_space(pdf, 30)
    pdf.set_font("helvetica", "B", 12.5)
    pdf.set_text_color(*accent)
    pdf.set_x(pdf.l_margin + 5)
    pdf.cell(0, 8, titulo, new_x="LMARGIN", new_y="NEXT")

    y_start = pdf.get_y()
    pdf.set_x(pdf.l_margin + 5)
    pdf.set_text_color(*TEXT_COLOR)
    html = "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
    pdf.write_html(
        html,
        tag_styles=TAG_STYLES,
        li_prefix_color=accent,
        ul_bullet_char="disc",
    )
    y_end = pdf.get_y()
    draw_left_strip(pdf, pdf.l_margin, y_start - 1, y_end, tint(accent, 0.35))
    pdf.ln(6)


def draw_bloque(pdf, numero, bloque, accent):
    check_space(pdf, 34)

    bar_h = 9
    y0 = pdf.get_y()
    pdf.set_fill_color(*accent)
    pdf.rect(pdf.l_margin, y0, pdf.w - pdf.l_margin - pdf.r_margin, bar_h,
              "F", round_corners=True, corner_radius=1.5)
    pdf.set_font("helvetica", "B", 12.5)
    pdf.set_text_color(*WHITE)
    pdf.set_xy(pdf.l_margin + 4, y0 + 1.4)
    pdf.cell(0, 6.2, f"Bloque {numero} -- {bloque['titulo']}")
    pdf.set_y(y0 + bar_h + 3)

    body_y0 = pdf.get_y()
    pdf.set_x(pdf.l_margin + 5)
    pdf.set_text_color(*TEXT_COLOR)
    html = "<ul>" + "".join(f"<li>{item}</li>" for item in bloque["items"]) + "</ul>"
    pdf.write_html(html, tag_styles=TAG_STYLES, li_prefix_color=accent, ul_bullet_char="disc")

    if bloque.get("errores"):
        pdf.set_x(pdf.l_margin + 5)
        pdf.set_text_color(*TEXT_COLOR)
        error_html = (
            f'<p><font color="#{ERROR_COLOR[0]:02X}{ERROR_COLOR[1]:02X}{ERROR_COLOR[2]:02X}">'
            f"<b>Error típico:</b></font> {bloque['errores']}</p>"
        )
        pdf.write_html(error_html, tag_styles=TAG_STYLES)

    body_y1 = pdf.get_y()
    draw_left_strip(pdf, pdf.l_margin, body_y0, body_y1, tint(accent, 0.35))
    pdf.ln(6)


def build_pdf(output_path):
    pdf = GuiaPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(left=18, top=15, right=18)
    pdf.set_title(META["titulo"] + " - " + META["subtitulo"])
    pdf.add_page()

    draw_hero_banner(pdf)
    draw_callout(pdf, CONOCIMIENTO_PREVIO["titulo"], CONOCIMIENTO_PREVIO["items"], HIGHLIGHT_COLOR)

    for i, bloque in enumerate(BLOQUES, start=1):
        accent = BLOCK_COLORS[(i - 1) % len(BLOCK_COLORS)]
        draw_bloque(pdf, i, bloque, accent)

    check_space(pdf, 16)
    pdf.set_font("helvetica", "I", 10.5)
    pdf.set_text_color(*GRAY_TEXT)
    pdf.set_x(pdf.l_margin)
    pdf.cell(pdf.w - pdf.l_margin - pdf.r_margin, 8, "Éxito en tu evaluación :)", align="C")

    pdf.output(output_path)


if __name__ == "__main__":
    build_pdf("Clase 17.5 - Evaluación Condicionales - Temario de Evaluación.pdf")
    print("PDF generado.")
