"""Construye demo-autos/index.html (autocontenido, funciona offline) incrustando la fuente pixel."""
import base64
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(AQUI, "demo-autos", "demo_template.html"), encoding="utf-8").read()
fuente = base64.b64encode(open(os.path.join(AQUI, "assets", "PressStart2P-Regular.ttf"), "rb").read()).decode()
salida = os.path.join(AQUI, "demo-autos", "index.html")
open(salida, "w", encoding="utf-8").write(tpl.replace("__FONT_B64__", fuente))
print("OK ->", salida)
