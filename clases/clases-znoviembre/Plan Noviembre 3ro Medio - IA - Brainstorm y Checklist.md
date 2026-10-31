# Plan Noviembre 3ro Medio — IA: Brainstorm y Checklist

> **Estado: planificación, nada ejecutado.** Complementa `Plan Noviembre 3ro Medio - IA y Aplicaciones.md` (memo del 2026-09-23). Última actualización: 2026-10-31. Contexto: 10 sesiones seguras en noviembre solo con 3ro medio (salen a la universidad en 2028). Convención de redacción: cada concepto técnico va primero en inglés y luego su traducción más cercana al español.

## 1. Decisiones tomadas (2026-10-22)

| Tema | Decisión |
|---|---|
| Fondo pedagógico | Marco **UNESCO** (AI Competency Framework for Students, 2024) como verificación de cobertura; los estudiantes no lo ven |
| Lo visible para estudiantes | **4D de AI Fluency** (Delegation/delegación, Description/descripción, Discernment/discernimiento, Diligence/diligencia) como lente fija de cómo interactúan con IA en todo momento |
| Base técnica | Python hasta listas. **Sin pandas** (se perdieron clases). Datasets chicos, acotados, hechos por ellos |
| Orden conceptual | Cascada: rules (reglas) → Machine Learning (aprendizaje automático) → neural network (red neuronal) / Deep Learning (aprendizaje profundo) → Generative AI (IA generativa) y LLM. Token va con el LLM, no antes |
| Herramienta de código | **scikit-learn desde el inicio**: binary classification (clasificación binaria) y luego multiclass classification (clasificación multiclase) |
| LLM | Una sola sesión, **aplicada y discutida**: un **mini-LLM** propio como "principio de los LLM". Énfasis en que alucina porque predice probabilidades y tiene limitaciones. Sin sesión extra de teoría "del mini al real" |
| Modalidad de clase | Cuaderno individual como dinámica principal; parejas o tríos solo para discusión breve y de forma opcional (ver §1b) |
| Ética | Sesión propia con caso real aplicado usando 4D |
| Evaluación | **Sin definir** (2026-10-31): se saca de la planificación hasta tener claro cómo evaluar |
| Nombre del recurso | "Mini-LLM: la misma idea a escala de juguete". **No** decir "tu propio ChatGPT" (la arquitectura real es otra) |

## 1b. Condiciones reales y restricciones (2026-10-31)

- **Mucha ausencia.** Hay muchas inasistencias, así que el trabajo en parejas es riesgoso: si alguien falta, su pareja queda sin compañero/a de trabajo. Diego igual quisiera poder usarlo, pero ninguna sesión debe depender de que la pareja esté presente.
- **Solo 3ro medio.** Con suerte son unos 15 estudiantes por sala, y menos si faltan más.
- **Dinámica actual: cuadernos de programación individuales.** Ha sido la dinámica principal del curso y sigue siendo necesaria. Aun así, Diego quiere explorar otros formatos de **creación fácil**, para no gastar tiempo innecesario en producir material.
- **Qué implica para el diseño:** cada actividad tiene un piso individual (se puede hacer sola/o) y la pareja o el trío suma, pero no es requisito.

## 2. Objetivo macro (validado)

> **Al terminar noviembre, cada estudiante puede explicar con sus palabras cómo aprende y cómo se equivoca una IA, entrena y evalúa un modelo simple con datos propios, y decide con criterio (4D) cuándo usar, delegar o desconfiar de una IA generativa en su vida de estudiante.**

Tres verbos ordenan toda la secuencia:
- **Entender:** qué es IA, ML y LLM, y cómo aprenden.
- **Construir:** un modelo propio con scikit-learn.
- **Decidir:** usar IA con criterio (4D) y discutir su ética.

## 3. Secuencia de 10 sesiones

