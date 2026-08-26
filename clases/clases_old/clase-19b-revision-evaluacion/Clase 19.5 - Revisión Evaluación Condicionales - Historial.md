# Clase 19.5 — Revisión Evaluación Condicionales — Historial

**Estado:** Colab de clase **aprobado** (2026-08-02). Existen el material de proyección, la spec, el Colab de clase, el Solucionario y el JSON del Ticket de Salida; faltan el PPT y el PPT aparte del Ticket de Salida, que quedan para una sesión aparte.

**Fecha prevista:** lunes 3 de agosto de 2026 · 80 minutos.
**Numeración:** N° 19.5, decimal, para no renumerar el resto del plan (mismo patrón que 22.5 y 28.5). Va entre la evaluación del 28-07 y For anidado del 06-08.

---

## 2026-08-01 — Diagnóstico de resultados de la Evaluación 2

Se calcularon los porcentajes de logro por ítem y por componente a partir de la fuente que tiene los puntajes reales (el generador de los Colabs de devolución). Resultados agregados, sin datos individuales:

| Ítem | Máx | % todos | % tramo alto | % tramo bajo |
|---|---|---|---|---|
| 1A.1 — `and` simple | 4 | 65% | 85% | 41% |
| 1A.2 — `and` + `or` | 4 | 60% | 85% | 28% |
| 1B.1 — bug `=` / `==` | 4 | 89% | 92% | 81% |
| 1B.2 — bug `>` / `>=` en el límite | 5 | 82% | 92% | 75% |
| 1B.3 — bug falta `:` | 4 | 94% | 100% | 88% |
| 1B.4 — bug de indentación | 4 | 89% | 100% | 78% |
| **1B.5 — bug orden de `elif`** | 5 | **48%** | **66%** | 22% |
| 2.1 — Modo Fiesta | 12 | 83% | 100% | 58% |
| 2.2 — Micro a Talagante | 16 | 61% | 97% | 6% |
| 2.3 — Ahorro en dólares | 18 | 65% | 99% | 6% |
| 2.4 — Sala de juego | 24 | 61% | 97% | 0% |

**Conclusiones que dirigen el diseño:**

1. **La distribución está partida en dos, sin medio:** 13 estudiantes sobre 88 puntos, 8 bajo 34, y un solo caso intermedio. Solo 2 tienen la prueba perfecta.
2. **Para el tramo alto la Sección 2 no dejó nada que reforzar** (97-100%). Una clase de repaso general de condicionales los desperdiciaría.
3. **El único error genuinamente transversal es 1B.5 — el orden de la cadena de `elif`:** 7 de los 13 del tramo alto perdieron puntos ahí, y 5 de ellos sacaron 1 de 5. El mismo hilo reaparece en los dos componentes más débiles de ese tramo: anidamiento (2.2 y 2.4) y operadores consistentes en las fronteras (2.3). Sumados, alcanzan a 10 de los 13.
4. **Los 8 del tramo bajo dejaron 2.2/2.3/2.4 en blanco.** Es un problema de producción y de tiempo, no de matiz conceptual: necesitan volver a escribir programas completos con andamiaje, no ver una corrección proyectada.
5. Errores menores, reales pero de otro eje: hardcodear el resultado en los ítems 1A, y pedir un dato con `input()` sin convertirlo a número.

## 2026-08-01 — Enfoque acordado

El eje único de la clase es la pregunta **"¿estas dos preguntas son independientes, excluyentes, o una depende de la otra?"**. Absorbe los tres errores en un solo concepto con tres casos:

| Relación | Forma en Python | Error que explica |
|---|---|---|
| Independientes | varios `if` seguidos | *nunca se enseñó* — es contenido nuevo |
| Excluyentes | `if / elif / else` | 1B.5 |
| Una depende de la otra | `if` anidado | 2.2 y 2.4 |

Que los `if` sueltos sean contenido nuevo está verificado contra la spec de la Clase 14: ahí se enseñó "solo una rama se ejecuta" y "el orden importa", pero siempre dentro de `elif`, nunca contrastado con `if` independientes.

