#!/usr/bin/env python3
"""
crear_colab_ejercicios.py — Generador del Colab de ejercicios adicionales

Uso:
    python crear_colab_ejercicios.py <ruta_a_ejercicios.md> <ruta_salida.ipynb>

Ejemplo:
    python crear_colab_ejercicios.py clases/clase-07-input/ejercicios.md clases/clase-07-input/02-ejercicios.ipynb

Lee un archivo markdown con la propuesta aprobada de ejercicios adicionales
y produce un Jupyter notebook (.ipynb) con cada ejercicio en su sección,
celda de código vacía para el estudiante y solución oculta con <details>.

Requiere: nbformat (instalar con: pip install nbformat)
"""

import sys
import re
from pathlib import Path

try:
    import nbformat
    from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
except ImportError:
    print("ERROR: nbformat no está instalado. Instálalo con:")
    print("    pip install nbformat")
    sys.exit(1)


# =====================================================================
# PARSER DEL ARCHIVO DE EJERCICIOS
# =====================================================================

def parsear_ejercicios(ruta_md: Path) -> dict:
    """Parsea el archivo ejercicios.md y devuelve un diccionario estructurado."""
    contenido = ruta_md.read_text(encoding="utf-8")

    datos = {
        "numero_clase": None,
        "tema": None,
        "introduccion": None,
        "ejercicios": [],
    }

    # Encabezado: "# Ejercicios adicionales — Clase 07: ..." o "# Ejercicios adicionales — Clase 8a: ..."
    match_titulo = re.search(
        r"^#\s+Ejercicios adicionales\s*[—\-–]\s*Clase\s+(\w+)\s*[:\-–—]\s*(.+)$",
        contenido,
        re.MULTILINE,
    )
    if match_titulo:
        raw = match_titulo.group(1)
        datos["numero_clase"] = int(raw) if raw.isdigit() else raw
        datos["tema"] = match_titulo.group(2).strip()

    # Introducción: contenido entre "## Introducción" y el primer "## Ejercicio"
    match_intro = re.search(
        r"##\s+Introducción\s*\n(.*?)(?=##\s+Ejercicio\s+\d)",
        contenido,
        re.DOTALL,
    )
    if match_intro:
        datos["introduccion"] = match_intro.group(1).strip()

    # Ejercicios: cada uno empieza con "## Ejercicio N — Título"
    # Capturamos todos los bloques de ejercicio
    bloques = re.split(r"##\s+Ejercicio\s+(\d+)\s*[—\-–]\s*([^\n]+)", contenido)
    # bloques[0] = todo lo antes del primer ejercicio
    # Luego se repite: [numero, titulo, contenido, numero, titulo, contenido, ...]

    for i in range(1, len(bloques), 3):
        if i + 2 >= len(bloques):
            break
        num = bloques[i].strip()
        titulo = bloques[i + 1].strip()
        cuerpo = bloques[i + 2]

        ejercicio = parsear_ejercicio_individual(num, titulo, cuerpo)
        datos["ejercicios"].append(ejercicio)

    return datos


