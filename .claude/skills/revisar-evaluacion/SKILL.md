---
name: revisar-evaluacion
description: Orquesta la revisión completa de una evaluación Python — desde preparar las entregas (submissions) hasta calibrar la rúbrica, revisar en lotes, generar el resumen final y el feedback individual en Excel. Usa esta skill cuando Diego diga que quiere revisar, calificar o corregir entregas, evaluaciones o notebooks de estudiantes (ej. "revisemos las entregas de Classroom", "quiero calificar los notebooks").
---

# Skill: revisar-evaluacion

## Propósito

Orquestar la revisión completa de una evaluación Python: desde la lectura de notebooks de estudiantes hasta generar el resumen final (md, csv, xlsx) y el feedback individual en Excel.

## Cuándo activar

Cuando Diego diga algo como "vamos a revisar la evaluación", "quiero calificar los notebooks" o "revisemos las entregas de Classroom".

---

## Flujo de trabajo

### Fase 0 — Preparar submissions

1. Leer los notebooks de estudiantes en la carpeta de entregas de la evaluación.
2. Ejecutar `tools/review_eval/preparar_submissions.py` para crear `revision/puntajes.json` con la estructura inicial de todos los estudiantes.
3. Verificar que `puntajes.json` tiene todos los estudiantes del curso (consultar `referencia-estudiantes` para la nómina oficial).

### Fase 0.5 — Extraer el código programáticamente ⚠️ OBLIGATORIA

**Ningún script, subagente ni persona transcribe código de estudiante a mano. Nunca.**

Escribir un extractor que lea cada `.ipynb` y produzca `revision/codigo_extraido_<evaluacion>.json` con el código real de cada ítem por estudiante. De ahí en adelante, **esa es la única fuente del código de estudiante** — ningún script posterior vuelve a abrir un `.ipynb` de entrega.

Reglas del extractor:
- **Anclar por encabezado markdown** (`**Ítem 1A.1**`, `## 🎯 Ejercicio N`), nunca por índice fijo de celda: siempre hay entregas con una celda de más que desalinean el índice.
- El código de un ítem es la concatenación de **todas** las celdas de código entre su ancla y la siguiente (tolerar celdas markdown sueltas o vacías entre medio).
- Antes de cerrar la fase, verificar que **todas** las entregas resolvieron el 100% de las anclas, y revisar a mano los casos que emitan advertencias.

> **Por qué es obligatoria.** En la Evaluación 2 la calibración se hizo transcribiendo código a mano a un diccionario Python. Un estudiante tenía programas completos en dos ejercicios que la transcripción registró como celda vacía: se le calificó 0/18 y 0/24 sobre código real. Hubo que reiniciar el proceso completo.

### Fase 1 — Calibrar la rúbrica parcelada por componentes

**Esta fase es obligatoria antes de calificar el primer batch.**

**No uses el modelo todo-o-nada** (un puntaje por ítem con niveles ✅/⚠️/❌ sobre el ítem completo). Ese modelo manda a 0 respuestas que tienen la mitad de la lógica correcta. Usa **rúbrica parcelada**: cada ítem se divide en 2-5 componentes independientes, cada uno con su propio presupuesto de puntos y sus propios niveles. El puntaje del ítem es la suma.

**Cómo parcelar según el tipo de ítem:**

| Tipo de ítem | Cómo se parcela | Componentes típicos |
|---|---|---|
| **Programa completo** (el estudiante escribe todo) | Por **piezas del programa** | lectura del dato y su tipo · valores exactos (umbrales) · operadores de comparación · estructura de ramas · anidamiento/dependencia entre bloques · uso genuino de las variables (no hardcodear) · mensajes distinguibles por camino |
| **"Arma la expresión"** (la línea está en blanco, las variables dadas) | Por **piezas de la expresión** | usa las variables dadas (no hardcodea el valor) · cada operador en su rol |
| **"Arregla el bug"** (el fragmento ya venía escrito y correcto salvo un error) | Por el **acto de corregir** — ver abajo | 🔎 Diagnóstico · 🔧 Corrección · 🛡️ Sin daños |

**Los ítems "arregla el bug" son el caso especial.** Si los parcelas por piezas del programa, todos ganan puntos por el código que ya traía el enunciado, incluso quien entregue la celda sin tocar nada. Por eso se parcela el acto de corregir:

