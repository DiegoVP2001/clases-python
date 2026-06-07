---
name: referencia-bloom
aliases:
  - taxonomia-bloom
  - bloom
  - demanda-cognitiva
  - niveles-cognitivos
  - verbos-bloom
description: Consulta la Taxonomía de Bloom para calibrar el nivel cognitivo de objetivos, preguntas, tickets de salida, evaluaciones y rúbricas. Usa esta skill cuando necesites elegir un verbo observable para un objetivo de aprendizaje, verificar que un ticket de salida exija la misma demanda cognitiva que el objetivo, o clasificar una actividad según su nivel (recordar, comprender, aplicar, analizar, evaluar, crear).
---

# Skill: Taxonomía de Bloom como referencia para diseño pedagógico

## Propósito de la skill

Esta skill permite que un agente IA use la **Taxonomía de Bloom** como marco de referencia para:

- clasificar la demanda cognitiva de objetivos, actividades, preguntas y evaluaciones;
- redactar objetivos de aprendizaje observables y medibles;
- ajustar actividades para subir o bajar el nivel cognitivo;
- verificar alineación entre objetivo, práctica, ticket de salida, evaluación y rúbrica;
- evitar que una planificación declare un nivel cognitivo alto, pero evalúe solo tareas de recuerdo o repetición.

La skill está diseñada para ser usada como **referencia transversal** por otros agentes o skills de planificación de clases, evaluación, retroalimentación, diseño de rúbricas y construcción de materiales pedagógicos.

---

## Cuándo usar esta skill

Usa esta skill cuando el usuario pida cualquiera de las siguientes tareas:

- crear o revisar objetivos de aprendizaje;
- diseñar actividades, guías, evaluaciones, tickets de salida o preguntas;
- clasificar preguntas por nivel cognitivo;
- subir o bajar la complejidad de una actividad;
- revisar si una evaluación está alineada con el objetivo declarado;
- construir rúbricas o criterios de logro;
- mejorar la progresión de una clase desde tareas simples hacia tareas complejas;
- hacer que una planificación tenga mayor rigor cognitivo;
- distinguir entre recordar, comprender, aplicar, analizar, sintetizar y evaluar;
- adaptar una actividad para distintos niveles de profundidad.

No uses esta skill como único marco pedagógico cuando el usuario haya solicitado explícitamente otro modelo principal, por ejemplo: Diseño Universal de Aprendizaje, Aprendizaje Basado en Proyectos, Clase que Soñamos, PAES, competencias MINEDUC u otro. En esos casos, usa Bloom como **marco auxiliar** para calibrar la demanda cognitiva.

## Cuándo omitir esta skill

No es necesario consultarla cuando:

- La tarea es de iteración cosmética sobre un artefacto ya diseñado (ajustes de redacción, formato, typos) y no toca el verbo del objetivo, la actividad ni la evaluación.
- Diego ya calibró el nivel cognitivo del objetivo en una sesión anterior y no cambió el alcance — basta con mantener la consistencia ya establecida.
- La tarea pertenece a un workflow paralelo (generación de notebooks/PPT, ayudantías, revisión de evaluaciones) que no implica diseñar ni ajustar un objetivo de aprendizaje.

---

## Principios centrales

### 1. El nivel cognitivo depende de la tarea real, no solo del verbo

No clasifiques una actividad únicamente por el verbo usado. El mismo verbo puede pertenecer a distintos niveles según el contexto, la información entregada y la evidencia solicitada.

Ejemplo:

- “Explica la definición de energía” puede ser comprensión básica.
- “Explica por qué una solución tecnológica reduce el desperdicio de agua usando evidencia de una entrevista” puede acercarse a análisis o evaluación.

El agente debe mirar siempre:

1. qué información recibe el estudiante;
2. qué debe producir;
3. qué decisiones cognitivas debe tomar;
4. qué evidencia permite verificar el aprendizaje.

