# Clase 41 — Mapa de la IA + pipeline

**Estado:** Spec aprobada — 2026-10-31 (v2; definiciones de IA y ML resumidas; diagramas también en el HTML; el Colab dice «vamos a la actividad X de la página»; códigos por defecto, Diego puede cambiarlos)
**Clase Picuino:** N/A — bloque de IA (Plan Noviembre v3, sesión 1)
**Fuente del diseño:** `clases-znoviembre/Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` (§3 fila 1, §4 y §10)
**Flujo:** liviano (Spec → Colab guía + HTML interactivo + 2 diagramas + PPT paso a paso del pipeline → gate; sin Ejercicios.ipynb, sin Ticket por Form)

## Contexto

- **Curso:** 3ro medio (4to ya egresó; desde noviembre el curso es solo 3ro)
- **Duración:** 80 min · **Fecha:** lun 2-nov-2026
- **Modalidad:** individual como piso (no se menciona en ningún material; la anuncia Diego en vivo)
- **Plataforma:** Google Colab (guía) + HTML interactivo publicado en `clases-ia-mario-bertero.vercel.app`
- **Entrega:** ninguna. Práctica y ticket **autorrevisados**; Diego no recolecta resultados y mira el aprendizaje a ojo
- **Contenidos previos asumidos:** nada de IA. Python hasta listas, sin pandas (esta clase ni siquiera pide código)
- **Contenidos nuevos:** IA, ML, DL e IA generativa; regla y patrón; datos, variables, etiqueta, entrenamiento, prueba, predicción y evaluación (panorámico)
- **Contextos temáticos:** riego de una viña en Isla de Maipo con datos ficticios (hilo de N°41–43), música, spam, imágenes, traducción, generación de texto
- **Voz:** ChatGPT Voice como codocente, operada solo por Diego (ver «Guion de la voz» y la `Guía Docente Voz`)

## Objetivo

Ubicar ejemplos de IA en el mapa (reglas, ML, DL e IA generativa) y ordenar el recorrido de los datos hasta la evaluación de un modelo, con curiosidad.

*Verbos Bloom: ubicar (comprender) y ordenar (aplicar).*

**OAs:** OA1, OA6 | OAk

**Actitud: Curiosidad** (se retoma en el cierre). *Desde el 2026-10-31 las specs no llevan sección «Propósito»: la actitud queda como etiqueta y como pregunta de cierre.*

## ¿Por qué lo veremos?

La IA ya decide cosas a nuestro alrededor —el filtro de spam, las canciones que nos recomiendan, las respuestas de ChatGPT— y saber cómo funciona cada una nos dice cuánto confiar. Además, el recorrido datos → entrenar → evaluar es el que seguiremos todo noviembre para entrenar nuestros propios modelos, empezando por predecir si hay que regar una viña.

## Mapa de tiempos (80 min)

| Bloque | Min | Quién lidera |
|---|---|---|
| 1. Bienvenida | 5 | Voz |
| 2. Haz Ahora (diagnóstico oral) | 10 | Voz plantea, Diego modera |
| 3. Recorrido de noviembre | 8 | Voz presenta, Diego completa |
| 4. ICN 1 · El mapa | 21 | Diego explica con el diagrama (8) · voz verifica (3) · HTML M1–M3 (10) |
| 5. ICN 2 · El pipeline | 21 | Diego explica con el diagrama (8) · voz verifica (3) · HTML P1–P4 (10) |
| 6. Ticket (en el HTML) | 10 | Cada estudiante, en silencio |
| 7. Cierre | 5 | Diego (a viva voz) |

## Dinámica general: del concepto a la actividad, con código de 3 números

El Colab guía **salta de un concepto a su actividad en el HTML** y vuelve: concepto → actividad → concepto → actividad. **Cada actividad del HTML está bloqueada con un código de 3 números** que Diego entrega **justo antes de avanzar**, para que nadie se adelante. El código solo regula el ritmo de la clase, no es seguridad (el archivo es inspeccionable). Los códigos viven como constantes al inicio del HTML (editables) y se listan en la `Guía Docente Voz`.

