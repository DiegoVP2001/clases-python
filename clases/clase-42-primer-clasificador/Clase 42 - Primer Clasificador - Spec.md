# Clase 42 — Primer clasificador ML

**Estado:** Spec aprobada — 2026-11-03 (objetivo simplificado por Diego: «entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico»; dataset, casos nuevos, escenarios y tiempos aprobados tal cual)
**Clase Picuino:** N/A — bloque de IA (Plan Noviembre v3, sesión 2)
**Fuente del diseño:** `clases-znoviembre/Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` (§3 fila 2, §5 y §10) y `Plan Noviembre - Checklist y traspaso entre sesiones.md` §4
**Flujo:** liviano (Spec → Colab + Solucionario + Guía Docente Voz → gate; sin Ejercicios.ipynb, sin Ticket por Form, sin PPT). HTML interactivo: **se decide después de ver el Colab terminado.**

## Contexto

- **Curso:** 3ro medio · **Duración:** 80 min · **Fecha:** mar 3-nov-2026
- **Modalidad:** individual como piso (no se menciona en ningún material; la anuncia Diego en vivo)
- **Plataforma:** Google Colab. **Entrega:** ninguna; práctica y ticket **autorrevisados** (`check_*()`), Diego no recolecta resultados
- **Contenidos previos asumidos:** Python hasta listas (sin pandas). De la N°41: variables, etiqueta, entrenar ≠ predecir, la prueba se guarda aparte. **Quien faltó a la N°41 parte igual:** el Colab trae recapitulación y datos propios.
- **Contenidos nuevos:** `DecisionTreeClassifier`, `fit()` (entrenar), `predict()` (predecir) y lectura del árbol con `export_text`; entradas y etiquetas en **listas**. **No** se calcula `accuracy` (llega en N°44) y **no** se separa entrenamiento/prueba en código todavía.
- **Historia continua (toda la clase):** **la micro a Santiago.** Vecinas y vecinos de La Islita quieren saber si la micro de las 7:00 llegará atrasada, para decidir si salen antes o toman colectivo. Datos ficticios. *Decisión de Diego (2026-11-03): reemplaza al riego de la viña en esta clase.*
- **Voz:** ChatGPT Voice como codocente, operada solo por Diego (ver «Guion de la voz»)

## Objetivo

Entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico.

*Verbos Bloom: entrenar y predecir (aplicar). El pensamiento crítico es la actitud, no un verbo del objetivo.*

**OAs:** OA1, OA6 | OAk (a confirmar contra `OAs-referencia.md` en el gate)

**Actitud: Pensamiento crítico** (elegida por Diego, 2026-11-03; se retoma en el cierre).

## ¿Por qué lo veremos?

Cuando una app nos dice «tu micro llegará atrasada», alguien la entrenó con datos de días anteriores, y saber cómo se hace nos permite revisar si su respuesta tiene sentido. Hoy entrenamos un primer modelo con los datos de la micro de La Islita y lo usamos con días nuevos.

## Dataset de la clase (escrito en el Colab, sin archivos)

Variables por fila: `lluvia_mm` (lluvia de la madrugada) · `km_taco` (km de taco en la Ruta 78 a las 6:45) · `pasajeros` (personas esperando en el paradero). Etiqueta: `1` = la micro llegó **atrasada**, `0` = llegó **puntual**.

```python
entradas = [[0, 1, 10], [0, 2, 25], [1, 0, 15], [0, 3, 30], [2, 1, 20], [0, 0, 8],
            [12, 6, 22], [15, 8, 30], [8, 7, 12], [20, 9, 18], [10, 2, 28], [18, 5, 9],
            [3, 8, 14], [0, 9, 26], [6, 1, 35], [14, 3, 20]]
etiquetas = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
```

Con `DecisionTreeClassifier(max_depth=3, random_state=0)` (verificado con scikit-learn 1.9.1) el árbol queda **estable** así:

```
|--- km_taco <= 4.00
|   |--- lluvia_mm <= 8.00 → puntual (0)
|   |--- lluvia_mm >  8.00 → atrasada (1)
|--- km_taco >  4.00 → atrasada (1)
```

**Hallazgos útiles para el pensamiento crítico (a usar en la clase):**
- El árbol **ignoró `pasajeros`**: ¿porque no importa, o porque en los datos no se nota? (la voz y el curso lo discuten).
- El umbral de **8 mm** cae en un hueco: no hay filas entre 6 y 8 mm con taco bajo, así que un día de 7 mm se predice «puntual» sin que el modelo haya visto algo parecido.
- Casos nuevos de la clase (con su predicción verificada): `[0, 2, 12]` → puntual · `[16, 6, 20]` → atrasada · `[7, 4, 15]` → puntual · `[1, 8, 22]` → atrasada · `[5, 1, 40]` → puntual (ignora los 40 pasajeros).

