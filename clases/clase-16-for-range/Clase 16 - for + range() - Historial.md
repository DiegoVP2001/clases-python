# Historial — Clase 16

## 2026-07-08 — Especificación aprobada
- Objetivo: Construir programas con `for` y `range()` para repetir instrucciones y generar secuencias numéricas, con orden.
- Contexto temático: Mundial 2026 (resultados reales al 7 de julio de 2026, investigados vía web search).
- Estructura aprobada en varias iteraciones:
  - Objetivo/propósito: actitud ajustada de "perseverancia" (propuesta inicial) a "orden" a pedido de Diego; propósito acortado y pasado a plural ("nos" en vez de "te").
  - Haz Ahora: ajustado para recordar el bloque de programación por bloques (`for_bloques.pdf`, "contar con VARIABLE desde X hasta Y de a Z hacer") en vez de una actividad genérica.
  - ICN: conceptos de `range()` fusionados en uno solo (`range(inicio, fin, salto)` con valores por defecto) para alinear con el bloque ya visto.
  - Guiada: situación reescrita con el framing "la semana pasada ya sabíamos los resultados hasta octavos" para no depender de resultados que cambiarán antes de dictar la clase.
  - Independiente: cambiado de 2 ejercicios fijos a 1 obligatorio + 1 bonus (décimas extra), reflejando el nuevo default de trabajo en parejas.
  - Ticket de Salida: 3 preguntas revisadas y aprobadas por Diego antes de guardar el spec.
- Cambios sistémicos derivados de esta clase (aplicados a CLAUDE.md y skills):
  - Modalidad de trabajo por defecto: Parejas (antes Individual).
  - Práctica Independiente: 1 ejercicio obligatorio + 1 bonus (antes 2 fijos).
  - Ninguna solución vive en los notebooks de estudiante (Clase.ipynb, Ejercicios.ipynb) — todas se consolidan en Solucionario.ipynb, que Diego sube a Classroom después de dictar la clase.
  - Formato del propósito fijado en la skill `disenar-clase`: 3 frases, plural, sin listas intercaladas.

## 2026-07-08 — Colab de clase iterado (Haz Ahora, ICN, Ticket, Guiada)
- Haz Ahora: la recreación HTML del bloque no se veía en Colab → reemplazada por la imagen real recortada de `for_bloques.pdf` (`assets/bloque_for.png`), incrustada como base64. Nuevo: el generador (`crear_colab.py`) incrusta automáticamente cualquier imagen local referenciada en el spec (`incrustar_imagenes_locales`).
- ICN: `for` y `range(inicio, fin, salto)` presentados como tabla comparativa lado a lado en vez de dos conceptos separados. Nuevo tipo de item `**Comparación:**` soportado por el generador (análogo a `**Concepto:**`/`**Demostración:**`).
- Encabezado del Colab: emojis ⚽🏆🌎 agregados (ajuste cosmético específico de esta clase, no vive en el spec — se reaplica manualmente si se regenera el notebook).
- Cambios sistémicos derivados de esta iteración (aplicados a CLAUDE.md y skills):
  - Práctica Guiada nunca lleva celda "Mis respuestas" — Diego escribe el código directo en la celda de código.
  - El Colab de clase incluye una sección placeholder "🎫 Ticket de Salida" antes del Cierre, avisando que se proyecta en la tele — nunca las preguntas ni alternativas (esas siguen solo en Solucionario.ipynb).
  - Se corrigió una inconsistencia en `disenar-clase/SKILL.md`: sus plantillas de Paso 4/5 todavía decían "2 ejercicios fijos" para Independiente en vez de "1 obligatorio + 1 bonus".

## 2026-07-08 — Práctica Guiada: pasos y resultado en tabla de 2 columnas
- Reemplazado el formato de lista numerada + bloque único de "Resultado esperado" por una tabla de 2 columnas (qué debe hacer el programa | resultado esperado), un paso (o grupo de pasos) por fila. Los pasos 2 y 3 originales (construir el bucle + sumar y mostrar dentro de él) se fusionaron en una fila, porque separados el paso de "construir el bucle" quedaba sin resultado propio. El resultado de cada fila se acortó con `...` para no ser tan largo de mostrar.
- Bug encontrado y corregido durante la implementación: los backticks (`` `range()` ``) dentro de una tabla HTML cruda no se convierten a `<code>` porque Jupyter/Colab no reprocesa markdown inline dentro de bloques `<table>`. Nueva función `backticks_a_code()` en `crear_colab.py`, aplicada tanto a la tabla de pasos guiados como a la tabla de "Comparación" del ICN.
- Cambio sistémico (aplicado a CLAUDE.md restricción 20, `disenar-clase/SKILL.md` y `generar-colab-clase/SKILL.md`): formato de tabla para pasos guiados queda como default para todas las clases futuras. Formato antiguo (lista + resultado único) se mantiene como fallback retrocompatible en el parser.
- Cambio sistémico adicional (CLAUDE.md restricción 21): el signo peso (`$`) en texto markdown/prosa de los specs debe escaparse siempre como `\$` — sin escapar, Colab lo interpreta como delimitador de fórmula MathJax y descuadra el texto. Corregidos los ejemplos con `$` sin escapar en CLAUDE.md, `disenar-clase/SKILL.md`, `generar-colab-clase/SKILL.md` y `referencia-isla-de-maipo/SKILL.md`.
- Pendiente anotado (no resuelto aún): `generar-ppt-clase/crear_ppt.py` todavía no reconoce el tipo `**Comparación:**` del ICN — cuando lleguemos al paso del PPT de esta clase, esa sección se saltaría silenciosamente si no se corrige antes.