- 🔎 **Diagnóstico** — ¿modificó el elemento que causaba el bug?
- 🔧 **Corrección** — ¿el cambio deja la lógica correcta?
- 🛡️ **Sin daños** — ¿el resto del fragmento quedó intacto y ejecuta?

con la **regla de portazo**: *si Diagnóstico = 0, el ítem completo es 0.* No se premia entregar el código tal como llegó. El motor de Fase 5 valida esta regla con un `assert`.

**Pasos:**
1. Leer el solucionario de la evaluación.
2. **Antes de proponer nada, mirar el código real de todos los estudiantes** en el JSON de Fase 0.5 y ejecutarlo. La rúbrica se diseña sobre los patrones que aparecieron de verdad, no sobre patrones imaginados.
3. Proponerle a Diego la tabla de componentes por ítem, con los deltas de puntaje que provoca sobre los casos ya revisados. **Esperar aprobación.**
4. Guardar en `revision/rubrica_parcelada_<evaluacion>.md` + `revision/criterios_calibracion.json`.
5. **No calificar ningún notebook antes de terminar esta fase.**

**Criterios permanentes** (aplican a toda evaluación, no se renegocian):
- **No se evalúa eficiencia ni elegancia del código, solo lo que hace.** Ramas repetidas, condiciones de más, nombres raros o pasos innecesarios **no descuentan**. Solo descuenta lo que produce un resultado equivocado. Al redactar una razón: si señala algo que no cambia lo que el programa entrega, se saca.
- **Nunca penalizar el mismo bug en dos componentes.**
- **Verificar ejecutando, nunca el output pegado en la celda.** Colab no re-ejecuta al editar, así que el output visible puede estar desactualizado. Si el estudiante cambió valores que venían fijos en el enunciado, reponer los originales y calificar la lógica que escribió.
- **Se califica el comportamiento, no la forma.** Una estructura aplanada o reescrita que produce el resultado correcto en todos los casos vale el puntaje completo, aunque no se parezca a la solución de referencia.

> La rúbrica NO es estática. Cada evaluación tiene su propio solucionario y sus propios criterios. Nunca asumir criterios de evaluaciones anteriores — lo que sí se hereda es el **método** de arriba.

### Fase 2 — Revisar en batches (subagentes en paralelo + gate de consolidación)

Repartir los estudiantes en batches de 4-5 y lanzar **un subagente por batch, todos en paralelo**. Es varias veces más rápido que secuencial y no pierde calidad, **con una condición innegociable: el gate de consolidación de más abajo.**

**Antes de lanzar nada, escribir el prompt del subagente una sola vez y validarlo.** Correrlo primero sobre 2 estudiantes elegidos porque entre ambos activan las reglas más difíciles, contra una calificación independiente hecha a ciegas por la sesión principal. Si no coinciden, el problema es el prompt, no el subagente. Guardar el prompt validado en `revision/PROMPT_BATCH_<evaluacion>.md` junto con la composición de los batches.

El prompt debe obligar a: sacar el código **solo** del JSON de Fase 0.5, **ejecutar** cada ítem con un runner compartido (ver abajo), puntuar componente por componente en el orden de la rúbrica, y devolver **solo JSON, sin escribir ningún archivo**. Más un campo `patrones_nuevos` donde el subagente reporta lo que no calza en la rúbrica en vez de inventar un puntaje.

**Runner compartido (`ejecutar_item.py`).** Un script que corre una batería fija de casos por ítem — todos los caminos y los valores límite de cada umbral, reponiendo los valores que el enunciado traía fijos si el estudiante los cambió. Que los cuatro agentes midan exactamente lo mismo es lo que hace comparables sus puntajes. Sin esto, cada uno prueba lo que se le ocurre.

**🚩 Gate de consolidación — obligatorio antes de escribir un solo puntaje.**

```bash
python tools/review_eval/gate_consolidacion.py \
    --codigo revision/codigo_extraido_<evaluacion>.json \
    --batches b1.json b2.json b3.json b4.json \
    --items-bug 1B.1 1B.2 ... --items-programa 2.1 2.2 ...
```

Verifica aritmética, estructura (todos con los mismos ítems y componentes), regla de portazo, cobertura (celda vacía ⇒ 0), **consistencia entre batches** y sintaxis, y junta los `patrones_nuevos` de todos.

