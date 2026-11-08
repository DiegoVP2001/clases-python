# Clase 42b — De la tabla a las listas

**Estado:** Spec v3 — v2 aprobada por Diego (2026-11-07); **ajustes del 2026-11-08 (v3)** aplicados al Colab, Solucionario, Guía del colega y slides (a la espera del gate 2). Cambios v3: las 3 columnas las fija la clase (el estudiante solo justifica); la etiqueta se define en el Haz Ahora («¿se cayó el wifi?», 1 = sí, 0 = no); se quita el dictado de datos; `max_depth` = «cuánto le dejamos pensar»; el concepto 6 pasa de «Accuracy» a «Revisar» (leer el árbol con las features + accuracy); slides 100 % con el wifi. Cambios de Diego respecto de la v1: columna media vuelve a `temperatura_sala`; el **tipeo completo** de las listas ocurre en el ICN; la **Práctica guiada es el ejercicio obligatorio** y el resto son extras; nuevo objetivo; la tabla no marca el test y va precedida de un diagrama del 80/20; OAs confirmados.
**Clase Picuino:** N/A — fila de IA (calendario v5)
**Fuente del diseño:** entrevista del 2026-11-07 y plan `C:\Users\diego\.claude\plans\necsito-hacer-una-o-vast-mochi.md`; reglas en `disenar-clase/SKILL.md` («Reglas vigentes desde 2026-11-07»).
**Flujo:** liviano (Spec → gate → Colab + Solucionario + Guía Docente Voz + slides animadas → gate → push). Sin PPT, sin `Ejercicios.ipynb`, sin Ticket por Form.

## Contexto

- **Curso:** 3ro medio · **Duración:** 80 min · **Fecha:** lun 9-nov-2026
- **Modalidad:** individual como piso (no se menciona en ningún material; la anuncia Diego en vivo)
- **Plataforma:** Google Colab. **Entrega:** ninguna; práctica y ticket **autorrevisados** (`check_*()`)
- **Contenidos previos:** Python hasta listas; de la N°42: `DecisionTreeClassifier`, `fit()`, `predict()`, `export_text`. **Quien faltó a la N°42 parte igual:** el Colab trae recapitulación de la receta.
- **Contenidos nuevos:** pasar una **tabla** a listas (`[dato1, dato2, dato3]` por fila; filas separadas por coma y envueltas en otro corchete), etiquetas **alineadas** con las filas, elegir 3 de 6 columnas con criterio, **train/test (80 % y 20 %: 16 y 4 filas)** y `accuracy_score`. **No** hay índices anidados, `for`/`append` para armar filas ni *slicing*: todo se tipea a mano, enfoque intuitivo.
- **Historia continua (toda la clase):** **el wifi del liceo.** El encargado de informática quiere saber si la red se cae durante una fila de clases. Datos ficticios. *Decisión de Diego (2026-11-07): reemplaza a la micro de la N°42.*
- **Colega del profesor** (ChatGPT Voice operada solo por Diego; así se nombra en todo material de estudiantes).

## Objetivo

Convertir una tabla de datos en listas de entradas y etiquetas para entrenar y evaluar un modelo con atención.

*Verbos Bloom: convertir, entrenar y evaluar (aplicar). «Con atención» va en el objetivo por decisión de Diego (como el asombro en la N°43).*

**OAs:** OA1, OA3 (confirmados por Diego, 2026-11-07)

**Actitud: Atención** (elegida por Diego, 2026-11-07; se retoma en el cierre). Se aterriza en que cada dato queda en su posición y en que cada etiqueta corresponde a su fila.

## ¿Por qué lo veremos?

Antes de que un modelo aprenda algo, alguien tiene que ordenar los datos para dárselos, y un dato en el lugar equivocado le enseña algo falso sin que nadie lo note. Hoy ordenamos los registros del wifi del liceo y medimos qué tan bien predice la red.

## Datos de la clase

Columnas: **claras** `dispositivos_conectados`, `estudiantes_viendo_video`, `horas_desde_reinicio` · **medias** `temperatura_sala`, `hora_del_bloque` · **sin relación** `dia_del_mes`. Etiqueta `cae`: `1` = el wifi se cayó, `0` = aguantó. Archivo: `datos_wifi_verificados.json` (semilla 16393).

