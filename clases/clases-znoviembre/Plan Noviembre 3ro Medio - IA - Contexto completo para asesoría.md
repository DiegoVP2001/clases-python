# Plan Noviembre 3ro Medio — IA: contexto completo para asesoría

> **Para quién es este documento:** otra IA (o persona) que ayudará a Diego a tomar dos decisiones urgentes sobre el tramo de noviembre con 3ro medio. Está escrito para leerse solo, sin acceso al resto del proyecto. Fecha: 2026-10-31. Estado: **planificación, nada ejecutado**.
>
> **Convención de redacción:** cada concepto técnico va primero en inglés y luego su traducción más cercana al español.
>
> **Privacidad:** no incluye nombres de estudiantes (el repo es público).

---

## 0. Lo que se le pide a la IA asesora

Hay dos decisiones abiertas, y ambas condicionan todo lo demás:

1. **Dinámicas de clase con un codocente de voz.** Diego usará **ChatGPT Voice (modo de voz)** como codocente (co-teacher). Falta decidir **a qué grado** participa y **en qué momentos de la clase** interviene.
2. **Cómo evaluar.** Diego aún no está convencido de ningún formato. La evaluación debe ser **fácil de crear y de corregir**, como ha sido hasta ahora con los Jupyter notebooks: un agente de IA puede crear el instrumento y también revisarlo con **rúbricas claras definidas de antemano**.

Lo que se espera de la IA asesora:
- Un diagnóstico breve de las tensiones que ve entre las restricciones (§3, §4 y §7).
- Para cada decisión, 2 o 3 opciones concretas con sus pros y contras, y **una recomendación directa** (Diego prefiere primero la recomendación y después las alternativas).
- Para cada opción, qué tendría que preparar Diego y cuánto trabajo de creación implica.
- Una lista de datos que le faltan para decidir mejor (ver §9).

---

## 1. Quién es Diego y el contexto del curso

- Profesor de matemáticas y programación en Santiago, Chile (los contextos locales de sus ejemplos usan Isla de Maipo). Hace las clases de Python de 3ro y 4to medio.
- **4to medio ya egresó** (última clase de 4to: jueves 29-oct). Desde noviembre el curso queda **solo con 3ro medio**.
- 3ro medio sale a la universidad en 2028, así que lo de noviembre puede servir de puente hacia lo que viene.
- Ritmo: lunes, martes y jueves, **80 minutos** por sesión. En noviembre se asume que se mantiene (por confirmar).
- Los estudiantes tienen computador en la sala y usan **Google Colab**. Entregan por **Google Classroom**.
- Diego prepara el material con ayuda de agentes de IA (Claude Code) y quiere seguir haciéndolo así.

---

## 2. Estado del curso: qué se ha aprendido

Todo en **Python**, con Colab, en este orden real:

| Bloque | Contenidos |
|---|---|
| Base | Variables, tipos de dato, `print()`, `input()`, booleanos (comparaciones y operadores lógicos) |
| Condicionales | `if` / `else`, `if` anidados, `elif` (evaluación sumativa individual rendida el 2026-07-28) |
| Ciclos (loops) | `for` + `range()`, `for` anidado, `continue` / `break`, `while` (evaluación sumativa el 2026-08-27) |
| Funciones | `def`, parámetros, `return`, uso del valor retornado |
| Strings (cadenas de texto) | Índices y rebanadas (slicing), recorrido con `for`, métodos (`upper()`, `lower()`, `strip()`, `replace()`, `split()`), búsqueda (`in`, `find()`) |
| Listas | Alcance **recortado**: creación, acceso por índice, slicing; sin modificar ni listas anidadas |
| Pandas (octubre, vía proyecto) | Abrir y mirar una tabla, dejarla lista (convertir a número, descartar filas), filtrar, agrupar, ordenar, graficar barras. Se enseñó como **receta de copiar y cambiar parámetros** (6 espacios), no como programación libre |

