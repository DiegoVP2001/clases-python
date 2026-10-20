# Historial — Clase 38 y 38b (Responder con datos)

## 2026-10-20 — Giro plug-and-play: diseño y generación

**Origen.** Diego revisó los 40 cuadernos de la 37b (lun 19-oct) y la asistencia (22 presentes): casi nadie pasó del Paso 3 y los obstáculos eran de estructura, no de pandas. Decidió simplificar mucho para que todos logren responder al menos una pregunta, y ganar tiempo.

**Decisiones de Diego (entrevista del 20-oct)**
- N°38 se modifica el mismo día. ICN que siga construyendo concepto sobre concepto («Escríbelo tú»). Receta visible con las líneas de cambio arriba. Salidas: filas usadas y perdidas, tabla top N con %, mayor/menor/promedio, gráfico de barras.
- Dos cuadernos separados y enfocados: **Código** y **Texto**. Lo que se entrega hoy se reutiliza hasta el lunes 26; no hay cuaderno nuevo el jueves. Los cuadernos no se presentan (se presenta el PPT); unidos son el Colab final.
- Bases completas, limpias, **con los mismos nombres de columna** (hay grupos avanzando sobre la v2). Cada base con 5 columnas sugeridas con rol, y una galería con un ejemplo por base.
- «Conoce su base» (15 pts): 5 por el mínimo y 10 por una pregunta distinta (segunda pregunta o columna fuera de las sugeridas).
- Todo lo nuevo en `clase-38y38b/`; las carpetas originales en `old/`.
- Pendientes por decisión de Diego: Ticket de Salida de la N°38 (no tocar), base del trío Cifuentes + Moyano + Julián Aravena, uniones futuras de cuadernos (solo la 37b por ahora).

**Estudio de columnas con números escritos con palabras (pedido de Diego)**
- Se revisaron las columnas de texto de las 12 bases. Hallazgos aprobados e implementados (la columna original se conserva): SIES `Ingreso_min`/`Ingreso_max` (rango escrito con palabras) y `Acreditacion_anios` (`No` = 0); ODEPA consumidor `Unidad_cantidad`/`Unidad_medida`; ODEPA mayorista `Envase`/`Unidad_cantidad`/`Unidad_medida` y `Mes_num`.
- Diego dejó **sin separar** `Producto` (ODEPA consumidor, `Palta|Hass|Primera`), `UBICACION` (CONASET) y `Calidad` (ODEPA mayorista). Los códigos de dependencia/rural/grupo quedan **explicados en una nota simple**, no decodificados.
- Problema detectado: ODEPA mezcla `$/kilo` con `$/unidad`; queda como nota de límite y los ejemplos filtran una sola unidad.
- Interpretaciones mías, para que Diego revise: `"$/kilo (en saco de 25 kilos)"` = 1 kilo (el paréntesis describe el envase); `"$/docena de atados"` = 12 unidades; atados y canastillos cuentan como unidades; `"$/paquete"` sin cantidad queda vacío.

**Qué se produjo**
- `datos-compartidos-v3/` (12 bases, README) generadas por `tools/datos_octubre/preparar_bases_v3.py`, con verificación automática (lo convertido coincide con los valores verdaderos, lo no tocado queda idéntico a la v2, las columnas nuevas son coherentes). La v1 y la v2 no se tocaron.
- Diccionario de Columnas (36b) y PDF de muestras (37b) regenerados para v3 (el Diccionario es un `.tex` a mano; el PDF de muestras sale de `generar_muestra_pdf.py`).
- `generar_cuadernos.py` → Código (68 celdas), Texto (23) y Solucionario (38).
- Las carpetas `clase-38-pandas3-responder-con-datos` y `clase-38b-aplicacion-mi-evidencia` pasaron a `old/` sin cambios. `Historial-Curricular.md` actualizado.

**Verificación**
- Los 12 ejemplos de la galería se ejecutaron contra la v3 local; cada uno comprueba un dato conocido (nº de filas, filas perdidas o valor máximo).
- El cuaderno de Código se ejecutó de punta a punta como lo haría un estudiante (llenando los espacios con CONASET): 16 celdas de código sin errores.
- `nbformat.validate` pasa en los tres. Sin `$` suelto en markdown. «3ro y 4to medio» en el encabezado. Voz colectiva, sin nombrar a Diego.

