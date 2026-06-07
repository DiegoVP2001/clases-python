---
name: referencia-clase-que-sonamos
description: Diseña planificaciones pedagógicas según el modelo “La Clase que Soñamos” de Enseña Chile, usando planificación a la inversa, protagonismo estudiantil, propósito, demostración de aprendizaje y gestión emocional.
---

# Skill: Diseño instruccional — La Clase que Soñamos

## 1. Propósito de la skill

Actúa como un motor de diseño instruccional para generar, revisar o mejorar planificaciones de clase basadas en el modelo **“La Clase que Soñamos”** y en la lógica de **Enseñanza como Liderazgo Colectivo** de Enseña Chile.

La planificación debe concebirse como un ecosistema pedagógico diseñado **retrospectivamente**, es decir, desde la evidencia final de aprendizaje hacia las actividades iniciales. Toda clase debe:

- tener un **propósito claro y significativo**;
- transferir el **protagonismo cognitivo** al estudiante;
- generar **emociones movilizadoras** y un espacio seguro para aprender;
- levantar **evidencia demostrable de aprendizaje**;
- usar contextos, ejemplos y problemas conectados con la identidad, intereses, necesidades y realidad sociocultural del curso.

La clase no debe limitarse a “pasar contenido”. Debe diseñar una experiencia donde los estudiantes comprendan **para qué aprenden**, practiquen activamente, demuestren lo aprendido y reflexionen sobre su proceso.

---

## 2. Cuándo usar esta skill

Usa esta skill cuando el usuario pida:

- diseñar una planificación de clase completa;
- mejorar una clase ya existente;
- transformar una idea de clase en una secuencia pedagógica;
- construir una clase con estructura de Enseña Chile;
- planificar usando **Haz Ahora, ICN, Práctica Guiada, Práctica Independiente, Ticket de Salida y Cierre**;
- revisar si una clase está alineada con “La Clase que Soñamos”;
- crear materiales instruccionales para estudiantes, guías, tickets, actividades o secuencias;
- convertir un contenido curricular en una experiencia de aprendizaje con propósito, protagonismo, demostración y emoción;
- ajustar una planificación para que sea más contextualizada, activa, inclusiva y evaluable.

También debe usarse cuando el usuario mencione explícitamente alguno de estos marcos o conceptos:

- “La Clase que Soñamos”;
- Enseña Chile;
- Enseñanza como Liderazgo Colectivo;
- planificación a la inversa;
- ticket de salida como orientador de la clase;
- protagonismo estudiantil;
- propósito de aprendizaje;
- cultura del error;
- metacognición;
- DUA;
- clase de 5 pasos.

## Cuándo omitir esta skill

No es necesario consultarla cuando:

- La tarea es de iteración cosmética sobre un artefacto ya diseñado (ajustes de redacción, formato, typos, errores de indentación) y no toca la estructura pedagógica de 5 pasos ni la alineación objetivo–Ticket de Salida.
- La estructura de la clase ya fue diseñada y aprobada en una sesión anterior, y la tarea actual es generar o ajustar el Colab/PPT a partir del spec aprobado — esa etapa la cubren `generar-colab-clase` y `generar-ppt-clase`.
- La tarea pertenece a un workflow paralelo (ayudantías, revisión de evaluaciones) que no implica diseñar ni revisar la secuencia pedagógica completa de una clase.

---

## 3. Información mínima que debes intentar recopilar

Antes de diseñar la clase, identifica si el usuario entregó estos antecedentes:

| Antecedente | Para qué sirve |
|---|---|
| Curso o nivel | Ajustar complejidad, lenguaje y autonomía esperada. |
| Asignatura o módulo | Definir tipo de habilidades, productos y criterios. |
| Objetivo de aprendizaje, habilidad u OA | Alinear el propósito y la evidencia. |
| Duración de la clase | Distribuir tiempos de manera realista. |
| Contenido específico | Definir conceptos clave de la ICN. |
| Perfil del curso | Contextualizar ejemplos, intereses y nivel de desafío. |
| Producto o evidencia esperada | Construir el Ticket de Salida. |
| Restricciones logísticas | Adaptar actividades a sala, recursos, número de estudiantes, tecnología disponible. |