**Diagrama del 80 / 20 (va en el Colab justo antes de la tabla; imagen en `diagramas/split_80_20.png`).** Una barra horizontal de 20 casillas numeradas del 1 al 20:

```
 ┌───────────────────────────────────────────────────────┬───────────────┐
 │ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16        │ 17 18 19 20   │
 │ ← las primeras 16 filas (80 %) →                     │ ← los últimos │
 │ 🧠 la computadora APRENDE con estos                    │ 4 (20 %) →    │
 │                                                        │ 📝 los guardamos│
 │                                                        │ para PROBARLA │
 └───────────────────────────────────────────────────────┴───────────────┘
```

Debajo, una frase corta: «De 20 filas anotados, aprende con 16 y se prueba con 4 que no vio.» (Mismo diagrama en las slides.) La tabla que sigue **no marca** cuáles filas son de qué grupo: el corte lo dice el diagrama y lo aplican los estudiantes al tipear.

| # | dispositivos | video | horas reinicio | temperatura | fila | día | cae |
|---|---|---|---|---|---|---|---|
| 1 | 71 | 0 | 20 | 24 | 8 | 7 | 1 |
| 2 | 62 | 2 | 12 | 29 | 6 | 23 | 0 |
| 3 | 79 | 2 | 2 | 23 | 1 | 23 | 0 |
| 4 | 73 | 0 | 15 | 19 | 7 | 20 | 0 |
| 5 | 102 | 9 | 22 | 18 | 6 | 4 | 1 |
| 6 | 103 | 20 | 1 | 23 | 6 | 31 | 1 |
| 7 | 101 | 17 | 12 | 26 | 5 | 29 | 1 |
| 8 | 59 | 22 | 23 | 30 | 3 | 6 | 1 |
| 9 | 77 | 7 | 22 | 24 | 4 | 4 | 1 |
| 10 | 50 | 0 | 14 | 30 | 4 | 27 | 0 |
| 11 | 76 | 0 | 14 | 26 | 6 | 28 | 0 |
| 12 | 69 | 0 | 7 | 24 | 5 | 18 | 0 |
| 13 | 59 | 0 | 19 | 33 | 7 | 21 | 0 |
| 14 | 115 | 28 | 22 | 20 | 4 | 26 | 1 |
| 15 | 47 | 2 | 2 | 19 | 6 | 21 | 0 |
| 16 | 78 | 0 | 16 | 29 | 3 | 31 | 1 |
| 17 | 51 | 0 | 16 | 22 | 5 | 3 | 0 |
| 18 | 117 | 0 | 16 | 30 | 4 | 5 | 1 |
| 19 | 75 | 22 | 2 | 18 | 8 | 24 | 1 |
| 20 | 66 | 0 | 9 | 27 | 6 | 5 | 0 |

**Verificado con scikit-learn 1.9** (`DecisionTreeClassifier(max_depth=3, random_state=0)`; aprende con las filas 1-16 y se prueba con las filas 17-20):

| Trío | Aciertos en test (de 4) | Validación cruzada |
|---|---|---|
| **Sensato** (dispositivos, video, horas reinicio) | **4** | **0,90** (el mejor de los 20 tríos) |
| dispositivos, video, temperatura | 4 | 0,70 |
| dispositivos, video, día del mes (con la columna sin relación) | 2 | 0,80 |
| dispositivos, temperatura, día del mes | 1 | 0,55 |
| temperatura, hora del bloque, día del mes (los tres «flojos») | 1 | 0,55 |

El árbol con las **6 columnas** usa solo las tres claras (importancias: dispositivos 0,17 · video 0,60 · horas 0,23). Con el trío sensato queda: `video <= 4,5` → (`horas <= 15,5` → 0, si no `dispositivos <= 65` → 0, si no 1), si no 1.

**Lectura honesta para la clase (cierre y Prueba 1):** con solo 4 días de test, un trío con una columna floja puede sacar 4/4 igual que el sensato (dispositivos, video, temperatura); lo que lo delata es la validación cruzada, que no se enseña. El mensaje es que **4 días prueban poco**: acertar 4 de 4 no basta para confiar, y cambiar una columna clara por una floja suele empeorar el resultado.

## Mapa de tiempos (80 min)

