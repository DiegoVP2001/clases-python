# Prompt de sesión — Clase N°34: Control Strings — Métodos y Búsqueda

**Fecha programada:** martes 2026-09-15 (control) · lunes 2026-09-14 se dicta recién la Clase 33
**Clase Picuino de referencia:** N/A — consolidación (clases foco: N°32 y N°33)
**Estado:** planificación de infraestructura hecha (2026-09-11, en modo plan, sin ejecutar). Diseño de contenido del Control **no iniciado** — falta la sesión de propuesta en chat.

## Por qué existe esta clase (contexto de la sesión 2026-09-11 que la creó)

Diego perdió clases: la **Clase 33 (Strings — búsqueda, `in`/`find()`)** no alcanzó a dictarse en su fecha original (martes 08-sep) y se dicta recién el **lunes 2026-09-14**. El **martes 2026-09-15** Diego quiere aplicar un **Control** que cubra las dos clases de Strings que quedaron sin control propio:

- **Clase 32 — Strings: métodos** (`clase-32-strings-metodos`): operadores `+`/`*`, `upper()`/`lower()`/`title()`, `strip()`/`replace()`, `split()` con asignación múltiple.
- **Clase 33 — Strings: búsqueda** (`clase-33-strings-busqueda`): `in`, normalizar con `.lower()` antes de comparar, `find()`.

El Control N°31 (`clase-31-lunes-control-strings`, lunes 07-sep) **no cubre ninguna de las dos** — su foco quedó acotado solo a N°28 (indexing/slicing) y N°29 (recorrido con `for`).

Como el martes 15-sep no es un "lunes estándar" (no hay sesión de ejercitación en parejas el día anterior — el lunes 14-sep se usa para dictar la Clase 33), este Control es un artefacto nuevo, con número real propio: toma el **N°34**. La clase de Listas que antes ocupaba ese número se renumeró a **N°35** y su fecha se movió a la vuelta de vacaciones, **lunes 2026-09-28** (carpeta ya renombrada a `clase-35-listas`, reemplaza ahí al "Kahoot de reactivación" que el Plan de Cierre tenía asignado ese día — ver `Historial-Curricular.md` y `Plan Cierre...md` para el detalle completo de la renumeración 2026-09-11).

## Decisiones ya tomadas con Diego (2026-09-11, vía `AskUserQuestion`)

- **Sí lleva una Ejercitación corta** de acompañamiento, aunque no haya sesión en parejas dedicada — no es el patrón exacto de "lunes estándar", pero reutiliza la misma mecánica de notebook de práctica antes del control (guiado + ejercicios hermanos de los ítems del Control).
- El Control **no lleva Ejercicios "0"** (regla permanente: nunca en un instrumento con nota).
- El lunes 28-sep pasa a ser directamente Clase 35 — Listas, reemplazando el Kahoot de reactivación que tenía asignado el `Plan Cierre...md` ese día.

## Qué falta para poder generar (retomar desde acá)

Esta clase **no pasó por la sesión de diseño todavía**. Al retomar, seguir el "Workflow: lunes estándar" del `CLAUDE.md` del proyecto (aplica aunque el control caiga un martes: se diseña primero el Control, después la Ejercitación espejo):

1. **Preguntar a Diego en el chat** (gates formales, no se saltan):
   - Qué actitud ancla el cierre del Control — Clase 32 usó "Orden", Clase 33 usó "Rigor"; puede repetir una, mezclar, o elegir otra.
   - Qué pregunta del banco de "Cierre de actitud en Control y Evaluación" usar (rotar familia, evitar repetir la Familia 3 recién usada en el Control N°31).
   - Confirmar el reparto de ítems entre los dos focos — propuesta base a validar: 3 ítems, 100 pts, ~2 ítems anclados en Clase 32 (tiene más conceptos: operadores, `upper/lower/title`, `strip/replace`, `split`) y ~1-2 en Clase 33 (`in`/`find()`), sin `input()` (valores fijos, mismo criterio que Control N°31).
   - Contexto/escenario: ¿continúa Los Mellis Al Paso (mismo negocio ancla de ambas clases foco) o diversifica?