---

### 2. La demanda cognitiva debe estar alineada

Toda tarea debe mantener coherencia entre:

- objetivo de aprendizaje;
- actividad de modelamiento;
- práctica guiada;
- práctica independiente;
- ticket de salida;
- evaluación;
- rúbrica o criterios de logro.

Si el objetivo dice “analizar”, pero el ticket de salida solo pide “nombrar”, hay desalineación.

Si la evaluación pide “evaluar”, pero durante la clase solo se practicó “identificar”, hay salto cognitivo no enseñado.

---

### 3. Los niveles no son una escalera rígida, pero sí una progresión útil

La secuencia base utilizada por esta skill es:

1. Conocimiento
2. Comprensión
3. Aplicación
4. Análisis
5. Síntesis
6. Evaluación

Puede haber clases que combinen niveles. Sin embargo, el agente debe identificar el **nivel predominante** y el **nivel más alto efectivamente exigido**.

---

### 4. Las tareas de mayor nivel requieren criterios explícitos

Para análisis, síntesis y evaluación, el estudiante necesita criterios, evidencias, fuentes, restricciones o condiciones claras.

No basta pedir “evalúa” o “justifica” de manera genérica. Debe explicitarse:

- qué se evalúa;
- con qué criterios;
- desde qué evidencia;
- para qué propósito;
- qué formato debe tener la respuesta.

---

### 5. El rigor cognitivo debe ser enseñado, no solo exigido

Si se espera que el estudiante analice, diseñe, sintetice o evalúe, la planificación debe incluir antes:

- modelamiento del procedimiento;
- ejemplo resuelto;
- criterios de éxito;
- andamiaje inicial;
- oportunidad de práctica;
- retroalimentación o autoevaluación.

---

## Niveles de la Taxonomía de Bloom

### Vista general

| Nivel | Acción cognitiva central | Evidencia observable | Riesgo frecuente |
|---|---|---|---|
| 1. Conocimiento | Recordar o reconocer información | El estudiante nombra, define, identifica, registra o repite información | Confundir memoria con comprensión |
| 2. Comprensión | Entender y explicar significado | El estudiante explica, resume, interpreta, traduce o relaciona ideas | Aceptar explicaciones copiadas sin elaboración propia |
| 3. Aplicación | Usar conocimientos en una situación concreta | El estudiante resuelve, usa, calcula, ejecuta, demuestra o emplea un procedimiento | Aplicar mecánicamente sin entender el criterio de uso |
| 4. Análisis | Descomponer, comparar y establecer relaciones | El estudiante diferencia, clasifica, compara, contrasta, examina o identifica relaciones | Llamar “análisis” a una simple lista |
| 5. Síntesis | Integrar partes para construir algo nuevo | El estudiante diseña, organiza, formula, propone, construye o combina elementos | Pedir creación sin restricciones ni criterios |
| 6. Evaluación | Emitir juicios fundamentados según criterios | El estudiante juzga, valora, selecciona, justifica, revisa o recomienda con evidencia | Pedir opiniones sin criterios explícitos |

---

## Nivel 1: Conocimiento

### Definición operativa

Corresponde a la capacidad de **recordar hechos, términos, métodos, procesos, fórmulas, estructuras o marcos de referencia** sin transformarlos ni elaborarlos en profundidad.

El estudiante demuestra este nivel cuando puede recuperar información en su forma original o reconocerla entre alternativas.

### Verbos asociados

Usa o reconoce verbos como:

- apuntar;
- definir;
- describir;
- encontrar;
- enlistar;
- identificar;
- marcar;
- memorizar;
- nombrar;
- numerar;
- reconocer;
- recordar;
- registrar;
- relatar;
- repetir;
- subrayar.

### Formatos de tarea adecuados

- “Define el concepto de…”
- “Identifica las partes de…”
- “Nombra tres características de…”
- “Reconoce cuál alternativa corresponde a…”
- “Completa la tabla con los términos correctos.”

