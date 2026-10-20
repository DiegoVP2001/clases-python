"""Genera 'Clase 38y38b - Muestra de las Bases.tex' y lo compila a .pdf (tectonic).

Reemplaza al Excel de muestras (se descartó: al abrirlo en otros idiomas/configuraciones regionales Excel podía
cambiar 250.3 por 250,3 y desfigurar justo lo que se quiere mostrar). El PDF es estático: se ve igual en cualquier equipo.

Una página (o más) por base del menú: TODAS las columnas de la base v3 (ya limpia) y 6 filas reales (semilla fija),
elegidas para que cada columna con vacíos aparezca con dato en una fila y vacía en otra. Los valores son el texto
literal del CSV. Cada fila de la muestra va en una columna del PDF (la tabla está traspuesta para que quepan las
bases de 71 columnas). Al final de cada base se explican sus columnas nuevas (separadas o calculadas).

Uso:  python generar_muestra_pdf.py
"""
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
V3 = AQUI / "datos-compartidos-v3"
NOMBRE = "Clase 38y38b - Muestra de las Bases"
TEX = AQUI / f"{NOMBRE}.tex"
PDF = AQUI / f"{NOMBRE}.pdf"

N_FILAS = 6
SEMILLA = 37

# (n° del menú, nombre completo, archivo)
BASES = [
    ("1", "Empleabilidad e ingresos por carrera (SIES)", "01_sies.csv"),
    ("2", "Puntajes de corte por carrera — Admisión 2026 (DEMRE)", "02_demre.csv"),
    ("3", "SIMCE 2° medio 2025, por establecimiento", "03_simce_establecimiento.csv"),
    ("4", "SIMCE 2° medio 2025, por comuna", "04_simce_comuna.csv"),
    ("5", "Matrícula de estudiantes por establecimiento 2025 (Mineduc)", "05_matricula.csv"),
    ("6", "Subvenciones a establecimientos 2025", "06_subvenciones.csv"),
    ("7", "Siniestros de tránsito 2020-2025 (CONASET), Región Metropolitana", "07_conaset_rm.csv"),
    ("8", "Precios de alimentos al consumidor 2025 (ODEPA), Región Metropolitana", "08a_odepa_consumidor.csv"),
    ("9a", "Estadísticas hospitalarias 2024 — mensual", "09a_hospitalarias_mensual.csv"),
    ("9b", "Estadísticas hospitalarias 2024 — anual", "09b_hospitalarias_anual.csv"),
]

# Columnas que no vienen en la fuente: se calculan o se separan al preparar la base (la columna original se conserva).
AVISOS_COLUMNAS_NUEVAS = {
    ("01_sies.csv", "Acreditacion_anios"): "Sale de «Acreditación institución»: «5 años» pasa a 5. «No» (sin acreditación) pasa a 0.",
    ("01_sies.csv", "Ingreso_min"): "Sale de «Ingreso Promedio al 4° año»: el mínimo del rango, en pesos. Vacío si el rango dice s/i.",
    ("01_sies.csv", "Ingreso_max"): "Sale de «Ingreso Promedio al 4° año»: el máximo del rango, en pesos. Vacío si dice s/i o «Sobre $3 millones 500 mil» (sin tope).",
    ("01_sies.csv", "Ingreso_punto_medio"): "El punto medio de Ingreso_min e Ingreso_max, en pesos. En «Sobre $3 millones 500 mil» vale 3.500.000.",
    ("02_demre.csv", "MARGEN_P25_MENOS_ULTIMO"): "Calculada: PROM_OBLIGATORIAS_P25 menos PROM_OBLIGATORIAS_ULTIMO_SELEC.",
    ("08a_odepa_consumidor.csv", "Unidad_cantidad"): "Sale de «Unidad»: «$/bolsa 800 grs» da 800. Lo que va entre paréntesis describe el envase: «$/kilo (en saco de 25 kilos)» da 1.",
    ("08a_odepa_consumidor.csv", "Unidad_medida"): "Sale de «Unidad»: kilos, gramos, litros, ml o unidades.",
    ("07_conaset_rm.csv", "Mes_num"): "Número del mes (1 a 12), para ordenar por mes.",
    ("09a_hospitalarias_mensual.csv", "Egresos_por_dia"): "Calculada: Numero_de_Egresos ÷ Dias_mes. 3.129 es tres coma ciento veintinueve egresos por día, no tres mil.",
}

