# Historial — Clase 21 - Ayudantía Ejercitación Ciclos

## 2026-08-07 — Set de ayudantía generado

- **Clase:** Clase 21 - Ayudantía Ejercitación Ciclos
- **Clases foco:** `clase-16-for-range` (for + range()) y `clase-20-for-avanzado` (for anidado) — alcance NO incluye continue/break
- **Propuesta:** `Clase 21 - Ayudantía Ejercitación Ciclos - Ejercicios propuesta.json`
- **Generado con la skill `generar-ayudantia-ejercicios`**
- **Contenido:** objetivo + resumen rápido de los dos conceptos + ejercicio guiado ("Riego por goteo en una parcela") + 5 ejercicios independientes (2 de `for`+`range()`, 2 de `for` anidado, 1 mixto combinando ambos) + Ticket de Salida de 4 preguntas
- **Dificultad:** mixta (base → alta)
- **Autochequeo:** celda de verificador (`verificar_ejercicio_1()`…`verificar_ejercicio_5()`) incluida a pedido explícito de Diego — todas las soluciones y verificadores se probaron por script antes de entregar (20/20 casos de prueba correctos, 5/5 verificadores en verde)

### Cambios de alcance sobre lo inicialmente planeado

- Diego pidió agregar un **resumen rápido** de los dos conceptos (con un ejemplo de código breve cada uno) al inicio del notebook, entre el Objetivo y el ejercicio guiado. Primera versión: tabla HTML side-by-side con `<pre>` dentro de las celdas — Diego la vio "pésimo" en el notebook real, así que se corrigió a dos subsecciones apiladas (subtítulo + definición + bloque \`\`\`python\`\`\` nativo de Jupyter), sin tabla y sin la palabra "torpedo".
- Diego pidió agregar una **sección de Cierre con Ticket de Salida**, algo que las ayudantías nunca habían tenido hasta ahora. Se resolvió así:
  - 4 preguntas (no 3, ya que esta ayudantía consolida dos clases foco).
  - Mecanismo idéntico al de una clase regular: PPT aparte (`Clase 21 - Ayudantía Ejercitación Ciclos - Ticket de Salida.pptx`, mismo diseño de marca, generado reutilizando `crear_ppt_ticket.py`), mismo Google Form, y las respuestas quedan en `Clase 21 - Ayudantía Ejercitación Ciclos - Ticket de Salida Respuestas.json` para que la skill `trazabilidad-ticket-salida` la cruce igual que cualquier clase.
  - Las preguntas viven solo en el Solucionario — nunca en el notebook de estudiante.

### Extensiones de infraestructura hechas en esta sesión

Estas tres capacidades no existían antes en `generar-ayudantia-ejercicios` y se agregaron aquí porque Diego las pidió explícitamente para esta ayudantía; quedan disponibles para futuras ayudantías vía los mismos campos JSON (opcionales, no rompen propuestas anteriores):

1. `verifier_setup_py` + `verifier_call` por ejercicio → celda de autochequeo ejecutable en el notebook de estudiante.
2. `resumen_rapido_md` → sección de resumen rápido entre el Objetivo y el ejercicio guiado (nunca como tabla HTML — se ve mal en Jupyter/Colab).
3. `ticket_de_salida` → sección de Ticket de Salida en el Solucionario + `Ticket de Salida Respuestas.json`. El PPT aparte se genera fuera del script, alimentando `crear_ppt_ticket.py` (de `generar-ppt-clase`) con un fragmento de spec derivado del mismo JSON.

Ver `.claude/skills/generar-ayudantia-ejercicios/SKILL.md` para el schema actualizado.

### Pendiente para Diego

- Subir `Ejercicios.ipynb` a Google Colab.
- El día de la ayudantía (2026-08-10): proyectar `Ticket de Salida.pptx` y subir `Solucionario.ipynb` a Classroom después de la sesión.
- **No commitear/pushear `Ticket de Salida.pptx` ni `Ticket de Salida Respuestas.json` antes del 2026-08-10** — mismo criterio que las clases regulares (repo público, contienen las respuestas correctas).