2. **Guardar la propuesta aprobada** en `Clase 34 - Control Strings Métodos y Búsqueda - Propuesta.json` (misma forma que `clase-31-lunes-control-strings/Clase 31 - Lunes Control Strings - Propuesta.json`: bloques `actitud`, `ejercitacion` con `guided_exercise` + `exercises`, `control` con `items` + `componentes` parcelados + `cierre_actitud`).
3. **Generar con un script propio** `generar_control.py` en esta carpeta, adaptado de `clase-31-lunes-control-strings/generar_lunes.py` (helpers `md_cell`/`code_cell`/`notebook`, `bloque_pistas`, `bloque_ejemplo`, verificador de autochequeo para la Ejercitación, `build_control`, `build_control_solucionario_docente`, `build_control_solucionario_estudiantes`). La Ejercitación **no debe mencionar modalidad de trabajo** (regla ya vigente para cualquier Ejercitación/Independiente) — esta sesión no tiene parejas sorteadas.
4. **Verificar cada solución** ejecutándola contra su caso de prueba antes de escribir los notebooks (mismo estándar que `clase-31`). Cuadrar puntajes: suma de componentes = puntaje del ítem, suma de ítems = 100 pts.
5. **Publicación:** la Ejercitación puede subirse (commit+push acotado a esta carpeta) apenas esté aprobada. `Control.ipynb` y ambos Solucionarios **no se pushean hasta después de aplicado el control** (martes 15-sep, una vez corregido) — mismo criterio que todos los controles anteriores.

## Artefactos que produce esta carpeta

```
clase-34-control-strings-metodos-busqueda/
├── Prompt.md                                                          (este archivo)
├── Clase 34 - Control Strings Métodos y Búsqueda - Propuesta.json
├── Clase 34 - Control Strings Métodos y Búsqueda - Ejercitación.ipynb
├── Clase 34 - Control Strings Métodos y Búsqueda - Control.ipynb
├── Clase 34 - Control Strings Métodos y Búsqueda - Control Solucionario Docente.ipynb
├── Clase 34 - Control Strings Métodos y Búsqueda - Control Solucionario Estudiantes.ipynb
├── Clase 34 - Control Strings Métodos y Búsqueda - Historial.md
└── generar_control.py
```

## Pendiente de bookkeeping (todavía no ejecutado — hacerlo junto con o antes del diseño)

- Renombrar carpeta `clase-34-listas` → `clase-35-listas` y actualizar su `Prompt.md` (N°35, fecha 2026-09-28, nota de renumeración).
- `Historial-Curricular.md`: insertar fila N°34 (esta clase), renombrar la fila de Listas a N°35, correr en cascada +1 todo lo que sigue (Listas iteración/métodos 35→36, Integración 36→37, Evaluación F+S+L 36.5→37.5, Proyecto OA4 37-38→38-39, Proyecto OA5 39-42→40-43), actualizar "Próxima clase disponible" y "Bloques temáticos del año".
- `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md`: corregir SM37 (08-sep no se dictó Clase 33, agregar filas reales 14-sep/15-sep), SM38 (14-sep/15-sep ya ocupados, 17-sep sigue sin definir), SM40 (28-sep: Clase 35 reemplaza al Kahoot de reactivación), y todas las referencias de numeración +1 en el resto del documento.

## Prompt para iniciar la sesión

> Vamos con el Control N°34 — Strings: Métodos y Búsqueda (cubre Clase 32 y Clase 33), a aplicar el martes 2026-09-15. Es clase nueva, carpeta `clase-34-control-strings-metodos-busqueda`. Sigue el "Workflow: lunes estándar" del `CLAUDE.md` aunque se aplique un martes: diseña primero el Control, después la Ejercitación espejo. Antes de proponer nada, pregúntame la actitud, la pregunta del banco para el cierre, y el reparto de ítems entre las dos clases foco. Después de aprobar el diseño, aplica también el bookkeeping pendiente (renombrar `clase-34-listas` a `clase-35-listas`, actualizar `Historial-Curricular.md` y el `Plan Cierre...md` con la renumeración completa).