La verificación que justifica el gate es la de **consistencia**: agrupa el código real normalizado —sin comentarios, sin nombres de variable, sin el texto de los mensajes— y avisa si dos estudiantes con código equivalente recibieron puntajes distintos. El riesgo del paralelismo no es que un agente se equivoque, es que dos califiquen el mismo patrón distinto sin que nadie lo note.

> **Lo que el gate NO puede hacer, y por eso hay que hacerlo a mano:** detecta cuando dos agentes se contradicen, no cuando los cuatro se equivocan igual. **Verifica siempre un par de estudiantes por tu cuenta**, ejecutando su código con el runner, eligiendo los casos de mayor riesgo (los que el gate marcó, los que reportaron patrones nuevos, los puntajes extremos).
>
> **Al leer el flag de consistencia, mira el código crudo antes de concluir.** El normalizador borra los strings, así que un ítem donde lo que falla es *qué mensaje quedó en cada rama* aparece como "equivalente" siendo distinto. En la Evaluación 2 el único flag fue exactamente eso: un falso positivo.

**Cerrar los `patrones_nuevos` con Diego antes de escribir.** Cada patrón se resuelve **subiéndolo a la rúbrica** —para que aplique igual a todos— y nunca parchando el puntaje de un estudiante. Presentárselos juntos, con el impacto en puntos de cada opción y una recomendación.

**Recién entonces, escribir los puntajes.** Si los cuadernos de Fase 5 se arman desde una estructura de datos (lo normal), usar `escribir_puntajes()` del motor: deriva `puntajes.json` de **la misma fuente** que arma los Colabs, así el cuaderno que ve el estudiante y el JSON que alimenta el resumen final no pueden divergir. Es el mismo principio que hace que el código venga siempre del extractor.

> **Dos señales de que la rúbrica necesita un nivel nuevo,** las dos aparecieron en la Evaluación 2 y valen para cualquiera:
> - **Un nivel que castiga más al que lo hizo mejor.** Si un patrón que entrega el resultado correcto saca menos que uno que revienta, el nivel está definido por la forma y no por el comportamiento. Redefinirlo por comportamiento.
> - **Un error transversal que ningún componente mide.** Ej.: el ítem no compila, así que no imprime nada, pero todas las decisiones de lógica están bien. No lo repartas a la fuerza dentro de los componentes: agrégalo como **penalización del ítem** (`"penalizacion": {...}`), que se muestra como fila propia en la tabla y se resta del total sin bajar de 0.

### Fase 3 — Calcular notas

Ejecutar `tools/review_eval/calcular_notas.py` para agregar los totales y notas al `puntajes.json`.

Fórmula chilena (dos tramos lineales):
- `nota_min = 2.0`, `nota_aprobacion = 4.0`, `nota_max = 7.0`
- Exigencia por defecto: **50%**
- Si Diego indica otra exigencia, usar esa.

### Fase 4 — Generar resumen final

Ejecutar `tools/review_eval/generar_resumen_final.py`.

**Exclusiones obligatorias:**
- Estudiantes ausentes (total == 0)
- Estudiantes excluidos por deshonestidad académica (configurar en `EXCLUDED` del script)

> Nota: las exclusiones por deshonestidad son específicas de cada evaluación. No son permanentes. Verificar con Diego cuáles aplican.

Genera:
- `revision/resumen_final.md` — tabla markdown con puntajes y estadísticas
- `revision/resumen_final.csv` — importable a Google Sheets
- `revision/resumen_final.xlsx` — Excel formateado con color coding

### Fase 5 — Colab personalizado de devolución (formato principal)

Un `.ipynb` por estudiante que sirve dos veces: primero Diego lo revisa para auditar la corrección, y después se le entrega tal cual al estudiante. **Reemplaza al Excel de feedback** como formato principal de devolución.

Motor: `tools/review_eval/colab_devolucion.py`. El script de cada evaluación arma un objeto `Devolucion` con lo suyo (ítems, componentes, soluciones de referencia, puntajes y razones por estudiante) y llama a `generar_colabs()`. El motor pone el formato y las validaciones.

