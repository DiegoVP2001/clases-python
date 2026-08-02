#!/usr/bin/env python3
"""
limpiar_outputs_haz_ahora.py — Deja el Colab de clase con outputs solo donde
corresponde: en los ejemplos del ICN.

Uso:
    python limpiar_outputs_haz_ahora.py "clases/clase-NN-tema/Clase NN - Tema - Clase.ipynb"

Por qué: el flujo estándar ejecuta el notebook con nbconvert para verificar que
corre sin errores, y eso deja los outputs guardados dentro del .ipynb.

- En el **ICN** eso está bien y es lo que se quiere: el estudiante lee el ejemplo
  junto a su resultado, sin depender de haber ejecutado en orden.
- En **cualquier otra sección** el output guardado sabotea la actividad. Un Haz
  Ahora que consiste en ejecutar programas con un error y observar qué imprimen
  deja de tener sentido si el resultado ya está impreso; y una celda de
  verificación de la Práctica Independiente que ya trae su salida invita a
  leerla en vez de ejecutarla.

Regla aplicada: conservar outputs solo en las celdas de código que caen dentro
de la sección "## 2️⃣ Introducción al Contenido Nuevo"; limpiar todas las demás.
"""

import sys
from pathlib import Path

try:
    import nbformat
except ImportError:
    print("ERROR: nbformat no está instalado. Instálalo con:")
    print("    pip install nbformat")
    sys.exit(1)

# Encabezado de la única sección cuyos outputs se conservan.
SECCION_CON_OUTPUTS = "## 2️⃣"
# Cualquier encabezado de sección de nivel 2 marca el fin de la sección anterior.
PREFIJO_SECCION = "## "


def limpiar(ruta: Path) -> int:
    nb = nbformat.read(ruta, as_version=4)
    conservar = False
    limpiadas = 0

    for celda in nb.cells:
        if celda.cell_type == "markdown":
            for linea in celda.source.splitlines():
                if linea.startswith(PREFIJO_SECCION):
                    conservar = linea.startswith(SECCION_CON_OUTPUTS)
            continue
        if not conservar and celda.cell_type == "code" and celda.get("outputs"):
            celda.outputs = []
            celda.execution_count = None
            limpiadas += 1

    if limpiadas:
        nbformat.write(nb, ruta.open("w", encoding="utf-8"))
    return limpiadas


def main():
    if len(sys.argv) != 2:
        print("Uso: python limpiar_outputs_haz_ahora.py <ruta_Clase.ipynb>")
        sys.exit(1)

    ruta = Path(sys.argv[1])
    if not ruta.exists():
        print(f"ERROR: no existe el archivo {ruta}")
        sys.exit(1)

    limpiadas = limpiar(ruta)
    if limpiadas:
        print(f"🧹 {limpiadas} celda(s) fuera del ICN quedaron sin output en: {ruta}")
    else:
        print(f"✅ {ruta} no tenía outputs que limpiar fuera del ICN.")


if __name__ == "__main__":
    main()