| Actividad | Qué es | Código (por defecto) |
|---|---|---|
| M1 | Regla o patrón | 417 |
| M2 | Ubica en el mapa | 238 |
| M3 | El caso dudoso | 659 |
| P1 | Ordena el recorrido (se abre con el código de la **página 2**) | 172 |
| P2 | Variables y etiqueta | 884 |
| P3 | Entrenar o predecir | 306 |
| P4 | Caza el error | 591 |
| TK | Ticket de salida (se abre con el código de la **página 3**) | 725 |

Cada actividad trae **pistas** (1–2 por ejercicio, colapsables) y un botón **Comprobar** que responde ✅ o ⚠️ con una pista, sin mostrar la solución; permite reintento. Los códigos son editables y Diego puede cambiarlos antes de la clase.

## Cambios del 2026-10-31 (v3) — prevalecen sobre el resto de la spec

- **Sin sección «Cómo funciona»** en el HTML.
- **El HTML tiene 3 páginas.** Página 1: recorrido, Diagrama 1 y M1–M3 (cada una con su código). **Página 2** (Diagrama 2 + P1–P4): se abre con el código **172**, que abre también P1; P2, P3 y P4 conservan sus códigos. **Página 3** (ticket): se abre con **725**. El paso de M3 a P1 y de P4 al ticket es un cambio de página con contraseña.
- **Diagrama 2 rediseñado:** separa el **set de entrenamiento** («aquí la computadora aprende») del **set de prueba** («aquí vemos si es capaz de predecir», se guarda aparte), con el modelo en medio y la evaluación abajo.
- **Dos ejemplos:** lo que explica Diego (diagramas y PPT) usa el **riego automatizado de una viña de Isla de Maipo, como Santa Ema**; las actividades de la página usan el **sistema de climatización de las bodegas donde fermenta la uva** (¿hay que enfriar el tanque?). Datos ficticios en ambos casos.
- **PPT paso a paso del pipeline** (`Clase 41 - Mapa IA - Presentación.pptx`, 14 diapositivas con notas): un paso por diapositiva, contraste «entrenar no es predecir», error típico y resumen. Solo cubre el pipeline, no el mapa.
- **Terminología:** «set de entrenamiento» y «set de prueba».

## Diagramas para proyectar (y subir)

Dos diagramas resumidos, para **proyectar en la pantalla mientras Diego explica** y para **subir** después a los estudiantes. Se entregan como **imagen PNG 1920×1080** (se incrustan en el Colab guía y quedan descargables en el sitio, `/clase-41/diagramas/`). Fuente en SVG, sin dependencias externas. Contraste alto, tamaño de letra legible desde el fondo de la sala y el significado nunca solo por color.

### Diagrama 1 — El mapa de la IA

Tres círculos anidados (IA ⊃ ML ⊃ DL) y, a un lado, **IA generativa** como categoría definida **por lo que produce**, unida con línea punteada a ML/DL («hoy se construye sobre todo con DL, p. ej. ChatGPT»); **no** se dibuja como cuarto círculo anidado (v2 §4). Texto de cada pieza (resumido):

- **IA:** máquinas que hacen tareas que normalmente requieren inteligencia humana: aprender, razonar y decidir.
- **Machine Learning (ML):** la computadora descubre patrones en los datos y decide sin que le indiquen cómo.
- **Deep Learning (DL):** ML con redes neuronales de muchas capas; sirve para imágenes, voz y texto.
- **IA generativa:** produce contenido nuevo (texto, imágenes, música) a partir de lo que aprendió.

**Fuera del diagrama, en una franja inferior con dos tarjetas** (definiciones cortas y claras):
- **Regla:** instrucción que escribe una persona y que le dice a la máquina qué hacer en cada caso; no cambia sola.
- **Patrón:** algo que se repite en los datos y que la máquina descubre sola mirando muchos ejemplos.

*Las definiciones de IA y ML se resumieron a pedido de Diego (2026-10-31); el Colab usa las mismas versiones cortas que el diagrama. El diagrama también va **dentro del HTML** (en pantalla completa para proyectar), además del PNG.*

