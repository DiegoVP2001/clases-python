# Historial — Clase 27 - Evaluación Ciclos

## 2026-08-19 — Diseño completo: Spec, renumeración, correcciones de contenido y Solucionario Docente

**Punto de partida:** Diego pidió armar las 3 carpetas de la semana del 24-ago (lunes estándar de Funciones, simulacro de Ciclos, evaluación de Ciclos) y partir diseñando la evaluación del jueves. Las 3 carpetas ya existían vacías en disco (creadas por Diego el 18-ago): `clase-25-lunes-control-funciones`, `clase-26-simulacro-ciclos`, `clase-22b-evaluacion-ciclos`.

**Renumeración (dos rondas el mismo día):**
1. Se formalizó en `Historial-Curricular.md` la numeración ya implícita en los nombres de carpeta: N°25 (Lunes estándar Control Funciones), N°26 (Simulacro Ciclos), manteniendo N°22.5 (decimal) para la evaluación — cascada +2 sobre Strings/Listas/Proyectos.
2. Diego pidió después que la evaluación dejara de ser decimal y tomara el siguiente entero libre (**N°27**), igual que cualquier otra sesión — cascada +1 más. Carpeta renombrada `clase-22b-evaluacion-ciclos` → `clase-27-evaluacion-ciclos`. Detalle completo de ambas rondas en `Historial-Curricular.md` y en el Plan de Cierre.

**Spec v1 (primer intento, con un error de alcance):** propuse 10 ítems (2 armar + 4 bug en Sección 1, 4 ejercicios en Sección 2) con actitud Rigurosidad (Familia 2 del banco de cierre) y contextos variados sin repetir los de las 6 clases foco de Ciclos. Generé también una preview con respuestas para que Diego revisara cómo se vería en Colab.

**Corrección crítica (v2) — contenido no visto:** Diego detectó que 1A.2, 1B.3, 1B.4 iteraban directo sobre una lista literal (`for x in lista:`) y que 2.2 usaba `.strip()` — **ninguno de los dos se ha enseñado**: el `for` de este curso siempre se enseñó sobre `range()` (Listas es N°30, muy posterior) y ningún método de string se ha visto (eso es N°29). Rediseñé esos 4 puntos para usar solo `for`+`range()`, `if`, `while`, `continue`, `break` — mismos patrones de bug, contextos nuevos (atletismo, karaoke por rango, ajedrez por rango). De paso Diego pidió 2 ítems de bug adicionales (grilla de sensores del taller de robótica, estacionamiento) y hubo que rebalancear puntaje: Sección 1 subió a 8 ítems (40 pts), Sección 2 bajó a 15 pts por ejercicio (60 pts).

**Ajuste de balance (v3):** Diego pidió una segunda pasada de calibración:
- Sección 1: 4 armar + 4 bug (en vez de 2+6) — los 2 bugs nuevos de robótica/estacionamiento pasaron a ser ítems "arma" en vez de "arregla el bug", mismo contexto y dificultad.
- Puntaje: Sección 1 (rápidas) baja a 32 pts (4 pts × 8 ítems); Sección 2 (desarrollo) sube a 68 pts, con puntaje distinto por dificultad real (15/17/18/18) en vez de parejo.
- 2.1 (ventas del almacén): reformulado el enunciado para explicitar "por cada vuelta del `for`, pedir la venta correspondiente con `input()`" + pista sobre reutilizar la misma variable en vez de crear una por iteración.
- 2.2 (baile del Aniversario): estaba desbalanceado frente a 2.1 (código de solución mucho más corto/trivial) — se extendió agregando un acumulador de `total_integrantes` sobre el ciclo anidado.
- 2.3 (estación meteorológica): 2 pistas agregadas (cómo se calcula un promedio; no olvidar contar cuántos registros hubo).
- 2.4 (caja fuerte): 2 pistas agregadas (qué es un contador; qué es un flag/bandera).
- Todas las pistas son solo texto, sin código, como pidió Diego explícitamente.