**Proyecto de cierre de octubre (ABP, aprendizaje basado en proyectos):** cada equipo eligió una base de datos pública chilena (hay 12: educación superior, productos agrícolas, accidentes de tránsito, nacimientos, etc.), formuló una pregunta, la respondió con pandas, la comunicó en un Colab narrado y en un PPT, y la defendió. Hubo **showcase** de 4to (jueves 29-oct) y habrá uno de 3ro (lunes 2-nov).

**Lo que dejó el proyecto (relevante para noviembre):**
- En una clase de trabajo autónomo (37b) **nadie pasó del paso 3**: ~20 de 40 cuadernos quedaron vacíos. Las trabas fueron reescribir la tabla en cada celda, typos y no saber dónde poner el código. Diego respondió **simplificando**: una receta fija de 6 espacios y cuadernos separados (uno de código y uno de texto). Después de eso el trabajo avanzó.
- Lección: la autonomía con consignas abiertas falla en este grupo. Lo que funciona es **un molde cerrado que se llena o se modifica**.
- Por las clases perdidas, la nota del proyecto se midió por **trabajo realizado, no por calidad**. Las notas finales quedaron entre 3,1 y 7,0 en 13 equipos.

**Decisión previa sobre pandas en noviembre:** el plan de IA usa Python **hasta listas y sin pandas**, porque se perdieron clases y el dominio de pandas es frágil. Los datasets serán chicos, acotados y hechos por ellos mismos.

---

## 3. Realidad de aula: asistencia y conducta

Esto es lo que más pesa en el diseño.

- **Baja asistencia en general.** Ejemplos concretos del último trimestre:
  - El martes 6-oct no hubo clase por ausencia masiva a causa de la lluvia.
  - El 29-sep se perdió por una actividad del liceo.
  - En los controles recuperativos finales (tomados el 29-oct), **18 de ~30 estudiantes entregaron trabajo**; el resto devolvió la plantilla en blanco.
  - Hubo estudiantes que faltaron a controles completos y hubo que armar una prueba separada para ellos.
- **Con 3ro solo:** con suerte son **unos 15 estudiantes por sala**, y menos si faltan más.
- **Consecuencia directa:** el trabajo en parejas es riesgoso, porque quien falta deja a su pareja sin compañero. Diego igual querría poder usarlo (la discusión con otro ayuda), pero **ninguna actividad puede depender de que la pareja esté presente**. Regla fija de Diego: ninguna actividad con dependencia entre estudiantes.
- **Dinámica dominante hasta ahora: cuadernos de programación individuales** en Colab. Funciona y es necesaria, pero Diego quiere **explorar otros formatos de creación fácil**, para no gastar tiempo innecesario en producir material.
- **Uso indebido de IA generativa.** En los recuperativos, dos estudiantes recibieron 2,0 por usar ChatGPT para resolver; hubo además casos de posible copia entre pares. Cualquier evaluación futura tiene que contar con que **los estudiantes ya saben recurrir a un chatbot** y con que Diego ya sancionó eso.
- **Régimen de notas (hasta ahora):** escala chilena con exigencia 50% (2,0 a 7,0). En los controles, quien no rinde queda con 2,0 en el Excel de notas; "Pendiente" mientras hay algo por rendir.
- Política de IA: en la clase 37b se abrió con unos 5 minutos de "política de IA" (qué se puede y qué no). Para noviembre cambia la situación, porque ahora la IA es el **tema** y además será parte de la clase.

---

## 4. Modelo de clase que usamos

**Clase regular (martes y jueves), 80 min, siempre con esta estructura de 5 pasos:**

1. **Haz Ahora (Do Now):** calentamiento de unos minutos. Activa conocimiento previo o hace un adelanto sutil del tema **en lenguaje natural, sin mostrar la sintaxis**. Comparte escenario narrativo con la práctica guiada.
2. **ICN (Introducción al Contenido Nuevo):** 2 o 3 conceptos. Cada uno trae una "Idea clave" (la frase que el estudiante anotaría en el cuaderno) y un ejercicio **"Escríbelo tú"**: el cuaderno trae el código incompleto y el estudiante escribe la sintaxis nueva, en vez de solo ejecutar un ejemplo ya hecho. Cierra con una tabla-resumen.
3. **Práctica Guiada:** un ejercicio que se resuelve en conjunto, con el mismo escenario del Haz Ahora.
4. **Práctica Independiente:** 3 ejercicios obligatorios (2 directos y 1 contextualizado y más complejo) + 1 desafío opcional. Cada uno con narrativa breve, lista de "El programa debe:", pistas colapsables y el resultado esperado.
5. **Ticket de Salida (Exit Ticket):** 3 preguntas de alternativas (A/B/C/D) que Diego proyecta una por una; los estudiantes responden en silencio y recién al final envían un Google Form (que además trae una autoevaluación 1-5). Las preguntas nunca van en el cuaderno del estudiante.

