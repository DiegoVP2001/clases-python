# Historial — Clase 19 - Evaluación Condicionales

## 2026-08-19 — Revisión de Diego Cifuentes (Atrasada) y cierre final de la evaluación

**Motivo:** Diego Cifuentes Tessada (N°27) — único pendiente desde 2026-08-14 — rindió la reposición (`estudiantes/diego.ipynb`, identidad confirmada por el propio encabezado del notebook: "nombre: diego cifuentes").

**Revisión de su código**, ejecutando cada ítem con un runner (no leyendo el output pegado), contra la rúbrica ya calibrada en `rubrica_parcelada_atrasada.md`:
- Sección 1 (70/70): los 4 programas completos correctos, sin desviaciones.
- Sección 2 (21/30): 5 ítems perfectos. 2A.2 con 3/4 (omite paréntesis en `a and b or c` — mismo patrón parcial ya calibrado con Maura). 2B.2 con 0/5 (cambió `>` por `==` en vez de `>=` — mismo patrón full ya calibrado). **2B.5, patrón nuevo:** mezcla `<=`/`>=` en vez de reordenar de mayor a menor umbral — acierta el valor de ejemplo (12) pero, verificado contra el rango completo (0-30), falla en 7/15 valores probados (incluye asignar "VIP" a solo 4-6 compras). Diego (profesor) decidió parcial, 2/5 pts.
- **Total: 91/100 → nota base 6,5.**

**Décimas de bono:** tenía 3 décimas registradas (`decimas_ejercitacion.csv`, fila N°27, vía cuenta compartida "polar tv") nunca consumidas — estuvo ausente sin justificar el día original, así que no se gastaron ahí. Diego decidió explícitamente **no aplicarlas** en esta instancia → **decimas = 0, nota final = 6,5 (Aprobado)**.

**Artefactos actualizados:**
- `version-atrasada/revision/notebooks_atrasada/diego_cifuentes.ipynb` (copia de `estudiantes/diego.ipynb`) + re-ejecutado `extraer_codigo_atrasada.py` → `codigo_extraido_atrasada.json` ahora con los 5 estudiantes.
- `puntajes.json`: agregado `diego_cifuentes` (11 ítems + razones); `rubrica_parcelada_atrasada.md` y `criterios_calibracion_atrasada.json` actualizados con su detalle y el patrón nuevo de 2B.5.
- `generar_devolucion_atrasada.py`: agregado a `NOMBRE_COMPLETO`, mensaje de apertura personalizado, y `decimas["diego_cifuentes"] = 0` (explícito, por decisión de Diego). Generado y movido `Diego Alonso Cifuentes Tessada - Revisión Detallada.ipynb` a `EVALUACIONES-REVISADAS/PRUEBAS/Clase 19 - Evaluación Condicionales - 2026-07-28/` (mismo destino ya usado para los otros 24).
- `generar_resumen_final_clase19.py`: ya tenía a Diego Cifuentes mapeado en `ATRASADOS_MAP`, no necesitó cambios de código — solo recorrerlo. Recalculado `revision-consolidada/resumen_final_clase19.md/csv/xlsx`.

**Cierre de la evaluación completa:** 31 estudiantes en registro, **26 con nota (19 aprobados, 73%), 0 pendientes, 5 ausentes** sin instancia de reposición agendada (Lucas Valenzuela, Francisca Parra, Paula Inzunza, Víctor Olguín, Nacor Pardo). Promedio 5,6. Los 25 Colabs de devolución de Día+Atrasada están completos en `EVALUACIONES-REVISADAS/PRUEBAS/Clase 19 - Evaluación Condicionales - 2026-07-28/`. `version-atrasada/revision/colabs_devolucion/` se eliminó tras el movimiento (misma limpieza que el 2026-08-18). Nada de `revision/`, `revision-consolidada/` ni `EVALUACIONES-REVISADAS/` se sube a git (regla permanente, repo público).

## 2026-08-18 — Revisión de Simón Abrahams (Atrasada), método de combinación y consolidación final

**Motivo:** Simón Abrahams (N°25) rindió la Atrasada. Es el único caso con intento en el día original (34/100) además de la Atrasada — el método de combinación había quedado explícitamente sin definir el 2026-08-14 (`METODO_COMBINACION_SIMON = None`).

**Revisión de su código (`estudiantes/simon.ipynb`)**, ejecutando cada ítem con un runner (no leyendo el output pegado), aplicando la rúbrica ya calibrada en `rubrica_parcelada_atrasada.md`:
- Sección 1: 1.1 (18/18) y 1.2 (12/12) correctos. 1.3 (**0/24**) — compara `"VIP"` en vez de `"vip"`, le faltan por completo las ramas "general"/"preferencial", y `lleva_acompañante = "si" or "no"` no usa el input real (esa expresión vale siempre `"si"` en Python). 1.4 (**0/16**) — celda interrumpida sin terminar; pide el efectivo siempre sin importar la entrada digital, la estructura `if entrada == "no": if entrada == "si":` es lógicamente inalcanzable, y el efectivo se compara con `== 6000` exacto (no cubre "no alcanza"). Ambos patrones encajan en el nivel "full" ya escrito en la rúbrica, sin necesitar aprobación de patrón nuevo.
- Sección 2: los 7 ítems cortos perfectos (acepta 1:1 en los 7).
- **Total Atrasada: 60/100 → nota 4,6.**