| Fila | Min | Quién lidera |
|---|---|---|
| 1. Bienvenida | 5 | Colega |
| 2. Haz Ahora (el colega como encargado de informática) | 8 | Colega plantea, Diego modera |
| 3. Recordatorio puente (ayer → hoy → mañana) | 3 | Diego |
| 4. ICN «Escríbelo tú» **con el tipeo completo** de las listas (6 conceptos) | 34 | Diego + curso · colega verifica (1) |
| 5. Práctica guiada = **el ejercicio obligatorio** (12 trabajo + 8 revisión en vivo con una pareja que explica) | 20 | Curso, con Diego |
| 6. Ticket de salida (PPT + Google Form) | 5 | Cada estudiante, en silencio |
| 7. Cierre | 5 | Diego (a viva voz) |

> **Ejercicios extra (0a, 0b, 1, 2, 3, 4):** no tienen fila de tiempo; quedan en el Colab como tarea u opcionales. Por decisión de Diego, el ICN se mezcla con la guiada y la guiada reemplaza a la independiente: se prefiere revisar bien un ejercicio y pasar al ticket y al cierre.

## Estructura de la clase

### 1. Bienvenida (5 min)
El colega saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo (aparece en el Colab). Luego Diego toma la clase.

### 2. Haz Ahora (8 min) — el colega como encargado de informática, sin código
El colega hace de **encargado de informática del liceo**: registró varios datos en una tabla, donde las distintas columnas son (se listan las 6 con lo que mide cada una), y no sabe cuáles le podrían servir para resolver el problema. Preguntas cerradas, una por una, con celda de texto (opcional, sin revisión). *(v3, redacción de Diego 2026-11-08)*

1. Mirando los nombres de las 6 columnas, ¿cuáles 3 creen que más ayudan a saber si el wifi se cae?
2. ¿Cuáles son las 3 que descartaron y por qué?
3. Al final de cada registro, el encargado tiene otra columna que se llama **«¿Se cayó el wifi?»**. ¿Cómo representarían esa respuesta con una **etiqueta** binaria, en código? → **1 = sí, 0 = no** (el 1 es «sí», no «bueno»).
4. Si el cuaderno tiene **20 filas de datos**, ¿cuántas filas de datos dejarían para entrenar el modelo y cuántas para probarlo (testearlo)? (prepara el 80 / 20)

Tras el Haz Ahora, Diego **fija las 3 columnas de la clase** y las compara con lo que propuso el curso.

*Terminología (regla desde 2026-11-08): se dice **filas** o **filas de datos**, nunca «bloques».* El nombre de columna `hora_del_bloque` se mantiene porque es un dato de la tabla.

*Conexión con la Práctica guiada (regla 9):* comparten el escenario del wifi (la guiada usa el liceo vecino) y el Haz Ahora lo plantea sin código.

### 3. Recordatorio puente (3 min) — con la tabla Ayer / Hoy / Mañana
**🔁 Ayer:** el árbol encontró solo las preguntas que separan los días atrasados de los puntuales; los datos ya venían escritos. **🔀 Hoy:** nosotros los escribimos: de la tabla del cuaderno a las listas que recibe el modelo, y probamos qué tan bien aprendió. **➡️ Mañana:** la misma receta con otro modelo, una neurona.

### 4. ICN «Escríbelo tú» (34 min) — con el tipeo completo

Primero el diagrama del 80 / 20 y después la tabla completa de 20 filas en markdown (sin marcar el test). Cada concepto trae **Idea clave** («qué anoto en el cuaderno»), **Instrucción**, **Punto de partida** y **Resumen tabla**; el `Ejemplo` completo (autocontenido) va en el Solucionario. **Estimación de tipeo: 6-8 min en total** (20 filas × 3 columnas + 20 etiquetas, copiando de la tabla).