RE_NUM = re.compile(r"-?[\d.,]+")


def categoria(v: str) -> str:
    if v == "":
        return "vacio"
    if v == "s/i":
        return "si"
    if re.fullmatch(r"-?\d+,\d+", v):
        return "coma"
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})+", v):
        return "miles"
    if re.fullmatch(r"-?\d+\.\d+", v):
        return "punto"
    if re.fullmatch(r"-?\d+", v):
        return "entero"
    return "otro"


def columnas_texto_numerico(texto: pd.DataFrame, tipos: pd.Series) -> list:
    """Columnas que pandas lee como texto pero cuyo contenido son números (con coma, miles o s/i)."""
    cols = []
    for c in texto.columns:
        if str(tipos[c]) not in ("str", "object", "string"):
            continue
        s = texto[c][texto[c] != ""]
        if len(s) and s.str.fullmatch(RE_NUM.pattern + "|s/i").mean() >= 0.9:
            cols.append(c)
    return cols


def elegir_filas(texto: pd.DataFrame, cols: list) -> list:
    """Cobertura voraz: la fila que aporta más pares (columna, categoría) todavía no vistos."""
    rng = random.Random(SEMILLA)
    candidatos = list(range(len(texto)))
    if len(candidatos) > 4000:
        candidatos = rng.sample(candidatos, 4000)
    cats = {c: texto[c].map(categoria) for c in cols}
    firmas = {i: {(c, cats[c].iat[i]) for c in cols} for i in candidatos}
    cubiertos, elegidas = set(), []
    for _ in range(N_FILAS):
        mejor = max(candidatos, key=lambda i: (len(firmas[i] - cubiertos), rng.random()))
        if not (firmas[mejor] - cubiertos):
            break
        elegidas.append(mejor)
        cubiertos |= firmas[mejor]
        candidatos.remove(mejor)
    while len(elegidas) < N_FILAS:
        i = rng.choice(candidatos)
        candidatos.remove(i)
        elegidas.append(i)
    return sorted(elegidas)


# ───────────────────────── LaTeX ─────────────────────────
ESCAPES = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
    "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    # Que TeX no cambie el dato: comilla simple recta (no ’), comilla doble recta y guiones sin ligaduras (-- → –).
    "'": r"\textquotesingle{}", '"': r"\textquotedbl{}", "`": r"\textasciigrave{}", "-": "-{}",
}


def esc(texto: str) -> str:
    return "".join(ESCAPES.get(ch, ch) for ch in texto)


def partir_largo(token: str, paso: int = 9) -> str:
    """Permite cortar una palabra larga sin espacios (URLs, códigos) para que no desborde la celda."""
    if len(token) <= 14:
        return esc(token)
    return r"\allowbreak{}".join(esc(token[i:i + paso]) for i in range(0, len(token), paso))


def valor_tex(v: str) -> str:
    if v == "":
        return r"\textit{\color{gris}(vacío)}"
    return " ".join(partir_largo(t) for t in v.split(" "))


def nombre_col_tex(nombre: str) -> str:
    # La columna se escribe tal cual (monoespaciada); se permite cortar después de cada guion bajo.
    partes = [esc(p) for p in nombre.split("_")]
    return r"\texttt{" + r"\_\allowbreak{}".join(partes) + "}"