**Cruce con el día:** se comparó ítem por ítem contra `version-dia/revision/puntajes_evaluacion2.json` (34/100 → nota 3,5 con su décima ya incluida) usando la tabla de correspondencia de contextos del Historial (entrada 2026-07-28). En los 11 ítems la Atrasada iguala o supera al día — no hay ningún ítem donde el día aportara algo mejor. Se propusieron 3 métodos (más a menos benevolente): "mejor de las dos" (4,6), "solo la Atrasada" (4,6 — coincide con "mejor" porque la Atrasada domina en todos los ítems) y "promedio" (4,1). **Diego confirmó "solo_atrasada" → nota final 4,6, Aprobado.**

**Artefactos actualizados:**
- `version-atrasada/revision/notebooks_atrasada/simon_abrahams.ipynb` (copia de `estudiantes/simon.ipynb`) + re-ejecutado `extraer_codigo_atrasada.py` → `codigo_extraido_atrasada.json` ahora con los 4 estudiantes.
- `puntajes.json`: agregado `simon_abrahams` (11 ítems + razones), recalculado por el mismo motor (`generar_devolucion_atrasada.py`) — decimas de Simón fijadas explícitamente en 0 (ya las gastó en la nota del día; sumarlas de nuevo sería contarlas dos veces).
- `rubrica_parcelada_atrasada.md` y `criterios_calibracion_atrasada.json`: agregado el detalle de Simón, movido de "pendientes" a calibrado.
- `generar_devolucion_atrasada.py`: agregado su mensaje de apertura personalizado; generado `colabs_devolucion/simon_abrahams - Revisión Detallada.ipynb`.
- `generar_resumen_final_clase19.py`: `METODO_COMBINACION_SIMON = "solo_atrasada"` (fijado, ya no `None`). Recalculado `revision-consolidada/resumen_final_clase19.md/csv/xlsx` y `Notas.xlsx` — ahora 25 con nota (18 aprobados), solo Diego Cifuentes (N°27) pendiente.

**Consolidación pedida por Diego:** se creó `revision-consolidada/colabs_devolucion/` con los 25 Colabs de devolución finales en una sola carpeta (21 del día + Alain/Cristóbal/Maura/Simón de la Atrasada — para Simón se usó la versión Atrasada, no la del día, porque es la que cuenta como nota final). Los 4 de la Atrasada se renombraron de su clave interna (`alain_moyano`, etc.) a nombre real, igual que los del día. Las carpetas originales (`version-dia/revision/colabs_personalizados/`, `version-atrasada/revision/colabs_devolucion/`) se dejaron intactas — son el output de origen de cada generador; la carpeta nueva es solo para tener todo junto a mano. Sigue sin subirse nada de esto a git (regla permanente, `revision*/`).

**Pendiente:** Diego Cifuentes (N°27) — no ha rendido la Atrasada.

## 2026-08-18 (cont.) — Cierre: carpeta compartida `EVALUACIONES-REVISADAS/PRUEBAS/`

**Motivo:** Diego formalizó el cierre de toda revisión con el mismo destino ya usado para Controles (`CLAUDE.md` §"Workflow: evaluaciones individuales sumativas — generación", paso 5, y `revisar-evaluacion/SKILL.md`): los `.ipynb` personalizados finales se mueven a `clases/EVALUACIONES-REVISADAS/PRUEBAS/<Clase NN - Nombre evaluación - fecha>/`, la carpeta que Diego comparte tal cual con el curso — nunca resúmenes/Excel/JSON agregados, solo el cuaderno de cada estudiante.

**Ejecutado para Clase 19:** creada `EVALUACIONES-REVISADAS/PRUEBAS/Clase 19 - Evaluación Condicionales - 2026-07-28/` (fecha del día original; la Atrasada fue el 2026-08-06). Movidos ahí los 25 Colabs de devolución finales — **movidos de verdad** (no copiados) desde `version-dia/revision/colabs_personalizados/` (21) y `version-atrasada/revision/colabs_devolucion/` (Alain, Cristóbal, Maura, Simón), y renombrados de nombre corto/clave interna a **nombre completo real** tomado de la nómina oficial (`referencia-estudiantes/lista-estudiantes.md`), igual convención que ya usa `CONTROLES/`.

**Excepción intencional:** el Colab del día de Simón (34/100, en `Logro 0-59%`) **no se movió** — quedó superado por su nota de la Atrasada (60/100, la que cuenta como final) y compartirlo confundiría al estudiante con un puntaje que no es el suyo. Se dejó tal cual en `version-dia/revision/colabs_personalizados/Logro 0-59%/` (dentro de `revision/`, nunca compartido ni subido a git).

**Limpieza:** se eliminó `revision-consolidada/colabs_devolucion/` — la carpeta que había armado la vuelta anterior como "todo junto" quedó redundante en cuanto se formalizó el destino oficial (`EVALUACIONES-REVISADAS/PRUEBAS/`, verificado 25/25 archivos antes de borrar). También se eliminaron las subcarpetas `Logro 60-79%` y `Logro 80-100%` de `version-dia/revision/colabs_personalizados/` y la carpeta `version-atrasada/revision/colabs_devolucion/`, ya vacías tras el movimiento.

**Estado final de `revision/` para esta evaluación:** solo quedan los insumos internos (código extraído, `puntajes.json`, rúbrica calibrada, scripts) — ningún cuaderno de estudiante. Nada de esto se sube a git (`clases/**/revision*/` y `clases/EVALUACIONES-REVISADAS/` en `.gitignore`).

