# Prompt de sesión — Clase N°28: Strings — indexing y slicing

**Fecha programada:** lunes 2026-08-31
**Clase Picuino de referencia:** N°21 — Cadenas de texto + N°22 — Índices de cadenas de texto (combinadas, foco recortado a acceso/rebanadas — ver más abajo)
**Estado:** contenidos acordados en chat (2026-08-26), spec aún sin generar.

## Contexto acordado (planificación 2026-08-20, ajustada 2026-08-26)

- Primera clase de contenido nuevo después de la Evaluación de Ciclos (N°27, rendida 27-ago). Ocupa el lunes 31-ago, que antes tenía reservada la revisión formativa de esa evaluación — **esa revisión se corre a otro día, aún por definir** (Diego lo resolverá cuando termine de revisar el calendario completo).
- Contenidos previos asumidos: todo hasta N°27 inclusive (Ciclos completo: for, range, for anidado, continue/break, while + Funciones N°24a/24b).
- Arranca el bloque temático "Datos textuales" (Strings), primer bloque después de Iteración y Abstracción. Es la primera de 3 clases de Strings dictadas en la misma semana (lunes/martes/jueves): N°28 (esta) → N°29 (nueva, recorriendo texto con `for`, martes 1-sep) → N°30 (métodos y f-strings, jueves 3-sep) → N°31 (lunes estándar, control sobre las 3, 7-sep).

## Foco de contenido — recortado en sesión de diseño 2026-08-26

A diferencia del foco original de la ficha Picuino N°21+N°22 completa, esta clase se acotó **solo a acceso por índice y rebanadas** — sin creación básica de cadenas (comillas/escapes/Unicode), sin unión (`+`) ni repetición (`*`), y sin recorrido con `for` (eso se mueve a la Clase N°29 nueva).

- **Acceso por índice:** índices desde 0, índices negativos desde el final, `len()` para conocer la cantidad de caracteres y el rango válido, qué pasa si el índice está fuera de rango (error).
- **Rebanadas (slicing):** `[inicio:fin]`, omitir límites (`[:n]`, `[n:]`), qué pasa si la rebanada se pasa de rango (cadena vacía, sin error — contraste explícito con el error del índice único).
- Insistir en índice cero y en la diferencia entre índice único (`texto[0]`) y rebanada (`texto[0:3]`).

**Contenido descartado explícitamente de esta clase (razón registrada en el chat de diseño):**
- Comillas/escapes/Unicode/multilínea (N°21): no aporta al foco índice/rebanada, se puede tocar de pasada sin slide propio.
- Unión (`+`) y repetición (`*`): se traslada como posible contenido de la Clase N°30 (métodos/f-strings) — riesgo de reforzar el patrón `print("texto" + variable)` que la regla 14 del CLAUDE.md prohíbe.
- Recorrido con `for` (directo o con índice) y las actividades Picuino "deletrea sin/con índices", "impresión progresiva", "ventana móvil": se mueven íntegras a la Clase N°29 nueva (ver su propio Prompt.md).

## Especificación acordada en chat (Paso 3 de `disenar-clase`, 2026-08-26)

Objetivo, propósito y actitud ya están aprobados por Diego — falta solo Paso 4 (estructura completa de 5 pasos) y Paso 5 (guardar `Clase 28 - Strings - Spec.md`). **El objetivo de abajo está reescrito respecto al aprobado originalmente en el chat**, porque el recorte de alcance (fuera creación/unión/repetición, ver más arriba) pasó *después* de aprobar objetivo y propósito — se sacó la mención a "creación, unión, repetición" para que quede fiel al contenido final. El propósito no cambió, ya estaba centrado en índice/rebanada.

- **Actitud elegida:** Precisión — el contenido gira en índice cero, índices negativos y límites de slicing donde un número mal contado cambia todo el resultado.
- **Objetivo (ajustado al alcance final):** Extraer caracteres y segmentos específicos de una cadena de texto mediante índices y rebanadas, con precisión.
- **Propósito:** "La precisión es acertar en el número exacto, sin margen de error, cuando cada posición cuenta. Hoy la practicamos ubicando caracteres exactos dentro de un texto, usando índices y rebanadas."

## OAs sugeridos

OA2, OA3 (según fila ya registrada en `Historial-Curricular.md`).

## Prompt para iniciar la sesión

> Vamos con la clase de Strings — indexing y slicing (recorte del Picuino N°21+N°22, solo acceso por índice y rebanadas), para el lunes 2026-08-31. Es N°28 en `Historial-Curricular.md`, carpeta `clase-28-strings`. Contenidos previos: todo hasta N°27 (Ciclos completo + Funciones). Actitud, objetivo y propósito ya acordados — ver sección "Especificación acordada en chat" arriba; retoma directo desde el Paso 4 de `disenar-clase` (estructura completa de 5 pasos), sin volver a proponer objetivo/actitud salvo que Diego pida ajustarlos. Actívate con `disenar-clase`.
