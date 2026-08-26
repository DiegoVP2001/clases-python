# Investigación freeCodeCamp Python — Ideas para Evaluaciones, Controles y Proyectos

> **Este documento es insumo de investigación, no un documento de decisiones.** Reúne hallazgos verificados (con URL) o marcados explícitamente "de memoria, no verificado" sobre cómo freeCodeCamp diseña su curso de Python (`https://www.freecodecamp.org/learn/python-v9/`). El brainstorm y las decisiones de qué adoptar, adaptar o descartar se hacen en **otra sesión**, partiendo de este archivo. Nada de lo escrito aquí implica un cambio ya resuelto en el proyecto.
>
> **Generado:** 2026-08-18, mediante 3 subagentes de investigación en paralelo (uno por ángulo), orquestados en una sesión de Claude Code. Método de acceso: la URL raíz (`/learn/python-v9/`) es una SPA de React que no devuelve contenido a un fetch simple; el contenido real se obtuvo del código fuente público del curriculum en `github.com/freeCodeCamp/freeCodeCamp` (carpeta `curriculum/`), que es el motor que sirve esa página, más búsquedas web y las páginas públicas de `freecodecamp.org/news` y `freecodecamp.org/certification`.
>
> **Contexto de referencia** (para leer los hallazgos con el mismo marco que se le dio a los agentes): 4to medio, Santiago, 80 min/clase, parejas, todo en Google Colab. Sistema propio ya vigente: flujo de 5 pasos (Haz Ahora → ICN → Práctica Guiada → Práctica Independiente → Ticket de Salida), "lunes estándar" (Ejercitación + Control con nota, rúbrica parcelada por componentes, corrección por agente IA), Evaluación individual sumativa (Solucionario Docente con rúbrica de 3 niveles / Solucionario Estudiantes sin puntajes), autochequeo automático por default. Próximos hitos relevantes: Control de Funciones (lunes 2026-08-24), Evaluación de Ciclos (jueves 2026-08-27), Proyecto OA4 — análisis de datos (oct 2026, 2 sesiones) y Proyecto OA5 — app con IA (oct 2026, 4 sesiones).

---

## 1. Evaluaciones y Controles

*(Agente: diseño de evaluaciones/checks de freeCodeCamp)*

**1.1 — Quiz de opción múltiple con umbral de aprobación 90% (18/20), no simple mayoría.**
Cada bloque de contenido cierra con un quiz de exactamente 20 preguntas, 3 distractores + 1 correcta, con regla explícita de "al menos 18/20 para aprobar".
Fuentes: [quiz-python-basics](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/quiz-python-basics/67f41242431cbf3db8ca79c7.md), [quiz-loops-and-sequences](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/quiz-loops-and-sequences/67f41268a129e63f8e071736.md).
Relevancia: ancla de calibración distinta a la exigencia 50% (escala 2.0-7.0) que usa Diego — punto de contraste si en algún momento se evalúa agregar un instrumento MCQ al Control o a la Evaluación (hoy son 100% programación).

**1.2 — Distractores de quiz como bloques de código casi idénticos, no solo texto.**
Preguntas de predicción de comportamiento con snippets reales (ej. `developer.endswith('N')`, slicing `message[0:6]`), y alternativas que son 4 variantes de código casi iguales (ej. 4 formas de definir una función, solo una válida).
Fuente: mismos quizzes de 1.1.
Relevancia: confirma que el diseño actual del Ticket de Salida de Diego (regla 17: predicción de salida directa, no preguntas truco) ya está alineado con este patrón. El matiz nuevo es usar **4 variantes de código** como alternativas, no solo texto — aplicable a preguntas del Control de Funciones.

