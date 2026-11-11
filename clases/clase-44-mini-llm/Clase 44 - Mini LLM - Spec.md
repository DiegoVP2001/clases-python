# Clase 44 — Cómo funciona ChatGPT: modelo de lenguaje, tokens y probabilidades

**Estado:** Spec v2 aprobada por Diego (2026-11-11), con ajustes del mismo día: (1) LLM = *Large Language Model* explicado en el concepto 1; (2) **se eliminó** la sección «Lo que debes saber responder en la Prueba» (con lo que se responde en clase ya queda claro qué aprender); (3) «Verificamos lo aprendido» con **al menos una pregunta por concepto** (2 por concepto en el Colab); (4) la práctica guiada es **réplica de la Parte D de la Prueba 1** (texto + regla + D1/D2/D3, se responde a mano y luego se comprueba ejecutando celdas), con el texto «hoy toca mate…» (D1: `toca` → `mate`, 2 de 3; D2: `hoy` → `toca`, 3 de 4; D3: `feriado` nunca apareció); (5) slides con animaciones por concepto (LLM que aprende, tijera que corta tokens, conteo paso a paso, ruleta probabilística); (6) Ticket de Salida de **4 preguntas, una por concepto**; (9) **v4 (2026-11-11): el ICN pasa a 4 conceptos con más bullets, el concepto 3 trae una bajada («las respuestas de un LLM son azarosas; el proceso para verlo es…»), la actividad con ChatGPT es el concepto 4 «Evidenciarlo en la práctica» y se descartó el interactivo final**; (8) **v3 (2026-11-11): conceptos 3 y 4 fusionados en «Probabilidad y azar: la bolsa de fichas»**, interactivo final «La bolsa de fichas» y palabra nunca vista = saca al azar entre las que sí conoce; LLM definido como estocástico desde el concepto 1; (7) **terminología (Diego, 2026-11-11): «estocástico», no «probabilístico»**, y no se separa el mini modelo («determinístico») del LLM real: **todo lo de la clase es estocástico** (sistema cuyo comportamiento no se puede predecir con total exactitud; o sea, tiene azar). «Determinístico» solo aparece como contraste con la calculadora.
**Clase Picuino:** N/A — fila de IA (calendario v6) · **Fecha:** lun 16-nov-2026 · **Curso:** 3ro medio · **Duración:** 80 min
**Flujo:** liviano (Spec → Colab + Solucionario + Guía Docente Voz + slides + Ticket al Form → gate → push de la carpeta; el `Ticket de Salida.pptx` NO se pushea antes de dictar).
**Modalidad:** no se menciona en ningún material; la anuncia Diego.
**Regla de la clase (Diego):** foco en **comprender conceptos**. Los estudiantes **no programan nada**: solo ejecutan celdas ya escritas y leen su salida. Cambiar el texto base queda como extra opcional.

## Objetivo
Comprender con curiosidad cómo funciona ChatGPT: qué es un modelo de lenguaje, qué son los tokens y por qué predice la siguiente palabra con probabilidades.

**OAs:** OA1, OA3 (por confirmar). **Actitud: Curiosidad** (Diego, 2026-11-11): abrir la caja de ChatGPT y descubrir que por dentro predice la siguiente palabra.

## ¿Por qué lo veremos?
El teclado que te sugiere la siguiente palabra en WhatsApp y ChatGPT hacen lo mismo en el fondo: predecir qué palabra viene. Entender cómo lo hacen explica por qué ChatGPT puede responder distinto a la misma pregunta.

## Vocabulario que se usa en toda la clase (Diego)
- **Determinístico:** misma entrada → **siempre** la misma salida (como una calculadora: 7 × 8 siempre da 56).
- **Probabilístico:** misma entrada → la salida **puede variar**, porque se elige entre varias opciones según su probabilidad.
- **Estocástico:** sistema cuyo comportamiento **no se puede predecir con total exactitud**; o sea, tiene azar. **Lo son el LLM gigante y también nuestro modelo chiquito** (no se separa «chiquito = determinístico»). Se enfatiza en el Colab, las slides, la Guía y el Ticket (aviso en el concepto 1, desarrollo en los conceptos 3 y 4, resumen y cierre).
- **Determinístico** solo como **contraste** con la calculadora (7 × 8 siempre da 56).
- «La más probable» **no es** «la segura»: tras `en` viene `el` 2 de 3 veces, pero 1 de 3 viene `la`.

