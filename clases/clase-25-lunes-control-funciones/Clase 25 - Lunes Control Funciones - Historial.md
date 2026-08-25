# Clase 25 — Lunes Control Funciones · Historial

**Fecha de aplicación:** lunes 2026-08-24
**Formato:** lunes estándar (ejercitación en parejas sorteadas + control individual con nota + revisión)
**Clases foco:** N°24a (def, parámetros, return) y N°24b (uso del retorno: guardar y reutilizar)

---

## 2026-08-19 — Diseño y generación

Segunda aplicación del formato "lunes estándar" (la primera fue Clase 23, 2026-08-17). La carpeta ya existía vacía, creada por Diego con `Investigación freeCodeCamp Python - Ideas Evaluaciones, Controles y Proyectos.md` como insumo de brainstorm (documento de investigación pura, sin decisiones — las decisiones de qué adoptar se tomaron en esta sesión).

### Decisiones tomadas con Diego en esta sesión

- **Sin contenido nuevo, foco explícito en los dos puntos de quiebre diagnosticados en 24b** (ver memoria `funciones-consolidar-antes-de-avanzar`): (1) el patrón `variable = funcion(argumento)` — guardar antes de reutilizar, no solo antes de imprimir — y (2) el caso `None` cuando una función usa `print()` en vez de `return`. Ninguno de los 3 ítems introduce sintaxis nueva de funciones (nada de valores por omisión, `*args`, funciones que llaman a otras funciones).
- **Actitud elegida:** Confianza en el proceso — encaja con sostener el patrón definir→consultar→evaluar→imprimir bajo la presión de tiempo del control individual, entre 4 opciones propuestas (Confianza en el proceso, Constancia, Método —repetir la de 24b—, Precisión).
- **Cierre de actitud:** Familia 2 (Evidencia + consecuencia), rotando desde la Familia 1 que usó Clase 23.
- **Ítem 3 = función + `if/elif/else`** (no función + ciclo), a pedido explícito de Diego — mismo tipo de combinación que ya usó la Guiada/Ejercicio 3 de 24a.
- **Ronda de revisión de distintividad (a pedido de Diego):** la primera versión de los 4 ejercicios/ítems quedó demasiado calcada de los notebooks ya generados de 24a/24b (el guiado repetía literalmente `ganancia_venta` de la Guiada de 24b; el Ítem 2 repetía la mecánica exacta de "dos llamados sumados + comparación con meta" de esa misma Guiada; el Ítem 3 repetía la forma de `cobro_entrada` — tramos de edad que retornan el precio final directo). Se rediseñaron los 4:
  - **Guiado** — de "puesto de cerámica" (clon de `ganancia_venta`) a "ahorro para el viaje de estudios a Valparaíso": mecanismo nuevo, encadenar dos llamados (el resultado del primero es argumento del segundo), no sumar dos llamados independientes.
  - **Ítem 1** — de "taller de serigrafía" (`base + tasa*cantidad`) a "piscina municipal / estacionamiento de bicicletas": resta simple sin condicional, patrón nunca usado en los independientes de 24a/24b.
  - **Ítem 2** — de "muestra folclórica" (dos llamados sumados + meta) a "bingo solidario / rifa del taller de teatro": un solo llamado, guardado, reutilizado restándole un gasto pedido aparte.
  - **Ítem 3** — de `bono_categoria(edad)` (tramos de edad, retorna el precio final) a "pedido de arcilla / entradas a la muestra de cortometrajes": la función retorna un **descuento** por tramo de cantidad, que se resta de un total bruto calculado aparte — dos pasos combinados, no uno.
- **Contextos nuevos, ninguno repetido:** ahorro/viaje de estudios, estacionamiento de bicicletas, piscina municipal, rifa de teatro, bingo del Centro de Padres, muestra de cortometrajes, pedido de arcilla — ninguno coincide con kiosco, huerto, club deportivo, peña de la vendimia, Escuela de Rock, biblioteca, radio escolar o ajedrez ya usados en 24a/24b.
- **Casos de prueba con progresión típico → borde**, siguiendo el hallazgo 1.3 del documento de investigación freeCodeCamp: cada ítem trae un caso visible típico y casos ocultos que aíslan el límite exacto de una condición (`>=` vs `>`) o un resultado en cero — sin adoptar el resto del documento (quizzes MCQ, verificación AST, etc., fuera de alcance de este control).
- **Rúbrica:** componente explícito en los 3 ítems que penaliza usar `print()` en vez de `return` dentro de la función (el error que produce `None`) — la forma "constructiva" de evaluar el mismo punto de quiebre que el Ticket de Salida de 24b evaluaba por predicción.

