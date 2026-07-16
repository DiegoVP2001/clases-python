# Historial — Clase 19 - Evaluación Condicionales

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
