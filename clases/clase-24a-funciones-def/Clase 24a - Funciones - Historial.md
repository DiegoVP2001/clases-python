# Historial — Clase 24a

## 2026-08-12 — Especificación aprobada
- Objetivo: Construir funciones propias con `def` que resuelvan una tarea puntual, con claridad.
- Actitud elegida tras iterar dos rondas de opciones: Claridad (descartadas: Orden, Método, Precisión, Criterio, Responsabilidad, Autonomía).
- Objetivo ajustado por Diego: se quitó la mención a "sin leer el código interno" y a "parámetros y return" del enunciado del objetivo — quedó centrado en `def` + tarea puntual + claridad, sin enumerar toda la sintaxis.
- Estructura de 5 pasos aprobada con dos rondas de ajuste de contexto:
  - Ronda 1: propuesta completa con Haz Ahora/Guiada en la Feria de las Pulgas (descuento a socios del club de coleccionistas) y Ejercicio 2 en el kiosco del liceo (cálculo de vuelto).
  - Ronda 2 (aprobada): Haz Ahora/Guiada se movieron al kiosco del liceo (descuento CEE) y el Ejercicio 2 pasó a Club Deportivo de Isla de Maipo (cuota mensual × meses atrasados, sin condicional) para no duplicar la lógica de descuento por categoría que ya cubre la Guiada.
- **Cambio sistémico registrado en el `CLAUDE.md` raíz (reglas 15/16/20), vigente desde esta clase en adelante:** Práctica Independiente pasa de 2 obligatorios + 1 desafío a **3 obligatorios (2 directos + 1 contextualizado/complejo) + 1 desafío opcional**; la Práctica Guiada sube su nivel de dificultad para igualar al Ejercicio 3. Motivación de Diego: que esta clase sirva de modelo directo para el Control del Lunes Estándar de Funciones (24-ago).
- Ajuste explícito de Diego: sin ninguna conexión textual entre esta clase y el Lunes Estándar — se diseñó de forma autónoma, sin alusiones.
- Pendiente: Clase 24b (Picuino N°20 — valores por omisión), a diseñar como clase separada para el jueves 20-ago.

## 2026-08-13 — Colab de clase aprobado
- Archivos: `Clase 24a - Funciones - Clase.ipynb`, `Clase 24a - Funciones - Solucionario.ipynb`, `Clase 24a - Funciones - Ticket de Salida Respuestas.json`.
- Generados con la skill `generar-colab-clase`. Notebook ejecutado sin errores (`nbconvert --execute`); outputs del ICN verificados contra el spec.
- **Bug de parser corregido en el spec (técnico, no cambia contenido):** las 4 tablas "Resultado esperado" con `input()` (Guiada, Ejercicios 1-3) estaban escritas como tabla markdown (`| Ejemplo 1 | Ejemplo 2 |`), formato que el generador no reconoce y descarta en silencio — se convirtieron a la tabla HTML canónica (mismos datos), sin lo cual esas cuatro secciones habrían quedado vacías en el notebook de estudiante.
- **Mismo bug detectado en la Clase 22 ya publicada** (sus Ejercicios 1-4 perdieron el "Resultado esperado" en el `.ipynb` subido) — pendiente que Diego decida si corregirla también.

## 2026-08-13 — Ticket de Salida (PPT) aprobado
- Archivo: `Clase 24a - Funciones - Ticket de Salida.pptx` (8 slides: portada + 3 preguntas + pantalla del Form + 3 slides de revisión).
- Generado con `crear_ppt_ticket.py`. Respuestas correctas: P1=B, P2=C, P3=A.
- **No se commitea ni pushea a GitHub todavía** — regla fija de la skill (repo público, el archivo expone preguntas y respuestas): se sube recién después de dictada la clase.