### Diagrama 2 — El recorrido de los datos (pipeline)

Una cinta horizontal con los **7 pasos** del caso del riego, agrupados en cuatro bloques con nombre: **Preparar** (1 problema · 2 datos, variables y etiqueta · 3 separar entrenamiento y prueba) → **Entrenar** (4) → **Evaluar** (5 predecir sobre la prueba · 6 evaluar) → **Usar** (7 casos nuevos y revisar). Con dos recuadros de apoyo: *variables = lo que el modelo recibe; etiqueta = lo que queremos que prediga* y *la prueba se guarda aparte*. Un ejemplo mínimo de fila (humedad, temperatura, días sin lluvia → ¿se regó?) bajo el paso 2.

## Estructura de la clase

### 1. Bienvenida (5 min)

La voz saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo (aparece en el Colab guía). Luego Diego toma la clase. No hay contenido ni preguntas en este bloque.

### 2. Haz Ahora (10 min) — diagnóstico oral, sin nota

La voz hace las preguntas, una por una, y Diego da la palabra al curso. Se aceptan respuestas tentativas. Diego anota en la pizarra las ideas y las confusiones para retomarlas en el cierre.

1. ¿Dónde han escuchado hablar de IA?
2. ¿Qué creen que hace una IA?
3. ¿Qué han probado ustedes?
4. ¿Cómo creen que aprende?
5. ¿Qué dudas o riesgos les genera?

**No hay respuestas esperadas**: el bloque mide lo que traen. No se piden relatos personales sensibles y la experiencia previa no cuenta como ventaja.

*En el Colab guía, cada pregunta tiene una celda de texto para anotar la idea propia (opcional, sin revisión).*

### 3. Recorrido de noviembre (8 min)

La voz presenta el bloque (es la última unidad del curso) y Diego completa con lo que ella no sabe: fechas y notas.

- **Ruta:** ubicar la IA → entrenar un clasificador → construir una neurona → entrenar una red y medir aciertos → generar texto → usar ChatGPT → analizar ética → integrar.
- **Qué hace cada uno:** escribe y ejecuta código y explica sus resultados; no basta con ejecutar todo.
- **Evaluaciones:** E1 jue 12-nov · E2 jue 19-nov · E3 jue 26-nov. **Dos notas:** promedio de E1 y E2, y E3 sola.
- **El mar 17-nov no hay clase.**

*En el HTML, este bloque es una sección «Nuestro recorrido» (línea de tiempo simple, sin actividad ni código).*

### 4. ICN 1 · El mapa (21 min)

**Qué explica Diego (8 min), proyectando el Diagrama 1:** primero **regla y patrón** (las dos tarjetas), luego los círculos IA ⊃ ML ⊃ DL con un ejemplo cada uno, y la **IA generativa** por lo que produce; ChatGPT como ejemplo de generación basada en aprendizaje profundo. **No se enseña como ley la cadena IA ⊃ ML ⊃ DL ⊃ generativa.**

**Salto concepto → actividad (colab ↔ HTML):**

| Concepto en el Colab | Actividad en el HTML | Qué hace el estudiante | Pistas |
|---|---|---|---|
| Regla y patrón (tarjetas) | **M1 · Regla o patrón** | Para 6 ejemplos, decide si es **regla** o **patrón** | 2: «¿alguien escribió cada condición?» / «¿cambia si le muestro más datos?» |
| IA, ML, DL, IA generativa (Diagrama 1) | **M2 · El mapa** | Ubica 8 ejemplos (solo regla, ML o DL) y marca **si genera contenido nuevo** | 2: la definición del círculo / un ejemplo ya resuelto |
| *Cuando algo no calza* | **M3 · El caso dudoso** | Lee un caso con dos lecturas posibles y elige **qué información faltaría** | 2: «¿qué recibe?» / «¿qué produce?» |

**Verificación de la voz (3 min):** le pide a dos estudiantes que expliquen con sus palabras la diferencia entre regla y patrón, y resuelve dudas.