| Sesión | Tema | Qué se hace en clase | Objetivo (al terminar, el estudiante puede...) | Verbo |
|---|---|---|---|---|
| **1** | **El mapa:** Artificial Intelligence (IA) ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI | Ubican ejemplos reales dentro del mapa; comparan una regla escrita a mano con un patrón aprendido de datos; **intro 4D** (15 min) | ubicar ChatGPT dentro del mapa y explicar la diferencia entre una regla escrita por una persona y un patrón aprendido de datos | Entender |
| **2** | **El pipeline de ML**, desenchufado: data (datos) → features (variables de entrada) y labels (etiqueta a predecir) → train/test split (división entrenamiento/prueba) → algorithm (algoritmo) → model (modelo) | Sin computador: arman a mano un mini dataset sí/no con datos del propio curso y lo dividen en entrenamiento y prueba | nombrar cada etapa del pipeline y armar un mini dataset sí/no | Entender |
| **3** | **Primer modelo en scikit-learn:** binary classification (clasificación binaria), `fit()`/`predict()`, accuracy (exactitud) | Código guiado en el cuaderno con un ejemplo simple (horas de estudio → aprobó); luego lo repiten con el dataset del curso | entrenar un modelo sí/no, predecir un caso nuevo y decir qué tan bien acierta | Construir |
| **4** | **La red neuronal:** neuron (neurona) como suma ponderada, weights (pesos), error function (función de error), `MLPClassifier` | Discuten qué hace una neurona; cambian el algoritmo del modelo de la sesión 3 por `MLPClassifier` y comparan resultados | explicar qué hace una neurona y que "aprender" es ajustar pesos para equivocarse menos | Entender y Construir |
| **5** | **Más de dos categorías:** multiclass classification (clasificación multiclase), confusion matrix (matriz de confusión) | Entrenan un clasificador con 3 o más clases y leen la matriz para ver dónde se confunde | entrenar un clasificador con 3 o más clases e identificar en cuál se confunde y por qué | Construir |
| **6** | **Mini-LLM:** token (fragmento de texto), next-token prediction (predicción del siguiente token), probabilities (probabilidades), hallucination (alucinación), limitations (limitaciones) | Código del mini-LLM, probabilidades con `predict_proba`, generación con sorteo y discusión en pareja de por qué inventa; cierre comparando con un LLM real | mostrar que un LLM reparte probabilidades y no "sabe", y explicar por qué alucina | Entender y Construir |
| **7** | **Prompting (cómo escribir buenas instrucciones a una IA):** role (rol), task (tarea), context (contexto), output format (formato de salida) + tone (tono), examples (ejemplos), constraints (restricciones) | Reciben la guía de 4 componentes y la plantilla; reescriben un prompt malo hasta dejarlo bueno; comparan la respuesta de una IA con el prompt malo y con el bueno; cierran con la D de **Descripción** (ver §4b) | escribir un prompt con los 4 componentes y explicar por qué un prompt más claro da una respuesta más útil | Construir y Decidir |
| **8** | **Ética en un caso real:** bias (sesgo) y privacy (privacidad), con 4D aplicado | Leen un caso real, lo analizan con las cuatro D y defienden su postura (por escrito, o frente a un compañero si hay quórum) | analizar un caso real con las cuatro D y defender una postura | Decidir |
| **9** | **Colchón:** ponerse al día, repasar o actividad nueva si se decide | Repaso de lo que más costó y espacio para absorber ausencias o imprevistos; opciones de actividad en §8 (humano vs. máquina, caza de alucinaciones) | ponerse al día y reforzar los puntos débiles antes del cierre | — |
| **10** | **Cierre de la secuencia** (formato por definir) | Integrar lo visto (modelo y accuracy, matriz de confusión, límites de un LLM) con una reflexión final aplicando las cuatro D; formato por definir | integrar todo lo visto y decidir con criterio (4D) cómo usar IA | Entender, Construir y Decidir |

La evaluación está fuera de la planificación por ahora (ver §6). No hay proyectos en noviembre por directriz del liceo (ausencias, dificultad para cerrar notas): lo que se haga debe resolverse dentro de una sola sesión.

## 4. Detalle de la sesión 6 — Mini-LLM

**Idea:** es el principio de los LLM. Un modelo que, dadas las palabras anteriores, predice la siguiente. Se trabaja en el cuaderno de forma individual, con discusión breve (en parejas/tríos si hay quórum) entre cada bloque de código.

**Código base** (propuesto por Diego; verificado en un entorno aislado el 2026-10-22): `CountVectorizer` + `MLPClassifier(hidden_layer_sizes=(10,))` entrenado con frases cortas donde cada ejemplo es "texto → siguiente palabra".

**Qué se observó al ejecutarlo:**
- `"me gusta"` → `estudiar` 64 %, `aprender` 31 %: el modelo reparte probabilidades.
- `"gusta me"` (orden invertido) → resultado idéntico: ignora el orden de las palabras.
- `"hola"` (palabra que nunca vio) → inventa `gusta` con 45 %: ejemplo directo de alucinación.
- Generación por sorteo según probabilidades → frase repetitiva (`me gusta aprender python python es`).