| # | Concepto | Idea clave | Instrucción | Punto de partida |
|---|---|---|---|---|
| 1 | **Elegir las 3 columnas** *(v3: sin «Escríbelo tú»)* | El modelo no necesita todas las columnas: usamos las que podrían explicar la etiqueta y dejamos fuera las que no, y lo justificamos (ahorra procesamiento: menos que anotar y escribir, menos ruido, y en bases enormes menos cómputo; aquí casi no se nota). | Se muestran en markdown las **3 columnas elegidas** (`dispositivos_conectados`, `estudiantes_viendo_video`, `horas_desde_reinicio`), qué mide cada una y la **tabla reducida de 20 filas** (de ahí copian). El estudiante escribe una **breve justificación** (celda de texto): por qué esas 3 sí y las otras 3 no. | Tabla reducida |
| 2 | **Una fila es una lista** | Una fila se escribe `[dato1, dato2, dato3]`: cada coma separa una columna y el **orden** es siempre el mismo. | Escribe la **fila 2** como lista con las 3 columnas, en ese orden, en `fila_2` (el ejemplo del texto es la fila 1: `[71, 0, 20]`). | `fila_2 = [ ]` |
| 3 | **La tabla: filas separadas por coma, dentro de otro corchete** | Las filas se separan con comas y se envuelven en otro corchete; las etiquetas (1 = sí, 0 = no) van en otra lista, en el mismo orden. | Completa `entradas_train` (filas 1 a 16) y `etiquetas_train`. | filas 1 y 2 ya escritos |
| 4 | **Los 4 filas que guardamos para probar** | Con el 80 % la computadora aprende (train); el 20 % se guarda para probarla (test). | Escribe `entradas_test` y `etiquetas_test` (filas 17 a 20). | listas vacías |
| 5 | **La receta: crear → fit → predict** | `max_depth` = cuánto le dejamos «pensar» al árbol: mientras menos, mejor, siempre que los resultados no cambien (menos procesamiento). `random_state=0` = semilla para que a todos nos resulte el mismo árbol. | Entrena con train y guarda en `predicciones` lo que predice para `entradas_test`. | modelo creado. **Después del código, un `<details>` oculto: «¿Cómo cambian los resultados si variamos `max_depth`?»** |
| 6 | **Revisar** | *(bullets al grano)* «Al revisar hacemos dos cosas»: 1. **leer el árbol** (`export_text(modelo, feature_names=nombres_variables)`; los nombres son las *features*, en el mismo orden que las listas) y 2. **ver la precisión** (`accuracy_score(etiquetas_test, predicciones)`: aciertos ÷ total). | Escribe `nombres_variables` y muestra el árbol; luego calcula el accuracy en `exactitud` y muéstralo con una etiqueta. | imports de `export_text` y `accuracy_score` |

**`max_depth` (v3):** el texto del Colab solo dice que es cuánto le dejamos «pensar» (mientras menos, mejor si los resultados no cambian) y explica `random_state=0`. **Se quitaron la tabla y la justificación de usar 3**; van **después del código, en un desplegable oculto** «¿Cómo cambian los resultados si variamos `max_depth`?»: con 1 o 2 el árbol aún se equivoca en el entrenamiento (2 y 1 de 16 filas); con 3 acierta todas; con 4 o más queda igual que con 3. Verificado con los datos de la clase. La slide 7 lo muestra con botones.

Sin caja preparada: todas las listas se tipean en el ICN (decisión de Diego). *(v3)* El trío **lo fija la clase**, así que `check_icn()` valida listas en el orden dispositivos-video-horas, `nombres_variables` y `exactitud`.

**Momentos del colega dentro del ICN:**
- *(v3: se quitó el dictado de datos.)*
- **Verificación (2 min, tras el concepto 6):** a dos estudiantes: ¿para qué guardamos 4 filas aparte? ¿qué cambia si una etiqueta queda en otra posición?

**Errores típicos a evitar:** cambiar el orden de las columnas entre una fila y otra; omitir una etiqueta (largos distintos: `fit` falla); `predict([0, 2, 12])` en vez de `[[...]]`; mirar el test mientras se elige el modelo; creer que 4 de 4 prueba que el modelo es bueno.

### 5. Práctica guiada = ejercicio obligatorio (20 min: 12 de trabajo + 8 de revisión)
Mismo escenario, pregunta nueva, **un solo ejercicio** (nivel del Ejercicio 3, regla 20), que todos hacen sí o sí. *Narrativa:* el liceo vecino anotó **10 filas** en una tabla de 5 columnas (`computadores_en_uso`, `estudiantes_viendo_video`, `horas_desde_reinicio`, `ancho_de_banda_contratado`, `dia_del_mes`) y el encargado pide trabajar con tres: los tres primeros. El estudiante **tipea las listas del 80 % (8 filas) y del 20 % (2 filas)**, entrena, predice, calcula el accuracy y dice en una frase si cuadra con lo que vio. Formato canónico (narrativa + «El programa debe:» + 1-2 pistas + resultado esperado con ícono + `<em>` + `<pre>` + celda `# Tu programa`). **Revisión (regla 18):** Diego trae a una pareja a explicar la guiada al frente. *(Datos del liceo vecino: por definir y verificar al generar el Colab.)*

