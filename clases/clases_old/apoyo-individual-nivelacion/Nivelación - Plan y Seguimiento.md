# Nivelación individual — Plan y Seguimiento

## Propósito

Dos estudiantes del curso tienen muchas inasistencias por diversas razones, y no tiene sentido evaluarlos con el mismo ritmo y las mismas pruebas que al resto del curso. En vez de eso, avanzan de forma autónoma con notebooks de repaso **sin nota**, y la nota real sale de **2 pruebas atrasadas** proctoreadas aparte (para evitar que se copien la solución del propio notebook de práctica).

Formato de los 3 notebooks: idéntico al usado en `clases/Clase-17-apoyo-individual/Clase-17-apoyo-individual.ipynb` — teoría breve por bloque, ejemplo resuelto, ejercicio, y todas las soluciones plegadas (`<details>`) al final del documento. A diferencia de los `Clase.ipynb` normales del curso, estos SÍ incluyen solución, porque son material de autorrevisión sin nota, no un notebook que se sube a Classroom antes de una evaluación.

## Los 3 notebooks generados

| Notebook | Alcance |
|---|---|
| `Nivelación - 01 Fundamentos - Apoyo Individual.ipynb` | `input()`, tipos de datos (`int`/`float`/`str`/`bool`), variables, `print()`, conversión con `int()`/`float()` — clase 7. 5 bloques, 5 ejercicios. |
| `Nivelación - 02 Condicionales - Apoyo Individual.ipynb` | Copia fiel de `Clase-17-apoyo-individual.ipynb`: booleanos, comparadores, operadores lógicos, análisis de condiciones, `if`/`else`, `if` anidados, `elif` — clases 8a-14, 17. 7 bloques + desafío final, 8 ejercicios en total. |
| `Nivelación - 03 Ciclos - Apoyo Individual.ipynb` | **Alcance parcial:** `for` + `range()`, acumuladores, `for` anidado — clases 16 y 20. 5 bloques, 5 ejercicios. NO incluye `continue`/`break` ni `while` (ver nota de bloqueo abajo). |

## Calendario tentativo

| Cuándo | Qué hacen ellos | Hito |
|---|---|---|
| Semana 2026-08-04 al 2026-08-10 | Notebook 1 — Fundamentos | — |
| Semana 2026-08-10 al 2026-08-17 | Notebook 2 — Condicionales | — |
| **2026-08-17** (o 08-18) | — | 🎯 **Prueba atrasada 1** — Fundamentos + Condicionales, versión paralela de la Evaluación N°19 |
| Desde 2026-08-17 | Notebook 3 — Ciclos (alcance parcial) | — |
| Semana del 2026-08-24 al 2026-08-31 (tentativa) | — | 🎯 **Prueba atrasada 2** — Ciclos, versión paralela de la Evaluación N°22.5 |

Trabajan en tiempo de clase regular, en paralelo con el resto del curso (que sigue el ritmo normal: N°16, N°20, N°21, N°21.5, N°22 → N°22.5). Si alguno de los dos no llega listo para una fecha, esa prueba se corre sin arrastrar la otra — son hitos independientes.

## Pendiente — pruebas atrasadas (NO generadas todavía)

- **Prueba atrasada 1** (Fundamentos + Condicionales): se construye reutilizando el patrón `generar_evaluacion.py` de `clases/clase-19-evaluacion-condicionales/`, cambiando contexto y números para que no sea copia literal de la que ya rindió el resto del curso. Generarla cuando los estudiantes estén por terminar el Notebook 2.
- **Prueba atrasada 2** (Ciclos): bloqueada hasta que la Evaluación N°22.5 exista con contenido real para el resto del curso — hoy (`clases/Historial-Curricular.md`) es solo un placeholder "sep 2026", sin spec ni notebook.
- Ambas entran al flujo `revisar-evaluacion` ya existente en el proyecto, para que la nota quede justificada con la misma rúbrica que usa el resto del curso.

## Notas

- **No commitear ni pushear esta carpeta a git sin autorización explícita de Diego.** El repo es público; estos notebooks de nivelación no tienen por qué quedar expuestos apenas se crean, a diferencia del resto del material del curso.
- Cuando existan specs aprobadas de continue/break (N°21.5) y while (N°22) para el resto del curso, ampliar el Notebook 3 con esos bloques (no regenerarlo desde cero — agregar bloques nuevos al final, antes de la sección de Soluciones).