### Artefactos generados

| Archivo | Destino |
|---|---|
| `Clase 25 - Lunes Control Funciones - Propuesta.json` | Fuente de verdad (ejercitación + control + rúbrica) |
| `generar_lunes.py` | Generador y verificador (adaptado del de Clase 23). **Nunca editar los `.ipynb` a mano** |
| `Clase 25 - Lunes Control Funciones - Ejercitación.ipynb` | Estudiantes (Colab) — guiado + 3 ejercicios + verificador automático + `## 🔓 Soluciones` |
| `Clase 25 - Lunes Control Funciones - Control.ipynb` | Estudiantes (Classroom) — 3 ítems, sin soluciones |
| `Clase 25 - Lunes Control Funciones - Control Solucionario Docente.ipynb` | Profesor + agente corrector — rúbrica parcelada + criterios |
| `Clase 25 - Lunes Control Funciones - Control Solucionario Estudiantes.ipynb` | Publicar después de aplicado el control — sin rúbrica de puntos |

### Mapeo ejercitación ↔ control

| Ejercitación | Control | Habilidad |
|---|---|---|
| Guiado — Ahorro viaje de estudios a Valparaíso | *(sin hermano — recordatorio del patrón completo)* | función con `return`, encadenar un llamado sobre el resultado del anterior |
| Ej. 1 — Estacionamiento de bicicletas del liceo | Ítem 1 — Piscina municipal de Isla de Maipo | función con `return`, guardar en variable e imprimir (sin condicional) |
| Ej. 2 — Rifa del taller de teatro | Ítem 2 — Bingo solidario del Centro de Padres | guardar el resultado de una función y reutilizarlo en un cálculo posterior |
| Ej. 3 — Muestra de cortometrajes del taller audiovisual | Ítem 3 — Pedido de arcilla para el taller de cerámica | función con `if/elif/else` que retorna un descuento, combinado con un total calculado aparte |

### Verificación

`python generar_lunes.py --check` corre cada solución de referencia contra sus casos de prueba (con `input()` simulado) y valida que los componentes de la rúbrica sumen el puntaje declarado de cada ítem y del control completo.

Resultado al generar: **18/18 casos OK**, puntajes cuadrados (25 + 30 + 45 = 100).

### Publicación

- `Ejercitación.ipynb` puede subirse el lunes 24-ago en la mañana.
- **`Control.ipynb`, `Control Solucionario Docente.ipynb` y `Control Solucionario Estudiantes.ipynb` no se pushean hasta después de aplicado el control** — el repo es público, mismo criterio que rige para `Ticket de Salida.pptx` y para Clase 23.

### Pendientes

- Corrección de las entregas reales tras dictar la clase (mismo flujo que Clase 23: extractor programático + rúbrica parcelada + Colabs de devolución en `EVALUACIONES-REVISADAS/CONTROLES/`).
- Sigue pendiente definir **X** (controles eliminables al cierre del semestre) — no bloquea esta clase.

## 2026-08-19 — Pistas desplegables agregadas (Ejercitación y Control)

Diego fijó una regla permanente: de ahora en adelante siempre se agregan 1-2 pistas desplegables (`<details>`) por ejercicio, salvo en instrumentos con nota (Control/Evaluación), donde el default sigue siendo sin pistas y él avisa explícitamente, instancia por instancia, si quiere agregarlas — y confirmó que sí quiere para este Control en particular. Regla 15.3 del `CLAUDE.md` raíz actualizada con el alcance ampliado (aplica también a la `Ejercitación.ipynb` de un lunes estándar, no solo a la Práctica Independiente de una clase regular) y la excepción permanente de Control/Evaluación.

- **Ejercitación** — 1 pista por ejercicio (3 en total): resta simple sin condicional (Ej. 1), guardar el ingreso antes de restar el gasto (Ej. 2), separar el cálculo del total bruto del cálculo del descuento (Ej. 3). El guiado no lleva pista (se resuelve en conjunto en clase).
- **Control** — 1 pista en los Ítems 1 y 2 (mismo criterio que sus hermanos), 2 pistas en el Ítem 3 (el más difícil): separar el total bruto de la función, y usar `>=` en los límites de tramo.
- `Propuesta.json` actualizado con el campo `pistas` en cada ejercicio/ítem; `generar_lunes.py` con el helper `bloque_pistas()`, insertado entre `statement_md` y el bloque de resultado esperado/ejemplo válido — mismo lugar canónico que usa `generar-colab-clase` para la Práctica Independiente.
- Los 4 notebooks se regeneraron; `--check` sigue en verde (18/18 casos, 25+30+45=100 pts).