## 2026-08-14 — Script consolidador de resumen final (Día + Atrasada)

**Motivo:** Diego pidió un plan para ordenar la entrega de esta evaluación. Estado encontrado al auditar: la versión del día ya tenía sus 22 calificaciones y sus 22 Colabs de devolución listos (Diego confirmó el gate ya aprobado); faltaba solo la Fase 6 (resumen final del curso), nunca generada pese a que el plan de seguimiento (`version-dia/revision/PLAN_REVISION_EVALUACION2.md`) había quedado desactualizado. Diego pidió explícitamente **dejar todo listo para correr un solo comando** cuando falten resolver Simón y Diego Cifuentes (Atrasada) y el método de combinación de la nota de Simón — sin tener que rearmar el resumen a mano cada vez.

**Artefacto nuevo:** `generar_resumen_final_clase19.py` (raíz de esta carpeta, fuera de `revision/` — es código, no datos). Combina `version-dia/revision/puntajes_evaluacion2.json` (31 registros: 22 calificados + 9 ausentes) con `version-atrasada/revision/puntajes.json` (crece a medida que se califica), aplicando la misma fórmula de nota (`calcular_nota` de `tools/review_eval/colab_devolucion.py`, exigencia 50%) y las mismas décimas de bono (`decimas_ejercitacion.csv`) ya usadas en los Colabs de devolución. Produce `revision-consolidada/resumen_final_clase19.md/csv/xlsx`.

**Se puede correr en cualquier momento sin romperse:** a quien de la Atrasada aún no rinde lo deja como "Pendiente"; a Simón (única persona con intento el día + Atrasada) lo deja como "PENDIENTE — falta definir método de combinación" mientras `METODO_COMBINACION_SIMON` (constante al inicio del script) siga en `None` — Diego lo fija ahí (o pasa `--metodo-simon promedio/mejor/solo_atrasada`) el día que decida, y basta con volver a correr el script.

**Corrección de seguridad aplicada de paso:** el `.gitignore` protegía `clases/**/revision/` (nombre exacto) pero no una carpeta como `revision-consolidada/`, que igual contiene notas y nombres reales. Se generalizó el patrón a `clases/**/revision*/` para que cualquier carpeta de este tipo quede excluida por defecto, no solo la que se llama literalmente `revision`.

**Resultado al correrlo hoy (estado real, sin decidir el método de Simón):** 24 con nota (17 aprobados, 7 reprobados; promedio 5,6), 2 pendientes (Simón, Diego Cifuentes — no han rendido la Atrasada), 5 ausentes sin instancia de reposición agendada (Lucas Valenzuela, Francisca Parra, Paula Inzunza, Víctor Olguín, Nacor Pardo). Nada de `revision-consolidada/` se sube a git (misma regla permanente que `revision/`).

**Pendiente para cerrar la entrega:** definir canal de entrega de los Colabs a cada estudiante (Classroom u otro — no definido en esta sesión), y resolver antes el hallazgo de Alain (ítems 1.1/1.2 de la Atrasada sin relación al enunciado — conversarlo con él).

## 2026-08-14 — Revisión de la versión Atrasada (3 de 5 estudiantes con justificación)

**Motivo:** 3 estudiantes llegaron atrasados a rendir la reposición y ya entregaron (`estudiantes/alain_eva.ipynb`, `estudiantes/ev_cricri.ipynb`, `estudiantes/maura.ipynb`). Simón Abrahams Delgado (N°25) y Diego Cifuentes Tessada (N°27) también están en el grupo de atrasados pero **no han rendido todavía** (justificación) — quedan pendientes de una revisión futura, no forman parte de este batch.

**Identidad de `ev_cricri.ipynb`:** el encabezado no traía nombre declarado. Confirmado por Diego como Cristóbal Alonso Muñoz Cubillos (N°19) — registrado en `alias-cuentas-conocidas.md`.

**Flujo aplicado (adaptado de la skill `revisar-evaluacion`, escala reducida a 3 entregas — sin batches paralelos ni gate de consolidación, innecesarios a esta escala):**
- Extractor propio `revision/extraer_codigo_atrasada.py` (la Atrasada tiene narrativa distinta a la Evaluación 2 del día, no comparte anclajes) → `revision/codigo_extraido_atrasada.json`, los 3 con los 11 ítems encontrados.
- Calibración de rúbrica sobre el código real, verificando **ejecutando** cada ítem (no leyendo el output pegado) → `revision/rubrica_parcelada_atrasada.md` + `revision/criterios_calibracion_atrasada.json`.
- `revision/puntajes.json` con los 3 estudiantes y sus notas.

