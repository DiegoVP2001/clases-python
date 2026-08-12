# Clase 23 — Lunes While y Break · Historial

**Fecha de aplicación:** lunes 2026-08-17
**Formato:** lunes estándar (ejercitación en parejas sorteadas + control individual con nota + revisión)
**Clases foco:** N°21.5 (continue y break) y N°22 (while)

---

## 2026-08-12 — Diseño y generación del primer lunes estándar

Primera aplicación del formato definido en el `CLAUDE.md` del proyecto ("Workflow: lunes estándar") y en la §4 del `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md`. Reemplaza al formato de ayudantía suelta que se usó hasta N°21.

### Decisiones tomadas con Diego en esta sesión

- **Numeración:** la sesión queda como **N°23 entero** (no decimal), porque los lunes dejan de ser ayudantías y pasan a ser sesiones con control con nota. Todo lo posterior corrió +1 (ver la nota de renumeración en `Historial-Curricular.md`).
- **Sin Ticket de Salida.** El control reemplaza al TdS como instrumento de medición del día.
- **El control lleva nota.** Promedio de todos los controles del semestre; quien rinda todos podrá eliminar los X peores (X aún por definir). Registro futuro en `Controles - Trazabilidad.xlsx`.
- **Corrección por agente**, con el método ya calibrado en la Evaluación 2 (Clase 19). Los errores de corrección los reclaman los estudiantes; no hay auditoría entrega por entrega.
- **Rúbrica parcelada por componentes** al nivel de detalle de `rubrica_parcelada_seccion2_evaluacion2.md`: 100 pts repartidos en 4-6 componentes independientes por ítem.
- **Ítem 3 = mezcla simple:** `while` + **uno solo** de `continue`/`break`, no los tres juntos. Quedó `while` + `continue`.
- **Contexto disfrazado:** ningún ítem dice "programa un `while` que…". Una o dos líneas de contexto obligan a decidir qué estructura corresponde. Por lo mismo, el título interno del `Control.ipynb` es neutro ("Control de Ciclos"), sin nombrar las tres estructuras.
- **Soluciones colapsadas al final de la Ejercitación**, dentro de `<details>` — excepción explícita a la Restricción 5 del `CLAUDE.md`, agregada ese mismo día y acotada solo a este archivo.
- **Práctica guiada:** a pedido de Diego, se diseñó como espejo del Ítem 3 y con dos recordatorios explícitos que el guiado hace visibles de una pasada: (1) `continue` y `break` también funcionan dentro de un `while`, no solo en `for`; (2) un `input()` puede pedirse dentro de un ciclo, dentro de un `if`, o dentro de un `if` que está dentro de un ciclo.
- **Sin verificador automático** en la Ejercitación (a diferencia de N°21.5 y N°22): las soluciones colapsadas cumplen ese rol y dejan más espacio en los 45 minutos.

### Artefactos generados

| Archivo | Destino |
|---|---|
| `Clase 23 - Lunes While y Break - Propuesta.json` | Fuente de verdad (ejercitación + control + rúbrica) |
| `generar_lunes.py` | Generador y verificador. **Nunca editar los `.ipynb` a mano** |
| `Clase 23 - Lunes While y Break - Ejercitación.ipynb` | Estudiantes (Colab) — guiado + 4 ejercicios + `## 🔓 Soluciones` |
| `Clase 23 - Lunes While y Break - Control.ipynb` | Estudiantes (Classroom) — 3 ítems, sin soluciones |
| `Clase 23 - Lunes While y Break - Control Solucionario.ipynb` | Profesor + agente corrector |

### Mapeo ejercitación ↔ control

| Ejercitación | Control | Habilidad |
|---|---|---|
| Guiado — Kiosco de sopaipillas | (espejo del Ítem 3) | `while` + `continue` + `break`, con `input()` dentro de un `if` |
| Ej. 1 — Impresora de la sala de profesores | Ítem 1 — Batería del robot repartidor | `while` con variable de control que se actualiza |
| Ej. 2 — El día que se pasaron | Ítem 2 — El primer video que despegó | `for` + `break` |
| Ej. 3 — Encuesta del curso | Ítem 3 — Máquina de reciclaje | `while` + `continue` |
| Ej. 4 — Turno en la biblioteca | *(sin hermano — sube el escalón)* | `while` + `continue` + `break` |

Ningún ítem del control es el mismo ejercicio con otros números: misma habilidad, contexto y estructura distintos. Contextos verificados contra los ya usados en N°21.5 (playlist, series de entrenamiento, notificaciones) y N°22 (aforo del gimnasio, cupos del taller, préstamo de notebooks) — ninguno se repite.

### Verificación

`python generar_lunes.py --check` corre cada solución de referencia contra sus casos de prueba (con `input()` simulado) y valida que los componentes de la rúbrica sumen el puntaje declarado de cada ítem y del control completo.

Resultado al generar: **19/19 casos OK**, puntajes cuadrados (25 + 30 + 45 = 100).

### Pendientes

- Definir **X** (cuántos controles se pueden eliminar al cierre del semestre) y qué pasa con quien falta a uno: ¿promedia en 0, o solo pierde el derecho a eliminar? No bloquea el lunes; se necesita al construir `Controles - Trazabilidad.xlsx`.
- Formalizar la skill del lunes estándar (`generar_lunes.py` vive por ahora en esta carpeta, igual que `generar_evaluacion.py` en la Clase 19). Se escribe después de aplicar este primer lunes, cuando el formato haya sobrevivido al uso real.
- Al abrir el Colab, confirmar que los bloques de código dentro de `<details>` se vean con formato (patrón estándar de fence markdown con línea en blanco después de `</summary>`).

### Publicación

- `Ejercitación.ipynb` puede subirse el mismo lunes en la mañana.
- **`Control.ipynb` y `Control Solucionario.ipynb` no se pushean hasta después de aplicado el control** — el repo es público, mismo criterio que rige para los `Ticket de Salida.pptx`.
