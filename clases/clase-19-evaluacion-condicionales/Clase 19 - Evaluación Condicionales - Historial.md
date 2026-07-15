# Historial — Clase 19 - Evaluación Condicionales

## 2026-07-15 — Creación

**Motivo:** construir la evaluación individual sumativa de Condicionales (2026-07-21), pensada para 75 minutos efectivos, a partir del temario (`Clase 17.5 - Evaluación Condicionales - Temario.md`), el Solucionario de la Ejercitación de Clase 17 y el repaso de apoyo individual — sin introducir formatos de pregunta nuevos ni contenidos no trabajados.

**Renumeración curricular:** esta evaluación pasa de N° 17.5 a **N° 19** en `Historial-Curricular.md`, dejando N° 18 reservado para un Reforzamiento (repaso de Clase 17 + nueva guía rápida, pendiente de otra sesión). Todo lo que venía después (for avanzado, while, evaluación de ciclos, funciones, strings, listas, proyectos) se corrió +1 en la numeración.

**Decisiones de formato (respecto al repaso de Clase 17.5):**
- Se mantiene el descarte de "predicción de output sin ejecutar" — es una evaluación en computador, ese formato de papel no aplica (mismo criterio que [[feedback-formato-repaso-computador]]).
- A diferencia del repaso, **esta evaluación sí usa `input()`** en la Sección 2, por pedido explícito de Diego — siempre siendo explícito en el enunciado sobre el tipo de dato esperado (entero, con decimales, o texto exacto), en lenguaje natural, sin nombrar `int()`/`float()` en la narrativa.
- La Sección 1 (ítems cortos) se mantiene **sin `input()`** — variables ya definidas, para ir rápido.
- **Sin autocheck** (a diferencia de la Ejercitación de Clase 17): es una evaluación sumativa, no práctica — la corrección es posterior con la pauta del Solucionario.
- Sin Práctica Guiada dentro del documento — va directo de instrucciones a los ejercicios.
- Todos los contextos son nuevos, sin repetir ninguno usado en Clase 17, Clase 14, Clase 11/13 ni en el apoyo individual.

**Estructura final (100 pts, 75 min):**
- **Sección 1 — Ítems cortos** (30 pts, 7 ítems, ~21 min): 2 "Arma la condición" (Bloque 2) + 5 "Arregla el bug" (uno por Bloque 1, 3, 4, 5, 6).
- **Sección 2 — Programas completos** (70 pts, 4 ejercicios, ~54 min, con `input()`): Modo Fiesta de una playlist (⭐ Fácil, if/else, 12 pts), Micro a Talagante (⭐⭐ Media, if anidados, 16 pts), Ahorro semanal (⭐⭐ Media-alta, elif 4 categorías, 18 pts), Salas de matchmaking (⭐⭐⭐ Difícil, Bloque 7: elif + anidado, 24 pts).

**Escala de nota:** 100 pts, exigencia 50% (nota 4.0 al 50% de logro), pauta completa en el Solucionario.

**Generación:** ambos notebooks (`Clase 19 - Evaluación Condicionales - Evaluación.ipynb` y `- Solucionario.ipynb`) se generan con `generar_evaluacion.py` — fuente de verdad, no editar los `.ipynb` a mano, regenerar el script si hay que cambiar algo.

**Siguiente paso:** cuando Diego pida iterar (agregar ítems, cambiar contextos, ajustar puntaje), editar `generar_evaluacion.py` y regenerar. La revisión de las entregas después de rendida la evaluación se hace con la skill `revisar-evaluacion`.
