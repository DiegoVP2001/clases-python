# Clase 42b — De la tabla a las listas · Historial

## 2026-11-07 — Entrevista y diseño

- **Origen:** Diego notó que en la N°42 el curso entendió crear → entrenar → evaluar, pero **no qué significa cada coma dentro de un corchete ni cada grupo de corchetes**. Además, la N°43 (neurona v1) partía ajustando pesos a mano, y quiere que la computadora aprenda sola. El jueves 12-nov no hay clase, así que se corrió el calendario (v5). Plan completo: `C:\Users\diego\.claude\plans\necsito-hacer-una-o-vast-mochi.md`.
- **Decisiones de Diego:** una sola clase nueva (42b) antes de la neurona; listas **a mano**, enfoque intuitivo (sin índices anidados, `for`/`append` ni *slicing*); elegir 3 de 6 columnas con criterio; split **80/20 = 16 train + 4 test** (nombres en inglés); sin ajuste manual de pesos; slides animadas en Vercel en cada clase; 2 pruebas de 60 min.
- **Contexto:** el wifi del liceo (reemplaza a la micro de la N°42, para no repetir el criterio de la clase pasada). **Actitud: Atención.** Objetivo: «Convertir una tabla de datos en listas de entradas y etiquetas para entrenar y evaluar un modelo con atención.» OA1, OA3 confirmados.
- **Datos:** 20 bloques × 6 columnas (3 claras, 2 medias —`temperatura_sala` y `hora_del_bloque`—, 1 sin relación —`dia_del_mes`—). Verificados con scikit-learn 1.9 (semilla 16393): el trío sensato acierta 4/4 en el test y tiene 0,90 de validación cruzada (el mejor de los 20 tríos); el árbol con las 6 columnas usa solo las 3 claras. Corrección de realismo: en una primera versión había más estudiantes viendo video que dispositivos conectados; se arregló y se repitió la búsqueda.
- **Feedback de Diego sobre la spec v1 → v2:** volver a `temperatura_sala` (era mejor que `docentes_en_videollamada`); el tipeo completo va **en el ICN**; la **guiada es el ejercicio obligatorio** y el resto son extras; nuevo objetivo; la tabla **no marca** las últimas 4 filas como test y va precedida de un **diagrama del 80/20**.

## 2026-11-07 — Colab, Solucionario, Guía del colega y slides generados (a la espera del gate 2)

- `generar_clase.py` crea `Clase.ipynb` (61 celdas) y `Solucionario.ipynb`; los resultados esperados se calculan ejecutando las soluciones. `diagramas/construir_diagrama.py` genera `split_80_20.png` (incrustado en el Colab). Datos en `datos_wifi_verificados.json` y `datos_extras_verificados.json`.
- **Estructura:** verificador preparado → Haz Ahora → Ayer/Hoy/Mañana → ICN (diagrama 80/20 + tabla de 20 filas + 6 conceptos «Escríbelo tú» + `check_icn()`) → Guiada (el liceo vecino, 10 bloques × 5 columnas, pide las 3 primeras) → Ticket (D, B, C, A) → Cierre → Ejercicios extra (0a, 0b, 1, 2, 3, 4).
- **Verificado:** el Solucionario se ejecutó de arriba abajo con `py -3` sin errores y todos los `check_*()` dan ✅ con las soluciones; `check_ticket()` da 4/4 con D, B, C, A. El cuaderno de estudiantes sin tocar solo falla en el Ejercicio 2 (el `ValueError` es intencional). Verificadores probados con errores típicos: columnas permutadas (se acepta y se informa cuáles usó), dos datos intercambiados en un bloque, etiqueta omitida, etiqueta en otra posición, otras columnas en la guiada, accuracy faltante o errado, etiqueta agregada al final en el Ejercicio 2.
- **Cambio de diseño al verificar:** el desafío (Ejercicio 4) usaba «poner 40» y el accuracy no cambiaba; ahora el dato queda **mal anotado en 100** y el accuracy baja de 1,0 a 0,5 (encaja con la atención y con «4 bloques prueban poco»).
- **Decisión técnica:** `check_icn()` detecta qué trío eligió cada estudiante comparando sus listas con la tabla (en cualquier orden de columnas), sin revelar cuál es el «mejor».
- Pendiente: gate 2 (Diego), commit con pathspec, push, deploy del hub y link de Colab.

## 2026-11-08 — Feedback de Diego sobre el Colab (aplicado, v3)

