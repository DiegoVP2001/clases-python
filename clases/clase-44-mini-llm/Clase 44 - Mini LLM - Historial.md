# Clase 44 — Cómo funciona ChatGPT · Historial

Registro de iteraciones y feedback de Diego (todo el 2026-11-11, salvo indicación).

## Diseño
- **Spec v1:** mini LLM contando a mano (escenario: teclado del celular; actitud: curiosidad).
- **Feedback:** enfocar en **comprender conceptos** (LLM, tokens, probabilidades, código de ejemplo con el texto como «base de datos») y **no programar** (solo ejecutar celdas) → **Spec v2 aprobada**.
- La actividad de comparar dos respuestas pasó a ser **un prompt real en vivo** («Explica las diferencias entre ChatGPT, Claude y Gemini») enviado dos veces por el profesor.

## Colab, Solucionario, slides y Ticket
1. Primera versión generada (4 conceptos; Ticket de 4 preguntas, una por concepto).
2. Feedback: agregar qué significa **LLM en inglés**; slides con **animaciones bonitas por concepto**; **«Verificamos lo aprendido»** con al menos una pregunta por concepto; **quitar «Lo que debes saber para la prueba»**; práctica guiada como **réplica de la Parte D** (texto «hoy toca mate…»).
3. Feedback de terminología: **«estocástico», no «probabilístico»**; no separar el mini modelo («determinístico») del LLM real; todo es azaroso.
4. Propuesta aceptada: **fusionar** probabilidad y azar con la imagen de la **bolsa de fichas**; **palabra nunca vista = saca una ficha al azar entre las palabras que sí conoce**; lo que responde depende de las probabilidades con que se entrenó; LLM definido como estocástico desde el concepto 1; interactivo final (luego **descartado**).
5. Feedback final: bajada en el concepto 3; **más bullets** en 1, 2 y 3; **ChatGPT como concepto 4 «Evidenciarlo en la práctica»**; **quitar referencias a la prueba y «Cómo contar a mano»** del Colab.
6. **Aprobada** por Diego («con eso cerramos»).

## Alineación con las pruebas (no se pushean hasta después de rendidas)
- Prueba 1 · Parte D: D3 acepta «sí, pero al azar, sin base»; nota de alineación con esta clase.
- Prueba 2 · Parte B: rúbrica B2 y Temario con «estocástico».
- Prompts de las clases 46 y 48 con el vocabulario de la 44.

## Pendientes
- Guía Docente Voz (el colega del profesor) y confirmar OAs (OA1, OA3).
- `Ticket de Salida.pptx` solo local: subir después de dictar la clase (lun 16-nov).
