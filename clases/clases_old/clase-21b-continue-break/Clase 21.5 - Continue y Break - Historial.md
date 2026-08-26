# Historial — Clase 21.5

## 2026-08-07 — Especificación aprobada
- Objetivo: Construir programas con ciclos `for` que salten iteraciones con `continue` y corten búsquedas o intentos con `break`, con método.
- Actitud elegida: Método (entre Criterio, Método, Precisión y Perseverancia).
- Estructura aprobada en una sola iteración de chat, con un ajuste de contexto: el escenario de Haz Ahora/Guiada pasó de Brawl Stars a Free Fire (pedido explícito de Diego).
- Contenido acordado de antemano en `Plan Semana 2026-08-10 - Cierre de Ciclos.md` (2026-08-04): `continue` como herramienta de legibilidad, `break` como herramienta que agrega capacidad real, `for...else` fuera de alcance (reemplazado por el patrón de "bandera").
- Guiada usa el patrón de "intentos limitados" (código de acceso); Ejercicio 2 de Independiente usa el patrón de "búsqueda que se detiene" (entrenamiento), para no repetir el mismo patrón de `break` dos veces.

## 2026-08-07 — Colab de clase aprobado
- Archivos: `Clase 21.5 - Continue y Break - Clase.ipynb`, `Clase 21.5 - Continue y Break - Solucionario.ipynb`, `Clase 21.5 - Continue y Break - Ticket de Salida Respuestas.json`.
- Generados con la skill `generar-colab-clase`. Diego confirmó incluir el autochequeo (verificador por salida) en los 3 ejercicios de Independiente; como el Ejercicio 2 y el 3 usan `input()`, cada `verificar_ejercicio_N()` le pide al estudiante ingresar los datos del Ejemplo 1 del enunciado para comparar contra un caso fijo.
- Correcciones técnicas aplicadas sin gate (regla 6 CLAUDE.md): `print("Etiqueta", var, ":", resto)` cambiado a `print("Etiqueta", var, "-", resto)` en Guiada, Ejercicio 2 y Ejercicio 3 (evitaba un espacio de más antes de los dos puntos); Ejercicio 2 pasó de `float(input(...))` a `int(input(...))` para calzar con el resultado esperado documentado (minutos enteros).
- Iteración de feedback tras la primera generación:
  - Se reemplazó el nombre propio "Tomás" por "un estudiante del curso" en Haz Ahora y Guiada — no usar nombres de estudiantes particulares en escenarios de clase.
  - Se agregaron comentarios inline cortos en los 3 ejemplos del ICN, mostrando la operación con un valor concreto (ej. `# ej: si numero vale 3, 3 % 3 == 0 → se cumple, se salta`).
  - Se aplicó `== True` / `== False` explícito en Concepto 3, Guiada, Ejercicio 2, Ejercicio 3 y Pregunta 3 del Ticket (convención permanente del proyecto, ver memoria `feedback_booleanos_con_==_true_explicito`).
  - Se agregó una nota al inicio de Independiente: no borrar el comentario `# Tu solución — Ejercicio N` (lo usa el verificador) y que no se necesitan nombres de variable particulares.
  - Se simplificó la narrativa y los bullets del Ejercicio 2 (Entrenamiento), que había quedado tan largo como el desafío.
- Aprobado por Diego ("todo bien") tras revisar en Colab.

## 2026-08-11 — Ticket de Salida.pptx generado
- Archivo: `Clase 21.5 - Continue y Break - Ticket de Salida.pptx`, generado con `crear_ppt_ticket.py`.
- 8 slides (portada + 3 preguntas + slide del Formulario + 3 revisiones). Respuestas correctas P1=B, P2=A, P3=C, coincidiendo con `Ticket de Salida Respuestas.json` (ya existente). Sin avisos de layout en consola.
- No commiteado ni pusheado — se genera para proyectar el día de la clase y el repo es público (regla del skill `generar-ppt-clase`).
