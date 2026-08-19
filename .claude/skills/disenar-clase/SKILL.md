---
name: disenar-clase
description: Diseña la especificación pedagógica de una clase de Python siguiendo el flujo de 5 pasos (Haz Ahora, Introducción al Contenido Nuevo, Práctica Guiada, Práctica Independiente, Ticket de Salida). Usa esta skill cuando Diego pida diseñar, planificar, estructurar o iterar una clase del currículo Picuino. Produce un archivo de especificación (Clase NN - Tema - Spec.md) que sirve como contrato para las skills posteriores de generación de Colab y PPT.
---

# Skill: Diseñar clase de Python (flujo 5 pasos)

## Propósito

Producir una especificación pedagógica completa y aprobada para una clase de Python, antes de generar cualquier artefacto. Esta especificación se guarda en `clases/clase-NN-tema/Clase NN - Tema - Spec.md` y es el contrato que consumen las skills generadoras (`generar-colab-clase`, `generar-colab-ejercicios`, `generar-ppt-clase`).

## Cuándo usar esta skill

Actívate cuando Diego:
- Diga que quiere diseñar, planificar o estructurar una clase
- Mencione un número de clase Picuino o un tema del currículo
- Pida iterar sobre un objetivo o estructura ya propuesta
- Quiera cambiar el foco o el contexto de una clase ya especificada

NO te actives cuando Diego pida directamente "genera el Colab" o "genera el PPT". En esos casos, debe existir ya una `Clase NN - Tema - Spec.md` aprobada. Si no existe, indícale que primero hay que diseñar la clase.

## Flujo obligatorio (NO saltes pasos)

### Paso 1 — Confirmar contexto

**Antes que cualquier otra cosa, lee `clases/Historial-Curricular.md`.** Este archivo es la fuente de verdad de lo que Diego efectivamente ha enseñado, en su numeración real — que puede divergir de la numeración Picuino cuando una clase se profundiza, se divide en partes (8a/8b/8c) o se inserta como refuerzo. Te dice:
- Qué número real corresponde a la próxima clase (sección "Próxima clase disponible").
- Qué contenidos y carpetas existen hasta ahora, para no adelantar nada que no se haya visto realmente.

No asumas la numeración real a partir de la numeración Picuino — pueden no coincidir. Si Diego menciona un número que no calza con lo que dice el archivo, pregunta para resolver la discrepancia antes de avanzar.

Luego, asegúrate de tener:

1. **Clase Picuino de referencia** (1 a 33). Consulta la skill `referencia-curriculo` para ver foco, conceptos y actividades de esa clase. Recuerda que el número real (de `Historial-Curricular.md`) y el número Picuino de referencia son cosas distintas — regístralos por separado.
2. **Contenidos previos.** Usa `Historial-Curricular.md` para confirmar exactamente qué se ha visto hasta ahora (no asumas "1 a N-1" mecánicamente). Si hay ambigüedad, confirma brevemente con Diego.
3. **Contexto temático preferido** (opcional). Si Diego no indica, propón 2-3 contextos posibles usando `referencia-intereses-estudiantes`. Si Diego pide contexto de Isla de Maipo o algo local/cotidiano de la comuna, consulta `referencia-isla-de-maipo` para extraer escenarios auténticos (transporte, fiestas, viñas, río, comercio, etc.).
4. **Foco específico.** Si la clase Picuino cubre varios subconceptos, pregunta cuál priorizar. Por ejemplo, la clase 9 (if-else) podría enfocarse en condicionales simples o ya incluir lógica compuesta.

**Defaults** (ver `CLAUDE.md`): no preguntes duración, plataforma, modalidad ni evidencia. Asume 80 min, Google Colab, individual, entrega por Classroom.

### Paso 2 — Detectar sobrecarga de contenidos

Antes de proponer el objetivo, evalúa si lo que Diego quiere cubrir en la clase es UN foco o varios.

Indicadores de sobrecarga (sugiere dividir en dos clases):
- Sintaxis nueva + abstracción nueva (ej: introducir `def` y al mismo tiempo parámetros con valores por omisión)
- Estructura de control + tipo de dato nuevo (ej: `for` + listas en la misma clase)
- Lógica + comunicación (ej: actualización de variables + `print()` avanzado con `sep`/`end`)
- Concepto + depuración compleja
- Contenido nuevo + proyecto creativo extenso