**Hallazgos relevantes (confirmados ejecutando el código, no solo leyéndolo):**
- **Alain** (70/100, nota 5.2): los ítems 1.1 y 1.2 (30 pts) tienen código sin ninguna relación con el enunciado — un `while` contando "personas_contador" hasta 149/150, sin `input()` de kilómetros/batería ni condicionales. Los ítems 1.3 y 1.4 están perfectos. **Pendiente:** preguntarle directamente a Alain qué pasó ahí — podría ser una confusión de notebook o código de otra práctica que no alcanzó a borrar.
- **Cristóbal** (100/100, nota 7.0): todo correcto. Único caso de calibración menor: mensaje del Ítem 1.3 con redacción distinta a la pedida pero que igual distingue el caso — Diego aprobó puntaje completo, extendiendo el mismo criterio que ya regía en el Ítem 1.4.
- **Maura** (70/100, nota 5.2): Sección 1 casi perfecta salvo el Ítem 1.4, donde un bug de indentación propio saca el segundo `if/else` fuera del `else` del primero — el programa se cae con `NameError` en el camino "si" (falla el Ejemplo 1 del enunciado). Diego decidió mitad de puntaje (8/16), reconociendo que la lógica y el umbral estaban bien pensados. Sección 2 con 5 de 7 ítems en 0 pts: cambió operadores (`or`→`and` en 2A.2, `==`→truthy en 2B.1, `>`→`<` con mensajes invertidos en 2B.2), dejó sin corregir el bug de 2B.5, y en 2B.4 el `print()` final imprime un string literal en vez de la variable. Varios de estos se confirmaron adversarialmente (reponiendo valores originales que ella había cambiado) para no calificar solo por el ejemplo fijo.

**Fase 5 — Colabs de devolución y consolidación de notas (2026-08-14, mismo día):** Diego aprobó los 3 borradores sin cambios. Se generaron los Colabs finales (`revision/colabs_devolucion/`, motor `generar_devolucion_atrasada.py`) **con nota** (Diego confirmó explícitamente, exigencia 50%).

**Décimas de bono cruzadas:** `version-dia/revision/decimas_ejercitacion.csv` (bono de la Ejercitación de Clase 17, registrado 2026-07-28) quedaba explícitamente marcado como "insumo para cuando se revise la Clase 19" sin aplicar todavía a nadie — se confirmó que ninguno de los 3 lo tenía consumido (en `puntajes_evaluacion2.json` del día original figuran con `total: 0, decimas: None`, ausentes ese día). Valores: Cristóbal +4 décimas (sin efecto, ya estaba en el tope 7,0), Alain y Maura +0.

**Notas finales:** Cristóbal Muñoz 100/100 → 7,0. Alain Moyano y Maura Muñoz 70/100 → 5,2 cada uno.

**Siguiente paso:** falta la revisión de Simón Abrahams (N°25) y Diego Cifuentes (N°27) cuando rindan la reposición — mismo flujo, misma rúbrica ya calibrada en `rubrica_parcelada_atrasada.md` (sirve de referencia, no de fuente automática — sigue habiendo que revisar su código real). Nada de `revision/` está pusheado (regla permanente, repo público).

## 2026-07-28 — Reorganización en subcarpetas por versión

**Motivo:** con dos versiones de la evaluación conviviendo en la misma carpeta (regular y atrasada), Diego pidió separarlas en subcarpetas propias para no mezclar archivos.

**Cambio aplicado:** se movieron (con `git mv` los archivos ya trackeados) a:
- `version-dia/` — `generar_evaluacion.py`, los 3 notebooks regulares y `revision/` (insumos de corrección de la evaluación rendida en la fecha original).
- `version-atrasada/` — `generar_evaluacion_atrasada.py` y sus 3 notebooks (recién generados, aún no commiteados).

`Spec.md` e `Historial.md` se mantienen en la raíz de `clase-19-evaluacion-condicionales/` porque documentan ambas versiones. Ningún script necesitó cambios de código: ambos generadores calculan su carpeta de salida con `os.path.dirname(os.path.abspath(__file__))`, así que escriben automáticamente dentro de su propia subcarpeta.

## 2026-07-28 — Réplica "Atrasada" (reposición) para estudiantes que rinden después

**Motivo:** la evaluación original ya está publicada en el repo público (`Evaluación.ipynb`, `Solucionario.ipynb` y `Solucionario Estudiantes.ipynb` visibles en GitHub desde el 2026-07-16/21). Diego pidió una réplica para los estudiantes que la rindan atrasada, el **jueves 6 de agosto de 2026**, con la misma dificultad y puntaje pero reordenada y recontextualizada para que no sea posible copiar directamente las respuestas de quienes ya la rindieron.

**Artefactos nuevos:** `generar_evaluacion_atrasada.py` (script fuente de verdad, independiente de `generar_evaluacion.py` — no lo importa porque el contenido narrativo difiere en los 11 ítems) y sus 3 notebooks:
- `Clase 19 - Evaluación Condicionales - Evaluación (Atrasada).ipynb`
- `Clase 19 - Evaluación Condicionales - Solucionario (Atrasada).ipynb`
- `Clase 19 - Evaluación Condicionales - Solucionario Estudiantes (Atrasada).ipynb`

**Qué cambia respecto al original (nada de dificultad ni puntaje):**
1. **Se invierten las secciones:** Sección 1 = Programas completos (70 pts, antes era Sección 2), Sección 2 = Ítems cortos (30 pts, antes era Sección 1).
2. **Derangement dentro de cada sección** — ningún ítem/ejercicio quedó en su posición original:
   - Programas: Ej.1 Ahorro→Natación, Ej.2 Modo Fiesta→Batería PS5, Ej.3 Sala de juego→Fiesta Vendimia, Ej.4 Micro a Talagante→Convención videojuegos/anime.
   - Ítems cortos: 2A.1↔2A.2 (swap), 2B = corrimiento cíclico de 2 sobre el orden original (1B.3→2B.1, 1B.4→2B.2, 1B.5→2B.3, 1B.1→2B.4, 1B.2→2B.5).
