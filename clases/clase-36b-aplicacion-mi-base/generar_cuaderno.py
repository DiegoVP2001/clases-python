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

RAW = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos-v2/"


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

> Es el primer paso real de tu proyecto de cierre: antes de decidir qué investigar, hay que saber qué hay dentro de tu base. Lo que escribas hoy es la materia prima para las próximas clases del proyecto.

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
lineas_links = []
for n, nombre, ruta, aviso in BASES:
    lineas_links.append(f"# {n} · {nombre}{(' ' + aviso) if aviso else ''}")
    lineas_links.append(f'# "{link(ruta)}"')
    lineas_links.append("")
celda_links = "\n".join(lineas_links).rstrip()

md("""
---

## 🔗 Links de las bases

Copia el link de **tu** base —con sus comillas— y pégalo dentro de `pd.read_csv(...)`. Están en la celda de abajo, comentados, así que ejecutarla no hace nada.
""")

code(celda_links)

md("""
✅ **Tu base ya viene preparada.** Se abre con `pd.read_csv(link)`, sin ningún parámetro extra.
""")

md("""
### ⏳ Si tu base es pesada

Las bases de 10 a 44 MB tardan unos segundos en descargarse. Ábrela **una sola vez**: la variable `tabla` queda guardada en memoria. Para probar cosas distintas usa otras celdas que partan de `tabla`, sin volver a ejecutar la celda del `read_csv`.
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
| Abrir un CSV de otra fuente que no se lee bien | `pd.read_csv("link", sep=";", encoding="latin-1")` | La tabla bien separada y con las tildes correctas |
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

La celda de abajo está vacía a propósito: escribe en ella tu encabezado, línea por línea, siguiendo al profe y la tabla de herramientas de arriba (título → nombre del proyecto, negrita → base de datos, lista → integrantes, cita → por qué esa base, línea → cierre). Cuando termines, `Shift + Enter` para ver cómo quedó.
""")