**Modificaciones acordadas al código:**
1. Ajustar `CountVectorizer` con **todas** las frases (hoy solo ve los prefijos, así que palabras como `matemáticas` o `útil` nunca entran al vocabulario y el modelo no puede continuar después de ellas).
2. Mostrar `predict_proba` (top 3 candidatas con su porcentaje) en vez de solo `predict`.
3. Bucle de generación que agrega una palabra a la vez, sorteando según probabilidades (introduce temperature/temperatura sin nombrarla todavía).
4. Imprimir el vocabulario (`get_feature_names_out()`) para conectar con token. Aclarar: acá el token es una palabra; en los LLM reales suele ser un pedazo de palabra.

**Preguntas de discusión en pares/tríos (borrador):**
- ¿Por qué el modelo responde con seguridad algo que nunca vio?
- ¿Qué pasa si cambiamos el orden de las palabras? ¿Por qué?
- ¿Qué cambia si lo entrenamos solo con frases de fútbol? (garbage in, garbage out / basura entra, basura sale)
- ¿En qué situación real usarías una respuesta así sin verificarla? (conecta con **Discernimiento** del 4D)

**Cierre (≈10 min, discusión y no clase magistral):** comparación mini-LLM vs. real: 7 frases vs. casi todo internet; 10 neuronas vs. miles de millones de parámetros; ignora el orden vs. attention (atención) sobre todo el contexto. Sin entrar a pre-training/fine-tuning como teoría.

## 4b. Detalle de la sesión 7 — Prompting

**Idea:** después del mini-LLM ya saben que un modelo predice la siguiente palabra a partir de lo que recibe. Por eso importa cómo se redacta el prompt: es el contexto con el que el modelo predice. Conecta con la D de **Descripción** (Description) del 4D.

**Material base** (guía breve de prompts de Diego; se adapta a 3ro medio, con ejemplos de su mundo y no de 7.º básico):
- **4 componentes:** role/rol (¿quién quiero que sea la IA?), task/tarea (¿qué necesito que haga?), context/contexto (¿qué información necesita conocer?), output format/formato (¿cómo quiero recibir la respuesta?).
- **3 opcionales:** tone/tono, examples/ejemplos, constraints/restricciones (se agregan solo cuando ayudan a precisar).
- **Plantilla reutilizable** ROL / TAREA / CONTEXTO / FORMATO / OPCIONALES.
- **Recomendaciones:** ser específico, dar contexto relevante sin sobrecargar, iterar si la primera respuesta no sirve.

**Secuencia de la clase (borrador):**
1. Se les muestra un prompt malo ("explícame las ecuaciones") y predicen qué tan útil será la respuesta.
2. Se presentan los 4 componentes y la plantilla.
3. Cada estudiante (con discusión breve si hay quórum) reescribe el prompt malo con los 4 componentes.
4. Comparan la respuesta al prompt malo con la del prompt bueno. Si no se puede usar una IA real, las respuestas van ya impresas o proyectadas.
5. Iteran: ajustan el prompt con tono, ejemplos o restricciones y ven qué cambia.
6. Cierre con la D de Descripción: ¿qué información le faltaba a la IA y cómo lo noté?

**Por qué cabe en cuaderno individual:** el trabajo central es escribir y reescribir prompts, sin depender de una pareja.

## 5. Datasets: ejemplo visible primero, el del curso después

Patrón para sesiones 2-6:
1. **Ejemplo mínimo visible**, aunque sea malo, para ver resultados de inmediato (ej.: 8 filas de horas de estudio → aprobó/reprobó; 7 frases para el mini-LLM).
2. **Ampliarlo con datos del propio curso**: cada pareja/trío aporta 5 filas o frases a una lista común; reentrenan y comparan cuánto mejora (lección: más datos, mejores resultados; garbage in, garbage out).

Precaución: temas neutros (horas de sueño, uso del celular, deporte). Evitar notas reales de compañeros, salud o nombres.

## 6. Evaluación

**Sin definir.** Diego aún no está convencido de cómo evaluar, así que se quita de la planificación (2026-10-31). Antes se había propuesto 3 controles individuales cortos + una prueba de cierre en parejas; ninguna de las dos opciones queda decidida.

Restricciones que cualquier propuesta futura debe respetar (ver §1b): mucha ausencia (no depender de parejas), unos 15 estudiantes por sala y que resolverse dentro de una sola sesión.

## 7. Referencias (qué se toma de cada una)

