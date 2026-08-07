# Historial — Clase 22

## 2026-08-07 — Especificación aprobada
- Objetivo: Construir programas con ciclos `while` que repitan un proceso hasta cumplir una condición, evitando bucles infinitos, con perseverancia.
- Actitud elegida: Perseverancia (entre 4 opciones ofrecidas: Método, Precisión, Criterio, Perseverancia).
- Ajuste de Diego al objetivo: sacar las menciones literales a "`while True`" y "actualizando bien la variable de control" de la redacción del objetivo.
- Contexto temático propuesto por Diego: "algo para nuestro liceo, como que la directora Rossana nos pide" — se ancló en el Liceo Bicentenario Mario Bertero Cevasco y la directora Rossana (real, vía `referencia-isla-de-maipo`). Escenario compartido Haz Ahora + Guiada: buzón de sugerencias del Centro de Estudiantes. Independiente: aforo del gimnasio, cupos de taller de fotografía, desafío de préstamo de notebooks.
- Corrección de nombre: siempre "directora Rossana", nunca solo "Rossana".
- Ejercicio 2 de la Independiente alargado (60 → 73 palabras) para sacar una frase demasiado directa que adelantaba la tarea antes de la sección "El programa debe".
- Estructura aprobada en una sola iteración de ajustes menores (objetivo, nombre de personaje, largo del Ejercicio 2).

## 2026-08-07 — Colab de clase aprobado
- Archivos: `Clase 22 - While - Clase.ipynb`, `Clase 22 - While - Solucionario.ipynb`, `Clase 22 - While - Ticket de Salida Respuestas.json`.
- Generados con la skill `generar-colab-clase` a partir del spec aprobado.
- Verificación de código: como los ejemplos del ICN (Concepto 2 y 3) y todos los ejercicios usan `input()`, y el Concepto 4 es un bucle infinito intencional, `nbconvert --execute` no sirve para el notebook completo (falla con `StdinNotImplementedError` en las celdas con `input()`). Se verificó cada snippet manualmente con `input()` simulado (mock de stdin) contra los resultados esperados del spec — Guiada, Ejercicios 1-3 y las 3 preguntas del Ticket coinciden exactamente. El Concepto 1 (sin `input()`) sí se ejecutó y quedó con su output cacheado en el notebook, como corresponde al ICN; el resto de las celdas de ejemplo/ejercicio quedan sin output (se ejecutan interactivamente en Colab).
- Corrección menor al spec durante la verificación: dos definiciones del ICN (Conceptos 2 y 4) empezaban con minúscula tras "Definición:" — se corrigió capitalización y se regeneró el notebook.