**Cierre:** el objetivo se reimprime y se hacen dos preguntas a viva voz: comprensión (escala 1-5) y propósito.

**Elementos que se repiten en cada clase:**
- **Actitud (attitude/trait)** elegida por clase (ej. perseverancia, rigor, método) con una pregunta de propósito. Es el eje socioemocional que se retoma al final.
- Sección **"¿Para qué sirve?"** (máx. 2 frases con ejemplos reales del contenido).
- **Contextos reales y variados** (Isla de Maipo, intereses de los estudiantes), nunca enunciados genéricos de una línea.
- El **PPT** acompaña la exposición y termina en el slide de Cierre; la práctica se trabaja desde el cuaderno.
- Todo el material se genera con scripts a partir de una **especificación aprobada** (Spec); nunca se edita a mano el cuaderno final.

**Lunes estándar (consolidación), 80 min en 3 fases:** sorteo de parejas → **Fase 1: ejercitación** en parejas sorteadas (~45 min, con soluciones colapsadas al final) → **Fase 2: control individual con nota** (~20 min, entrega por Classroom) → **Fase 3: revisión y reflexión** a viva voz (~10 min). Nunca trae contenido nuevo.

**Las voces del material:** español de Chile, voz colectiva ("vamos a", "nos pide"), nunca nombrar a Diego en tercera persona en el material de estudiantes.

---

## 5. Cómo hemos evaluado hasta ahora (la maquinaria que ya existe)

Todo esto funciona y Diego quiere **reutilizarlo** en lo posible:

- **Instrumento = un Jupyter notebook** generado por un script a partir de un JSON o Spec aprobada ("fuente de verdad"). Nunca se edita el `.ipynb` a mano.
- **Tres cuadernos por instrumento:** el del estudiante (sin ninguna solución), un solucionario para el profesor y el corrector, y un solucionario para estudiantes que se publica después de rendido.
- **Rúbrica parcelada por componentes:** el puntaje (100 pts) se reparte en 3 a 5 componentes **independientes** por ítem, cada uno con tres niveles (✅ completo / ⚠️ parcial / ❌ cero). Un componente fallado no arrastra a los demás y un error no se descuenta dos veces.
- **Criterios permanentes de corrección:**
  - Se califica el **comportamiento, no la forma** (no se evalúa eficiencia ni elegancia).
  - Se verifica **ejecutando** el código, nunca leyendo el output pegado.
  - El código del estudiante se extrae **programáticamente** del `.ipynb`, nunca se transcribe a mano.
- **Corrección por un agente de IA** que sigue la rúbrica; los estudiantes pueden reclamar errores de corrección.
- **Devolución:** un cuaderno de Colab personalizado por estudiante (qué se revisó, puntaje, nota).
- **Trazabilidad:** Excel acumulado por estudiante y por sesión (controles y tickets de salida).
- **Antitrampa:** existe una versión impresa (papel, transcripción fiel) de evaluaciones y controles para rendir sin computador.
- **Banco de preguntas de actitud:** cada control o evaluación cierra con una pregunta abierta, sin nota, que ancla la actitud del período a lo que el estudiante hizo (12 preguntas, ninguna respondible con sí/no).

**Qué cambia en noviembre:** el contenido deja de ser programación. Los instrumentos anteriores medían "¿tu código funciona?" y eso se corrige ejecutando. En IA hay que medir **comprensión de conceptos, uso de un modelo y criterio**, y eso se corrige distinto. La maquinaria (generación por script + rúbrica parcelada + corrección por agente + devolución) se puede reutilizar, pero los ítems deben diseñarse de nuevo.

