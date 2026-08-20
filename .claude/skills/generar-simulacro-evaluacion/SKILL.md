---
name: generar-simulacro-evaluacion
description: Diseña y genera un Simulacro — una sesión de práctica estilo evaluación, sin nota, que se dicta 1-3 días antes de una Evaluación individual sumativa, con ítems que aplican los mismos conceptos que la prueba real pero con una operación distinta en cada uno (nunca la misma, para que resolver el simulacro no filtre respuestas). Usa esta skill cuando Diego pida preparar un "simulacro", "repaso estilo prueba" o "ensayo" antes de una evaluación de Ciclos, Funciones, etc. Requiere que el Spec de la Evaluación real ya exista y esté aprobado.
---

# Skill: Simulacro de evaluación

## Propósito

Un Simulacro es una sesión de práctica formativa (sin nota) que se dicta 1-3 días antes de una Evaluación individual sumativa, con el mismo formato y nivel de exigencia que la prueba real, pero con ítems que no se puedan memorizar directamente para el día de la evaluación. Cierra con una revisión conjunta de errores en la misma clase.

Referencia real: `clases/clase-26-simulacro-ciclos/` (simulacro de `clase-27-evaluacion-ciclos`, diseñado y generado el 2026-08-20).

## Cuándo usar esta skill

- Diego pide un "simulacro", "ensayo", "repaso estilo prueba" o "práctica antes de la evaluación" para una Evaluación individual sumativa ya planificada.
- **Nunca la actives sin que la Evaluación real correspondiente ya tenga su `Spec.md` aprobado** — ver Prerrequisito.

## Prerrequisito — la Evaluación real debe existir primero

El simulacro se diseña **a partir de** la Evaluación, ítem por ítem, no al revés. Antes de proponer nada, lee completo `clases/clase-NN-evaluacion-tema/Clase NN - Evaluación Tema - Spec.md` (workflow "evaluaciones individuales sumativas" del `CLAUDE.md` raíz). Si ese Spec no existe o no está aprobado todavía, dilo y ofrece diseñar primero la Evaluación — no hay forma de garantizar que el simulacro no sea un clon sin tener la prueba real delante para comparar cada ítem.

Del Spec de la Evaluación necesitas, por cada ítem: qué constructo evalúa (`for`+`range()`, `for` anidado, `while`, `continue`/`break`, combinaciones), y qué **operación concreta** resuelve (no solo el contexto narrativo) — es el insumo para la Regla de oro más abajo.

## Flujo de diseño: iterar en chat, sin generar archivos hasta aprobar

Igual que el resto del proyecto (ver "Convenciones de iteración" del `CLAUDE.md` raíz): propone la estructura completa en el chat (tabla de ítems con constructo + operación + contexto), espera el feedback de Diego, ajusta, y solo genera archivos cuando diga explícitamente que aprueba. En la sesión de referencia esto tomó varias rondas: acortar la cantidad de ítems, mover la Guiada al inicio del documento completo (no solo de la Sección 2) y pedirle el problema más complejo, agregar Objetivo/Propósito y Ticket de Salida, y por último cuestionar la distancia real entre cada ítem y su equivalente en la prueba — todas correcciones legítimas de esta etapa, no señales de que conviene saltarse el chat.

## Regla de oro: mismo concepto, operación distinta

Cada ítem del simulacro debe aplicar **el mismo constructo** que su ítem equivalente en la Evaluación, pero resolviendo una **operación distinta** — no alcanza con cambiar el contexto narrativo manteniendo la misma lógica interna. Si el código de solución del simulacro es un cambio de nombres de variables sobre el código de la prueba, no sirve.

**Técnicas de diferenciación** (usa varias, no siempre la misma):

- **Cambiar la operación de agregación:** suma/promedio → máximo/mínimo; suma total → doble clasificación por categoría (dos contadores en vez de un acumulador + un contador de umbral).
- **Cambiar el tipo de tarea, no solo el contenido:** si la prueba solo pide *corregir* un `break`/`continue`, el simulacro puede pedir *escribirlo* desde cero (o viceversa) — la prueba casi nunca cubre ambas direcciones de la misma construcción.
- **Cambiar el mecanismo del bug, no solo su ubicación:** un bug de `continue` puede ser una condición invertida en la prueba, y un error de **orden de instrucciones** (el contador queda sin protección del filtro) en el simulacro — mismo constructo, diagnóstico distinto.
- **Enriquecer un ítem con un requisito adicional:** un `for` anidado que solo imprime + cuenta impresiones en la prueba puede pasar a acumular un valor ponderado (no +1 por vuelta) y sumar un contador condicional a nivel del ciclo externo en el simulacro — el código de solución queda visiblemente más largo y distinto.
- **Aprovechar construcciones sin ítem equivalente en la prueba** (ej. si la Evaluación nunca prueba un bug de `for` anidado porque en su última versión ese ítem pasó a "armar") — ahí no hay clon posible, es el caso más seguro.
- **Contextos nunca repetidos**, ni de la Evaluación ni de las clases foco que la Evaluación ya excluyó (su propio Spec suele traer la lista — revísala). Usa `referencia-intereses-estudiantes` para un banco de temáticas frescas (videojuegos, música, redes sociales, finanzas, estudio, tecnología/robots) si hace falta variedad.