**Ejemplos** (descritos como *tipos de sistema*, sin afirmar que un producto concreto use una técnica sin evidencia): un semáforo con temporizador fijo (regla); un filtro que bloquea correos con la palabra «premio» (regla); un sistema que recomienda música según lo que se escucha (ML); un sistema que predice si hay que regar con datos de años anteriores (ML); un desbloqueo por reconocimiento de rostro (DL); un traductor automático (DL); ChatGPT escribiendo un texto (generativa basada en DL); un programa que crea imágenes desde una descripción (generativa). **Caso dudoso:** un corrector de texto del celular (puede ser reglas, ML o ambos: depende de cómo se construyó).

**Interacción:** arrastrar y soltar **y** alternativa por botones/teclado; el significado nunca depende solo del color; reintento en todas las rondas.

### 5. ICN 2 · El pipeline (21 min)

**Qué explica Diego (8 min), proyectando el Diagrama 2:** el recorrido con **un solo caso**: el riego de una viña.

1. Definir el problema (¿hay que regar mañana?, sí/no).
2. Reunir y preparar datos; identificar **variables** (humedad, temperatura, días sin lluvia) y **etiqueta** (¿se regó?).
3. Separar **entrenamiento** y **prueba**.
4. **Entrenar** (el modelo aprende de los datos de entrenamiento).
5. **Predecir** sobre los datos de prueba.
6. **Evaluar** (¿cuántas veces acertó?).
7. Usar en casos nuevos y revisar.

Dos ideas para dejar claras: **entrenar no es predecir**, y **el conjunto de prueba se queda fuera del entrenamiento**. Es una primera vista: la implementación llega en el N°42.

**Idea clave (para el cuaderno):**
- Variables: lo que el modelo recibe. Etiqueta: lo que queremos que prediga.
- Entrenar es aprender de ejemplos; predecir es usar lo aprendido en un caso.
- La prueba se guarda aparte: si evaluamos con lo mismo que entrenamos, no sabemos cómo le irá con casos nuevos.

**Salto concepto → actividad (colab ↔ HTML):**

| Concepto en el Colab | Actividad en el HTML | Qué hace el estudiante | Pistas |
|---|---|---|---|
| Los 7 pasos (Diagrama 2) | **P1 · Ordena el recorrido** | Ordena los 7 pasos (arrastrar o botones subir/bajar) | 2: «¿qué va antes de entrenar?» / «¿cuándo se mide?» |
| Variables y etiqueta | **P2 · Variables y etiqueta** | Marca las columnas de una tabla de riego (variable o etiqueta) | 2: «¿qué sabemos hoy?» / «¿qué queremos saber?» |
| Entrenar vs. predecir | **P3 · Entrenar o predecir** | Clasifica 6 acciones del caso como *entrenar* o *predecir* | 2 |
| La prueba se guarda aparte | **P4 · Caza el error** | Lee un pipeline con una falla (evalúa con los mismos datos con que entrenó) y señala dónde está | 2: «¿con qué datos se evaluó?» / «¿esos datos ya los vio el modelo?» |

**Verificación de la voz (3 min):** pregunta al curso «¿por qué guardamos datos aparte?» y «¿qué diferencia hay entre entrenar y predecir?».

### 6. Ticket de salida (10 min) — dentro del HTML

**Bloqueado con su código de 3 números (TK)**, que Diego entrega al cierre. Cuatro preguntas de alternativas (A–D), retroalimentación explicativa inmediata y reintento. **Formativo: sin nota y sin exportación.** Es autorrevisado y Diego no ve los resultados.

1. **(Mapa)** Un sistema que bloquea correos porque contienen la palabra «premio», con una condición escrita por una persona, es:
   A) Machine Learning · B) Deep Learning · **C) una regla escrita por una persona, que no aprende de datos** · D) IA generativa
2. **(Pipeline)** Un equipo entrena el sistema de climatización de una bodega y lo evalúa con **los mismos registros** con que lo entrenó. ¿Qué problema tiene?
   **A) No sabemos cómo le irá con casos nuevos, porque esos registros ya los vio** · B) Usa pocas variables · C) Debió entrenar después de evaluar · D) No tiene ningún problema