PREAMBULO = r"""\PassOptionsToPackage{table}{xcolor}
\documentclass[10pt]{article}
\usepackage[a4paper,landscape,left=1.5cm,right=1.5cm,top=2.1cm,bottom=1.6cm,headheight=14pt]{geometry}
\usepackage{fontspec}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[most]{tcolorbox}
\usepackage{xltabular}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{parskip}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{ragged2e}

\definecolor{azuloscuro}{HTML}{1F4E79}
\definecolor{azulclaro}{HTML}{DCE9F5}
\definecolor{rojoalerta}{HTML}{B3261E}
\definecolor{gris}{HTML}{777777}

\newtcolorbox{alertabox}[1][]{enhanced, colback=white, colframe=rojoalerta, coltitle=white, fonttitle=\bfseries\small,
  title={#1}, boxrule=0.8pt, arc=2pt, left=6pt, right=6pt, top=3pt, bottom=3pt, breakable}
\newtcolorbox{guiabox}[1][]{enhanced, colback=white, colframe=azuloscuro, coltitle=white, fonttitle=\bfseries\small,
  title={#1}, boxrule=0.8pt, arc=2pt, left=6pt, right=6pt, top=3pt, bottom=3pt, breakable}

\titleformat{\section}{\Large\bfseries\color{azuloscuro}}{}{0pt}{}[\vspace{-4pt}\textcolor{azuloscuro}{\rule{\linewidth}{0.8pt}}]
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Clase 38y38b --- Muestra de las bases}
\fancyhead[R]{\small 4.º medio --- Proyecto de cierre}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\parindent}{0pt}
\setlength{\tabcolsep}{3.5pt}
\renewcommand{\arraystretch}{1.2}
\setlength{\LTpre}{4pt}
\setlength{\LTpost}{4pt}
\newcommand{\hdr}[1]{\textbf{\color{white}#1}}
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
\sloppy
"""

PORTADA = r"""
\begin{center}
{\Huge\bfseries\color{azuloscuro} Muestra de las bases\par}
\vspace{4pt}
{\large Las bases del proyecto de cierre, tal como se abren en tu cuaderno\par}
\vspace{2pt}
{\small Clase 38y38b --- Responder con datos\par}
\end{center}

\vspace{4pt}
Cada base del menú tiene su propia página (o más): \textbf{todas sus columnas} y \textbf{6 filas reales}. Cada fila de la muestra es una columna del PDF (\textit{fila 1} a \textit{fila 6}); cada fila de este PDF es una columna de tu base.

\begin{guiabox}[Cómo leer lo que ves]
\begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
\item Las bases ya vienen \textbf{limpias}: los números son números, con \textbf{punto} decimal (\texttt{0.65} es sesenta y cinco centésimos) y sin punto de miles (\texttt{253447695}).
\item \textit{(vacío)} $\to$ dato que falta. Pandas lo cuenta como vacío.
\item Hay columnas \textbf{nuevas}, que no vienen en la fuente: se calcularon o se separaron para que puedas trabajar con números (por ejemplo \texttt{Ingreso\_min} e \texttt{Ingreso\_max}). La columna original se conserva y cada base explica las suyas al final de su página.
\end{itemize}
\end{guiabox}

\begin{alertabox}[Ojo]
\begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
\item Los valores están copiados \textbf{tal cual} del archivo CSV: nada está redondeado ni cambiado.
\item Que una columna sea un número no quiere decir que se pueda sumar: un año, un código o una fecha son números que funcionan como \textbf{etiquetas}.
\item En tu cuaderno verás el tipo de cada columna con \texttt{.dtype}.
\end{itemize}
\end{alertabox}

\vspace{4pt}
\begin{guiabox}[Índice]
\begin{tabular}{@{}r l@{}}
"""