**Solucionario Docente generado:** con bloque de criterios de corrección para el agente que revise (mismo espíritu que `clase-19`, adaptado a ciclos: condición de corte, `break`/`continue` mal ubicados, regla de portazo en "arregla el bug"), tabla de puntaje con la fórmula de nota (escala 1.0–7.0, exigencia 50%), y rúbrica flexible de 3 niveles (✅/⚠️/❌) por cada uno de los 12 ítems/ejercicios. Verificado ejecutando las 12 soluciones con inputs simulados — todas corren sin error y calzan con la salida esperada documentada en el Spec.

**Solucionario Estudiantes generado (mismo día, a pedido explícito de Diego):** `Clase 27 - Evaluación Ciclos - Solucionario Estudiantes.ipynb` — mismas narrativas y soluciones que el Docente, pero sin ningún lenguaje de puntaje/descuento; cada ítem cierra con `🔎 **Qué se revisó:**` usando el campo `criterio` ya definido para cada ítem/ejercicio. Verificado: 12/12 soluciones ejecutan sin error y no quedó ninguna frase de rúbrica/descuento filtrada (escaneo automático de las frases prohibidas). `generar_evaluacion.py` ahora genera los 4 notebooks por defecto (`Evaluación`, `Preview con Respuestas`, `Solucionario`, `Solucionario Estudiantes`).

**Archivo de trabajo interno (no es un artefacto canónico):** `Clase 27 - Evaluación Ciclos - Preview con Respuestas.ipynb` — copia del notebook de estudiante con la respuesta agregada debajo de cada celda de código, generada a pedido puntual de Diego para revisar rápido en Colab antes de que existiera el Solucionario formal. Queda en la carpeta como referencia pero es redundante con el Solucionario ahora que existe; se puede borrar sin pérdida de información si Diego lo prefiere.

**Estado de publicación:** nada de esta carpeta se ha pusheado a GitHub. El repo es público y esta evaluación se rinde el 27-ago — igual criterio que ya rige para Ticket de Salida/Control: **el Colab de la Evaluación no se sube hasta después de rendida**, y el Solucionario (Docente o Estudiantes) tampoco. Commit local hecho, sin push (ver detalle al pie de este documento o en el mensaje de cierre de la sesión).

---

## Lecciones aprendidas (para futuras evaluaciones/controles/ayudantías de este curso)

1. **"Estar en el temario" no basta — hay que verificar CÓMO se enseñó, no solo QUÉ.** El `for` ya estaba en el temario de esta evaluación, pero eso no autorizaba iterar sobre listas: en este curso el `for` se enseñó exclusivamente sobre `range()` (Listas es contenido muy posterior, N°30). Del mismo modo, que "for" aparezca no habilita usar cualquier método asociado a otro tipo de dato (ej. `.strip()` de N°29). **Antes de escribir un ítem que combine dos construcciones, hay que confirmar contra `Historial-Curricular.md` qué se enseñó realmente de cada una**, no asumir por el nombre del concepto. Esto es una instancia más específica de la Restricción #1 del `CLAUDE.md` ("no adelantes contenidos no vistos"), y vale la pena tenerla presente activamente cada vez que un ítem cruza dos temas (ej. ciclos + tipos de datos, condicionales + funciones).
2. **El puntaje de una evaluación debe reflejar la dificultad real de cada ítem, no repartirse parejo por sección.** Cuando dos ejercicios de la misma sección tienen código de solución de largo/complejidad muy distinta, conviene puntuarlos distinto (o extender el más corto) en vez de dejarlos con el mismo puntaje solo porque están en la misma sección — se detectó porque el ejercicio 2.2 se sentía "como si no tuviera nada" comparado con 2.1 pese a valer lo mismo.
3. **Las pistas de una evaluación (cuando se piden) van 100% en palabras, nunca con código** — ni siquiera un fragmento ilustrativo. Aplica el mismo criterio que ya rige para las pistas de la Práctica Independiente en clases regulares.
4. **Las evaluaciones sumativas dejaron de numerarse con decimal.** Antes (N°19.5, N°22.5) el decimal marcaba que la evaluación cerraba un bloque sin importar el orden real de dictado. Desde esta sesión (2026-08-19), Diego decidió que toman el siguiente entero libre como cualquier sesión — de mantenerse el criterio, aplicaría también a la próxima evaluación (N°32.5, Funciones+Strings+Listas) salvo que Diego indique lo contrario llegado el momento.
