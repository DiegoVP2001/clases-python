# Historial — Clase 35

## 2026-09-23 — Especificación aprobada
- Objetivo: extraer datos de una fila real de `bbdd_guaguas.csv` con `split(",")`, índice y slicing, con atención al detalle.
- Actitud elegida tras dos rondas de opciones: **Atención al detalle**.
- Alcance acotado en dos rondas de iteración: se descartó modificar por índice, `+`/`*` de listas, `in` y listas anidadas — quedó en `split()` + índice ± + slicing + `int()`, con `[ ]`/`len()` solo mostrados al pasar.
- Se agregó una sección inicial "Presentación de proyecto" (15-20 min, antes del Haz Ahora) para el pitch del menú de 9 bases, con mención breve al lanzamiento completo del 13-oct (Diego había nombrado por error el HTML de rúbricas del 13-oct para el 28-sep; se aclaró la fecha correcta y se resolvió incluyendo ambos momentos).
- A pedido de Diego, el dataset se nombra `bbdd_guaguas.csv` (convención de nombres de bases de datos reales) en vez de "el archivo".
- Estructura completa aprobada en una sola iteración tras ver el código de cada contenido.

## 2026-09-23 — Colab de clase aprobado
- Archivos: `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json`, `Ticket de Salida.pptx`
- Generados con la skill `generar-colab-clase`, con la sección "🎉 Presentación de proyecto" insertada al inicio de `Clase.ipynb` (no estándar de la plantilla, específica de esta clase).
- Ambos notebooks ejecutados sin errores; outputs limpiados fuera del ICN; verificado sin fugas de soluciones al notebook de estudiante.
- Diego agregó el link real del formulario de inscripción/elección de base (gestionado externamente en Google Forms, fuera de este repo) — pendiente incorporarlo al texto de la sección "Presentación de proyecto" si Diego quiere que quede embebido en el notebook.

## 2026-09-24 — Colab de clase corregido
- **Causa:** Diego detectó que el ICN no siguió el formato piloteado en Clase 33 ("Idea clave → ✍️ Escríbelo tú" con celda incompleta) porque quedó registrado como "demo, NO default" y `disenar-clase` nunca pedía los campos `Instrucción`/`Punto de partida` — ver regla 25 nueva del CLAUDE.md raíz, que ahora lo deja como default para todas las clases.
- **ICN:** sube de 4 a 5 conceptos — se agrega "¿Qué es un CSV?" al inicio, con tabla comparativa Excel/CSV (columnas del Haz Ahora, 3 filas con `...` para representar lo largo). Los 5 conceptos pasan al formato "Escríbelo tú"; el `Ejemplo` completo de cada uno se hizo autocontenido (antes los Conceptos 2-4 dependían de `datos` definido en el Concepto 1). ICN sube de 15 a 17 min, Independiente baja de 17 a 15 (la suma de los 5 pasos se mantiene en ~54 min).
- **Voz colectiva:** se reescribió el Haz Ahora, la Guiada y los ejercicios para no nombrar a Diego en tercera persona ("Diego trae...", "les pide") — ahora en plural colectivo ("nos pide ayuda", "la periodista nos pasa..."), a pedido explícito de Diego (feedback sistémico, guardado en memoria).
- **Torpedo de "Presentación de proyecto":** se reemplazó el puntero al Catastro por el contenido completo (voz colectiva, sin nombrar a Diego): pitch, tabla de las 9 bases con una pregunta de partida cada una, cómo se elige la base (incluye que varios equipos pueden compartir base), tabla de equipos (individual/pareja) y tabla de fechas clave, con el link real del formulario ya embebido.
- **Criterio de equipos:** cambia de "parejas o tríos" a "individual o pareja (máximo 2), a elección" — actualizado también en los documentos de `clases-octubre/` (Plan y Pendientes, Catastro, Rúbricas, Ficha de coevaluación, Formulario de inicio, Versión Estudiantes). El Google Form real lo actualiza Diego directamente.
- **Bug del generador corregido:** la tabla-resumen del ICN (`generar_resumen_icn_markdown`) se tragaba la nota adicional de un concepto porque la regex de `Resumen tabla` no cortaba en `\n- `; ahora sí. Verificado sin regresión regenerando Clase 33 (0 diferencias salvo un ajuste manual preexistente de Diego en la celda de la Guiada, ajeno a este fix).
- Ambos notebooks (`Clase.ipynb`, `Solucionario.ipynb`) regenerados con `generar-colab-clase`, ejecutados con `nbconvert --execute` sin errores, outputs limpiados; verificado sin fugas de soluciones.
- **Foto de la nota del LUN incrustada:** Diego pidió agregar `foto_lun.png` debajo del texto "De dónde partimos". Se incrustó como *attachment* del notebook (`cell.attachments`, base64 dentro del `.ipynb`) en vez de referenciarla como archivo aparte — así se ve en Colab sin depender de que la imagen viaje junto al `.ipynb` o de un link externo. El `.ipynb` sube de ~30 KB a ~1 MB por esto.
