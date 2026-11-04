# Clase 43 — Guía docente: el colega del profesor (ChatGPT Voice)

**Solo para ti (no se sube a Classroom ni se proyecta).** **Lunes 9-nov-2026** · 80 min · 3ro medio. *(En todo lo que ven los estudiantes —Colab y página— se le llama «el colega del profesor»; aquí aparece ChatGPT Voice solo porque es la herramienta que usas.)*

Hoy el colega tiene **tres papeles**: dice él mismo el «¿Por qué lo veremos?» (para asombrar y entusiasmar), plantea el Haz Ahora como **apicultor que quiere automatizar algo que los estudiantes no conocen**, y **lanza retos desafiantes** al curso. Además queda disponible para **responder preguntas difíciles** cuando tú lo actives. Sigue sin ser protagonista en la práctica ni en el cierre. **Solo habla cuando tú lo activas.**

## 1. Antes de la clase (5 min)

- [ ] Cuenta de profesor abierta en ChatGPT, **modo de voz probado** con el parlante de la sala (volumen y eco).
- [ ] **Conexión estable** (celular como respaldo).
- [ ] **Pega el prompt de arranque** (sección 2) y espera su confirmación («Listo, Colega al aire»). Después **silencia el micrófono**: responde ante cualquier pausa o ruido.
- [ ] Colab proyectado y la página `https://clases-ia-mario-bertero.vercel.app/clase-43/` abierta en otra pestaña (paso a paso y laboratorio).
- [ ] Plan B listo: esta guía impresa o en otra pantalla.

## 2. Prompt de arranque (copiar y pegar)

> Eres «Colega», un colega docente que me acompaña en una clase de 3ro medio en un liceo de Isla de Maipo, Chile. Hablas español de Chile, con tono cercano y entusiasta, para estudiantes de 16 y 17 años.
>
> **Reglas:**
>
> 1. Solo hablas cuando te lo pido con la frase «Colega, …». Si no te hablo, guardas silencio total.
> 2. Tus intervenciones duran como máximo 20 a 30 segundos (la bienvenida puede llegar a 40).
> 3. Te diriges al curso («curso» o «estudiantes»), no a mí.
> 4. Cuando planteas un reto o una pregunta, esperas la respuesta del curso. No la respondes tú.
> 5. No inventas datos sobre el liceo, el curso ni las personas. **Si no estás segura de algo, lo dices con esas palabras («no estoy segura»).** Nunca inventes cifras ni nombres de productos.
> 6. No adelantas contenidos: **no expliques cómo se entrenan o ajustan los pesos de forma automática** (eso es de la próxima clase). Si te preguntan, di que la próxima clase lo vemos.
> 7. No das discursos ni resumes la clase si no te lo pido.
> 8. Si alguien se equivoca, no lo corriges de inmediato: preguntas «¿cómo podemos comprobarlo con la neurona?».
>
> **Datos de la clase de hoy (úsalos tal cual, no agregues otros):**
>
> - Objetivo: crear nuestra primera inteligencia artificial: una neurona, con asombro.
> - Qué es una neurona artificial: recibe datos, multiplica cada dato por un número llamado *peso* (su importancia), los suma, le agrega un número llamado *sesgo* y decide con una regla simple: si el resultado `z` es 0 o más, sale 1 (se activa); si no, sale 0.
> - Historia de la clase: un apicultor de Isla de Maipo quiere automatizar la decisión de si sus abejas saldrán hoy a buscar néctar. Los datos son ficticios. Cada día se anotan tres cosas: temperatura en grados, viento en km/h y lluvia en milímetros. La etiqueta es 1 si las abejas salieron y 0 si se quedaron.
> - Los días se separan en **entrenamiento** (8 días: aquí se ajustan los pesos) y **prueba** (4 días nuevos: se miran una sola vez, al final, para ver si la neurona predice días que nunca vio).
> - Pesos de partida: temperatura 1, viento −0,5, lluvia −2; sesgo −13.
> - Qué pasa con ellos: acierta 6 de 8 días del entrenamiento; falla el día 4 (30 °C, 20 km/h de viento) y el día 6 (26 °C, 6 km/h, 4 mm). Subir la importancia del viento (peso −1) arregla los dos días, pero en la prueba acierta 3 de 4.
> - Sobre ti: tú estás hecha de redes de neuronas artificiales; sus pesos se ajustan automáticamente con muchos datos, y son miles de millones. No des cifras exactas ni detalles de tu arquitectura: no los sabes con certeza.
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos del colega (las frases de activación son sugerencias y pueden variar)

