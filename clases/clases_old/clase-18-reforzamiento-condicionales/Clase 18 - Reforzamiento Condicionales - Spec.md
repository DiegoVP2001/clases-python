# Clase 18 — Reforzamiento Condicionales — Spec

**Estado:** planificación — pendiente de generar los dos entregables listados abajo.
**Slot curricular:** N°18 (ver `Historial-Curricular.md`, fila 26 y nota de renumeración 2026-07-15) — "Reforzamiento — repaso Clase 17 + nueva guía rápida".
**Ubicación en la secuencia:** entre Clase 17 (`clase-17-ejercitacion-condicionales`, ejercicios en pareja ya realizados) y Clase 19 (`clase-19-evaluacion-condicionales`, evaluación individual sumativa, martes 21 de julio de 2026).
**Modalidad de la clase 18:** parejas (mismas parejas que trabajaron los ejercicios de Clase 17).

## Contexto

En Clase 17 las parejas trabajaron 4 ejercicios de condicionales (delivery, gimnasio, furgón escolar, festival) con avance disparejo — algunas parejas resolvieron casi todo, otras se quedaron atrás. Las preguntas quedaron publicadas en el Colab de cada pareja, pero la ronda de revisión proyectada no alcanzó a hacerse en clase (se acabó el tiempo y los estudiantes ya se habían ido).

Clase 18 cierra ese pendiente y además deja publicada una guía de repaso rápido, alineada con el temario real de la evaluación (Clase 19), para que las parejas avanzadas —o cualquier estudiante que quiera repasar por su cuenta— tengan material acotado antes del 21 de julio.

## Entregable 1 — Dinámica de revisión (documento para Diego)

**Archivo a generar:** `Clase 18 - Reforzamiento Condicionales - Dinámica.md`

Documento operativo para Diego como profesor, sin material adicional que preparar — reutiliza únicamente lo que ya existe (Colabs de cada pareja de Clase 17 + `Clase 17 - Ejercitación Condicionales - Solucionario.ipynb`, ambos en `old/` dentro de `clase-17-ejercitacion-condicionales/`).

**Dinámica acordada — "Quien terminó, enseña — quien no, corrige en vivo":**

- **Apertura (1 min):** se avisa que se revisa lo pendiente de Clase 17 y que las parejas avanzadas ayudan a explicar.
- **Bloque único, ejercicio por ejercicio (1 → 2 → 3 → 4):** para cada ejercicio, Diego pregunta qué pareja lo tiene resuelto y la proyecta explicando su propio Colab (las preguntas ya son públicas, no hay problema en mostrarlas tal cual). Si nadie llegó a ese ejercicio, Diego lo resuelve en vivo proyectando directamente el Solucionario ya existente.
- **Parejas muy avanzadas (terminaron los 4):** no esperan sentadas — pasan a rol de "consultoras", ayudando a la pareja más cercana que sigue atascada, en vez de que Diego circule solo.
- **Antes de empezar:** Diego define el orden en que va a preguntar por parejas avanzadas, usando lo que ya recibió en Classroom (evita improvisar en vivo quién pasa).

El documento debe explicar esta dinámica en detalle (pasos, tiempos aproximados dentro del bloque de 80 min, criterios para elegir qué pareja pasa primero, y qué hacer si dos parejas resolvieron el mismo ejercicio con estructuras distintas — mostrar ambas si el tiempo alcanza, conecta con el objetivo de "elegir la estructura correcta").

## Entregable 2 — Spec de la guía de repaso rápido (Colab)

**Tipo de artefacto final (no es este documento):** un Colab de repaso corto y conciso, mismo tipo que `clases/Clase-17-apoyo-individual/Clase-17-apoyo-individual.ipynb` (repaso exprés con teoría condensada, un ejemplo resuelto y un ejercicio con valores de prueba concretos por bloque, desafío final, soluciones plegables al fondo) — pero **más breve** que ese precedente.

**Nota de flujo:** Diego está generando este Colab en otra sesión de agente en paralelo, basado en el temario real de la evaluación. Esta sección documenta el alcance esperado para que ambas sesiones queden alineadas — no se genera el `.ipynb` desde esta carpeta.

**Alcance final aprobado (2026-07-15) — más acotado que la propuesta original:**

En vez de 1 ítem por cada uno de los 7 bloques, la guía se concentra solo en **Bloque 6 (`elif`) y Bloque 7 (`elif` + `if` anidado)** — lo último que se vio en Clase 17 y a lo que la mayoría de las parejas no alcanzó a llegar (Ejercicios 3 y 4: furgón escolar y festival). Los bloques 1-5 ya quedan cubiertos por la Dinámica (Entregable 1), que retoma los 4 ejercicios completos de Clase 17.

- **Estructura:** 3 ítems cortos + 1 Desafío final + 2 Ejercicios propuestos (más difíciles) — sin separar en Sección 1/Sección 2.
- **Sin autocheck** (feedback de Diego, 2026-07-15: los prints de los estudiantes pueden no calzar exacto en texto y dar falsos ❌). Todas las soluciones (incluidos los 3 ítems) viven en una única sección `<details>` al final, escrita con texto en negrita en vez de encabezado markdown (`**✅ Soluciones**`, sin `#`/`##`) para que no aparezca en el índice/outline de Colab.
- **Títulos de ítems sin descripción técnica:** "Ítem 1", "Ítem 2", "Ítem 3", "Desafío final", "Propuesto 1/2" — sin nombrar el bloque, operador o tipo de ejercicio en el título (esa info solo vive en la narrativa).
- **Sin `input()`** en ningún ítem — variables ya definidas, igual que la Sección 1 de la evaluación real.
- **Sin "predecir output sin ejecutar":** todo ítem se corre, nunca se adivina en papel.
- **Contextos usados (todos nuevos, sin repetir Clase 17, apoyo individual de Maura, ni la evaluación real de Clase 19):** clima (Ítem 1), streaming musical (Ítem 2), veterinaria/mascotas (Ítem 3, arregla el bug), notas/promedio (Desafío final), batería de celular y descuento de streaming de películas (Propuestos 1 y 2).
- **Extensión:** deliberadamente más corta que el apoyo individual de Maura — repaso express de 10-15 min, no un curso condensado.

**Archivo generado:** `Clase 18 - Reforzamiento Condicionales - Guía de Repaso.ipynb` (vía `generar_guia_repaso.py`, fuente de verdad — no editar el `.ipynb` a mano). Sin autocheck (feedback de Diego, 2026-07-15): las 6 soluciones (Ítems 1-3, Desafío final, Propuestos 1-2) viven plegadas en una única sección `<details>` al final, sin encabezado markdown para que no aparezca en el índice de Colab.

**Estado:** ✅ ambos entregables generados, commiteados y pusheados a `origin/master` (commit `96b85fc`) — 2026-07-15.

## Pendiente

- [x] Generar `Clase 18 - Reforzamiento Condicionales - Dinámica.md` (Entregable 1) — 2026-07-15.
- [x] Generar `Clase 18 - Reforzamiento Condicionales - Guía de Repaso.ipynb` (Entregable 2) — 2026-07-15.
- [x] Registrar en `Historial-Curricular.md` (fila N°18: carpeta + estado + fecha 2026-07-20) — 2026-07-15.
- [x] Confirmar fecha de dictado: **lunes 20 de julio de 2026** (un día antes de la evaluación del 21) — confirmada por Diego.