## Mapa de tiempos (80 min)

| Bloque | Min | Quién lidera |
|---|---|---|
| 1. Bienvenida | 5 | Voz |
| 2. Haz Ahora (la voz como cliente) | 10 | Voz plantea, Diego modera |
| 3. Recapitulación N°41 | 3 | Diego (en el Colab) |
| 4. ICN «Escríbelo tú» (4 conceptos) | 25 | Diego explica + curso escribe · voz verifica (3) |
| 5. Práctica guiada | 12 | Curso, con Diego |
| 6. Práctica independiente | 15 | Curso, con `check_*()` |
| 7. Ticket de salida (en el Colab) | 5 | Cada estudiante, en silencio |
| 8. Cierre | 5 | Diego (a viva voz) |

## Estructura de la clase

### 1. Bienvenida (5 min)
La voz saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo (aparece en el Colab). Luego Diego toma la clase.

### 2. Haz Ahora (10 min) — la voz como cliente, sin código
La voz hace de **dirigente de la junta de vecinos de La Islita** y le pide al curso un sistema que le avise si la micro de las 7:00 llegará atrasada. Diego da la palabra al curso. Preguntas cerradas, una por una, con celda de texto en el Colab (opcional, sin revisión):

1. ¿Qué cosas del día antes de las 7:00 podrían influir en que la micro se atrase?
2. De esas, ¿cuáles podríamos medir con un número?
3. ¿Qué dato tendríamos que anotar cada día para saber si la micro sí se atrasó?
4. ¿Cuántos días de datos pediríamos, más o menos, antes de confiar en el sistema?

*Conexión con la Práctica Guiada (regla 9):* ambos comparten el escenario de la micro; el Haz Ahora lo plantea sin código y la Guiada lo baja a código con otra pregunta.

### 3. Recapitulación N°41 (3 min)
En el Colab: variables = lo que el modelo recibe; etiqueta = lo que queremos que prediga; entrenar es aprender de ejemplos y predecir es usar lo aprendido en un caso nuevo. Una tabla con las 3 variables y la etiqueta de la micro (sin código).

### 4. ICN «Escríbelo tú» (25 min)

Los datos (`entradas`, `etiquetas`) ya vienen escritos en la primera celda de código. Cada concepto trae **Idea clave** («qué anoto en el cuaderno»), **Instrucción**, **Punto de partida** (código incompleto) y **Resumen tabla**. El `Ejemplo` completo de cada concepto es autocontenido y va en el Solucionario.

| # | Concepto | Idea clave | Instrucción («Escríbelo tú») | Punto de partida |
|---|---|---|---|---|
| 1 | **Crear el modelo** | El modelo es un árbol de preguntas sí/no; al crearlo todavía no sabe nada. | Importa `DecisionTreeClassifier` y crea el modelo con `max_depth=3` y `random_state=0` en una variable llamada `modelo`. | `entradas` y `etiquetas` ya escritas |
| 2 | **`fit()` = entrenar** | `modelo.fit(entradas, etiquetas)` es entrenar: el árbol busca las preguntas que mejor separan los días atrasados de los puntuales. | Entrena el modelo con las entradas y las etiquetas. | `modelo` creado en el concepto 1 (autocontenido en el Solucionario) |
| 3 | **`predict()` = predecir** | `modelo.predict([[...]])` es predecir: recibe una lista con los datos de un día **nuevo** y devuelve 1 (atrasada) o 0 (puntual). | Pregunta al modelo por un día con 0 mm de lluvia, 2 km de taco y 12 pasajeros, y muestra el resultado con una etiqueta clara. | modelo entrenado + `dia_nuevo` sin la línea que predice |
| 4 | **Leer el árbol** | `export_text` muestra las preguntas que el árbol encontró: es el **patrón** que descubrió solo. | Muestra el árbol con `export_text`, indicando los nombres de las variables. | modelo entrenado + `nombres_variables = ["lluvia_mm", "km_taco", "pasajeros"]` |

**Momentos de la voz dentro del ICN:**
- **Humano vs. voz vs. modelo (tras el concepto 3):** el curso predice a ojo para `[7, 4, 15]`, la voz predice, y recién después se corre `predict()`; se comparan los tres.
- **Explicar un error (tras el concepto 4):** con el árbol a la vista, la voz explica por qué predijo «puntual» el día de `[5, 1, 40]` (40 pasajeros) y el curso **juzga si la explicación cuadra con el árbol**.
- **Verificación (3 min, tras el concepto 4):** la voz pregunta a dos estudiantes qué diferencia hay entre `fit()` y `predict()` y por qué el árbol ignoró `pasajeros`.