### Si falta información

Si falta un dato crítico para diseñar con precisión, formula preguntas breves y concretas.  
Si el usuario necesita una respuesta inmediata, avanza con supuestos razonables y decláralos explícitamente en la sección **Supuestos usados**.

No bloquees la planificación por falta de información menor. Resuelve con criterios pedagógicos prudentes.

---

## 4. Principios centrales de diseño

Toda planificación debe integrar transversalmente los cuatro pilares del modelo.

### 4.1 Propósito: dar sentido

El aprendizaje debe responder explícitamente:

> ¿Para qué sirve esto?

Debes vincular el objetivo de la clase con:

- experiencias cotidianas de los estudiantes;
- desafíos reales de su contexto;
- intereses juveniles;
- proyectos personales o comunitarios;
- aspiraciones futuras;
- problemas locales o escolares;
- decisiones que podrían tomar fuera de la clase.

El propósito debe formularse en lenguaje cercano y comprensible para estudiantes, no solo en lenguaje curricular.

#### Regla operativa

Cada clase debe incluir una sección explícita:

```markdown
Propósito para estudiantes:
Hoy aprenderemos esto porque nos permite...
```

Evita propósitos genéricos como:

- “porque entra en la prueba”;
- “porque es parte del currículum”;
- “porque es importante saberlo”.

Estos pueden mencionarse como contexto, pero no deben ser el sentido principal de la clase.

---

### 4.2 Protagonistas: agencia y autonomía

El estudiante debe realizar el trabajo cognitivo y socioemocional más importante de la clase.

Diseña actividades para que más del **50% del tiempo total** esté dedicado a que los estudiantes:

- piensen;
- resuelvan;
- discutan;
- escriban;
- argumenten;
- creen;
- practiquen;
- comparen estrategias;
- tomen decisiones;
- expliquen procesos;
- reciban y usen retroalimentación.

El docente no debe concentrar la clase en exposición frontal. Su rol principal es diseñar, modelar, observar, hacer preguntas, retroalimentar y ajustar.

#### Regla operativa

La suma de **Práctica Guiada + Práctica Independiente + Ticket de Salida** debe ocupar más del 50% de la clase.

---

### 4.3 Demuestran: dominio, evidencia y metacognición

La clase debe hacer visible el aprendizaje.

Los estudiantes deben demostrar no solo el resultado, sino también el proceso utilizado para alcanzarlo. La planificación debe incluir momentos donde puedan:

- explicar cómo pensaron;
- justificar decisiones;
- mostrar procedimientos;
- autoevaluarse;
- comparar su respuesta con criterios de éxito;
- revisar errores;
- transferir lo aprendido a una situación nueva.

Aplica principios del **Diseño Universal de Aprendizaje (DUA)**, ofreciendo múltiples formas de representación, acción, expresión y participación cuando sea pertinente.

#### Regla operativa

Toda planificación debe incluir:

- criterios de éxito claros;
- respuesta ejemplar del Ticket de Salida;
- evidencia observable de aprendizaje;
- una instancia breve de metacognición.

---

### 4.4 Emociones: bienestar y disposición al aprendizaje

La cognición y la emoción son interdependientes. La clase debe cuidar el clima emocional y convertir el error en una fuente legítima de aprendizaje.

Diseña experiencias que incluyan:

- estímulos cautivantes;
- problemas cercanos;
- dinámicas colaborativas;
- humor pertinente;
- recursos visuales, audiovisuales o interactivos;
- oportunidades de logro progresivo;
- espacios para nombrar emociones frente al desafío.

El lenguaje de instrucciones debe ser formal, claro y cercano, evitando tonos punitivos.

#### Regla operativa

Cada clase debe incluir al menos un **chequeo emocional** o una pregunta de cierre que conecte aprendizaje y emoción.

Ejemplos:

- “¿Con qué emoción te vas de esta clase?”
- “¿Qué parte te generó más seguridad?”
- “¿Qué parte te desafió más?”
- “¿Qué error te ayudó a entender mejor?”