**Estructura de cada cuaderno:**
1. Mensaje de apertura personalizado (ver abajo).
2. Puntaje total + explicación de cómo se corrigió.
3. Por ítem: tabla de componentes (Componente | Puntaje | Comentario) → 📝 "Lo que escribiste" (código verbatim del JSON de Fase 0.5) → ✅ "Cómo debía quedar" (solución de referencia anotada con comentarios inline en las líneas donde faltó algo, cerrando con un bloque `💬 En simple: ...`).
4. **La nota se pregunta, no se asume.** Antes de generar, preguntarle a Diego si los cuadernos van **con nota o solo con puntajes** — depende de si los entrega junto con las notas oficiales o antes. Si van con nota, preguntar también **qué décimas de bono aplican** (suelen venir de una actividad previa registrada aparte). Se activa con `mostrar_nota=True` y `decimas={...}` en `Devolucion`; ambos vienen apagados por defecto. El cuaderno muestra entonces `Puntaje → Nota (exigencia) → Décimas → Nota final`, arriba y al cierre.
5. **Repartir los cuadernos en carpetas por tramo de logro** si Diego lo pide (`tramos_logro` en `Devolucion`, ej. 0-59% / 60-79% / 80-100%). El tramo se calcula sobre el **puntaje**, no sobre la nota con décimas: las décimas son bono, no logro demostrado en la prueba.

> **Las décimas se leen del archivo donde están registradas, no se copian al script.** Mismo principio que el código de estudiante. Poner un `assert` que reviente si algún estudiante queda fuera del registro: sin eso, un nombre que no calza suma 0 en silencio.

**Estilo del feedback — aplica a todos los cuadernos:**

1. **Mensaje de apertura, siempre, sea cual sea el resultado.** Encabezado *"📬 Antes de ver los puntajes, lee este mensaje"* + un kaomoji (`ヘ( ^o^)ノ`, `ᕦ(ò_óˇ)ᕤ`, `٩(◕‿◕)۶`, `(๑˃ᴗ˂)ﻭ`, `\(^▽^)/`, `( •̀ ω •́ )✧`, `(๑•̀ㅂ•́)و✧`…). **Habla en macro: de las lógicas y habilidades** que la persona ya maneja y las que le toca trabajar — no referencia ejercicios ni secciones en detalle, para eso está el desglose. Parte por lo que **sí** logró (todos tienen algo), da ánimo, cierra abriendo camino con otro kaomoji. Se adapta al resultado; no es la misma plantilla para todos.
2. **Cierres `💬 En simple` de 2-3 frases.** Explican la idea de fondo y qué mirar, no todo el razonamiento de la corrección — el detalle ya está en la tabla y en los comentarios inline.
3. **Tono suave.** Nunca apilar el error sobre sí mismo. Fuera: *"el problema es doble"*, *"además"*, *"ni siquiera"*, *"quedó roto"*, *"la salida quedó sucia"*. Se describe qué falta y qué efecto tiene, **una vez**, y se pasa a qué hacer. Preferir "lo que falta es…", "el detalle que lo cambia todo es…", "con X calza exacto".
4. **Ítems en blanco o sin corregir: decir qué estudiar.** En vez de "no hay nada que evaluar", indicar en concreto qué contenido repasar (un dict `QUE_ESTUDIAR` con una entrada por ítem) y recordar que el puntaje se reparte por partes, así que escribir aunque sea el comienzo suma.
5. **Sin bloques de "evidencia de ejecución".** El código igual se verifica ejecutándolo, pero al estudiante no se le muestran tablas de trazas. Si un caso concreto ayuda, va en una frase dentro de la razón del componente ("con 12 días muestra X").

### Fase 5b — Excel de feedback (opcional)

Solo si Diego lo pide además del Colab. Ejecutar `tools/review_eval/generar_feedback.py`.

Genera `revision/feedback_estudiantes.xlsx`:
- Hoja "Bienvenida": lista alfabética de nombres con hipervínculo a la hoja del estudiante
- Una hoja por estudiante, nombradas anónimamente ("Estudiante 1", "Estudiante 2", …) ordenadas por puntaje descendente
- Dentro de cada hoja: tabla de ejercicios, total, nota, mensaje motivacional según nivel
- Sin nombre del estudiante dentro de la hoja individual (privacidad)

Mensajes motivacionales según nivel:
- **Aprobado (nota ≥ 4.0):** celebrar la dedicación, proyectar hacia el futuro
- **Medio (total ≥ 30, nota < 4.0):** validar el avance, señalar que la aprobación está cerca
- **Reprobado (total < 30):** no desanimar, expresar confianza del profesor, normalizar el error como aprendizaje

---

## Archivos del sistema

