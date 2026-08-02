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