Como herramienta transversal se enseña **probar el valor del borde** (14, 7, 3, 800), que es el hábito que faltó y que explica tanto 1B.5 como las fronteras de 2.3.

Los errores menores del punto 5 **no entran al ICN** — van a las 3 preguntas del Ticket de Salida, para no sobrecargar la clase.

**Decisiones de Diego tomadas en esta sesión:**
- No hay recuperativa: es **cierre formativo**, la nota está cerrada. Conviene decirlo al abrir para que la clase no se vuelva negociación de puntos.
- Los Colabs de devolución se entregan **al inicio** de la clase, no al final.
- El tramo alto no hace de ayudantía: tiene trabajo propio (diseñar los casos límite que rompen programas). El emparejamiento con el tramo bajo es simétrico — quien diseña casos necesita un programa que probar, y quien repara necesita saber si su arreglo aguanta.

## 2026-08-01 — Material generado

`Clase 19.5 - Revisión Evaluación Condicionales - Tres Formas.html` — landing de proyección, pixel art, un solo archivo sin dependencias externas (funciona sin internet en la sala).

- Los tres casos representados como ríos animados: cauces paralelos, un cauce con desvíos en cadena, y compuertas en serie.
- Dentro del caso anidado, un **par de escenas de contraste** con el mismo pasajero —uno que sí tiene pase escolar—: con anidado el cauce del saldo queda seco; con dos `if` sueltos el saldo corre por su propio río y la pregunta se hace igual. El panel incorrecto se ve idéntico al caso 1, que es exactamente el punto.
- Mascota: el logo de Python en pixel art. Solo se dibuja la serpiente azul; la amarilla se genera rotándola 180°.
- El agua fluye ⟶ en los tramos horizontales y ⟱ en las bifurcaciones (pedido de Diego).
- **Convención de estilo pedida por Diego:** toda condición sobre una variable booleana se escribe con `== True` explícito (`if hay_mensaje_nuevo == True:`), para que a los estudiantes les quede claro qué se está comparando. Las comparaciones numéricas quedan tal cual. Es una decisión pedagógica deliberada — no "corregirla" a la forma idiomática de Python.

Verificado en navegador: los 7 canvas con escalado entero, sin desborde horizontal, y la lógica de cada escena comprobada leyendo los píxeles pintados.

## 2026-08-01 — Spec aprobada

Objetivo: distinguir si dos condiciones son independientes, excluyentes o dependientes, escribir la forma de `if` que corresponde y comprobarla en el valor del borde, **con rigurosidad**. OAs: `OA1, OA3 | OAd`.

Actitud elegida entre cuatro candidatas (Criterio, Rigurosidad, Método, Autocrítica). Diego eligió **Rigurosidad**, que ancla la clase en la herramienta transversal —probar el valor del borde— y no solo en el eje de decisión.

**Cambio de arquitectura pedido por Diego durante el diseño (v1 → v2).** La primera versión abría con un escenario inventado (una corrida familiar por la ribera del Maipo) que compartía narrativa con la Práctica Guiada, según el patrón por defecto. Diego pidió que **la revisión de la prueba se "comiera" el Haz Ahora**, partiendo con ejemplos de los errores comunes y usándolos como rampa de entrada al HTML. Se descartó la corrida por completo: la clase entera se construye ahora sobre ítems reales de la Evaluación 2.

Esto destrabó un hallazgo que ordenó el resto: **el ítem 1B.5 (el error transversal, 48% de logro) es la racha de días de estudio con umbrales 14 / 7 / 3 — exactamente el escenario y los números que ya estaban dibujados en la tarjeta 2 del HTML.** El mapa fragmento → tarjeta quedó registrado en la spec.

**Segundo ajuste pedido por Diego (v2 → v3).** El Haz Ahora pasó de ser una secuencia proyectada y conducida por Diego a una **actividad trabajada por los estudiantes**: los tres fragmentos van como celdas ejecutables en el Colab, con cuatro preguntas escritas que responden en parejas antes de revisar en conjunto. Esto resolvió de paso el timer del PPT (`<<7:00>>` sobre el tramo autónomo) y evitó pedir "predecir sin ejecutar" en Colab. El presupuesto se reajustó a 4 / 7+5 / 15 / 18 / 20 / 6 / 5 = 80 min; el ICN pudo bajar a 15 porque el Haz Ahora ahora hace trabajo real.