### Criterios de calidad

Una tarea de conocimiento es correcta si:

- solicita información claramente enseñada o disponible;
- permite verificar si el estudiante recuerda o reconoce el dato;
- no exige interpretación profunda, transferencia ni juicio de valor;
- es breve, precisa y verificable.

### Errores que el agente debe evitar

- Declarar que el estudiante “comprende” solo porque repite una definición.
- Usar tareas de conocimiento como única evidencia de logro en objetivos de análisis, síntesis o evaluación.
- Plantear preguntas memorísticas cuando el propósito declarado exige transferencia.

---

## Nivel 2: Comprensión

### Definición operativa

Corresponde a la capacidad de **entender el significado de información, ideas, procesos o conceptos**, y expresarlos con palabras propias, ejemplos, resúmenes, traducciones o interpretaciones.

El estudiante no solo recuerda: también muestra que entiende la relación básica entre las ideas.

### Verbos asociados

Usa o reconoce verbos como:

- completar;
- descubrir;
- ejemplificar;
- esquematizar;
- explicar;
- expresar;
- identificar;
- informar;
- interpretar;
- listar;
- localizar;
- narrar;
- nombrar;
- organizar;
- predecir;
- preparar;
- reafirmar;
- reconocer;
- relacionar;
- resumir;
- revisar;
- secuenciar;
- traducir;
- transcribir;
- ubicar.

### Formatos de tarea adecuados

- “Explica con tus palabras…”
- “Resume la idea principal de…”
- “Interpreta el significado de…”
- “Da un ejemplo cotidiano de…”
- “Ordena los pasos de…”
- “Relaciona cada concepto con su descripción.”

### Criterios de calidad

Una tarea de comprensión es correcta si:

- exige reformular o explicar, no solo copiar;
- permite observar si el estudiante entiende el significado;
- puede incluir ejemplos, analogías, resúmenes o representaciones;
- no requiere necesariamente resolver un problema nuevo.

### Errores que el agente debe evitar

- Usar “comprender” como verbo de objetivo sin evidencia observable.
- Aceptar respuestas textuales copiadas como evidencia suficiente de comprensión.
- Diseñar una pregunta de comprensión que en realidad solo pide memoria literal.

---

## Nivel 3: Aplicación

### Definición operativa

Corresponde a la capacidad de **usar conocimientos, reglas, métodos, fórmulas, procedimientos o principios en situaciones concretas**.

El estudiante demuestra aplicación cuando puede ejecutar un procedimiento aprendido o transferirlo a un caso particular.

### Verbos asociados

Usa o reconoce verbos como:

- actualizar;
- aplicar;
- calcular;
- cambiar;
- completar;
- construir;
- demostrar;
- dibujar;
- ejecutar;
- emplear;
- esbozar;
- examinar;
- experimentar;
- ilustrar;
- interpretar;
- operar;
- planear;
- practicar;
- programar;
- trazar;
- usar;
- utilizar.

### Formatos de tarea adecuados

- “Resuelve el problema usando…”
- “Aplica el procedimiento para…”
- “Calcula…”
- “Usa la fórmula en el siguiente caso…”
- “Ejecuta el algoritmo con estos datos…”
- “Demuestra cómo se utiliza…”

### Criterios de calidad

Una tarea de aplicación es correcta si:

- presenta una situación concreta;
- exige usar un conocimiento o procedimiento;
- tiene condiciones claras;
- permite observar si el estudiante selecciona y ejecuta correctamente el procedimiento;
- puede incluir transferencia moderada, pero no necesariamente análisis profundo.

### Errores que el agente debe evitar

- Convertir la aplicación en copia mecánica de un ejemplo idéntico.
- Omitir el contexto o los datos necesarios para aplicar el procedimiento.
- Pedir resolución sin haber modelado antes el procedimiento esperado.