---

## 5. Lógica de diseño obligatoria: planificación a la inversa

La clase siempre debe comenzar por el final.

Antes de escribir las actividades cronológicas, define:

1. **Objetivo de la clase**  
   Qué deben aprender o demostrar los estudiantes.

2. **Ticket de Salida**  
   Cómo demostrarán exactamente ese aprendizaje al final.

3. **Criterios de éxito**  
   Qué debe cumplir una respuesta lograda.

4. **Respuesta ejemplar**  
   Qué se espera que produzca un estudiante que logró el objetivo.

5. **Habilidades necesarias para resolver el Ticket**  
   Qué hay que enseñar, modelar y practicar antes del cierre.

Solo después de definir esto, diseña el Haz Ahora, la ICN, la Práctica Guiada y la Práctica Independiente.

---

## 6. Ticket de Salida como brújula de la clase

El **Ticket de Salida (TS)** es el elemento central de la planificación.

No debe ser una actividad decorativa ni una pregunta suelta. Debe ser el instrumento principal para verificar si los estudiantes lograron el objetivo.

### 6.1 Propósito del Ticket de Salida

Debe responder:

> ¿Cómo demostrarán exactamente los estudiantes lo que aprendieron?

El Ticket debe permitir observar evidencia concreta de aprendizaje. Puede adoptar distintos formatos:

- resolución de problema;
- explicación breve;
- selección justificada;
- creación de un ejemplo;
- análisis de caso;
- mini producto;
- reflexión con evidencia;
- corrección de error;
- transferencia a una situación nueva;
- respuesta escrita;
- diagrama, tabla o esquema;
- código breve, si corresponde;
- decisión argumentada.

### 6.2 Requisitos del Ticket de Salida

Todo Ticket de Salida debe cumplir:

- ser breve;
- ser autónomo;
- estar alineado exactamente con el objetivo;
- evaluar la habilidad central de la clase;
- usar un contexto claro;
- incluir criterios de éxito;
- tener una respuesta ejemplar;
- permitir al docente tomar decisiones para la próxima clase.

### 6.3 Alineación retrospectiva

Una vez definido el Ticket de Salida:

- la ICN debe entregar solo los conceptos necesarios para resolverlo;
- la Práctica Guiada debe modelar el tipo de pensamiento que requiere;
- la Práctica Independiente debe preparar a los estudiantes para ejecutarlo de forma autónoma;
- el Cierre debe ayudarles a reconocer cómo llegaron a ese aprendizaje.

Si una actividad no prepara para el Ticket de Salida, debe eliminarse, ajustarse o justificarse.

---

## 7. Estructura esperada de clase

La planificación debe organizarse en la siguiente estructura pedagógica.

> Nota: aunque el Ticket de Salida aparece hacia el final en la ejecución, debe diseñarse primero.

---

### 7.1 Diseño inverso previo

Antes de la secuencia de clase, presenta:

```markdown
## Diseño inverso de la clase

**Objetivo de clase:**  
...

**Propósito para estudiantes:**  
...

**Ticket de Salida:**  
...

**Criterios de éxito del Ticket de Salida:**  
1. ...
2. ...
3. ...

**Respuesta ejemplar esperada:**  
...

**Habilidades necesarias para resolver el Ticket:**  
- ...
- ...
- ...
```

---

### 7.2 Paso 1: Inicio y Haz Ahora

#### Propósito pedagógico

Capturar la atención inmediata, activar conocimientos previos y establecer el propósito transversal de la clase conectándolo con la vida y el contexto de los estudiantes.

#### Diseño operativo

El Haz Ahora debe:

- ser breve;
- ser resoluble al entrar al aula;
- activar ideas previas;
- conectar con una situación concreta;
- poder realizarse sin una explicación larga del docente;
- permitir levantar información inicial del curso;
- preparar cognitivamente para el objetivo.

Puede usar:

- meme;
- noticia local;
- imagen;
- dilema;
- encuesta rápida;
- problema cotidiano;
- mini caso;
- pregunta provocadora;
- error común;
- comparación entre dos opciones;
- ejemplo cercano a la cultura del grupo.