**Autochequeo de honestidad antes de la aprobación final.** Antes de que Diego apruebe, arma una tabla ítem por ítem con un semáforo:
- 🟢 **Alto** — operación genuinamente distinta, o sin equivalente directo en la prueba.
- 🟡 **Medio** — mismo constructo y misma forma general (a veces inevitable: es literalmente lo que se está practicando), pero la lógica interna cambia.
- 🔴 **Bajo** — evítalo; si un ítem queda así, rediséñalo antes de proponerlo.

Presenta esta tabla en el chat aunque Diego no la pida — es lo que le permite decidir con criterio en vez de confiar a ciegas. En la sesión de referencia, el ítem guiado (mismo esqueleto `while`+centinela que la prueba, cambiando promedio por máximo) y un bug de `continue` quedaron en 🟡 de forma justificada: no se puede alejar más sin dejar de practicar esa habilidad puntual.

## Estructura fija del documento

A diferencia de una clase regular (Haz Ahora → ICN → Guiada → Independiente → Ticket) y de la Evaluación (sin Guiada, va directo a los ítems), el Simulacro usa este orden:

1. **Encabezado + Objetivo + Propósito** — el objetivo liga los constructos de la Evaluación; el propósito explica el sentido de practicar bajo presión controlada sin nota.
2. **Práctica Guiada — el problema más complejo, al inicio de todo el documento (no al inicio de la Sección 2), se resuelve en conjunto.** Se elige el más exigente de los candidatos de "desarrollo" (el que tenga más ramificación/casos borde), justamente porque se destraba en grupo antes de que cada quien trabaje solo. Nunca lleva celda "Mis respuestas" (regla 19 del `CLAUDE.md` — Diego escribe directo en `# Tu programa`).
3. **Sección 1 — ítems cortos** (armar + arregla el bug, sin `input()`), en la misma proporción que Diego pida — no asumas 4+4 como la Evaluación si te pidió acortar.
4. **Sección 2 — desarrollo** (con `input()` cuando corresponda), con los candidatos restantes tras sacar el más complejo para la Guiada.
5. **Ticket de Salida** (3 preguntas de alternativas) — mismo mecanismo que cualquier clase regular: mismo Google Form, PPT aparte, JSON de respuestas. Aunque el simulacro completo no lleve nota, el Ticket sigue el flujo estándar de trazabilidad.
6. **Cierre** breve, sin la pregunta de actitud del banco (esa es exclusiva de `Control.ipynb`/`Evaluación.ipynb` — un Simulacro no es un instrumento formal de esa categoría).

## Decisiones de formato que van fijas (a menos que Diego diga lo contrario)

- **Sin nota, sin autocheck durante el trabajo** — igual que la Evaluación, para simular condiciones reales; el `Solucionario.ipynb` es la herramienta de la revisión conjunta, no algo que se entregue con calificación.
- **Modalidad individual** (a diferencia del default de parejas del resto del curso) — documéntalo en el `Spec.md` (sección Contexto), pero **nunca lo escribas en el notebook de estudiante**: la modalidad de trabajo nunca se anuncia por escrito ahí (Diego la anuncia en vivo), misma regla que rige para cualquier clase.
- **Pistas desplegables en todos los ítems** (Guiada, Sección 1 y Sección 2) — el simulacro es una serie de práctica sin nota, así que aplica el default "siempre pistas" vigente desde Clase 25.
- **Solucionario sin rúbrica de puntaje.** En vez de la rúbrica de 3 niveles que usa el Solucionario de una Evaluación, cada ítem cierra con una nota breve `🔎 **Qué se revisó:**` (1-2 frases, mismo espíritu que el Solucionario Estudiantes de una evaluación sumativa) — es lo que Diego usa para comentar en voz alta durante la revisión conjunta.
- **Ticket de Salida con rotación de letra correcta**, sin repetir la misma dos veces seguidas, cubriendo construcciones distintas entre las 3 preguntas.

