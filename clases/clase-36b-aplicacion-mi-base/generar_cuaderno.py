"""Genera Clase 36b - Mi Base - Abrir y Mirar - Clase.ipynb.

Fuente de verdad del cuaderno: no editar el .ipynb a mano, editar acá y regenerar.
Uso:  python generar_cuaderno.py
"""
from pathlib import Path
from urllib.parse import quote

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

CARPETA = Path(__file__).resolve().parent
SALIDA = CARPETA / "Clase 36b - Mi Base - Abrir y Mirar - Clase.ipynb"

RAW = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/"


def link(ruta):
    return RAW + quote(ruta)


# (n° del menú, nombre, ruta dentro de datos-compartidos, aviso de peso)
BASES = [
    (1, "Empleabilidad e ingresos por carrera (SIES)", "01_sies_empleabilidad/Buscador_Empleabilidad_ingresos_2025_2026_SIES.csv", ""),
    (2, "Puntajes de corte por carrera — Admisión 2026 (DEMRE)", "02_demre_admision/ADM2026_INDICADORES_POR_CARRERA_PROMEDIO_OBLIGATORIAS_20260116.csv", ""),
    (3, "SIMCE 2° medio 2025, por establecimiento", "03_simce_2m/simce2m2025_rbd_final.csv", ""),
    (4, "SIMCE 2° medio 2025, por comuna", "03_simce_2m/simce2m2025_comuna_final.csv", ""),
    (5, "Matrícula de estudiantes por establecimiento 2025 (Mineduc)", "05_mineduc_matricula/20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv", ""),
    (6, "Subvenciones a establecimientos 2025", "06_subvenciones/20260421_Detalle Subvenciones 2025_20240520.csv", "⏳ pesada (~30 MB)"),
    (7, "Siniestros de tránsito 2020-2025 (CONASET), Región Metropolitana", "07_conaset/CONASET_siniestros-transito-RM_2020-2025.csv", "⏳ pesada (~45 MB)"),
    (8, "Precios de alimentos al consumidor 2025 (ODEPA)", "08_odepa/ODEPA_precios-consumidor_2025.csv", "⏳ pesada (~60 MB)"),
    (9, "Estadísticas hospitalarias 2024", "09_salud/Estadísticas Hospitalarias Año 2024.csv", ""),
]

# Base elegida → equipos (nombre y primer apellido). Estado del Form al 2026-10-06.
EQUIPOS = [
    ("🚗 Siniestros de tránsito (CONASET)", "Santino García y Tomás Díaz · Benjamín Mejías · Felipe Román"),
    ("🎓 Puntajes de corte (DEMRE)", "Maura Muñoz y Simón Abrahams · Eduardo Pacco y Damián Flores · Diego Peña y Felipe Aravena · Vicente Benítez y Vicente Narváez · Martín Sánchez"),
    ("💼 Empleabilidad e ingresos (SIES)", "Francisca Parra y Julián Sandoval · Sebastián Ulloa"),
    ("🏥 Estadísticas hospitalarias", "Francisco Vega y Héctor Vergara · Alex Saravia y Diego Donoso"),
    ("📝 SIMCE 2° medio por establecimiento", "Cristóbal Muñoz y Luckas Letelier"),
    ("🏫 Matrícula por establecimiento", "Diego Vargas y Benjamín Díaz"),
]

cells = []


def md(texto):
    cells.append(new_markdown_cell(texto.strip("\n")))


def code(texto):
    cells.append(new_code_cell(texto))


# ───────────────────────── Portada ─────────────────────────
md("""
# 🐍 Clase 36b — Mi base: abrir y mirar

**Curso:** 4to medio  |  **Duración:** ~80 min  |  **Plataforma:** Google Colab

---
""")

md("""
## 🎯 Objetivo de hoy

Aplicar lo que aprendimos en la Clase 36 (abrir y mirar con pandas) a la base de datos de tu proyecto: abrirla, describir con tus palabras qué contiene y dejar escrita una primera pregunta que te gustaría responder con ella.

## 🔎 ¿Para qué sirve?

> Es el primer paso real de tu proyecto de cierre: antes de decidir qué investigar, hay que saber qué hay dentro de tu base. Lo que escribas hoy es la materia prima para el 13-oct.

**Cómo funciona este cuaderno:** lee, escribe el código en las celdas vacías y responde en las celdas 📝 **con tus palabras** — esas respuestas cuentan para tu nota de proceso.
""")

