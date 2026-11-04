"""Dibuja 'Una neurona' en versión general (la esencia): 3 datos -> neurona -> salida.
Sin valores de pesos, sin sumas ni multiplicaciones: los números aparecen recién al final de la clase.
Ejecutar: py -3 construir_diagrama.py"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

AQUI = Path(__file__).resolve().parent
AZUL, VERDE, ROJO, GRIS, NARANJA = "#1f4e79", "#2e7d32", "#c62828", "#555555", "#e65100"
fig, ax = plt.subplots(figsize=(10, 5.4), dpi=150)
ax.set_xlim(0, 12); ax.set_ylim(0, 6.4); ax.axis("off")


def caja(x, y, texto, color, ancho=2.6, alto=0.9, relleno="#ffffff", lw=2.2, size=11):
    ax.add_patch(FancyBboxPatch((x - ancho / 2, y - alto / 2), ancho, alto, boxstyle="round,pad=0.05,rounding_size=0.18",
                                fc=relleno, ec=color, lw=lw))
    ax.text(x, y, texto, ha="center", va="center", fontsize=size, color=color, fontweight="bold")


entradas = [("temperatura", 5.0), ("viento", 3.2), ("lluvia", 1.4)]
nx, ny = 6.2, 3.2
for nombre, y in entradas:
    caja(1.6, y, nombre, AZUL)
    ax.annotate("", xy=(nx - 0.95, ny + (y - ny) * 0.28), xytext=(2.95, y),
                arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=3.2))
    mx, my = 4.2, y + (ny + (y - ny) * 0.28 - y) * 0.45
    ax.text(mx, my + (0.42 if y >= ny else -0.42), "peso", fontsize=12, fontweight="bold", color=GRIS, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))

ax.add_patch(Circle((nx, ny), 0.95, fc="#fff8e1", ec=NARANJA, lw=3))
ax.text(nx, ny + 0.12, "NEURONA", ha="center", va="center", fontsize=12, fontweight="bold", color=NARANJA)
ax.text(nx, ny - 0.28, "decide", ha="center", va="center", fontsize=10.5, color=NARANJA)

ax.annotate("", xy=(9.05, ny + 0.75), xytext=(nx + 0.95, ny + 0.2), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2.6))
ax.annotate("", xy=(9.05, ny - 0.75), xytext=(nx + 0.95, ny - 0.2), arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=2.6))
ax.text(7.95, ny + 0.85, "se activa", ha="center", fontsize=10.5, fontweight="bold", color=VERDE)
ax.text(7.95, ny - 0.95, "no se activa", ha="center", fontsize=10.5, fontweight="bold", color=ROJO)
caja(10.3, ny + 0.75, "1 = SALEN", VERDE, ancho=2.3, relleno="#e8f5e9")
caja(10.3, ny - 0.75, "0 = SE QUEDAN", ROJO, ancho=2.3, relleno="#fdecea")

ax.text(6, 6.15, "Así decide una neurona (la idea general)", ha="center", fontsize=13, fontweight="bold", color="#222222")
ax.text(1.6, 5.85, "DATOS DEL DÍA", ha="center", fontsize=9.5, color=AZUL)
ax.text(10.3, 5.0, "SALIDA", ha="center", fontsize=9.5, color=GRIS)
ax.text(6, 0.3, "Los datos entran, cada uno con su importancia (su peso), y la neurona decide si se activa",
        ha="center", fontsize=10.5, color=NARANJA, fontweight="bold")
fig.savefig(AQUI / "Diagrama - Una neurona.png", bbox_inches="tight", facecolor="white")
print("ok")