3. **Los 11 contextos narrativos se reemplazaron por completo** (consultadas `referencia-intereses-estudiantes` y `referencia-isla-de-maipo` para variedad), manteniendo exactamente el mismo patrón lógico, tipo de dato y valores de umbral/puntos/tiempo por ítem — ver tabla de mapeo original→nuevo más abajo. Ningún contexto se repite con Clase 17, Clase 14, Clase 11/13, el apoyo individual ni con la evaluación original de Clase 19.

**Mapeo contexto original → contexto atrasada (referencia interna, no se publica a estudiantes):**

| Ítem | Original | Atrasada |
|---|---|---|
| Ej. Programas (18 pts, elif 4 niveles) | Ahorro semanal en dólares | Kilometraje semanal de natación |
| Ej. Programas (12 pts, if/else simple) | Modo Fiesta de una playlist | Batería del control de PS5 |
| Ej. Programas (24 pts, elif 3 + anidado) | Sala de juego según tu rango | Entrada a la Fiesta de la Vendimia |
| Ej. Programas (16 pts, if/else anidado en input) | Micro a Talagante | Convención de videojuegos y anime |
| 1A.1/2A.1 (and simple, 4 pts) | Concurso fotografía Instagram | Riego por goteo (parcela Isla de Maipo) |
| 1A.2/2A.2 (var1 and (var2 or var3), 4 pts) | Backstage festival de música | Modo cooperativo secreto de videojuego |
| 1B.1/2B.4 (bug `=` vs `==`, 4 pts) | Máquina expendedora | Casillero inteligente del gimnasio |
| 1B.2/2B.5 (bug `>` vs `>=`, 5 pts) | Torneo de básquetbol | Batalla de un juego de estrategia online |
| 1B.3/2B.1 (bug falta `:`, 4 pts) | Verificación TikTok | Plataforma de estudio en línea |
| 1B.4/2B.2 (bug indentación, 4 pts) | Parlante inteligente | Dron de reparto |
| 1B.5/2B.3 (bug orden `elif`, 5 pts) | Racha de días estudiando | Fidelidad en tienda de skate |

**Verificación:** se ejecutaron las 4 soluciones de Programas completos (8 combinaciones de ejemplo) y los 7 ítems cortos contra un intérprete Python — todos los resultados coinciden con el valor esperado documentado en cada celda del Solucionario. Puntaje total confirmado en 100 pts (70 + 30), igual que el original.

**Pendiente — política de publicación:** por el mismo motivo que el original (repo público), **no corresponde pushear ningún archivo de esta réplica hasta después de rendida la evaluación el 2026-08-06** — ni siquiera `Evaluación (Atrasada).ipynb`, porque su sola presencia en el repo antes de esa fecha podría alertar a otros estudiantes de que existe una versión distinta y motivar a buscarla. Diego debe confirmar explícitamente cuándo y qué subir (posiblemente: `Evaluación (Atrasada).ipynb` el mismo día de la reposición para que los estudiantes lo abran en Colab, y los dos Solucionarios recién después).

## 2026-07-28 — Registro de décimas de la Ejercitación (Clase 17) como insumo de bono

**Motivo:** antes de revisar esta evaluación, Diego pidió cruzar las 36 entregas de la Ejercitación de Clase 17 (trabajadas en pareja) contra la nómina oficial y dejar registradas las décimas que corresponden a cada estudiante, para sumarlas como bono al calcular las notas de esta evaluación.

**Artefacto generado:** `revision/decimas_ejercitacion.md` (+ `.csv`) — 32 filas (nómina completa), con Sección 1 / Ej.1-4 desglosados y el total (máx. +6 c/u). El detalle completo del método, el criterio "ligero" usado y las decisiones de identidad (cuentas con apodo, casos de pareja) quedó documentado en `Clase 17 - Ejercitación Evaluación - Historial.md` (entrada 2026-07-28), para no duplicarlo aquí.

**Estado:** el registro está listo pero **no se ha aplicado todavía** a ninguna nota de esta evaluación — queda pendiente para cuando se active la skill `revisar-evaluacion` sobre las entregas de Clase 19.

## 2026-07-27 — Auditoría pre-examen: fecha desincronizada + ambigüedad coma/punto decimal

**Motivo:** Diego pidió auditar `Evaluación.ipynb` en busca de enunciados poco claros, sin sentido o que evaluaran contenido no visto. Se detectaron dos problemas (ninguno de contenido curricular — la cobertura contra el Temario de Clase 17.5 y los Bloques 1-7 se verificó completa y correcta).

**Hallazgo 1 — fecha desincronizada:** el `.ipynb` vivo mostraba "martes 28 de julio, 2026" en el encabezado (con el "**75 minutos**" ya quitado de esa línea), pero `generar_evaluacion.py` y este Spec seguían generando "martes 21 de julio, 2026" — evidencia de una edición manual directa al notebook, sin pasar por el script (contra la convención de este proyecto). Como el examen efectivamente se rindió/rinde el 28 (hoy es 27, un día antes), se sincronizó el script y el Spec con esa fecha, preservando el ajuste ya hecho a mano.