Si detectas sobrecarga, antes de proponer la estructura di algo como:

> "Veo que aquí hay dos focos distintos: X y Y. Recomiendo separarlos en dos clases para que cada una tenga una práctica y una evidencia claras. ¿Quieres que enfoquemos esta clase en X y dejemos Y para la siguiente?"

Espera respuesta. No avances con sobrecarga si Diego no lo aprueba explícitamente.

### Paso 3 — Elegir actitud, y proponer objetivo y propósito

**Primero, ofrece opciones de actitud (obligatorio — no propongas una sola).** Presenta 3-4 actitudes candidatas (ej. Orden, Precisión, Paciencia, Método, Perseverancia, Criterio) con una descripción breve de por qué cada una calza con el contenido específico de la clase, y espera que Diego elija una antes de redactar el objetivo. Usa `AskUserQuestion` o una lista simple en el chat, lo que calce mejor con el resto de la conversación.

Con la actitud elegida, propón el objetivo de aprendizaje con esta estructura:

```
Objetivo: [Verbo observable de Bloom] [contenido específico], [actitud].

Ejemplo: Construir programas con ciclos `for` anidados que generen tablas
y patrones organizados en filas y columnas, con orden.
```

Verbos recomendados (consulta `referencia-bloom` si necesitas calibrar nivel):
- Aplicar: Demostrar, Aplicar, Construir, Usar, Implementar
- Analizar: Comparar, Diferenciar, Examinar, Depurar
- Crear: Diseñar, Crear, Combinar, Construir

Evita verbos no observables: "comprender", "saber", "conocer", "entender".

**Propósito — formato corto (default vigente desde 2026-07-28, Clase 20):** el propósito debe estar escrito para estudiantes, conectar explícitamente con la actitud elegida, y mantenerse **muy concreto y corto — 2 frases, sin enumeraciones ni ejemplos intercalados**:
1. Frase que define la actitud en términos cotidianos para un estudiante de 3ro/4to medio ("El orden es organizar el trabajo en pasos claros, uno dentro de otro, sin mezclarlos.")
2. Frase breve que conecta directamente con el contenido de la clase de hoy ("Hoy lo practicamos anidando ciclos `for`.")

Ejemplo del formato vigente (2 frases, corto): "El orden es organizar el trabajo en pasos claros, uno dentro de otro, sin mezclarlos. Hoy lo practicamos anidando ciclos `for`." (Clase 20, actitud "Orden".)

> **Formato anterior (superado por el default corto, usado hasta Clase 19):** 3 frases — definición de la actitud, proyección **en plural** más allá del liceo ("Esa habilidad nos sirve en cualquier proceso real que..."), y conexión con la clase de hoy. Ofrécelo solo si Diego pide explícitamente un propósito más desarrollado que proyecte la actitud a situaciones de la vida real fuera de la programación — no es el default. Specs anteriores a 2026-07-28 (ej. `clase-13-if-anidadas`, `clase-16-for-range`) usan este formato de 3 frases o el aún más antiguo en singular — no son la referencia vigente.

Presenta objetivo + propósito y espera aprobación o ajuste antes de avanzar.

### Paso 4 — Proponer estructura de 5 pasos

Una vez aprobado el objetivo, propón la estructura completa. NO entregues el código aún, solo la descripción de cada paso con tiempos y propósito.

Estructura obligatoria:

```markdown
## Estructura propuesta — Clase NN: [tema]

**Duración total:** 80 min

### 1. Haz Ahora (5-8 min)
Tiene dos funciones (pueden coexistir):
1. **Calentar** conocimiento previo que será útil en la clase de hoy.
2. **Spoiler sutil**: plantear el problema de la clase en lenguaje cotidiano sin revelar la sintaxis Python — los estudiantes no se dan cuenta de que ya están "haciendo" lo que aprenderán.

**Patrón por defecto — mismo escenario que la Guiada, siempre (default desde Clase 20; validado antes solo para clasificación desde Clase 14).** El Haz Ahora y la Práctica Guiada comparten **el mismo escenario narrativo** — no uno análogo, el mismo — sin importar el tipo de contenido (clasificación/rangos, bucles, funciones, listas, lo que sea). El Haz Ahora presenta el escenario sin código y plantea 2-5 preguntas cerradas y concretas: piden un dato, una cantidad, o qué viene después — resolubles sin ambigüedad y en un par de palabras. Evita preguntas de opinión y evita disyuntivas obvias que telegrafían la respuesta dentro de la propia pregunta (ej. no "¿pasa a la fila 2 o repite la fila 1?" — mejor "¿cuál butaca revisa justo después?"). Cierra la narrativa con un gancho hacia la Guiada, del estilo: "el/la [personaje del escenario], sabiendo de sus habilidades de programación, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:" y ahí van las preguntas. La Guiada retoma el mismo escenario con una pregunta relacionada pero distinta, ya "bajada a código" (ver Paso 3 más abajo).

Regla crítica: **NO revelar explícitamente** el contenido nuevo de hoy. No mostrar operadores, funciones ni sintaxis que se introducirán en el ICN. La actividad puede ser desconectada (papel) o tener una celda de código si es pertinente (para activar algo ya visto).

Duración: usa un número exacto de minutos, no un rango (ej. `(6 min)`, no `(5-8 min)`) — `generar-ppt-clase` lo lee para armar el timer en pantalla del slide (`⚡ Haz Ahora <<6:00>>`). Este timer es exclusivo del Haz Ahora; la Guiada no lleva timer en el PPT porque no se trabaja desde ahí.

**Nunca uses las etiquetas "Propósito:" ni "Actividad:" como texto literal, ni en la propuesta de chat ni en el spec final.** Son categorías de tu propio razonamiento de diseño, no contenido para estudiantes — un bug detectado en Clase 20 mostró que si se escriben en el spec (con o sin negrita), pueden filtrarse literalmente al notebook. Al proponer en el chat, describe la actividad directamente como narrativa + preguntas; si quieres dejar registro del razonamiento de diseño, va en "Decisiones de diseño relevantes" del spec final, nunca en el cuerpo del Haz Ahora.

### 2. Introducción al Contenido Nuevo (15-20 min)
Presentación de cada concepto con DEFINICIÓN + EJEMPLO + IDEA CLAVE.
Cada concepto será un slide rico en el PPT, así que estructúralos bien.
Conceptos a presentar (3-4 máx):
  - Concepto 1: [nombre breve]
  - Concepto 2: [nombre breve]
  - Concepto 3: [nombre breve]
Errores típicos a anticipar: [2-3 errores predecibles para tabla]

### 3. Práctica Guiada (20-25 min)
Construcción CON el curso, en el mismo escenario del Haz Ahora (ver Paso 1), con una pregunta relacionada pero distinta — ya "bajada a código". No entregar código resuelto al inicio. Mismo formato canónico que Independiente (ver Paso 4): narrativa (sin necesidad de etiqueta "Situación") + `**El programa debe:**` en lenguaje natural de alto nivel (describe QUÉ hacer sin revelar nombre exacto de variable ni operador/comando — eso lo aporta la clase) + pista `<details>` opcional si algo lo amerita + resultado esperado.
Situación/narrativa: [retoma el escenario del Haz Ahora]
El programa debe: [bullets de requisitos, en lenguaje natural de alto nivel]
Resultado esperado: [output esperado — un solo bloque si no hay `input()` con valores variables, tabla `Ejemplo 1`/`Ejemplo 2` en **markdown GFM** (`| Ejemplo 1 | Ejemplo 2 |` — nunca `<table>` HTML, que a veces se descuadra en pantalla en Colab) si sí lo hay]

### 4. Práctica Independiente (15-18 min)
Trabajo individual, alineado con la guiada pero NO copia literal. Formato "revisión rápida": ejercicios breves y directos, no problemas extensos multi-parte.
Los enunciados NO incluyen nombres de variables, operadores ni comandos — solo descripción en lenguaje natural de qué calcular. Los ejemplos de input/output usan lenguaje natural ("si alguien ingresa un saldo de \$80.000..."), nunca nombres de variables. Los outputs esperados tienen etiquetas descriptivas. Recuerda escapar el signo peso como `\$` — ver CLAUDE.md restricción 21.
**Presupuesto de palabras (default desde Clase 20 v2, 2026-08-05):** narrativa + bullets apunta a 60-90 palabras por ejercicio (sin contar el resultado esperado), para que los tres obligatorios alcancen a resolverse en el tiempo de la sección — ver CLAUDE.md regla 15/16. El autochequeo (ver abajo) no necesita instrumentación en los bullets: usa el "Verificador por salida" (`generar-colab-clase/SKILL.md`), que revisa lo que el programa imprime, no nombres de variable.
Cantidad de ejercicios: **3 obligatorios (2 directos + 1 contextualizado) + 1 desafío opcional (fijo — no preguntar la cantidad; default desde Clase 24, 2026-08-12 — ver CLAUDE.md regla 16)**. Los obligatorios usan el mismo formato canónico y la misma exigencia de narrativa — ninguno se presenta como bonus ni con narrativa más breve. El desafío (Ejercicio 4) es para quien termine antes los tres obligatorios: mismo formato canónico, con algo más de margen de narrativa que el presupuesto de arriba.
Contextos: [variados entre los ejercicios]
Criterio de logro: [qué evidencia el aprendizaje]

**Autochequeo — default incluido siempre (vigente desde 2026-08-13, salvo que la clase alimente un Control o Evaluación, que no pasan por esta skill).** No preguntar si Diego lo quiere: redacta el spec asumiendo que sí, para cada ejercicio que produzca una secuencia de líneas impresas comparable (el caso normal). Agrega:
- Un bloque `**Celda de configuración:**` en la intro de la sección 4, con el preámbulo reutilizable tal cual (copiarlo sin modificar) — ver "Verificador por salida" en `generar-colab-clase/SKILL.md`.
- Una `**Celda de verificación:**` por ejercicio, con su propia `verificar_ejercicio_N()` y la lista `esperadas` (las líneas exactas que debe imprimir la solución de referencia — se derivan directo del `- Solución:` de ese ejercicio, no hace falta inventarlas aparte).
- Único caso sin `**Celda de verificación:**`: un ejercicio cuyo producto no es una secuencia de líneas impresas (ej. `**Celda de respuesta:**` en markdown, una batería de casos de prueba) — ahí no hay contra qué comparar.
- Para clases de `while`: el verificador re-ejecuta la celda del estudiante, así que un ciclo infinito en su código cuelga también al verificador — riesgo ya aceptado (documentado en `generar-colab-clase/SKILL.md`), no motivo para omitirlo.

### 5. Ticket de Salida (5-8 min)
3 preguntas de alternativas (4 opciones, rotuladas A/B/C/D) sobre lo más importante de la clase — cantidad fija desde Clase 20, no preguntar (si Diego pide explícitamente una 4ta pregunta para una clase puntual, es una excepción de esa clase, no cambia el default — ver CLAUDE.md regla 17). Se responden vía Google Form (ver CLAUDE.md regla 17) — las preguntas y alternativas NO se incluyen en el Colab de clase (solo un aviso de que se proyectan en la tele), van completas solo en el Solucionario.
Cada pregunta lleva un bloque de código breve aludiendo a ella (código como foco — se predice output/comportamiento — o código como referencia — solo ilustra el enunciado conceptual; mezcla ambos entre las preguntas). **Prioriza predicción de salida directa ("¿qué imprime este programa?") sobre preguntas "truco" centradas en un detalle puntual** (default desde Clase 20 v2, 2026-08-05) — las alternativas deben representar errores de comprensión reales, no variaciones cosméticas. Antes de reusar el código de un ejemplo del ICN, confirma que sea algo que Diego realmente va a enseñar/enfatizar — aparecer en el ICN no lo vuelve automáticamente evaluable. Si la pregunta pide identificar una línea específica del código, márcala con un comentario inline (ej. `print()  # <- esta línea`).
Preguntas: [código + enunciado + 4 alternativas (A/B/C/D) + cuál es correcta + justificación breve, para cada una]
Reparte la respuesta correcta en una letra distinta por pregunta — nunca todas caen en la misma alternativa.