| Referencia | Uso en el plan |
|---|---|
| [UNESCO — AI Competency Framework for Students (2024)](https://raise.mit.edu/wp-content/uploads/2025/04/391105eng.pdf): 4 dimensiones (mentalidad centrada en lo humano, ética, técnicas y aplicaciones, diseño de sistemas) y 3 niveles (comprender, aplicar, crear) | Fondo pedagógico: revisar que la secuencia cubra las 4 dimensiones |
| [OECD + Comisión Europea — AI Literacy Framework](https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/) (borrador 2025; 4 dominios: interactuar, crear, gestionar, diseñar con IA; alimenta PISA 2029) | Argumento ante el colegio; "gestionar IA" ≈ Delegación |
| [AI4K12 — 5 Big Ideas](https://govtech.com/education/k-12/advisory-group-promotes-5-big-ideas-in-ai-for-k-12-schools) (percepción, representación y razonamiento, aprendizaje, interacción natural, impacto social) | Chequeo conceptual |
| [AI Fluency for K–12 educators](https://academy.claude.com/courses/ai-fluency-for-k-12-educators) (4D) | Lente visible para estudiantes |
| [Day of AI (MIT RAISE)](https://dayofai.org/units/what-is-artificial-intelligence) | Actividades de datos y sesgo a reutilizar |
| Países: [EAU](https://www.arabianbusiness.com/gcc/uae/uae-to-introduce-mandatory-ai-subject-in-schools-from-2025-what-does-this-mean-for-teachers) (IA obligatoria K-12 desde 2025-26) y China (instrucción obligatoria en IA); [panorama](https://www.analyticsinsight.net/education/top-countries-leading-ai-education-in-2026) | Motivación: en otros países ya es asignatura. Fuentes secundarias; Corea del Sur sin confirmar |

## 8. Ideas en reserva (no incluidas por ahora)

- Test de Turing del curso (textos de compañeros vs. IA).
- Red neuronal física: cada estudiante es una neurona con tarjetas.
- RLHF humano: el curso vota entre dos respuestas y "entrena" preferencias.
- Mapa de laboratorios (Anthropic, OpenAI, Google DeepMind, Meta, Mistral, DeepSeek, Latam-GPT) y arena ciega de modelos.
- Gradio en Colab para convertir el modelo en app web.
- Casos locales de ética: data centers y agua en la RM, deepfakes en elecciones, IA en selección laboral.
- Prompt golf (extensión de la sesión 7), bounty de alucinaciones, carta a mi yo universitario 2028.
- Elements of AI (U. Helsinki) como autoestudio con décimas.

## 9. Checklist trazable

**Decidido**
- [x] Cascada conceptual (reglas → ML → red neuronal → generativa/LLM).
- [x] UNESCO como fondo, 4D como lente visible.
- [x] scikit-learn desde el inicio, sin pandas, datasets chicos propios.
- [x] LLM en una sola sesión aplicada (mini-LLM), con foco en probabilidades y alucinación.
- [x] Objetivo macro validado por Diego.
- [x] Sin proyectos en noviembre (directriz del liceo): sesiones 8-9 como colchón, sesión 10 de cierre.
- [x] Sesión 7 de prompting agregada (2026-10-31); ética pasa a la sesión 8 y los dos colchones se fusionan en la sesión 9.
- [x] Evaluación fuera de la planificación hasta definir cómo evaluar (2026-10-31).

**Por decidir**
- [ ] Confirmar fechas exactas de las 10 sesiones y feriados de noviembre.
- [ ] Verificar política de edad/cuentas del colegio para herramientas de IA que usarían los estudiantes (Claude.ai exige 18+).
- [ ] Decidir el destino de Picuino 29–33 (descartar, diciembre o mini-cápsula).
- [ ] Definir cómo evaluar (si habrá nota, con qué instrumento y cómo se maneja la ausencia).
- [ ] Explorar formatos de actividad de creación fácil, distintos del cuaderno de programación individual, para no gastar tiempo en producir material.
- [ ] Elegir el caso real de ética de la sesión 8 (2 globales + 1 local candidatos en el memo original).
- [ ] Decidir qué se hace en la sesión 9 y en la sesión 10 (hoy: colchón y cierre, formato por definir).
- [ ] Sesión 7: decidir si usan una IA real (depende de la política de edad/cuentas) o respuestas ya impresas/proyectadas.
- [ ] Sesión 7: Diego revisa la guía de prompts adaptada a 3ro medio y los ejemplos elegidos.
- [ ] Decidir el formato de producción de estas clases (flujo `disenar-clase` de 5 pasos o formato más liviano).
- [ ] Actualizar `Plan Cierre...` §6 con la decisión final.