---

## 6. Noviembre: objetivo y secuencia

### 6.1 Objetivo macro (validado por Diego)

> Al terminar noviembre, cada estudiante puede explicar con sus palabras cómo aprende y cómo se equivoca una IA, entrena y evalúa un modelo simple con datos propios, y decide con criterio (4D) cuándo usar, delegar o desconfiar de una IA generativa en su vida de estudiante.

Tres verbos ordenan la secuencia: **Entender**, **Construir**, **Decidir**.

### 6.2 Decisiones ya tomadas

| Tema | Decisión |
|---|---|
| Marco de fondo | **UNESCO** (AI Competency Framework for Students, 2024) solo como verificación de cobertura; los estudiantes no lo ven |
| Lente visible para estudiantes | **4D de AI Fluency:** Delegation (delegación), Description (descripción), Discernment (discernimiento), Diligence (diligencia) |
| Base técnica | Python hasta listas, sin pandas; datasets chicos hechos por ellos |
| Orden conceptual | Cascada: rules (reglas) → Machine Learning (aprendizaje automático) → neural network (red neuronal) / Deep Learning (aprendizaje profundo) → Generative AI (IA generativa) y LLM |
| Herramienta de código | **scikit-learn** desde el inicio (binary y luego multiclass classification) |
| LLM | Una sola sesión **aplicada y discutida** con un **mini-LLM** propio. Nombre del recurso: "Mini-LLM: la misma idea a escala de juguete" (**no** "tu propio ChatGPT") |
| Proyectos | **Ninguno en noviembre**, por directriz del liceo (ausencias y dificultad para cerrar notas). Todo debe resolverse dentro de una sola sesión |
| Evaluación | **Sin definir** |

### 6.3 Las 10 sesiones "seguras"

"Seguras" quiere decir las sesiones que Diego da por confirmadas para el tramo de IA. Con el lunes 2-nov (showcase de 3ro) y el martes 3-nov (pendientes y convivencia de cierre) ocupados, las fechas probables son: **5, 9, 10, 12, 16, 17, 19, 23, 24 y 26 de noviembre**. Esto **no está confirmado**: falta verificar feriados o actividades del liceo en noviembre.

| N° | Tema | Qué se hace (borrador) | Al terminar, el estudiante puede... | Verbo |
|---|---|---|---|---|
| **1** | **El mapa:** IA ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI | Ubican ejemplos reales dentro del mapa, comparan una regla escrita a mano con un patrón aprendido de datos; **intro de las 4D** (15 min) | ubicar ChatGPT en el mapa y explicar la diferencia entre una regla escrita por una persona y un patrón aprendido | Entender |
| **2** | **El pipeline de ML**, sin computador: data → features (variables de entrada) y labels (etiqueta a predecir) → train/test split → algorithm → model | Arman a mano un mini dataset sí/no con datos del propio curso y lo dividen en entrenamiento y prueba | nombrar cada etapa y armar un mini dataset sí/no | Entender |
| **3** | **Primer modelo en scikit-learn:** binary classification, `fit()` / `predict()`, accuracy (exactitud) | Código guiado con un ejemplo simple (horas de estudio → aprobó); luego lo repiten con el dataset del curso | entrenar un modelo sí/no, predecir un caso nuevo y decir qué tan bien acierta | Construir |
| **4** | **La red neuronal:** neuron (neurona) como suma ponderada, weights (pesos), error function, `MLPClassifier` | Discuten qué hace una neurona; cambian el algoritmo de la sesión 3 por `MLPClassifier` y comparan | explicar que "aprender" es ajustar pesos para equivocarse menos | Entender y Construir |
| **5** | **Más de dos categorías:** multiclass classification, confusion matrix (matriz de confusión) | Entrenan un clasificador con 3 o más clases y leen la matriz para ver dónde se confunde | entrenar un clasificador multiclase y decir en qué se confunde y por qué | Construir |
| **6** | **Mini-LLM:** token, next-token prediction (predicción del siguiente token), probabilities, hallucination (alucinación), limitations | Código del mini-LLM con `predict_proba` y generación por sorteo; discuten por qué inventa; cierre comparando con un LLM real | mostrar que un LLM reparte probabilidades y no "sabe", y explicar por qué alucina | Entender y Construir |
| **7** | **Prompting** (cómo escribir buenas instrucciones a una IA): role (rol), task (tarea), context (contexto), output format (formato) + tone, examples, constraints | Reciben la guía de 4 componentes y la plantilla; reescriben un prompt malo hasta dejarlo bueno; comparan la respuesta con el prompt malo y con el bueno; cierre con la D de **Descripción** | escribir un prompt con los 4 componentes y explicar por qué uno más claro da una respuesta más útil | Construir y Decidir |
| **8** | **Ética en un caso real:** bias (sesgo) y privacy (privacidad), con 4D | Leen un caso real, lo analizan con las cuatro D y defienden su postura (por escrito, o frente a un compañero si hay quórum) | analizar un caso real con las cuatro D y defender una postura | Decidir |
| **9** | **Colchón:** ponerse al día, repasar o actividad nueva | Repaso de lo más difícil y espacio para absorber ausencias o imprevistos; opciones: humano vs. máquina, caza de alucinaciones | ponerse al día antes del cierre | — |
| **10** | **Cierre de la secuencia** (formato por definir) | Integrar lo visto (modelo y accuracy, matriz de confusión, límites de un LLM) con una reflexión final con las cuatro D | integrar todo y decidir con criterio cómo usar IA | Entender, Construir y Decidir |