def construir() -> str:
    partes = [PREAMBULO, PORTADA]
    for n, nombre, _ in BASES:
        partes.append(f"{n} & \\hyperlink{{base{n}}}{{\\textcolor{{azuloscuro}}{{\\underline{{{esc(nombre)}}}}}}} \\\\\n")
    partes.append("\\end{tabular}\n\\end{guiabox}\n")

    resumen = []
    for n, nombre, archivo in BASES:
        ruta = V3 / archivo
        texto = pd.read_csv(ruta, dtype=str, keep_default_na=False, na_values=[], low_memory=False)
        # Que cada columna con vacíos se vea con dato en alguna fila de la muestra y también vacía en otra
        cols_con_vacios = [c for c in texto.columns if (texto[c] == "").any() and (texto[c] != "").any()]
        filas = (elegir_filas(texto, cols_con_vacios) if cols_con_vacios
                 else sorted(random.Random(SEMILLA).sample(range(len(texto)), N_FILAS)))
        muestra = texto.iloc[filas]
        resumen.append((n, archivo, len(texto), len(texto.columns), filas))

        partes.append("\n\\clearpage\n")
        partes.append(f"\\hypertarget{{base{n}}}{{}}\\phantomsection\\pdfbookmark[1]{{Base {n}}}{{bm{n}}}\n")
        partes.append(f"\\section{{{esc(n)} · {esc(nombre)}}}\n")
        partes.append(
            f"\\small Archivo \\texttt{{{esc(archivo)}}} · {len(texto):,} filas × {len(texto.columns)} columnas · "
            f"estas son 6 filas reales del archivo.\\normalsize\n\n".replace(",", ".")
        )
        partes.append("\\footnotesize\n")
        partes.append("\\begin{xltabular}{\\linewidth}{@{}p{4.3cm} " + "Y " * N_FILAS + "@{}}\n")
        encabezado = ("\\rowcolor{azuloscuro}\\hdr{Columna} & "
                      + " & ".join(f"\\hdr{{fila {k}}}" for k in range(1, N_FILAS + 1)) + " \\\\\n")
        partes.append(encabezado + "\\endfirsthead\n")
        partes.append(encabezado + "\\endhead\n")
        for k, col in enumerate(texto.columns):
            fondo = "\\rowcolor{azulclaro}" if k % 2 == 0 else ""
            celdas = " & ".join(valor_tex(v) for v in muestra[col])
            partes.append(f"{fondo}{nombre_col_tex(col)} & {celdas} \\\\\n")
        partes.append("\\end{xltabular}\n\\normalsize\n")

        avisos = [(c, AVISOS_COLUMNAS_NUEVAS[(archivo, c)]) for c in texto.columns if (archivo, c) in AVISOS_COLUMNAS_NUEVAS]
        if avisos:
            partes.append("\n\\begin{alertabox}[Columnas nuevas de esta base]\n\\begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]\n")
            for c, aviso in avisos:
                partes.append(f"\\item {nombre_col_tex(c)}: {esc(aviso)}\n")
            partes.append("\\end{itemize}\n\\end{alertabox}\n")

    partes.append("\n\\end{document}\n")
    return "".join(partes), resumen


def compilar() -> None:
    exe = shutil.which("tectonic") or str(Path.home() / "AppData/Local/Programs/tectonic/tectonic.exe")
    r = subprocess.run([exe, "-X", "compile", "--keep-logs", TEX.name], cwd=AQUI, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print((r.stdout + r.stderr)[-1500:])
    if r.returncode != 0:
        sys.exit("Falló la compilación con tectonic")


def verificar(resumen) -> int:
    """Abre el PDF y comprueba que los valores de la muestra están, tal cual, en el texto."""
    import pypdf

    lector = pypdf.PdfReader(PDF)
    texto_pdf = re.sub(r"\s+", "", " ".join(p.extract_text() or "" for p in lector.pages))
    errores = 0
    for n, archivo, _, _, filas in resumen:
        texto = pd.read_csv(V3 / archivo, dtype=str, keep_default_na=False, na_values=[], low_memory=False)
        faltan = 0
        for i in filas:
            for v in texto.iloc[i]:
                # Se revisa palabra por palabra (al envolverse en celdas, el texto extraído mezcla las líneas
                # de columnas vecinas); de las palabras muy largas se revisan solo los primeros 8 caracteres.
                for palabra in v.split():
                    token = palabra if len(palabra) <= 14 else palabra[:8]
                    if token not in texto_pdf:
                        faltan += 1
                        if faltan <= 3:
                            print("  no encontrado en el PDF:", archivo, repr(palabra[:40]))
        if faltan:
            errores += faltan
            print(f"ERROR {archivo}: {faltan} valores no aparecen en el PDF")
    print("Páginas del PDF:", len(lector.pages))
    return errores


def main() -> int:
    tex, resumen = construir()
    TEX.write_text(tex, encoding="utf-8")
    for n, archivo, filas_csv, cols, _ in resumen:
        print(f"{n:3s} {archivo:34s} {filas_csv:>7} filas x {cols:>2} cols")
    compilar()
    errores = verificar(resumen)
    print("OK" if not errores else f"{errores} errores")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