**Pendiente**
- Aprobación de Diego para subir a GitHub (repo público): `clase-38y38b/` sin el Solucionario ni los archivos del Ticket. Los cuadernos leen las bases por URL desde `clase-38y38b/datos-compartidos-v3/`, así que sin push no abren.
- Actualizar la rúbrica y el Colab de criterios (publicado el 19-oct): «Conoce su base», nota de prensa simplificada, errores de la Defensa en la receta, hito 37b = nota de progreso.
- Nota de progreso de la 37b y unión de cuadernos de pareja (37b).
- Agregar `CUADERNOS ESTUDIANTES/` al `.gitignore` (tiene código real de estudiantes).
- Banco de errores de la Defensa técnica sobre la receta.

## 2026-10-20 (tarde) — Ajustes tras revisar los cuadernos

**Pedidos de Diego**
- Sacar del cuaderno de Código el bloque «Dentro de Producto» y generar en esta carpeta **una nueva versión de la rúbrica**, que incluya también los equipos y bases.
- Traer a esta carpeta los PDF índice nuevos (Diccionario de Columnas y Muestra de las Bases), que no estaban acá.
- Acortar el texto de cada concepto nuevo del ICN; en el Concepto 5, poner ejemplos de tipo de columna con la tabla de guaguas.
- Cerrar y subir a git lo necesario.

**Qué se hizo**
- **ICN más corto:** las definiciones de los Conceptos 1-4 pasan de ~4 oraciones a 2. El Concepto 5 se reescribe: tabla de tipos de columna con guaguas (`nombre`, `anio`, `sexo`, `cantidad_guaguas`: etiqueta o cantidad, y en qué espacio va), una sola idea clave, ficha, receta y una lista corta de «cómo se lee lo que salió».
- **Cuaderno de Código:** se quitó «Dentro de Producto» y las menciones sueltas de puntajes («10 de los 15 puntos»); ahora dicen que la rúbrica lo premia y enlazan a ella.
- **Rúbrica nueva (v5)**, en dos versiones: `Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb` (estudiantes) y `Rúbricas y Evaluación - Proyecto Cierre Octubre (v5).md` (interna). Cambios: «Archivo usable» → **«Conoce su base»** (5 pts mínimo + 10 pts pregunta distinta), mapa de dónde se corrige cada criterio en los dos cuadernos, errores de la Defensa en la receta, hitos de Proceso con la 37b como nota de progreso, y sección de equipos y bases.
- **PDF nuevos en esta carpeta:** `Diccionario de Columnas` y `Muestra de las Bases` (v3, con índice), con los enlaces de los cuadernos apuntando acá. Los archivos de la 36b y la 37b que se habían modificado en su lugar se devolvieron a su versión original (siguen siendo los de la v2).

**Lo que dejé marcado para Diego**
- La tabla de equipos viene de la 37b (19-oct) y **no coincide con el Calendario v4**: allí Benjamín Mejías queda fuera, y no aparecen la pareja Lucas Valenzuela + Víctor Olguín ni el trío Cifuentes + Moyano + Julián Aravena. Se corrige con la lista actual.
- Niveles de «Pregunta distinta», cálculo de la nota de progreso 37b y normalización de Producto (115 pts): propuestas, por confirmar (§10 de la rúbrica interna).
- En el cuaderno de estudiantes puse el hito 37b de forma neutra («cuenta el avance que dejó cada equipo ese día»); el detalle del cálculo queda solo en la versión interna.

## 2026-10-20 (noche) — Nota de prensa como noticia real

**Pedidos de Diego:** que la nota de prensa no sea de 3 o 4 líneas sino una noticia estructurada (bajada, entrada, desarrollo, cierre); poner el hipervínculo de la nota del LUN en los cuadernos de Código y de Texto; reutilizar lo escrito en las respuestas de texto; y sacar la idea de usar IA. Además, el cuaderno de Código ya no lleva el bloque de equipos (solo la rúbrica).

**Qué se hizo**
- **Texto, sección 8:** tabla que compara las partes de la nota del LUN con las de la nuestra (titular, bajada, entrada, desarrollo, cierre) y de qué sección se reutiliza cada una; celda de respuesta con las cinco partes. Se eliminó todo lo de borrador propio y versión con IA.
- **Enlace a la noticia** en «De dónde partimos» (Código) y en la sección 8 (Texto).
- **Solucionario:** el modelo de la nota de prensa sigue la estructura nueva, con CONASET. Las cifras (305 fallecidos, 6,9 %, promedio de 6,1 y el ranking de bicicletas) salen de ejecutar los datos, no de escribirlas a mano.
- **Rúbrica (estudiantes e interna):** la nota de prensa se evalúa como noticia estructurada; se quitó el nivel de IA «con registro». Rigen «Nada de IA» (código y todos los textos) y «Libre» (diseño de la presentación). La tabla de IA de la v4 queda como registro en la versión interna.

**Texto de la noticia:** solo se citan el titular, la bajada y la fuente; el desarrollo con expertos no se reproduce en los cuadernos.