# ───────────────────────── Rúbrica ─────────────────────────
md("""
---

## 📋 Cómo se evalúa (recordatorio)

El proyecto de cierre se traduce en **una sola nota** (vale doble en el promedio semestral), armada con 4 partes:

| Parte | Peso | Qué mide |
|---|---|---|
| 📓 Producto — Colab narrado | 35% | Análisis correcto y razonamiento explicado en texto, de corrido |
| 🎤 Presentación ante dirección | 20% | Claridad del hallazgo, evidencia y qué NO se puede concluir |
| 🔍 Defensa técnica — código intervenido | 30% | Explicar tu propio código y corregir errores metidos a propósito |
| 📒 Proceso — bitácora e hitos | **15%** | Avance real clase a clase, con evidencia |

### 👉 Este cuaderno cuenta para **Proceso (15%)**

Se revisa que:

1. ✅ **El código corre** de arriba hacia abajo sobre tu base.
2. ✅ **Cada pregunta tiene su respuesta escrita en markdown, con tus palabras.** No basta con que el código muestre el resultado: hay que explicar qué significa.
3. ✅ **La bitácora de hoy está completa** (al final del cuaderno).
4. ✅ **Lo entregas hoy** en Classroom.

> 🚫 **Sobre la IA:** el código y los textos de este cuaderno se escriben sin IA. Es el código que vas a tener que explicar en la Defensa técnica.
""")

# ───────────────────────── Equipos y bases ─────────────────────────
filas_equipos = "\n".join(f"| {base} | {equipos} |" for base, equipos in EQUIPOS)
md(f"""
---

## 👥 Equipos y bases

| Base elegida | Equipos |
|---|---|
{filas_equipos}

¿Tu nombre no aparece? Elige del menú de abajo la base que más te interese y avísale al profe cuál elegiste. Hoy trabajas igual que el resto.
""")

# ───────────────────────── Links ─────────────────────────
filas_links = "\n".join(
    f"| {n} | {nombre}{(' ' + aviso) if aviso else ''} | `{link(ruta)}` |"
    for n, nombre, ruta, aviso in BASES
)
md(f"""
---

## 🔗 Links de las bases

Copia el link de **tu** base y pégalo entre comillas dentro de `pd.read_csv(...)`.

| # | Base | Link |
|---|---|---|
{filas_links}

Si tu base no abre bien a la primera, mira qué ves y qué le falta:

| Qué ves | Qué falta | Se arregla con |
|---|---|---|
| Todo en una sola columna (`tabla.shape` da `(filas, 1)`), o un `ParserError` | el separador | `sep=";"` |
| `UnicodeDecodeError`, o tildes raras (`Ã³`, `�`) | el encoding | `encoding="latin-1"` |
| Columnas llamadas `Unnamed: 0`, `Unnamed: 1`... y un título en las primeras filas | la fila donde están los nombres | `header=2` |
""")

md("""
### 💡 `sep=` — todo quedó en una sola columna

Un CSV es texto con valores separados por un carácter. Lo normal es la coma, pero algunos archivos usan punto y coma (`;`). Si pandas espera comas y el archivo trae `;`, **no separa nada**: ves una columna enorme con los nombres pegados (`ANYO_PROCESO;CODIGO_CARRERA;...`) o un error como `ParserError: Expected 1 fields in line 6, saw 2`.

```python
tabla = pd.read_csv("link", sep=";")
```
""")

md("""
### 💡 `encoding=` — error al leer o letras raras

Un archivo guarda las letras con una "tabla de códigos" llamada *encoding*. pandas asume `utf-8`. Si el archivo se guardó con otra, aparece un `UnicodeDecodeError: 'utf-8' codec can't decode byte...` o las tildes salen mal (`Ã³` en vez de `ó`). El más común en archivos antiguos es `latin-1`.

```python
tabla = pd.read_csv("link", encoding="latin-1")
```

⚠️ No lo pongas "por si acaso": si el archivo **ya era** `utf-8` y le pones `latin-1`, ahí sí las letras salen rotas.
""")

md("""
### 💡 `header=` — columnas `Unnamed` y títulos arriba

pandas supone que la **primera fila** del archivo trae los nombres de las columnas. Algunos archivos traen antes un título o filas vacías. `header=2` significa: *"los nombres de las columnas están en la fila 2 del archivo, contando desde 0"* (la tercera línea).

```python
tabla = pd.read_csv("link", header=2)
```

Cómo averiguar el número: mira `tabla.head()` sin `header` y busca la fila donde aparecen los nombres reales de las columnas. El número que pandas muestra a la izquierda de esa fila **más 1** es tu `header`. Pruébalo y revisa con `tabla.head()`.

*Este parámetro no lo vimos en la Clase 36: es nuevo y solo lo necesitas si tu base lo pide.*
""")

md("""
### ⏳ Si tu base es pesada

Las bases de 30 a 60 MB tardan unos segundos en descargarse. Ábrela **una sola vez**: la variable `tabla` queda guardada en memoria. Para probar cosas distintas usa otras celdas que partan de `tabla`, sin volver a ejecutar la celda del `read_csv`.
""")

