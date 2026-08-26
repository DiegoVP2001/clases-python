# Prompt de sesión — Clase N°30: Strings — métodos y f-strings

**Fecha programada:** jueves 2026-09-03
**Clase Picuino de referencia:** N°23 — Métodos de cadenas de texto + N°24 — Formateo de cadenas de texto (f-strings)
**Estado:** sin propuesta aún.

## Contexto acordado (planificación 2026-08-20, renumerada 2026-08-26)

- Tercera de 3 clases de Strings dictadas en la misma semana: N°28 (indexing/slicing, lunes 31-ago) → N°29 (nueva, recorriendo texto con `for`, martes 1-sep) → **N°30 (esta, jueves 3-sep)** → N°31 (lunes estándar, control sobre las 3, 7-sep).
- Contenidos previos asumidos: todo hasta N°29 inclusive (Strings: acceso por índice + rebanadas + recorrido con `for`).
- **Renumerada 2026-08-26:** esta clase era N°29 hasta que se insertó la Clase N°29 nueva (recorrido con `for`) entre indexing/slicing y métodos/f-strings — ver `Historial-Curricular.md` para el detalle completo de la renumeración. Carpeta renombrada de `clase-29-strings-avanzado` a `clase-30-strings-avanzado`.

## Foco de contenido (de la ficha Picuino N°23 y N°24)

- Métodos de cadena: `upper()`, `lower()`, `swapcase()`, `title()`, `find()`, `strip()`, `replace()`, `split()`.
- `in` para verificar si un texto está dentro de otro (sensible a mayúsculas/minúsculas — normalizar con `lower()`).
- f-strings: `f'...{variable}...'`, formato numérico básico (`:03d`, `:.2f`, alineación `:>20`).
- Sugerencia de diseño, a validar en el gate de objetivo: priorizar formatos con aplicación real (notas, montos, porcentajes) antes que casos más exóticos de la ficha Picuino (binario, hexadecimal, exploración Unicode) — mismo criterio de recorte de alcance que ya usaron otras clases del bloque.
- **Posible, a confirmar en el diseño:** unión de cadenas con `+` y repetición con `*` — contenido de N°21 que se sacó de la Clase 28 (ver su Prompt.md) porque enseñarlo ahí corría el riesgo de reforzar el patrón `print("texto" + variable)`, prohibido por la regla 14 del CLAUDE.md. Aquí, junto a f-strings como alternativa "buena" de formateo, el contraste puede ser justamente el punto pedagógico — evaluar si aporta o si sigue sin caber, y decidirlo explícitamente en el gate de objetivo.

## OAs sugeridos

OA2, OA3.

## Qué falta para la especificación completa

Esta clase no pasó por sesión de diseño todavía — el foco de arriba es el de la ficha Picuino original, sin recorte propio ni actitud/objetivo/propósito elegidos. Al retomar, `disenar-clase` parte desde su Paso 1 completo (igual que cualquier clase nueva), incluyendo decidir si entra o no la unión/repetición trasladada desde Clase 28 (ver nota arriba).

## Prompt para iniciar la sesión

> Vamos con la clase de Strings — métodos y f-strings (Picuino N°23+N°24), para el jueves 2026-09-03. Es N°30 en `Historial-Curricular.md`, carpeta `clase-30-strings-avanzado`. Contenidos previos: todo hasta N°29 (Strings indexing/slicing + recorrido con for). Evalúa si incluir unión (`+`)/repetición (`*`) como contraste con f-strings — ver nota arriba. Actívate con `disenar-clase`.
