"""Genera 'Charla Electivo Computación.pptx' — estilo arcade nocturno / pixel art.

Fuente de verdad de la charla: editar este script y regenerar (no editar el .pptx a mano).
Uso:  python generar_charla.py
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

AQUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(AQUI, "assets")
GEN = os.path.join(ASSETS, "gen")
FUENTE = os.path.join(ASSETS, "PressStart2P-Regular.ttf")
SALIDA = os.path.join(AQUI, "Charla Electivo Computación.pptx")
os.makedirs(GEN, exist_ok=True)

W, H = 1920, 1080  # px de diseño; 1 px = 1/144 in  (slide 13.333 x 7.5 in)

# ── Paleta ────────────────────────────────────────────────────────────
BG = (11, 16, 38)
CIAN = (34, 229, 255)
MAGENTA = (255, 62, 165)
AMARILLO = (255, 225, 77)
VERDE = (61, 255, 138)
ROJO = (255, 70, 90)
BLANCO = (245, 247, 255)
GRIS = (130, 140, 175)
OSCURO = (24, 30, 66)

PAL = {
    "k": (15, 15, 35), "s": (255, 205, 160), "h": (90, 50, 30), "r": (255, 62, 165),
    "w": (255, 255, 255), "b": (34, 229, 255), "y": (255, 225, 77), "o": (255, 150, 40),
    "g": (61, 255, 138), "d": (60, 70, 110), "m": (160, 170, 200), "e": (230, 40, 70),
    "n": (40, 60, 170), "c": (34, 229, 255), "p": (180, 80, 255), "f": (20, 90, 60),
}

SPRITES = {
    "corredor": [
        "...hhhhhh...", "..hhhhhhhh..", "..hssssssh..", "..ssskssks..", "..ssssssss..",
        "...ssssss...", "....ssss....", "..rrrrrrrr..", ".ssrwwwwrss.", ".ss.rwwr.ss.",
        ".ss.rwwr.ss.", "....rrrr....", "...bbbbbb...", "..bbb..bbb..", "..ss....ss..",
        ".kkk....kkk.",
    ],
    "trofeo": [
        ".yyyyyyyyyy.", "yy.yyyyyy.yy", "y..yyyyyy..y", "yy.yyyyyy.yy", ".yyyyyyyyyy.",
        "..yyyyyyyy..", "....yyyy....", ".....yy.....", ".....yy.....", "....yyyy....",
        "...oooooo...", "...oooooo...",
    ],
    "medalla": [
        "...rr..bb...", "...rr..bb...", "....rrbb....", "....rrbb....", "...yyyyyy...",
        "..yyyooyyy..", "..yyoyyoyy..", "..yyoyyoyy..", "..yyyooyyy..", "...yyyyyy...",
    ],
    "libro": [
        "nnnnnnnnnnnn", "nccccnnccccn", "ncwwcnncwwcn", "nccccnnccccn", "ncwwcnncwwcn",
        "nccccnnccccn", "ncwwcnncwwcn", "nccccnnccccn", "nnnnnnnnnnnn", "..kkkkkkkk..",
    ],
    "birrete": [
        ".......nn.......", ".....nnnnnn.....", "...nnnnnnnnnn...", ".nnnnnnnccnnnnn.",
        "...nnnnnnnnnn..y", ".....dddddd...y.", "....dddddddd..yy", "....dddddddd..yy",
    ],
    "pizarron": [
        "kkkkkkkkkkkkkk", "kffffffffffffk", "kfwwwfwwfffffk", "kffffffffffffk",
        "kfwwwwwfwwwffk", "kffffffffffffk", "kkkkkkkkkkkkkk", "..k........k..",
        "..k........k..", ".kk........kk.",
    ],
    "robot": [
        ".....yy.....", ".....kk.....", "..mmmmmmmm..", ".mmccmmccmm.", ".mmccmmccmm.",
        ".mmmmmmmmmm.", ".mmkkkkkkmm.", "..mmmmmmmm..", "mmmmmmmmmmmm", "mmmrrmmrrmmm",
        "mm.mmmmmm.mm", "...mm..mm...", "..kkk..kkk..",
    ],
    "auto": [
        ".....rrrrr....", "....rrwwwrr...", "..rrrrrrrrrrr.", ".rrrrrrrrrrrrr",
        ".rrkkrrrrkkrrr", "..kkkk..kkkk..",
    ],
    "moneda": [
        "...oooo...", "..oyyyyo..", ".oyyooyyo.", "oyyyooyyyo", "oyyyooyyyo",
        "oyyyooyyyo", "oyyyooyyyo", ".oyyooyyo.", "..oyyyyo..", "...oooo...",
    ],
    "corazon": [
        ".eee.eee.", "eeeeeeeee", "eeeeeeeee", ".eeeeeee.", "..eeeee..", "...eee...", "....e....",
    ],
    "bloques": [
        "...yy..yy...", "..yyyyyyyy..", "..yyyyyyyy..", ".rr..rr..rr.", ".rrrrrrrrrr.",
        ".rrrrrrrrrr.", "bb..bb..bb..", "bbbbbbbbbbbb", "bbbbbbbbbbbb",
    ],
    "grafico": [
        "............", "........gg..", "........gg..", "....yy..gg..", "....yy..gg..",
        "rr..yy..gg..", "rr..yy..gg..", "rr..yy..gg..", "kkkkkkkkkkkk", "............",
    ],
    "terminal": [
        "mmmmmmmmmmmm", "mkkkkkkkkkkm", "mkgkkkkkkkkm", "mkkgkkkkkkkm", "mkgkkkkkkkkm",
        "mkkkkgggkkkm", "mkkkkkkkkkkm", "mkkkkkkkkkkm", "mmmmmmmmmmmm", "..mmmmmmmm..",
    ],
}


TILDES = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}


def sprite(nombre, escala):
    filas = SPRITES[nombre]
    ancho = len(filas[0])
    assert all(len(f) == ancho for f in filas), f"sprite {nombre}: filas de distinto ancho"
    img = Image.new("RGBA", (ancho, len(filas)), (0, 0, 0, 0))
    for y, fila in enumerate(filas):
        for x, ch in enumerate(fila):
            if ch != ".":
                img.putpixel((x, y), PAL[ch] + (255,))
    img = img.resize((ancho * escala, len(filas) * escala), Image.NEAREST)
    ruta = os.path.join(GEN, f"spr_{nombre}_{escala}.png")
    img.save(ruta)
    return ruta, img.size


def texto_pixel(lineas, tam, colores, nombre, sombra=MAGENTA, interlinea=1.7, alinear="center"):
    """Renderiza texto con Press Start 2P como PNG (se ve igual en cualquier PC)."""
    if isinstance(lineas, str):
        lineas = [lineas]
    if not isinstance(colores, (list, tuple)) or isinstance(colores[0], int):
        colores = [colores] * len(lineas)
    fuente = ImageFont.truetype(FUENTE, tam)
    u = tam / 8  # un "pixel" de la fuente
    pad = int(4 * u)  # espacio arriba para las tildes
    ancho = int(max(len(l) for l in lineas) * tam) + 12
    paso = int(tam * interlinea)
    alto = paso * len(lineas) + 12 + pad
    tope = fuente.getbbox("A")[1]  # y donde empieza una mayúscula
    img = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def dibujar(linea, x, y, color):
        for k, ch in enumerate(linea):
            base = TILDES.get(ch, ch)
            cx = x + k * tam
            d.text((cx, y), base, font=fuente, fill=color + (255,))
            if ch in TILDES:  # la fuente no trae tildes en mayúscula: se dibujan a mano
                for dx, dy in ((3, -1), (4, -2), (5, -3)):
                    px0 = cx + dx * u
                    py0 = y + tope + dy * u
                    d.rectangle([px0, py0, px0 + u - 1, py0 + u - 1], fill=color + (255,))

    for i, linea in enumerate(lineas):
        w = len(linea) * tam
        x = {"center": (ancho - w) // 2, "left": 0, "right": ancho - w}[alinear]
        y = pad + i * paso
        off = max(2, tam // 12)
        if sombra:
            dibujar(linea, x + off, y + off, sombra)
        dibujar(linea, x, y, colores[i])
    ruta = os.path.join(GEN, f"txt_{nombre}.png")
    img.save(ruta)
    return ruta, img.size


def fondo(nivel, nombre):
    rnd = random.Random(7 + nivel)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for _ in range(170):  # estrellas
        x, y = rnd.randrange(0, W, 8), rnd.randrange(90, H - 140, 8)
        c = rnd.choice([(70, 80, 130), (120, 130, 190), CIAN, (200, 210, 255)])
        t = rnd.choice([4, 4, 8])
        d.rectangle([x, y, x + t - 1, y + t - 1], fill=c)
    # piso con grilla
    d.rectangle([0, H - 120, W, H], fill=(20, 18, 56))
    d.rectangle([0, H - 120, W, H - 112], fill=MAGENTA)
    for x in range(0, W, 96):
        d.line([(x, H - 112), (x - 120 + (x // 8 % 2) * 0, H)], fill=(60, 40, 120), width=4)
    for y in range(H - 80, H, 32):
        d.line([(0, y), (W, y)], fill=(60, 40, 120), width=4)
    # HUD superior
    d.rectangle([0, 0, W, 80], fill=(7, 10, 26))
    d.rectangle([0, 76, W, 84], fill=CIAN)
    f = ImageFont.truetype(FUENTE, 24)
    d.text((40, 26), "1UP", font=f, fill=AMARILLO)
    d.text((150, 26), "003600", font=f, fill=BLANCO)
    d.text((W // 2 - 130, 26), f"NIVEL {nivel}/8", font=f, fill=CIAN)
    d.text((W - 560, 26), "HI-SCORE 999999", font=f, fill=MAGENTA)
    ruta = os.path.join(GEN, f"bg_{nombre}.png")
    img.save(ruta)
    return ruta


# ── python-pptx helpers ───────────────────────────────────────────────
prs = Presentation()
prs.slide_width = Inches(W / 144)
prs.slide_height = Inches(H / 144)
LAYOUT = prs.slide_layouts[6]


def px(v):
    return Inches(v / 144)


def nueva(nivel, nombre, notas):
    s = prs.slides.add_slide(LAYOUT)
    s.shapes.add_picture(fondo(nivel, nombre), 0, 0, prs.slide_width, prs.slide_height)
    s.notes_slide.notes_text_frame.text = notas
    return s


def pic(slide, ruta_tam, x, y, centrar=False):
    ruta, (w, h) = ruta_tam
    if centrar:
        x = (W - w) // 2
    return slide.shapes.add_picture(ruta, px(x), px(y), px(w), px(h))


def texto(slide, x, y, w, h, txt, tam=22, color=BLANCO, negrita=False, alinear=PP_ALIGN.LEFT,
          fuente="Consolas"):
    tb = slide.shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    lineas = txt if isinstance(txt, list) else [txt]
    for i, l in enumerate(lineas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = alinear
        p.space_after = Pt(8)
        r = p.add_run()
        r.text = l
        r.font.name = fuente
        r.font.size = Pt(tam)
        r.font.bold = negrita
        r.font.color.rgb = RGBColor(*color)
    return tb


def caja(slide, x, y, w, h, color, grosor=6, relleno=OSCURO):
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, px(x), px(y), px(w), px(h))
    r.fill.solid()
    r.fill.fore_color.rgb = RGBColor(*relleno)
    r.line.color.rgb = RGBColor(*color)
    r.line.width = Pt(grosor)
    r.shadow.inherit = False
    return r


def suelo(slide, nombres, escala=8, y_base=H - 118):
    """Sprites parados sobre el piso."""
    xs = [150, 520, 900, 1250, 1580]
    for n, x in zip(nombres, xs):
        ruta, (w, h) = sprite(n, escala)
        slide.shapes.add_picture(ruta, px(x), px(y_base - h), px(w), px(h))


# ── Slide 1: PRESS START ──────────────────────────────────────────────
s = nueva(1, "s1", (
    "[0:00-0:20] Saludo breve. 'Buenas, vengo a contarles de un electivo que es distinto a todos.' "
    "No explicar nada todavía: dejar que el título y el tono arcade hagan el trabajo. "
    "Pasar de inmediato a presentarme."))
pic(s, texto_pixel("ELECTIVO DE", 64, BLANCO, "s1a", sombra=(40, 60, 170)), 0, 190, centrar=True)
pic(s, texto_pixel("COMPUTACIÓN", 104, AMARILLO, "s1b"), 0, 310, centrar=True)
pic(s, texto_pixel(">  PRESS START  <", 40, CIAN, "s1c", sombra=(10, 60, 90)), 0, 620, centrar=True)
texto(s, 0, 720, W, 60, "Para 2° y 3° medio  ·  Profe Diego", 24, GRIS, alinear=PP_ALIGN.CENTER)
suelo(s, ["corredor", "robot", "auto", "trofeo", "libro"], escala=9)

# ── Slide 2: PLAYER 1 ─────────────────────────────────────────────────
s = nueva(2, "s2", (
    "[0:20-1:20] Me presento como si fuera un personaje de videojuego. "
    "Soy Diego: me gusta correr y me gusta leer. Tres veces campeón nacional universitario de cross country "
    "y campeón de la Maratón de Temuco 2025 (correr es mi forma de entrenar la disciplina). "
    "Ingeniero UC, y desde el año pasado profesor, por Enseña Chile. "
    "Idea fuerza: lo que más me enseñó correr es que se llega lejos con constancia, y eso es lo que les voy a pedir."))
pic(s, texto_pixel("PLAYER 1", 48, CIAN, "s2a", sombra=(10, 60, 90)), 120, 130)
caja(s, 120, 250, 420, 560, MAGENTA)
pic(s, sprite("corredor", 24), 120 + (420 - 288) // 2, 300)
pic(s, texto_pixel("DIEGO", 40, AMARILLO, "s2b"), 120 + 40, 710)
filas = [
    ("trofeo", "3X CAMPEÓN NACIONAL", "Cross country universitario", AMARILLO),
    ("medalla", "CAMPEÓN MARATÓN", "Maratón de Temuco 2025", CIAN),
    ("libro", "LECTOR", "Me gusta correr y me gusta leer", VERDE),
    ("birrete", "INGENIERO UC", "Pontificia Universidad Católica", MAGENTA),
    ("pizarron", "PROFE", "Por Enseña Chile, desde 2025", AMARILLO),
]
for i, (spr, tit, det, col) in enumerate(filas):
    y = 190 + i * 150
    ruta, (w, h) = sprite(spr, 8)
    s.shapes.add_picture(ruta, px(640 + (112 - w) // 2), px(y + (112 - h) // 2), px(w), px(h))
    pic(s, texto_pixel(tit, 28, col, f"s2f{i}", sombra=None, alinear="left"), 800, y + 6)
    texto(s, 800, y + 62, 1000, 50, det, 22, BLANCO)

# ── Slide 3: LA PREGUNTA ──────────────────────────────────────────────
s = nueva(3, "s3", (
    "[1:20-2:20] PAUSA LARGA. Leer la pregunta en voz alta, sin prisa, y esperar. "
    "'¿Qué sería lo que más les gustaría crear el día de mañana?' "
    "Escuchar 2 o 3 respuestas (una app, un juego, una empresa, algo para ayudar a alguien...). "
    "Repetir lo que dicen con entusiasmo: todo eso se construye con código. "
    "Si nadie responde, tirar un ejemplo propio y volver a preguntar."))
pic(s, texto_pixel(["¿QUÉ SERÍA LO QUE MÁS", "LES GUSTARÍA CREAR"], 64, BLANCO, "s3a",
                   sombra=(40, 60, 170)), 0, 250, centrar=True)
pic(s, texto_pixel("EL DÍA DE MAÑANA?", 80, AMARILLO, "s3b"), 0, 560, centrar=True)
pic(s, sprite("moneda", 10), 150, 780)
pic(s, sprite("moneda", 10), W - 250, 780)
texto(s, 0, 790, W, 60, "(piénsalo un momento... y dilo en voz alta)", 22, GRIS, alinear=PP_ALIGN.CENTER)

# ── Slide 4: PARA QUIÉN ES ────────────────────────────────────────────
s = nueva(4, "s4", (
    "[2:20-3:00] Enganche. 'Este electivo es para quienes quieren cambiar el mundo con creatividad.' "
    "No hace falta ser 'bueno para la computación' ni saber programar: hace falta ganas de crear. "
    "Conectar con lo que dijeron en la slide anterior: eso que imaginaron se construye aquí."))
pic(s, texto_pixel("NIVEL 4: ¿PARA QUIÉN ES?", 32, CIAN, "s4a", sombra=(10, 60, 90)), 0, 150, centrar=True)
pic(s, texto_pixel("PARA QUIENES QUIEREN", 60, BLANCO, "s4b", sombra=(40, 60, 170)), 0, 290, centrar=True)
pic(s, texto_pixel("CAMBIAR EL MUNDO", 84, MAGENTA, "s4c", sombra=(90, 20, 80)), 0, 430, centrar=True)
pic(s, texto_pixel("CON CREATIVIDAD", 84, AMARILLO, "s4d"), 0, 590, centrar=True)
texto(s, 0, 790, W, 60, "Lo que imaginaste hace un momento no se pide: se construye.", 26, BLANCO,
      alinear=PP_ALIGN.CENTER)

# ── Slide 5: EL MAPA ──────────────────────────────────────────────────
s = nueva(5, "s5", (
    "[3:00-3:50] El mapa del juego: cuatro mundos. "
    "Mundo 1, Cimientos: entendemos las definiciones esenciales y partimos programando con bloques tipo LEGO. "
    "Mundo 2, Python: pasamos de los bloques al código y le damos órdenes al computador. "
    "Mundo 3, Datos: hacemos que miles de datos cuenten una historia. "
    "Mundo 4, IA: entrenamos modelos y vemos qué hay detrás (árboles de decisión, neuronas). "
    "No es magia: es matemática y código que ustedes pueden entender y controlar."))
pic(s, texto_pixel("EL MAPA DEL JUEGO", 52, CIAN, "s5a", sombra=(10, 60, 90)), 0, 140, centrar=True)
mundos = [
    ("bloques", "MUNDO 1", "CIMIENTOS", "Definiciones esenciales y primeros pasos con bloques tipo LEGO.", CIAN),
    ("terminal", "MUNDO 2", "PYTHON", "Pasamos de los bloques al código: le das órdenes al computador.", VERDE),
    ("grafico", "MUNDO 3", "DATOS", "Haces que miles de datos te cuenten una historia.", AMARILLO),
    ("robot", "MUNDO 4", "IA", "Entrenas modelos y ves qué hay detrás: árboles y neuronas.", MAGENTA),
]
CW, GAP = 400, 70
X0 = (W - (4 * CW + 3 * GAP)) // 2
for i, (spr, mundo, nombre, desc, col) in enumerate(mundos):
    x = X0 + i * (CW + GAP)
    caja(s, x, 280, CW, 600, col)
    ruta, (w, h) = sprite(spr, 8)
    s.shapes.add_picture(ruta, px(x + (CW - w) // 2), px(320), px(w), px(h))
    ruta1, (w1, h1) = texto_pixel(mundo, 22, col, f"s5m{i}", sombra=None)
    s.shapes.add_picture(ruta1, px(x + (CW - w1) // 2), px(450), px(w1), px(h1))
    ruta2, (w2, h2) = texto_pixel(nombre, 40 if len(nombre) > 6 else 48, BLANCO, f"s5n{i}", sombra=None)
    s.shapes.add_picture(ruta2, px(x + (CW - w2) // 2), px(510), px(w2), px(h2))
    texto(s, x + 22, 620, CW - 44, 250, desc, 19, BLANCO, alinear=PP_ALIGN.CENTER)
    if i < 3:
        pic(s, texto_pixel(">>", 32, col, f"s5a{i}", sombra=None), x + CW + 2, 540)

# ── Slide 6: MODO DIFÍCIL ─────────────────────────────────────────────
s = nueva(6, "s6", (
    "[3:50-4:30] ¿Cómo serán las clases? Les exigiré harto, porque quiero sacar lo mejor de cada uno. "
    "Es la última hora de la jornada, y justo por eso se la vamos a sacar al máximo: "
    "no es una hora para 'pasar el rato', es para construir cosas. "
    "A cambio, salen entendiendo cómo funciona la IA, no solo usándola. "
    "Si corro maratones, sé que lo difícil es lo que más se disfruta al final."))
pic(s, texto_pixel("¿CÓMO SERÁN LAS CLASES?", 64, AMARILLO, "s6a"), 0, 150, centrar=True)
texto(s, 260, 290, 1400, 200, "Les exigiré harto porque quiero sacar lo mejor de cada uno.", 36, BLANCO, True)
texto(s, 260, 510, 1400, 140,
      "La última hora de la jornada: le vamos a sacar todo el jugo.", 30, BLANCO)
texto(s, 260, 650, 1400, 140,
      "A cambio, sales entendiendo cómo funciona la IA, no solo usándola.", 30, CIAN)
pic(s, texto_pixel("ENERGÍA", 28, VERDE, "s6b", sombra=None, alinear="left"), 260, 805)
for i in range(18):
    b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, px(260 + i * 66), px(880), px(54), px(40))
    b.fill.solid()
    b.fill.fore_color.rgb = RGBColor(*VERDE)
    b.line.fill.background()
    b.shadow.inherit = False
for i in range(3):
    pic(s, sprite("corazon", 7), 1600 + i * 90, 800)

# ── Slide 7: HOY LA IA ESTÁ EN TODO ───────────────────────────────────
s = nueva(7, "s7", (
    "[4:30-5:00] Hoy la IA está en todo: en el celular, en las redes, en los trabajos. "
    "Hay dos formas de vivir eso: usarla o entenderla. "
    "Usarla la puede usar cualquiera. Entenderla (saber cómo aprende, por qué se equivoca) "
    "es lo que les permite crear la suya. "
    "Gancho: 'Les quiero mostrar algo que armé justo para esto.'"))
pic(s, texto_pixel("LA IA ESTÁ EN TODO", 56, BLANCO, "s7a", sombra=(40, 60, 170)), 0, 140, centrar=True)
caja(s, 130, 300, 650, 460, GRIS)
pic(s, texto_pixel("USARLA", 44, GRIS, "s7b", sombra=None), 130 + (650 - 270) // 2, 340)
texto(s, 170, 460, 570, 260, "Escribirle algo y esperar la respuesta. Lo hace cualquiera.", 26,
      GRIS, alinear=PP_ALIGN.CENTER)
pic(s, texto_pixel("VS", 48, AMARILLO, "s7c"), 0, 500, centrar=True)
caja(s, 1140, 300, 650, 460, CIAN)
pic(s, texto_pixel("ENTENDERLA", 44, CIAN, "s7d", sombra=(10, 60, 90)), 1140 + (650 - 440) // 2, 340)
texto(s, 1180, 460, 570, 260,
      "Saber cómo aprende, por qué se equivoca y crear la tuya.", 24, BLANCO,
      alinear=PP_ALIGN.CENTER)
pic(s, texto_pixel("MIREN ESTO...", 36, AMARILLO, "s7e"), 0, 830, centrar=True)

# ── Slide 8: INSERT COIN ──────────────────────────────────────────────
s = nueva(8, "s8", (
    "[5:00-5:20] Cierre y paso a la demo. Abrir demo-autos/index.html en pantalla completa ANTES de "
    "llegar a esta slide (dejarlo en otra ventana) y cambiar a ella al decir 'miren'. "
    "Mientras corre: 'Estos autos no saben manejar. Parten con cerebros al azar, chocan, y "
    "cada generación los mejores pasan sus genes a los siguientes. Eso que ven iluminarse "
    "es una red neuronal. Esto es lo que hay detrás de una IA, y es lo que vamos a construir.' "
    "Terminar con: 'Electivo de Computación. ¿Juegas?'  (F = acelerar, Espacio = pausa)."))
pic(s, sprite("moneda", 14), 150, 330)
pic(s, sprite("moneda", 14), W - 290, 330)
pic(s, texto_pixel(["¿QUIERES VER A UNA IA", "APRENDER SOLA?"], 64, BLANCO, "s8a",
                   sombra=MAGENTA), 0, 250, centrar=True)
pic(s, texto_pixel(">> DEMO <<", 64, AMARILLO, "s8b"), 0, 560, centrar=True)
pic(s, texto_pixel("ELECTIVO DE COMPUTACIÓN  ·  ¿JUEGAS?", 28, CIAN, "s8c", sombra=(10, 60, 90)),
    0, 780, centrar=True)
suelo(s, ["auto", "auto", "robot", "auto", "auto"], escala=9)

try:
    prs.save(SALIDA)
except PermissionError:  # el archivo está abierto en PowerPoint
    SALIDA = SALIDA.replace(".pptx", " (nueva).pptx")
    prs.save(SALIDA)
    print("AVISO: el original está abierto; se guardó una copia aparte.")
print("OK ->", SALIDA)