### 6.4 Cómo se explica cada sesión (para decidir dónde interviene la voz)

- **Sesión 1:** es la más conceptual y la más "conversable". La mitad es discusión (¿esto es IA? ¿por qué?). Sirve para ver cómo responde una IA a preguntas de clasificación.
- **Sesión 2:** sin computador, con datos del propio curso. Es la única que no necesita pantalla; temas neutros (horas de sueño, uso del celular, deporte), nunca notas reales de compañeros, salud ni nombres.
- **Sesiones 3, 4 y 5:** son las de código. Se parecen al formato conocido por los estudiantes (Colab, Escríbelo tú, ejemplo visible primero). Se espera que la mayor parte del tiempo sea individual.
- **Sesión 6 (mini-LLM):** tiene un código ya verificado (`CountVectorizer` + `MLPClassifier`). Se observó que el modelo reparte probabilidades, ignora el orden de las palabras, "inventa" ante una palabra que nunca vio y genera frases repetitivas. Preguntas de discusión: ¿por qué responde con seguridad algo que nunca vio? ¿qué pasa si cambiamos el orden? ¿qué cambia si solo lo entrenamos con fútbol?
- **Sesión 7 (prompting):** es la más natural para integrar una IA real, porque el producto de la clase **es** un prompt y su efecto se ve en la respuesta.
- **Sesión 8 (ética):** es la más "hablada". Los casos candidatos son privacidad de conversaciones, algoritmos y violencia real, trabajo humano oculto detrás de la IA e impacto laboral; falta elegir uno (2 globales + 1 local).

---

## 7. Restricciones que cualquier propuesta debe respetar

1. **Ausencia alta:** ninguna actividad puede depender de que otra persona esté presente. El piso de toda actividad es individual; la pareja o el trío suma, pero no es requisito.
2. **Unos 15 estudiantes por sala** (menos si faltan más).
3. **Sin proyectos:** todo se resuelve dentro de una sola sesión.
4. **Esfuerzo de creación bajo para Diego.** Debe poder generarse con un agente de IA a partir de una especificación y revisarse con una rúbrica clara.
5. **Material sin soluciones visibles** antes de rendir (el repo es público); las soluciones salen después.
6. **Sin estudiantes bloqueados** esperando a otro.
7. **Temas sensibles:** evitar salud, peso corporal, notas reales o nombres de compañeros en los datasets.
8. **Cuentas de IA y edad:** Claude.ai exige 18+ y otras herramientas pueden tener restricciones parecidas. Hay que verificar la política del colegio antes de que los estudiantes usen cuentas propias de una IA.
9. El curso viene de varias **clases perdidas** (lluvia, actividades del liceo, feriados), así que el dominio de lo anterior es frágil y conviene no asumir contenidos previos sólidos.