## Artefactos y nombrado

Carpeta `clases/clase-NN-simulacro-tema-breve/`, prefijo `Clase NN - Simulacro Tema - [Tipo]`:

```
clases/
└── clase-NN-simulacro-tema-breve/
    ├── Clase NN - Simulacro Tema - Spec.md
    ├── generar_simulacro.py                              # fuente de verdad — no editar los .ipynb a mano
    ├── Clase NN - Simulacro Tema - Simulacro.ipynb        # estudiantes, sin ninguna solución
    ├── Clase NN - Simulacro Tema - Solucionario.ipynb     # revisión conjunta, sin rúbrica de puntaje
    ├── Clase NN - Simulacro Tema - Ticket de Salida.pptx
    ├── Clase NN - Simulacro Tema - Ticket de Salida Respuestas.json
    └── Clase NN - Simulacro Tema - Historial.md
```

## Generación técnica

1. **`Spec.md`** es la fuente de verdad narrativa. Debe incluir, para que las herramientas de abajo lo puedan parsear:
   - Encabezado `# Clase NN — Simulacro Tema`.
   - Una sección `### N. Ticket de Salida` con bloques `**Pregunta N:**` en el mismo formato que usa una clase regular (código opcional, enunciado, alternativas `- A: ...`..`- D: ...`, `**Respuesta correcta:**`, `**Justificación:**`) — es el formato que espera `crear_ppt_ticket.py`.
   - Una sección final "Decisiones de diseño relevantes" con la tabla de diferenciación ítem por ítem (mismo contenido validado en el chat), para que quede registrado por qué cada ítem no es un clon.

2. **`generar_simulacro.py`** — escribe un script propio por simulacro (mismo patrón que `generar_evaluacion.py` de una Evaluación): los datos de cada ítem (narrativa, código con blanco/bug, solución, pista, resultado esperado, qué se revisó) van embebidos como diccionarios de Python, y el script construye ambos `.ipynb` con `nbformat` (`new_notebook`, `new_markdown_cell`, `new_code_cell`). No intentes reusar el parser de `generar-colab-clase/crear_colab.py` — está hecho para el formato de 5 pasos de una clase regular (Haz Ahora/ICN/Guiada/Independiente/Ticket) y no calza con la estructura del Simulacro.

3. **`Ticket de Salida.pptx`** — no lo generes a mano. Reutiliza el script ya existente de la skill `generar-ppt-clase`:
   ```bash
   python .claude/skills/generar-ppt-clase/crear_ppt_ticket.py \
     "clases/clase-NN-simulacro-tema-breve/Clase NN - Simulacro Tema - Spec.md" \
     "clases/clase-NN-simulacro-tema-breve/Clase NN - Simulacro Tema - Ticket de Salida.pptx"
   ```
   En Windows, si la consola trunca la ejecución por un `UnicodeEncodeError` al imprimir el emoji final, no es un fallo real — el `.pptx` ya se guardó antes de ese print. Verifica abriendo el archivo (`python -c "from pptx import Presentation; print(len(Presentation('...').slides))"`) en vez de confiar en el mensaje de consola.

4. **`Ticket de Salida Respuestas.json`** — mismo formato que cualquier clase (`clase`, `tema`, `respuestas` con claves `"Respuestas a ticket [1]"`..`"[4]"`, `"No se preguntó"` en las que sobren).

## Verificación antes de entregar

Ejecuta **todas** las soluciones (Guiada, cada ítem de Sección 1 en su versión corregida y, si aplica, en su versión con bug para confirmar que el bug realmente produce el comportamiento descrito, cada ejercicio de Sección 2, y las 3 preguntas del Ticket) contra el output declarado, incluyendo los casos borde que mencione el Spec. Un patrón simple con `contextlib.redirect_stdout` y un `input()` mockeado con `iter()` alcanza — no hace falta `jupyter nbconvert` para esto salvo que quieras además confirmar que el `.ipynb` corre limpio de punta a punta.

## Cierre de etapa

Sigue el protocolo estándar de commit + push del `CLAUDE.md` raíz, con una excepción: **`Ticket de Salida.pptx` y `Ticket de Salida Respuestas.json` no se pushean hasta después de dictada la sesión** (mismo criterio que rige para el Ticket de Salida de cualquier clase — el repo es público). El resto de la carpeta (`Spec.md`, `generar_simulacro.py`, `Simulacro.ipynb`, `Solucionario.ipynb`, `Historial.md`) sí se puede subir apenas Diego apruebe.