## 2026-08-21 — Piloto: ejercicios "0" de práctica directa en la Ejercitación

Diego pidió probar un nuevo tipo de ejercicio para la Práctica Independiente/Ejercitación: 1-2 ítems iniciales muy directos que aplican la definición pelada del contenido (sin narrativa, sin disfrazar el constructo), antes de los ejercicios con contexto — a diferencia de los Ejercicios 1-3 actuales, que ya traen narrativa aunque sean "directos". Se usó esta Ejercitación como maqueta de trabajo para probar el formato antes de decidir si se generaliza al `CLAUDE.md`.

- **Agregados `Ejercicio 0a` y `Ejercicio 0b`**, insertados después del verificador automático y antes del Ejercicio 1 (sin renumerar 1-3). Consigna técnica explícita, sin narrativa ni pistas:
  - **0a** — definir función con `return`, llamar, guardar, imprimir (`calcular_total`, dos números → suma).
  - **0b** — mismo patrón pero reutilizando el resultado guardado en un cálculo posterior, sin volver a llamar la función (`calcular_doble`, número → doble, luego +10).
- Se decidieron 2 (no 1) porque el objetivo de la clase tiene dos matices distintos que ameritan drill separado: `return` vs `print()`, y reutilizar un resultado guardado.
- **⚠️ Edición manual directa del `.ipynb`, sin pasar por `Propuesta.json` / `generar_lunes.py`.** Es un piloto explícito de Diego — el resto del flujo del proyecto exige que el `.ipynb` nunca se edite a mano y que `Propuesta.json` sea la fuente de verdad. Si se corre `generar_lunes.py` (regeneración o `--check`) sin antes portar estos dos ejercicios al JSON, **se pierden**. Pendiente: si Diego confirma que el formato funciona bien en clase, portar 0a/0b a `Propuesta.json` y generalizar la regla en el `CLAUDE.md` (regla 16); mientras tanto, no regenerar este archivo desde el script.
- Alcance: solo piloto en Clase 25 por ahora. `Control.ipynb` no se tocó.

## 2026-08-25 — Corrección de las entregas reales

Diego subió las 40 entregas descargadas de Classroom (`controles/controles_jupyters/`) + `controles/asistencia.txt`. La primera versión de la asistencia tenía errores (confirmados por Diego en el camino): tres estudiantes marcados presentes en realidad no vinieron (Benjamín Mejías González, Simón Abrahams Delgado, Vicente Benítez Muñoz — sus tres archivos de Control estaban completamente vacíos, consistente con la ausencia). La lista corregida que Diego entregó quedó en **20 asistieron / 11 no asistieron**; de los 20, Felipe Aravena Cárdenas hizo el control pero lo dejó en un pendrive — queda pendiente, se agrega cuando lo suba.

**Universo calificado: 19 estudiantes.** Extracción programática de código (`controles/revision/extraer_control25.py`, resolviendo los alias de cuenta ya documentados en `alias-cuentas-conocidas.md`: `polar tv` → Julián Aravena Sagal, `Estudiante Profesor Diego 1` → Alex Saravia Lara, `Vicho 17` → Vicente Narváez Fernández, confirmados por el nombre declarado en el encabezado de cada entrega puntual) + corrección con la rúbrica parcelada del Solucionario Docente (`controles/revision/generar_devolucion_control25.py`), **cada código ejecutado de verdad** contra los 3 casos de prueba de cada ítem (visibles y ocultos) — no se leyó ningún output pegado. Criterio benevolente confirmado por Diego (mismo que Clase 23): parcial generoso quando el comportamiento final es correcto aunque la estructura no siga el patrón pedido al pie de la letra; solo 0 cuando el error es insalvable.

### Resultado