---

## 8. Las dos decisiones, con lo que se sabe

### 8.1 Decisión A — ChatGPT Voice como codocente

**Lo que ya se decidió:** Diego usará ChatGPT Voice como codocente.

**Lo que falta decidir:** a qué **grado** participa y **en qué momentos** de la clase.

**Datos relevantes:**
- Es un **modo de voz conversacional**, pensado para una persona hablando con la IA, no para una sala. Hay que tener en cuenta el ruido de la sala, los turnos de habla y que la IA no distingue voces.
- Probablemente funcione en **una sola cuenta del profesor**, proyectada o con parlante en la sala. Dar cuentas a cada estudiante choca con la restricción de edad y de política del colegio.
- Los LLM **alucinan**, y eso es justamente un contenido de la secuencia (sesión 6). Un codocente que se equivoca en vivo puede ser un recurso pedagógico (ejercer la D de **Discernimiento**) o un riesgo, según cómo se diseñe.
- La regla del PPT de Diego incluye "no ocupen audífonos", y la política de uso de teléfonos y de IA del liceo no está documentada acá.
- Los estudiantes ya mostraron que recurren a chatbots para hacer trampa. Un codocente de IA en el aula cambia ese equilibrio y hay que plantear reglas claras.

**Marco para pensar el "grado" (no son decisiones, son puntos de referencia):**

| Grado | Descripción | Quién opera la voz |
|---|---|---|
| 1. Demostrador | La IA responde a lo que Diego le pide para mostrar un fenómeno (una alucinación, el efecto de un prompt) | Diego |
| 2. Respondedor | Los estudiantes proponen preguntas o prompts; Diego los dicta a la IA y modera la respuesta | Diego, con aportes de la sala |
| 3. Coanfitrión | La IA presenta una parte de la clase (explica, hace preguntas al curso, da retroalimentación) y Diego guía y corrige | Diego y la IA |
| 4. Tutor individual | Cada estudiante habla con una IA propia mientras trabaja | Cada estudiante (probablemente inviable por cuentas) |

**Dónde podría intervenir dentro de la clase** (a evaluar, no es propuesta cerrada): Haz Ahora, explicación del concepto, ejemplo vivo, práctica guiada, retroalimentación de la práctica, ticket de salida o cierre reflexivo. Cada etapa tiene un riesgo distinto.

**Preguntas que la IA asesora debería abordar:**
- ¿Qué grado y qué momentos protegen mejor el aprendizaje de los 15 estudiantes presentes sin depender de la asistencia de nadie?
- ¿Cómo evitar que la voz reemplace el razonamiento del estudiante en lugar de provocarlo?
- ¿Qué reglas de uso deben quedar claras antes de la primera clase?
- ¿Qué pasa si falla la conexión, si la IA se equivoca o si responde algo inapropiado?
- ¿Cómo se integra esto con el cuaderno individual, que es lo que ya funciona?
- ¿Qué se puede hacer sin computador y con la voz sola (sesión 2, sesión 8)?

### 8.2 Decisión B — Cómo evaluar

**Estado:** Diego no está convencido de ningún formato, y por eso se sacó la evaluación del plan (2026-10-31).

**Propuesta anterior (descartada por ahora, no por mala):** 3 controles individuales de unos 15 min al final de las sesiones 3, 5 y 7, cada uno cerrando con una pregunta 4D, más una **prueba de cierre en parejas sorteadas** en la sesión 10 con una situación que integra todo y termina en reflexión 4D, y una versión de reemplazo para quien falte. La dudas: la dependencia de las parejas con tanta ausencia, y que todavía no se sabía bien qué se mide.

