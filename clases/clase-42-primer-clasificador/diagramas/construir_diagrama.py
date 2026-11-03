"""Dibuja el diagramita 'Así decide un árbol de decisión' (ejemplo inventado, distinto al árbol real de la clase).
Ejecutar: py -3 construir_diagrama.py"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

AQUI = Path(__file__).resolve().parent
AZUL, VERDE, ROJO, GRIS = "#1f4e79", "#2e7d32", "#c62828", "#555555"
fig, ax = plt.subplots(figsize=(9, 5.6), dpi=150)
ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")


def caja(x, y, texto, color, ancho=3.0, alto=0.9, relleno="#ffffff", lw=2.2):
    ax.add_patch(FancyBboxPatch((x - ancho / 2, y - alto / 2), ancho, alto, boxstyle="round,pad=0.05,rounding_size=0.18",
                                fc=relleno, ec=color, lw=lw))
    ax.text(x, y, texto, ha="center", va="center", fontsize=11, color=color, fontweight="bold")


def flecha(x1, y1, x2, y2, etiqueta, resaltar=False):
    c = "#f9a825" if resaltar else GRIS
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=c, lw=3.2 if resaltar else 1.8))
    ax.text((x1 + x2) / 2 + (-0.28 if x2 < x1 else 0.28), (y1 + y2) / 2, etiqueta, fontsize=11, fontweight="bold",
            color=c if not resaltar else "#e65100", ha="center", va="center")


# Pregunta raíz y pregunta intermedia (azul), respuestas finales (verde = puntual, rojo = atrasada)
caja(5, 5.4, "¿Llovió más de 10 mm?", AZUL)
caja(2.6, 3.3, "¿Taco de más de 5 km?", AZUL)
caja(7.6, 3.3, "ATRASADA", ROJO, ancho=2.3, relleno="#fdecea")
caja(1.3, 1.1, "PUNTUAL", VERDE, ancho=2.3, relleno="#e8f5e9")
caja(3.9, 1.1, "ATRASADA", ROJO, ancho=2.3, relleno="#fdecea")

flecha(4.2, 4.95, 2.9, 3.75, "No", resaltar=True)
flecha(5.8, 4.95, 7.4, 3.75, "Sí")
flecha(2.2, 2.85, 1.4, 1.55, "No", resaltar=True)
flecha(3.1, 2.85, 3.8, 1.55, "Sí")

ax.text(5, 6.05, "Así decide un árbol de decisión (ejemplo inventado)", ha="center", fontsize=13, fontweight="bold", color="#222222")
ax.text(9.9, 5.4, "PREGUNTA\n(sí / no)", ha="right", va="center", fontsize=9.5, color=AZUL)
ax.text(9.9, 1.1, "RESPUESTA\n(final)", ha="right", va="center", fontsize=9.5, color=GRIS)
ax.text(6.2, 0.35, "Día nuevo: 3 mm de lluvia y 2 km de taco  →  No, No  →  PUNTUAL (camino naranja)",
        ha="center", fontsize=10.5, color="#e65100", fontweight="bold")
fig.savefig(AQUI / "Diagrama - Un arbol de decision.png", bbox_inches="tight", facecolor="white")
print("ok")