---

## Nivel 4: Análisis

### Definición operativa

Corresponde a la capacidad de **descomponer un problema, texto, fenómeno, objeto o situación en partes**, identificando relaciones, patrones, jerarquías, causas, supuestos, diferencias o tensiones entre sus componentes.

El análisis permite comprender cómo se organiza una situación y por qué sus partes se relacionan de cierta manera.

### Verbos asociados

Usa o reconoce verbos como:

- analizar;
- clasificar;
- categorizar;
- comparar;
- contrastar;
- criticar;
- cuestionar;
- debatir;
- diagramar;
- diferenciar;
- discriminar;
- discutir;
- distinguir;
- examinar;
- experimentar;
- explicar;
- identificar;
- inspeccionar;
- investigar;
- organizar;
- probar;
- relatar;
- resolver.

### Formatos de tarea adecuados

- “Compara dos soluciones y explica sus diferencias relevantes.”
- “Clasifica las respuestas según criterios dados.”
- “Identifica causas y consecuencias de…”
- “Distingue hechos, opiniones y supuestos.”
- “Analiza qué partes del problema están conectadas entre sí.”
- “Examina qué evidencia respalda cada conclusión.”

### Criterios de calidad

Una tarea de análisis es correcta si:

- exige separar partes o dimensiones;
- requiere establecer relaciones explícitas;
- usa criterios de comparación o clasificación;
- pide justificar con evidencia;
- no se limita a enumerar información.

### Errores que el agente debe evitar

- Llamar “análisis” a una tarea que solo pide identificar o listar.
- Pedir análisis sin entregar criterios, fuentes, datos o material a analizar.
- Exigir conclusiones sin pedir relaciones entre evidencia y argumento.

---

## Nivel 5: Síntesis

### Definición operativa

Corresponde a la capacidad de **integrar partes, ideas, datos, evidencias o procedimientos para construir un producto, propuesta, modelo, plan, estructura o solución nueva**.

La síntesis implica reorganizar elementos para formar un todo que antes no estaba dado de manera explícita.

### Verbos asociados

Usa o reconoce verbos como:

- arreglar;
- catalogar;
- coleccionar;
- combinar;
- componer;
- construir;
- concluir;
- crear;
- decidir;
- diferenciar;
- dirigir;
- diseñar;
- elegir;
- ensamblar;
- establecer;
- formular;
- influenciar;
- justificar;
- moderar;
- organizar;
- planear;
- preparar;
- priorizar;
- proponer;
- recomendar;
- reunir;
- validar.

### Formatos de tarea adecuados

- “Diseña una propuesta que integre…”
- “Construye un modelo para explicar…”
- “Formula una hipótesis a partir de…”
- “Organiza la información en una estructura nueva.”
- “Propón una solución considerando estas restricciones…”
- “Combina las evidencias para elaborar una conclusión.”

### Criterios de calidad

Una tarea de síntesis es correcta si:

- exige integrar múltiples elementos;
- produce algo nuevo o reorganizado;
- incluye restricciones, propósito y criterios de éxito;
- requiere decisiones justificadas;
- no se reduce a completar una plantilla de manera mecánica.

### Errores que el agente debe evitar

- Pedir “crear” sin criterios de calidad.
- Confundir síntesis con decoración o producción superficial.
- Exigir una propuesta sin datos, restricciones ni usuario objetivo.
- Diseñar actividades creativas sin conexión con el objetivo de aprendizaje.

---

## Nivel 6: Evaluación

### Definición operativa

Corresponde a la capacidad de **formular juicios fundamentados sobre el valor, calidad, pertinencia, efectividad o coherencia de ideas, soluciones, métodos, productos o argumentos**, usando criterios internos o externos.

Puede incluir juicios cuantitativos o cualitativos, siempre que estén fundamentados en evidencia y criterios claros.

### Verbos asociados

Usa o reconoce verbos como:

