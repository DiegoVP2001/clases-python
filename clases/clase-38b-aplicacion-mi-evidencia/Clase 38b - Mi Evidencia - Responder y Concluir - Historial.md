# Historial — Clase 38b (Mi evidencia y mi conclusión)

## 2026-10-19 — Diseño y generación (v1, pendiente de aprobación)

**Por qué existe.** Patrón contenido → aplicación del bloque pandas: la N°38 (receta de 5 espacios: filtrar, agrupar y resumir, ordenar, graficar) se aplica sobre la base v2 de cada equipo y la pregunta elegida en la 37b. Se dicta el jueves 22-oct (~77 min). Producto: 1 tabla o gráfico que responda la pregunta + qué NO se puede concluir + conclusión. El Colab narrado se entrega hasta el viernes 23-oct (Producto 35% + Proceso 15%). Sin Ejercicios, PPT ni Ticket de Salida. Se corta el círculo de crítica formal entre grupos.

**Fuente de verdad usada.** El Spec de la N°38 (versión del Plan de Cambios del 17-oct, con los cinco espacios `COL_FILTRO`, `VALOR`, `COL_GRUPO`, `COL_NUMERO`, `N`), no la Vista Previa de la 38b (que usaba `COLUMNA_FILTRO`/`GRUPO`/`NUMERO`). La N°38 se dicta el martes 20-oct, así que **no se pudo verificar que se dictara como se planeó**: revisar su Historial después del martes y ajustar el torpedo si cambió algo.

**Decisiones**
- Molde de estilo: cuaderno de la 37b (foto del LUN como *attachment*, rúbrica, equipos, links v2 comentados, índice «Plan de hoy», cada paso con «Lo que necesitas saber» + «Lo que debes hacer» + celda de código vacía + celda 📝).
- **Torpedo** = las cuatro preguntas de la receta + tabla «si tu pregunta es…» (incluye «no filtrar») + celda de código comentada con la receta sobre guaguas + resumen de la limpieza de la 37 para quien faltó. Marcadores a reemplazar y recordatorio de revisar el cuaderno de la 37b debajo. Texto «adapta / analiza caso a caso», sin «copiar y pegar».
- **Pasos:** 0 Retoma tu tabla y tu pregunta · 1 Traduce tu pregunta a los cinco espacios · 2 Produce tu evidencia · 3 Mira lo que salió · 4 Qué NO puedo concluir · 5 Mi conclusión. Los pasos 4 y 5 no llevan celda de código (son solo escritura).
- **Paso 3** incluye cuántas filas hay detrás de cada barra (`.count()`) y el caso del filtro que deja 0 filas (el gráfico falla con `IndexError`; se comprobó al simular).
- **Paso 4** trae una tabla de tipos de límite reales (promedio de promedios, filas descartadas, pocas filas detrás, columna que no mide lo que se cree, alcance, asociación no es causa) para evitar frases de relleno.
- Encabezado «Curso: 3ro y 4to medio» (memoria `feedback_curso_3ro_y_4to_medio_encabezado`).
- Sin PDF de apoyo: la tabla de límites y el torpedo alcanzan.

**Qué se produjo**
- `generar_cuaderno.py` → `... - Clase.ipynb` (34 celdas) y `... - Solucionario.ipynb` (22 celdas, ejecutado contra la URL real).
- Solucionario: tabla de qué se revisa por paso (Producto/Proceso), pasos 0-5 resueltos con SIES (*¿qué áreas tienen mejor empleabilidad al 1er año en universidades?*, `.mean()`), y nota docente con una pregunta plausible y su límite típico para cada base inscrita, recalculada en vivo sobre los CSV.

**Verificación**
- `nbformat.validate` pasa en ambos; Solucionario ejecuta sin errores.
- Cuaderno de estudiantes ejecutado completo con celdas vacías: sin errores y sin outputs guardados.
- Revisión de texto: sin `$` sin escapar, sin `<details>`, sin menciones a la modalidad de trabajo, sin «copiar y pegar», sin tabla de errores típicos; `foto_lun.png` como *attachment*; los 10 links v2 y el Diccionario existen.
- Receta simulada con 10 preguntas en 6 bases (SIES, DEMRE, CONASET, Hospitalarias mensual y anual, SIMCE, Matrícula): todas producen el gráfico sin errores.
- Cifras del Solucionario medidas sobre los CSV (SIES: 1.690 filas, 1.190 de universidades, Tecnología 0,787 y Humanidades 0,412; filas por área desde 16 hasta 266).

**Corrección durante la generación.** Primera versión del Solucionario decía que en el Paso 0 se descartaban filas de SIES; la ejecución mostró 0 perdidas (`Empleabilidad 1er año` no tiene vacíos). Se corrigió el texto. También se precisó que las áreas con pocas carreras son Humanidades (16), Agropecuaria (29), Derecho y Ciencias Básicas (31).

**Pendiente**
- Aprobación de Diego antes de subir nada (el repo es público).
- Revisar el Historial de la N°38 tras dictarla (mar 20-oct) y ajustar si la receta cambió.
- Con aprobación: commit con pathspec explícito (`generar_cuaderno.py`, los 2 `.ipynb` y este Historial; sin Prompt ni Vista Previa) y fila en `Historial-Curricular.md`.