### Cierre (5 min)
**Objetivo de la clase:** [copiar el objetivo aprobado]
**Pregunta 1 — Metacognición (escala 1-5):** [donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"]
**Pregunta 2 — Actitud proyectada al futuro:** [pregunta conectada a la actitud del objetivo]
```

Presenta esta estructura completa. **Espera aprobación explícita.** Diego puede pedir ajustes (cambiar contexto, redistribuir tiempos, modificar dificultad). Itera hasta que apruebe.

### Paso 5 — Guardar la especificación

Cuando Diego apruebe la estructura, crea el archivo `clases/clase-NN-tema/Clase NN - Tema - Spec.md` con TODO lo aprobado más metadatos. Usa esta plantilla:

```markdown
# Clase NN — [Tema]

**Estado:** Spec aprobada — [fecha]
**Clase Picuino:** N° NN — [título Picuino]
**URL Picuino:** [URL si aplica]

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** [individual / parejas / grupos]
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** [lista]
- **Contenidos nuevos:** [lista]
- **Contextos temáticos:** [lista]

## Objetivo

[Objetivo aprobado]

## Propósito

[Propósito aprobado, dirigido a estudiantes]

## Estructura de la clase

### 1. Haz Ahora (N min)
[Narrativa del escenario (2-4 líneas) + gancho hacia la Guiada + preguntas numeradas (2-5), sin las etiquetas "Propósito:" ni "Actividad:" — ver Paso 4 arriba. N es un número exacto de minutos (ej. `(6 min)`), no un rango — `generar-ppt-clase` lo usa para el timer del slide.]

1. [pregunta cerrada 1]
2. [pregunta cerrada 2]
3. [pregunta cerrada 3]

**Respuestas esperadas:**
1. [respuesta 1]
2. [respuesta 2]
3. [respuesta 3]

### 2. Introducción al Contenido Nuevo (15-20 min)

**Concepto 1: [nombre breve del concepto]**
- Definición: [Una o dos frases que expliquen qué es y cómo funciona, lenguaje de 4to medio]
- Ejemplo:
  ```python
  [código mínimo que muestra el concepto en acción, 2-4 líneas]
  ```
- Idea clave: [Frase corta que el estudiante debe recordar, lo más importante de este concepto]

**Concepto 2: [nombre breve]**
- Definición: ...
- Ejemplo:
  ```python
  ...
  ```
- Idea clave: ...

**Concepto 3: [nombre breve]**
- Definición: ...
- Ejemplo:
  ```python
  ...
  ```
- Idea clave: ...

[Puedes incluir tantos conceptos como necesite la clase — típicamente 3 a 5, pero
no hay tope. Cada concepto generará un slide propio en el PPT con su definición,
ejemplo de código e idea clave. Si necesitas 6 conceptos para enseñar bien el
tema, agrega 6 conceptos.]

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| ... | ... | ... |

**Regla crítica para escribir el ICN (y todo el spec):**
Cualquier mención a código Python o términos técnicos debe ir entre backticks `así`.
Esto incluye nombres de funciones (`input()`, `print()`, `int()`), tipos
(`str`, `TypeError`, `ValueError`), variables (`nombre_usuario`), operadores
(`+`, `=`), valores literales (`"texto"`, `42`).

El PPT renderiza automáticamente el texto entre backticks en fuente Consolas
color verdoso, dando consistencia visual a todo lo que es código. Si olvidas
backticks, el código aparece en el PPT como texto normal Calibri blanco,
que se ve mal y rompe la marca.

Ejemplos:
- ✅ "La función `input()` siempre devuelve un valor de tipo `str`"
- ❌ "La función input() siempre devuelve un valor de tipo str"

### 3. Práctica Guiada (20-25 min)
[Narrativa (2-4 líneas) que retoma el mismo escenario del Haz Ahora, con una pregunta relacionada pero distinta, ya "bajada a código". Sin etiqueta "Situación:" — el texto libre antes de "El programa debe:" es la narrativa.]

**El programa debe:**
- [requisito 1, en lenguaje natural de alto nivel, sin revelar variable/operador]
- [requisito 2]
- [requisito 3]

[Opcional — pista `<details>` si algo lo amerita, mismo formato que en Independiente más abajo.]

**Resultado esperado:**
```
[output esperado — un solo bloque si no hay input() con valores variables; acórtalo con `...` si es largo y repetitivo]
```

- Solución:
  ```python
  [código de referencia que produce el resultado esperado]
  ```

**Formato antiguo (retrocompatible, solo para regenerar clases previas a Clase 20):** `**Situación:**` + `**Pasos guiados (tabla):**` con un bloque `- Paso N: ... / Resultado: \`\`\`...\`\`\`` por fila, renderizado como tabla de 2 columnas. El parser detecta automáticamente cuál formato usa el spec — no mezclar ambos en una misma clase.

### 4. Práctica Independiente (15-18 min)
**Celda de configuración:**
```python
[preámbulo reutilizable del "Verificador por salida" — copiarlo tal cual desde "Autochequeo" en generar-colab-clase/SKILL.md, sin modificar]
```

**Ejercicio 1 — [contexto]**
[Narrativa 3-4 líneas, formato revisión rápida — nunca "la pareja"/"ustedes" como sujeto de la narrativa ni ninguna otra referencia a la modalidad de trabajo: Diego decide y anuncia la modalidad en vivo, en clase, no el notebook]

**El programa debe:**
- [requisito 1]
- [requisito 2]

[Default siempre desde Clase 24b (2026-08-19) — 1-2 pistas por ejercicio, a criterio de quien diseña:]
<details>
<summary>💡 Pista — [subtítulo]</summary>
[texto orientador]
</details>

[Opcional — `**Nota:**` para una aclaración breve que no cabe en un bullet ni en una pista. Ya no hace falta para pedir nombres de variable exactos — el "Verificador por salida" (`generar-colab-clase/SKILL.md`) no los necesita:]
**Nota:** [aclaración breve]

**Resultado esperado:**
```
[output esperado; si el ejercicio usa input() con valores variables, tabla `Ejemplo 1`/`Ejemplo 2` en markdown GFM en vez de este bloque único — ver formato exacto abajo]
```

[Formato de la tabla cuando hay input() con valores variables — markdown, nunca `<table>` HTML (se descuadra en pantalla en Colab):]
| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`valor1`<br>`valor2` | 📥 *El usuario ingresa:*<br>`valor1`<br>`valor2` |
| 📤 *El programa imprime:*<br>`línea de output` | 📤 *El programa imprime:*<br>`línea de output` |

- Solución:
  ```python
  [código de referencia]
  ```

**Celda de verificación:**
```python
[llamada a verificar_ejercicio_1(), con su propia lista `esperadas` derivada de la solución de arriba — ver "Autochequeo" en generar-colab-clase/SKILL.md. Omitir solo si el ejercicio no produce una secuencia de líneas impresas comparable]
```

**Ejercicio 2 — [contexto distinto]**
[Mismo formato que el Ejercicio 1, incluida su propia `**Celda de verificación:**` — los 3 obligatorios usan el mismo formato canónico (no hace falta escribirlo en el título, ninguno se marca como bonus ni con narrativa más breve)]

**Ejercicio 3 — [contexto contextualizado, más complejo]** *(obligatorio desde Clase 24 — ver CLAUDE.md regla 16)*
[Mismo formato canónico + `**Celda de verificación:**` propia. Narrativa más contextualizada, combina o profundiza el concepto principal — este es también el nivel que fija el techo de dificultad de la Guiada.]

**Ejercicio 4 — Desafío: [contexto]** *(opcional, default desde Clase 24 — ver CLAUDE.md regla 16)*
[Mismo formato canónico + `**Celda de verificación:**` propia, para quien termine antes los tres obligatorios. Puede llevar algo más de narrativa que el presupuesto de palabras de los obligatorios (ver arriba). No adelantes contenido no visto — reutiliza sintaxis ya vista en clases anteriores para el giro extra del desafío.]

### 5. Ticket de Salida (5-8 min)
**Pregunta 1:**
```python
[código breve aludiendo a la pregunta — como foco o como referencia]
```
[enunciado]
- A: [alternativa]
- B: [alternativa]
- C: [alternativa]
- D: [alternativa]
**Respuesta correcta:** [A/B/C/D]
**Justificación:** [explicación breve, para que Diego la use al revelar la respuesta en vivo]

**Pregunta 2:**
```python
[código breve]
```
[enunciado]
- A: [alternativa]
- B: [alternativa]
- C: [alternativa]
- D: [alternativa]
**Respuesta correcta:** [A/B/C/D, distinta de la Pregunta 1]
**Justificación:** [explicación breve]

**Pregunta 3:**
```python
[código breve]
```
[enunciado]
- A: [alternativa]
- B: [alternativa]
- C: [alternativa]
- D: [alternativa]
**Respuesta correcta:** [A/B/C/D, distinta de las Preguntas 1 y 2]
**Justificación:** [explicación breve]

[3 preguntas fijas siempre (default desde Clase 20 — ya no depende de la cantidad de conceptos del ICN). El bloque de código es opcional pero es el default: sin él, la pregunta queda solo como texto conceptual. Si el código debe señalar una línea específica, márcala con un comentario inline (ej. `print()  # <- esta línea`).]

### Cierre (5 min)
**Objetivo de la clase:** [copiar el objetivo aprobado]

**Pregunta 1 — Metacognición (escala 1-5):** [ej: "¿Qué tan seguro/a te sientes usando [tema]?, donde 1 es 'no entendí nada' y 5 es 'puedo explicárselo a otro'"]

**Pregunta 2 — Actitud proyectada al futuro:** [ej: "¿En qué situación real — en otro ramo, en tu vida diaria — podrías usar lo que aprendiste hoy?"]

## Decisiones de diseño relevantes

[Cualquier decisión que valga la pena registrar: por qué este contexto, por qué este nivel de dificultad, qué se descartó y por qué]
```

Crea también la carpeta y un `Clase NN - Tema - Historial.md` inicial:

```markdown
# Historial — Clase NN

## [fecha] — Especificación aprobada
- Objetivo: [resumen]
- Estructura aprobada en N iteraciones
- [notas relevantes del proceso]
```

**Actualiza también `clases/Historial-Curricular.md`:**
1. En la tabla "Clases dictadas y plan curricular completo": si la clase ya existe como fila con estado "Planificada", cambia su estado a "Spec aprobada" y agrega la fecha. Si no existía como fila, agrégala con todos los campos.
2. Recalcula "Próxima clase disponible" apuntando a la siguiente fila "Planificada" de la tabla.

Commitea y pushea **solo la carpeta de esta clase** a GitHub (ver "Protocolo de cierre de etapa" en el `CLAUDE.md` raíz):

```
git add "clases/clase-NN-tema-breve/"
git commit -m "Clase NN - Tema: Spec aprobada"
git push
```

Si el push falla, avisa a Diego con el error explícito — no reintentes con `--force`.

Confirma a Diego que la spec y el historial curricular quedaron guardados y subidos a GitHub. Luego di: *"Antes de continuar al Colab de clase, ejecuta `/compact` para limpiar el contexto. Avísame cuando estés listo."* Cuando confirme, activa la skill `generar-colab-clase`.

## Consultas a skills de referencia

Durante este flujo, consulta proactivamente:

- **`clases/Historial-Curricular.md`**: SIEMPRE primero, antes que cualquier skill — es la fuente de verdad de qué se ha enseñado realmente y con qué numeración. No es una skill, es un archivo de memoria del proyecto; léelo directo.
- **`referencia-curriculo`**: SIEMPRE al inicio, para ver qué dice Picuino sobre esta clase específica (foco, conceptos, sintaxis, actividades originales).
- **`referencia-bloom`**: cuando estés calibrando el verbo del objetivo o evaluando si el ticket de salida tiene la misma demanda cognitiva que el objetivo.
- **`referencia-clase-que-sonamos`**: cuando necesites profundizar en el modelo de 5 pasos, planificación a la inversa o protagonismo estudiantil.
- **`referencia-intereses-estudiantes`**: cuando vayas a proponer contextos temáticos o variables para los ejercicios.

No es necesario consultar todas en cada clase. Consulta lo que aplique.

## Iteración sobre clases ya especificadas

Si Diego pide ajustar una clase que ya tiene `Clase NN - Tema - Spec.md`:

1. Lee el spec actual.
2. Aplica el cambio solicitado.
3. Actualiza la fecha del spec.
4. Registra el cambio en `Clase NN - Tema - Historial.md`.
5. Si el cambio afecta artefactos ya generados (`Clase NN - Tema - Clase.ipynb`, etc.), avisa a Diego que esos archivos están desactualizados y pregunta si quiere regenerarlos.

## Reglas críticas

1. **Nunca generes el .ipynb desde esta skill.** Esta skill produce SOLO el spec. La generación de archivos es responsabilidad de otras skills.
2. **Nunca avances sin aprobación explícita.** "Ok", "sí", "dale", "perfecto", "apruebo", "genera" son señales de aprobación válidas. Ante ambigüedad, pregunta.
3. **Si Diego pide saltarse pasos** (ej: "no me importa el objetivo, genera el Colab directo"), recuérdale brevemente por qué el flujo importa, pero respeta su decisión si insiste. En ese caso, marca el spec con `Estado: Aprobado sin iteración completa` para que quede registrado.
4. **No copies literalmente las actividades Picuino.** Picuino es la referencia conceptual; los ejercicios deben adaptarse al contexto de Diego (estudiantes chilenos de 4to medio, Colab en vez de IDLE, intereses locales).
