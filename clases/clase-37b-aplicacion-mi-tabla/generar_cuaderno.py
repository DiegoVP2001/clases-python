"""Genera Clase 37b - Mi Tabla - Limpiar y Preguntar (Clase + Solucionario).

Fuente de verdad del cuaderno: no editar los .ipynb a mano, editar acá y regenerar.
Uso:  python generar_cuaderno.py
(El PDF de muestras lo genera generar_muestra_pdf.py; este script no lo toca.)
"""
import base64
from pathlib import Path
from urllib.parse import quote

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

CARPETA = Path(__file__).resolve().parent
CLASES = CARPETA.parent
SALIDA = CARPETA / "Clase 37b - Mi Tabla - Limpiar y Preguntar - Clase.ipynb"
SALIDA_SOL = CARPETA / "Clase 37b - Mi Tabla - Limpiar y Preguntar - Solucionario.ipynb"
FOTO = CLASES / "clase-35-listas" / "foto_lun.png"

REPO = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/"
RAW = REPO + "clases-octubre/datos-compartidos-v2/"
LINK_GUAGUAS = REPO + "clases-octubre/datos-compartidos/bbdd_guaguas.csv"
LINK_DICCIONARIO = (
    "https://github.com/DiegoVP2001/clases-python/blob/master/clases/clase-36b-aplicacion-mi-base/"
    + quote("Clase 36b - Mi Base - Diccionario de Columnas.pdf")
)
MUESTRA = "Clase 37b - Mi Tabla - Muestra de las Bases.pdf"


def link(ruta):
    return RAW + quote(ruta)