Debe incluir:

- consigna para estudiantes;
- 1 o 2 preguntas simples;
- respuesta o ideas esperadas;
- transición hacia el objetivo y propósito.

#### Formato sugerido

```markdown
### 1. Inicio y Haz Ahora

**Tiempo estimado:** ... minutos

**Consigna para estudiantes:**  
...

**Preguntas del Haz Ahora:**  
1. ...
2. ...

**Respuesta o ideas esperadas:**  
...

**Conexión con el objetivo:**  
...

**Propósito en lenguaje estudiante:**  
...
```

#### Errores a evitar

- iniciar con exposición larga;
- partir copiando el objetivo sin sentido;
- usar una actividad entretenida pero desconectada del aprendizaje;
- hacer preguntas demasiado amplias o vagas;
- usar contextos genéricos que no resuenan con el curso.

---

### 7.3 Paso 2: Introducción al Contenido Nuevo (ICN)

#### Propósito pedagógico

Entregar los fundamentos, conceptos o herramientas necesarias para que los estudiantes puedan iniciar la práctica.

La ICN debe ser concisa, clara y multimodal.

#### Diseño operativo

La ICN debe:

- limitarse a un máximo de **3 conceptos clave**;
- priorizar lo imprescindible para resolver el Ticket de Salida;
- usar explicaciones breves;
- incluir ejemplos visuales, analógicos o digitales;
- representar la información de más de una forma cuando corresponda;
- evitar sobrecarga cognitiva;
- conectar cada concepto con la práctica posterior.

#### Formato sugerido

```markdown
### 2. Introducción al Contenido Nuevo (ICN)

**Tiempo estimado:** ... minutos

**Concepto clave 1:** ...  
Explicación breve: ...  
Ejemplo o apoyo visual: ...

**Concepto clave 2:** ...  
Explicación breve: ...  
Ejemplo o apoyo visual: ...

**Concepto clave 3:** ...  
Explicación breve: ...  
Ejemplo o apoyo visual: ...

**Chequeo rápido de comprensión:**  
...
```

#### Errores a evitar

- incluir más de 3 conceptos centrales;
- transformar la ICN en una clase magistral;
- explicar procedimientos sin mostrar ejemplos;
- usar lenguaje excesivamente técnico sin mediación;
- enseñar contenidos que no serán usados en la práctica o Ticket de Salida.

---

### 7.4 Paso 3: Práctica Guiada (PG)

#### Propósito pedagógico

Proveer andamiaje y modelar el paso a paso de cómo pensar y ejecutar la tarea que luego se exigirá en la Práctica Independiente y en el Ticket de Salida.

La Práctica Guiada debe mostrar no solo qué hacer, sino **cómo pensar**.

#### Diseño operativo

La PG debe:

- tener instrucciones claras en máximo **5 pasos**;
- usar un ejemplo contextualizado;
- aplicar técnica de **modelar el pensamiento** o *Think Aloud*;
- verbalizar decisiones, dudas, criterios y estrategias;
- incluir participación activa del curso;
- seguir un ciclo de **Practicar → Revisar → Practicar**;
- preparar directamente para el Ticket de Salida.

#### Formato sugerido

```markdown
### 3. Práctica Guiada

**Tiempo estimado:** ... minutos

**Desafío guiado:**  
...

**Pasos del modelo docente:**  
1. ...
2. ...
3. ...
4. ...
5. ...

**Modelamiento del pensamiento docente:**  
- “Primero observo... porque...”
- “Decido... porque el criterio dice...”
- “Si me equivoco en..., puedo corregirlo revisando...”

**Participación del curso:**  
...

**Respuesta esperada o solución guiada:**  
...

**Cómo prepara para el Ticket de Salida:**  
...
```

#### Errores a evitar

- modelar solo la mecánica sin explicar el razonamiento;
- resolver todo sin participación del estudiante;
- usar ejemplos abstractos o desconectados;
- hacer una práctica guiada que no se parece al Ticket de Salida;
- saltarse los criterios de éxito.

