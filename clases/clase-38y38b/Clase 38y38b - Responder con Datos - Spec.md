# Clase 38 y 38b — Responder con datos (giro plug-and-play)

**Estado:** Spec aprobada por Diego — 2026-10-20
**Reemplaza:** las clases originales N°38 (`old/clase-38-pandas3-responder-con-datos`) y 38b (`old/clase-38b-aplicacion-mi-evidencia`), que quedaron archivadas sin cambios.
**Fechas:** mar 20-oct (Clase 38) y jue 22-oct (Clase 38b); el trabajo sigue hasta el lun 26-oct (Colab final, 23:59). Calendario v4 se mantiene.

## Por qué existe

En la 37b (lun 19-oct) nadie llegó al Paso 4: de 40 cuadernos, ~20 estaban vacíos y casi todos se quedaron en el Paso 1-2. Los obstáculos no fueron de pandas: volvían a leer la tabla en cada celda, typos (`import panda`, `read_cvs`), dejaban `tabla["col"]` sin reemplazar y no sabían dónde poner el código. Se decidió simplificar: bases limpias, una receta visible donde solo se cambian las líneas de arriba, y un cuaderno que se usa de principio a fin (sin "retoma lo anterior").

## Contexto

- **Curso:** 3ro y 4to medio · **Plataforma:** Google Colab · **Entrega:** Google Classroom
- **Objetivo:** construir una secuencia ordenada de pasos que responda una pregunta con una tabla de datos —quedarse con lo que interesa, resumirlo, ordenarlo y graficarlo—, con método.
- **Sin funciones propias (`def`)** ni `try/except`.
- **Ticket de Salida de la N°38:** **pendiente, no se toca ni se elimina** (decisión de Diego). Los archivos originales siguen en `old/clase-38-pandas3-responder-con-datos/`. Sus preguntas usan la receta de 4 líneas; al decidir qué hacer con él, ojo con que el ICN nuevo agrega `RESUMEN` y `.agg(...)` en el Concepto 5.

## Dos cuadernos separados y enfocados

| Cuaderno | Qué contiene | Quién lo lleva en una pareja |
|---|---|---|
| 🧑‍💻 **Código** | Haz Ahora, ICN 1-5 (guaguas), Guiada (CONASET), galería de 12 ejemplos, "Mi base" (Pasos 1-4) | Uno de los dos |
| ✍️ **Texto** | Frases para completar, una sección por diapositiva, nota de prensa, Bitácora de 3 entradas | El otro (o la misma persona, si trabaja sola) |

- Cada vez que el Código dice **«✍️ Responde ahora en el cuaderno de Texto, sección N»**, se pasa al otro.
- El Texto abre con un aviso destacado de que **al final hay una Bitácora** que se responde cada día (mar 20, jue 22, lun 26).
- El Texto trae un cuadro **«Pega aquí tus 6 espacios y tu tabla»** para que quien escribe no dependa de que su pareja le dicte las cifras (regla: nadie queda bloqueado esperando a otro).
- **Los cuadernos no se presentan: se presenta el PPT.** Unidos, son el Colab final (Producto, 35%). Cada integrante entrega el suyo y Diego los une cuando lo indique.
- **Lo que se entrega hoy es lo que se usa hasta el lunes 26:** no hay cuaderno nuevo el jueves.

## La receta (6 espacios, sin `def`)

```python
COL_FILTRO = ...   # 🔎 ¿en qué columna miro?
VALOR      = ...   # 🔎 ¿con qué valor me quedo?  (None = no filtrar)
COL_GRUPO  = ...   # 🧺 ¿qué junto?
COL_NUMERO = ...   # 🔢 ¿qué cifra resumo?
RESUMEN    = ...   # "sum" · "mean" · "count"
N          = ...   # ¿cuántos muestro?
TITULO     = ""    # opcional
```

Salidas: filas que dejó el filtro y filas sin dato (límites) · cifras del top y % del total (evidencia) · mayor, menor del top y promedio de los grupos (hallazgo) · gráfico de barras horizontales con título automático.

## Estructura de las dos sesiones