md("""
### 🆘 Cómo se abre cada base

Si ya probaste todo y no abre, esta es la tabla completa:

| Base | Cómo abrirla |
|---|---|
| Siniestros de tránsito, Empleabilidad (SIES), Matrícula, Subvenciones, Precios (ODEPA) | solo el link: `pd.read_csv("link")` |
| Puntajes de corte (DEMRE) | `pd.read_csv("link", sep=";")` |
| SIMCE (por establecimiento y por comuna) | `pd.read_csv("link", sep=";", encoding="latin-1")` |
| Estadísticas hospitalarias | `pd.read_csv("link", header=2)` |
""")

# ───────────────────────── Preparación ─────────────────────────
md("""
---

### 🔧 Preparación

Ejecuta esta celda antes de empezar — instala pandas en tu sesión de Colab, por si acaso.
""")
code("!pip install pandas")

# ───────────────────────── Torpedo ─────────────────────────
md("""
---

## 🧾 Repaso rápido de la Clase 36

Esto es todo lo que vimos. Tenlo a mano mientras trabajas en tu base.

| Quiero... | Escribo | Qué entrega |
|---|---|---|
| Traer pandas | `import pandas as pd` | Deja `pd` listo para usar |
| Abrir un CSV | `tabla = pd.read_csv("link")` | La tabla completa, guardada en `tabla` |
| Abrir un CSV que no se lee bien | `pd.read_csv("link", sep=";", encoding="latin-1")` | La tabla bien separada y con las tildes correctas |
| 🆕 Abrir uno con títulos arriba | `pd.read_csv("link", header=2)` | La tabla con los nombres de columna en su lugar |
| Ver las primeras filas | `tabla.head()` | Las 5 primeras filas |
| Saber el tamaño | `tabla.shape` | `(filas, columnas)`, en ese orden |
| Ver los nombres de las columnas | `list(tabla.columns)` | Una lista con los nombres exactos |
| Elegir columnas | `tabla[["col1", "col2"]]` | Una tabla nueva con solo esas columnas |
| Contar vacíos de una columna | `tabla["col"].isna().sum()` | Un número |
| Contar vacíos de varias columnas | `tabla[["col1", "col2"]].isna().sum()` | Un número por columna |

#### ⚠️ Errores típicos a evitar

| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Usar corchete simple para varias columnas: `tabla["col1", "col2"]` | `KeyError` | Doble corchete: `tabla[["col1", "col2"]]` |
| Escribir `.shape()` con paréntesis | `TypeError` | `.shape` va sin paréntesis |
| Escribir el nombre de una columna a ojo (mayúsculas, tildes, espacios, símbolos como `°`) | `KeyError` | Copiar el nombre exacto desde `list(tabla.columns)` |
""")

# ───────────────────────── Markdown: encabezado en vivo ─────────────────────────
md("""
---

## ✍️ Markdown: escribamos juntos el encabezado de tu proyecto

Además de código, tus respuestas van en **celdas de texto** (markdown). Lo vamos a aprender armando **entre todos** el encabezado de tu proyecto: el nombre, la base de datos, los integrantes y por qué la elegiste. Cada línea usa una herramienta distinta: el profe escribe en pantalla y tú escribes lo tuyo a la vez.

**Lo básico de una celda de texto:**

- **Crear una:** botón **+ Texto** (arriba a la izquierda).
- **Escribir:** doble clic sobre la celda.
- **Ver el resultado:** `Shift + Enter`. Para volver a editar, doble clic de nuevo.

### 🧰 Las herramientas, una por línea del encabezado

| Paso | Quiero... | Herramienta | Escribo | Se ve así |
|---|---|---|---|---|
| 1 | Poner el nombre del proyecto | **título** | `# Proyecto: Mi nombre` | un texto grande, como el título de este cuaderno |
| 2 | Decir qué base uso | **negrita** | `**Base de datos:** CONASET` | **Base de datos:** CONASET |
| 3 | Listar a los integrantes | **lista** | `- Nombre Apellido` (una línea por persona) | una lista con viñetas |
| 4 | Explicar por qué elegí esa base | **cita** | `> Esta base me interesa porque...` | un párrafo con una barra al costado |
| 5 | Separar el encabezado del resto | **línea** | `---` | una línea horizontal |

Y dos herramientas más para tus respuestas de hoy:

| Quiero... | Escribo | Se ve así |
|---|---|---|
| Nombrar una columna o un comando | `` `nombre_columna` `` | `nombre_columna` |
| Dar énfasis suave | `*esto es clave*` | *esto es clave* |

💡 Para separar párrafos, deja **una línea en blanco** entre ellos. Y si escribes un signo peso, ponle una barra antes (`\\$5.000`); si no, la celda se desordena.
""")