---

### 7.5 Paso 4: Práctica Independiente (PI)

#### Propósito pedagógico

Consolidar el protagonismo estudiantil mediante un desafío cognitivo autónomo.

Es el momento en que los estudiantes aplican lo modelado, prueban estrategias, cometen errores, corrigen y se preparan para el Ticket de Salida.

#### Diseño operativo

La PI debe:

- concentrar una parte importante del tiempo de clase;
- tener instrucciones observables y secuenciadas;
- incluir límites de tiempo explícitos;
- proponer una tarea con rigor cognitivo;
- conectarse con un contexto pertinente;
- permitir trabajo individual o colaborativo con roles claros;
- entregar criterios de éxito visibles;
- permitir que el docente monitoree evidencia durante la ejecución.

#### Formato sugerido

```markdown
### 4. Práctica Independiente

**Tiempo estimado:** ... minutos

**Consigna para estudiantes:**  
...

**Producto esperado:**  
...

**Instrucciones:**  
1. ...
2. ...
3. ...

**Criterios de éxito:**  
- ...
- ...
- ...

**Modalidad de trabajo:**  
Individual / parejas / grupos con roles.

**Rol del docente durante la práctica:**  
- Monitorear...
- Hacer preguntas...
- Retroalimentar...
- Registrar evidencias...

**Errores esperables y apoyos:**  
| Error esperable | Pregunta o apoyo docente |
|---|---|
| ... | ... |
```

#### Errores a evitar

- interrumpir constantemente al grupo completo;
- convertir la práctica independiente en otra explicación docente;
- entregar tareas de bajo rigor;
- no definir producto observable;
- no dar tiempo suficiente;
- no anticipar errores comunes;
- no conectar la actividad con el Ticket de Salida.

---

### 7.6 Paso 5: Ticket de Salida, Cierre y Metacognición

#### Propósito pedagógico

Verificar el logro del objetivo, hacer consciente el proceso de aprendizaje y consolidar el vínculo entre aprendizaje, estrategia y emoción.

Este paso debe incluir:

1. ejecución autónoma del Ticket de Salida;
2. revisión breve con criterios de éxito;
3. metacognición;
4. chequeo emocional;
5. decisión docente para la próxima clase.

#### Diseño operativo

El cierre no debe ser solo un resumen del profesor. Debe permitir que el estudiante reconozca:

- qué aprendió;
- cómo lo aprendió;
- qué estrategia utilizó;
- qué error le ayudó;
- qué fue fácil o difícil;
- dónde podría usar esto nuevamente;
- con qué emoción termina la clase.

#### Formato sugerido

```markdown
### 5. Ticket de Salida, Cierre y Metacognición

**Tiempo estimado:** ... minutos

**Ticket de Salida para estudiantes:**  
...

**Criterios de éxito:**  
1. ...
2. ...
3. ...

**Respuesta ejemplar esperada:**  
...

**Autoevaluación rápida:**  
Marca tu nivel:
- Lo logré.
- Estoy cerca.
- Necesito apoyo.

**Pregunta metacognitiva:**  
...

**Chequeo emocional:**  
...

**Uso docente de la evidencia:**  
Si la mayoría logra..., la próxima clase...
Si aparecen errores en..., la próxima clase...
```

#### Errores a evitar

- cerrar solo con un resumen docente;
- no aplicar el Ticket de Salida;
- usar un Ticket que no evalúa el objetivo;
- no incluir respuesta ejemplar;
- omitir la reflexión del estudiante;
- no usar la evidencia para decidir próximos pasos.

---

## 8. Criterios de calidad

Antes de entregar una planificación, valida internamente estos criterios.

### 8.1 Alineación a la inversa

Verifica:

- el objetivo coincide exactamente con el Ticket de Salida;
- la ICN enseña lo necesario para resolver el Ticket;
- la PG modela los pasos o estrategias requeridas;
- la PI permite practicar una tarea similar o progresiva;
- el cierre recupera evidencia del aprendizaje.

Pregunta de control:

> ¿Todas las partes de la clase preparan al estudiante para demostrar el objetivo en el Ticket de Salida?

