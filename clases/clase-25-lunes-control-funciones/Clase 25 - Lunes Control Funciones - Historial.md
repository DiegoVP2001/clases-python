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