### 6. Ejercicios extra (sin tiempo asignado; tarea u opcionales)
Todos con **pistas 1-2** y **`check_*()`** en los clave (✅/⚠️ + pista, sin mostrar la solución). La historia sigue en el liceo:

| Ejercicio | Escenario | Qué se pide |
|---|---|---|
| **0a** (directo, sin narrativa ni pistas) | Consigna pelada | «Escribe una lista con las 3 filas de esta tabla y otra con sus 3 etiquetas, en el mismo orden.» |
| **0b** (directo) | Consigna pelada | «Pregunta al modelo ya entrenado por un único fila nueva; guarda la predicción en una variable e imprímela con etiqueta.» (hace que usen `[[...]]`) |
| **1** | Biblioteca del liceo: ¿se cae la red en el fila de estudio? | Tabla de 10 filas × 4 columnas; el encargado pide 3; tipear el 80 % y el 20 %; `check_ej1()` |
| **2** | Sala de computación: encontrar la **etiqueta desalineada** | Listas ya tipeadas con una etiqueta omitida: detectar por qué falla y corregir; `check_ej2()` |
| **3** | Evento del liceo (sala de actos): 6 columnas | Tabla de 10 filas × 6 columnas; elegir 3 con criterio, tipear, calcular accuracy y compararlo con el de un trío «del compañero» ya escrito; explicar por escrito cuál conviene y por qué (con 2 filas de test, una diferencia pequeña prueba poco); `check_ej3()` |
| **4** (desafío opcional) | Mismo escenario del Ej. 3 | Cambiar un dato de test y ver si la conclusión cambia |

### 7. Ticket de salida (5 min) — Google Form + PPT *(v3, 2026-11-08)*
El Colab **termina con el link al formulario** (`https://forms.gle/sjRpbgmQzrpkEBsH9`) y el tema a escribir («De la tabla a las listas»); **no trae las preguntas**. Diego las proyecta desde `Ticket de Salida.pptx` (10 slides: portada, 4 preguntas, formulario, 4 revisiones; solo local hasta dictar la clase). **4 preguntas de alternativas (A–D)** con bloque de código breve. **Respuestas correctas: D, B, C, A** (también en `Ticket de Salida Respuestas.json` y en el Solucionario). Esquema:

1. **(Forma de la tabla)** ¿cuál de estas opciones escribe correctamente la tabla de 3 filas con 3 columnas?
2. **(Alineación)** dadas `entradas` y `etiquetas` de 4 filas, ¿qué etiqueta le corresponde a la fila 3?
3. **(`predict`)** ¿cómo se pregunta por una sola fila nueva: `predict([88, 17, 4])` o `[[88, 17, 4]]`?
4. **(Pensar sobre el test)** un modelo acierta 4 de 4 en el test: ¿qué se concluye? (que acertó esas 4 filas; con tan pocas no alcanza para confiar).

### 8. Cierre (5 min)
Diego reimprime el objetivo (en el Colab) y hace, **a viva voz**:
- ¿Del 1 al 5, cuánto entendimos el objetivo de hoy?
- ¿En qué momento de hoy tuvimos que **poner atención** para no cambiar un dato de lugar? (sin respuesta binaria)
- ¿Qué parte del orden de los datos revisamos con cuidado y cuál habríamos dejado pasar?
- Anticipo: **mañana usamos la misma receta con otro modelo: una neurona.**

## Guion del colega (detalle en `Clase 42b - De la Tabla a las Listas - Guía Docente Voz.md`)