---

### 8.2 Contextualización sociocultural

Verifica:

- los ejemplos son pertinentes para edad, curso y contexto;
- el Haz Ahora conecta con experiencias concretas;
- los problemas evitan abstracciones innecesarias;
- el lenguaje se ajusta al grupo;
- hay conexión con intereses, cultura local o situaciones escolares.

Si el usuario entrega un perfil de intereses, úsalo explícitamente.

Ejemplos de buena contextualización:

- organizar un evento de K-pop para promover conciencia ambiental;
- analizar consumo de agua en lavamanos del liceo;
- crear un presupuesto para una feria escolar;
- programar una app de recordatorios para actividades estudiantiles;
- evaluar datos de asistencia o hábitos cotidianos del curso.

---

### 8.3 Protagonismo estudiantil

Verifica:

- los estudiantes trabajan activamente más del 50% del tiempo;
- hay momentos de discusión, creación o práctica;
- el docente no domina la clase con exposición frontal;
- la PI tiene suficiente tiempo;
- el Ticket requiere producción autónoma.

---

### 8.4 Evidencia demostrable

Verifica:

- hay producto observable;
- hay criterios de éxito;
- hay respuesta ejemplar;
- hay posibilidad de monitorear errores;
- hay metacognición.

---

### 8.5 Tono, bienestar y cultura del error

Verifica:

- las instrucciones son claras, formales y cercanas;
- se evita lenguaje punitivo;
- se presenta el error como información para aprender;
- se incluye chequeo emocional;
- las actividades no ridiculizan ni exponen negativamente a estudiantes.

---

### 8.6 Accesibilidad y DUA

Verifica:

- hay apoyos visuales o ejemplos;
- las instrucciones están secuenciadas;
- la carga cognitiva es razonable;
- se entregan formas claras de participación;
- hay opciones de expresión cuando sea pertinente;
- el lenguaje evita ambigüedades innecesarias.

---

## 9. Formato de salida esperado

Cuando diseñes una planificación completa, usa este formato.

```markdown
# Planificación de clase — [Asignatura / Unidad]

## Datos generales

| Elemento | Detalle |
|---|---|
| Curso | ... |
| Duración | ... |
| Asignatura | ... |
| Unidad o tema | ... |
| Objetivo de aprendizaje / habilidad | ... |
| Recursos | ... |
| Perfil o contexto del curso | ... |

## Supuestos usados

- ...

## Diseño inverso de la clase

**Objetivo de clase:**  
...

**Propósito para estudiantes:**  
...

**Ticket de Salida:**  
...

**Criterios de éxito del Ticket de Salida:**  
1. ...
2. ...
3. ...

**Respuesta ejemplar esperada:**  
...

**Habilidades necesarias para resolver el Ticket:**  
- ...
- ...
- ...

---

## Secuencia de clase

### 1. Inicio y Haz Ahora

**Tiempo:** ... minutos  
**Propósito pedagógico:** ...  
**Consigna para estudiantes:** ...  
**Preguntas:**  
1. ...
2. ...

**Respuesta o ideas esperadas:** ...  
**Transición hacia el objetivo:** ...

---

### 2. Introducción al Contenido Nuevo (ICN)

**Tiempo:** ... minutos  
**Conceptos clave:**  
1. ...
2. ...
3. ...

**Explicación docente breve:** ...  
**Apoyo visual / analógico / digital:** ...  
**Chequeo rápido de comprensión:** ...

---

### 3. Práctica Guiada

**Tiempo:** ... minutos  
**Desafío guiado:** ...  
**Pasos modelados:**  
1. ...
2. ...
3. ...
4. ...
5. ...

**Modelamiento del pensamiento docente:** ...  
**Participación del curso:** ...  
**Respuesta esperada:** ...  
**Conexión con el Ticket de Salida:** ...

---

### 4. Práctica Independiente

**Tiempo:** ... minutos  
**Consigna para estudiantes:** ...  
**Producto esperado:** ...  
**Modalidad:** ...  
**Instrucciones:**  
1. ...
2. ...
3. ...

**Criterios de éxito visibles:**  
- ...
- ...
- ...

**Errores esperables y apoyos docentes:**  

| Error esperable | Pregunta o apoyo docente |
|---|---|
| ... | ... |

---

### 5. Ticket de Salida, Cierre y Metacognición

**Tiempo:** ... minutos  

**Ticket de Salida:**  
...

**Criterios de éxito:**  
1. ...
2. ...
3. ...

**Respuesta ejemplar:**  
...

**Autoevaluación:**  
- Lo logré.
- Estoy cerca.
- Necesito apoyo.

**Pregunta metacognitiva:**  
...

**Chequeo emocional:**  
...

**Uso docente de la evidencia:**  
...

---

## Verificación de calidad

| Criterio | Cumple | Observación |
|---|---:|---|
| Objetivo y Ticket de Salida están alineados | Sí/No | ... |
| La clase fue diseñada a la inversa | Sí/No | ... |
| PG y PI preparan para el Ticket | Sí/No | ... |
| Más del 50% del tiempo es práctica estudiantil | Sí/No | ... |
| Hay propósito claro para estudiantes | Sí/No | ... |
| Hay contextualización sociocultural | Sí/No | ... |
| Hay respuesta ejemplar del Ticket | Sí/No | ... |
| Hay metacognición y chequeo emocional | Sí/No | ... |
| Hay criterios de éxito claros | Sí/No | ... |
| Se evita sobrecarga cognitiva | Sí/No | ... |

## Próximos pasos sugeridos

- ...
```

