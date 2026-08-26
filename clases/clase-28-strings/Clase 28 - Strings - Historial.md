# Historial — Clase 28

## 2026-08-26 — Especificación aprobada
- Objetivo: Extraer caracteres y segmentos específicos de una cadena de texto mediante índices y rebanadas, con precisión (actitud: Precisión).
- Alcance recortado respecto a Picuino N°21+N°22 en sesión de diseño previa (ver `Prompt.md`): solo índice y rebanada, sin creación/unión/repetición de cadenas ni recorrido con `for` (movido a Clase N°29 nueva).
- Estructura de 5 pasos propuesta y aprobada en una iteración, con un ajuste: Diego pidió fusionar los conceptos del ICN — índice positivo + índice negativo en un solo concepto, y rebanada + rebanada fuera de rango en otro — quedando 3 conceptos en vez de 5.
- Escenario compartido Haz Ahora/ICN/Guiada: código de sala de un torneo de videojuego móvil. Independiente con Ejercicios 0a/0b (índice puntual y rebanada), 1 (código de seguimiento de pedido), 2 (tag de clan gamer), 3 contextualizado (RUT — cuerpo y dígito verificador) y 4 desafío (código de acceso simétrico, sin usar `[::-1]` para no adelantar sintaxis).

## 2026-08-26 — Colab de clase generado (con corrección de orden en el spec)
- Archivos: `Clase 28 - Strings - Clase.ipynb`, `Clase 28 - Strings - Solucionario.ipynb`, `Clase 28 - Strings - Ticket de Salida Respuestas.json`, `Clase 28 - Strings - Ticket de Salida.pptx`.
- Generados con `generar-colab-clase` + `generar-ppt-clase/crear_ppt_ticket.py`.
- **Bug detectado y corregido en el spec antes de que llegara al notebook:** en los 6 ejercicios de la Independiente (0a, 0b, 1, 2, 3, 4) había escrito `- Solución:` antes que `**Celda de verificación:**`, invertido respecto al orden que exige el parser (`parsear_independiente()` corta el contenido justo antes de `- Solución:`, así que todo lo escrito después de esa marca se pierde). Primera pasada del Colab generó los 6 ejercicios sin ninguna celda de verificación. Se corrigió el orden en el spec (Celda de verificación antes de Solución, como documenta `generar-colab-clase/SKILL.md`) y se regeneró — la segunda pasada trajo las 6 celdas de verificación correctamente.
- Verificado: `Clase.ipynb` y `Solucionario.ipynb` ejecutan sin errores (`jupyter nbconvert --execute`); las 6 soluciones de referencia producen exactamente las líneas `esperadas` de sus verificadores (chequeado aparte, fuera del notebook).

## 2026-08-26 — Cambio de escenario compartido: código de sala gamer → patente/Registro Civil
- A propuesta de Diego, el escenario del Haz Ahora + ICN + Guiada cambió de "código de sala de torneo gamer" a "patente de auto en el Registro Civil" (patente chilena vigente, 4 letras + 2 números, ej. `BRTZ21`).
- Se evitó inventar significado real a cada letra/número (el sistema actual de patentes no codifica región ni categoría) — se trata solo como bloque de letras + bloque de números.
- La patente tiene naturalmente 2 segmentos (no 3 como el código de sala descartado); se agregó la extracción de la primera letra por separado ("para ordenar el archivo alfabéticamente") como tercera pieza de la Guiada, para mantener el mismo nivel de dificultad (índice único + rebanada combinados).
- RUT se mantiene sin cambios como Ejercicio 3 — quedó como punto abierto al proponer el cambio y Diego aprobó la propuesta completa sin objetarlo.
- Regenerados `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json` y `Ticket de Salida.pptx` desde el spec actualizado; ambos notebooks ejecutan sin errores.

## 2026-08-26 — Colab de clase aprobado
- Archivo: `Clase 28 - Strings - Clase.ipynb` (con el escenario de patente/Registro Civil).
- Generado con la skill `generar-colab-clase`.
- Sin más iteraciones tras el cambio de contexto — aprobado directo.
