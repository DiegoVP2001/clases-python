# Clase 43 — Construir una neurona · Historial

## 2026-11-04 — Spec (iteración en chat)

- Actitud elegida por Diego: **Asombro** («darles harto hype sobre las neuronas»). Historia nueva: **colmenas de un apicultor de Isla de Maipo**. Página: slides + neurona interactiva. Voz: bienvenida, Haz Ahora, retos desafiantes planificados y modo de preguntas abiertas.
- **Feedback de Diego sobre la Spec v1:**
  - El objetivo queda solo como «Crear nuestra primera inteligencia artificial: una neurona, con asombro.»
  - El perceptrón de 1958 «no tiene ningún sentido y es muy out of nowhere»: se quitó junto con el Nobel 2024 y la mosca conectoma.
  - El «¿Por qué lo veremos?» **lo dice la voz de ChatGPT** para asombrar y entusiasmar: los estudiantes construirán los cimientos de lo que ella es.
  - Diagrama simple (datos → neurona → salida) que sea un **espejo de lo que se programa**, bonito y modificable; la página muestra primero el **paso a paso** (cómo se ingresan los inputs, se evalúan y se activa o no la salida) y después el laboratorio dinámico.
  - Diego aprueba la Spec con esos cambios y revisa el resto ya renderizado (Colab + página).
- Interpretación del diagrama: 3 entradas con sus pesos → **1** neurona → salida (no una capa de 3 neuronas), porque en el Colab se programa una sola neurona.

## 2026-11-04 — Colab, Solucionario, Guía de Voz, página y Ticket PPT generados (a la espera del gate 2)

- `generar_clase.py` crea `Clase.ipynb` y `Solucionario.ipynb`; los resultados esperados se calculan ejecutando las soluciones. `diagramas/construir_diagrama.py` dibuja el diagrama PNG incrustado en el Colab (antes del concepto 1).
- **Verificado:** el Solucionario corre de arriba abajo sin errores; `check_ej1/2/3` dan ✅ con la solución y ⚠️ con los errores típicos probados (sin sesgo, `>` en vez de `>=`, función sin `return`, pesos de partida, ajuste que rompe otro día); `check_ticket` 4/4 con B, D, A, C. El Colab de estudiantes no contiene soluciones ni letras del ticket (solo el «3 de 4» del resultado esperado del desafío).
- **Cambios respecto de la Spec aprobada (datos, para que el diseño funcione):**
  - Día 6 de las colmenas: `[26, 6, 4]` (en vez de lluvia 3). Con eso, **cambiar solo el peso del viento a −1 arregla los dos días que fallan** (4 y 6); el peso de la lluvia a −3 arregla solo el día 6. Reemplaza la afirmación de la Spec («cada falla se arregla con un peso distinto»).
  - Guiada del enjambre: pesos de partida `[1, −0.2, 0.5]` (3 de 6); con horas de sol en 2 acierta los 6.
  - Ej. 3 (miel): pesos de partida `[1, 1, −1]` acierta 6 de 7; subir el primer peso a 2 arregla una semana pero **rompe otra** (la semana 5, z = 0); bajar el peso de lluvia a −3 la corrige: enseña que un ajuste puede romper otro día.
  - Naltagua (Ej. 1) incluye 2 días con `z = 0` exacto para detectar `>` en vez de `>=`; se usaron pesos con decimales exactos (0,5; 0,25) para evitar errores de coma flotante.
  - Ej. 4 (desafío): caso «calor o néctar pero no ambos»; entre todas las combinaciones de pesos y sesgo enteros de −3 a 3, el máximo es 3 de 4.
- Autochequeos: el Ej. 1 y 2 prueban la función `neurona` del estudiante; el Ej. 3 lee `pesos` y `sesgo`. Ticket en el Colab con letras como huellas SHA-256 y justificación en base64 (práctica sin nota).
- **Página** `sitio-hub/clase-43/index.html` (8 slides): 1 diagrama · 2 entra un día · 3 dato × peso · 4 suma + sesgo · 5 se evalúa y se activa · 6 los 8 días (6 de 8) · 7 laboratorio con perillas (diagrama, tabla y conteo de aciertos en vivo; con el peso del viento en −1 marca 8 de 8) · 8 escala (cifra del cerebro humano verificada: 86,1 ± 8,1 mil millones, Azevedo et al. 2009). Pestaña «Clase 43» agregada en `clase-42/` y tarjeta en el índice del hub. Probada con capturas de Edge headless; la extensión de Chrome no estaba conectada.
- `Ticket de Salida.pptx` (10 slides) generado con `crear_ticket_ppt.py`; **solo local, no se sube antes de dictar la clase**. Las letras de ejemplo de la slide del Colab son A, B, C, D (no las correctas).
- **OAs propuestos:** OA1, OA3 | OAd (mismos que la N°42). *Pendiente de confirmar por Diego.*
- Pendiente: gate 2 (Diego revisa Colab y página renderizados) → commit con pathspec, push, deploy del hub en Vercel (necesario para el link del Colab), actualizar checklist e `Historial-Curricular.md`.

## 2026-11-04 — Feedback de Diego y Spec/Colab v2 (aplicado)