- apreciar;
- arreglar;
- calificar;
- combinar;
- componer;
- construir;
- crear;
- diseñar;
- elaborar;
- escoger;
- escribir;
- estimar;
- evaluar;
- inventar;
- juzgar;
- medir;
- planear;
- planificar;
- producir;
- reconstruir;
- resolver;
- revisar;
- seleccionar;
- valorar;
- valuar.

### Formatos de tarea adecuados

- “Evalúa cuál solución es más pertinente según los criterios dados.”
- “Justifica qué alternativa elegirías usando evidencia.”
- “Valora la calidad de una propuesta según una rúbrica.”
- “Selecciona la mejor opción y explica por qué.”
- “Revisa el trabajo de un par usando criterios de logro.”
- “Emite un juicio sobre la efectividad de…”

### Criterios de calidad

Una tarea de evaluación es correcta si:

- exige emitir un juicio;
- entrega o solicita criterios claros;
- requiere fundamentar con evidencia;
- permite comparar alternativas, estándares o niveles de logro;
- no se limita a expresar una preferencia personal.

### Errores que el agente debe evitar

- Pedir “opinión” y clasificarla como evaluación.
- Omitir criterios de juicio.
- Aceptar respuestas sin evidencia.
- Evaluar algo que no fue analizado o comprendido previamente.

---

## Flujo operativo para el agente

Cuando uses esta skill, sigue este flujo:

### Paso 1: Identificar la evidencia esperada

Antes de elegir un verbo, determina qué debe demostrar el estudiante.

Preguntas guía:

- ¿Debe recordar información?
- ¿Debe explicar con sus palabras?
- ¿Debe aplicar un procedimiento?
- ¿Debe comparar partes o relaciones?
- ¿Debe construir una propuesta nueva?
- ¿Debe emitir un juicio con criterios?

### Paso 2: Clasificar el nivel cognitivo predominante

Determina el nivel más alto que la tarea realmente exige, no el que declara.

Formato recomendado:

```markdown
Nivel cognitivo predominante: [nivel]
Justificación: [por qué la tarea exige ese nivel]
Nivel cognitivo declarado: [si existe]
Alineación: [alineado / parcialmente alineado / desalineado]
```

### Paso 3: Redactar el objetivo observable

Usa esta estructura:

```text
[Verbo observable] + [contenido o habilidad] + [contexto o condición] + [criterio de logro o evidencia]
```

Ejemplos:

- “Identificar las partes de una entrevista semiestructurada a partir de un ejemplo dado.”
- “Explicar con palabras propias cómo una entrevista permite levantar necesidades reales de un usuario.”
- “Aplicar una pauta de entrevista para formular preguntas abiertas alineadas con un objetivo.”
- “Analizar respuestas de usuarios para distinguir problemas, causas y oportunidades de diseño.”
- “Diseñar una propuesta de solución sustentable integrando evidencia de entrevista y criterios de factibilidad.”
- “Evaluar dos soluciones tecnológicas usando criterios de impacto, viabilidad y pertinencia para el usuario.”

### Paso 4: Alinear actividad y evaluación

Verifica que la actividad enseñe exactamente lo que el instrumento evaluará.

| Elemento | Pregunta de alineación |
|---|---|
| Objetivo | ¿Qué aprendizaje observable se espera? |
| Actividad | ¿Qué práctica permite desarrollar ese aprendizaje? |
| Evaluación | ¿Qué evidencia demuestra que se logró? |
| Criterios | ¿Cómo se distinguirá una respuesta lograda de una incompleta? |

### Paso 5: Ajustar la demanda cognitiva

Si el usuario pide aumentar el rigor, transforma tareas de menor nivel en tareas de mayor nivel.

Ejemplo de progresión sobre un mismo contenido:

