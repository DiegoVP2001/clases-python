"""Genera Clase 38b - Mi Evidencia - Responder y Concluir (Clase + Solucionario).

Fuente de verdad del cuaderno: no editar los .ipynb a mano, editar acá y regenerar.
Uso:  python generar_cuaderno.py
"""
import base64
from pathlib import Path
from urllib.parse import quote

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

CARPETA = Path(__file__).resolve().parent
CLASES = CARPETA.parent
SALIDA = CARPETA / "Clase 38b - Mi Evidencia - Responder y Concluir - Clase.ipynb"
SALIDA_SOL = CARPETA / "Clase 38b - Mi Evidencia - Responder y Concluir - Solucionario.ipynb"
FOTO = CLASES / "clase-35-listas" / "foto_lun.png"

REPO = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/"
RAW = REPO + "clases-octubre/datos-compartidos-v2/"
LINK_GUAGUAS = REPO + "clases-octubre/datos-compartidos/bbdd_guaguas.csv"
LINK_DICCIONARIO = (
    "https://github.com/DiegoVP2001/clases-python/blob/master/clases/clase-36b-aplicacion-mi-base/"
    + quote("Clase 36b - Mi Base - Diccionario de Columnas.pdf")
)


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
# 🐍 Clase 38b — Mi evidencia y mi conclusión

**Curso:** 3ro y 4to medio  |  **Duración:** ~77 min  |  **Plataforma:** Google Colab

---
""")

foto_b64 = base64.b64encode(FOTO.read_bytes()).decode("ascii")
portada_foto = new_markdown_cell(
    "## 📰 De dónde partimos\n\n"
    "Con datos públicos como los de tu base se armó una noticia de circulación nacional: "
    "*cuánto ganan los ingenieros civiles industriales según su universidad de egreso*.\n\n"
    "![La nota del LUN — Cuánto ganan los ingenieros civiles industriales según su universidad de egreso](attachment:foto_lun.png)\n\n"
    "Un titular así es creíble por dos cosas: **la evidencia** (una cifra o un gráfico que responde una pregunta clara) y "
    "**la honestidad sobre sus límites** (qué no se puede afirmar con esos datos). Hoy produces las dos para tu propia pregunta."
)
portada_foto["attachments"] = {"foto_lun.png": {"image/png": foto_b64}}
cells.append(portada_foto)

md("""
## 🎯 Objetivo de hoy

Aplicar la receta de la Clase 38 (filtrar, agrupar y resumir, ordenar y graficar) a tu base para responder tu pregunta con **una tabla o un gráfico**, decir **qué no puedes concluir** con esos datos y escribir tu **conclusión**.

## 🔎 ¿Para qué sirve?

> Un gráfico que «salió» no es lo mismo que un gráfico que responde. Un promedio de porcentajes pesa igual a una carrera con 5 titulados que a una con 500; un filtro mal escrito deja cero filas sin avisar. Lo que escribas hoy es el centro de tu Colab narrado y lo que vas a presentar ante dirección.

**Cómo funciona este cuaderno:** trae todo lo que necesitas, aunque hayas faltado a la Clase 37b o a la 38. Lee, escribe el código en las celdas vacías y responde en las celdas 📝 **con tus palabras**: esas respuestas cuentan para tu nota.
""")

# ───────────────────────── Rúbrica ─────────────────────────
md("""
---

## 📋 Cómo se evalúa (recordatorio)

El proyecto de cierre se traduce en **una sola nota** (vale doble en el promedio semestral), armada con 4 partes:

| Parte | Peso | Qué mide |
|---|---|---|
| 📓 Producto — Colab narrado | **35%** | Análisis correcto y razonamiento explicado en texto, de corrido |
| 🎤 Presentación ante dirección | 20% | Claridad del hallazgo, evidencia y qué NO se puede concluir |
| 🔍 Defensa técnica — código intervenido | 30% | Explicar tu propio código y corregir errores metidos a propósito |
| 📒 Proceso — bitácora e hitos | **15%** | Avance real clase a clase, con evidencia |

### 👉 Este cuaderno alimenta **Producto (35%)** y **Proceso (15%)**

**Producto** — se revisa que:

1. ✅ **El gráfico o la tabla responde tu pregunta**, y lo explicas con tus palabras.
2. ✅ **Dices un límite real:** qué NO puedes concluir con estos datos (no una frase de relleno).
3. ✅ **Tu conclusión** nombra la pregunta, la respuesta con una cifra de tu evidencia y ese límite.

**Proceso** — se revisa que:

1. ✅ **El código corre** de arriba hacia abajo sobre tu base.
2. ✅ **Cada celda 📝 tiene su respuesta**, escrita en markdown con tus palabras.
3. ✅ **La bitácora de hoy está completa** y la entregas en Classroom **hasta el viernes 23-oct**.

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

md(f"""
📖 **Diccionario de Columnas** (qué significa cada columna de cada base): [abrir el PDF]({LINK_DICCIONARIO})

✅ **Tu base ya viene preparada**: se abre con `pd.read_csv(link)`. Las bases de 10 a 44 MB tardan unos segundos; ábrela **una sola vez** y sigue trabajando con la variable `tabla`, sin volver a ejecutar esa celda.
""")

md("""
---

### 🔧 Preparación

Ejecuta esta celda antes de empezar: instala pandas en tu sesión de Colab, por si acaso.
""")
code("!pip install pandas")

# ───────────────────────── Torpedo ─────────────────────────
md("""
---

## 🧾 Repaso rápido

### Clase 38: la receta de cuatro preguntas

Cada pregunta de la receta se responde llenando uno o dos espacios:

| Pregunta | Espacios que llenas | Línea |
|---|---|---|
| 1. ¿Con qué parte de la tabla me quedo? | `COL_FILTRO`, `VALOR` | `tabla[tabla[COL_FILTRO] == VALOR]` |
| 2. ¿Qué junto y qué cifra resumo? | `COL_GRUPO`, `COL_NUMERO` | `.groupby(COL_GRUPO)[COL_NUMERO].sum()` |
| 3. ¿En qué orden lo pongo y cuántos muestro? | `N` | `.sort_values(ascending=False).head(N)` |
| 4. ¿Cómo lo muestro para compararlo? | título y ejes | `.plot(kind="bar", ...)` |

### Otras preguntas con la misma receta

Para otra pregunta no hay que empezar de cero: cambias la respuesta de **una** de las cuatro preguntas.

| Si tu pregunta es... | Cambia la respuesta de la... | Línea resultante |
|---|---|---|
| El **promedio**, no el total | Pregunta 2 | `.sum()` → `.mean()` |
| **Cuántas filas** hay por grupo | Pregunta 2 | `.sum()` → `.count()` |
| El **mayor** valor de cada grupo | Pregunta 2 | `.sum()` → `.max()` |
| Los **menores**, no los mayores | Pregunta 3 | `ascending=False` → `ascending=True` |
| Solo valores **sobre un umbral** | Pregunta 1 | `==` → `>` (ej. `tabla[tabla["cantidad_guaguas"] > 1000]`) |
| Todo **menos** un valor | Pregunta 1 | `==` → `!=` (ej. `tabla[tabla["nombre"] != "Antonia"]`) |
| Barras **horizontales** (nombres largos) | Pregunta 4 | `"bar"` → `"barh"` |
| **No filtrar** nada | Pregunta 1 | se omite la línea y se parte de `tabla` |

> ⚠️ Antes de elegir el resumen, piensa **qué representa cada fila** de tu base. `.mean()` y `.count()` significan lo que esperas solo si cada fila es una persona, un registro o una carrera.

### Clase 37: dejar una columna lista (si tu tabla lista no está hecha)

| Concepto | Ejemplo |
|---|---|
| Leer con cuidado | `pd.read_csv(archivo, dtype={"col": "str"})` |
| Sacar los espacios sobrantes | `columna.str.strip()` |
| Arreglar el separador (según lo que veas) | miles `2.908` → `columna.str.replace(".", "", regex=False)` · coma decimal `607,5` → `columna.str.replace(",", ".", regex=False)` · punto decimal `0.65` → nada |
| Convertir a número real | `pd.to_numeric(columna, errors="coerce")` |
| Descartar filas que no se pudieron limpiar | `tabla[tabla["col"].notna()]` |
""")