**Criterios para elegir un formato** (los que Diego ha repetido):
1. **Fácil de crear:** que un agente de IA lo genere a partir de una especificación, como los cuadernos actuales.
2. **Fácil de corregir:** con **rúbrica clara y definida antes**, corregible por un agente de IA sobre el contenido extraído del notebook, con niveles ✅ / ⚠️ / ❌ y sin ambigüedad.
3. **Se resuelve en una sola sesión** (sin proyectos).
4. **Individual** (o con un piso individual claro), por la ausencia.
5. **Resistente al uso de un chatbot:** tiene que medir algo que un chatbot no resuelva por el estudiante, o que quede visible en el proceso (por ejemplo, el prompt que escribió y cómo juzgó la respuesta).
6. **Compatible con el codocente de voz:** si la voz participa en clase, la evaluación debe medir lo que el estudiante hace por sí mismo o su criterio sobre lo que dice la IA.
7. **Mide lo que importa:** explicar con sus palabras, construir un modelo simple, decidir con criterio (4D).

**Cosas que Diego no ha decidido:**
- Si habrá nota o será formativa (sin nota).
- Con qué ponderación y con qué rúbrica 4D.
- Cómo se maneja al estudiante que falta (versión de reemplazo, nota a partir de lo que sí rindió, etc.).
- Si la evaluación se hace durante la clase o es una sesión aparte.

**Qué se podría aprovechar de lo que ya existe** (a evaluar): rúbrica parcelada, solucionario con criterios para el corrector, devolución en Colab, banco de preguntas de actitud y trazabilidad en Excel. Los controles anteriores medían código; los nuevos tendrían que medir otras cosas (por ejemplo: interpretar la salida de un modelo, justificar un prompt, detectar una alucinación, aplicar las 4D a un caso).

**Preguntas que la IA asesora debería abordar:**
- ¿Qué tipos de ítem se pueden generar y corregir de forma confiable con un agente sin que la rúbrica sea ambigua?
- ¿Qué se puede medir en 15 minutos al final de una clase y qué necesita una sesión completa?
- ¿Cómo se verifica el razonamiento propio frente a un chatbot?
- ¿Cómo se evalúa algo que ocurre en una conversación de voz?
- ¿Con nota o sin nota? ¿Qué pasa con la motivación si no hay nota, dada la asistencia?

---

## 9. Datos que faltan

- Fechas exactas de las 10 sesiones y feriados o actividades del liceo en noviembre.
- Política del colegio sobre IA y edad de las cuentas; si los estudiantes pueden usar una IA propia o solo se usa la del profesor.
- Si el liceo permite grabar o transmitir audio de una IA en sala.
- Si habrá nota por este tramo y cómo se integra al semestre (Diego aún no lo define).
- Cuántos estudiantes de 3ro asisten realmente de forma regular (el "15" es el tope realista que estima Diego).
- Qué caso real se usará en la sesión de ética.
- Qué se hace con Picuino N°29 a N°33 (búsqueda y ordenación): quedó en pausa, sin decidir si se cancela, se pasa a diciembre o se deja como cápsula.
- Si diciembre tendrá clases (no está asegurado).
- Formato de producción de estas clases: el flujo de 5 pasos de siempre o algo más liviano.

---

## 10. Archivos de referencia en el proyecto

Todos dentro de `clases/` del proyecto:
- `clases-znoviembre/Plan Noviembre 3ro Medio - IA - Brainstorm y Checklist.md`: el plan vigente de las 10 sesiones, con el detalle de la sesión 6 (mini-LLM) y de la 7 (prompting).
- `clases-znoviembre/Plan Noviembre 3ro Medio - IA y Aplicaciones.md`: el memo original del 2026-09-23.
- `clases-znoviembre/borrador-clases-1-3/`: borradores docentes de las sesiones 1 a 3.
- `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md`: calendario agosto a noviembre y mecánica de los lunes estándar.
- `Historial-Curricular.md`: qué se enseñó realmente y con qué numeración.
- `OAs-referencia.md`: Objetivos de Aprendizaje (OA) MINEDUC; los de noviembre son OA1, OA4, OA5, OA6 y OAk.

**Fuentes externas que respaldan el plan:** UNESCO AI Competency Framework for Students (2024), OECD + Comisión Europea AI Literacy Framework, AI4K12 Five Big Ideas, curso *AI Fluency for K–12 educators* (4D).