**Hallazgo 2 — Ejercicio 3 (Ahorro semanal en dólares), ambigüedad coma/punto decimal:** el enunciado escribía los umbrales con notación chilena de coma decimal ("Entre 10 y 29,99 dólares", "Entre 30 y 59,99 dólares"), mientras el único ejemplo de input mostrado usa punto (`62.5`, formato que exige Python). Riesgo real: un estudiante podía escribir `29,99` literal en su código (se interpreta como tupla `(29, 99)`, `TypeError` al comparar) o tipearlo así en el `input()` (`ValueError` en `float()`). Ningún contenido previo aclaró la diferencia coma/punto. La solución oficial ni siquiera necesita ese literal (usa `< 30` directamente).

**Cambio aplicado (en `generar_evaluacion.py`, regenerados los 3 notebooks):**
- Umbrales de Ejercicio 3 reformulados sin decimales exactos: "Entre 10 y menos de 30 dólares" / "Entre 30 y menos de 60 dólares", en vez de "29,99"/"59,99". Coincide ahora con los límites `< 30` / `< 60` de la solución de referencia.
- Encabezado de fecha sincronizado a "martes 28 de julio, 2026" en el script (se quitó también el `| **75 minutos**` sobrante de esa línea, ya redundante con las Instrucciones generales).

**Verificación:** diff post-regeneración confirmó que los únicos cambios de contenido en los 3 notebooks fueron estos dos (más ruido esperado de IDs de celda). `Solucionario.ipynb` (profesor) no cambió texto porque no incluye la narrativa/lista "El programa debe" de los ejercicios, solo código y rúbrica.

## 2026-07-16 — Revisión: agregar "Qué se revisó" al Solucionario Estudiantes

**Motivo:** Diego pidió que el Solucionario Estudiantes indicara el criterio de revisión de cada ítem/ejercicio (qué se evaluó en la lógica), sin mencionar puntos.

**Cambio aplicado:** se agregó un campo `criterio` a cada uno de los 11 ítems/ejercicios en `generar_evaluacion.py` (una o dos frases describiendo qué exigía la lógica evaluada, ej. "que la condición exigiera ambas variables a la vez"). `build_solucionario_estudiantes_notebook()` ahora agrega un bloque `🔎 **Qué se revisó:** ...` justo después de cada solución — sin números de puntos ni el lenguaje de descuento del Solucionario del profesor.

**Verificación:** se regeneraron los 3 notebooks; diff confirmó que `Evaluación.ipynb` no cambió contenido (solo IDs) y `Solucionario.ipynb` tampoco (los criterios nuevos solo se usan en el notebook de estudiantes).

## 2026-07-16 — Solucionario para publicar a estudiantes

**Motivo:** Diego pidió un solucionario para publicar directamente a los estudiantes, distinto del `Solucionario.ipynb` existente (ese es fuente de verdad para el profesor/agente corrector — trae la rúbrica flexible de 3 niveles con lenguaje de descuento de puntos, que no corresponde mostrarle al curso).

**Advertencia hecha a Diego:** la evaluación se rinde el 2026-07-21 y esto se generó y publicó el 2026-07-16, es decir **antes** de rendirse — el repo es público, así que el solucionario queda expuesto a quien tenga el link desde ahora. Diego confirmó explícitamente que quiere publicarlo de inmediato, no esperar a después de la evaluación.

**Artefacto nuevo:** `Clase 19 - Evaluación Condicionales - Solucionario Estudiantes.ipynb`, generado por una nueva función (`build_solucionario_estudiantes_notebook()`) en `generar_evaluacion.py`. Reutiliza narrativas y soluciones de `ITEMS_1`/`EJERCICIOS_2` (misma fuente de verdad), pero omite: el encabezado "Solo para el profesor", el bloque `CRITERIOS_CORRECCION_MD` (instrucciones para el agente que corrige) y el bloque `🔍 Rúbrica flexible` de cada ítem/ejercicio. Incluye solo: narrativa, tabla de ejemplos (en Sección 2), código solución y resultado esperado.

**Verificación:** se regeneraron los 3 notebooks (`Evaluación.ipynb`, `Solucionario.ipynb`, `Solucionario Estudiantes.ipynb`); diff confirmó que `Evaluación.ipynb` y `Solucionario.ipynb` no cambiaron contenido (solo IDs de celda, ruido esperado).

## 2026-07-15 — Revisión 3: rúbrica flexible por ítem para el agente revisor

**Motivo:** Diego pidió actualizar el Solucionario para que quede pensado como fuente de verdad para un agente que corrige (skill `revisar-evaluacion`), no solo para el profesor humano. El pedido explícito: que el agente sepa tomar una postura flexible ante la diversidad de "codeo" de los estudiantes — lo importante es la funcionalidad, no la forma exacta — y que cuando un estudiante no escriba exactamente lo pedido pero diga en esencia lo mismo, el error sea tan mínimo que no se le resten puntos, o a lo más 1-2.