md(f"""
### 📋 La receta completa

La celda de abajo reúne la receta de la Clase 38 con la tabla de nombres de guaguas (`bbdd_guaguas.csv`), que se usó como ejemplo en clase. Los cinco espacios van arriba y el resto son las cuatro líneas de la receta.

Es una **referencia para que la analices caso a caso**: fíjate qué espacio responde cada pregunta, de qué variable parte cada línea y qué deja. Lo que corresponda a tu base lo decides tú mirando tus datos (se explica paso a paso más abajo).
""")

code(f'''# ═══════════ Clase 38 · la receta, con la tabla de guaguas ═══════════
# Ejemplo: ¿en qué años nacieron más Antonias?  (tabla ya limpia: columna "cantidad_guaguas")

# import pandas as pd
# import matplotlib.pyplot as plt
# tabla = pd.read_csv("{LINK_GUAGUAS}", dtype={{"n": "str"}})
# tabla["cantidad_guaguas"] = pd.to_numeric(tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce")
# tabla = tabla[tabla["cantidad_guaguas"].notna()]

# ── Lo único que cambias (tu pregunta, traducida) ──
# COL_FILTRO = "nombre"            # 1. ¿en qué columna miro?
# VALOR      = "Antonia"           # 1. ¿con qué valor me quedo?
# COL_GRUPO  = "anio"              # 2. ¿qué junto?
# COL_NUMERO = "cantidad_guaguas"  # 2. ¿qué cifra resumo?
# N          = 10                  # 3. ¿cuántos muestro?

# ── La receta ──
# filtrada = tabla[tabla[COL_FILTRO] == VALOR]
# resumen  = filtrada.groupby(COL_GRUPO)[COL_NUMERO].sum()   # o .mean(), .count()
# top      = resumen.sort_values(ascending=False).head(N)
# top.plot(kind="bar", title="Años con más " + VALOR, xlabel="Año", ylabel="Cantidad de guaguas")  # 4. ¿cómo lo muestro?
# plt.show()''')

md("""
> 🔁 **Ojo con los nombres:** `COL_FILTRO`, `VALOR`, `COL_GRUPO`, `COL_NUMERO`, `N` y `col` son marcadores. Debes **reemplazarlos por los nombres de tus columnas**, tal como aparecen en `list(tabla.columns)`.
>
> 📒 **Antes de seguir, revisa tu cuaderno de la Clase 37b:** ahí dejaste tu tabla lista y tu pregunta elegida, y hoy partes desde ese trabajo.
""")

# ───────────────────────── Plan de hoy ─────────────────────────
md("""
---

## 🧭 Plan de hoy

Hoy conviertes tu pregunta en evidencia y en conclusión, en 6 pasos. En cada uno encontrarás primero **lo que necesitas saber para ese paso** y luego lo que debes hacer.

| Paso | Qué harás | Para qué |
|---|---|---|
| **0** | Retomar tu **tabla lista** y tu **pregunta** de la Clase 37b | No partir de cero |
| **1** | **Traducir** tu pregunta a los cinco espacios de la receta | Que la tabla o el gráfico responda *tu* pregunta |
| **2** | **Producir** tu evidencia: la tabla y el gráfico de barras | Tener algo que mostrar |
| **3** | **Mirar** lo que salió: ¿responde? ¿las cifras tienen sentido? | No creerle a un gráfico solo porque «salió» |
| **4** | Escribir **qué NO puedes concluir** | Ser honesto con la evidencia |
| **5** | Escribir tu **conclusión** | Cerrar el Colab narrado |

Cada paso tiene una consigna, una celda de código y una celda 📝 para responder con tus palabras. Las preguntas no piden copiar el resultado: piden **explicar qué descubriste y por qué decidiste lo que decidiste**.
""")

md("""
---

## 🔍 Trabajo en tu base
""")