def parsear_ejercicio_individual(numero: str, titulo: str, cuerpo: str) -> dict:
    """Parsea un bloque individual de ejercicio."""
    ejercicio = {
        "numero": numero,
        "titulo": titulo,
        "es_desafio": False,
        "nivel": None,
        "enunciado": None,
        "pistas": None,
        "resultado_esperado": None,
        "solucion": None,
    }

    # Detectar si es desafío opcional
    if re.search(r"⭐|desafío|opcional|reto|avanzado", titulo, re.IGNORECASE):
        ejercicio["es_desafio"] = True

    # Nivel (opcional)
    match_nivel = re.search(r"\*\*Nivel:\*\*\s*(.+)", cuerpo)
    if match_nivel:
        ejercicio["nivel"] = match_nivel.group(1).strip()
        if "desafío" in ejercicio["nivel"].lower() or "avanzado" in ejercicio["nivel"].lower():
            ejercicio["es_desafio"] = True

    # Enunciado: entre "**Enunciado:**" y el siguiente "**...:**" o sección
    match_enunciado = re.search(
        r"\*\*Enunciado:\*\*\s*\n(.*?)(?=\n\*\*[A-ZÁÉÍÓÚ]|\n##|\Z)",
        cuerpo,
        re.DOTALL,
    )
    if match_enunciado:
        ejercicio["enunciado"] = match_enunciado.group(1).strip()

    # Pistas (opcional)
    match_pistas = re.search(
        r"\*\*Pistas?:\*\*\s*\n(.*?)(?=\n\*\*[A-ZÁÉÍÓÚ]|\n##|\Z)",
        cuerpo,
        re.DOTALL,
    )
    if match_pistas:
        ejercicio["pistas"] = match_pistas.group(1).strip()

    # Resultado esperado
    match_resultado = re.search(
        r"\*\*Resultado esperado:\*\*\s*\n```\n?(.*?)```",
        cuerpo,
        re.DOTALL,
    )
    if match_resultado:
        ejercicio["resultado_esperado"] = match_resultado.group(1).rstrip()

    # Solución (código Python)
    match_solucion = re.search(
        r"\*\*Solución:\*\*\s*\n```python\n(.*?)```",
        cuerpo,
        re.DOTALL,
    )
    if match_solucion:
        ejercicio["solucion"] = match_solucion.group(1).rstrip()

    return ejercicio


# =====================================================================
# CONSTRUCCIÓN DEL NOTEBOOK
# =====================================================================

def construir_notebook(datos: dict) -> nbformat.NotebookNode:
    """Construye el notebook de ejercicios."""
    nb = new_notebook()
    nb.cells = []

    # --- ENCABEZADO ---
    nb.cells.append(new_markdown_cell(generar_encabezado(datos)))

    # --- INTRODUCCIÓN ---
    if datos["introduccion"]:
        nb.cells.append(new_markdown_cell(generar_introduccion(datos)))

    # --- ÍNDICE DE EJERCICIOS ---
    nb.cells.append(new_markdown_cell(generar_indice(datos)))

    # --- CADA EJERCICIO ---
    for ejercicio in datos["ejercicios"]:
        nb.cells.append(new_markdown_cell(generar_enunciado(ejercicio)))
        nb.cells.append(new_code_cell(f"# Tu solución del Ejercicio {ejercicio['numero']}\n"))

    # --- CIERRE ---
    nb.cells.append(new_markdown_cell(generar_cierre(datos)))
    nb.cells.append(new_markdown_cell("---\n\n"))

    # --- SOLUCIONES AL FINAL ---
    nb.cells.append(new_markdown_cell(generar_seccion_soluciones(datos)))

    return nb


def generar_encabezado(datos: dict) -> str:
    n = datos['numero_clase']
    num = f"{n:02d}" if isinstance(n, int) else (str(n) if n is not None else "??")
    return f"""# 💪 Ejercicios — Clase {num}: {datos['tema']}

**Práctica adicional para reforzar lo aprendido en clase.**

---"""


def generar_introduccion(datos: dict) -> str:
    return f"## 📌 Antes de empezar\n\n{datos['introduccion']}\n"


def generar_indice(datos: dict) -> str:
    bloque = "## 📋 Lista de ejercicios\n\n"
    for ej in datos["ejercicios"]:
        titulo_limpio = ej["titulo"].replace("⭐", "").strip()
        marca = " ⭐" if ej["es_desafio"] else ""
        bloque += f"- **Ejercicio {ej['numero']}** — {titulo_limpio}{marca}\n"
    bloque += "\n⭐ = Desafío opcional para quienes quieran ir más allá.\n\n"
    bloque += "**Recomendación:** intenta cada ejercicio por tu cuenta antes de mirar la solución. "
    bloque += "Si te atascas más de 10 minutos, revisa la pista (si la tiene) y solo después la solución.\n"
    return bloque