**Andamiaje de la Ruta B — decidido por Diego: opción A (tabla de decisión).** Se le presentaron las dos opciones lado a lado: (A) andamiaje en el enunciado, con una tabla de decisión que completan antes de programar y celda de código vacía; (B) starter code con los `if` puestos y las condiciones en blanco. Eligió A, que además respeta la regla 15 del `CLAUDE.md` (celda de código siempre vacía, sin código de partida). Razón pedagógica: B les regala la estructura, que es exactamente lo que fallaron.

Se mantuvo sin cambios desde la v1: la Práctica Independiente diferenciada en parejas cruzadas (Ruta A diseña la batería de casos límite y la corre contra el programa de su pareja; Ruta B reescribe los ítems 2.2 y 2.3), las 3 preguntas del Ticket de Salida (hardcodear el resultado, `input()` sin convertir, y `elif` vs. `if` sueltos) y el Cierre.

Carpeta y nombrado: se conservan `clase-19b-revision-evaluacion` para la carpeta y el prefijo `Clase 19.5 - ...` para los archivos, tal como ya existían.

## 2026-08-02 — Colab de clase generado

Archivos: `Clase 19.5 - ... - Clase.ipynb` (39 celdas), `... - Solucionario.ipynb` y `... - Ticket de Salida Respuestas.json` (B / C / D). Generados con `generar-colab-clase`. El notebook se ejecutó completo con `nbconvert`: 0 errores, y los 7 outputs calzan uno a uno con lo documentado en el spec.

**Correcciones técnicas aplicadas al spec** (sin cambiar el diseño aprobado, solo lo necesario para que el generador produzca lo que el spec ya describía):
- Los cuatro ejemplos del ICN venían sin definir sus variables (`bateria_baja`, `racha_dias_estudio`, `tiene_pase_escolar`) — reventaban con `NameError` y obligaban a ejecutar en orden estricto. Ahora cada celda es autocontenida y trae su salida con `>>`. El ejemplo del Concepto 3 usa **los mismos datos del Programa 3 del Haz Ahora** (`"si"` / 200) a propósito: ahí imprimía dos líneas contradictorias, acá imprime una sola.
- Las tres tablas de resultado esperado (Guiada, Ruta B Ej 1 y Ej 2) pasaron de tabla markdown a `<table>` HTML, que es el formato canónico y el único que el parser reconoce.
- Las tablas de decisión de la Ruta B pasaron del enunciado a `**Plantilla de respuesta:**`, así el estudiante las completa en su propia celda editable en vez de escribir sobre el enunciado.

**Cambio de contenido que sí conviene revisar:** los rótulos de las rutas eran `Ruta A — para quienes ya resolvieron la Sección 2 completa` y `Ruta B — para quienes dejaron esos ejercicios sin terminar`. En el spec eso está bien, pero el notebook lo abre el curso entero, así que en el material visible quedaron neutros y descriptivos del trabajo: **"Ruta A — Diseñar los casos que rompen programas"** y **"Ruta B — Escribir los programas"**. Quién va en cada ruta lo dice Diego en la sala; el criterio de rendimiento quedó registrado en el spec como nota de conducción. La intro de la sección también se reescribió en voz de estudiante ("hoy trabajan en parejas cruzadas…") en vez de la voz de planificación original.

**Agregado al Solucionario:** batería de referencia de la Ruta A (4 casos de la micro + 5 del ahorro, con el error que caza cada uno). Sin eso Diego no tenía contra qué comparar lo que entregue ese tramo. La Ruta A Ejercicio 2 no lleva referencia porque depende del programa que le toque probar.