---

## 10. Formato de salida para revisión de una clase existente

Si el usuario entrega una clase ya diseñada y pide revisión, usa este formato.

```markdown
# Revisión de planificación — La Clase que Soñamos

## Diagnóstico ejecutivo

...

## Fortalezas

1. ...
2. ...
3. ...

## Riesgos pedagógicos detectados

| Riesgo | Por qué afecta la clase | Ajuste recomendado |
|---|---|---|
| ... | ... | ... |

## Revisión por dimensión

| Dimensión | Evaluación | Evidencia | Mejora sugerida |
|---|---|---|---|
| Propósito | ... | ... | ... |
| Protagonistas | ... | ... | ... |
| Demuestran | ... | ... | ... |
| Emociones | ... | ... | ... |

## Revisión de alineación a la inversa

**Objetivo:** ...  
**Ticket de Salida:** ...  
**Nivel de alineación:** Alto / Medio / Bajo  
**Ajuste necesario:** ...

## Versión mejorada de la clase

[Entregar planificación corregida o ajustes puntuales, según lo solicitado.]

## Verificación final

- ...
```

---

## 11. Estilo lingüístico y tono

Todos los materiales dirigidos a estudiantes deben usar un tono:

- formal pero cercano;
- claro;
- empático;
- inclusivo;
- motivador sin exageración;
- orientado a la acción;
- compatible con una cultura del error.

Prefiere formulaciones como:

- “Observemos juntos...”
- “Probemos una estrategia...”
- “El error nos da información para mejorar...”
- “Te invito a justificar tu decisión...”
- “Compara tu respuesta con los criterios...”

Evita formulaciones como:

- “Esto es fácil, no deberían equivocarse.”
- “El que no termina, pierde.”
- “Copien rápido.”
- “Solo memoricen esto.”
- “Si no saben esto, están mal.”

---

## 12. Restricciones y errores que el agente debe evitar

### 12.1 Errores de diseño instruccional

No debes:

- diseñar la clase sin Ticket de Salida;
- escribir el Ticket después de las actividades sin revisar alineación;
- proponer actividades atractivas pero no alineadas al objetivo;
- confundir actividad con aprendizaje;
- omitir criterios de éxito;
- omitir respuesta ejemplar;
- usar prácticas independientes demasiado simples;
- diseñar clases centradas casi por completo en exposición docente;
- dejar el cierre como resumen del profesor;
- omitir metacognición;
- omitir chequeo emocional;
- exceder 3 conceptos clave en la ICN;
- entregar instrucciones largas, ambiguas o no observables;
- usar ejemplos genéricos si hay contexto disponible;
- plantear tareas desconectadas de la realidad del curso.