## Textos de la clase (verificados por script, sin empates)
Escenario: **el teclado del celular sugiriendo palabras en el chat del curso**. Personaje: quien programa el teclado. El texto cargado en el Colab es nuestra «base de datos» de juguete.

- **ICN (patio):** `nos vemos en el patio . nos vemos en el patio . nos vemos en la plaza . ya llegué al casino .` Tras `en` → `el` (2 de 3); tras `nos` → `vemos` (3 de 3); tras `el` → `patio` (2 de 2). Palabra nunca vista: `biblioteca`.
- **Práctica guiada · réplica de la Parte D (horario):** `hoy toca mate . hoy toca mate . hoy hay prueba . hoy toca inglés .` D1: tras `toca` → `mate` (2 de 3); D2: tras `hoy` → `toca` (3 de 4 = 75 %); D3: `feriado` nunca apareció. Mismo formato que la prueba (texto + regla + D1/D2/D3), se responde **a mano** y luego se comprueba ejecutando celdas.
- **Ticket (recreo):** `voy al kiosco . voy al kiosco . voy al baño . voy a clases .` Tras `voy` → `al` (3 de 4); tras `al` → `kiosco` (2 de 3).
- El `.` cuenta como una palabra (igual que en la prueba).

## Mapa de tiempos (80 min)
Bienvenida 5 (colega) · Haz Ahora 7 · Puente 3 · ICN 35 (incluye el prompt en vivo) · Leer y responder 15 · Ticket 5 · Cierre 5 (≈75). Extras sin tiempo.

## Estructura

### Haz Ahora (colega como quien programa el teclado, sin código)
Contexto: el teclado sugiere la siguiente palabra y quiere aprenderlo del chat del curso. Se muestra un chat corto de 3 mensajes (distinto del texto de la clase). Preguntas cerradas:
1. Si escribes «nos», ¿qué palabra sugerirías y por qué?
2. En ese chat, ¿cuántas veces aparece «en»?
3. De esas veces, ¿cuántas veces la palabra que sigue es «el»?
4. Una calculadora, ¿te da siempre el mismo resultado para 7 × 8? Y un amigo al que le pides recomendar una película, ¿te recomienda siempre la misma? (spoiler sutil de determinístico vs. probabilístico, sin nombrarlos)

### Recordatorio puente
🔁 Ayer: la neurona pondera columnas con números · 🔀 Hoy es distinto: ya no hay columnas ni números, hay **texto**, y el modelo predice **la siguiente palabra** · ➡️ La próxima clase (lun 23, **después de la Prueba 1 del jueves 19**): prompting, cómo pedirle bien las cosas a ChatGPT.

### ICN (4 conceptos, v4: probabilidad y azar fusionados + evidencia en la práctica; todos con celdas ya escritas: solo se ejecutan y se lee la salida)
Imagen única de la clase: la **bolsa de fichas** (probabilidad = proporción de fichas; el modelo **saca una ficha al azar**).
0. **🔧 Ejecuta esta celda primero:** carga las funciones (`mostrar_probabilidades`, `sacar_fichas`, `generar_varias`, `ver_tokens`…) y el **texto base**. Sin librerías externas.
1. **¿Qué es un LLM?** **LLM = Large Language Model** (large = grande, language = lenguaje, model = modelo): aprendió de textos a predecir la siguiente palabra **y es estocástico** (su comportamiento no se puede predecir con total exactitud; tiene azar). El teclado es uno chiquito y ChatGPT uno gigante; **los dos tienen azar**: lo que responden depende del azar y de las probabilidades con que se entrenaron. Celda: muestra el texto base («base de datos»).
2. **Tokens.** Trozos (fichas) que el modelo lee. En el mini modelo, 1 palabra = 1 token (y el `.`); en los modelos grandes se cortan palabras largas o raras (ilustración).
3. **Probabilidad y azar: la bolsa de fichas.** ① Aprender = contar: la bolsa de `en` tiene 2 fichas `el` y 1 `la`. ② Probabilidad = proporción de fichas (2 de 3 ≈ 67 %, 1 de 3 ≈ 33 %). ③ Azar = el modelo saca una ficha sin mirar: `el` sale más seguido pero **no siempre**; por eso es estocástico y lo que responde depende de las probabilidades con que se entrenó. ④ **Palabra que nunca vio** (`biblioteca`): no tiene bolsa propia, pero **no se queda callado: saca una ficha al azar entre las palabras que sí conoce** (cualquier cosa, sin base). 📝 La regla de las pruebas («la que más veces la siguió») es la ficha más grande: la más probable, **no la segura**. Celdas: `mostrar_probabilidades`, `sacar_fichas(…, "en", 10)` (varía en cada ejecución), `biblioteca`, `generar_varias`.
4. **Evidenciarlo en la práctica: ChatGPT también es azaroso.** Concepto simple: el profesor envía **dos veces**, en conversaciones nuevas, «Explica las diferencias entre ChatGPT, Claude y Gemini»; el curso anota qué cambió, qué se mantuvo y por qué, con citas y usando «estocástico» (ensayo de la Prueba 2 · Parte B). Aviso: las respuestas pueden traer datos desactualizados o erróneos.
- **Verificamos lo aprendido:** bloque de 2-3 preguntas después de cada concepto (6-7 en total); respuestas en el Solucionario.
- **Resumen tabla (ICN):** LLM (estocástico) · Token · Bolsa y probabilidad · Estocástico · Palabra nunca vista · Determinístico (solo como contraste con la calculadora).
- **Errores típicos:** olvidar el `.` · dar la palabra sin la proporción · usar el largo del texto como total · creer que ante una palabra nueva el modelo «no responde» · creer que ChatGPT siempre dice la más probable · creer que el chiquito es «exacto» y el gigante tiene azar.