**1.3 — Casos de prueba ordenados como progresión pedagógica: típico → borde → "par cercano" con resultado opuesto.**
En los "daily coding challenges" (funciones con `unittest.TestCase`), la secuencia de asserts sigue: (a) caso típico, (b) caso límite (longitud 0, negativo, cero), (c) un par de inputs muy similares con resultados opuestos, diseñado para forzar lógica real y no memorización de patrón (ej. `is_balanced("Lorem Ipsum")` → True vs. `is_balanced("Kitty Ipsum")` → False, mismo formato, distinto conteo real).
Fuentes: [Vowel Balance](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/daily-coding-challenges-python/6814d8e1516e86b171929de4.md), [Unnatural Prime](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/daily-coding-challenges-python/6821ebc9237de8297eaee78f.md) (prime vs. negativo vs. 0 vs. 1, cada uno ataca un error conceptual distinto).
Relevancia: receta concreta para elegir *qué* caso de prueba oculto (`hidden: true`) agregar en un Ítem del Control — no "un caso más" sino uno que descarta específicamente el error de comprensión más probable. Coherente con la regla 17 de Diego sobre que las alternativas/casos deben representar errores de comprensión reales.

**1.4 — El mensaje humano del test siempre va separado del código de aserción.**
Cada hint trae una línea en prosa ("`fibonacci_sequence([0, 1], 0)` should return `[]`.") antes del bloque de test real.
Fuente: [Fibonacci Sequence](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/daily-coding-challenges-python/681cb1a2dab50c87ddb2e514.md).
Relevancia: valida el patrón que Diego ya usa (autochequeo/verificador de salida con mensaje separado del assert) — refuerzo, no idea nueva.

**1.5 — Input "grande" como caso de prueba deliberado para exponer manejo de tipos/rangos, no solo lógica.**
Un test de Fibonacci usa semillas de 9 dígitos, no para subir la dificultad lógica sino para detectar truncamiento/manejo de tipo.
Fuente: mismo Fibonacci de 1.4.
Relevancia: para la Evaluación de Ciclos (for/while/range), un caso con rango grande (ej. `range(0, 500)`) sirve para detectar soluciones que "hardcodean" un resultado corto en vez de iterar correctamente hasta el corte real.

**1.6 — Verificación estructural (AST) solo en pasos guiados, nunca en evaluación sumativa — contraste, no receta a copiar.**
En los tutoriales "learn X by building Y" (52-105 pasos), cada paso verifica la *presencia* de una construcción específica en el código (`_Node(_code).find_function(...).has_stmt(...)`), porque el programa aún está incompleto. Esto es lo opuesto a "se evalúa el comportamiento, no la forma".
Fuente: [Step 11, expense tracker](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/learn-lambda-functions-by-building-an-expense-tracker/65821fcc010c3245718f2a06.md).
Relevancia: freeCodeCamp reserva la verificación estructural exclusivamente para tutoriales guiados paso a paso, nunca para su instancia "que certifica" — esto de hecho **refuerza** que la regla ya vigente de Diego (evaluar comportamiento, no forma, en Control/Evaluación) es la decisión correcta; el patrón AST solo tendría sentido en una Práctica Guiada ultra-fraccionada, no en el Control.

**1.7 — Repaso pre-quiz en formato "cheat sheet" con snippets, no prosa larga.**
Antes del quiz de básicos hay un archivo de repaso con bullets + snippet compacto por concepto.
Fuente: [review-python-basics](https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/blocks/review-python-basics/67f39b40deaec81a3e40e0c5.md).
Relevancia: valida el mecanismo ya vigente (Ejercitación de la Fase 1 antes del Control de la Fase 2 en el lunes estándar) — mismo principio de repaso denso en código ejecutable, no narrativo.

