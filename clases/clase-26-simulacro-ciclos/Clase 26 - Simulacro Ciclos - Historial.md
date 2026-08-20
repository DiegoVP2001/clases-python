# Clase 26 — Simulacro Ciclos — Historial

## 2026-08-20 — Diseño y generación completa

Diego pidió generar la Clase 26 (Simulacro de Ciclos, martes 25-ago) tomando como base la Evaluación de Ciclos (Clase 27, jueves 27-ago), pero con la condición explícita de que **no fuera una copia** — que cada ítem aplicara el mismo concepto que su equivalente en la Evaluación, sin ser la misma operación, para que resolver el simulacro no filtrara respuestas de la prueba real.

**Iteración de la propuesta en chat (sin generar archivos) antes de la aprobación:**

1. Propuesta inicial: estructura completa mirando la Evaluación (8 ítems cortos + 3-4 de desarrollo), contextos nuevos, sin nota, individual, sin autocheck durante el trabajo.
2. Diego pidió acortar: 2 armar + 2 bugs + 2 de desarrollo, y agregar una Práctica Guiada al inicio de la sección de desarrollo.
3. Diego pidió mover la Guiada al inicio de todo el documento (no solo al inicio de la sección de desarrollo), que fuera el problema más complejo de los tres candidatos de desarrollo, y agregar Objetivo + Propósito al inicio y un Ticket de Salida al cierre (mismo mecanismo que una clase regular: Google Form + PPT aparte + JSON de respuestas).
4. Diego cuestionó si los ítems quedaban suficientemente distintos de la Evaluación en la *operación*, no solo en el contexto. Se rediseñaron todos los ítems para diferenciar la operación concreta (ej. mismo constructo `while`+centinela pero calculando el máximo en vez del promedio; bug de `continue` por orden de instrucciones en vez de condición invertida; `for` anidado con acumulador ponderado + contador de bloques en vez de imprimir+contar; clasificación doble en vez de suma+umbral).
5. Diego pidió que uno de los ítems "arma" dejara escribir un `break` desde cero (la Evaluación solo lo pide corregir, nunca escribir) — se ajustó el ítem 1A.2 (parque de diversiones).
6. Aprobación final: "apruebo así que dale".

**Artefactos generados:**
- `Clase 26 - Simulacro Ciclos - Spec.md`
- `generar_simulacro.py` (fuente de verdad — script que construye ambos notebooks; no editar los `.ipynb` a mano)
- `Clase 26 - Simulacro Ciclos - Simulacro.ipynb` (estudiantes, sin soluciones)
- `Clase 26 - Simulacro Ciclos - Solucionario.ipynb` (para la revisión conjunta en clase — sin rúbrica de puntaje, con nota "🔎 Qué se revisó" por ítem)
- `Clase 26 - Simulacro Ciclos - Ticket de Salida.pptx` (generado con `crear_ppt_ticket.py` de la skill `generar-ppt-clase`, a partir del Spec)
- `Clase 26 - Simulacro Ciclos - Ticket de Salida Respuestas.json`

**Verificación:** todas las soluciones (Guiada, 4 ítems de Sección 1 en su versión corregida y con bug, 2 ejercicios de desarrollo, y las 3 preguntas del Ticket) se ejecutaron para confirmar que el output coincide exactamente con lo declarado en el Spec y en los notebooks, incluyendo los casos borde (sin puntajes en la Guiada, todas las lecturas normales/de alerta en el Ejercicio 2).

**Ajuste durante la generación:** se quitó una mención a "trabaja de forma individual" que había quedado en las instrucciones del notebook de estudiante — la modalidad de trabajo nunca se anuncia por escrito en el notebook (Diego la anuncia en vivo), regla que aplica también a este simulacro aunque la modalidad en sí (individual, para simular la evaluación) sí quedó documentada en el Spec.

**Pendiente:** Diego revisa el Simulacro y el Solucionario antes del martes 25-ago.

## 2026-08-20 — Cierre: commit y push

Diego aprobó el contenido ("todo bien actualiza y cierra"). Se hizo commit y push de `Spec.md`, `generar_simulacro.py`, `Simulacro.ipynb`, `Solucionario.ipynb` y este `Historial.md`.

**`Ticket de Salida.pptx` y `Ticket de Salida Respuestas.json` quedan fuera del push** — mismo criterio que rige para el Ticket de Salida de cualquier clase (regla 17 del `CLAUDE.md`): el repo es público, así que esos dos archivos no se suben hasta después de dictada la sesión (martes 25-ago).

## 2026-08-20 — Renombrado a "Ejercitación" + autochequeo en cada ítem/ejercicio

Diego pidió dos cambios sobre el notebook de estudiante:

1. **Renombrar el artefacto.** `Clase 26 - Simulacro Ciclos - Simulacro.ipynb` → `Clase 26 - Simulacro Ciclos - Ejercitación.ipynb`. Toda alusión a "Simulacro" como nombre de la actividad dentro del propio notebook se cambió por "Ejercitación": el título (`# 📝 Ejercitación — Ciclos`), el texto del Propósito ("Hoy practicamos bajo las condiciones..." en vez de "Hoy simulamos..."), y el campo del Ticket de Salida ("Tema de la clase de hoy": `ejercitación ciclos`). Se mantuvo sin tocar el nombre de la carpeta (`clase-26-simulacro-ciclos`), `Spec.md`, `Historial.md`, el título del `Solucionario.ipynb` ("Solucionario — Simulacro Ciclos") y el nombre del script `generar_simulacro.py` — ahí "Simulacro Ciclos" describe el tipo de sesión (repaso pre-evaluación vía la skill `generar-simulacro-evaluacion`), no es el nombre que ve el estudiante.
2. **Autochequeo en cada ítem/ejercicio, excepto la Guiada.** Se reutilizó el mecanismo ya validado en `clase-21b-continue-break` (`_revisar()` + `verificar_*()`, re-ejecuta la celda de solución del estudiante buscándola por un comentario-marca en la primera línea y compara su output línea por línea). Se agregó una sola celda de configuración `🔧 Verificador automático` antes de la Sección 1, y una función/llamada por cada uno de los 6 ítems (1A.1, 1A.2, 1B.1, 1B.2, Ejercicio 1, Ejercicio 2). El Ejercicio 2 (usa `input()`) avisa al estudiante que ingrese los mismos datos del Ejemplo 1 al re-ejecutar. La Práctica Guiada quedó excluida a propósito (se resuelve en conjunto en clase, no de forma autónoma).

**Implementación:** todo se hizo editando `generar_simulacro.py` (fuente de verdad) y regenerando — no se tocó ningún `.ipynb` a mano. Se verificó el mecanismo simulando el historial `In[]` de IPython fuera de Jupyter: una solución correcta del Ítem 1A.1 da "✅ ¡Perfecto!", la versión con bug sin corregir del Ítem 1B.1 detecta la primera línea que no coincide, y el Ejercicio 2 con los inputs del Ejemplo 1 también valida correcto.