| Nivel | Tarea |
|---|---|
| Conocimiento | Nombra tres tipos de residuos presentes en el liceo. |
| Comprensión | Explica por qué esos residuos generan un problema sustentable. |
| Aplicación | Usa una pauta para registrar residuos observados en un recreo. |
| Análisis | Clasifica los residuos según origen, frecuencia y posible causa. |
| Síntesis | Diseña una propuesta para reducir el residuo más frecuente usando los datos levantados. |
| Evaluación | Evalúa dos propuestas y selecciona la más viable según impacto, costo y facilidad de implementación. |

---

## Formato de salida esperado

Cuando el usuario pida aplicar Bloom a una planificación, evaluación o actividad, responde preferentemente con este formato:

```markdown
## Clasificación según Taxonomía de Bloom

| Elemento revisado | Nivel Bloom | Justificación | Ajuste sugerido |
|---|---:|---|---|
| [Objetivo / pregunta / actividad] | [Nivel] | [Razón técnica] | [Mejora concreta] |

## Objetivo ajustado

[Objetivo en formato observable]

## Evidencia esperada

[Producto, respuesta, desempeño o acción verificable del estudiante]

## Criterios de logro

- [Criterio 1]
- [Criterio 2]
- [Criterio 3]

## Versión en menor complejidad

[Versión ajustada hacia niveles más bajos, si corresponde]

## Versión en mayor complejidad

[Versión ajustada hacia niveles más altos, si corresponde]

## Verificación de alineación

| Criterio | Estado | Observación |
|---|---|---|
| Objetivo y actividad están alineados | [Sí / Parcial / No] | [Comentario] |
| Evaluación mide el nivel declarado | [Sí / Parcial / No] | [Comentario] |
| Hay criterios explícitos | [Sí / Parcial / No] | [Comentario] |
| La tarea exige evidencia observable | [Sí / Parcial / No] | [Comentario] |
```

---

## Formato breve de referencia para otros agentes

Cuando otra skill necesite solo una referencia rápida, usa este resumen:

```markdown
Bloom rápido:
1. Conocimiento: recordar, nombrar, identificar, definir.
2. Comprensión: explicar, resumir, interpretar, ejemplificar.
3. Aplicación: usar, calcular, resolver, ejecutar.
4. Análisis: comparar, clasificar, distinguir, relacionar causas y partes.
5. Síntesis: diseñar, construir, formular, proponer integrando elementos.
6. Evaluación: juzgar, valorar, seleccionar o recomendar con criterios y evidencia.

Regla clave: clasifica por la evidencia cognitiva exigida, no solo por el verbo.
```

---

## Criterios de calidad

Antes de entregar una propuesta, el agente debe validar:

1. **Observabilidad:** el objetivo permite ver o recoger evidencia concreta.
2. **Alineación:** actividad, práctica y evaluación exigen el mismo nivel cognitivo o una progresión justificada.
3. **Rigor real:** el nivel declarado coincide con la operación mental solicitada.
4. **Criterios explícitos:** especialmente en análisis, síntesis y evaluación.
5. **Contexto suficiente:** el estudiante cuenta con datos, ejemplos, fuentes o condiciones necesarias.
6. **Andamiaje:** si la tarea es compleja, hay modelamiento previo.
7. **Progresión:** la clase no salta de recuerdo a evaluación sin pasos intermedios.
8. **Lenguaje claro:** las instrucciones son comprensibles y precisas para estudiantes.
9. **Evidencia de aprendizaje:** existe un producto, respuesta o desempeño verificable.
10. **No inflación cognitiva:** no se usan verbos de alto nivel para tareas de bajo nivel.

---

## Restricciones y errores que el agente debe evitar

### Evita clasificar solo por verbo

Incorrecto:

```text
La pregunta dice “analiza”, entonces es nivel análisis.
```

Correcto:

```text
Aunque usa el verbo “analiza”, la tarea solo pide nombrar elementos; por tanto corresponde a conocimiento o comprensión básica.
```

### Evita objetivos no observables

