# Historial — Clase 20

## 2026-07-28 — Especificación aprobada
- Objetivo: Construir programas con ciclos `for` anidados que generen tablas y patrones organizados en filas y columnas, con orden.
- Alcance recortado en el diseño: la clase pasó de cubrir continue + break + for anidado a enfocarse 100% en for anidado. Continue y break quedan pendientes para una clase futura, sin fecha ni número asignado, anotados como recordatorio sin urgencia.
- Actitud "Orden" elegida entre 4 opciones (Orden, Precisión, Paciencia, Método).
- Propósito acortado a pedido de Diego: solo definición de la actitud + conexión con el contenido de hoy (sin la frase de proyección "más allá del liceo" del formato canónico).
- Ticket de Salida cambiado de conteo de dedos a alternativas A/B/C/D — cambio de convención permanente, actualizado en `CLAUDE.md` regla 17.
- Estructura aprobada en varias iteraciones (objetivo/actitud, propósito, alcance, estructura de 5 pasos, formato del Ticket de Salida).

## 2026-07-29 — Colab de clase revisado (iteración sobre el aprobado)
- **Motivo:** el Haz Ahora original tenía una sola actividad abierta (sin preguntas numeradas) y, por un bug del generador, la nota interna `Propósito:` (sin negrita) no se filtró y quedó expuesta en el notebook de estudiante. Además el piso hardcodeado de 3 en "Mis respuestas" no calzaba con la cantidad real de preguntas.
- **Haz Ahora:** reescrito con narrativa del Cinemark del Mall Plaza Oeste (equipo de aseo revisando butacas) + 3 preguntas cerradas y concretas (qué asiento sigue, cuántos asientos en total, cuántas veces se reinicia el conteo). Incluye el gancho "el equipo del cine, sabiendo de sus habilidades de programación, les pide ayuda... pero antes de escribir código, quiere que primero tengan clara la lógica".
- **Práctica Guiada:** dejó el escenario de "talleres extraprogramáticos" y pasó a compartir el mismo escenario Cinemark del Haz Ahora (automatizar la lista de revisión de asientos), en el formato canónico de ejercicio (narrativa + "El programa debe" + resultado esperado) en vez de la tabla de pasos de 2 columnas.
- **Práctica Independiente:** los 2 ejercicios (torneo de tenis de mesa, tablero de ajedrez) pasaron de "1 obligatorio + 1 bonus" a **ambos obligatorios**, mismo formato canónico. El Ejercicio 2 (ajedrez) agregó una pista `<details>` explicando el operador módulo (antes solo aparecía en la versión bonus).
- **Ticket de Salida:** pasó de 2 a 3 preguntas fijas (nuevo default de ahora en adelante), cada una con un bloque de código breve (como foco o como referencia) aludiendo a la pregunta, y las respuestas correctas repartidas en letras distintas (A, C, D) para no clusterizarlas todas en una misma alternativa.
- **Bugs corregidos en `crear_colab.py`:** filtro de "Propósito:"/"Actividad:" ahora acepta con o sin negrita; el piso de `num_items` en el Haz Ahora pasó de forzar mínimo 3 a usar el conteo real (fallback 1 si no detecta ninguna). Se implementó de verdad el render del formato canónico ("El programa debe" + pistas `<details>` + resultado) para Guiada e Independiente — antes solo estaba documentado en el SKILL.md pero no codificado. El Ticket de Salida ahora soporta un bloque de código opcional por pregunta (solo se renderiza en `Solucionario.ipynb`, nunca en `Clase.ipynb`).
- Regenerado con `crear_colab.py`, ejecutado con `jupyter nbconvert --execute` sin errores, outputs verificados manualmente contra lo esperado.
- **Este cambio se guardó también al workflow** (ver `CLAUDE.md` raíz reglas 9, 15, 16, 17, 20 y las skills `disenar-clase`/`generar-colab-clase`), como nuevo default para todas las clases futuras.
- **Ajuste posterior (mismo día):** el "Resultado esperado" de Guiada e Independiente todavía se veía como bloque de código markdown plano, sin el lenguaje visual (ícono 📤 + `<em>` + `<pre>`) que usa `Clase 19 - Evaluación Condicionales - Evaluación.ipynb`. Corregido en `crear_colab.py` para que ambas secciones rendericen igual que las evaluaciones; además se agregó el emoji 🎯 al encabezado de cada ejercicio, mismo detalle visual que la evaluación.

## 2026-08-02 — PPT de clase y PPT del Ticket de Salida generados