- **Nombre:** «el colega del profesor» en lugar de «la voz de ChatGPT» (Colab, página, Guía, PPT).
- **Haz Ahora:** enfocado en cómo automatizarían algo que no conocen y qué patrones revisarían (4 preguntas nuevas; la 3 prepara «peso» y la 4 «set de prueba»).
- **Recordatorio puente** ayer → hoy es distinto → próxima clase (con mini-tabla árbol vs. neurona y la frase «árbol = preguntas · neurona = suma de importancias · la próxima clase = la computadora ajusta los números»). Queda como regla de toda clase (`disenar-clase/SKILL.md` + memoria).
- **Error y ajuste manual sin código pesado:** el evaluador (`evaluar_entrenamiento()` / `evaluar_prueba()`) viene preparado; los estudiantes programan la neurona (conceptos 1-3 y Ej. 1-2 y guiada) pero no el recorrido de errores; se evalúa la **justificación** de su mejor resultado (marco de frase).
- **Entrenamiento y prueba** (regla permanente para toda IA que se entrena): 8 + 4 días en las colmenas; 6 + 3 en la guiada; 7 + 3 en la miel; 12 + 4 en el desafío. La prueba se mira una sola vez; el evaluador avisa si se mira dos.
- **Caja lista primero:** el ICN parte con la neurona ya armada para iterar desde el minuto cero y después «abrimos la caja».
- **Desafío (Ej. 4) nuevo:** apiario del cerro, 12 días de entrenamiento con un día raro; el máximo posible es 11 de 12 (verificado por búsqueda y por programación lineal: 12/12 es imposible); `check_ej4()`. El caso «calor o néctar pero no ambos» (una neurona no lo resuelve) sale de la clase; queda como curiosidad para la N°44.
- **Datos finales:** colmenas prueba `[[27,12,0],[18,6,0],[21,10,0],[29,24,0]]` / `[1,0,1,0]`: partida 6/8 y 2/4; a mano `[1,-1,-2],-13` 8/8 y 3/4; computadora `[3,77,-3,83,-9,53],-45,22` 8/8 y 3/4 (falla el mismo día). Guiada: partida 3/6 y 1/3; final `[1,-0.2,2],-29` 6/6 y 3/3. Miel: partida `[1,1,-1],-30` 6/7 y 2/3; subir el primer peso a 2 arregla la semana 6 pero rompe la 5 (z = 0); final `[2,1,-3]` 7/7 y 3/3. Desafío: partida `[1,-0.5,-0.25],-14` 10/12 y 3/4; `[1,-1,-0.25],-14` 11/12 y 4/4.
- **Ticket:** la pregunta 4 pasa a «entrenamiento vs. prueba» (reemplaza la del error); respuestas siguen B, D, A, C.
- **Página:** 10 slides (recordatorio · diagrama · entra un día · dato × peso · suma + sesgo · se evalúa y se activa · los 8 días del entrenamiento · laboratorio con prueba oculta y aviso · tus pesos vs. los de la computadora · escala con la nota de `hidden_layer_sizes`).
- **Calendario v4 (acordado):** 43 el lunes 9-nov; **44 (nueva) el martes 10-nov: la computadora ajusta sola** con `MLPClassifier(hidden_layer_sizes=())` (una sola neurona; se menciona `hidden_layer_sizes` como decisión por prueba y error con sistemas que automatizan la búsqueda, pero seguimos con una); mini-LLM jue 12; evaluaciones siempre los jueves (E1 19, E2 26, E3 3-dic). Detalle en el checklist de traspaso.
- **Verificado:** el Solucionario corre completo; `check_ej1..4` dan ✅ con la solución y ⚠️ con los errores típicos; `check_ticket` 4/4; el Colab de estudiantes no filtra soluciones ni nombra a ChatGPT; capturas de la página con Edge headless (la extensión de Chrome no estaba conectada).
- Pendiente: revisión de Diego (Colab y página ya renderizados), confirmar OAs, commit/push con pathspec y deploy en Vercel.


## 2026-11-04 — Diagrama general («la esencia») en el Colab y en la página

- **Feedback de Diego:** el diagrama del Colab no debe llevar valores de pesos ni sumas o multiplicaciones: solo «peso» y la idea general; los números se muestran recién al final. Pidió que lo mismo se vea la primera vez que aparece el diagrama en la página.
- **Colab:** diagrama nuevo (`diagramas/construir_diagrama.py`): flechas iguales rotuladas «peso», neurona que «decide», salidas «se activa» / «no se activa» (1 = SALEN, 0 = SE QUEDAN); el texto que lo acompaña ya no habla de colores ni de suma.
- **Página:** la slide 2 es general (sin valores, sin colores verde/rojo, sin el bloque `pesos`/`sesgo`); también la slide 3 («Entra un día»), donde solo entra el día. Los valores de los pesos aparecen en la slide 4 («dato × peso») y el sesgo, con `z`, en la 5. El laboratorio y la revelación final conservan los números.

## 2026-11-04 — Gate 2 aprobado y publicación

- Diego revisó Colab y página renderizados («ya perfecto») y pidió montar todo para cerrar.
- Publicado: carpeta `clases/clase-43-neurona/` (sin `Ticket de Salida.pptx`, que se sube después de dictar la clase), `sitio-hub/` (clase-43, pestaña en clase-42 y tarjeta) y los registros del plan; deploy del hub en Vercel (`clases-ia-mario-bertero.vercel.app/clase-43/`).
- OAs propuestos (OA1, OA3 | OAd) sin confirmación explícita de Diego.

