"""Genera neurona.png y activacion.png (clase 43 v2) con los pesos reales de la neurona (random_state=0).
Ejecutar: py -3 -X utf8 construir_diagramas.py
"""
import json
import warnings
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from sklearn.neural_network import MLPClassifier  # noqa: E402

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
W = json.loads((AQUI.parents[1] / "clase-42b-tabla-a-listas" / "datos_wifi_verificados.json").read_text(encoding="utf-8"))
X, Y = [f[:3] for f in W["X"]], W["y"]
M = MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=0).fit(X[:16], Y[:16])
PESOS, SESGO = M.coefs_[0].ravel(), float(M.intercepts_[0][0])
AZUL, NARANJA, VERDE, ROJO, GRIS = "#1d4ed8", "#b45309", "#065f46", "#b91c1c", "#475569"
NOMBRES = ["dispositivos_conectados", "estudiantes_viendo_video", "horas_desde_reinicio"]
COL = [AZUL, NARANJA, VERDE]

# ── Diagrama 1: la neurona ──
fig, ax = plt.subplots(figsize=(10, 4.6))
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.6)
ys = [3.7, 2.3, 0.9]
for y, n, c, w in zip(ys, NOMBRES, COL, PESOS):
    ax.text(0.1, y, n, ha="left", va="center", fontsize=11, color=c, fontweight="bold")
    ax.annotate("", xy=(5.0, 2.3), xytext=(3.2, y), arrowprops=dict(arrowstyle="->", color=c, lw=2 + 6 * min(abs(w), 0.5)))
    ax.text(4.0, (y + 2.3) / 2 + 0.2, "× peso", fontsize=10, color=c, ha="center")
ax.add_patch(plt.Circle((5.7, 2.3), 0.75, fc="#dbeafe", ec=AZUL, lw=2.5))
ax.text(5.7, 2.3, "suma", ha="center", va="center", fontsize=13, fontweight="bold")
ax.annotate("", xy=(7.6, 2.3), xytext=(6.45, 2.3), arrowprops=dict(arrowstyle="->", color=GRIS, lw=2))
ax.add_patch(plt.Rectangle((7.6, 1.8), 1.3, 1.0, fc="#fef3c7", ec=NARANJA, lw=2.5))
ax.text(8.25, 2.3, "nivel de\nactivación", ha="center", va="center", fontsize=10, fontweight="bold")
ax.annotate("", xy=(9.9, 2.3), xytext=(8.9, 2.3), arrowprops=dict(arrowstyle="->", color=GRIS, lw=2))
ax.text(9.95, 3.0, "1 = se cae", ha="right", fontsize=11, color=NARANJA, fontweight="bold")
ax.text(9.95, 1.5, "0 = aguanta", ha="right", fontsize=11, color=AZUL, fontweight="bold")
ax.set_title("Una neurona: recibe, pondera, suma y decide", fontsize=14, fontweight="bold")
fig.tight_layout(); fig.savefig(AQUI / "neurona.png", dpi=110); plt.close(fig)

# ── Diagrama 2: nivel de activación ──
fig, ax = plt.subplots(figsize=(10, 4.6))
z = np.linspace(-7, 7, 300)
ax.plot(z, 1 / (1 + np.exp(-z)), color=AZUL, lw=3)
ax.axhline(0.5, color=GRIS, ls="--", lw=1.5)
ax.text(-6.9, 0.53, "umbral 0,5: arriba decide 1, abajo decide 0", color=GRIS, fontsize=10)
for i, f in enumerate(X[16:]):
    zi = float(np.dot(PESOS, f) + SESGO)
    pi = 1 / (1 + np.exp(-zi))
    c = NARANJA if Y[16 + i] == 1 else AZUL
    ax.scatter([zi], [pi], s=120, color=c, zorder=5, edgecolor="black")
    ax.annotate(f"fila {17 + i}", (zi, pi), textcoords="offset points", xytext=(8, -14 if pi > 0.5 else 8), fontsize=10)
ax.set_xlabel("suma de lo ponderado (más el sesgo)", fontsize=11)
ax.set_ylabel("nivel de activación (0 a 1)", fontsize=11)
ax.set_title("El nivel de activación: de la suma a una decisión (puntos = filas de prueba; color = lo que pasó de verdad)", fontsize=11, fontweight="bold")
ax.scatter([], [], color=NARANJA, edgecolor="black", label="en realidad se cayó (1)")
ax.scatter([], [], color=AZUL, edgecolor="black", label="en realidad aguantó (0)")
ax.legend(loc="lower right", fontsize=10)
fig.tight_layout(); fig.savefig(AQUI / "activacion.png", dpi=110); plt.close(fig)
print("Listo: neurona.png, activacion.png · pesos", np.round(PESOS, 3), "sesgo", round(SESGO, 3))