## 2026-07-08 — PPT generado (pendiente del tipo Comparación resuelto)
- Diego pidió saltar el Colab de ejercicios por ahora e ir directo al PPT.
- Se resolvió el pendiente anotado: `parsear_icn_enriquecido` en `crear_ppt.py` ahora detecta bloques `**Comparación: título**` (tabla HTML `<table>`) al mismo nivel que `**Concepto N:**`, los intercala por posición real de aparición en el spec y los renumera junto con los Concepto (`📘 N.`). La tabla se convierte a filas de texto plano (`<code>` → backticks para Consolas verdoso; `<pre>`/`<strong>`/`<em>` se aplanan preservando saltos de línea) y se renderiza con el bloque `tipo="tabla"` que el slide ICN flexible ya soportaba — sin necesidad de un layout nuevo.
- Cambio sistémico adicional: `insertar_tabla_pptx` ahora soporta celdas con saltos de línea reales (`\n` → párrafo nuevo), necesario para el contenido `<pre>` de la Comparación. Retrocompatible con las tablas markdown existentes (Haz Ahora, errores típicos), que no usan `\n` dentro de una celda.
- Verificado con `--preview-icn`: la tabla Comparación aparece completa (4×2), seguida del slide de Acumulador y el resumen `dos_columnas` — nada se pierde en silencio.
- Documentado en `generar-ppt-clase/SKILL.md` (tabla de tipos de concepto + nueva sección "Comparación (tabla lado a lado)" en sintaxis del spec).
- `Clase 16 - for + range() - Presentación.pptx` generado. Colab de ejercicios queda pendiente para después.

## 2026-07-09 — Fix visual: tabla Comparación del ICN se veía muy larga en Colab
- La tabla `<table>` de la Comparación `for`/`range()` no tenía ancho ni wrap definidos, así que en Colab se desbordaba horizontalmente en vez de partir el texto en líneas (ver captura `Screenshot_1.png`).
- Corregido agregando `style="width:100%; table-layout:fixed;"` al `<table>`, `width:50%` a los `<th>`, y `white-space:normal; word-wrap:break-word;` a los `<td>` (más `white-space:pre-wrap` dentro de los `<pre>` para que el código también parta de línea si hace falta). Aplicado en `Clase.ipynb` y en el spec (fuente de verdad) para que una regeneración futura no reintroduzca el bug.
- Cambio puntual de esta clase, no sistémico — el ICN de comparación lado a lado es un patrón nuevo (introducido el 2026-07-08) y aún no está documentado con estilos por defecto en `disenar-clase/SKILL.md` ni en `crear_colab.py`; si vuelve a aparecer en otra clase, vale la pena moverlo al generador.

## 2026-07-09 — Fix de texto: descripción de `for` en la tabla Comparación difícil de entender
- Diego marcó que la descripción de la columna `for` era confusa ("Repite el bloque de código indentado una vez por cada valor que le entrega la secuencia que recorre...").
- Simplificada a: "Repite las líneas de código que están indentadas debajo de él, una vez por cada número de la secuencia. En cada vuelta, la variable pasa sola al siguiente número — nunca tienes que actualizarla tú." Aplicado en `Clase.ipynb` y en el spec.

## 2026-07-09 — Tabla Comparación pasada de HTML crudo a markdown; texto de `for` reescrito de nuevo
- Diego pidió el texto final de la descripción de `for`: "El ciclo for repite un bloque de código una vez por cada valor de una secuencia. La variable cambia automáticamente en cada vuelta." (reemplaza la simplificación anterior del mismo día).
- Además pidió cambiar la estructura de la tabla Comparación de `<table>` HTML crudo a una tabla markdown (`| col | col |`), más simple de mantener. Aplicado en `Clase.ipynb` y en el spec: encabezados y descripciones ahora en sintaxis markdown con backticks nativos; los dos bloques de código conservan `<pre style="white-space:pre-wrap;">` con `<br>` en vez de saltos de línea reales (una tabla markdown no admite saltos de línea crudos dentro de una celda).
- Nota para Diego: este formato markdown para bloques `**Comparación:**` diverge de lo que hoy genera `crear_colab.py` (que copia el `<table>` HTML tal cual del spec). Si esta clase se regenera desde cero con la skill `generar-colab-clase`, revisar que el generador siga produciendo este formato o actualizarlo — no se tocó el generador en este fix porque fue una edición puntual post-generación.
- `Presentación.pptx` no se actualizó con este cambio de texto ni de formato (la Comparación en el PPT usa su propio pipeline de parseo de tabla HTML). Diego confirmó explícitamente que **no** quiere regenerar el PPT — el desfase entre el PPT (texto/tabla antiguos) y el Colab (texto/tabla nuevos) queda aceptado, no pendiente.
- Sesión cerrada con Colab de ejercicios todavía sin hacer — sigue pendiente para otra sesión, sin fecha definida.

## 2026-07-09 — Reel generado
- Archivo: `Clase 16 - for + range() - Reel.mp4`
- Errores mostrados: 3 (fin de `range()` no incluido, indentación olvidada bajo `for`, acumulador inicializado dentro del bucle) — tomados directo de la tabla "Errores típicos" del spec.
- Conceptos: 3 escenas separadas (`for`, `range(inicio, fin, salto)`, acumulador), a pedido de Diego — la propuesta inicial fusionaba `for`+`range()` en una sola escena.
- Hook con contexto real (apps como Google mostrando resultados del Mundial partido por partido).
- Colab de ejercicios sigue pendiente (no bloquea el Reel).