| Estudiante | Puntaje | Nota |
|---|---|---|
| Santino García Colombati | 100/100 | 7,0 |
| Eduardo Pacco Ríos | 97/100 | 6,8 |
| Francisco Vega Sanhueza | 97/100 | 6,8 |
| Diego Peña Bustamante | 91/100 | 6,5 |
| Cristóbal Muñoz Cubillos | 90/100 | 6,4 |
| Felipe Román Brito | 89/100 | 6,3 |
| Maura Muñoz Gutiérrez | 83/100 | 6,0 |
| Alex Saravia Lara | 70/100 | 5,2 |
| Sebastián Ulloa Cuevas | 55/100 | 4,3 |
| Lucas Valenzuela Donoso | 48/100 | 3,9 |
| Diego Donoso Figueroa | 42/100 | 3,7 |
| Julián Aravena Sagal | 25/100 | 3,0 |
| Vicente Narváez Fernández | 20/100 | 2,8 |
| Damián Flores Silva | 15/100 | 2,6 |
| Martín Sánchez Orellana | 5/100 | 2,2 |
| Francisca Parra Marínquez | 5/100 | 2,2 |
| Benjamín Díaz Silva | 0/100 | 2,0 |
| Diego Vargas Jaqui | 0/100 | 2,0 |
| Diego Cifuentes Tessada | 0/100 | 2,0 |
| **Felipe Aravena Cárdenas** | *pendiente (pendrive)* | — |

Sin décimas de bono. Exigencia 50%, escala 2,0-4,0-7,0.

**Hallazgos de la corrección real por ejecución** (no visibles con una lectura superficial):
- Julián Aravena Sagal parecía tener las 3 funciones "desarrolladas" por el largo del archivo, pero ninguna se llega a llamar ni a imprimir en ningún ítem — 25/100 real.
- Diego Peña Bustamante y Felipe Román Brito tienen el límite del tramo medio del Ítem 3 mal puesto (`kilos > 10` en vez de `kilos >= 10`) — falla justo en el caso borde de 10 kilos exactos; en el de Felipe Román el programa ni siquiera imprime nada para ese caso.
- Varios (Diego Peña, Cristóbal Muñoz, Felipe Román) resolvieron el Ítem 3 con la lógica de tramos fuera de la función pedida — comportamiento final correcto en la mayoría de los casos, pero no el patrón enseñado.

### Artefactos generados (no se suben a git)

| Archivo | Ubicación |
|---|---|
| `codigo_extraido_control25.json` | `controles/revision/` |
| `generar_devolucion_control25.py` | `controles/revision/` |
| `resultado_control25.json` | `controles/revision/` — fuente cruda (puntaje + nota por estudiante) para la trazabilidad acumulada |
| 19 Colabs `<Nombre> - Revisión Control.ipynb` | `clases/EVALUACIONES-REVISADAS/CONTROLES/Clase 25 - Control de Funciones - 2026-08-24/` (carpeta compartida con el curso) |

`.gitignore` actualizado: se agregó el patrón `clases/**/controles/` (la carpeta `controles/` de esta clase no calzaba con el patrón previo `controles_estudiantes/`).

### `clases/Controles - Trazabilidad.xlsx` — primera versión (2026-08-25)

No existía ningún registro acumulado de controles hasta ahora (tampoco se había construido para Clase 23). Se armó siguiendo la misma arquitectura que `Ticket de Salida - Trazabilidad.xlsx`: un script (`tools/controles_trazabilidad/actualizar_trazabilidad.py`) que reconstruye el Excel completo desde cero escaneando cualquier `resultado_control*.json` bajo `clases/` (fuente cruda que cada script de corrección de control escribe a partir de la misma estructura que generó los Colabs de devolución, sin duplicar datos a mano) + la nómina oficial. Tres hojas: Detalle (fila por estudiante × control), Resumen por estudiante (nota por control + promedio), Resumen por clase (estadísticas agregadas). Sí se sube a git (mismo criterio que la Trazabilidad de Ticket de Salida: son solo nombres, puntajes y notas agregadas, no código de estudiantes).

**Por ahora solo cubre Clase 25** (19 estudiantes, 1 control) — Clase 23 no está backfillada porque su script de corrección (`generar_devolucion_control23.py`) no escribió un `resultado_control23.json` en su momento. Es rápido de agregar si Diego lo pide (el script ya tiene toda la data en su dict `ESTUDIANTES`, solo falta el mismo bloque de exportación que se le agregó a Clase 25).

### Pendientes

- Felipe Aravena Cárdenas — corregir cuando suba su entrega real, y agregar su puntaje a `resultado_control25.json` (regenerando `generar_devolucion_control25.py` y `actualizar_trazabilidad.py`).
- Backfill de Clase 23 en `Controles - Trazabilidad.xlsx` (opcional, ver arriba).
- Definir **X** (controles eliminables al cierre del semestre) — sigue sin bloquear.
