# Prompt de sesión — Clase N°30: Strings — métodos para modificar y separar texto

**Fecha programada:** jueves 2026-09-03
**Clase Picuino de referencia:** N°23 — Métodos de cadenas de texto (**parcial** — ver recorte abajo)
**Estado:** diseño en curso — actitud, contexto y recorte de contenido acordados en sesión 2026-08-26 (ver abajo). Falta aprobar formalmente objetivo/propósito (el borrador que se alcanzó a proponer mencionaba f-strings, que ya no aplica — hay que reformularlo) y la estructura de 5 pasos completa.

## Progreso acordado en sesión 2026-08-26 (sesión cortada por tokens — retomar desde acá)

- **Esta clase nació de dividir la antigua "Clase 30 — Strings: métodos y f-strings" en piezas más chicas.** Diego determinó que modificar/separar texto, buscar texto y dar formato con f-strings son 3 habilidades distintas que no caben bien en una sola sesión de 80 min. Ver `Historial-Curricular.md`, nota "Renumeración 2026-08-26 (segunda pasada)", para el detalle completo de la división y la cascada de renumeración que provocó.
- **Actitud elegida: Orden.** Se ofrecieron 4 opciones (Orden, Responsabilidad, Adaptabilidad, Precisión) — Diego eligió Orden: tomar datos de texto desordenados y dejarlos siempre en el mismo formato estándar.
- **Contexto — Los Mellis (confirmado, escenario único de TODA la clase, incluida la Independiente):** local de comida rápida de la zona, [losmellisalpaso.cl](https://losmellisalpaso.cl/). Narrativa: su sistema de boletas está fallando y el SII exige que el formato de las boletas cumpla ciertas reglas. Diego eligió explícitamente mantener Los Mellis como escenario único de principio a fin (Haz Ahora, ICN, Guiada y los 3-4 ejercicios de Independiente), a sabiendas de que esto se aparta de la regla 3 del CLAUDE.md ("contextos variados, no concentrar todo en un solo tema") — decisión consciente, no hay que cuestionarla ni diversificar por cuenta propia.
- **Contenido confirmado para ESTA clase (recorte de la ficha Picuino N°23):**
  - Unión (`+`) y repetición (`*`) de strings — sección corta y separada, ANTES del bloque de métodos, aclarando que son *operadores* (no métodos con punto). Sin contraste forzado con f-strings (esa comparación ya no aplica, f-strings se sacó del currículo cercano — ver abajo).
  - `upper()` / `lower()` / `title()` — cambiar mayúsculas y minúsculas (normalizar para comparar, presentar bonito en la boleta).
  - `strip()` / `replace()` — limpiar espacios sobrantes y corregir texto mal escrito.
  - `split()` — cortar una línea de pedido cruda (ej. `"Papas Fritas,3400"`) en sus partes. **Importante:** usar asignación múltiple (`producto, precio_texto = linea.split(",")`) para no tener que mostrar/explicar el objeto lista completo — Listas recién se enseña en Clase 33.
- **Contenido que se SACÓ de esta clase (no reintroducir aquí):**
  - Búsqueda de texto (`in`, `find()`) → se movió a la Clase N°32 nueva (`clase-32-strings-busqueda`), porque es una habilidad distinta (consultar vs. modificar).
  - f-strings / formateo (Picuino N°24) → se sacó por completo del currículo cercano. Diego lo considera "una forma de escritura distinta" que vale la pena ver en una sesión separada más adelante, **sin fecha ni número asignado todavía, no urgente** (mismo tratamiento que quedó "valores por omisión" tras el rediseño de Clase 24b). No asumir que esta clase necesita cubrirlo de ninguna forma.
  - `swapcase()` — descartado desde la propuesta inicial (sin aplicación real en el escenario de Los Mellis, solo demo de sintaxis en Picuino).
  - `find()` (aislado) — se evaluó sacarlo por falta de aplicación real sin `in`, pero terminó yéndose junto con `in` a la Clase 32 (ahí sí tiene sentido, como par de búsqueda).
- **Objetivo borrador (a re-confirmar — NO usar tal cual, mencionaba f-strings):** "Aplicar métodos de cadenas de texto para transformar datos desordenados en un formato limpio y estándar, con orden." Ajustar en la próxima sesión antes de dar por aprobado el gate de objetivo.
- **Propósito borrador (a re-confirmar):** "El orden es tomar algo desordenado y dejarlo siempre en el mismo formato, sin importar cómo llegó. Hoy lo practicamos limpiando y dando formato estándar al texto de un pedido."
- **OAs sugeridos:** OA2, OA3 (sin cambios respecto al plan original).
- **Pendiente para retomar:** cerrar formalmente el gate de objetivo/propósito (Paso 3 de `disenar-clase`, con el objetivo ajustado sin mención a f-strings), y luego proponer y aprobar la estructura completa de 5 pasos (Paso 4).

**Prompt para retomar la sesión:**
> Retomemos el diseño de la Clase 30 (Strings — métodos para modificar y separar texto). Ya acordamos actitud (Orden), contexto (Los Mellis como escenario único de toda la clase) y el recorte de contenido (sin búsqueda in/find, que se movió a Clase 32; sin f-strings, que quedó pendiente sin clase) — ver la sección "Progreso acordado en sesión 2026-08-26" arriba. Actívate con `disenar-clase`, ajusta el objetivo/propósito (el borrador anterior mencionaba f-strings, ya no aplica) y sigue desde el Paso 3 hacia la estructura de 5 pasos.

## Contexto acordado (planificación 2026-08-20, renumerada 2026-08-26 dos veces)

- Tercera de las clases de Strings dictadas en la misma semana/quincena: N°28 (indexing/slicing, lunes 31-ago) → N°29 (recorrido con `for`, martes 1-sep) → **N°30 (esta, jueves 3-sep)** → N°31 (lunes estándar, control sobre 28/29/30, 7-sep) → N°32 (búsqueda de texto, martes 8-sep).
- Contenidos previos asumidos: todo hasta N°29 inclusive (Strings: acceso por índice + rebanadas + recorrido con `for`).
- **Primera renumeración 2026-08-26:** esta clase era N°29 hasta que se insertó la Clase N°29 nueva (recorrido con `for`) entre indexing/slicing y métodos. Carpeta renombrada de `clase-29-strings-avanzado` a `clase-30-strings-avanzado`.
- **Segunda renumeración 2026-08-26 (esta sesión):** el alcance de esta clase se recortó de "métodos y f-strings" a solo "métodos para modificar y separar texto" (ver "Progreso acordado" arriba). Carpeta renombrada de `clase-30-strings-avanzado` a `clase-30-strings-metodos`. El N° real (30) no cambió. Ver `Historial-Curricular.md` para el detalle completo de ambas renumeraciones.

## Foco de contenido (de la ficha Picuino N°23, recortado)

- Métodos de cadena incluidos: `upper()`, `lower()`, `title()`, `strip()`, `replace()`, `split()`.
- Operadores incluidos: unión (`+`) y repetición (`*`) de strings — contenido de Picuino N°21 que se sacó de la Clase 28 (ver su Prompt.md) porque enseñarlo ahí corría el riesgo de reforzar el patrón `print("texto" + variable)`, prohibido por la regla 14 del CLAUDE.md.
- Excluidos de esta clase (ver "Contenido que se sacó" arriba): `swapcase()`, `in`, `find()`, todo el formateo con f-strings.

## OAs sugeridos

OA2, OA3.

## Qué falta para la especificación completa

El gate de objetivo/propósito quedó a medio camino (propuesto pero no aprobado, y desactualizado por el recorte posterior). Al retomar, `disenar-clase` entra directo al Paso 3 con la actitud ya decidida (Orden), reformula el objetivo sin mencionar f-strings, y una vez aprobado avanza al Paso 4 (estructura de 5 pasos).
