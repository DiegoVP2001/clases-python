# Historial — Clase 37b (Mi tabla lista y mi pregunta)

## 2026-10-14 — Ajustes de Diego tras revisar el cuaderno (v2)

**Cuaderno (`generar_cuaderno.py`, regenerado)**
- Debajo del torpedo se agregó un aviso: `col`, `col1` y `col2` son marcadores que deben reemplazarse por los nombres de **sus** columnas (copiados desde `list(tabla.columns)`), y un recordatorio de revisar el cuaderno de proceso anterior (Clase 36b) para retomar su trabajo.
- Se quitó la tabla «Errores típicos a evitar».
- «Los códigos de la Clase 37, para copiar y pegar» pasa a **«Los códigos de la Clase 37»**: sin alusión a copiar/pegar ni a descomentar; se presenta como referencia para analizar bien, caso a caso, qué hace cada línea y de qué columna parte.
- La sección «Estrategia: qué columnas elegir…» se reemplazó por un **índice «Plan de hoy»** (qué se hace en cada uno de los 6 pasos y para qué). Las explicaciones que estaban juntas (dos tipos de columnas, método A-B-C-D, tabla «mira y decide», ejemplos de cordura, uso de `.notna()`) se **intercalaron en el paso donde se necesitan**, cada una como «Lo que necesitas saber» seguida de «Lo que debes hacer».
- Se eliminaron «Varias columnas a la vez» y «Tres avisos» por confundir sin aportar (se conservó solo lo esencial dentro de los pasos: una línea por columna, copiar nombres desde `list(tabla.columns)`).
- Todas las menciones al Excel pasan al PDF; el Solucionario se actualizó igual.

**Excel descartado → PDF estático.** Diego no quiere el Excel porque, al abrirlo con otro idioma o configuración regional, podría desplegar mal los ejemplos. Se reemplazó por `Clase 37b - Mi Tabla - Muestra de las Bases.tex/.pdf` (generado por `generar_muestra_pdf.py`, compilado con tectonic, 15 páginas apaisadas): portada con «qué mirar» + índice con hipervínculos, y una sección por base con **todas** sus columnas y las mismas 6 filas reales de antes (semilla 37, cobertura de formatos), traspuestas (cada fila de la muestra es una columna del PDF) para que quepan las bases de hasta 71 columnas. Los valores son el texto literal del CSV: se desactivó la separación silábica y las ligaduras/comillas tipográficas de TeX para que el dato no cambie (p. ej. `O'HIGGINS` con comilla recta). Las notas de `MARGEN_P25_MENOS_ULTIMO` (DEMRE) y `Egresos_por_dia` (Hospitalarias mensual) pasan a una caja «Ojo con esta base» al final de su sección. El PDF **no muestra el `.dtype`**: ese contraste lo hacen los estudiantes en el Paso 2. Verificación: cada palabra de las 6 filas de las 10 bases aparece en el texto del PDF; revisión visual de varias páginas. Los archivos del Excel quedaron en `_descartado-excel/`.
- Entrega: sigue por Classroom (decisión previa); al ser un PDF podría enlazarse desde GitHub como el Diccionario si Diego lo prefiere.

## 2026-10-14 — Diseño y generación

**Por qué existe.** Patrón contenido → aplicación del bloque pandas: la N°37 (limpiar a número + descartar filas) se aplica sobre la base v2 de cada equipo. Se dicta el lunes 19-oct (~77 min), abre con la política de IA y cierra con «mi pregunta». Diego perdió clases y hay mucha ausencia, así que el cuaderno es **independiente de las clases anteriores** y trae el código de la N°37 dentro (no hace falta abrir el Solucionario, como pasó en la 36b).