3. **(Pipeline)** En una tabla de climatización con las columnas temperatura del tanque, temperatura de la bodega, horas de fermentación y «¿se activó el enfriamiento?», ¿cuál es la etiqueta?
   A) La temperatura del tanque · **B) La columna «¿se activó el enfriamiento?», porque es lo que queremos que el modelo prediga** · C) Las horas de fermentación · D) Todas las columnas por igual
4. **(Aplicación o duda)** ChatGPT responde con mucha seguridad. ¿Qué conviene hacer?
   A) Aceptarla: si suena segura, es correcta · B) Descartarla siempre · C) Pedirle lo mismo hasta que cambie la respuesta · **D) Revisarla con otra fuente, porque genera texto que suena bien aunque pueda estar equivocado**

**Reparto de respuestas correctas:** C, A, B, D (nunca todas en la misma letra).

### 7. Cierre (5 min)

Diego reimprime el objetivo (aparece en el Colab guía) y hace, **a viva voz**:

- ¿Del 1 al 5, cuánto entendimos el objetivo de hoy?
- Volvemos al diagnóstico: ¿qué idea del principio cambiaría ahora?
- ¿En qué se nos nota hoy la curiosidad? (anclaje de la actitud, sin respuesta binaria)
- Anticipo: mañana entrenamos nuestro primer clasificador.

## Guion de la voz (resumen; el detalle va en `Clase 41 - Mapa IA - Guía Docente Voz.md`)

| Momento | Rol de la voz | Frase de activación |
|---|---|---|
| Bienvenida | Saluda, espera respuesta del curso y pide que alguien lea el objetivo | «Colega, da la bienvenida al curso.» |
| Haz Ahora | Plantea las 5 preguntas del diagnóstico, una por una | «Colega, plantea el diagnóstico.» |
| Recorrido de noviembre | Presenta el bloque como la última unidad del curso | «Colega, presenta el recorrido de noviembre.» |
| ICN 1 (tras explicar el mapa) | Verifica comprensión (regla vs. patrón) y resuelve dudas | «Colega, verifica comprensión del mapa.» |
| ICN 2 (tras explicar el pipeline) | Verifica comprensión (entrenar vs. predecir; prueba aparte) | «Colega, verifica comprensión del pipeline.» |
| Práctica, ticket y cierre | No es protagonista | — |

Entre intervenciones se **silencia el micrófono** de la voz. **Plan B:** Diego lee la intervención escrita, o un error de la voz se usa como momento de curiosidad crítica («¿cómo podemos comprobarlo?»).

## Colab guía — `Clase 41 - Mapa IA - Clase.ipynb`

Es la **puerta de entrada y el hilo de la clase**; la práctica vive en el HTML y el Colab dice cuándo ir a cada actividad.

1. Encabezado «Clase 41 — Mapa de la IA + pipeline» · curso 3ro medio.
2. 🎯 Objetivo · 🌱 ¿Por qué lo veremos? (sin sección de Propósito).
3. **Enlace al HTML** (`https://clases-ia-mario-bertero.vercel.app/clase-41/`) con una línea: «Lo abrimos y vamos a la actividad que nos indiquen; cada una se abre con un código que nos entregan en la sala».
4. Haz Ahora: 5 celdas de texto para anotar ideas propias.
5. «Nuestro recorrido»: ruta de noviembre, fechas de E1/E2/E3 y cómo se forman las dos notas.
6. **ICN 1:** Diagrama 1 (imagen incrustada) + Ideas clave (IA completa, ML, DL, generativa, regla, patrón) → «👉 Ahora la actividad **M1** en el interactivo» → siguiente concepto → **M2** → **M3**.
7. **ICN 2:** Diagrama 2 (imagen incrustada) + Ideas clave (variables y etiqueta, entrenar vs. predecir, la prueba aparte) → **P1** → **P2** → **P3** → **P4**.
8. «🎫 Ticket de salida: lo abrimos en el interactivo con el código que nos entreguen» (sin preguntas ni alternativas en el Colab).
9. Cierre: objetivo reimpreso y preguntas para responder a viva voz (sin celdas de respuesta).
10. **Ningún código Python, ninguna respuesta, nada de la modalidad de trabajo, ningún código de actividad escrito en el Colab.**