- **Haz Ahora:** lista los nombres de las 6 columnas (con lo que mide cada una). La **etiqueta** se trabaja ahí: «el encargado nos pregunta ¿se cayó el wifi?; ¿cómo la presentarían con una etiqueta binaria, en código?» → **1 = sí, 0 = no**; el Colab aclara que el 1 es «sí», no «bueno».
- **Elegir las 3 columnas:** sin «Escríbelo tú». La clase ya trae las 3 columnas (dispositivos, video, horas desde el reinicio) en una tabla markdown con la tabla reducida de 20 filas; el estudiante solo escribe una **breve justificación** de por qué esas 3 sí y las otras no. Mensaje: elegir pocas columnas ahorra procesamiento (aquí casi no se nota, pero hay que justificarlo).
- **Todo el ICN con el ejemplo del wifi** (se quitó el ejemplo de `edad`/`estatura`; el bloque 1 `[71, 0, 20]` es el ejemplo y el estudiante escribe el bloque 2). Se **quitó el dictado de datos**.
- **`max_depth` (concepto 5):** «cuánto le dejamos pensar al computador»; con los datos de la clase, profundidad 1 → 2 errores de 16 en el entrenamiento, 2 → 1, 3 → 0, 4 → igual que 3; usamos 3 por ser el menor valor que no empeora los resultados. También se explica `random_state=0`.
- **Concepto 6:** «Accuracy» pasa a **«Revisar»**: leer el árbol con `export_text` y `nombres_variables` (explicando que las columnas que damos al modelo son las *features*, en el mismo orden que en las listas) y después el accuracy.
- **Verificador:** `check_icn()` ahora valida columnas fijas, `nombres_variables` y `exactitud` (probado con: todo correcto, nombres en otro orden, faltantes, otro trío, accuracy errado).
- **Slides:** 11 (antes 8), todas con el wifi y las 3 columnas; nuevas: la pregunta y la etiqueta, de 6 columnas a 3 con justificación, `max_depth` interactivo, leer el árbol siguiendo el camino del bloque 17.
- Decisiones: la etiqueta va en el Haz Ahora y no como concepto numerado (por tiempo); la justificación de columnas es la práctica de «elegir con criterio» (el Ejercicio 3 extra sigue pidiendo elegir); la Prueba 1 no debería pedir elegir columnas desde cero, sino justificar un trío dado.

## 2026-11-08 (2.ª ronda) — Terminología y ajustes de Diego (aplicados)

- **«Bloque» → «fila» / «fila de datos»** en todo el Colab, Solucionario, ticket, verificadores, slides, diagrama del 80/20, spec y guía (el nombre de columna `hora_del_bloque` se mantiene: es un dato de la tabla). Regla guardada para las clases futuras.
- **Haz Ahora (redacción de Diego):** «El encargado registró varios datos en una tabla donde las columnas son … y no sabe cuáles le podrían servir»; P2 «¿cuáles son las 3 que descartaron y por qué?»; P3 «al final de cada registro tiene otra columna, ¿Se cayó el wifi?; ¿cómo representarían esa respuesta con una **etiqueta** binaria, en código?»; P4 «20 filas de datos: ¿cuántas para entrenar y cuántas para probar (testear)?».
- **`max_depth`:** sin tabla ni justificación del 3 en el texto; después del código va un `<details>` oculto «¿Cómo cambian los resultados si variamos max_depth?» (1 o 2 se equivocan en el entrenamiento; 3 acierta todo; 4 o más igual que 3).
- **Concepto 6 «Revisar»:** reducido a «Al revisar hacemos dos cosas»: 1. leer el árbol (`export_text`, con las *features* en el mismo orden) y 2. ver la precisión (`accuracy_score`), cada una con una descripción breve del código.
- **Slides:** cada una lleva la etiqueta «Concepto N del cuaderno» para mostrarlas paso a paso junto al Colab.

## 2026-11-08 (3.ª ronda) — Ticket fuera del Colab (regla permanente de Diego)

- El Colab **ya no trae las preguntas del ticket ni `check_ticket()`**; termina con el link al Google Form y el tema a escribir. Se quitaron del verificador las huellas de respuestas. Regla **siempre**, no solo para esta clase.
- Generados: `Ticket de Salida.pptx` (10 slides, con `crear_ticket_ppt.py` y el generador estándar de la skill `generar-ppt-clase`; **solo local, no se pushea antes de dictar**) y `Ticket de Salida Respuestas.json` (D, B, C, A).
- Nuevo estándar para clases de IA: una slide animada por concepto del ICN, partes del Haz Ahora, «Para pensar» y resumen en viñetas (ya cumplido por la 42b).
- **Cierre de etapa:** gate aprobado por Diego el 2026-11-08; commit + push de la carpeta (sin el `.pptx`) y de `sitio-hub/`.
