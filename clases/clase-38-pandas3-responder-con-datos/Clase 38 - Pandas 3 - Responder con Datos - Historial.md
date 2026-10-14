# Historial — Clase 38

## 2026-10-14 — Especificación aprobada
- Objetivo: Construir una secuencia ordenada de pasos que responda una pregunta con una tabla de datos —quedarse con lo que interesa, resumirlo, ordenarlo y graficarlo—, con método.
- Actitud elegida: Método (opciones ofrecidas: Honestidad, Criterio, Método, Claridad; Perseverancia descartada por ser la de N°37).
- Contexto de partida (dicho por Diego): los 5 conceptos de N°37 se vieron en clase, pero no alcanzó el tiempo para ejercitarlos; eso se hizo en la 37b.
- Estructura aprobada en 4 iteraciones:
  1. Plan inicial: ICN parcelado, un concepto nuevo por paso (filtrar → agrupar → ordenar → graficar), y la tabla se lee una sola vez en una celda de inicio.
  2. Diego pidió **quitar el Propósito** y dejar solo "¿Para qué sirve?" ligado al proyecto, y un **Ticket de 4 preguntas** muy ligadas al ICN, sin comandos no vistos (ni creación de tablas con `pd.DataFrame`).
  3. Diego pidió un **torpedo de ideas** (promedio, conteo, etc.), aplicando uno solo en el ICN. Se aplica `.sum()`; el resto queda como referencia, fuera del Ticket y de los ejercicios.
  4. Aprobación final.
- Sin Ejercicios 0 (decisión de Diego). Sin PPT principal ni Ejercicios.ipynb (Calendario v3).
- Hallazgos técnicos medidos antes de proponer (2026-10-14, sobre `bbdd_guaguas.csv` con el mismo limpiado de N°37): `.sum()` por año es confiable; `.mean()` y `.count()` calculan por fila, no por guagua (Antonia: 105 filas en 102 años por `sexo` sin normalizar). Todas las líneas del torpedo corren sin error. Cifras de la Guiada y de los ejercicios salen de esa ejecución.
- Pendiente de Diego: si las operaciones del torpedo cuentan para la Defensa del 26-oct (recomendación: no).
- Pendiente de revisar al generar el Colab: la celda de inicio, la receta y el torpedo son bloques nuevos que el generador puede no reconocer.
- Dos decisiones solo de esta clase que podrían volverse default (preguntar a Diego más adelante, sin cambiar nada ahora): clase sin sección Propósito; Ticket de 4 preguntas.