**Cambios al generador `crear_colab.py`** — todos generales, aplican a clases futuras:
- Acepta numeración decimal en el título (`Clase 19.5`); antes quedaba sin número ni tema.
- Haz Ahora con celdas de código ejecutables cuando el spec trae bloques ` ```python `.
- Práctica Independiente diferenciada por rutas (`#### Ruta X — …`), con numeración propia por ruta.
- Directivas nuevas por ejercicio: `**El trabajo debe:**` (alias), `**Celda de respuesta:**`, `**Plantilla de respuesta:**`, `**Solución de referencia:**`.
- Resultado esperado en tabla HTML side-by-side (la variante con `input()` variable, que estaba documentada pero sin implementar).
- Filtro de `Nota de conducción:` junto a `Propósito:` / `Objetivo:`.
- Dos bugs corregidos: la "Idea clave" se cortaba en la primera palabra en negrita, y los backticks dentro de las pistas `<details>` salían literales en vez de renderizarse como código.
- Script nuevo `limpiar_outputs_haz_ahora.py`: la ejecución de verificación deja los outputs dentro del `.ipynb`, y en el Haz Ahora eso elimina justo el acto de ejecutar que se está pidiendo. Las celdas del ICN sí conservan su salida.

## 2026-08-02 — Haz Ahora reestructurado (feedback de Diego)

El Haz Ahora tenía los tres programas seguidos y las cuatro preguntas juntas al final. Diego pidió dos cambios, ambos aplicados:

1. **Cada programa lleva ahora su propio enunciado**, con título de escenario (`Programa 1 — La app de hábitos de estudio`) y una línea `*Lo que debía hacer:*` que describe el comportamiento correcto. Razón textual de Diego: *"dudo que se acuerden ni yo lo recuerdo"*. Sin eso la pregunta "¿qué debería imprimir?" no es contestable — solo se ve el output, no la brecha.
2. **La pregunta y su espacio de respuesta van pegados a cada programa**, no todas al final. La secuencia quedó: enunciado → celda de código → pregunta → celda markdown editable, tres veces, más la pregunta 4 ("¿cuál se parece a un error tuyo?") bajo un bloque **Para cerrar**.

Para esto se agregó al generador el marcador `[[respuesta]]`: una línea con solo eso inserta una celda markdown editable en ese punto, y desactiva la celda única de "Mis respuestas" del final. Es general, sirve para cualquier clase futura cuyo Haz Ahora alterne bloque de código y pregunta.

El notebook quedó en 45 celdas (antes 39). Re-ejecutado con `nbconvert`: 0 errores, y los outputs del Haz Ahora limpiados de nuevo.

## 2026-08-02 — Ticket con contextos nuevos + Práctica Independiente rediseñada

**Ticket de Salida.** Diego aprobó los tres ejercicios pero pidió cambiarles el contexto para que no repitieran la clase ni la prueba. Misma trampa y mismo código en cada uno, situación nueva: P1 pasó del torneo al **espacio libre del celular para instalar un juego** (correcta C); P2, del saldo bip al **precio de la entrada a un partido** (correcta A); P3, de batería/wifi a **dos avisos de un videojuego: vida baja y amigo conectado** (correcta D). Las tres letras siguen siendo distintas. Se dejó anotada la razón en el spec: el Ticket mide transferencia a una situación nueva, no memoria del ejercicio.

**Práctica Independiente — descartada la versión de rutas cruzadas.** Diego la declaró inviable. El problema de fondo no era diferenciar, sino la **dependencia entre las dos rutas**: quien diseñaba casos no podía empezar a probar hasta que su pareja tuviera un programa funcionando, y esa pareja era justamente el tramo que había dejado esos ejercicios en blanco. Sumado a eso, armar las parejas cruzadas antes de la clase y sostener dos bloques paralelos en un mismo notebook.

Se le propusieron tres alternativas, todas sin rutas ni dependencias. **Eligió la opción A**, con dos pedidos propios:
1. Que el programa del Ejercicio 1 tuviera **dos o más funcionalidades declaradas**, para que la búsqueda del error fuera más difícil.
2. Que hubiera un **verificador ejecutable** para que se autorrevisen entre ejercicio y ejercicio.