**Cambios aplicados (en `generar_evaluacion.py`, solo Solucionario — Evaluación.ipynb sin cambios de contenido):**
1. **Rúbrica de 3 niveles por ítem/ejercicio** (campo `rubrica` en cada dict de `ITEMS_1` y `EJERCICIOS_2`, 11 en total): `acepta` (variantes sin descuento, específicas a la lógica de ese ítem — más allá de lo genérico), `parcial` (descuenta 1-2 pts por un detalle menor donde la esencia está bien pero algo quedó impreciso — tope explícito de 2 pts) y `full` (errores de lógica reales que sí cuestan la mayoría o todo el puntaje del ítem). Varios ítems de Sección 1 (1B.2, 1B.3, 1B.4) no tienen nivel `parcial` natural — se documentó explícitamente que ahí no hay término medio (o la lógica clave está bien, o hay error real).
2. **`CRITERIOS_CORRECCION_MD` reescrito** dirigiéndose directamente al agente que corrige ("Si estás revisando esta evaluación..."), explicando el sistema de 3 niveles como marco general y agregando una "regla de oro": ante la duda de si algo es un error, no lo es; solo bajar de nivel 1 cuando se pueda señalar con precisión qué caso de entrada distinto daría un resultado equivocado.
3. **Nueva función `rubrica_md()`** que renderiza el bloque de cada ítem (`🔍 Rúbrica flexible para este ítem`) justo después de la celda de solución, en vez de dejar todo el criterio solo en la sección general del inicio.

**Verificación:** se comparó cada solución del Solucionario contra `Evaluación.ipynb` antes de tocar nada — ya coincidían 1:1 (11 ítems, 100 pts, mismos contextos), así que no fue necesario corregir ninguna solución de referencia. Se regeneraron ambos notebooks y se confirmó por diff que `Evaluación.ipynb` no cambió su contenido (solo IDs de celda, que `generar_evaluacion.py` regenera al azar en cada corrida — ruido esperado, no una diferencia real).

**Puntaje:** no cambió (100 pts, misma distribución).

## 2026-07-15 — Revisión 2: niveles enumerados, dólares, sin jerga técnica

**Motivo:** tras revisar la Revisión 1, Diego pidió 4 ajustes más a Sección 2, y pidió revisar el resto de los ejercicios por si tenían el mismo problema. Se aplicó en dos pasos aprobados por separado: primero el Colab de estudiante, después el Solucionario.

**Revisión propia detectada (no pedida explícitamente, pero con el mismo defecto que el Ejercicio 3):** el Ejercicio 2 (Micro a Talagante) tenía 3 caminos posibles pero la tabla de ejemplos solo mostraba 2 mensajes — el tercero ("Paga el pasaje con la tarjeta bip.") nunca aparecía en el enunciado, solo en la pauta del profesor. Se corrigió junto con el resto.

**Cambios aplicados (en `generar_evaluacion.py`, regenerados ambos `.ipynb`):**
1. **Ejercicio 2 — Micro a Talagante:** saldo de la tarjeta bip pasa de `float()` a `int()` (los pesos chilenos no tienen decimales — la app real de bip tampoco los muestra). Se agregó un punteo con los 3 mensajes exactos posibles.
2. **Ejercicio 3 — ahora "Ahorro semanal en dólares":** cambio de contexto de pesos a dólares (así los decimales tienen sentido real — muchas personas en Chile ahorran en USD para protegerse de la fluctuación del peso). Se agregó un punteo con los 4 niveles y sus umbrales exactos (antes solo decía "cuatro niveles, del más bajo al más alto" sin definirlos).
3. **Ejercicio 4 — ahora "Sala de juego según tu rango":** se sacó "matchmaking" del título y del enunciado (anglicismo que puede no ser conocido). Se sacó la frase que decía explícitamente "asigna la sala usando `elif`... anida la pregunta de la racha dentro de la rama oro" — revelaba la técnica de antemano. Se agregó en su lugar un punteo con los 4 casos posibles y su mensaje exacto, más la aclaración de que la pregunta de la racha solo se hace si el rango es "oro" (información de comportamiento, no de implementación). Único requisito explícito de forma: usar `input()` para pedir los datos.
4. **Ejercicio 1:** revisado, sin cambios — ya tenía sus 2 únicos desenlaces posibles completamente documentados en la tabla de ejemplos.

**Puntaje:** no cambió (100 pts, misma distribución).

**Verificación:** se probaron los 7 ítems de Sección 1 y **las 13 combinaciones de entrada** de los 4 ejercicios de Sección 2 (incluyendo los caminos que no aparecen en la tabla de ejemplos, como "paga con bip" en el Ej. 2 y "oro sin racha" en el Ej. 4) contra el Solucionario — todos coinciden con el mensaje documentado en el punteo del enunciado.

## 2026-07-15 — Revisión 1: subsecciones, contextos, sin dificultad, rúbrica flexible

**Motivo:** Diego pidió 5 ajustes tras revisar la primera versión.

**Cambios aplicados (en `generar_evaluacion.py`, regenerados ambos `.ipynb`):**
1. **Sección 1 reordenada en subsecciones explícitas** — `### 1A — Arma la condición` (2 ítems) y `### 1B — Arregla el bug` (5 ítems), en vez de ir mezclados por bloque. Mismo patrón que ya usa la Ejercitación de Clase 17.
2. **Quitado "Bloque N — Tema" y el patrón técnico (ej. `` `and` simple ``) de cada ítem en el notebook de estudiante** — un ítem ahora es solo `**Ítem 1A.1** (4 pts)` + narrativa, para no regalar de antemano qué construcción se está evaluando. Esos metadatos se mantienen en el Solucionario (uso interno del profesor).
3. **4 de los 7 ítems de Sección 1 cambiaron de contexto** por ser demasiado parecidos a los de la Ejercitación de Clase 17 (mismo patrón de "código/clave de acceso", mismo evento "feria de Isla de Maipo", ambos "elegibilidad de cuenta gamer", o ambos literalmente "robot"):
   - 1B.1 (antes "código Discord") → máquina expendedora, monto exacto sin vuelto.
   - 1A.1 (antes "Feria de la Vendimia") → concurso de fotografía en Instagram (cuenta pública + hashtag).
   - 1A.2 (antes "clasificatoria de videojuego") → backstage de un festival de música (pulsera VIP + prensa/staff).
   - 1B.4 (antes "robot aspirador") → parlante inteligente (conectado a internet + reconoció comando).
   - Los otros 3 (básquetbol, TikTok, racha de estudio) y los 4 ejercicios de Sección 2 se mantuvieron: su dominio ya difiere lo suficiente del de Clase 17 (la similitud estructural que queda es inevitable, la exige la técnica evaluada, no el contexto).