**Errores típicos a evitar:** pasar un solo día como lista simple (`[0, 2, 12]` en vez de `[[0, 2, 12]]`); llamar `predict()` antes de `fit()`; invertir el orden `fit(etiquetas, entradas)`; creer que el modelo «sabe» algo que no está en los datos.

### 5. Práctica guiada (12 min)
Mismo escenario, pregunta nueva, un solo ejercicio guiado (nivel del Ejercicio 3, regla 20). *Narrativa:* la junta de vecinos agregó 8 días nuevos de la **micro de las 18:30 que vuelve de Santiago**, con las variables `lluvia_mm`, `km_taco` (de Autopista del Sol al regreso) y `minutos_espera`. Tienen que entrenar un modelo con esos datos, predecir **3 días nuevos** y decir con una frase si cada predicción cuadra con lo que vieron en los datos. Formato canónico (narrativa + «El programa debe:» + 1-2 pistas + resultado esperado con ícono + `<em>` + `<pre>` + celda `# Tu programa`). El dataset de este ejercicio va escrito en la celda.

### 6. Práctica independiente (15 min)
Todos con **pistas 1-2** y **`check_*()`** en los ejercicios clave (✅/⚠️ + pista, sin mostrar la solución). Cada ejercicio trae su dataset escrito. Contexto continuo de la micro, con un sector o situación distinta en cada uno (regla de contextos variados, dentro de la historia):

| Ejercicio | Escenario | Qué entrena | Qué se pide |
|---|---|---|---|
| **0a** (calentamiento directo, sin narrativa ni pistas) | Consigna pelada | Árbol con lista de entradas/etiquetas dadas | «Crea un árbol de decisión con `max_depth=2`, entrénalo y predice un caso nuevo; guarda la predicción en una variable e imprímela con etiqueta.» |
| **1** | Naltagua: ¿conviene tomar el colectivo en vez de la micro? | variables: lluvia, km_taco, minutos_espera | Entrenar, predecir 2 días nuevos, `check_ej1()` |
| **2** | Liceo Mario Bertero: ¿llegará el furgón de las 7:30 antes del timbre de las 8:00? | variables propias del furgón | Entrenar, predecir 2 días nuevos, `check_ej2()` |
| **3** (más contextualizado) | Feria / Casona del Maipo: ¿una vecina que vende en la feria llegará a tiempo al montar su puesto? (se suma una variable tomada de otra) | | Entrenar, predecir 3 días nuevos, **modificar una entrada** (p. ej. subir la lluvia) y **explicar por escrito** qué cambió y por qué; `check_ej3()` |
| **4** (desafío opcional) | Mismo escenario del Ej. 3 | | Cambiar `max_depth` (1 vs 3) y comparar los dos árboles con `export_text`; decir cuál sería más fácil de revisar |

> Presupuesto de palabras: 60-90 por ejercicio (Ejercicio 3 y desafío pueden exceder). Si el tiempo apremia, el Ejercicio 3 y el 4 quedan como tarea.

### 7. Ticket de salida (5 min) — en el Colab, autorrevisado
**4 preguntas de alternativas (A–D)**, con bloque de código breve, que se autocorrigen con `check_ticket()` (✅/⚠️ + explicación, sin nota, sin exportación). **Reparto de respuestas correctas: C, A, D, B** (nunca todas la misma letra). *Preguntas por definir en el Solucionario; criterios:* predicción de salida directa (no preguntas «truco»); alternativas que representan errores reales de comprensión. Esquema:

1. **(`fit` vs. `predict`)** Código con `modelo.fit(...)` seguido de `modelo.predict(...)`: ¿qué hace cada línea?
2. **(Forma de la entrada)** ¿Qué falla al llamar `modelo.predict([0, 2, 12])` en vez de `[[0, 2, 12]]`?
3. **(Leer el árbol)** Dado un `export_text` corto, ¿qué predice el árbol para un día concreto?
4. **(Pensamiento crítico)** El árbol predice «puntual» para un día con 40 pasajeros esperando: ¿qué conviene concluir? (que el modelo no usó esa variable y sus datos no tienen días como ese; no que «los pasajeros no importan»).

### 8. Cierre (5 min)
Diego reimprime el objetivo (aparece en el Colab) y hace, **a viva voz**:
- ¿Del 1 al 5, cuánto entendimos el objetivo de hoy?
- ¿Qué parte de las predicciones de hoy revisamos con los datos y cuál habríamos aceptado sin revisar?
- ¿En qué se nos notó hoy el pensamiento crítico? (sin respuesta binaria)
- Anticipo: el jueves construimos una **neurona** para ver cómo decide.

