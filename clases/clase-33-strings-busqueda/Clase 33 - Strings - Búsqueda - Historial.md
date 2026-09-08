# Historial — Clase 33

## 2026-09-05 — Especificación aprobada
- Objetivo: Aplicar los operadores `in` y `find()` para detectar si un texto contiene una palabra clave y en qué posición aparece, con rigor.
- Actitud: Rigor. Contexto: Los Mellis Al Paso (mismo negocio ancla de Clase 32).
- Propuesta presentada como plan bundleado (objetivo + OAs + estructura de 5 pasos, según el flujo maestro del proyecto) y aprobada en una sola iteración de estructura, con un ajuste durante el proceso: Diego propuso agregar una sección nueva "¿Para qué sirve?" después del Propósito (máx. 2 frases, ejemplos reales ligados a la práctica de la clase). Se acordó el texto y Diego pidió dejarlo como **default** para todas las clases futuras (no solo piloto) — ver actualización de `disenar-clase/SKILL.md`, `generar-colab-clase/SKILL.md`, `generar-ppt-clase/SKILL.md` y nueva regla 24 del `CLAUDE.md` raíz del proyecto.
- Todas las posiciones de `find()` usadas en las soluciones (Guiada, Ejercicios 1-4, Ticket de Salida) se verificaron ejecutando el código real en Python antes de guardar el spec.

## 2026-09-08 — Piloto: ICN con código mínimo + instrucción (demo, no regla)
- Origen: en Clase 32, dictando en vivo, Diego borró a mano el cuerpo del ejemplo de `split()` y dejó solo `linea = "Papas Fritas,3400"` en la celda, para que los estudiantes escribieran ellos `producto, precio_texto = linea.split(",")` y los `print()`. Ese cambio no había quedado registrado en el repo.
- Se llevó ese formato a los 3 conceptos del ICN de esta clase (`in`, `.lower()`, `find()`), como **demo puntual, no como default**: cada celda de código del ICN quedó solo con la línea de setup (`nota_pedido = "..."`), y cada bloque de concepto suma una línea `✍️ **Escríbelo tú:** <instrucción>` debajo de la Idea clave, pidiendo escribir la sintaxis nueva.
- El código completo de los 3 conceptos (antes visible en `Clase.ipynb`) se movió a una sección nueva del Solucionario: `## 2️⃣ Introducción al Contenido Nuevo — código completo`.
- Implementado como campos opcionales en el spec (`- Instrucción:` / `- Punto de partida:`) y soporte opt-in en `crear_colab.py` — un spec sin estos campos genera exactamente igual que antes (verificado regenerando Clase 32 y comparando celda por celda, sin diferencias).
- El PPT de esta clase (aún no generado) no se tocó por este piloto; su formato del ICN se decide en su propio gate.
- Pendiente: que Diego revise cómo queda el ICN en el aula y decida si el formato se generaliza a todas las clases (regla en `CLAUDE.md` + defaults en `disenar-clase`/`generar-colab-clase`/`generar-ppt-clase`) o si queda como excepción de esta clase.

## 2026-09-08 — Colab de clase aprobado
- Archivo: Clase 33 - Strings - Búsqueda - Clase.ipynb
- Generado con la skill generar-colab-clase, incluyendo el piloto de ICN con código mínimo + instrucción descrito arriba.
- Ejecutado con `nbconvert --execute` sin errores; outputs limpiados fuera del ICN (las 3 celdas del ICN quedan sin output, a propósito).