Clase se dicta el jueves 2026-08-06. Se ejecutó `PLAN-Reparacion-C16-C20.md`: el diseño de esta clase ya estaba al día desde la revisión del 2026-07-29, faltaba solo producción.

- Generado `Presentación.pptx` (10 slides con `crear_ppt.py`): portada, objetivo/propósito/reglas, Haz Ahora, los 4 conceptos del ICN completos (ciclo `for` anidado, filas y columnas, sangría de dos niveles, construir la salida por fila), resumen de conceptos, errores típicos y Cierre. Sin warnings de layout (no hizo falta acortar texto del spec). Termina en el slide de Cierre — Guiada, Independiente y Ticket de Salida no van en este PPT (regla CLAUDE.md 10).
- Generado `Ticket de Salida.pptx` (8 slides con `crear_ppt_ticket.py`): portada + 3 preguntas + slide del Formulario + 3 revisiones. Respuestas confirmadas A/C/D, coincidiendo con `Ticket de Salida Respuestas.json` (ya existente).
- `Solucionario.ipynb`: aviso "el Ticket de Salida se proyecta en clase y se responde a viva voz" corregido a "se responde vía Google Form".
- `Prompt.md`: título corregido de "continue, break, for anidado" a "For Anidado" (el alcance se recortó en el diseño del 2026-07-28); estado actualizado — ya no dice "Planificada — sin spec aún".
- `Spec.md`: agregada sección `## OAs MINEDUC` (OA1, OA3) entre Propósito y Estructura; agregado campo `- **Tema breve (Form):** for avanzado` en Contexto, para que el PPT del Ticket muestre exactamente el mismo string que ya usan el Colab de estudiante y el JSON (antes el PPT habría mostrado "For Anidado", el título de la clase, en vez del tema real del Form).
- **Reel:** declinado — Diego decidió no generar Reel para esta clase.
- **Ejercicios.ipynb:** no se genera para esta clase — la Ayudantía N°21 (2026-08-10) reemplaza esta pieza, igual que ya estaba decidido para Clase 16 (ver `Historial-Curricular.md`).
- Clase queda ✅ completa para dictarse el jueves 2026-08-06.

## 2026-08-04 — Autochequeo agregado a Práctica Independiente

Mismo pedido y mismo diseño que en Clase 16 (ver esa Historial para el contexto completo de la decisión): una sola celda de configuración compartida al inicio de la sección, checker sin argumentos que lee variables del estudiante por nombre exacto, sin listas ni concatenación de strings (todavía no vistas a esta altura del curso).

- Como ninguno de los dos ejercicios usa `input()` (parámetros fijos: 5 rondas, tablero 8×8), no hay "corridas" distintas que acumular — el checker hace varios chequeos puntuales en la única ejecución: 3 en Torneo (total de partidos, suma de rondas, suma de partidos) y 6 en Tablero (claras, oscuras, suma de filas, suma de columnas, total, y la casilla fila 1/columna 1).
- **Punto ciego encontrado y corregido antes de cerrar:** los primeros 4 chequeos del Tablero no detectaban invertir la condición par/impar (`!=` en vez de `==`), porque en un tablero 8×8 simétrico el conteo de claras/oscuras da 32/32 en ambos sentidos — el error pasaba piola. Se agregó `primera_casilla_es_clara`, un chequeo puntual sobre la casilla (1,1), que sí lo detecta. Probado con la solución correcta y con el bug deliberadamente introducido antes de dar el diseño por bueno.
- Regeneración con `crear_colab.py` verificada cell por cell contra la versión previa en git: sin ediciones manuales post-generación pendientes en esta clase (a diferencia de Clase 16), así que no hubo nada que restaurar aparte de la frase por defecto "Resuelve los siguientes ejercicios en pareja..." de la intro de Independiente, que se agregó de vuelta al spec junto con la nueva oración del autochequeo.
- Verificado con `nbconvert --execute` (Clase.ipynb y Solucionario.ipynb, sin errores).

## 2026-08-04 — Corrección: la nota de nombres de variable del autochequeo se perdía en silencio

Mismo hallazgo que en Clase 16 (ver esa Historial para el detalle completo del bug y del fix). Aquí el síntoma era más acotado: la tabla/bloque de "Resultado esperado" de ambos ejercicios sí se mostraba bien (esta clase no usa `input()`, así que ya traía la etiqueta `**Resultado esperado:**` desde el diseño original), pero la nota `> Los nombres de variable exactos son obligatorios...` quedaba atrapada entre los bullets de "El programa debe" y esa etiqueta — el parser de `crear_colab.py` solo conserva las líneas que empiezan con `-` dentro de ese bloque, así que la nota se descartaba sin avisar.