# ── Paso 0 ──
md("""
### Paso 0 · Retoma tu tabla y tu pregunta

**Lo que necesitas saber:** hoy no se parte de cero. Tu tabla lista (la que dejaste en el Paso 5 de la Clase 37b) y tu pregunta elegida (Paso 6) son el punto de partida. Si no tienes tu tabla a mano, la rehaces con el repaso de la Clase 37 de más arriba: abrir la base, limpiar las columnas que vienen como texto y descartar las filas vacías. A lo largo de este cuaderno la tabla se llama `tabla`.

**Lo que debes hacer:**

1. Abre tu base con `pd.read_csv(...)`, guárdala en `tabla` y deja lista la columna (o columnas) numérica que vas a resumir.
2. Muestra su `.shape` y sus primeras filas.
""")
code("# Paso 0 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 0

- **¿Qué representa una fila de tu tabla y cuántas filas tienes?**
- **Mi pregunta (la de la Clase 37b) es:**
- **¿Descartaste filas al dejar tu tabla lista? ¿Cuántas y por qué?** (lo vas a necesitar en el Paso 4)
""")

# ── Paso 1 ──
md("""
### Paso 1 · Traduce tu pregunta a los cinco espacios

**Lo que necesitas saber:** tu pregunta se traduce llenando los cinco espacios de la receta. Antes, tres decisiones:

- **¿Necesito filtrar?** Es opcional. Si tu pregunta es sobre toda la tabla (por ejemplo, «¿qué áreas tienen más...?»), no filtras y parte de `tabla`. Si es sobre una parte (una región, un año, un tipo de institución), filtras. **Un valor numérico va sin comillas; un texto, con comillas y escrito exacto** (misma mayúscula y misma tilde que en la tabla).
- **¿Total, promedio o cantidad?** `.sum()` responde «¿cuánto hay en total?»; `.mean()`, «¿cómo es lo típico?»; `.count()`, «¿cuántas filas hay?». Un `.mean()` de porcentajes es un **promedio de promedios**: cada fila pesa igual, aunque unas representen a muchas más personas que otras.
- **¿Hace falta calcular una columna?** Tu base ya puede traer columnas calculadas (`Ingreso_punto_medio`, `MARGEN_P25_MENOS_ULTIMO`, `Mes_num`, `Egresos_por_dia`). Mira `list(tabla.columns)` antes de inventar una.

**Lo que debes hacer:** escribe los cinco espacios para tu pregunta, con los nombres copiados desde `list(tabla.columns)`. Todavía no armes la receta: solo los espacios, y muestra cuántas filas deja tu filtro con `len(...)`.
""")
code("# Paso 1 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 1

- **¿Por qué elegiste esa columna para agrupar y esa para resumir?** (qué comparación te permite):
- **¿Usaste `.sum()`, `.mean()` o `.count()`, y por qué?**
- **¿Qué cambiaría en tu resultado si usaras otro de los tres?**
""")

