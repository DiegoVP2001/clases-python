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

## 2026-10-20 (noche, 2) — Un solo flujo de análisis, ejemplos plegados y Texto con preguntas abiertas

**Pedidos de Diego:** que el Texto no pida completar frases sino responder preguntas abiertas (salvo la nota de prensa, cuya celda de respuesta le gusta); unificar las dos preguntas (la primera y la «distinta»), porque pedir dos veces lo mismo queda raro; dejar los ejemplos como ejemplos y **plegados** como las pistas; y premiar la **originalidad** de las preguntas, permitiendo hacer los análisis que quieran copiando y pegando la receta si están bien explicados.

**Qué se hizo**
- **Código:** los 12 ejemplos van en una sola celda, cada base en un `<details>`. «Mi base» queda en Paso 1 (abrir y mirar), Paso 2 (primer análisis con título `⭐ Análisis 1 · mi pregunta`) y Paso 3 (revisar). Se eliminó el Paso 4 y se agregó «➕ Más análisis (lo que más se premia)», con las reglas del juego.
- **Texto:** pasa de 8 secciones con frases a **4 secciones con preguntas abiertas + nota de prensa**: 1 contexto, pregunta e hipótesis · 2 conoce tu base · 3 mis análisis (bloque del ⭐ principal con 4 preguntas y bloque opcional de 3, para copiar por cada análisis) · 4 conclusión · 5 nota de prensa (sin cambios de formato, con sus `___`). Se eliminó la sección «pregunta distinta». Bitácora en preguntas.
- **Solucionario:** modelo reescrito con la estructura nueva. El Análisis 1 es el ejemplo de la galería (entregarlo tal cual vale 0 en originalidad) y el Análisis 2 (bicicletas, columna fuera de las sugeridas) es el original; las cifras salen de los datos.
- **Rúbricas (estudiantes e interna):** «Conoce su base» = 5 mínimo + 10 originalidad, con tres niveles (10 / 5 / 0); sin tope de análisis pero cada uno con su explicación; cuenta el más original bien explicado; **análisis principal ⭐** (alimenta diapositivas 3-5, nota de prensa y Defensa); corrección acotada al principal y al más original. Mapas de «dónde se corrige» con la nueva numeración.

**Pendiente de confirmar con Diego:** quién decide si una pregunta «cambia la comparación» (propuesta: el corrector, comparándola con el ejemplo de su base).

## 2026-10-20 (noche, 3) — Columnas y códigos dentro de cada ejemplo, y texto antes de cada celda

**Pedidos de Diego:** dentro de cada ejemplo plegado de base, mostrar primero las columnas sugeridas y luego el ejemplo aplicado (más compacto, se abre solo lo necesario), con los códigos especiales en esos mismos bloques; y que en el cuaderno de Código el texto explicativo vaya **antes de la celda donde se aplica** (por ejemplo, el Paso 1 daba las 3 instrucciones juntas), revisando el resto.

**Qué se hizo**
- **Plegables por base:** cada `<details>` trae (1) las 5 columnas sugeridas con su rol, (2) los códigos especiales cuando la base los tiene (SIMCE por establecimiento, Matrícula y Subvenciones; con la advertencia de que «rural» se codifica distinto en SIMCE) y (3) el ejemplo aplicado. Desaparecen la tabla global de columnas sugeridas y la nota global de códigos, que ocupaban celdas aparte; el bloque pasó a estar dentro de «Mi base», antes del Paso 1.
- **Paso 1 intercalado:** cada instrucción va justo antes de su celda (1 abrir la base → 2 mirar las 5 columnas con la ficha → 3 explorar más allá), en lugar de las tres juntas arriba.
- **Resto del cuaderno revisado:** los Conceptos 1-5 y los Pasos 2-3 ya tenían el texto inmediatamente antes de su celda. Se separaron las tablas de referencia de «Para ir más allá», que queda pegado a su código; los enlaces a los PDF pasan a la celda de texto que precede a los links de las bases; se corrigió la Guiada, que remitía a una tabla que ya no existe.

## 2026-10-20 (noche, 4) — Ejemplo de pareja con nota 7 (DEMRE)

**Pedido de Diego:** un solo Colab, al grano, que muestre cómo se vería una pareja que saca un 7, con la base más popular y con el código al inicio y el texto respondido al final.

**Qué se hizo**
- Nuevo `Clase 38y38b - Ejemplo Pareja Nota 7 (DEMRE).ipynb` (ejecutado, con salidas): pareja ficticia, base **DEMRE** (la más elegida, 5 equipos).
- **Código:** Paso 1 (abrir y ficha), ⭐ Análisis 1 (Medicina, promedio del último seleccionado por universidad), Paso 3, y Análisis 2 (suma de vacantes de Medicina por universidad) con su Paso 3.
- **Texto:** espacios y cifras, secciones 1 a 4, nota de prensa en formato noticia y bitácora de las tres sesiones. Cifras verificadas contra la ejecución.
- Es material de referencia para Diego; no se ha publicado a estudiantes ni pusheado.