cells.append(new_markdown_cell(""))

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
""")
code("# Paso 1 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 1

*(doble clic para editar y escribir)*

- **Lo primero que notas al ver las primeras filas:**
- **¿Hay alguna columna que parezca un número pero esté escrita de forma rara (con coma, con punto de miles, `s/i`)?** Anótala, sin arreglarla.
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

> 💡 **Pista — vacíos que pandas no cuenta:** `.isna()` solo cuenta como vacío lo que está **realmente** vacío. Si en las filas ves marcas como `s/i`, `-` o `*`, pandas **no** las cuenta. Y los números escritos con coma o con punto de miles tampoco son vacíos, pero sí hay que resolverlos antes de calcular. No arregles nada hoy: anótalo en tu respuesta y lo resolvemos el martes 13.
""")
code("# Paso 4 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 4

- **Columna con más vacíos y cuántos tiene:**
- **¿Pueden afectar lo que quieres averiguar? ¿Por qué?**
- **Algo raro que notaste en los datos (marcas como `s/i`, o números escritos con coma o punto de miles):**
""")

md("""
### Paso 5 · Y ahora, ¿qué pregunta quieres responder?

Ahora que sabes lo que hay en tu base —qué representa cada fila, qué columnas tiene y qué le falta—, escribe una **primera pregunta** que te gustaría responder con estos datos. Es un borrador: el 19-oct (clase 37b) la afinamos.
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

**Sesión 08-oct — Mi base: abrir y mirar**
- Qué avanzamos hoy:
- Qué pensamos hacer el martes 13:
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
SALIDA_SOL = CARPETA / "Clase 36b - Mi Base - Abrir y Mirar - Solucionario.ipynb"
LINK_EJEMPLO = link("07_conaset_rm.csv")

sol = []


def sol_md(texto):
    sol.append(new_markdown_cell(texto.strip("\n")))


def sol_code(texto):
    sol.append(new_code_cell(texto))


sol_md("""
# 🔒 Solucionario — Clase 36b: Mi base, abrir y mirar

**Uso:** documento para el profesor. Muestra **a qué debería llegar cada estudiante al término de la clase**, usando como ejemplo una sola base: **Siniestros de tránsito (CONASET, Región Metropolitana)**. Cada equipo trabaja con la suya, así que sus respuestas serán distintas; lo que se mantiene es la estructura. Los nombres del encabezado son marcadores (*Estudiante 1*, *Estudiante 2*).

---

## ¿Qué se revisa en cada parte? (Proceso, 15%)

| Parte | Una respuesta suficiente... |
|---|---|
| Encabezado | usa las 5 herramientas (título, negrita, lista, cita, línea) y dice qué base, quiénes y por qué |
| Paso 1 | abre su base y **describe lo que ve en las primeras filas**, incluidas las columnas que parecen números pero están escritas raro |
| Paso 2 | da las dimensiones correctas y dice **qué representa una fila** con sus palabras |
| Paso 3 | elige 3 a 6 columnas **justificadas por su interés** y nombra una columna que le faltó |
| Paso 4 | informa los vacíos de **sus** columnas y evalúa si afectan lo que quiere averiguar |
| Paso 5 | formula una pregunta **abierta** (borrador) y las columnas que necesitaría |
| Bitácora | completa las dos líneas, con algo concreto de hoy |
""")

# ── Encabezado ──
sol_md("""
---

## ✍️ Markdown en vivo — el encabezado terminado

Así debería quedar la celda que escriben juntos, una vez que se ejecuta con `Shift + Enter`:
""")

ENCABEZADO = """# Proyecto: Los siniestros de tránsito en la Región Metropolitana

**Base de datos:** Siniestros de tránsito 2020-2025 (CONASET), recorte de la Región Metropolitana

**Integrantes:**

- Estudiante 1
- Estudiante 2

**¿Por qué esta base?**

> Me interesa entender cuáles son las causas de los siniestros y cuándo ocurren más, porque a diario me muevo por la calle y *saber qué los provoca* ayuda a prevenirlos.

---"""
sol.append(new_markdown_cell(ENCABEZADO))

sol_md(f"""
**Cómo se escribe** (el texto que va en la celda, línea por línea):

```
{ENCABEZADO}
```

| Línea | Herramienta | Lo que se escribe |
|---|---|---|
| Nombre del proyecto | título | `# ` al comienzo |
| Base de datos | negrita | `**...**` alrededor de la etiqueta |
| Integrantes | lista | `- ` al comienzo de cada línea (con una línea en blanco antes) |
| Por qué esta base | cita | `> ` al comienzo |
| Cierre | línea | `---` |
| *saber qué los provoca* | cursiva | `*...*` |
""")

# ── Pasos ──
sol_md(f"""
---

## 🔍 Trabajo en tu base — resuelto con CONASET

Link usado como ejemplo:

`{LINK_EJEMPLO}`
""")

sol_md("### Paso 1 · Abre tu base")
sol_code(f"""import pandas as pd

tabla = pd.read_csv("{LINK_EJEMPLO}")
tabla.head()""")
sol_md("""
#### 📝 Respuesta — Paso 1

- **Lo primero que notas al ver las primeras filas:** hay columnas de ubicación (`Calle_Uno`, `Calle_Dos`, `Ruta`) mezcladas con columnas de lo que pasó (`TIPO_SINIE`, `CAUSA_NUEV`). *No es solo una tabla de causas.*
- **¿Hay alguna columna que parezca un número pero esté escrita de forma rara?** En esta base no: los números ya vienen como números (por eso CONASET no sirve de ejemplo para el anzuelo de N°37; ver la nota al docente más abajo).
""")

sol_md("### Paso 2 · Dimensiones y columnas")
sol_code("""print("Filas y columnas:", tabla.shape)
print("Columnas:", list(tabla.columns))""")
sol_md("""
#### 📝 Respuesta — Paso 2

- **Mi base tiene 123.343 filas y 37 columnas.**
- **Cada fila representa:** un siniestro de tránsito ocurrido en la Región Metropolitana entre 2020 y 2025.
- **Las columnas que más me llaman la atención son** `CAUSA_NUEV` y `TIPO_SINIE`, y creo que significan la causa del siniestro (agrupada) y qué tipo de choque fue. También `FALLECIDOS`, el número de personas fallecidas, y `Mes_num`, el mes escrito como número del 1 al 12.
""")

sol_md("### Paso 3 · Elige las columnas que importan")
sol_code("""columnas_relevantes = tabla[["Mes", "CAUSA_NUEV", "TIPO_SINIE", "COMUNA", "FALLECIDOS", "Ruta"]]
columnas_relevantes.head()""")
sol_md("""
#### 📝 Respuesta — Paso 3

- **Columnas elegidas y por qué:** `Mes` (para ver cuándo ocurren), `CAUSA_NUEV` y `TIPO_SINIE` (para ver qué los provoca y de qué tipo son), `COMUNA` (para ver dónde) y `FALLECIDOS` (para medir qué tan graves son) y `Ruta` (para ver si pasó en una carretera).
- **Una columna que me habría gustado que existiera y no está:** el número de vehículos involucrados en cada siniestro.
- **¿Qué tan bien responde esta base a lo que me interesaba?** Por completo: trae causas, meses y fallecidos.
""")

sol_md("### Paso 4 · Cuenta los vacíos")
sol_code("""columnas_relevantes.isna().sum()""")
sol_md("""
#### 📝 Respuesta — Paso 4

- **Columna con más vacíos y cuántos tiene:** `Ruta`, con 118.077 vacíos de 123.343 filas. Las otras cinco dan 0.
- **¿Pueden afectar lo que quieres averiguar? ¿Por qué?** Para mis causas y fallecidos no, porque tienen dato en todas las filas. `Ruta` solo se llena cuando el siniestro ocurrió en una carretera, así que no sirve para comparar todos los siniestros.
- **Algo raro que notaste en los datos:** nada raro: los vacíos de `Ruta` son vacíos de verdad y pandas los cuenta. *El martes 13 vemos qué hacer con los vacíos y con los números escritos como texto.*
""")

sol_md("""
### Paso 5 · ¿Qué pregunta quieres responder?

#### 📝 Respuesta — Paso 5

- **Pregunta (borrador):** ¿Qué causa de siniestro provoca más fallecidos en la Región Metropolitana, aunque no sea la más frecuente?
- **Columnas que necesitaría para responderla:** `CAUSA_NUEV` y `FALLECIDOS`.
""")

sol_md("""
---

## 🧑‍🏫 Nota al docente — el anzuelo de N°37

Con las bases v2 ya no existen los espacios escondidos en CONASET (`Ruta` trae 118.077 vacíos reales). El anzuelo de N°37 son los **números escritos como texto**, que CONASET no tiene. Lo que conviene que cada equipo anote en el Paso 1 según su base:

- **SIES:** `Retención 1er año` y `Duración Real (semestres)` traen `s/i`, así que pandas las lee como texto. `Ingreso Promedio al 4° año` es un rango en texto (existe `Ingreso_punto_medio`, ya numérica).
- **DEMRE:** las 10 columnas `PROM_OBLIGATORIAS_*` se escriben con coma decimal (`807,13`) y pandas las lee como texto.
- **SIMCE (3 y 4):** los 6 `palu_eda_*` con coma decimal.
- **Subvenciones:** 23 columnas de monto con punto de miles (`253.447.695`).
- **ODEPA y Hospitalarias:** `Precio promedio` y los 5 indicadores con decimales vienen con coma.
- **Matrícula y CONASET:** no tienen el problema; solo vacíos.
""")

sol_md("""
---

## 📒 Bitácora

**Sesión 08-oct — Mi base: abrir y mirar**
- Qué avanzamos hoy: abrimos la base de siniestros de tránsito, vimos que tiene 123.343 filas y 37 columnas, elegimos 5 columnas y escribimos una primera pregunta.
- Qué pensamos hacer el martes 13: aprender a dejar la tabla lista (vacíos y números escritos como texto) y aplicarlo a las columnas que elegimos.
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

    NotebookClient(nb_sol, timeout=300, kernel_name="python3").execute()
    print("Solucionario ejecutado contra la URL real")
except Exception as error:  # noqa: BLE001
    print("⚠️ No se pudo ejecutar el Solucionario (queda sin resultados):", type(error).__name__, str(error)[:200])

nbformat.validate(nb_sol)
nbformat.write(nb_sol, SALIDA_SOL)
print("Generado:", SALIDA_SOL.name, "—", len(sol), "celdas")