**Cómo quedó:**
- **Ejercicio 1 — Las dos versiones del taller de robótica.** Se les dan dos programas completos que hacen dos cosas a la vez (decidir el ingreso + avisar cupos disponibles). Con casi cualquier dato imprimen lo mismo; solo difieren cuando la persona **está inscrita**, porque la Versión 2 le hace igual la pregunta de la autorización. El trabajo es encontrar un dato que las separe, anotarlo, y justificar cuál está bien. Contexto nuevo, no reusa la micro.
- **Ejercicio 2 — La alcancía en dólares.** Retoma el ítem 2.3 de la prueba (65% de logro) y le suma un aviso independiente del nivel: el recordatorio de repartir lo ahorrado si la alcancía fue compartida. Así el mismo programa mezcla **excluyentes** (las 4 franjas) e **independientes** (el aviso), que son dos de las tres formas del ICN.
- **Autochequeo.** Celda `#@title` al inicio de la sección con dos funciones. `comparar_versiones(...)` corre internamente ambas versiones del taller y dice si se comportaron igual o distinto — convierte "encuentra el caso que rompe esto" en algo verificable. `verificar_bordes(con_10=, con_30=, con_60=)` recibe lo que el programa del estudiante imprimió en los tres bordes y lo compara, normalizando tildes y puntuación para no dar falsos negativos. Ambas probadas antes de integrarlas.

Ya no hay tramos, ni rutas, ni rótulos: los mismos dos ejercicios para todo el curso. La diferenciación ocurre sola, porque encontrar el dato que separa las dos versiones tiene techo alto y la celda de código del Ejercicio 2 parte vacía para todos.

**Cambios adicionales al generador:** directivas `**Celda de configuración:**` (celda de código al inicio de la Independiente) y `**Celda de verificación:**` (por ejercicio, ubicada antes o después de la respuesta según si el ejercicio se responde en código o en markdown). Además se generalizó la limpieza de outputs: ahora la regla es **conservar outputs solo en el ICN** y limpiarlos en todas las demás secciones — antes solo limpiaba el Haz Ahora, y las celdas de verificación habrían quedado con su salida ya impresa.

Notebook final: 40 celdas, ejecutado sin errores, verificador funcionando.