4. **Quitadas las estrellitas y etiquetas de dificultad de Sección 2** (`⭐ Fácil`, `⭐⭐ Media`, `⭐⭐⭐ Difícil`, `(desafío)`) — los títulos ahora son solo `Ejercicio N — Título (pts)`.
5. **Cierre:** "...antes de compartir el Colab con el profesor." → "...antes de compartir el Colab."

**Rúbrica de corrección flexible:** se agregó una sección `## 🎯 Criterios de corrección` al inicio del Solucionario (después del título) indicando que la corrección debe enfocarse en la lógica de las condiciones — acepta mensajes de `print()`, nombres de variable o estructuras equivalentes distintas al ejemplo, y resta puntos solo por errores de lógica reales (operador incorrecto, caso límite mal manejado, rama faltante, tipo de dato mal leído, código que no ejecuta). Sirve como punto de partida para cuando la skill `revisar-evaluacion` calibre la pauta con Diego — no la reemplaza.

**Puntaje:** no cambió (100 pts, misma distribución por ítem/ejercicio, solo renumerados 1.1–1.7 → 1A.1/1A.2 + 1B.1–1B.5).

**Verificación:** las 7 soluciones de Sección 1 y las 4 de Sección 2 del Solucionario se ejecutaron (con `input()` simulado en Sección 2) y los resultados coinciden con el valor esperado documentado en cada celda.

## 2026-07-15 — Creación

**Motivo:** construir la evaluación individual sumativa de Condicionales (2026-07-21), pensada para 75 minutos efectivos, a partir del temario (`Clase 17.5 - Evaluación Condicionales - Temario.md`), el Solucionario de la Ejercitación de Clase 17 y el repaso de apoyo individual — sin introducir formatos de pregunta nuevos ni contenidos no trabajados.

**Renumeración curricular:** esta evaluación pasa de N° 17.5 a **N° 19** en `Historial-Curricular.md`, dejando N° 18 reservado para un Reforzamiento (repaso de Clase 17 + nueva guía rápida, pendiente de otra sesión). Todo lo que venía después (for avanzado, while, evaluación de ciclos, funciones, strings, listas, proyectos) se corrió +1 en la numeración.

**Decisiones de formato (respecto al repaso de Clase 17.5):**
- Se mantiene el descarte de "predicción de output sin ejecutar" — es una evaluación en computador, ese formato de papel no aplica (mismo criterio que [[feedback-formato-repaso-computador]]).
- A diferencia del repaso, **esta evaluación sí usa `input()`** en la Sección 2, por pedido explícito de Diego — siempre siendo explícito en el enunciado sobre el tipo de dato esperado (entero, con decimales, o texto exacto), en lenguaje natural, sin nombrar `int()`/`float()` en la narrativa.
- La Sección 1 (ítems cortos) se mantiene **sin `input()`** — variables ya definidas, para ir rápido.
- **Sin autocheck** (a diferencia de la Ejercitación de Clase 17): es una evaluación sumativa, no práctica — la corrección es posterior con la pauta del Solucionario.
- Sin Práctica Guiada dentro del documento — va directo de instrucciones a los ejercicios.
- Todos los contextos son nuevos, sin repetir ninguno usado en Clase 17, Clase 14, Clase 11/13 ni en el apoyo individual.

**Estructura final (100 pts, 75 min):**
- **Sección 1 — Ítems cortos** (30 pts, 7 ítems, ~21 min): 2 "Arma la condición" (Bloque 2) + 5 "Arregla el bug" (uno por Bloque 1, 3, 4, 5, 6).
- **Sección 2 — Programas completos** (70 pts, 4 ejercicios, ~54 min, con `input()`): Modo Fiesta de una playlist (⭐ Fácil, if/else, 12 pts), Micro a Talagante (⭐⭐ Media, if anidados, 16 pts), Ahorro semanal (⭐⭐ Media-alta, elif 4 categorías, 18 pts), Salas de matchmaking (⭐⭐⭐ Difícil, Bloque 7: elif + anidado, 24 pts).

**Escala de nota:** 100 pts, exigencia 50% (nota 4.0 al 50% de logro), pauta completa en el Solucionario.

**Generación:** ambos notebooks (`Clase 19 - Evaluación Condicionales - Evaluación.ipynb` y `- Solucionario.ipynb`) se generan con `generar_evaluacion.py` — fuente de verdad, no editar los `.ipynb` a mano, regenerar el script si hay que cambiar algo.

**Siguiente paso:** cuando Diego pida iterar (agregar ítems, cambiar contextos, ajustar puntaje), editar `generar_evaluacion.py` y regenerar. La revisión de las entregas después de rendida la evaluación se hace con la skill `revisar-evaluacion`.