## Guion de la voz (resumen; detalle en `Clase 42 - Primer Clasificador - Guía Docente Voz.md`)

| Momento | Rol de la voz | Frase de activación |
|---|---|---|
| Bienvenida | Saluda, espera respuesta y pide leer el objetivo | «Colega, da la bienvenida al curso.» |
| Haz Ahora | Hace de dirigente de la junta de vecinos de La Islita y plantea las 4 preguntas | «Colega, plantea el diagnóstico.» |
| ICN, concepto 3 | **Humano vs. voz vs. modelo:** predice el día `[7, 4, 15]` cuando Diego lo pida | «Colega, ¿qué predices para este día?» |
| ICN, concepto 4 | **Explica un error** del modelo (día `[5, 1, 40]`) para que el curso lo juzgue | «Colega, explica por qué predijo eso.» |
| ICN (cierre) | Verifica `fit` vs. `predict` y por qué ignoró `pasajeros` | «Colega, verifica comprensión de fit y predict.» |
| Práctica, ticket y cierre | No es protagonista | — |

Entre intervenciones se **silencia el micrófono**. **Plan B:** Diego lee la intervención escrita, o un error de la voz se usa para pensar «¿cómo lo comprobamos con los datos?».

## Colab — `Clase 42 - Primer Clasificador - Clase.ipynb`

1. Encabezado «Clase 42 — Primer clasificador» · curso 3ro medio.
2. 🎯 Objetivo · 🌱 ¿Por qué lo veremos?
3. Requisitos mínimos, cómo ejecutar (de arriba abajo), semillas fijas y datos incluidos (nada de archivos, sin pandas, sin descargas).
4. Haz Ahora (4 celdas de texto).
5. Recapitulación breve de la N°41 (tabla de variables y etiqueta de la micro).
6. ICN: 4 conceptos con Idea clave + «✍️ Escríbelo tú» + celda con punto de partida + Resumen tabla, y la tabla-resumen de cierre (regla 23).
7. Práctica guiada (formato canónico).
8. Práctica independiente (0a + 1 + 2 + 3 + 4 opcional), con `check_*()` definidos en una celda preparada al inicio («no hace falta entenderla»).
9. 🎫 Ticket de salida (celdas con `check_ticket()`; las preguntas viven en el propio Colab, a diferencia de las clases regulares, porque es autorrevisado).
10. Cierre: objetivo reimpreso y preguntas para viva voz (sin celdas de respuesta), + conclusión individual de una frase.
11. **Nada de la modalidad de trabajo, ninguna solución, ninguna respuesta del ticket visible.** Las soluciones de ICN, Guiada, Independiente y Ticket van en `Solucionario.ipynb`.

*Nota técnica:* los `check_*()` validan comportamiento (que el estudiante haya entrenado un modelo, que la predicción sea una lista válida) sin revelar el código solución.

## Decisiones de diseño relevantes

- **Pensamiento crítico (actitud):** elegida por Diego el 2026-11-03. Se aterriza en «explicar un error» y «humano vs. voz vs. modelo», y se retoma en el cierre.
- **Árbol de decisión (`max_depth=3`, `random_state=0`):** no necesita escalar datos, `export_text` muestra el patrón como preguntas legibles y conecta con «regla vs. patrón» de la N°41: la regla la escribe una persona; el árbol descubre una parecida por sí mismo.
- **Historia continua de la micro a Santiago:** decisión de Diego (2026-11-03). Se asume un solo contexto elegido a conciencia; la variedad viene de cambiar el tramo/situación en cada ejercicio (micro de ida, de vuelta, colectivo, furgón del liceo, feria).
- **Datos incluidos en el Colab:** sin archivos ni pandas; el dataset se verificó con scikit-learn 1.9.1 (árbol estable).
- **Sin `accuracy` y sin separar prueba en código:** quedan para N°44; la prueba se menciona solo como recordatorio de la N°41.
- **Sin 4D:** el «revisar si algo es confiable» se trabaja como pensamiento crítico sin nombrar las 4D.
- **Ejemplos genéricos:** la app de la micro es ficticia; no se atribuye la técnica a ningún producto real.

## Pendientes para el gate

- [ ] Confirmar el dataset de la clase (16 filas) y los 5 casos nuevos; confirmar la etiqueta «atrasada = 1».
- [ ] Confirmar los escenarios de la independiente (Naltagua, furgón del liceo, feria/Casona del Maipo).
- [ ] Confirmar el reparto de tiempos (si la independiente se siente corta, pasar el Ej. 3-4 a tarea).
- [ ] Decidir el HTML interactivo **después** de ver el Colab.
- [ ] Confirmar OAs contra `OAs-referencia.md`.
