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

## 2026-08-11 — Ticket de Salida.pptx generado
- Archivo: `Clase 22 - While - Ticket de Salida.pptx` (8 slides: portada/reglas + 3 preguntas + slide del Google Form + 3 slides de revisión).
- Generado con `crear_ppt_ticket.py` (skill `generar-ppt-clase`) a partir de la sección `### 5. Ticket de Salida` del spec aprobado.
- Respuestas correctas: P1=A, P2=C, P3=B — coinciden con `Clase 22 - While - Ticket de Salida Respuestas.json`.
- **No commiteado ni pusheado.** La clase está programada para el 2026-08-13 (jueves) y el repo es público — el archivo se sube a GitHub recién después de dictarla.

## 2026-08-13 — Feedback post-dictado (sistémico, no se corrigen estos cuadernos)
- Diego reportó dos problemas tras dictar la clase: (1) faltaba el autochequeo (verificador automático) en la Práctica Independiente, y (2) el Ejercicio 1 (Aforo del gimnasio) resultaba ambiguo — no quedaba claro si debía usarse `input()`, si el conteo era solo una suma, o si había un condicional de exceso.
- **Causa raíz encontrada:** los 3 ejercicios de la Independiente escribieron `**Resultado esperado:**` como tabla markdown (`| Ejemplo 1 | Ejemplo 2 |`) en el spec — deliberado por parte de Diego, porque `<table>` HTML a veces se descuadra en pantalla en Colab. El parser de `crear_colab.py` de entonces solo reconocía `<table>` HTML, así que la tabla markdown se perdió en silencio: `Clase.ipynb` quedó sin ningún ejemplo 📥/📤 en los 3 ejercicios, y por eso la ambigüedad.
- **No se corrigen `Clase.ipynb`/`Solucionario.ipynb` de esta clase** — la clase ya se dictó. El feedback se resolvió de forma sistémica para las clases futuras:
  - `crear_colab.py`: el parser ahora reconoce tabla markdown GFM como formato canónico (y sigue aceptando `<table>` HTML como legado); además, si `**Resultado esperado:**` no matchea ningún formato, imprime una advertencia explícita en vez de fallar en silencio. De paso se detectó y corrigió el mismo tipo de pérdida silenciosa en `clase-21b-continue-break` (Ejercicio 1 — Playlist, formato con línea `📤 *El programa imprime:*` antes del bloque de código), no corregido en ese notebook, solo señalado a Diego.
  - `disenar-clase/SKILL.md` y `generar-colab-clase/SKILL.md`: el autochequeo (verificador automático) pasa a ser default siempre en la Práctica Independiente, sin preguntar — excepción fija: `Control.ipynb` y `Evaluación.ipynb`. El template de `disenar-clase` ahora redacta `**Celda de configuración:**` + una `**Celda de verificación:**` por ejercicio como parte estándar del spec.
  - Ver memoria `resultado-esperado-tabla-markdown-no-html` y `autochequeo-default-siempre` para el detalle completo.