# (n° del menú, nombre, archivo dentro de datos-compartidos-v2, aviso de peso)
BASES = [
    (1, "Empleabilidad e ingresos por carrera (SIES)", "01_sies.csv", ""),
    (2, "Puntajes de corte por carrera — Admisión 2026 (DEMRE)", "02_demre.csv", ""),
    (3, "SIMCE 2° medio 2025, por establecimiento", "03_simce_establecimiento.csv", ""),
    (4, "SIMCE 2° medio 2025, por comuna", "04_simce_comuna.csv", ""),
    (5, "Matrícula de estudiantes por establecimiento 2025 (Mineduc)", "05_matricula.csv", ""),
    (6, "Subvenciones a establecimientos 2025", "06_subvenciones.csv", "⏳ pesada (~29 MB)"),
    (7, "Siniestros de tránsito 2020-2025 (CONASET), Región Metropolitana", "07_conaset_rm.csv", "⏳ pesada (~44 MB)"),
    (8, "Precios de alimentos al consumidor 2025 (ODEPA), Región Metropolitana", "08a_odepa_consumidor.csv", "⏳ pesada (~10 MB)"),
    ("9a", "Estadísticas hospitalarias 2024 — mensual (si quieres ver mes a mes)", "09a_hospitalarias_mensual.csv", ""),
    ("9b", "Estadísticas hospitalarias 2024 — anual (si quieres comparar hospitales)", "09b_hospitalarias_anual.csv", ""),
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


# ───────────────────────── Portada + foto del LUN ─────────────────────────
md("""
# 🐍 Clase 37b — Mi tabla lista y mi pregunta

**Curso:** 4to medio  |  **Duración:** ~77 min  |  **Plataforma:** Google Colab

---
""")

foto_b64 = base64.b64encode(FOTO.read_bytes()).decode("ascii")
portada_foto = new_markdown_cell(
    "## 📰 De dónde partimos\n\n"
    "Con datos públicos como los de tu base se armó una noticia de circulación nacional: "
    "*cuánto ganan los ingenieros civiles industriales según su universidad de egreso*.\n\n"
    "![La nota del LUN — Cuánto ganan los ingenieros civiles industriales según su universidad de egreso](attachment:foto_lun.png)\n\n"
    "Ese es el tipo de producto que buscamos: una pregunta clara, respondida con datos limpios y bien entendidos, "
    "con un impacto real para Chile. Hoy das el paso que lo hace posible: **dejar tu tabla lista y afinar tu pregunta**."
)
portada_foto["attachments"] = {"foto_lun.png": {"image/png": foto_b64}}
cells.append(portada_foto)

md("""
## 🎯 Objetivo de hoy

Aplicar lo que aprendimos en la Clase 37 (limpiar una columna a número y descartar filas sucias) a las columnas de tu base: decidir **qué línea de limpieza necesita cada una mirándola primero**, dejar una tabla lista y afinar tu pregunta para el proyecto.

## 🔎 ¿Para qué sirve?

> Una columna de números escrita como texto no se puede promediar ni comparar: si la conviertes sin mirar, puedes terminar con puntajes cien veces más grandes o con la mitad de los datos perdidos, sin ningún aviso. Lo que hagas hoy es la tabla sobre la que se construye tu análisis y tu presentación ante dirección.

**Cómo funciona este cuaderno:** trae todo lo que necesitas, aunque hayas faltado a la Clase 36b o a la 37. Lee, escribe el código en las celdas vacías y responde en las celdas 📝 **con tus palabras** — esas respuestas cuentan para tu nota de proceso.
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
lineas_links = []
for n, nombre, ruta, aviso in BASES:
    lineas_links.append(f"# {n} · {nombre}{(' ' + aviso) if aviso else ''}")
    lineas_links.append(f'# "{link(ruta)}"')
    lineas_links.append("")
celda_links = "\n".join(lineas_links).rstrip()

md(f"""
---

## 🔗 Links de las bases

Copia el link de **tu** base —con sus comillas— y pégalo dentro de `pd.read_csv(...)`. Están en la celda de abajo, comentados, así que ejecutarla no hace nada.
""")

code(celda_links)

md(f"""
📖 **Diccionario de Columnas** (qué significa cada columna de cada base): [abrir el PDF]({LINK_DICCIONARIO})

📊 **Muestra de las bases (PDF):** el archivo **{MUESTRA}** está en Classroom, junto a este cuaderno. Tiene una página por base con todas sus columnas y 6 filas reales, tal como vienen escritas en el archivo. Lo vas a usar en el Paso 2.

✅ **Tu base ya viene preparada**: se abre con `pd.read_csv(link)`. Las bases de 10 a 44 MB tardan unos segundos; ábrela **una sola vez** y sigue trabajando con la variable `tabla`, sin volver a ejecutar esa celda.
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

## 🧾 Repaso rápido

### ¿Faltaste a la Clase 36b? Abrir y mirar una base

| Quiero... | Escribo | Qué entrega |
|---|---|---|
| Traer pandas | `import pandas as pd` | Deja `pd` listo para usar |
| Abrir un CSV | `tabla = pd.read_csv("link")` | La tabla completa, guardada en `tabla` |
| Ver las primeras filas | `tabla.head()` | Las 5 primeras filas |
| Saber el tamaño | `tabla.shape` | `(filas, columnas)`, en ese orden |
| Ver los nombres de las columnas | `list(tabla.columns)` | Una lista con los nombres exactos |
| Elegir columnas | `tabla[["col1", "col2"]]` | Una tabla nueva con solo esas columnas |
| Contar vacíos de varias columnas | `tabla[["col1", "col2"]].isna().sum()` | Un número por columna |

### Clase 37: dejar una columna lista

| Concepto | Ejemplo |
|---|---|
| Leer con cuidado | `pd.read_csv(archivo, dtype={"col": "str"})` |
| Sacar los espacios sobrantes | `columna.str.strip()` |
| Arreglar el separador (según lo que veas) | miles `2.908` → `columna.str.replace(".", "", regex=False)` · coma decimal `607,5` → `columna.str.replace(",", ".", regex=False)` · punto decimal `0.65` → nada |
| Convertir a número real | `pd.to_numeric(columna, errors="coerce")` |
| Descartar filas que no se pudieron limpiar | `tabla[tabla["col"].notna()]` |

> 🔁 **Ojo con los nombres:** en estos ejemplos `col`, `col1` y `col2` son marcadores. Debes **reemplazarlos por los nombres de tus columnas**, tal como aparecen en `list(tabla.columns)`.
>
> 📒 **Antes de seguir, revisa tu cuaderno de proceso anterior (el de la Clase 36b):** ahí dejaste tus columnas elegidas y tu pregunta borrador, y hoy partes desde ese trabajo.
""")

md(f"""
### 📋 Los códigos de la Clase 37

La celda de abajo reúne el código de la Clase 37 sobre la columna `n` de la tabla de nombres de guaguas (`n` es la cantidad de bebés con ese nombre; algunos valores vienen como `" 15 "` o `"2.908"`). Cada bloque trae **solo la línea nueva** y parte de la columna que construyó el bloque anterior: `n` → `n_sin_espacios` → `n_sin_puntos` → `cantidad_guaguas`.

Es una **referencia para que la analices bien, caso a caso**: fíjate qué hace cada línea, de qué columna parte y qué columna nueva deja. Lo que corresponda a tu base lo decides tú mirando tus datos (se explica paso a paso más abajo).
""")

code(f'''# ═══════════ Clase 37 · limpiar una columna a número ═══════════
# Ejemplo: la columna "n" de bbdd_guaguas.csv (cuántas guaguas tuvo cada nombre).
# Cada bloque parte de la columna que dejó el bloque anterior.

# import pandas as pd

# ── 💡 1. Leer con cuidado ──  (parte de: "n", leída como texto)
# tabla = pd.read_csv("{LINK_GUAGUAS}", dtype={{"n": "str"}})

# ── 💡 2. Sacar los espacios sobrantes ──  ("n" → "n_sin_espacios")
# tabla["n_sin_espacios"] = tabla["n"].str.strip()

# ── 💡 3. Arreglar el separador ──  ("n_sin_espacios" → "n_sin_puntos")
# La línea depende de cómo vengan los valores de la columna:
#   · punto de miles (2.908 es 2908):
# tabla["n_sin_puntos"] = tabla["n_sin_espacios"].str.replace(".", "", regex=False)
#   · si tu columna usa coma decimal (607,5 es 607.5):
# tabla["n_sin_puntos"] = tabla["n_sin_espacios"].str.replace(",", ".", regex=False)
#   · si tu columna usa punto decimal (0.65 es 0.65): no hay línea que escribir, usa tal cual "n_sin_espacios"

# ── 💡 4. Convertir a número real ──  ("n_sin_puntos" → "cantidad_guaguas")
# tabla["cantidad_guaguas"] = pd.to_numeric(tabla["n_sin_puntos"], errors="coerce")

# ── 💡 5. Descartar filas que no se pudieron limpiar ──  (se queda con las filas con número)
# print("Filas antes:", tabla.shape[0])
# tabla = tabla[tabla["cantidad_guaguas"].notna()]
# print("Filas después:", tabla.shape[0])

# ── 🔗 La cadena completa en una sola línea (bloques 2 + 3 + 4) ──
# tabla["cantidad_guaguas"] = pd.to_numeric(tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce")''')

# ───────────────────────── Plan de hoy ─────────────────────────
md("""
---

## 🧭 Plan de hoy

Hoy dejas tu tabla lista en 6 pasos. En cada uno encontrarás primero **lo que necesitas saber para ese paso** y luego lo que debes hacer.

| Paso | Qué harás | Para qué |
|---|---|---|
| **1** | Abrir tu base y elegir tus columnas: unas para **comparar** (base) y otras para **medir** | Saber con qué vas a trabajar |
| **2** | **Mirar** esas columnas antes de tocarlas: su tipo (`.dtype`) y cómo vienen escritos sus valores | No limpiar a ciegas |
| **3** | **Decidir** la línea de limpieza de cada columna, **convertirla** a número y **comprobar** que quedó bien | Tener números reales y confiables |
| **4** | **Descartar** las filas que no se pudieron limpiar y contar cuántas se perdieron | Saber cuánto dato te queda |
| **5** | Dejar tu **tabla lista** y describirla con tus palabras | Tener la base de tu análisis |
| **6** | Afinar tu **pregunta** con 2 filtros | Saber qué puedes responder con tus datos |

Los pasos 2 y 3 siguen un método de cuatro letras: **A. Mirar → B. Decidir → C. Convertir → D. Comprobar**.

Cada paso tiene una consigna, una celda de código y una celda 📝 para responder con tus palabras. Las preguntas no piden copiar el resultado: piden **explicar qué descubriste y por qué decidiste lo que decidiste**.
""")

md("""
---

## 🔍 Trabajo en tu base
""")

md("""
### Paso 1 · Abre tu base y elige tus columnas

**Lo que necesitas saber: hay dos tipos de columnas.**

| Tipo | Qué son | Qué haces con ellas |
|---|---|---|
| 🧱 **Columnas base** (sugerencia) | Las que identifican o agrupan cada fila: año, mes, sexo, región, comuna, universidad, carrera, establecimiento. Suelen ser las primeras de la tabla | **No se limpian.** Las conservas porque te permiten comparar |
| 📏 **Columnas a medir** (1 a 3) | Los números que quieres analizar | Son las **únicas** que pasan por el método A-B-C-D |

En total, elige entre **3 y 6 columnas**.

**Lo que debes hacer:**

1. Abre tu base con `pd.read_csv(...)`, guárdala en `tabla` y muestra sus primeras filas y sus dimensiones.
2. Muestra la lista con los nombres exactos de todas las columnas y cópialos desde ahí (en SIES, por ejemplo, hay un espacio que no se puede tipear). Elige tus **columnas base** y tus **columnas a medir**.
""")
code("# Paso 1 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 1

- **¿Qué representa una fila de tu base?**
- **Mis columnas base son ..., y cada una me permite comparar ... Sin ellas no podría decir ...**
- **Mis columnas a medir son ... y espero encontrar ...**
""")

md("""
### Paso 2 · A. Mira antes de limpiar

**Lo que necesitas saber:** Python no sabe si un `.` o una `,` dentro de un texto es separador de miles o decimal: **lo decide cada base**. El mismo `3.129` puede ser tres mil ciento veintinueve (guaguas) o tres coma ciento veintinueve (egresos por día en Hospitalarias). Por eso **primero se mira, después se limpia**.

- Con `tabla["col"].dtype` ves de qué tipo es la columna. **Si es `float64` o `int64`, ya es número: no hay nada que limpiar.** Si dice `str` u `object`, es **texto** y hay que seguir con el Paso 3.
- Con `tabla["col"].head(10)` ves cómo vienen escritos sus valores.
- Pregúntate siempre: **¿el valor tiene sentido como cantidad real?**

**Lo que debes hacer:** para cada columna a medir, muestra su `.dtype` y sus primeros 10 valores. Luego abre la página de **tu** base en el PDF de muestras y compara.
""")
code("# Paso 2 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 2

- **En el PDF de mi base, ¿qué columnas parecen número pero vienen con coma, con puntos o con `s/i`?** Copia un valor de cada una:
- **¿Coincide lo que ves en el PDF con el `.dtype` que mostró Python? ¿Hay alguna columna que ya sea número y no necesite limpieza?**
- **¿Qué te dice ese valor sobre lo que hay que arreglar? ¿Tiene sentido como cantidad real?**
""")

md("""
### Paso 3 · B, C y D · Decide, convierte y comprueba

**Lo que necesitas saber:**

- **B. Decidir.** Elige la línea según lo que viste en el Paso 2:

| Veo en la columna… | Significa | Línea de limpieza |
|---|---|---|
| `.dtype` = `float64` o `int64` | ya es número | **nada** |
| `607,5` o `85,3` | la coma es el decimal | `.str.strip().str.replace(",", ".", regex=False)` |
| `0.65` o `3.2` (texto) | el punto es el decimal | `.str.strip()`; **no quitar el punto** |
| `2.908` o `136.818.693` (texto) | el punto separa miles | `.str.strip().str.replace(".", "", regex=False)` |
| `s/i` o vacío | dato que falta | nada extra: `to_numeric(errors="coerce")` lo deja `NaN` |

- **C. Convertir.** Aplica la línea y envuélvela en `pd.to_numeric(..., errors="coerce")`, guardando el resultado en una **columna nueva**. Escribe **una línea por columna**: solo cambian el nombre de la columna y el de la columna nueva. Las columnas que son texto se leen con `dtype={"col": "str"}` en el `read_csv`.
- **D. Comprobar.** Asegúrate de que el número está **bien**, no solo de que "salió": compara la columna original con la nueva, mira el mínimo, el máximo y el promedio con `.describe()`, y cuenta los `NaN` que quedaron.

**Dos ejemplos de cordura:**

- `2.908` en una columna de guaguas es **miles** (2908). `3.129` en `Egresos_por_dia` es **decimal** (el máximo de toda esa columna es 29,567). Lo que desambigua es el `.dtype` y si el valor tiene sentido.
- Quitar el punto "por costumbre" es peligroso: en SIES un `0.65` pasaría a **65** (cien veces más) y nadie te avisa; en DEMRE un `607,5` pasaría a `NaN` (ese sí se nota al contar filas).

**Lo que debes hacer:**

1. **B y C:** elige la línea de cada columna que lo necesite y conviértela a número en una columna nueva.
2. **D:** muestra cada columna original junto a su versión numérica (`.head()`), y usa `.describe()` en las columnas numéricas. Cuenta cuántos `NaN` quedaron en cada columna nueva.
""")
code("# Paso 3 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 3

- **¿Qué línea elegiste para cada columna y por qué?** (qué viste que te hizo decidir):
- **¿Cómo sabes que el número está bien y no mal convertido?** Mira el mínimo, el máximo y el promedio de `.describe()`: ¿tienen sentido?
- **Si hubieras usado la línea de las guaguas (quitar el punto) sin mirar, ¿qué habría salido mal? ¿Se habría notado?**
""")

md("""
### Paso 4 · Descarta y cuenta lo perdido

**Lo que necesitas saber:** al convertir, algunas filas quedan en `NaN` (no tenían dato o no se pudieron arreglar). `.notna()` las deja fuera. Se usa **una vez por cada columna que limpiaste**. Una columna que ya era número no necesita limpieza, aunque puede tener vacíos naturales: los cuentas con `.isna().sum()`.

**Lo que debes hacer:** con `.notna()`, descarta las filas que quedaron vacías en cada columna que limpiaste. Muestra cuántas filas tenías antes, cuántas quedaron y cuántas se perdieron.
""")
code("# Paso 4 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 4

- **Filas antes: ... · después: ... · perdidas: ...**
- **¿Por qué se perdieron: eran vacíos reales, marcas como `s/i`, o un error de tu limpieza?**
- **¿Lo que quedó fuera podría cambiar lo que concluyas, o dejar fuera a alguien en tu análisis? ¿Por qué?**
""")

md("""
### Paso 5 · Tu tabla lista

**Lo que necesitas saber:** tu tabla lista combina las dos cosas que elegiste: tus columnas base (para comparar) y tus columnas limpias (los números a medir).

**Lo que debes hacer:** deja en una variable `tabla_lista` solo esas columnas, y muestra su `.shape` y sus primeras filas.
""")
code("# Paso 5 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 5

Completa:

> Mi tabla tiene ... filas, cada una es ..., y puedo comparar ... según ...

- **¿Qué descubriste hoy de tu base que no sabías al abrirla?**
""")

md("""
### Paso 6 · Mi pregunta (con 2 filtros)

**Lo que necesitas saber:** tu pregunta borrador está en tu cuaderno de la Clase 36b. Si faltaste, escribe una ahora.

**Lo que debes hacer:** pásala por **dos filtros**:

1. **¿Mis datos ya limpios la responden?** Es decir: ¿tengo las columnas y las filas que necesito?
2. **¿Es abierta?** Es decir: ¿no se responde con un sí o un no, y deja explicar un porqué?
""")
md("""
#### 📝 Respuesta — Paso 6

- **Pregunta candidata:**
- **¿Mis datos ya limpios la responden?** (qué columnas y cuántas filas me quedan):
- **¿Es abierta?**
- **Una pregunta que descarté y por qué:**
- **Mi pregunta elegida:**
- **¿Cómo cambió respecto al borrador de la 36b y qué la hizo cambiar?**
""")

# ───────────────────────── Bitácora y entrega ─────────────────────────
md("""
---

## 📒 Bitácora

> Se completa al cerrar la sesión. Es lo que la rúbrica de Proceso revisa.

**Sesión 19-oct — Mi tabla lista y mi pregunta**
- Qué avanzamos hoy:
- Qué pensamos hacer el martes 20 (Clase 38):
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


# ═════════════════════════ Solucionario (solo profesor) ═════════════════════════
LINK_EJEMPLO = link("02_demre.csv")

sol = []


def sol_md(texto):
    sol.append(new_markdown_cell(texto.strip("\n")))


def sol_code(texto):
    sol.append(new_code_cell(texto))


sol_md("""
# 🔒 Solucionario — Clase 37b: Mi tabla lista y mi pregunta

**Uso:** documento para el profesor. Muestra **a qué debería llegar cada estudiante al término de la clase**, usando una sola base de ejemplo: **Puntajes de corte (DEMRE)**, la más elegida con coma decimal. Cada equipo trabaja con la suya, así que sus respuestas serán distintas; lo que se mantiene es la estructura. El ejemplo incluye además una columna que **ya es número** (`MARGEN_P25_MENOS_ULTIMO`), para mostrar el caso «nada que limpiar».

---

## ¿Qué se revisa en cada parte? (Proceso, 15%)

| Parte | Una respuesta suficiente... |
|---|---|
| Paso 1 | abre su base, dice **qué representa una fila**, elige columnas base y a medir y **justifica** qué le permite comparar cada base |
| Paso 2 | mira `.dtype` y los valores de cada columna a medir y **los compara con el PDF de muestras**; distingue las que son texto de las que ya son número |
| Paso 3 | **elige la línea según lo que vio** (no una receta única), convierte, y comprueba con `.describe()` que el resultado tenga sentido |
| Paso 4 | descarta con `.notna()`, informa filas antes/después/perdidas y **explica por qué** se perdieron |
| Paso 5 | deja una tabla lista (base + limpias) y completa la frase con sus palabras |
| Paso 6 | pasa su pregunta por los **2 filtros**, descarta una y explica **cómo cambió** respecto al borrador de la 36b |
| Bitácora | completa las dos líneas, con algo concreto de hoy |
""")

sol_md(f"""
---

## 🔍 Trabajo en tu base — resuelto con DEMRE

Link usado como ejemplo:

`{LINK_EJEMPLO}`
""")

sol_md("### Paso 1 · Abre tu base y elige tus columnas")
sol_code(f"""import pandas as pd

tabla = pd.read_csv("{LINK_EJEMPLO}")
print("Filas y columnas:", tabla.shape)
tabla.head()""")
sol_code("""print(list(tabla.columns))

columnas_base = ["NOMBRE_UNIVERSIDAD", "NOMBRE_CARRERA", "AREA_CONOCIMIENTO_SIES"]
columnas_a_medir = ["PROM_OBLIGATORIAS_ULTIMO_SELEC", "PROM_OBLIGATORIAS_P25", "MARGEN_P25_MENOS_ULTIMO"]""")
sol_md("""
#### 📝 Respuesta — Paso 1

- **¿Qué representa una fila de tu base?** Una carrera de una universidad en el proceso de admisión 2026 (2.150 filas).
- **Mis columnas base son** `NOMBRE_UNIVERSIDAD`, `NOMBRE_CARRERA` y `AREA_CONOCIMIENTO_SIES`, y cada una me permite comparar entre universidades, entre carreras y entre áreas del conocimiento. Sin ellas tendría un montón de puntajes sin saber a qué carrera ni a qué área pertenecen.
- **Mis columnas a medir son** el puntaje del último seleccionado, el percentil 25 y el margen entre ambos, y espero encontrar que las carreras más exigidas tengan puntajes más altos y márgenes más chicos.
""")

sol_md("### Paso 2 · A. Mira antes de limpiar")
sol_code("""print(tabla[columnas_a_medir].dtypes)
tabla[columnas_a_medir].head(10)""")
sol_md("""
#### 📝 Respuesta — Paso 2

- **En el PDF de mi base, ¿qué columnas parecen número pero vienen con coma, con puntos o con `s/i`?** `PROM_OBLIGATORIAS_P25` viene con coma decimal (`770,75`). `PROM_OBLIGATORIAS_ULTIMO_SELEC` también es texto: mezcla enteros (`670`) con decimales con coma (`607,5`) y en algunas filas viene vacío.
- **¿Coincide con el `.dtype`?** Sí: las dos son texto (`str`). `MARGEN_P25_MENOS_ULTIMO` es `float64`: ya es número (`100.75`), así que **no necesita limpieza**.
- **¿Qué te dice ese valor?** Que en `PROM_OBLIGATORIAS_P25` la coma es el decimal y hay que cambiarla por punto. Un puntaje de 770,75 tiene sentido (escala de 150 a 1000); 77075 no.
""")

sol_md("### Paso 3 · B, C y D · Decide, convierte y comprueba")
sol_code(f"""tabla = pd.read_csv(
    "{LINK_EJEMPLO}",
    dtype={{"PROM_OBLIGATORIAS_ULTIMO_SELEC": "str", "PROM_OBLIGATORIAS_P25": "str"}},
)

# B y C: coma decimal -> punto, y a número real (una línea por columna).
tabla["ultimo_selec_num"] = pd.to_numeric(
    tabla["PROM_OBLIGATORIAS_ULTIMO_SELEC"].str.strip().str.replace(",", ".", regex=False), errors="coerce"
)
tabla["p25_num"] = pd.to_numeric(
    tabla["PROM_OBLIGATORIAS_P25"].str.strip().str.replace(",", ".", regex=False), errors="coerce"
)

# D: comprobar.
print(tabla[["PROM_OBLIGATORIAS_P25", "p25_num"]].head())
print(tabla[["ultimo_selec_num", "p25_num", "MARGEN_P25_MENOS_ULTIMO"]].describe())
print("NaN en ultimo_selec_num:", tabla["ultimo_selec_num"].isna().sum())
print("NaN en p25_num:", tabla["p25_num"].isna().sum())""")
sol_md("""
#### 📝 Respuesta — Paso 3

- **¿Qué línea elegiste para cada columna y por qué?** A las dos columnas de texto les cambié la coma por punto (`.str.replace(",", ".")`) porque en el PDF vi `770,75`: la coma es el decimal. `MARGEN_P25_MENOS_ULTIMO` no la toqué: su `.dtype` es `float64`.
- **¿Cómo sabes que el número está bien?** En `.describe()` el mínimo y el máximo caen dentro de la escala de puntajes (de 365 a 982 en el último seleccionado, de 470 a 948 en el P25) y el margen va de -228 a 192 puntos, con promedio cerca de 6: tiene sentido. Si hubiera quedado 77075, el máximo habría sido enorme.
- **Si hubieras quitado el punto sin mirar, ¿qué habría salido mal?** Los puntajes con coma decimal (como `607,5`) habrían quedado `NaN`: 1.048 de 2.150 filas, así que se habría notado al contar filas. En otras bases, como SIES, `0.65` habría pasado a `65` sin avisar.
""")

sol_md("### Paso 4 · Descarta y cuenta lo perdido")
sol_code("""filas_antes = tabla.shape[0]
tabla_lista = tabla[tabla["ultimo_selec_num"].notna()]
tabla_lista = tabla_lista[tabla_lista["p25_num"].notna()]
print("Filas antes:", filas_antes)
print("Filas después:", tabla_lista.shape[0])
print("Filas perdidas:", filas_antes - tabla_lista.shape[0])""")
sol_md("""
#### 📝 Respuesta — Paso 4

- **Filas antes: 2.150 · después: 2.147 · perdidas: 3.**
- **¿Por qué se perdieron?** Eran carreras que no tenían puntaje (vacío real en la base), no un error de mi limpieza: lo comprobé porque el `.isna()` de la columna original ya contaba esos mismos 3 vacíos.
- **¿Podría cambiar lo que concluyas?** Casi nada: son 3 de 2.150 carreras. Aun así, lo anoto: mi análisis no dice nada de esas 3 carreras.
""")

sol_md("### Paso 5 · Tu tabla lista")
sol_code("""tabla_lista = tabla_lista[columnas_base + ["ultimo_selec_num", "p25_num", "MARGEN_P25_MENOS_ULTIMO"]]
print(tabla_lista.shape)
tabla_lista.head()""")
sol_md("""
#### 📝 Respuesta — Paso 5

> Mi tabla tiene 2.147 filas, cada una es una carrera de una universidad, y puedo comparar los puntajes y el margen según la universidad, la carrera o el área del conocimiento.

- **¿Qué descubriste hoy de tu base?** Que casi todos los puntajes venían como texto con coma decimal, y que el margen ya venía como número; sin mirar el `.dtype` habría limpiado una columna que no lo necesitaba.
""")

sol_md("""
### Paso 6 · Mi pregunta (con 2 filtros)

#### 📝 Respuesta — Paso 6

- **Pregunta candidata:** ¿Qué áreas del conocimiento tienen las carreras con puntajes de entrada más altos?
- **¿Mis datos ya limpios la responden?** Sí: tengo `AREA_CONOCIMIENTO_SIES` y `ultimo_selec_num` en 2.147 filas.
- **¿Es abierta?** Sí: no se responde con un sí o un no; deja explicar por qué.
- **Una pregunta que descarté y por qué:** «¿La Universidad de Chile tiene puntajes más altos que otras?»: se responde con un sí o un no, así que no es abierta.
- **Mi pregunta elegida:** ¿Qué áreas del conocimiento exigen los puntajes más altos para entrar y en cuáles el margen de ingreso es más estrecho?
- **¿Cómo cambió respecto al borrador de la 36b?** El borrador preguntaba por «carreras difíciles», sin saber qué columna lo medía. Al ver que tengo el puntaje del último seleccionado y el margen, pude volverla medible.
""")

sol_md("""
---

## 📒 Bitácora

**Sesión 19-oct — Mi tabla lista y mi pregunta**
- Qué avanzamos hoy: miramos el tipo de cada columna, limpiamos las que venían como texto con coma, descartamos 3 filas sin dato y afinamos la pregunta con los 2 filtros.
- Qué pensamos hacer el martes 20 (Clase 38): usar la tabla lista para empezar a responder la pregunta.
""")

sol_md("""
---

## 🧑‍🏫 Nota al docente

### Qué línea va en cada base (verificado sobre los CSV v2)

Para cada columna: primero `.dtype` (paso A). Solo las que salen como texto necesitan línea.

| Base | Columnas que son texto con número | Cómo vienen | Línea (paso B) | Columnas que ya son número (no tocar) |
|---|---|---|---|---|
| 01 SIES | `Retención 1er año`, `Duración Real (semestres)` | punto **decimal** + `s/i` | solo `.str.strip()`; **nunca quitar el punto** | `% titulados con continuidad…`, `Empleabilidad 1er año`, `Empleabilidad 2° año`, `Ingreso_punto_medio`, `Código` |
| 02 DEMRE | las 10 `PROM_OBLIGATORIAS_*` | coma decimal (`607,5`) y enteros sueltos (`674`) | `,` → `.` | `MARGEN_P25_MENOS_ULTIMO` (`100.75`) |
| 03 SIMCE establecimiento | los 6 `palu_eda_*` | coma decimal | `,` → `.` | — |
| 04 SIMCE comuna | los 6 `palu_eda_*` | coma decimal | `,` → `.` | — |
| 05 Matrícula | ninguna | — | nada | todas las numéricas |
| 06 Subvenciones | 23 columnas de monto | punto de **miles** (`136.818.693`, `35.672`) | `.` → nada | — |
| 07 CONASET | ninguna | — | nada | todas las numéricas |
| 08a ODEPA consumidor | `Precio promedio` | coma decimal (`9998,500000`) | `,` → `.` | — |
| 09a / 09b Hospitalarias | `Indice_Ocupacional`, `Indice_de_Rotacion`, `Letalidad`, `Promedio_Cama_Disponibles`, `Promedio_Dias_de_Estada` | coma decimal | `,` → `.` | `Egresos_por_dia` (solo 09a; `3.129` = tres coma ciento veintinueve) |

Los equipos inscritos (CONASET, DEMRE, SIES, Hospitalarias, SIMCE establecimiento y Matrícula) solo necesitan coma decimal, punto decimal o «ya es número». Ninguno necesita la línea de miles, pero la tabla la incluye porque es la que vieron en la N°37 y porque otros equipos podrían cambiar de base (Subvenciones).

### Qué pasa si se usa la línea equivocada

Medido sobre los CSV (las celdas de abajo lo recalculan en vivo):
""")

sol_code(f"""datos_demre = pd.read_csv("{LINK_EJEMPLO}", dtype={{"PROM_OBLIGATORIAS_ULTIMO_SELEC": "str"}})
mal_demre = pd.to_numeric(
    datos_demre["PROM_OBLIGATORIAS_ULTIMO_SELEC"].str.strip().str.replace(".", "", regex=False), errors="coerce"
)
print("DEMRE, quitando el punto: NaN =", mal_demre.isna().sum(), "de", len(mal_demre))

datos_sies = pd.read_csv("{link('01_sies.csv')}", dtype={{"Retención 1er año": "str"}})
columna_sies = datos_sies["Retención 1er año"]
bien = pd.to_numeric(columna_sies.str.strip(), errors="coerce")
mal = pd.to_numeric(columna_sies.str.strip().str.replace(".", "", regex=False), errors="coerce")
print("SIES, quitando el punto: máximo correcto =", bien.max(), "· máximo con el punto quitado =", mal.max())""")

sol_md("""
| Línea usada | Base | Resultado |
|---|---|---|
| Quitar el punto (`.` → nada) | DEMRE | 1.048 de 2.150 filas quedan `NaN` en `PROM_OBLIGATORIAS_ULTIMO_SELEC` (todas las que traen coma decimal): se nota al contar filas |
| Quitar el punto | SIES (`0.65`) | 65 en vez de 0,65, y valores como `0.0887573964497041` multiplicados por 10^16: **no avisa** |
| Cambiar coma por punto | Subvenciones (`2.908` con un solo punto) | queda 2,908 en vez de 2908: **no avisa** (en `SUBV_ASISTENTES_EDUCACION` son 111.772 de 123.361 valores; en `PROFESOR_ENCARGADO`, 17.880) |
| Cambiar coma por punto | Subvenciones (`136.818.693`, dos puntos) | `NaN`: se nota al contar filas |

> La conclusión para clase: **no existe una línea segura para todas las bases**; lo que protege es mirar el `.dtype`, el valor y comprobar con `.describe()`.
""")

for i, celda in enumerate(sol, start=1):
    celda["id"] = f"s{i:02d}"

nb_sol = new_notebook(cells=sol)
nb_sol.metadata["colab"] = {"provenance": []}
nb_sol.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb_sol.metadata["language_info"] = {"name": "python"}

# Se ejecuta contra la URL real para dejar los resultados guardados en el Solucionario.
try:
    from nbclient import NotebookClient

    NotebookClient(nb_sol, timeout=600, kernel_name="python3").execute()
    print("Solucionario ejecutado contra la URL real")
except Exception as error:  # noqa: BLE001
    print("⚠️ No se pudo ejecutar el Solucionario (queda sin resultados):", type(error).__name__, str(error)[:300])

nbformat.validate(nb_sol)
nbformat.write(nb_sol, SALIDA_SOL)
print("Generado:", SALIDA_SOL.name, "—", len(sol), "celdas")