### 12.2 Errores de tono

No debes:

- usar lenguaje punitivo;
- ridiculizar errores;
- infantilizar a estudiantes;
- usar motivación vacía sin conexión con el propósito;
- imponer emocionalidad artificial;
- escribir instrucciones con exceso de jerga técnica;
- usar un tono excesivamente frío en materiales para estudiantes.

### 12.3 Errores de evaluación

No debes:

- evaluar algo que no fue enseñado o practicado;
- pedir en el Ticket una habilidad distinta del objetivo;
- usar criterios de éxito vagos;
- no declarar qué evidencia observará el docente;
- no indicar cómo se usará la evidencia para la próxima clase.

### 12.4 Errores de contextualización

No debes:

- usar ejemplos de contextos lejanos si hay información local disponible;
- asumir intereses del curso sin declararlo como supuesto;
- usar cultura juvenil de forma caricaturesca;
- forzar contextos que distraen del objetivo;
- crear ejemplos sensibles o potencialmente estigmatizantes.

---

## 13. Reglas de calidad para tiempos

Cuando el usuario entregue duración, distribuye el tiempo con criterio realista.

Para una clase de 80 minutos, una distribución base puede ser:

| Momento | Tiempo sugerido |
|---|---:|
| Inicio y Haz Ahora | 8–10 min |
| ICN | 10–15 min |
| Práctica Guiada | 15–20 min |
| Práctica Independiente | 25–30 min |
| Ticket de Salida, Cierre y Metacognición | 8–12 min |

La distribución puede ajustarse según contenido, nivel, curso y propósito, pero siempre debe proteger:

- ICN breve;
- práctica suficiente;
- Ticket de Salida real;
- cierre metacognitivo.

---

## 14. Reglas de respuesta ante solicitudes ambiguas

Si la solicitud es ambigua:

1. Identifica qué falta.
2. Pregunta solo lo estrictamente necesario.
3. Si el usuario pide avanzar de todos modos, usa supuestos explícitos.
4. Mantén la estructura de diseño inverso.
5. No inventes OA, datos institucionales ni características del curso sin advertirlo.

Ejemplo de respuesta breve ante falta de contexto:

```markdown
Para diseñarla con precisión necesito 3 datos:
1. curso o nivel;
2. contenido u objetivo;
3. duración de la clase.

Si quieres que avance con supuestos, puedo asumir una clase de 80 minutos para 2° medio y dejarlo declarado.
```

---

## 15. Verificación interna obligatoria antes de responder

Antes de entregar cualquier planificación, revisa internamente:

- ¿El objetivo se puede demostrar?
- ¿El Ticket de Salida mide exactamente el objetivo?
- ¿La respuesta ejemplar permite calibrar calidad?
- ¿La ICN enseña solo lo necesario?
- ¿La PG modela el pensamiento, no solo el procedimiento?
- ¿La PI exige autonomía real?
- ¿El estudiante trabaja más que el docente?
- ¿El propósito está escrito en lenguaje estudiante?
- ¿Hay una conexión concreta con el contexto del curso?
- ¿El cierre incluye metacognición?
- ¿Hay chequeo emocional?
- ¿Las instrucciones son claras y observables?
- ¿Hay criterios de éxito?
- ¿Se evitan ejemplos genéricos o descontextualizados?
- ¿La evidencia obtenida sirve para decidir próximos pasos?

Si una respuesta no cumple estos criterios, debes corregirla antes de entregarla.

---

## 16. Prioridad pedagógica final

Cuando debas decidir entre una clase más extensa y una clase más efectiva, prioriza:

1. claridad del objetivo;
2. alineación del Ticket de Salida;
3. protagonismo estudiantil;
4. práctica suficiente;
5. propósito significativo;
6. evidencia observable;
7. bienestar emocional;
8. contextualización sociocultural;
9. cierre metacognitivo.

Una buena clase no es la que incluye más actividades, sino la que logra que los estudiantes puedan demostrar con claridad aquello que se propuso enseñar.
