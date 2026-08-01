# Clase 19.5 — Revisión Evaluación Condicionales — Historial

**Estado:** en diseño. Solo existe el material de proyección; **la spec todavía no se escribe** (queda para una sesión aparte, por decisión de Diego).

**Fecha prevista:** lunes 3 de agosto de 2026 · 80 minutos.
**Numeración:** N° 19.5, decimal, para no renumerar el resto del plan (mismo patrón que 22.5 y 28.5). Va entre la evaluación del 28-07 y For anidado del 06-08.

---

## 2026-08-01 — Diagnóstico de resultados de la Evaluación 2

Se calcularon los porcentajes de logro por ítem y por componente a partir de la fuente que tiene los puntajes reales (el generador de los Colabs de devolución). Resultados agregados, sin datos individuales:

| Ítem | Máx | % todos | % tramo alto | % tramo bajo |
|---|---|---|---|---|
| 1A.1 — `and` simple | 4 | 65% | 85% | 41% |
| 1A.2 — `and` + `or` | 4 | 60% | 85% | 28% |
| 1B.1 — bug `=` / `==` | 4 | 89% | 92% | 81% |
| 1B.2 — bug `>` / `>=` en el límite | 5 | 82% | 92% | 75% |
| 1B.3 — bug falta `:` | 4 | 94% | 100% | 88% |
| 1B.4 — bug de indentación | 4 | 89% | 100% | 78% |
| **1B.5 — bug orden de `elif`** | 5 | **48%** | **66%** | 22% |
| 2.1 — Modo Fiesta | 12 | 83% | 100% | 58% |
| 2.2 — Micro a Talagante | 16 | 61% | 97% | 6% |
| 2.3 — Ahorro en dólares | 18 | 65% | 99% | 6% |
| 2.4 — Sala de juego | 24 | 61% | 97% | 0% |

**Conclusiones que dirigen el diseño:**

1. **La distribución está partida en dos, sin medio:** 13 estudiantes sobre 88 puntos, 8 bajo 34, y un solo caso intermedio. Solo 2 tienen la prueba perfecta.
2. **Para el tramo alto la Sección 2 no dejó nada que reforzar** (97-100%). Una clase de repaso general de condicionales los desperdiciaría.
3. **El único error genuinamente transversal es 1B.5 — el orden de la cadena de `elif`:** 7 de los 13 del tramo alto perdieron puntos ahí, y 5 de ellos sacaron 1 de 5. El mismo hilo reaparece en los dos componentes más débiles de ese tramo: anidamiento (2.2 y 2.4) y operadores consistentes en las fronteras (2.3). Sumados, alcanzan a 10 de los 13.
4. **Los 8 del tramo bajo dejaron 2.2/2.3/2.4 en blanco.** Es un problema de producción y de tiempo, no de matiz conceptual: necesitan volver a escribir programas completos con andamiaje, no ver una corrección proyectada.
5. Errores menores, reales pero de otro eje: hardcodear el resultado en los ítems 1A, y pedir un dato con `input()` sin convertirlo a número.

## 2026-08-01 — Enfoque acordado

El eje único de la clase es la pregunta **"¿estas dos preguntas son independientes, excluyentes, o una depende de la otra?"**. Absorbe los tres errores en un solo concepto con tres casos:

| Relación | Forma en Python | Error que explica |
|---|---|---|
| Independientes | varios `if` seguidos | *nunca se enseñó* — es contenido nuevo |
| Excluyentes | `if / elif / else` | 1B.5 |
| Una depende de la otra | `if` anidado | 2.2 y 2.4 |

Que los `if` sueltos sean contenido nuevo está verificado contra la spec de la Clase 14: ahí se enseñó "solo una rama se ejecuta" y "el orden importa", pero siempre dentro de `elif`, nunca contrastado con `if` independientes.

Como herramienta transversal se enseña **probar el valor del borde** (14, 7, 3, 800), que es el hábito que faltó y que explica tanto 1B.5 como las fronteras de 2.3.

Los errores menores del punto 5 **no entran al ICN** — van a las 3 preguntas del Ticket de Salida, para no sobrecargar la clase.

**Decisiones de Diego tomadas en esta sesión:**
- No hay recuperativa: es **cierre formativo**, la nota está cerrada. Conviene decirlo al abrir para que la clase no se vuelva negociación de puntos.
- Los Colabs de devolución se entregan **al inicio** de la clase, no al final.
- El tramo alto no hace de ayudantía: tiene trabajo propio (diseñar los casos límite que rompen programas). El emparejamiento con el tramo bajo es simétrico — quien diseña casos necesita un programa que probar, y quien repara necesita saber si su arreglo aguanta.

## 2026-08-01 — Material generado

`Clase 19.5 - Revisión Evaluación Condicionales - Tres Formas.html` — landing de proyección, pixel art, un solo archivo sin dependencias externas (funciona sin internet en la sala).

- Los tres casos representados como ríos animados: cauces paralelos, un cauce con desvíos en cadena, y compuertas en serie.
- Dentro del caso anidado, un **par de escenas de contraste** con el mismo pasajero —uno que sí tiene pase escolar—: con anidado el cauce del saldo queda seco; con dos `if` sueltos el saldo corre por su propio río y la pregunta se hace igual. El panel incorrecto se ve idéntico al caso 1, que es exactamente el punto.
- Mascota: el logo de Python en pixel art. Solo se dibuja la serpiente azul; la amarilla se genera rotándola 180°.
- El agua fluye ⟶ en los tramos horizontales y ⟱ en las bifurcaciones (pedido de Diego).
- **Convención de estilo pedida por Diego:** toda condición sobre una variable booleana se escribe con `== True` explícito (`if hay_mensaje_nuevo == True:`), para que a los estudiantes les quede claro qué se está comparando. Las comparaciones numéricas quedan tal cual. Es una decisión pedagógica deliberada — no "corregirla" a la forma idiomática de Python.

Verificado en navegador: los 7 canvas con escalado entero, sin desborde horizontal, y la lógica de cada escena comprobada leyendo los píxeles pintados.

---

## Pendientes

- **Escribir la spec** con `disenar-clase` (objetivo + OAs + los 5 pasos). No se hizo en esta sesión por decisión de Diego.
- **Gate abierto que bloquea la clase:** Diego debe revisar los 22 Colabs de devolución de la Evaluación 2 antes de poder entregarlos el lunes. Mientras eso no ocurra, `puntajes_evaluacion2.json` sigue con todos los puntajes en `null`. Ver el plan de revisión en la carpeta de la Clase 19.
- Registrar la fila de esta clase en `Historial-Curricular.md` — corresponde hacerlo al guardar la spec aprobada, no antes.