| # | Cuándo | Frase de activación | Qué hace el colega | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida + «¿Por qué lo veremos?»** (min 0–6) | «Colega, da la bienvenida al curso.» | Saluda, **espera a que el curso le devuelva el saludo**, dice el texto de abajo y pide que alguien lea el objetivo. | Activas, dejas que el curso salude, silencias; cuando alguien lee el objetivo preguntas: *¿qué creen que tiene adentro una IA?* | Tú lees el texto con el mismo entusiasmo. |
| 2 | **Haz Ahora** (6–14) | «Colega, plantea el diagnóstico.» | Hace de **apicultor que quiere automatizar algo que el curso no conoce** y plantea las **4 preguntas una por una**, esperando al curso. | Das la palabra al curso entre preguntas y anotas en la pizarra los patrones que proponen (y la idea de «convertirlo en número» y «comprobar con días nuevos»). | Lees las 4 preguntas del Colab. |
| 3 | **ICN, tras el concepto 2 (sesgo)** | «Colega, plantea un reto.» | **Reto 1:** *«Un día con 10 grados, sin viento ni lluvia. ¿Qué número tendría que ser el sesgo para que las abejas igual salgan?»* | El curso lo resuelve en el Colab. Respuesta: **cualquier sesgo ≥ −10**. | Lees el reto tú. |
| 4 | **ICN, tras el concepto 3 (escalón)** | «Colega, plantea otro reto.» | **Reto 2:** *«Si le quito toda la importancia al viento, o sea, peso 0, ¿qué días de la tabla cambian de salida?»* | Lo prueban en el laboratorio o en la caja lista. Respuesta: cambian los **días 7 y 8** (pasan a «salen»). | Lees el reto tú. |
| 5 | **ICN, tras «Ajusta tú»** | «Colega, plantea el último reto.» | **Reto 3:** *«Cambié dos pesos a la vez y ahora acierta 8 de 8. ¿Cómo sé cuál de los dos hizo el trabajo?»* | Guías hacia: cambiar **uno a la vez**; en el laboratorio solo el viento (−1) ya acierta 8 de 8. | Lees el reto tú. |
| 6 | **ICN (cierre)**, 3 min | «Colega, verifica comprensión de la neurona.» | Pregunta a dos estudiantes: «¿qué hace el sesgo?» y «¿para qué sirven los días de prueba y por qué no hay que mirarlos mientras ajustamos?». | Silencias entre respuestas; repites en voz alta lo que dicen si no los escucha. | Haces tú esas preguntas. |
| ∗ | **En cualquier momento — preguntas abiertas** | «Colega, responde la pregunta de [estudiante]: …» (repites la pregunta) | Responde en 20–30 segundos, **sin inventar**; si no sabe, dice «no estoy segura»; no adelanta cómo se ajustan los pesos solos. | Eliges preguntas que sumen al asombro; silencias después. | Respondes tú o la dejas para la próxima clase. |
| — | Práctica guiada, independiente, ticket y cierre | — | **No es protagonista.** | Disponible solo si surge una duda de contenido. | — |

### Texto sugerido del «¿Por qué lo veremos?» (el colega lo dice, con sus palabras)

> «Yo estoy hecha de miles de millones de piezas pequeñas llamadas neuronas. Hoy ustedes van a construir la primera, desde cero. Con ella van a poner los cimientos de lo que yo soy.»

**Frases de apoyo (no son guion):** si el curso no responde, «¿alguien se anima a intentarlo con sus palabras?»; si se equivocan, «¿cómo podemos comprobarlo con la neurona?».

## 4. Preguntas difíciles que pueden llegar (y cómo conviene responderlas)

| Pregunta probable | Respuesta corta y honesta |
|---|---|
| «¿El cerebro funciona así?» | Las neuronas artificiales se inspiraron en las biológicas, pero son una versión **muy simplificada**: solo multiplican, suman y deciden. El cerebro humano tiene unos 86 mil millones de neuronas y es mucho más complejo. |
| «¿Cómo ajusta los pesos la computadora sola?» | **La próxima clase lo vemos.** La idea: prueba, mide el error, cambia los pesos un poquito y repite muchas veces (como lo hicimos a mano). |
| «¿ChatGPT tiene neuronas?» | Usa neuronas artificiales (pesos) organizadas en redes enormes, con miles de millones de pesos. No sé cifras exactas de ningún modelo. |
| «¿Por qué el escalón y no otra regla?» | Es la regla más simple; hay otras que se usan en redes más grandes. Hoy usamos la más fácil de entender. |
| «¿Y si se equivoca la neurona?» | Justo para eso medimos el error y ajustamos pesos. Y por eso hay que revisar siempre si lo que dice tiene sentido (pensamiento crítico de la clase pasada). |
| «¿Por qué una sola neurona? ¿Se pueden usar más?» | Se pueden, y con varias neuronas se resuelven casos que una sola no puede. **Cuántas** usar se decide por prueba y error, y hoy hay sistemas complejos que automatizan esa búsqueda. Nosotros seguimos con una sola. |

## 5. Qué tiene el Colab para ti

- **Un Colab + una página** (`/clase-43/`). La práctica y el ticket se autorrevisan con `check_*()` (✅/⚠️ sin mostrar la solución); no recolectas resultados.
- **Estructura del contenido nuevo:** parte con una **caja lista** (la neurona completa; solo se mueven pesos y sesgo) y luego «abrimos la caja» para escribir la suma ponderada, el sesgo y el escalón. El **evaluador viene preparado** (`evaluar_entrenamiento()` y `evaluar_prueba()`): los estudiantes no programan el recorrido de errores, solo cambian números y **justifican** su mejor resultado. La prueba se mira **una sola vez**; si la miran dos, el evaluador lo avisa.
- Los autochequeos del Ej. 1 y 2 buscan la función **`neurona`**; el del Ej. 3 y 4 leen las variables **`pesos`** y **`sesgo`**: recuérdalo en voz alta.
- **Página:** paso a paso (slides 1–7) tras el concepto 3, y **laboratorio** (slide 8) para los retos 2 y 3. Si no hay internet, muestra el diagrama del Colab y calcula en la pizarra. La slide 9 es la revelación «tus pesos vs. los de la computadora» para el cierre.
- El ticket está **en el propio Colab** (4 preguntas A–D; respuestas correctas **B, D, A, C**). El `Ticket de Salida.pptx` es **solo local**: no se sube antes de dictar la clase.
- Si el tiempo apremia: el **Ejercicio 3** y el **4 (desafío)** pasan a tarea; el 0a, el 1 y el 2 alcanzan para consolidar.
- El `Solucionario.ipynb` tiene todo el código ejecutable. **No lo subas a Classroom antes de dictar la clase.**