| Parte | Tiempo | Qué pasa |
|---|---|---|
| Haz Ahora | 6 min | Las 4 preguntas de siempre sobre las Antonias, sin código. |
| ICN 1-4 | 22 min | Filtrar → agrupar → ordenar → graficar, cada uno con su pregunta, **Idea clave** y **✍️ Escríbelo tú**, sobre guaguas. |
| **ICN 5 (nuevo)** | ~8 min | **Qué columna va en cada espacio** (etiqueta vs cantidad, trampas, ficha de columnas) y **cómo leer la salida**. Cierra con la tabla-resumen pregunta → espacios → tipo de columna → línea. |
| Guiada | 8 min | La receta sobre CONASET: llenan los 6 espacios con la pregunta de las comunas con más fallecidos en 2025. |
| Galería | referencia | Una receta ya llena por cada una de las **12 bases** (se ejecutó cada una al generar). |
| **Mi base** | resto de la sesión y la 38b | **Paso 1** abrir la base y ficha de las 5 columnas → ✍️ Texto 1-2 · **Paso 2** llenar los espacios y correr → ✍️ Texto 3-4 · **Paso 3** mirar lo que salió → ✍️ Texto 5 · **Paso 4** una pregunta distinta → ✍️ Texto 6-8. |

## Bases: 5 columnas sugeridas, con rol

Cada base trae 5 columnas sugeridas (🔎 filtrar · 🧺 agrupar · 🔢 cantidad) y una nota de «códigos que verás» (dependencia, grupo socioeconómico, rural), apoyada en el Diccionario de Columnas. Las bases viven en `datos-compartidos-v3/` (limpias, mismos nombres que la v2; ver su README).

## Evaluación (actualiza lo publicado el 19-oct)

La rúbrica completa, con equipos y bases, vive en esta carpeta: `Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb` (para estudiantes) y `Rúbricas y Evaluación - Proyecto Cierre Octubre (v5).md` (interna, con puntajes y niveles). El cuaderno de Código solo enlaza a ella.

- **«Conoce su base» (15 pts, dentro de Producto; reemplaza a «Archivo usable»):** **5 pts por cumplir el mínimo** (describir la base: qué es una fila, cuántas hay, qué columnas se usan y por qué) y **10 pts por una pregunta distinta** (una segunda pregunta, o una que use una columna fuera de las 5 sugeridas).
- **Nota de prensa:** se mantiene, simplificada (titular y 3-4 líneas); la versión corregida con IA lleva registro.
- **Defensa técnica (mar 27):** sin cambios de formato. Los errores intervenidos van en los espacios de la receta y en la receta misma.
- **Nota de progreso 37b:** hito de Proceso, lineal por pareja (la que más avanzó = 7,0, aunque tenga errores). Pendiente de calcular.

## Decisiones de diseño relevantes

- **`RESUMEN` pasa a ser el 6.º espacio:** «total, promedio o cantidad» era donde más se trababan. En el Concepto 2 se enseña `.sum()` (alineado con el Ticket pendiente) y en el Concepto 5 se generaliza con `.agg(RESUMEN)`.
- **Filtro opcional:** `VALOR = None` es «toda la tabla», resuelto con un `if/else`.
- **Título del gráfico automático** (`RESUMEN` de `COL_NUMERO` por `COL_GRUPO`), con `TITULO` para ponerle uno propio.
- **Ejemplos de la galería:** cortes distintos de los que probablemente elijan los equipos (por ejemplo, DEMRE muestra vacantes por área y no «Medicina»); advierten que copiarlos sin cambios no cuenta como pregunta propia.
- **ODEPA filtra una sola unidad** en los ejemplos: promediar `$/kilo` con `$/unidad` no significa nada.
- **No se separaron** `Producto` (ODEPA consumidor), `UBICACION` (CONASET) ni `Calidad` (ODEPA mayorista), por decisión explícita.

## Archivos de esta carpeta

| Archivo | Para quién |
|---|---|
| `Clase 38y38b - Responder con Datos - Código.ipynb` | Estudiantes (Colab) |
| `Clase 38y38b - Responder con Datos - Texto.ipynb` | Estudiantes (Colab) |
| `Clase 38y38b - Responder con Datos - Solucionario.ipynb` | Profesor (nunca antes de la entrega del lun 26) |
| `Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb` | Estudiantes (Colab): rúbrica v5, equipos y bases |
| `Rúbricas y Evaluación - Proyecto Cierre Octubre (v5).md` | Interna: puntajes, niveles y pendientes |
| `Clase 38y38b - Diccionario de Columnas.pdf` / `.tex` | Estudiantes: qué significa cada columna, con índice por base (v3) |
| `Clase 38y38b - Muestra de las Bases.pdf` / `.tex` | Estudiantes: 6 filas reales de cada base, con índice (v3) |
| `generar_cuadernos.py` | Fuente de verdad de los tres cuadernos: no editar los `.ipynb` a mano |
| `generar_rubrica.py` · `generar_muestra_pdf.py` | Fuentes de la rúbrica para estudiantes y del PDF de muestras (el Diccionario es un `.tex` escrito a mano; `logo.png` es su logo) |
| `datos-compartidos-v3/` | Bases limpias (se leen por URL raw desde los cuadernos) |
| `old/` | Las carpetas originales de la N°38 y la 38b, sin cambios |