| Momento | Rol del colega | Frase de activación |
|---|---|---|
| Bienvenida | Saluda, espera respuesta y pide leer el objetivo | «Colega, da la bienvenida al curso.» |
| Haz Ahora | Hace de encargado de informática y plantea las 4 preguntas | «Colega, plantea el diagnóstico.» |
| ICN (cierre) | Verifica comprensión (el 20 % guardado; etiqueta mal ubicada) | «Colega, verifica comprensión de las listas.» |
| En cualquier momento | Preguntas abiertas de los estudiantes, sin inventar | «Colega, responde la pregunta de…» |
| Guiada, ticket y cierre | No es protagonista | — |

Entre intervenciones se **silencia el micrófono**. **Plan B:** Diego lee la intervención escrita; un error del colega se usa para pensar «¿cómo lo comprobamos con la tabla?».

## Slides animadas — `sitio-hub/clase-42b/` (pestañas Clase 41 · 42 · 42b · 43 · Inicio)

*(v3: 11 slides, todas con el wifi del liceo y las 3 columnas elegidas; sin el ejemplo del básquetbol.)*
- **Inicio:** 1 la pregunta y la etiqueta (¿se cayó el wifi? 1 = sí, 0 = no) · 2 de 6 columnas a 3 (las descartadas se apagan, con la justificación y el ahorro de procesamiento).
- **Durante:** 3 una fila es una lista (con «cambiar dos datos de lugar») · 4 varias filas forman la tabla, con las etiquetas alineadas · 5 el 80 / 20 animado · 6 `predict` con doble corchete · 7 la receta y `max_depth` con botones 1 a 4.
- **Después:** 8 revisar (1): leer el árbol con las features y seguir el camino de la fila 17 · 9 revisar (2): accuracy fila por fila · 10 «4 de 4 prueba poco» · 11 resumen.

## Colab — `Clase 42b - De la Tabla a las Listas - Clase.ipynb`

1. Encabezado «Clase 42b — De la tabla a las listas» · 3ro medio · 2. 🎯 Objetivo · 🔎 ¿Por qué lo veremos? · 3. requisitos mínimos, cómo ejecutar, semillas y recapitulación de la N°42 · 4. Haz Ahora (4 celdas de texto) · 5. 🔁 Ayer → 🔀 Hoy → ➡️ Mañana · 6. ICN: **diagrama del 80 / 20, tabla de 20 filas en markdown sin marcar el test**, 6 conceptos con Idea clave, «✍️ Escríbelo tú», punto de partida y tabla-resumen de cierre · 7. Práctica guiada (el ejercicio obligatorio) · 8. 🎫 Ticket · 9. Cierre · 10. **Ejercicios extra** (0a, 0b, 1, 2, 3, 4) con `check_*()` en una celda preparada («no hace falta entenderla»).
11. **Nada de modalidad de trabajo, ninguna solución, ninguna respuesta del ticket visible.** Soluciones en `Solucionario.ipynb`.

## Decisiones de diseño relevantes

- **Listas a mano, sin índices:** la escala (20 filas) permite tipearlas; lo que se enseña es la **estructura** y la **alineación**, no la automatización.
- **80 / 20 desde el inicio, con diagrama:** formaliza el «esto debería dar 1/0» de la N°42; el corte se enseña con una imagen simple y no marcando filas en la tabla.
- **Tipeo completo en el ICN; guiada = ejercicio obligatorio; el resto extra** (Diego, 2026-11-07): se prefiere revisar bien un ejercicio y llegar al ticket y al cierre.
- **Elegir columnas con criterio** (3 claras, 2 medias, 1 sin relación) y mensaje honesto de que 4 días de test prueban poco.
- **Sin 4D, sin ponderar, sin if/else del árbol.**
- **Ejemplos genéricos:** el wifi es ficticio; no se atribuye la técnica a ningún sistema real.

## Pendientes para el gate

- [x] Columna media: `temperatura_sala` (Diego, 2026-11-07).
- [x] OAs: OA1, OA3 (Diego, 2026-11-07).
- [ ] Confirmar el dataset de 20 filas (semilla 16393) y que `dia_del_mes` sea la columna sin relación.
- [ ] Confirmar el mapa de tiempos (ICN 34 min con tipeo completo; guiada 20 min con revisión).
- [ ] Confirmar el diagrama del 80 / 20 (barra de 20 casillas, 16 + 4) y las slides animadas.
- [ ] Datos del liceo vecino (guiada) y de los Ejercicios extra: los verifico al generar el Colab.
