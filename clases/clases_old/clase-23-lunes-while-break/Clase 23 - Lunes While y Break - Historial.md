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

## 2026-08-13 — Cierre de actitud agregado al Control

El `CLAUDE.md` sumó ese mismo día la regla de "Cierre de actitud en Control y Evaluación" (pregunta individual, escrita, sin nota, al final del `Control.ipynb`/`Evaluación.ipynb`). Como esta Clase 23 ya estaba generada, se actualizó para incorporarla.

- **Actitud elegida:** Perseverancia — de las dos clases foco (N°21.5 = Método, N°22 = Perseverancia), Diego eligió Perseverancia como la representativa de este control.
- **Pregunta del banco:** #1 — Evidencia directa: *"En este control, cuenta en qué ítem tuviste que aplicar la perseverancia y cómo se vio en lo que hiciste."* (adaptada de "evaluación" a "control").
- **Ubicación:** última celda de `Control.ipynb`, después de "✅ Antes de entregar".
- **Implementación:** se agregó `control.cierre_actitud` (`actitud`, `pregunta_familia`, `pregunta_md`) a la Propuesta.json, y `build_control()` en `generar_lunes.py` ahora la renderiza siempre (con `ValueError` explícito si el campo falta, para que ningún lunes futuro se genere sin preguntarle a Diego primero). No se tocó `Control Solucionario.ipynb`: la pregunta no lleva nota ni respuesta correcta que registrar.
- Se regeneraron los tres notebooks; solo cambiaron los IDs de celda de `Ejercitación.ipynb` (ruido de regeneración, sin cambios de contenido) y las 2 celdas nuevas en `Control.ipynb`.

## 2026-08-13 — Apertura con actitud + propósito, y ajustes de modalidad/orden

Segunda vuelta el mismo día: Diego pidió que la actitud también abriera la sesión (no solo la cerrara), ligada al propósito, en ambos notebooks del día.

- **Se agregó un bloque `actitud` a nivel raíz de la Propuesta** (`nombre`, `proposito_md`, `frase_control_md`), compartido entre `Ejercitación.ipynb` y `Control.ipynb`. `cierre_actitud` dejó de repetir el nombre de la actitud (ahora vive una sola vez).
- **`Ejercitación.ipynb`** abre con `## 🎯 Objetivo` + `## 💡 Propósito` (cita reflexiva, mismo estilo que `disenar-clase`) ligando la actitud a lo que se entrena hoy.
- **`Control.ipynb`** abre, justo después del título y antes de "Antes de partir", con `## 💪 Actitud del control: Perseverancia` + una frase directa en imperativo ("**En este control debemos perseverar hasta el último ítem.** Si algo no te sale a la primera, no lo dejes: sigue intentando antes de pasar al siguiente.") — registro distinto del propósito reflexivo de la Ejercitación, más orientado a la instancia evaluativa.
- **Se sacó toda mención a "parejas sorteadas" de `Ejercitación.ipynb`** (la intro y el encabezado "Ahora en parejas..." de la serie de ejercicios) — rompía la regla ya vigente de no fijar la modalidad de trabajo en material que se sube con anticipación (Diego la anuncia en vivo). El texto de "sin nota, se evalúa el Control" se mantuvo, solo sin la mención a la modalidad.
- **Se reordenó el cierre de `Control.ipynb`:** la reflexión de actitud (pregunta + "Mi respuesta") ahora va **antes** del checklist "✅ Antes de entregar", que pasa a ser la última celda del notebook.
- **CLAUDE.md actualizado** (`Workflow: lunes estándar`): se documentaron las tres reglas de arriba como default para todo lunes estándar futuro, no solo para esta clase.
- Se regeneró todo con `python generar_lunes.py`; verificación de puntajes y casos de prueba en verde (25+30+45=100 pts, 19/19 casos OK).

## 2026-08-13 — Verificador automático agregado a la Ejercitación

Diego pidió revisar si el `Control.ipynb` y la `Ejercitación.ipynb` traían las consideraciones más recientes que se agregaron a `disenar-clase`/`generar-colab-clase`: el autochequeo (verificador automático) y la correcta indicación de `**El programa debe:**`. Revisión:

- **`**El programa debe:**`** — ya estaba completo en los 3 ítems del Control, el guiado y los 4 ejercicios, con los literales exactos (`botella`, `cierre`, `sin credencial`, `en blanco`) marcados en backtick. Sin cambios acá.
- **`Control.ipynb`** — correctamente sigue **sin** verificador: es la excepción fija documentada en `generar-colab-clase/SKILL.md` (línea ~306), instancia con nota.
- **`Ejercitación.ipynb`** — decisión de la entrada del 2026-08-12 fue dejarla **sin** verificador, apoyada solo en las soluciones colapsadas. Esa decisión es anterior en un día al default de autochequeo que se fijó para la Independiente de `Clase.ipynb` (2026-08-13). Diego decidió que Ejercitación **sí** debe llevar ambos mecanismos — el verificador para autorrevisarse sin mirar la solución primero, y las soluciones colapsadas como respaldo final.