**1.8 — La certificación final (5 proyectos) se evalúa 100% con tests automáticos de comportamiento, cero preguntas de opción múltiple.**
El MCQ queda reservado a los quizzes intra-curso; la instancia "que certifica" es pura programación.
Fuente: [certificación Scientific Computing with Python](https://www.freecodecamp.org/certification/scientific-computing-with-python).
Relevancia: coherente con que la Evaluación sumativa de Diego (más formal que el Control) sea 100% programación sin alternativas — mismo criterio que ya exige la regla del Control ("todos los ítems de programación, nada de alternativas").

**1.9 — (De memoria, no verificado en esta sesión) Revelado progresivo de hints en el editor al fallar un test.**
Comportamiento conocido de la plataforma freeCodeCamp: al fallar, se muestra el mensaje del hint fallido, pero no todos los hints/tests restantes de una vez — se revelan en orden a medida que se pasan los anteriores. No se pudo confirmar contra el markdown fuente (es comportamiento de frontend, no del contenido). **Si interesa este mecanismo, Diego debería verificarlo en la app en vivo antes de adaptarlo.**

---

## 2. Proyectos

*(Agente: diseño de proyectos de certificación de freeCodeCamp — ángulo de mayor interés declarado)*

**2.1 — Estructura de módulo con progresión explícita de andamiaje: Lecciones → Workshop (guiado paso a paso) → Lab (independiente, user stories + tests) → Review → Quiz.**
Ejemplo citado: "Build a Linked List" (workshop) → "Implement the Luhn Algorithm" (lab).
Fuente: [freeCodeCamp's New Python Certification is Now Live](https://www.freecodecamp.org/news/freecodecamps-new-python-certification-is-now-live/).
Relevancia: para el Proyecto OA5 (4 sesiones), sugiere una progresión explícita "guiado con andamiaje → independiente con criterio de aceptación" **dentro de cada sesión**, no solo entre sesiones distintas.

**2.2 — Proyectos "concepto único" antes de los proyectos integradores (capstones).**
La certificación Scientific Computing tiene 15 proyectos: 10 "foundational" de un concepto aislado (ej. "Learn String Manipulation by Building a Cipher", "Learn Classes and Objects by Building a Sudoku Solver") + 5 de certificación que integran varios conceptos.
Fuente: [Python Curriculum 2024 Upgrade](https://www.freecodecamp.org/news/python-curriculum-upgrade/).
Relevancia: para la sesión 1 de OA4/OA5, podría valer diseñar un mini-proyecto de "un concepto, un entregable chico" antes de pedir el proyecto integrador completo, en vez de saltar directo a la tarea grande.

**2.3 — Starter code = contrato de uso de la API, nunca esqueleto de la solución.**
El `main.py` de partida del Budget App no trae clases a medio llenar: trae un script que *usa* la clase que el estudiante debe construir (`food = budget.Category("Food")`, `food.deposit(1000, "initial deposit")`, `food.transfer(50, clothing)`, `print(create_spend_chart([...]))`). El estudiante ve el contrato exacto (nombres de métodos, orden de argumentos, qué se imprime) sin que se le regale la implementación.
Fuente: [boilerplate-budget-app/main.py](https://raw.githubusercontent.com/freeCodeCamp/boilerplate-budget-app/main/main.py).
Relevancia: patrón directamente trasladable al scaffolding de OA4/OA5 — una celda de "ejemplo de uso" al inicio del proyecto en Colab, que muestra cómo se llamaría el código final sin dar la implementación.

**2.4 — Especificación como "user stories" numeradas y testeables, no prosa abierta.**
Cada requisito se redacta como afirmación verificable y numerada, con mapeo 1:1 a un test automático (ej. "La clase Category debe tener un método `deposit(amount, description="")` que agregue `{"amount": amount, "description": description}` al ledger").
Fuentes: [A radically simple approach to user stories](https://www.freecodecamp.org/news/a-radical-simple-approach-to-user-stories/), foro de freeCodeCamp sobre Budget App.
Relevancia: sugiere reemplazar un enunciado narrativo único por una lista numerada de requisitos concretos — más cercano a la rúbrica parcelada por componentes que Diego ya usa en el Control que a un enunciado de ensayo.

**2.5 — Budget App combina OOP + visualización simple de datos sin librerías externas — puente directo a OA4.**
`create_spend_chart()` genera un gráfico de barras ASCII ("Percentage spent by category", eje Y en incrementos de 10, barras de `"o"`, redondeo hacia abajo a la decena más cercana) a partir de transacciones reales, sin `matplotlib`.
Fuente: [README de fuzzyray/budget-app](https://github.com/fuzzyray/budget-app).
Relevancia: referencia de "cuán simple puede ser una visualización que igual se sienta como análisis real" para el Proyecto OA4 (2 sesiones, sin currículo previo de estructura de proyecto en el curso de Diego).

**2.6 — (De memoria, contenido estable y ampliamente documentado, no verificado en vivo esta sesión) Probability Calculator = simulación Monte Carlo con clase + experimento.**
Pide una clase `Hat` con bolitas de colores y una función `experiment()` que hace N repeticiones de sorteo con reposición para estimar una probabilidad empírica, comparándola con el cálculo teórico.
Relevancia: ejemplo de "análisis de datos por simulación" en vez de por dataset externo — alternativa para OA4 si se prefiere generar datos sintéticos (simular un juego o encuesta) en vez de depender de un CSV real, evitando el problema de conseguir datasets chilenos apropiados.

**2.7 — Verificación 100% automática por test individual, no evaluación holística al final.**
Los 5 proyectos de certificación se aprueban solo cuando pasan todos los tests automáticos — sin revisión humana en el camino estándar.
Relevancia: contrasta con el modelo de Diego (revisión humana + rúbrica parcelada), pero valida por qué vale la pena portar el "autochequeo por default" (ya vigente en Independiente) a un proyecto completo en OA4/OA5, dando feedback inmediato por requisito individual y no solo al final.

**2.8 — Certificación = 5 constancias por 5 proyectos, sin examen final tradicional; certificado en URL permanente publicable.**
No hay examen: se certifica con la aprobación de los 5 proyectos + un "Academic Honesty Pledge", con URL pública para LinkedIn/CV.
Fuente: [Python Certifications are Now Live](https://www.freecodecamp.org/news/python-curriculum-is-live/).
Relevancia: para el cierre de año, sugiere una alternativa/complemento a la nota tradicional — un "portafolio con URL" (el repo de GitHub Pages del Proyecto OA5, ya contemplado en el plan) como pieza de cierre presentable.

**2.9 — (De memoria, patrón muy documentado y estable, no verificado en vivo esta sesión) Polygon Area Calculator usa herencia real dentro de un enunciado narrativo.**
Pide una clase `Rectangle` y una clase `Square` que hereda de `Rectangle` y reutiliza sus métodos — el único proyecto de certificación diseñado explícitamente para practicar herencia en un contexto "real" (geometría), no como ejercicio abstracto de sintaxis.
Relevancia: referencia a futuro si el currículo de Diego llega a tocar herencia/POO.

**2.10 — Brecha de investigación: no está documentada públicamente la proporción de tests visibles vs. ocultos por proyecto.**
A diferencia del sistema de Diego (`hidden: true/false` explícito por caso en el JSON), no se encontró fuente que precise esto en freeCodeCamp. **No asumir un dato aquí en el brainstorm** — queda como zona sin verificar.

---

## 3. Presentación de contenido nuevo

*(Agente: cómo freeCodeCamp secuencia lecciones — ángulo de menor prioridad declarado, hallazgos más selectivos)*

**3.1 — Ciclo fijo de 5 tipos de bloque por módulo: Lecture → Workshop → Lab → Review → Quiz.**
Ejemplo real del módulo de condicionales: `lecture-booleans-and-conditionals` → `workshop-movie-ticket-booking-calculator` → `lab-travel-weather-planner` → `review` → `quiz`.
Fuente: [python-v9.json (estructura del curso)](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/structure/superblocks/python-v9.json).
Relevancia: esqueleto similar al de Diego (ICN → Guiada → Independiente) pero con un peldaño intermedio explícito — el *workshop* — mucho más andamiado que la Guiada actual. Podría inspirar una Guiada con más de un checkpoint cuando un concepto es particularmente denso.

**3.2 — La lección (ICN) intercala prosa corta, tabla comparativa y código con resultado como comentario inline (`# True`/`# False`), y cierra con 2-3 preguntas de alternativas antes de tocar código — cada distractor con feedback dirigido a la confusión específica que revela.**
Fuente: [How Do Conditional Statements and Logical Operators Work?](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/challenges/english/blocks/lecture-booleans-and-conditionals/67fe85a3db9bad35f2b6a2bd.md).
Relevancia: cada alternativa incorrecta trae su propia explicación del error de comprensión que representa (no un genérico "inténtalo de nuevo") — trasladable al PPT del Ticket de Salida o a Kahoot, para la revisión oral post-Form.

**3.3 — El "workshop" es un mismo proyecto narrativo partido en 6-9 "Steps" consecutivos: cada uno pide 1-2 líneas nuevas sobre el código ya validado del paso anterior (que aparece "congelado"), con test automático antes de avanzar.**
Ejemplo: "Bill Splitter" — Step 1 crea `running_total = 0`; Step 2 reutiliza ese código y agrega `num_of_friends = 4`; así hasta un programa de 8 pasos.
Fuentes: [Bill Splitter, steps](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/challenges/english/blocks/workshop-bill-splitter/69757cc0faae0152c1418aad.md) y [continuación](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/challenges/english/blocks/workshop-bill-splitter/6976cc0b0c135686a4620b94.md).
Relevancia: el hallazgo más trasladable de este ángulo. Para un concepto con varias partes (ej. condicionales anidados, o un `for` con acumulador + condición), la Guiada podría ofrecerse como 2-3 sub-pasos verificables en vez de un bloque único, sin cambiar el resto del flujo de 5 pasos.

**3.4 — El "lab" es la contraparte abierta: editor casi vacío + user stories numeradas, tests que validan comportamiento, no forma.**
Fuente: [guía oficial "How to Work on Labs"](https://contribute.freecodecamp.org/how-to-work-on-labs/).
Relevancia: valida (no es idea nueva) el gradiente de autonomía que Diego ya aplica de Guiada a Independiente — freeCodeCamp lo separa en dos *bloques* completos (workshop vs. lab), Diego lo hace dentro del mismo notebook.

**3.5 — No hay narrativa/hilo conductor entre lecciones ni módulos — cada workshop resetea a un proyecto/escenario nuevo sin relación temática con el anterior.**
Inferido de la lista de bloques de `python-v9.json` y confirmado en el contenido de los steps.
Relevancia: hallazgo por ausencia. El patrón de Diego de compartir un mismo escenario entre Haz Ahora y Guiada (y a veces entre clases del mismo tema) es más ambicioso que lo que hace freeCodeCamp — no hay nada que copiar acá, pero confirma que es un diferenciador propio del sistema de Diego, no algo que esté dejando pasar.

**3.6 — Las preguntas de lección incluyen un `--video-solution--` con el índice de la respuesta correcta, sugiriendo resolución en video además de texto.**
Fuente: mismo archivo de 3.2.
Relevancia: menor prioridad — confirma que freeCodeCamp trata la verificación de comprensión como multi-modal (texto + video), pero no muy aplicable al setup de Diego (sin video por lección). Hallazgo de contraste, no de adopción directa.

---

## Notas metodológicas y brechas para la sesión de brainstorm

- Ningún agente pudo revisar en profundidad el bloque `quiz` de módulo completo ni el bloque `review` — si el brainstorm quiere profundizar ahí, la fuente sería `curriculum/structure/blocks/quiz-*.json` + su carpeta correspondiente en `curriculum/challenges/english/blocks/`, mismo patrón de acceso vía `raw.githubusercontent.com` usado en toda esta investigación.
- Los hallazgos marcados "de memoria" (1.9, 2.6, 2.9) no fueron verificados en vivo esta sesión — son contenido estable y ampliamente documentado del track de Python de freeCodeCamp, pero conviene confirmarlos en la app antes de basar una decisión de diseño en el detalle exacto.
- La brecha 2.10 (proporción de tests visibles/ocultos) queda explícitamente sin resolver — no asumir un número en el brainstorm.