def generar_enunciado(ejercicio: dict) -> str:
    titulo_limpio = ejercicio["titulo"].replace("⭐", "").strip()
    marca = " ⭐" if ejercicio["es_desafio"] else ""
    bloque = f"---\n\n## Ejercicio {ejercicio['numero']} — {titulo_limpio}{marca}\n\n"

    if ejercicio["nivel"]:
        bloque += f"**Nivel:** {ejercicio['nivel']}\n\n"

    if ejercicio["enunciado"]:
        bloque += ejercicio["enunciado"] + "\n\n"

    if ejercicio["pistas"]:
        bloque += "<details>\n<summary>💡 Ver pista (solo si te atascas)</summary>\n\n"
        bloque += ejercicio["pistas"] + "\n\n</details>\n\n"

    if ejercicio["resultado_esperado"]:
        bloque += "**Resultado esperado:**\n\n```\n"
        bloque += ejercicio["resultado_esperado"]
        bloque += "\n```\n"

    return bloque


def generar_solucion(ejercicio: dict) -> str:
    bloque = "<details>\n<summary>🔓 Ver solución (solo después de intentarlo)</summary>\n\n"
    if ejercicio["solucion"]:
        bloque += "```python\n" + ejercicio["solucion"] + "\n```\n"
    else:
        bloque += "_Solución no disponible. Consulta al profe._\n"
    bloque += "\n</details>"
    return bloque


def generar_cierre(datos: dict) -> str:
    num_total = len(datos["ejercicios"])
    num_desafios = sum(1 for ej in datos["ejercicios"] if ej["es_desafio"])
    num_base = num_total - num_desafios

    bloque = "---\n\n## 🏁 Ya terminaste\n\n"
    bloque += f"Has completado los {num_total} ejercicios de esta práctica "
    bloque += f"({num_base} de práctica base"
    if num_desafios > 0:
        bloque += f" + {num_desafios} desafío"
        if num_desafios > 1:
            bloque += "s"
        bloque += " opcional"
        if num_desafios > 1:
            bloque += "es"
    bloque += ").\n\n"
    bloque += "**Antes de cerrar:**\n\n"
    bloque += "1. ¿Cuál te resultó más fácil? ¿Por qué?\n"
    bloque += "2. ¿Cuál te costó más? ¿Qué hiciste para resolverlo?\n"
    bloque += "3. Si quieres seguir practicando, prueba cambiando los datos de entrada y observa qué pasa.\n"
    return bloque


def generar_seccion_soluciones(datos: dict) -> str:
    bloque = "## 📋 Soluciones\n\n"
    bloque += "> Intenta resolver cada ejercicio antes de mirar aquí.\n\n"
    for ej in datos["ejercicios"]:
        titulo_limpio = ej["titulo"].replace("⭐", "").strip()
        bloque += "<details>\n"
        bloque += f"<summary>🔓 Ejercicio {ej['numero']} — {titulo_limpio}</summary>\n\n"
        if ej["solucion"]:
            bloque += f"```python\n{ej['solucion']}\n```\n\n"
        else:
            bloque += "_Solución no disponible. Consulta al profe._\n\n"
        bloque += "</details>\n\n"
    return bloque.rstrip()


# =====================================================================
# MAIN
# =====================================================================

def main():
    if len(sys.argv) != 3:
        print("Uso: python crear_colab_ejercicios.py <ruta_ejercicios.md> <ruta_salida.ipynb>")
        sys.exit(1)

    ruta_md = Path(sys.argv[1])
    ruta_salida = Path(sys.argv[2])

    if not ruta_md.exists():
        print(f"ERROR: no existe el archivo {ruta_md}")
        sys.exit(1)

    print(f"📖 Leyendo propuesta de ejercicios: {ruta_md}")
    datos = parsear_ejercicios(ruta_md)

    print(f"✅ Parseado: Clase {datos['numero_clase']} — {datos['tema']}")
    print(f"   - {len(datos['ejercicios'])} ejercicios encontrados")
    desafios = sum(1 for e in datos["ejercicios"] if e["es_desafio"])
    if desafios:
        print(f"   - de los cuales {desafios} son desafío opcional")

    if len(datos["ejercicios"]) == 0:
        print("⚠️  ADVERTENCIA: no se detectó ningún ejercicio. Revisa el formato del archivo.")
        sys.exit(1)

    print(f"🛠️  Construyendo notebook...")
    nb = construir_notebook(datos)

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    with ruta_salida.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"💾 Notebook guardado en: {ruta_salida}")
    print(f"📤 Súbelo a Colab desde https://colab.research.google.com (Archivo → Subir cuaderno)")


if __name__ == "__main__":
    main()