- Migrada a la nueva directiva `**Nota:**` (agregada a `crear_colab.py` en esta misma sesión, ver `generar-colab-clase/SKILL.md`), que ahora sí se renderiza en el notebook.
- Se sacó `(obligatorio)` de ambos títulos de Independiente (redundante con la regla 16 del `CLAUDE.md`) y "en pareja" de la intro de la sección (Diego decide la modalidad de trabajo en vivo, no la quiere fija en el notebook) — este segundo cambio también se hizo permanente en el texto por defecto de `crear_colab.py` (`generar_seccion_independiente_intro`).
- Se agregó un comentario aclaratorio arriba de cada `verificar_ejercicio_N()` (`# Ejecuta esto para revisar tu Ejercicio N — puedes correrlo las veces que quieras`).
- Sin ediciones manuales post-generación que restaurar en esta clase (a diferencia de Clase 16) — la regeneración fue directa.
- Verificado con `nbconvert --execute` (Clase.ipynb y Solucionario.ipynb, sin errores) y confirmado por grep que la Nota ahora sí aparece en el notebook de estudiante.

## 2026-08-05 — Versión v2 (enunciados acotados) generada en paralelo, sin sobreescribir v1

Diego pidió una versión con enunciados más cortos para clases de martes/jueves (el formato extenso de v1 sirve para las ayudantías de los lunes, pero en 80 min no alcanzaba para los dos ejercicios de Independiente), además de arreglar el mensaje confuso del autochequeo que vio en Clase 16 (`Casos distintos superados: 1 / 5` en una respuesta correcta). Al investigar, ambos pedidos resultaron ser el mismo problema: el verificador leía variables del estudiante por nombre exacto desde `globals()`, lo que obligaba a dictar 6-7 nombres de variable por ejercicio (55-57% de los bullets de Independiente en v1) y, sin poder re-ejecutar el código del estudiante, impedía cerrar un contador real en una sola corrida.

**Se generó una v2 completa en `v2-acotada/` (Spec + Clase.ipynb + Solucionario.ipynb), sin tocar ningún archivo de v1.** Pendiente de que Diego la revise en Colab antes de promoverla sobre la v1 actual.

- **Verificador rediseñado — compara la salida impresa, no variables internas.** Ubica la celda de solución del estudiante en el historial `In` de IPython (por el comentario de su primera línea, `# Tu solución — Ejercicio N`), la vuelve a ejecutar con `exec` + `redirect_stdout`, y compara su salida línea por línea contra el resultado esperado (normalizando tildes/mayúsculas/espacios, pero preservando números y orden). Ya no se necesita ningún nombre de variable en el enunciado — la excepción a la regla 8 del `CLAUDE.md` que traía v1 deja de ser necesaria.
- **Cierra solo el punto ciego del tablero simétrico** que v1 necesitó un chequeo puntual extra (`primera_casilla_es_clara`) para tapar: al comparar el patrón línea por línea, invertir la paridad se detecta en la primera fila sin ningún chequeo adicional.
- **Probado con 8 casos** en un notebook de prueba aparte (no ejecutable desde `nbconvert` solo, porque simula la reejecución de celdas vía `In`): las 3 soluciones oficiales dan veredicto completo y honesto en una sola corrida (15/15, 8/8, 4/4); celda vacía da ⬜ sin alarmar; bug de rango y paridad invertida se detectan en la línea 1 con esperada/obtenida; código que lanza excepción da mensaje amigable sin traceback; una variante con nombres de variable y espaciado distintos sigue dando ✅ (la normalización tolera diferencias cosméticas sin perder precisión numérica).
- **Enunciados recortados** (mismo método de conteo antes/después): Guiada 96→83 palabras, Ejercicio 1 (torneo) 227→79 (-65%), Ejercicio 2 (ajedrez) 339→133 (-61%). Desaparecieron los bullets de contadores/sumas y la `Nota:` de nombres exactos en ambos ejercicios.
- **Ejercicio 3 (desafío) agregado**, a pedido de Diego: mismo escenario Cinemark del Haz Ahora/Guiada, recorrido en zigzag (`for` anidado + `if` + `range()` con paso negativo, ya visto en Clase 16). No obligatorio.
- Tiempos ajustados dentro de la sección: Guiada 22→20 min, Independiente 16→18 min. Haz Ahora, ICN, Ticket de Salida y Cierre quedan idénticos a v1 — el PPT no requiere regeneración.
- Verificado con `nbconvert --execute` sobre `Clase.ipynb` y `Solucionario.ipynb` (sin errores) y por grep que el notebook de estudiante no filtra ninguna solución ni ninguna `Nota:` de nombres de variable.
- **Alcance:** solo Clase 20. Clase 16 (ya dictada) no se toca — el `1 / 5` de su Historial queda anotado como pendiente para cuando se retome esa clase.