### Práctica guiada · réplica de la Parte D (15 min; reemplaza a la guiada)
Réplica de lo que se pregunta en la Prueba 1 · Parte D, con otro texto. Narrativa: el teclado aprende del chat donde el curso anota qué toca cada día. Se muestra el texto y la regla («después de una palabra, predice la que más veces la siguió») y se responde **a mano, por escrito**: **D1** qué predice tras `toca` y en cuántas de las veces; **D2** qué predice tras `hoy` y con qué proporción; **D3** `feriado` no aparece: ¿puede responder? sí/no y por qué. **Después** ejecutan celdas ya escritas para **comprobar**. No programan. Pistas 1–2 en `<details>`. Las respuestas modelo viven solo en el Solucionario. Revisión a viva voz con una pareja al frente.

### Extras (sin tiempo, con pistas)
0a cambiar una palabra del texto base (opcional) y anticipar la nueva predicción · 1 texto de otro contexto (recreo) con las mismas 3 preguntas · 2 desafío: generar 5 frases desde el mismo inicio y contar cuántas salen distintas.

### Ticket de Salida (Form + PPT local)
Colab: solo el link `https://forms.gle/sjRpbgmQzrpkEBsH9` y el tema «Mini modelo de lenguaje». 3 preguntas A–D con respuestas en letras distintas, con bloque de texto breve (recreo): (1) qué predice tras `voy` y con qué proporción (`al`, 3 de 4); (2) qué es un token; (3) por qué ChatGPT puede responder distinto a la misma pregunta (estocástico). + autoevaluación 1–5 (solo en el Form, no se proyecta). Genera `Ticket de Salida Respuestas.json`.

### Cierre (a viva voz)
Comprensión 1–5; «¿Qué te dio curiosidad de cómo funciona ChatGPT por dentro?»; **aviso del repaso** de la Prueba 1 (jueves 19; la Parte D es esta clase).

## Colega (detalle en la Guía Docente Voz)
Solo habla cuando Diego la activa: bienvenida, Haz Ahora como quien programa el teclado, verificación tras el concepto 4 («¿qué significa que ChatGPT sea estocástico? ¿lo es también el modelo chiquito?»). Nunca protagonista en la práctica ni el cierre. No inventa datos ni cifras.

## Slides animadas — `sitio-hub/clase-44/`
Haz Ahora (pregunta + chat + calculadora vs. amigo) · una slide por concepto 1–4 (1: texto base como «base de datos»; 2: **tokens**, una palabra que se parte en trozos; 3: conteo animado y barras de probabilidad + palabra no vista; 4: **«dado» que sortea** y da dos frases distintas, y contraste **determinístico vs. probabilístico**) · **«🎯 Para la prueba»** (los 4 tipos con respuesta modelo) · «Para pensar» (¿por qué ChatGPT cambió?) · resumen en viñetas. Etiqueta «Concepto N del cuaderno». Generadas con `construir_slides.py` (modelo: 42b).