md("""
### 🧑‍💻 Escribamos el encabezado juntos

Haz doble clic en la celda de abajo y vamos línea por línea, reemplazando los `...` con lo tuyo (agrega o borra viñetas de integrantes según haga falta). Cuando termines, `Shift + Enter` para ver cómo quedó.
""")

md("""
# Proyecto: ...

**Base de datos:** ...

**Integrantes:**

- ...
- ...

**¿Por qué esta base?**

> ...

---
""")

# ───────────────────────── Trabajo en tu base ─────────────────────────
md("""
---

## 🔍 Trabajo en tu base

Cada paso tiene una consigna, una celda de código y una celda 📝 para responder con tus palabras. Los pasos usan la variable `tabla` que dejas en el Paso 1.
""")

md("""
### Paso 1 · Abre tu base

1. Pega el link de tu base entre comillas dentro de `pd.read_csv(...)` y guarda el resultado en una variable llamada `tabla`.
2. Muestra sus primeras filas.

Si no abre bien a la primera, usa las pistas de más arriba.
""")
code("# Paso 1 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 1

*(doble clic para editar y escribir)*

- **¿Abrió bien a la primera?**
- **Si no abrió bien: ¿qué síntoma viste y qué parámetro lo arregló?**
- **Algo que te llamó la atención al ver las primeras filas:**
""")

md("""
### Paso 2 · Dimensiones y columnas

Muestra cuántas filas y columnas tiene tu base, y la lista con los nombres de todas sus columnas.
""")
code("# Paso 2 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 2

- **Mi base tiene ... filas y ... columnas.**
- **Cada fila representa:** (completa la frase con tus palabras: ¿una persona?, ¿un evento?, ¿un lugar?, ¿una medición?)
- **Las columnas que más me llaman la atención son ... y creo que significan:**
""")

md("""
### Paso 3 · Elige las columnas que importan

Quédate con **3 a 6 columnas** que tengan relación con lo que te interesó investigar (lo que escribiste en el formulario). Guárdalas en una variable llamada `columnas_relevantes` y muestra sus primeras filas.
""")
code("# Paso 3 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 3

- **Columnas elegidas y por qué:**
- **Una columna que me habría gustado que existiera y no está:**
- **¿Qué tan bien responde esta base a lo que me interesaba?** (por completo / a medias / poco, y por qué)
""")

md("""
### Paso 4 · Cuenta los vacíos

Cuenta cuántos vacíos tiene cada una de tus `columnas_relevantes`.

> 💡 **Pista — vacíos que pandas no cuenta:** `.isna()` solo cuenta como vacío lo que está **realmente** vacío. Si en las filas ves marcas como `s/i`, `-`, `*` o celdas que parecen vacías pero traen un espacio, pandas **no** las cuenta. No las arregles hoy: anótalas en tu respuesta y las resolvemos la próxima clase.
""")
code("# Paso 4 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 4

- **Columna con más vacíos y cuántos tiene:**
- **¿Pueden afectar lo que quieres averiguar? ¿Por qué?**
- **Algo raro que notaste en los datos (valores que parecen vacíos pero pandas no los cuenta):**
""")

md("""
### Paso 5 · Y ahora, ¿qué pregunta quieres responder?

Ahora que sabes lo que hay en tu base —qué representa cada fila, qué columnas tiene y qué le falta—, escribe una **primera pregunta** que te gustaría responder con estos datos. Es un borrador: el 13-oct la afinamos.
""")
md("""
#### 📝 Respuesta — Paso 5

- **Pregunta (borrador):**
- **Columnas que necesitaría para responderla:**
""")

# ───────────────────────── Bitácora y entrega ─────────────────────────
md("""
---

## 📒 Bitácora

> Se completa al cerrar la sesión. Es lo que la rúbrica de Proceso revisa.

**Sesión 06-oct — Mi base: abrir y mirar**
- Qué avanzamos hoy:
- Qué pensamos hacer la próxima clase:
""")

md("""
---

## 📤 Entrega

Antes de irte:

1. Ejecuta todo de arriba hacia abajo: menú **Entorno de ejecución → Ejecutar todo**. Revisa que no quede ningún error en rojo.
2. Revisa que todas las celdas 📝 y la bitácora tengan tu respuesta.
3. En la tarea de Google Classroom de hoy, presiona **Entregar**.
""")

# ───────────────────────── Armado ─────────────────────────
for i, celda in enumerate(cells, start=1):
    celda["id"] = f"c{i:02d}"

nb = new_notebook(cells=cells)
nb.metadata["colab"] = {"provenance": []}
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}

nbformat.validate(nb)
nbformat.write(nb, SALIDA)
print("Generado:", SALIDA.name, "—", len(cells), "celdas")