# ── Paso 2 ──
md("""
### Paso 2 · Produce tu evidencia

**Lo que necesitas saber:** con los espacios llenos, las cuatro líneas de la receta producen la evidencia. Además del gráfico, imprime `top`: la tabla con las cifras exactas es parte de la evidencia, porque un gráfico muestra la forma y la tabla muestra los números. Si los nombres de tus categorías son largos, usa `kind="barh"`. Dale un **título** que diga qué se está midiendo y **nombres a los ejes**.

**Lo que debes hacer:** escribe la receta completa sobre tu tabla, imprime `top` y grafica en barras con título y nombres para los dos ejes.
""")
code("# Paso 2 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 2

- **¿Qué muestra tu gráfico, en una frase?** (con una cifra de tu tabla):
""")

# ── Paso 3 ──
md("""
### Paso 3 · Mira lo que salió

**Lo que necesitas saber:** un resultado que «salió» no es un resultado correcto. Antes de creerle, revisa:

- **¿Responde mi pregunta?** El gráfico muestra lo que preguntaste, no algo parecido.
- **¿Las cifras tienen sentido?** Compáralas con la escala de tu columna (un puntaje de 77.075 en una escala de 150 a 1000 es un error).
- **¿Cuántas filas hay detrás de cada barra?** Un promedio calculado con 3 filas pesa lo mismo en el gráfico que uno calculado con 300. Lo ves con `.count()` en vez de `.mean()`.
- **¿El filtro dejó 0 filas?** Si el gráfico sale vacío, revisa cómo escribiste el valor.

**Lo que debes hacer:** muestra cuántas filas hay detrás de cada barra de tu gráfico (cambia el resumen a `.count()` en una línea aparte) y revisa el mínimo y el máximo de tu columna con `.describe()`.
""")
code("# Paso 3 — Tu código\n")
md("""
#### 📝 Respuesta — Paso 3

- **¿Responde tu gráfico la pregunta que hiciste? Si no del todo, ¿qué le falta?**
- **¿Qué revisaste para creerle a tu resultado?** (cifras, filas por barra, escala):
- **¿Hay alguna barra que se apoye en muy pocas filas? ¿Cuál y cuántas?**
""")

# ── Paso 4 ──
md("""
### Paso 4 · Qué NO puedo concluir

**Lo que necesitas saber:** todo resultado tiene límites, y decirlos es lo que lo hace creíble. Un límite real es **concreto de tus datos**, no una frase de relleno como «faltan más datos». Los más comunes:

| Tipo de límite | Ejemplo |
|---|---|
| Promedio de promedios | Cada carrera pesa igual en el promedio aunque tenga 5 o 500 titulados |
| Filas descartadas | «Perdí 3 filas sin puntaje»: mi análisis no dice nada de ellas |
| Pocas filas detrás | Una barra se apoya en 3 filas y otra en 300 |
| La columna no mide lo que creía | «Empleabilidad» mide haber trabajado, no cuánto se gana |
| Alcance | Es una región o un año, no todo Chile ni todos los años |
| Asociación no es causa | Dos cosas que suben juntas no prueban que una cause la otra |

**Lo que debes hacer:** elige el límite que más afecta a **tu** evidencia y escríbelo con una cifra o un dato de tu tabla.
""")
md("""
#### 📝 Respuesta — Paso 4

- **Con mis datos NO puedo concluir que...**
- **Lo sé porque** (cifra o dato de mi tabla que lo muestra):
- **Si alguien lo olvidara, ¿qué conclusión equivocada sacaría?**
""")

# ── Paso 5 ──
md("""
### Paso 5 · Mi conclusión

**Lo que necesitas saber:** una conclusión no repite el gráfico: responde la pregunta, apoyándose en la evidencia y reconociendo su límite. Tiene tres partes: **la respuesta** (con una cifra), **de dónde sale** (qué mostró el gráfico) y **hasta dónde llega** (el límite del Paso 4).

**Lo que debes hacer:** escribe tu conclusión como un párrafo corto, de corrido, como se la explicarías a la dirección del colegio.
""")
md("""
#### 📝 Respuesta — Paso 5

> Mi pregunta era ... La evidencia muestra que ... (cifra). Esto se ve en ... Sin embargo, no puedo concluir que ... porque ...

**Mi conclusión:**

- **Una cosa que haría distinta si tuviera más tiempo con esta base:**
""")

# ───────────────────────── Bitácora y entrega ─────────────────────────
md("""
---

## 📒 Bitácora

> Se completa al cerrar la sesión. Es lo que la rúbrica de Proceso revisa.

**Sesión 22-oct — Mi evidencia y mi conclusión**
- Qué avanzamos hoy:
- Qué falta para terminar el Colab narrado:
- Qué pensamos hacer el lunes 26 (Defensa técnica):
""")

md("""
---

## 📤 Entrega

El Colab narrado se entrega **hasta el viernes 23-oct**. Antes de entregar:

1. Ejecuta todo de arriba hacia abajo: menú **Entorno de ejecución → Ejecutar todo**. Revisa que no quede ningún error en rojo.
2. Revisa que todas las celdas 📝 y la bitácora tengan tu respuesta.
3. En la tarea de Google Classroom, presiona **Entregar**.
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
LINK_EJEMPLO = link("01_sies.csv")

sol = []


def sol_md(texto):
    sol.append(new_markdown_cell(texto.strip("\n")))


def sol_code(texto):
    sol.append(new_code_cell(texto))


sol_md("""
# 🔒 Solucionario — Clase 38b: Mi evidencia y mi conclusión

**Uso:** documento para el profesor. Muestra **a qué debería llegar cada estudiante al término de la clase**, usando una sola base de ejemplo: **Empleabilidad e ingresos (SIES)**, con la pregunta *«¿Qué áreas del conocimiento tienen mejor empleabilidad al primer año en las universidades?»*. Cada equipo trabaja con su base y su pregunta, así que sus respuestas serán distintas; lo que se mantiene es la estructura.

---

## ¿Qué se revisa en cada parte?

| Parte | Una respuesta suficiente... |
|---|---|
| Paso 0 | retoma su tabla lista, dice **qué representa una fila**, nombra su pregunta y recuerda si descartó filas |
| Paso 1 | llena los cinco espacios con nombres reales de columnas, **justifica** el resumen (`sum`/`mean`/`count`) y dice qué cambiaría con otro |
| Paso 2 | produce un gráfico de barras con título y ejes, imprime `top`, y describe lo que muestra **con una cifra** |
| Paso 3 | revisa filas por barra y escala de la columna; dice **qué revisó** para creerle al resultado |
| Paso 4 | nombra un **límite real y concreto** de sus datos (no «faltan datos»), respaldado con una cifra |
| Paso 5 | escribe un párrafo con la respuesta (cifra), su origen y el límite |
| Bitácora | completa las tres líneas, con algo concreto de hoy |

**Producto (35%):** pasos 2, 4 y 5 (evidencia, límite, conclusión). **Proceso (15%):** código que corre, celdas 📝 completas y bitácora.
""")

sol_md(f"""
---

## 🔍 Trabajo en tu base — resuelto con SIES

Link usado como ejemplo:

`{LINK_EJEMPLO}`
""")

sol_md("### Paso 0 · Retoma tu tabla y tu pregunta")
sol_code(f"""import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.read_csv("{LINK_EJEMPLO}")

# Empleabilidad 1er año ya es numérica (float64): no necesita limpieza. Solo se descartan las filas vacías.
filas_antes = tabla.shape[0]
tabla = tabla[tabla["Empleabilidad 1er año"].notna()]
print("Filas antes:", filas_antes, "· después:", tabla.shape[0], "· perdidas:", filas_antes - tabla.shape[0])
tabla[["Tipo de institución", "Área", "Nombre carrera genérica", "Empleabilidad 1er año"]].head()""")
sol_md("""
#### 📝 Respuesta — Paso 0

- **¿Qué representa una fila y cuántas filas tienes?** Una carrera de una institución (1.690 filas, ver la celda de arriba).
- **Mi pregunta es:** ¿Qué áreas del conocimiento tienen mejor empleabilidad al primer año en las universidades?
- **¿Descartaste filas?** No: `Empleabilidad 1er año` no tiene vacíos, así que no se perdió ninguna fila. Lo anoto igual, porque en otras bases sí se pierden y hay que decirlo en el Paso 4.
""")

sol_md("### Paso 1 · Traduce tu pregunta a los cinco espacios")
sol_code("""COL_FILTRO = "Tipo de institución"
VALOR      = "Universidades"
COL_GRUPO  = "Área"
COL_NUMERO = "Empleabilidad 1er año"
N          = 10

print("Filas después del filtro:", len(tabla[tabla[COL_FILTRO] == VALOR]))""")
sol_md("""
#### 📝 Respuesta — Paso 1

- **¿Por qué esa columna para agrupar y esa para resumir?** Agrupo por `Área` porque la pregunta compara áreas del conocimiento, y resumo `Empleabilidad 1er año` porque es la medida de empleabilidad que trae la base. Filtro `Universidades` porque la pregunta es solo sobre ellas (y así no mezclo institutos ni CFT).
- **¿Usaste `.sum()`, `.mean()` o `.count()`?** `.mean()`: la empleabilidad es un porcentaje y sumar porcentajes no tiene sentido; quiero lo típico de cada área.
- **¿Qué cambiaría con otro?** Con `.sum()` ganaría el área con más carreras, no la de mejor empleabilidad; con `.count()` solo vería cuántas carreras tiene cada área.
""")

sol_md("### Paso 2 · Produce tu evidencia")
sol_code("""filtrada = tabla[tabla[COL_FILTRO] == VALOR]
resumen  = filtrada.groupby(COL_GRUPO)[COL_NUMERO].mean()
top      = resumen.sort_values(ascending=False).head(N)
print(top.round(3))

top.plot(kind="barh", title="Empleabilidad promedio al 1er año, por área (universidades)", xlabel="Empleabilidad promedio", ylabel="Área")
plt.show()""")
sol_md("""
#### 📝 Respuesta — Paso 2

- **¿Qué muestra tu gráfico?** Que Tecnología es el área con mayor empleabilidad promedio al primer año (cerca de 0,79) y Humanidades la menor de las diez (cerca de 0,41); el resto queda entre ambas.
""")

sol_md("### Paso 3 · Mira lo que salió")
sol_code("""cuantas_filas = filtrada.groupby(COL_GRUPO)[COL_NUMERO].count().sort_values()
print(cuantas_filas)
print(filtrada[COL_NUMERO].describe())""")
sol_md("""
#### 📝 Respuesta — Paso 3

- **¿Responde tu gráfico la pregunta?** Sí: compara el promedio por área, que es lo que preguntaba.
- **¿Qué revisaste?** Que el mínimo y el máximo de la columna estén entre 0 y 1 (es una proporción), que el filtro dejara filas (no salió vacío) y cuántas carreras hay detrás de cada área.
- **¿Hay alguna barra con muy pocas filas?** Sí: Humanidades tiene 16 carreras, Agropecuaria 29 y Derecho y Ciencias Básicas 31, frente a las 266 de Tecnología. Sus promedios son menos confiables.
""")

sol_md("### Paso 4 · Qué NO puedo concluir")
sol_md("""
#### 📝 Respuesta — Paso 4

- **Con mis datos NO puedo concluir que** estudiar Tecnología asegure mejor empleo que Humanidades, ni que una carrera concreta de esa área tenga esa empleabilidad.
- **Lo sé porque** el valor de cada barra es un promedio de promedios: una carrera de Humanidades con pocos titulados pesa lo mismo que una de Tecnología con muchos, y Humanidades solo se apoya en 16 carreras.
- **Si alguien lo olvidara,** podría recomendar elegir un área solo por esa barra, sin saber que el promedio esconde la variación entre carreras.
""")

sol_md("### Paso 5 · Mi conclusión")
sol_md("""
#### 📝 Respuesta — Paso 5

> Mi pregunta era qué áreas tienen mejor empleabilidad al primer año en las universidades. La evidencia muestra que Tecnología lidera con cerca de 0,79 de empleabilidad promedio y Humanidades cierra con cerca de 0,41. Esto se ve en el gráfico de barras por área. Sin embargo, no puedo concluir que un área sea «mejor» que otra para cualquier persona, porque cada barra es un promedio de promedios y algunas áreas, como Humanidades, se apoyan en pocas carreras.

- **Una cosa que haría distinta:** comparar carreras específicas dentro de cada área, o ponderar por número de titulados si la base lo permitiera.
""")

sol_md("""
---

## 📒 Bitácora

**Sesión 22-oct — Mi evidencia y mi conclusión**
- Qué avanzamos hoy: retomamos la tabla de SIES, filtramos universidades, promediamos la empleabilidad por área y graficamos las 10 mejores.
- Qué falta para terminar el Colab narrado: pulir la conclusión y revisar que todas las celdas 📝 estén completas.
- Qué pensamos hacer el lunes 26 (Defensa técnica): repasar qué hace cada línea de la receta y por qué usamos `.mean()`.
""")

sol_md("""
---

## 🧑‍🏫 Nota al docente

### Qué parámetros tienen sentido en cada base inscrita

Cada fila es una unidad distinta, y de ahí sale qué resumen es honesto. Antes de cada celda de verificación se limpian solo las columnas que vienen como texto (ver tabla de la Clase 37b).

| Base | Una fila es... | Ejemplo de pregunta | `COL_GRUPO` · `COL_NUMERO` · resumen | Límite típico |
|---|---|---|---|---|
| 01 SIES | una carrera de una institución | ¿Qué áreas tienen mejor empleabilidad? | `Área` · `Empleabilidad 1er año` · `.mean()` | Promedio de promedios; áreas con pocas carreras |
| 02 DEMRE | una carrera de una universidad | ¿Qué áreas exigen puntajes más altos? | `AREA_CONOCIMIENTO_SIES` · `ultimo_selec_num` (limpiada) · `.mean()` | Promedio de promedios; 3 carreras sin puntaje |
| 03 SIMCE establecimiento | un establecimiento | ¿Qué comunas tienen mejor puntaje en lectura? | `nom_com_rbd` · `prom_lect2m_rbd` · `.mean()` | Comunas con pocos establecimientos; promedio de promedios |
| 05 Matrícula | un establecimiento | ¿Qué comunas concentran más matrícula? | `NOM_COM_RBD` · una columna `MAT_*` · `.sum()` | Cada columna `MAT_*` cubre solo un tipo de enseñanza o un sexo, no la matrícula total |
| 07 CONASET | un siniestro | ¿Qué comunas tuvieron más fallecidos en 2025? | `COMUNA` · `FALLECIDOS` · `.sum()` | Total absoluto no es riesgo: no considera población ni tránsito |
| 09a Hospitalarias (mensual) | un servicio de un hospital en un mes | ¿Qué meses tienen más egresos? | `Mes_num` · `Numero_de_Egresos` · `.sum()` | Es un solo año (2024): no muestra tendencia |
| 09b Hospitalarias (anual) | un servicio de un hospital | ¿Qué servicios de salud tienen más egresos? | `Servicio_Salud` · `Numero_de_Egresos` · `.sum()` | El total depende de cuántos hospitales tiene cada servicio |

Las celdas de abajo recalculan cada ejemplo sobre los CSV reales (la base DEMRE limpia primero la coma decimal).
""")

sol_code(f"""def leer(archivo, **kwargs):
    return pd.read_csv("{RAW}" + archivo, **kwargs)


def top_de(tabla, col_grupo, col_numero, resumen, n=5, col_filtro=None, valor=None):
    filtrada = tabla if col_filtro is None else tabla[tabla[col_filtro] == valor]
    serie = getattr(filtrada.groupby(col_grupo)[col_numero], resumen)()
    return len(filtrada), serie.sort_values(ascending=False).head(n)


resultados = {{}}

# DEMRE: coma decimal -> punto
demre = leer("02_demre.csv", dtype={{"PROM_OBLIGATORIAS_ULTIMO_SELEC": "str"}})
demre["ultimo_selec_num"] = pd.to_numeric(
    demre["PROM_OBLIGATORIAS_ULTIMO_SELEC"].str.strip().str.replace(",", ".", regex=False), errors="coerce"
)
demre = demre[demre["ultimo_selec_num"].notna()]
resultados["02 DEMRE"] = top_de(demre, "AREA_CONOCIMIENTO_SIES", "ultimo_selec_num", "mean")

# SIMCE establecimiento: coma decimal -> punto
simce = leer("03_simce_establecimiento.csv", dtype={{"prom_lect2m_rbd": "str"}})
simce["lectura_num"] = pd.to_numeric(
    simce["prom_lect2m_rbd"].str.strip().str.replace(",", ".", regex=False), errors="coerce"
)
simce = simce[simce["lectura_num"].notna()]
resultados["03 SIMCE"] = top_de(simce, "nom_com_rbd", "lectura_num", "mean")

# Matrícula, CONASET y Hospitalarias: columnas ya numéricas
resultados["05 Matrícula"] = top_de(leer("05_matricula.csv"), "NOM_COM_RBD", "MAT_ENS_1", "sum")
resultados["07 CONASET"] = top_de(
    leer("07_conaset_rm.csv", low_memory=False), "COMUNA", "FALLECIDOS", "sum", col_filtro="AÑO", valor=2025
)
resultados["09a Hospitalarias mensual"] = top_de(leer("09a_hospitalarias_mensual.csv"), "Mes_num", "Numero_de_Egresos", "sum", n=12)
resultados["09b Hospitalarias anual"] = top_de(leer("09b_hospitalarias_anual.csv"), "Servicio_Salud", "Numero_de_Egresos", "sum")

for nombre, (filas, serie) in resultados.items():
    print("──", nombre, "· filas tras el filtro:", filas)
    print(serie.round(2).to_string())
    print()""")

sol_md("""
> Lo que protege al estudiante en cualquier base es lo mismo que en la 37b: **mirar qué es una fila antes de elegir el resumen** y comprobar cuántas filas hay detrás de cada barra.
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

    NotebookClient(nb_sol, timeout=900, kernel_name="python3").execute()
    print("Solucionario ejecutado contra la URL real")
except Exception as error:  # noqa: BLE001
    print("⚠️ No se pudo ejecutar el Solucionario (queda sin resultados):", type(error).__name__, str(error)[:300])

nbformat.validate(nb_sol)
nbformat.write(nb_sol, SALIDA_SOL)
print("Generado:", SALIDA_SOL.name, "—", len(sol), "celdas")