## HTML interactivo — `Clase 41 - Mapa IA - Interactivo.html`

- **Un solo archivo autocontenido** (CSS y JS incluidos), sin bibliotecas ni servicios externos, que funciona sin conexión una vez descargado. Los diagramas se publican aparte como PNG.
- **Secciones, en orden:** orientación → nuestro recorrido → M1 · M2 · M3 → P1 · P2 · P3 · P4 → ticket (TK). **Cada actividad parte bloqueada** con su código de 3 números y se puede abrir una a la vez; las ya abiertas quedan abiertas.
- **Progreso visible**, instrucciones cortas en cada ronda, **pistas** colapsables, botón **Comprobar** con retroalimentación explicativa y reintento.
- Si guarda el avance en el navegador: aviso de dónde se guarda, botón «Reiniciar» y advertencia de equipo compartido (lectura/escritura en `try/catch`; debe funcionar sin almacenamiento).
- **Sin identificación personal.** No envía ni registra respuestas.
- **Criterio de aceptación (v2 §4):** completar mapa y pipeline, corregir, desbloquear cada actividad con su código (y verificar código incorrecto), conservar las respuestas al desbloquear la siguiente y usar todo **sin arrastre** (solo botones/teclado). Accesible (contraste, foco visible, no solo color) y sin scroll horizontal a ancho de teléfono.
- **Fórmulas:** ninguna en esta clase. Si apareciera alguna, MathJax o KaTeX local.
- **Convenciones:** español de Chile, voz colectiva («vamos a», «nos pide»), nunca Diego en tercera persona.

## Decisiones de diseño relevantes

- **Curiosidad (actitud):** elegida por Diego el 2026-10-31. Se retoma en el cierre con una pregunta no binaria.
- **Sin Propósito y «¿Por qué lo veremos?» (decisión de Diego, 2026-10-31, vigente para todas las clases desde ahora):** se elimina la sección «Propósito» y «¿Para qué sirve?» pasa a llamarse «¿Por qué lo veremos?».
- **Definiciones del mapa:** IA con la definición de Diego (resumida en el diagrama, completa en el Colab); ML **sin la palabra «regla»**; DL y generativa sin cambios; **regla y patrón** definidos aparte, fuera del diagrama.
- **Sin 4D en esta clase (decisión de Diego, 2026-10-31):** el v2 las ubica en ética (23-nov). La voz y Diego pueden mencionar la idea de «revisar si algo es confiable» sin nombrar las 4D.
- **La IA generativa no se presenta como cuarto círculo anidado** (v2 §4): se enseña por lo que produce.
- **Códigos de 3 números por actividad** (decisión de Diego, 2026-10-31): regulan el ritmo para que nadie se adelante; no son seguridad. Reemplazan a la contraseña única del ticket.
- **El ticket tiene 4 preguntas y vive solo en el HTML** (decisión de Diego, 2026-10-31; descartó el PPT): autorrevisado (v2 §4 ajustado en v3 §10.4), sin exportación ni entrega.
- **El HTML contiene las respuestas de las rondas y del ticket** (necesario para dar retroalimentación inmediata). Se asume que el repositorio y el sitio son públicos, igual que el resto del curso.
- **Sin pandas, sin código en la clase:** el código parte en N°42.
- **Ninguna actividad depende de otra persona:** todo se resuelve individualmente.
- **Ejemplos genéricos, sin atribuir técnicas a productos concretos** (v2 §4, recorrido obligatorio 2), salvo ChatGPT, que el v2 permite nombrar como generación basada en aprendizaje profundo.

## Pendientes para el gate

- [ ] **Códigos de las 8 actividades:** los de la tabla son valores por defecto; Diego los cambia o aprueba antes de generar el HTML.
- [ ] **Anuncio de la modalidad:** lo hace Diego en vivo (no aparece en ningún material).
- [ ] Confirmar que `clases-ia-mario-bertero` esté disponible como nombre de proyecto en Vercel; si no, se avisa antes de elegir otro.
