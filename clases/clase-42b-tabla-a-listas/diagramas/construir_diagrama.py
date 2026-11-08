"""Genera split_80_20.png: barra de 20 filas, 16 para aprender (80 %) y 4 para probar (20 %).
Ejecutar: py -3 construir_diagrama.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
FUENTE, NEGRITA = "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"
f = lambda ruta, t: ImageFont.truetype(ruta, t)

W, H = 1500, 470
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

AZUL, AZUL_BG, AMBAR, AMBAR_BG, TINTA, GRIS = "#1d4ed8", "#dbeafe", "#b45309", "#fef3c7", "#0f172a", "#475569"
x0, ancho, y0, alto = 50, 66, 170, 90   # 20 celdas de 66 px = 1320 px

def centrado(texto, cx, y, fuente, color):
    w = d.textlength(texto, font=fuente)
    d.text((cx - w / 2, y), texto, font=fuente, fill=color)

# títulos de cada grupo
cx_train = x0 + 8 * ancho
cx_test = x0 + 18 * ancho
centrado("Los primeras 16 filas (80 %)", cx_train, 28, f(NEGRITA, 34), AZUL)
centrado("la computadora APRENDE con estos", cx_train, 76, f(FUENTE, 28), TINTA)
centrado("Los últimos 4 (20 %)", cx_test, 28, f(NEGRITA, 34), AMBAR)
centrado("los guardamos para PROBARLA", cx_test, 76, f(FUENTE, 28), TINTA)

# celdas
for i in range(20):
    x = x0 + i * ancho
    train = i < 16
    d.rectangle([x, y0, x + ancho, y0 + alto], fill=AZUL_BG if train else AMBAR_BG,
                outline=AZUL if train else AMBAR, width=3)
    centrado(str(i + 1), x + ancho / 2, y0 + 26, f(NEGRITA, 34), AZUL if train else AMBAR)

# corte entre 16 y 17
xc = x0 + 16 * ancho
d.line([xc, y0 - 22, xc, y0 + alto + 22], fill=TINTA, width=6)

# llaves bajo cada grupo
for ini, fin, color in ((0, 16, AZUL), (16, 20, AMBAR)):
    xa, xb = x0 + ini * ancho + 4, x0 + fin * ancho - 4
    yb = y0 + alto + 28
    d.line([xa, yb, xb, yb], fill=color, width=5)
    d.line([xa, yb - 12, xa, yb], fill=color, width=5)
    d.line([xb, yb - 12, xb, yb], fill=color, width=5)

centrado("De 20 filas anotados: aprende con 16 y se prueba con 4 que no vio.", W / 2, 380, f(FUENTE, 32), TINTA)
centrado("Cada número es una fila de clases, en el mismo orden de la tabla.", W / 2, 424, f(FUENTE, 24), GRIS)

img.save(AQUI / "split_80_20.png")
print("Listo:", AQUI / "split_80_20.png")