**Decisiones**
- **Vista Previa anterior superada.** `Vista Previa - N37b Conceptos Esenciales.ipynb` seguía la versión recortada de la N°37 (sin `strip` ni `dtype`). Diego confirmó que se enseñó la de 5 conceptos; la Vista Previa queda como borrador histórico.
- **«Receta segura» descartada.** La idea inicial era una receta única (`,` → `.`) para todas las bases. No es segura: con punto de miles (`2.908`) convierte en silencio a 2,908 (Subvenciones: 111.772 de 123.361 valores en `SUBV_ASISTENTES_EDUCACION`). Se reemplazó por mirar y decidir por columna.
- **Método A-B-C-D** (Mirar → Decidir → Convertir → Comprobar) con la tabla «mira y decide». Si el `.dtype` ya es número, no hay nada que limpiar.
- **Torpedo con un solo cambio** respecto al resumen de la N°37: la fila 3 pasa de «Sacar el punto de miles» a «Arreglar el separador (según lo que veas)», porque las bases del proyecto usan coma decimal y la línea de la clase las deja en `NaN` o mal escaladas (SIES `0.65` → 65).
- **Una sola celda de código comentada** con el código de la N°37 sobre guaguas, un título por concepto y solo la línea nueva de cada paso (`n` → `n_sin_espacios` → `n_sin_puntos` → `cantidad_guaguas`); `import` y `read_csv` una sola vez; variantes de coma/punto decimal comentadas en el bloque 3.
- **Bases v2 sin tocar.**
- **Excel de muestras** (`Clase 37b - Mi Tabla - Muestra de las Bases.xlsx`, generado por `generar_muestra_excel.py`): una hoja por base, 6 filas reales como texto literal, y comentario en el encabezado de las dos columnas que parecen texto pero ya son número (`MARGEN_P25_MENOS_ULTIMO` en DEMRE y `Egresos_por_dia` en Hospitalarias mensual). **Se entrega por Classroom, no por GitHub**; el cuaderno solo nombra el archivo.
- Foto del LUN (`clase-35-listas/foto_lun.png`) incrustada como *attachment* base64 en la portada.
- Preguntas 📝 de reflexión (qué representa, por qué decidiste esa línea, cómo sabes que está bien, qué se perdió y a quién deja fuera), no de transcribir resultados. Paso 6 con los 2 filtros.
- Sin Ejercicios, PPT ni Ticket de Salida (clase de aplicación).

**Qué se produjo**
- `generar_cuaderno.py` → `Clase 37b - Mi Tabla - Limpiar y Preguntar - Clase.ipynb` (34 celdas) y `... - Solucionario.ipynb` (23 celdas, ejecutado contra la URL real con DEMRE).
- Solucionario: tabla de Proceso 15%, Pasos 1-6 con DEMRE (dos `PROM_OBLIGATORIAS_*` con coma + `MARGEN_P25_MENOS_ULTIMO` ya numérica), tabla docente de qué línea va en cada base y celdas que recalculan en vivo qué pasa con la línea equivocada.

**Verificación**
- `nbformat.validate` pasa; Solucionario ejecuta sin errores; el cuaderno de estudiantes corre completo con celdas vacías (la celda comentada no hace nada) y sin outputs guardados.
- Para cada columna de texto numérico de las bases 01, 02, 03, 04, 08a, 09a, 09b y 06, la línea de la tabla recupera todos los valores originales (0 no recuperados); 05 y 07 no tienen columnas de texto numérico.
- Cifras reales medidas: DEMRE 2.150 filas, 3 vacías en `PROM_OBLIGATORIAS_ULTIMO_SELEC`; quitar el punto deja 1.048 de 2.150 en `NaN`; en SIES quitar el punto lleva el máximo de 1,0 a ~4,8e16.
- Sin `$` sin escapar, sin `<details>`, sin menciones a la modalidad de trabajo ni a «receta segura»; la foto está como attachment; los 10 links v2, el Diccionario y `bbdd_guaguas.csv` existen.

**Corrección durante la generación.** Las cifras de la primera versión del Solucionario (p. ej. «1.045 de 2.147») venían del prompt; se reemplazaron por las medidas sobre el CSV (1.048 de 2.150) y se corrigió que `PROM_OBLIGATORIAS_ULTIMO_SELEC` mezcla enteros y decimales con coma.

**Pendiente**
- Aprobación de Diego antes de subir nada (el repo es público). El `.xlsx` no se sube; va por Classroom.