Evita:

```text
Comprender la importancia del reciclaje.
```

Prefiere:

```text
Explicar, con un ejemplo del liceo, por qué la separación de residuos puede reducir el impacto ambiental.
```

### Evita evaluación sin criterios

Evita:

```text
Evalúa la mejor solución.
```

Prefiere:

```text
Evalúa dos soluciones usando criterios de impacto ambiental, factibilidad y pertinencia para el usuario, justificando tu selección con evidencia.
```

### Evita creación superficial

Evita considerar como síntesis una tarea donde el estudiante solo decora, copia o completa una plantilla sin tomar decisiones cognitivas relevantes.

### Evita saltos no enseñados

No diseñes un ticket de salida de evaluación si la clase solo trabajó conocimiento y comprensión.

### Evita ambigüedad en el nivel esperado

Si hay varios niveles, explicita:

- nivel base necesario;
- nivel predominante;
- nivel más alto exigido;
- evidencia que justifica la clasificación.

---

## Integración con planificación de clases

Cuando esta skill se use junto con una skill de planificación, especialmente una planificación basada en ticket de salida, aplica esta regla:

> El ticket de salida debe medir el nivel cognitivo declarado en el objetivo, y las prácticas previas deben preparar explícitamente al estudiante para ese nivel.

Ejemplo:

```markdown
Objetivo: Analizar respuestas de entrevista para identificar necesidades del usuario.
Nivel Bloom: Análisis.
Práctica guiada: modelar cómo separar dato, problema, causa y oportunidad.
Práctica independiente: clasificar respuestas reales o simuladas usando una tabla.
Ticket de salida: analizar una respuesta breve e identificar problema, evidencia y oportunidad.
Criterio de logro: distingue correctamente dato, interpretación y oportunidad de diseño.
```

---

## Plantilla para rediseñar una pregunta según Bloom

```markdown
## Pregunta original

[Texto de la pregunta]

## Diagnóstico

- Nivel declarado: [si existe]
- Nivel real: [nivel]
- Evidencia solicitada: [qué debe producir el estudiante]
- Problema detectado: [si hay desalineación]

## Rediseño por niveles

| Nivel Bloom | Pregunta rediseñada |
|---|---|
| Conocimiento | [versión] |
| Comprensión | [versión] |
| Aplicación | [versión] |
| Análisis | [versión] |
| Síntesis | [versión] |
| Evaluación | [versión] |

## Recomendación

[Indicar qué versión conviene usar según el objetivo pedagógico]
```

---

## Plantilla para revisar una evaluación completa

```markdown
## Mapa cognitivo de la evaluación

| Ítem | Habilidad evaluada | Nivel Bloom | Evidencia exigida | Observación técnica |
|---:|---|---|---|---|
| 1 | [habilidad] | [nivel] | [evidencia] | [comentario] |

## Distribución de niveles

| Nivel Bloom | Cantidad de ítems | Porcentaje aproximado |
|---|---:|---:|
| Conocimiento | [n] | [%] |
| Comprensión | [n] | [%] |
| Aplicación | [n] | [%] |
| Análisis | [n] | [%] |
| Síntesis | [n] | [%] |
| Evaluación | [n] | [%] |

## Diagnóstico

[Conclusión sobre balance, rigor, progresión y alineación]

## Ajustes sugeridos

- [Ajuste 1]
- [Ajuste 2]
- [Ajuste 3]
```

---

## Nota sobre versiones de Bloom

Esta skill usa la secuencia clásica presentada en el documento base:

```text
Conocimiento → Comprensión → Aplicación → Análisis → Síntesis → Evaluación
```

Algunos marcos actuales usan una versión revisada donde “crear” aparece como nivel superior. Si el usuario solicita explícitamente la versión revisada, el agente puede adaptar la nomenclatura, pero debe explicitar el cambio para evitar mezclar ambos sistemas sin aclaración.