**Cambio aplicado en `generar_lunes.py` (`build_ejercitacion`):**
- Se agregó el preámbulo canónico del "Verificador por salida" (helpers `_fuente_solucion` / `_normalizar` / `_revisar`, copiado tal cual desde `generar-colab-clase/SKILL.md`) como celda de configuración, justo después de la intro de "## 🎯 Serie de ejercicios".
- Se agregó un `verificar_ejercicio_N()` por cada uno de los 4 ejercicios, con la lista `esperadas` derivada directo del caso de prueba visible de cada uno (`test["stdout"]`), y una pista de qué datos reingresar cuando el ejercicio usa `input()`.
- El marcador de la celda de solución cambió de `# Tu solución del Ejercicio N` a `# Tu solución — Ejercicio N` (el formato exacto que usa `_fuente_solucion` en el resto del proyecto).
- El ejercicio guiado **no** lleva verificador — se resuelve en conjunto en clase, mismo criterio que la Práctica Guiada en `Clase.ipynb` nunca lo lleva.
- La sección `## 🔓 Soluciones` al final se mantiene sin cambios, como respaldo tras usar el verificador.

**Verificación:** se simuló el entorno de Colab (`get_ipython().user_ns["In"]`) fuera del notebook y se corrieron las 4 soluciones de referencia contra sus propios `verificar_ejercicio_N()` — las 4 reportan "¡Perfecto!". Se probó además una solución con bug deliberado (Ejercicio 1) para confirmar que el verificador sí detecta fallas reales, no solo aprueba todo. `python generar_lunes.py --check` sigue en verde (19/19 casos, 25+30+45=100 pts).

Pendiente de decisión de Diego: si este cambio debe quedar como default permanente para todo lunes estándar futuro (actualizando la regla del `CLAUDE.md` que hoy dice que las soluciones colapsadas son la excepción/mecanismo de autorrevisión de la Ejercitación) — por ahora el cambio se aplicó solo a Clase 23.

## 2026-08-18 — Revisión del Control de los 15 estudiantes que asistieron + Colabs personalizados de devolución

Diego pidió un plan de revisión para quienes sí asistieron (`assitencia.txt`), cruzado contra los cuadernos entregados en `controles_estudiantes/`, con criterio de corrección benevolente ("si hay errores insalvables, sacar puntaje no más").

- **Mapeo asistencia ↔ archivo:** de los 32 archivos entregados (varios alias de cuenta personal — `Vicho 11`, `Paulino González`, `julian ghost`, etc. — y varios duplicados/vacíos), se resolvieron los 15 presentes usando `alias-cuentas-conocidas.md` y leyendo cada notebook. Ningún presente quedó sin archivo, pero **3 entregaron el control completamente vacío**: Simón Abrahams, Felipe Aravena, Francisca Parra (queda pendiente que Diego confirme con ellos qué pasó). El nombre "Santiago García Colombatti" de la lista de asistencia se mapeó a "Santino Garcia Colombati" de la nómina (único con ese apellido — probable error de transcripción al tomar lista).
- **Corrección** hecha a mano por mí (sin extractor automatizado — no existía uno para este control) sobre la rúbrica parcelada de `Control Solucionario Docente.ipynb`, con calibración benevolente: crédito generoso en bordes (`>` vs `>=`, `range` off-by-one), 0 solo en componentes genuinamente insalvables (variable nunca definida, condición invertida que deja el ciclo muerto, código que no llega a compilar/ejecutar). Resultados: de 9 a 100 puntos, promedio bajo por el Ítem 3 (`while`+`continue`) — fue donde más entregas tuvieron bugs insalvables o no llegaron por tiempo.
- **Colabs personalizados de devolución**, uno por estudiante, generados con el mismo motor genérico que usan las evaluaciones sumativas (`tools/review_eval/colab_devolucion.py`): mensaje de apertura personalizado, código real + solución de referencia + desglose por componente con comentario, y nota final (exigencia 50%, escala 2,0–7,0).
- **Fuente de verdad:** `controles_estudiantes/revision/codigo_extraido_control23.json` (código extraído) + `generar_devolucion_control23.py` (rúbrica, comentarios, mensajes, cálculo). Ambos en `revision/` — no se suben a git (dato real de estudiantes).
- **Destino de los `.ipynb` finales:** se movieron a la nueva carpeta compartida `clases/EVALUACIONES-REVISADAS/CONTROLES/Clase 23 - Control de Ciclos (while, for+break, while+continue) - 2026-08-17/` (ver memoria `evaluaciones-revisadas-carpeta-compartida` — convención nueva que aplica a toda Prueba/Control futuro, no solo a esta clase). El script quedó apuntando ahí directamente para cualquier regeneración futura.
- **`.gitignore` actualizado:** se agregaron `clases/**/controles_estudiantes/` (entregas crudas, no estaba cubierto) y `clases/EVALUACIONES-REVISADAS/` (mismo criterio de privacidad que `revision/`).
- **Pendiente:** que Diego confirme el criterio de corrección antes de tratarlo como definitivo, y que aclare el mecanismo real de "compartir" la carpeta con los estudiantes (ver conversación — riesgo de que un estudiante vea la nota/errores de otro si se comparte la carpeta completa en vez de por control/curso).