**Ajuste tras revisión de Diego (mismo día):**
- Bajada de Práctica Independiente reformateada de párrafo a bullets, agregando un punto nuevo que destaca que el verificador ya no exige nombres de variable específicos (a diferencia de v1).
- Enunciado del Ejercicio 3 (desafío) extendido: retoma explícitamente al equipo de aseo y al supervisor del Cinemark, explicando el porqué del zigzag (evitar volver caminando), en vez de la versión más telegráfica de la primera pasada.
- Regenerado con `crear_colab.py`, reverificado con `nbconvert --execute` (ambos notebooks, sin errores) y por grep que no hay fugas de nombres de variable ni soluciones en el notebook de estudiante.

**Segundo ajuste tras revisión de Diego (mismo día): Ticket de Salida — Pregunta 3 reemplazada y Pregunta 4 agregada.**
- Diego no quiso la Pregunta 3 original ("si eliminas esta línea marcada, ¿qué cambia?") por ser muy particular/puntual — pidió una alternativa más aplicada a "qué imprimirá", con varias opciones para elegir.
- Se propusieron 4 diseños (tabla simple, misma idea con `end=`/`print()` pero en formato de predicción completa, patrón triangular del torneo, conteo de ejecuciones) — eligió la tabla 2×3 simple.
- De paso, aclaró que el Ticket ya tenía 3 preguntas (no 2 como había dicho) y pidió subir a **4 preguntas, solo para esta clase** (excepción puntual a la regla 17 del `CLAUDE.md`, que sigue fija en 3 para el resto de las clases).
- La 4ª pregunta nueva reutiliza el concepto de `end=" "` + `print()` vacío (Concepto 4 del ICN) que la Pregunta 3 original cubría, pero en formato "¿qué imprime?" en vez de "qué pasa si borro esta línea" — así no se pierde cobertura de ese concepto.
- Respuestas correctas repartidas en las 4 letras: P1=A, P2=C, P3=B, P4=D.
- Regenerado `Clase.ipynb` + `Solucionario.ipynb` + `Ticket de Salida Respuestas.json` (ahora con las 4 casillas llenas, ninguna "No se preguntó"). Reverificado con `nbconvert --execute` y por grep que no hay fugas.
- Generado `Ticket de Salida.pptx` con `crear_ppt_ticket.py` (soporta cantidad variable de preguntas sin cambios de código): 10 slides (portada + 4 preguntas + formulario + 4 revisiones). Verificado el texto de cada slide con python-pptx — el intro de la portada ajusta solo el conteo ("Son 4 preguntas").
- `python-pptx` no estaba instalado en este entorno; se instaló (`pip install python-pptx`), ya documentado como dependencia estándar del workspace en el `CLAUDE.md` raíz.

**Tercer ajuste (mismo día): Pregunta 4 rediseñada — sin `end=""`/`print()`.**
- La primera versión de la Pregunta 4 reutilizaba el código exacto del Concepto 4 del ICN (`end=" "` + `print()` vacío). Diego la rechazó: no piensa enseñar/enfatizar ese mecanismo lo suficiente como para evaluarlo en el Ticket, aunque aparezca como ejemplo en el ICN.
- Reemplazada por el patrón de rango interno dependiente de la variable externa (mismo tipo de lógica del Ejercicio 1 del torneo, con otro contexto — semanas/sesiones en vez de rondas/partidos — para no ser memorización literal). Respuesta correcta: D (mantiene el reparto A/C/B/D entre las 4 preguntas).
- Regenerado `Clase.ipynb` + `Solucionario.ipynb` + `Ticket de Salida Respuestas.json`, reverificado con `nbconvert --execute` y por grep que no hay fugas.
- Regenerado `Ticket de Salida.pptx` (10 slides), verificado el texto de las slides 4 (pregunta) y 9 (revisión) con python-pptx. `Presentación.pptx` **no se tocó** — Diego pidió explícitamente no modificarla en esta iteración.