| Archivo | Propósito |
|---|---|
| `tools/review_eval/preparar_submissions.py` | Inicializa `puntajes.json` con todos los estudiantes |
| `tools/review_eval/gate_consolidacion.py` | **Gate obligatorio tras los batches paralelos** — aritmética, estructura, portazo, cobertura, consistencia entre batches y sintaxis |
| `tools/review_eval/colab_devolucion.py` | **Motor genérico del Colab de devolución** (formato, nota/décimas/tramos, validaciones de rúbrica) y `escribir_puntajes()` |
| `tools/review_eval/actualizar_batch.py` | Ingreso manual de un batch (legado; con `escribir_puntajes()` ya no hace falta) |
| `tools/review_eval/calcular_notas.py` | Calcula totales y notas |
| `tools/review_eval/generar_resumen_final.py` | Genera md, csv, xlsx del curso |
| `tools/review_eval/generar_feedback.py` | Excel de feedback individual (opcional, Fase 5b) |
| `revision/codigo_extraido_<evaluacion>.json` | **Única fuente del código de estudiante** (Fase 0.5) |
| `revision/ejecutar_item.py` | Runner compartido: batería fija de casos por ítem, para que todos los correctores midan lo mismo |
| `revision/PROMPT_BATCH_<evaluacion>.md` | Prompt validado del subagente + composición de los batches |
| `revision/puntajes.json` | Fuente de verdad de los puntajes |
| `revision/rubrica_parcelada_<evaluacion>.md` | Tabla de componentes por ítem, aprobada por Diego |
| `revision/criterios_calibracion.json` | Calibraciones adicionales y registro de decisiones de la evaluación |
| `revision/PLAN_REVISION_<evaluacion>.md` | Estado del avance por fase — **fuente de verdad al retomar en otra sesión** |

**Implementación de referencia (Evaluación 2 — Clase 19, Condicionales):** `clases/clase-19-evaluacion-condicionales/version-dia/revision/` tiene el ciclo completo — extractor (`extraer_codigo_evaluacion2.py`), las dos rúbricas parceladas, el plan de fases con su registro de avance (`PLAN_REVISION_EVALUACION2.md`) y el script que alimenta al motor (`generar_colab_personalizado_evaluacion2.py`). Úsalo como plantilla al empezar una evaluación nueva.

---

## Defaults

| Parámetro | Valor |
|---|---|
| Exigencia | 50% |
| Escala | 2.0 – 7.0 (nota de aprobación: 4.0) |
| Formato feedback | Excel (hoja por estudiante) |
| Formato resumen | md + csv + xlsx |

---

## Reglas críticas

1. **Nunca transcribir código de estudiante a mano.** Todo pasa por el extractor programático de Fase 0.5. Es la regla más importante de esta skill: romperla ya costó reiniciar una revisión completa.
2. **Verificar ejecutando el código, nunca el output pegado en la celda.**
3. **Calibrar siempre antes de calificar,** con rúbrica parcelada por componentes. No asumas criterios de evaluaciones anteriores; sí hereda el método.
4. **No se evalúa eficiencia ni elegancia del código, solo lo que hace.** Criterio permanente de Diego.
5. **Un patrón nuevo se sube a la rúbrica, no se parcha en el estudiante** — así aplica igual a los que faltan.
6. **Nunca incluir ausentes en el resumen final.** Filtrar por `total == 0`.
7. **Exclusiones por deshonestidad son específicas de cada evaluación.** Confirmar con Diego cuáles aplican.
8. **Batches de 4-5 estudiantes, en paralelo, con gate de consolidación obligatorio antes de escribir nada.** Los subagentes no tocan archivos: devuelven JSON.
9. **Preguntar si el Colab de devolución va con nota**, y con qué décimas — no asumir ninguna de las dos. En el Excel de feedback, no mostrar el nombre del estudiante dentro de su hoja, solo en la hoja de Bienvenida.
10. **`NAME_OVERRIDES`** en los scripts permite corregir nombres mal escritos o nicknames (ej: "Estudiante Profesor Diego 1" → "Alex").
11. **Nada de `revision/` se sube a git sin autorización explícita.** Contiene código y puntajes de estudiantes reales, y el repo `clases-python` es público.
12. **Diego prefiere una sesión nueva por fase.** No asumir que se sigue calificando en la misma sesión donde se calibró; cerrar cada fase dejando el estado escrito en el plan de la evaluación.