**Ajustes posteriores del Ejercicio 1 (mismo día).** Diego pidió que las dos versiones se vieran **lado a lado** y que la respuesta no fuera una tabla sino texto libre. Las dos versiones pasaron a una tabla HTML de dos columnas y una fila, con el código en `<pre>` (pierde el coloreado de sintaxis, que es el costo de ponerlas lado a lado — las cercas ```` ```python ```` no se pueden poner en columnas). Para que las columnas quepan sin desbordarse, los cinco mensajes se acortaron; el `<` de `cupos_disponibles < 5` va escapado como `&lt;` porque dentro de HTML crudo se interpretaría como apertura de etiqueta. La celda de respuesta quedó como una sola línea de consigna y espacio libre para escribir.

**Chequeo de sincronía.** El código de las dos versiones existe duplicado: el que se muestra en la tabla y el que el verificador corre por dentro. Si se desincronizan, el ejercicio miente. Se comparan programáticamente después de generar (extrayendo el `<pre>` del enunciado y el cuerpo de `_version_1`/`_version_2` del verificador) y quedaron idénticas línea a línea.

## 2026-08-02 — Colab de clase aprobado

- Archivos: `Clase 19.5 - ... - Clase.ipynb` (40 celdas), `... - Solucionario.ipynb`, `... - Ticket de Salida Respuestas.json`.
- Generados con `generar-colab-clase`; ejecutados con `nbconvert` sin errores.

**Decisión que se lleva a la skill:** el autochequeo (celda de configuración + celdas de verificación) queda como capacidad **opcional** de `generar-colab-clase`, y **se le pregunta explícitamente a Diego antes de incluirlo** en cualquier clase futura. No es parte del formato por defecto: cambia cómo se trabaja la Práctica Independiente en aula y cuesta tiempo de clase, así que la decisión es suya. Es una excepción deliberada a la restricción 6 del `CLAUDE.md` (aprobación solo en gates formales), documentada en el `SKILL.md`.

## 2026-08-02 — PPT de la clase generado

- Archivo: `Clase 19.5 - ... - Presentación.pptx` (10 slides, termina en el Cierre).
- Generado con `generar-ppt-clase`.

**Versión proyectada del Haz Ahora.** El Haz Ahora del Colab son tres programas completos en celdas ejecutables: volcarlo tal cual en una slide daba un resultado ilegible (código, marcadores `[[respuesta]]` y las cuatro preguntas apelmazados en una caja). Se agregó al spec una sección `## Proyección — Haz Ahora (PPT)`, al final del archivo, que **solo lee `generar-ppt-clase`** — el Colab no la ve, así que el notebook aprobado no se toca. Proyecta la consigna y la lista de tareas; el detalle lo tiene cada estudiante en su pantalla.

**Cuatro bugs del generador que este spec destapó, todos corregidos:**
- El número de clase no aceptaba decimales: la portada salía "Clase None".
- El `## Propósito` se comía las secciones intermedias (`## OAs MINEDUC`, `## Apertura`) y las imprimía en la slide 2.
- Las dos preguntas del Cierre salían vacías: el parser solo aceptaba el texto en la línea siguiente a la etiqueta, no en la misma línea.
- **Texto dibujado fuera de su caja** (anterior a esta clase): con ejemplos de 10-11 líneas, el código se salía del terminal negro y la Idea clave de su recuadro ámbar. El reparto de alturas era proporcional a una densidad estimada, sin mirar el largo real del contenido. Ahora hay un solver que mide y busca los tamaños con que todo cabe, apretando primero la prosa y dejando el código para el final. Verificado sin regresiones en las clases 14, 16 y 20.

Efecto colateral asumido: en los slides de los conceptos 2 y 3 el código quedó en 14pt, porque son ejemplos de 11 líneas.

## 2026-08-02 — Se saca toda alusión a la evaluación

Diego postergó la entrega de los Colabs de devolución (dos casos de sospecha de copia todavía abiertos) y pidió sacar del material **toda** referencia a la prueba. Cambios en el spec, con Colab, Solucionario, JSON y PPT regenerados:

| Antes | Ahora |
|---|---|
| Título: `Clase 19.5 — Revisión Evaluación Condicionales` | `Clase 19.5 — Condicionales: independientes, excluyentes y anidadas` |
| Haz Ahora: "Tres programas **de la prueba** que estuvieron mal resueltos" | "Tres programas que tienen algo mal: cada uno hace casi lo que debía, pero no del todo" |
| Pregunta 4: "¿cuál se parece a un error que cometiste tú **en la prueba**? Míralo en tu **Colab de devolución**" | "¿cuál te costó más darte cuenta de qué estaba mal? ¿Qué fue lo que te hizo verlo?" |
| Form, "Tema de la clase de hoy": `revision evaluacion` | `condicionales independientes` |
| Apertura: entregar los cuadernos + "la nota está cerrada, no hay recuperativa" | Sin entrega y sin mencionar la evaluación; los ~4 min quedan de holgura para la Independiente |
| Frase de entrada al HTML: "dos de estos tres los reconocen **de la prueba**" | "dos de estas tres formas ya las conocen" |

**Los nombres de archivo y de carpeta NO se renombraron** a propósito: los links de Colab ya pusheados a GitHub apuntan a `clase-19b-revision-evaluacion`, y renombrar los rompería, además de obligar a tocar `Historial-Curricular.md`. El desfase es solo interno — lo que ven los estudiantes es el título de la primera celda, que sí cambió.

Para poder cambiar el nombre breve del Form sin renombrar la carpeta, `generar-colab-clase` ahora acepta `- **Tema breve (Form):** ...` en el Contexto del spec, y ese valor manda por sobre el slug de la carpeta.

La pedagogía no cambió: los tres programas del Haz Ahora siguen siendo los ítems reales mal resueltos, solo que ya no se nombran como tales.

## 2026-08-02 — HTML de los tres ríos desplegado en Vercel

`Clase 19.5 - Revisión Evaluación Condicionales - Tres Formas.html` quedó además publicado en línea, como complemento al uso offline en la sala:

**https://clase-19-5-tres-rios.vercel.app**

Proyecto `diegovp2001/clase-19-5-tres-rios`, primer deploy del proyecto (por eso Vercel lo asignó directo a producción). Verificado en navegador: carga completo, sin dependencias externas rotas. De paso quedó autenticado el Vercel CLI local (cuenta `diegovp2001-9146`), reutilizable para desplegar material de proyección de otras clases sin volver a loguearse.

---

## 2026-08-02 — PPT del Ticket de Salida generado (y automatizado)

Archivo: `Clase 19.5 - Revisión Evaluación Condicionales - Ticket de Salida.pptx` — 8 slides.

Es el **primer** Ticket de Salida proyectado del proyecto, así que en vez de armarlo a mano se escribió un generador propio en la skill: `.claude/skills/generar-ppt-clase/crear_ppt_ticket.py`. Lee la sección `### 5. Ticket de Salida` del spec (misma fuente de verdad que el Solucionario y el JSON) y reusa la paleta y los helpers visuales de `construir_plantilla.py`, así que el diseño es idéntico al de `Presentación.pptx` sin duplicar nada.

Estructura:

| Slide | Contenido |
|---|---|
| 1 | Portada + reglas de la dinámica (una por una, en silencio, anota la letra, el Form al final) |
| 2-4 | Una por pregunta: enunciado + bloque de código + las 4 alternativas A/B/C/D |
| 5 | Pantalla del Form: link grande + qué escribir (nombre, `condicionales independientes`, las 3 letras) |
| 6-8 | Revisión: la alternativa correcta destacada en verde + la justificación |

Las slides de revisión van **después** de la del Form, no antes: ese es el orden de la dinámica y es lo que evita el efecto arrastre. Respuestas correctas verificadas contra `Ticket de Salida Respuestas.json`: C, A, D.

**Decisión de diseño del solver.** En las slides de pregunta el tamaño de fuente se resuelve automáticamente. La primera versión heredaba la prioridad del ICN (el código se achica último) y dejaba las alternativas en 14pt, ilegibles desde el fondo; se invirtió y quedaron en 24pt con el código en 16pt. Ver la corrección del mismo día, más abajo.

## 2026-08-02 — Preferencia definitiva: el código manda sobre las alternativas

Diego revisó el PPT del Ticket, achicó a mano las alternativas de la Pregunta 1 a ~20pt para darle aire al terminal y pidió que de ahí en adelante el generador prefiera **código grande y alternativas más chicas**.

La skill quedó con esa preferencia expresada como pesos explícitos en `crear_ppt_ticket.py`: `_PESO_COD = 2.0` vs `_PESO_ALT = 1.0` — cada punto de fuente que se le saca al código cuesta el doble que uno sacado a las alternativas, así que cuando algo tiene que ceder, ceden ellas. El razonamiento: las alternativas son frases cortas y aguantan un par de puntos menos, el código es el objeto de la pregunta y hay que leerlo desde el fondo de la sala.

| Pregunta | Antes (código/alternativas) | Ahora |
|---|---|---|
| P1 | 16 / 24 | **20** / 18 |
| P2 | 18 / 24 | **20** / 22 |
| P3 | 20 / 18 | **20** / 18 |

El código queda en 20pt (el techo de la escala) en las tres. Si alguna vez las alternativas quedan demasiado chicas, se sube `_PESO_ALT`; las escalas de tamaño no se tocan.

**El archivo de esta clase no se regeneró**: Diego ya lo dejó ajustado a mano y además lo renombró a `Clase 17 - ...`. El cambio aplica desde el próximo Ticket.

## Pendientes

- **El PPT del Ticket NO se commitea ni pushea antes de dictar la clase** — el repo es público y ese archivo trae las preguntas y las respuestas correctas. Se sube recién después del lunes 3, junto con el resto de la carpeta.
- **Aprobación del PPT de la clase** y, con eso, el commit + push de la carpeta.
- **Entrega de los 22 Colabs de devolución: postergada**, no es bloqueante para esta clase. Queda pendiente resolver los dos casos de sospecha de copia y, con eso, escribir `puntajes_evaluacion2.json` (hoy con todo en `null`). Ver el plan de revisión en la carpeta de la Clase 19.
- Sin decisiones abiertas de diseño: las rutas diferenciadas se descartaron y con ellas la duda de sus rótulos.
