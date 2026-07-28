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

### Paso 3 — Proponer objetivo y propósito

Propón el objetivo de aprendizaje con esta estructura:

```
Objetivo: [Verbo observable de Bloom] [contenido específico] [para + propósito], [actitud].

Ejemplo: Demostrar el uso de condicionales if-else en Python mediante la
construcción de programas que tomen decisiones simples, para automatizar
respuestas según datos de entrada, con perseverancia.
```

Verbos recomendados (consulta `referencia-bloom` si necesitas calibrar nivel):
- Aplicar: Demostrar, Aplicar, Construir, Usar, Implementar
- Analizar: Comparar, Diferenciar, Examinar, Depurar
- Crear: Diseñar, Crear, Combinar, Construir

Evita verbos no observables: "comprender", "saber", "conocer", "entender".

El **propósito** debe estar escrito para estudiantes y responder "¿para qué sirve esto?", proyectándose **más allá del aula y de la programación misma**. No basta con conectar el contenido con otros programas o ejercicios — el propósito debe mostrar cómo lo aprendido se aplica a decisiones, sistemas o situaciones de la vida real fuera del liceo (apps de banco, semáforos, música, deportes, trabajo, etc.). Diego aprobó explícitamente esta orientación: el propósito es agencia y proyección, no solo utilidad técnica.

**Regla crítica — actitud y propósito deben estar conectados:** La actitud del objetivo (ej: `con perseverancia`, `con orden`, `con criterio`) no es decorativa. El propósito **debe nombrarla explícitamente al inicio**, explicar qué significa en lenguaje cotidiano para un estudiante de 3ro y 4to medio, y cerrar mostrando cómo la clase de hoy la ejercita concretamente. Estructura canónica del propósito — **exactamente 3 frases, sin enumeraciones ni ejemplos entre guiones intercalados** (mantenerlo breve y fluido, no una lista de casos):
1. Frase que define la actitud en términos cotidianos ("El orden es la capacidad de...")
2. Frase que la proyecta más allá del liceo, **en plural** — el curso se piensa como colectivo, nunca "te sirve" sino "nos sirve" ("Esa habilidad nos sirve en cualquier proceso real que...")
3. Frase que conecta con la clase de hoy ("Hoy la vamos a ejercitar con `for` y `range()`, donde...")

Ejemplo del formato vigente (3 frases, plural, sin listas intercaladas): "El orden es la capacidad de escribir y organizar el código de manera clara, estructurada y fácil de seguir. Esa habilidad nos sirve en cualquier proceso real que se repita muchas veces, donde la claridad evita errores costosos. Hoy la vamos a ejercitar con `for` y `range()`, construyendo bucles ordenados para generar secuencias numéricas." Specs anteriores a esta fecha (ej. `clase-13-if-anidadas`) usan el formato antiguo en singular — no son la referencia vigente.

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

**Patrón por defecto — alineado con la Guiada (validado en Clase 14):** cuando el foco de la clase es clasificar/decidir entre casos (rangos, categorías, condiciones), el Haz Ahora debe reutilizar **el mismo escenario, tabla o dato** que después aparece en la Práctica Guiada — no uno análogo, el mismo. Los estudiantes resuelven a mano en el Haz Ahora exactamente lo que en la Guiada van a automatizar con código: así el momento "aha" ocurre al notar que ya sabían la lógica, solo faltaba escribirla. Preguntas simples y directas (2-5), resolubles sin ambigüedad y respondibles en un par de palabras en markdown en el cuaderno — no preguntas abiertas de opinión.
Si la clase no tiene ese tipo de foco (ej. bucles, funciones, listas), usa otra variante: predicción de output de código ya visto, detectar un error típico de la clase anterior, o un dilema entre dos formas de resolver algo — mantén siempre la conexión con lo que se hará en la Guiada, aunque no sea la tabla idéntica.

Regla crítica: **NO revelar explícitamente** el contenido nuevo de hoy. No mostrar operadores, funciones ni sintaxis que se introducirán en el ICN. La actividad puede ser desconectada (papel) o tener una celda de código si es pertinente (para activar algo ya visto).

Duración: usa un número exacto de minutos, no un rango (ej. `(6 min)`, no `(5-8 min)`) — `generar-ppt-clase` lo lee para armar el timer en pantalla del slide (`⚡ Haz Ahora <<6:00>>`). Este timer es exclusivo del Haz Ahora; la Guiada no lleva timer en el PPT porque no se trabaja desde ahí.

Propósito: [qué conocimiento previo activa Y/O qué intuición construye para hoy]
Actividad: [descripción breve — papel, predicción, código previo, etc.]

### 2. Introducción al Contenido Nuevo (15-20 min)
Presentación de cada concepto con DEFINICIÓN + EJEMPLO + IDEA CLAVE.
Cada concepto será un slide rico en el PPT, así que estructúralos bien.
Conceptos a presentar (3-4 máx):
  - Concepto 1: [nombre breve]
  - Concepto 2: [nombre breve]
  - Concepto 3: [nombre breve]
Errores típicos a anticipar: [2-3 errores predecibles para tabla]

### 3. Práctica Guiada (20-25 min)
Construcción paso a paso CON el curso. No entregar código resuelto al inicio.
Los pasos se redactan en **lenguaje natural de alto nivel**: describen QUÉ hacer sin revelar el nombre exacto de la variable ni el operador/comando a usar — eso lo aporta la clase. Ejemplo correcto: "Crea una variable que registre el saldo del usuario". Ejemplo incorrecto: "Crea `saldo = int(input(...))`".
Situación: [contexto narrativo]
Pasos y resultado: cada paso (o grupo de pasos que va junto) se presenta con su propio resultado esperado parcial, no solo un output final — se renderiza como tabla de 2 columnas (qué debe hacer el programa | resultado esperado). Agrupa pasos que no producen output propio con el paso que sí lo hace.

### 4. Práctica Independiente (15-18 min)
Trabajo individual, alineado con la guiada pero NO copia literal. Formato "revisión rápida": ejercicios breves y directos, no problemas extensos multi-parte.
Los enunciados NO incluyen nombres de variables, operadores ni comandos — solo descripción en lenguaje natural de qué calcular. Los ejemplos de input/output usan lenguaje natural ("si alguien ingresa un saldo de \$80.000..."), nunca nombres de variables. Los outputs esperados tienen etiquetas descriptivas. Recuerda escapar el signo peso como `\$` — ver CLAUDE.md restricción 21.
Cantidad de ejercicios: **1 obligatorio + 1 bonus/décimas extra (fijo — no preguntar)**
Contextos: [variados entre los 2 ejercicios]
Criterio de logro: [qué evidencia el aprendizaje]

### 5. Ticket de Salida (5-8 min)
2-3 preguntas de alternativas (4 opciones, rotuladas 1 dedo/2 dedos/3 dedos/4 dedos) sobre lo más importante de la clase. Se responden mostrando los dedos todos al mismo tiempo (conteo + revelación simultánea, ver CLAUDE.md regla 17) — las preguntas y alternativas NO se incluyen en el Colab de clase (solo un aviso de que se proyectan en la tele), van completas solo en el Solucionario.
Cantidad de preguntas: [2 si el ICN tiene 1-2 conceptos centrales relacionados; 3 si cubre 3+ conceptos o si dos conceptos son claramente independientes — no preguntar, decidir con este criterio]
Preguntas: [enunciado + 4 alternativas (1-4 dedos) + cuál es correcta + justificación breve, para cada una]

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
[Descripción detallada. N es un número exacto de minutos (ej. `(6 min)`), no un rango — `generar-ppt-clase` lo usa para el timer del slide.]

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
**Situación:** [contexto narrativo]

[Opcional — solo si la situación incluye una tabla de correspondencia (ej: rango de monto → actividad, temperatura → nivel): escríbela como tabla HTML con `<th>` y `<td>` en lugar de un bloque de código de texto plano. El generador la pasa tal cual al notebook y se renderiza limpiamente en Colab. No uses esto para situaciones narrativas sin tabla.]

**Variables:**
```python
[variables iniciales]
```
**Pasos guiados (tabla):**

- Paso 1: [texto del paso, en lenguaje natural, sin revelar variable/operador]
  Resultado:
  ```
  [output esperado de este paso, o una nota tipo "(todavía no hay output — es solo la variable inicial)" si el paso no produce output propio]
  ```

- Paso 2: [texto del paso]
  Resultado:
  ```
  [output esperado]
  ```

[Agrega tantas filas como pasos agrupados necesites — típicamente 3 a 5. Agrupa en una misma fila los pasos que no producen output propio con el paso que sí lo hace (ej: "construye el bucle" + "dentro del bucle, muestra en pantalla"), para que ninguna fila quede con un resultado vacío. Si el resultado de una fila es una secuencia larga y repetitiva, acórtala con `...` para que la tabla no quede demasiado larga de mostrar. Los backticks dentro de `paso` o `resultado` se convierten automáticamente a código con estilo — no hace falta escribir `<code>` a mano.]

### 4. Práctica Independiente (15-18 min)
**Ejercicio 1 — [contexto] (obligatorio)**
[Enunciado breve, formato revisión rápida]
Resultado esperado: ...

**Ejercicio 2 — [contexto distinto] (Bonus — décimas extra, solo si terminaron el Ejercicio 1)**
[Enunciado breve, formato revisión rápida]
Resultado esperado: ...

### 5. Ticket de Salida (5-8 min)
**Pregunta 1:** [enunciado]
- 1 dedo: [alternativa]
- 2 dedos: [alternativa]
- 3 dedos: [alternativa]
- 4 dedos: [alternativa]
**Respuesta correcta:** [1/2/3/4 dedos]
**Justificación:** [explicación breve, para que Diego la use al revelar la respuesta en vivo]

**Pregunta 2:** [enunciado]
- 1 dedo: [alternativa]
- 2 dedos: [alternativa]
- 3 dedos: [alternativa]
- 4 dedos: [alternativa]
**Respuesta correcta:** [1/2/3/4 dedos]
**Justificación:** [explicación breve]

[Agregar **Pregunta 3** solo si el ICN de esta clase cubre 3+ conceptos, o si dos conceptos son claramente independientes y ambos ameritan verificación separada — ver criterio en CLAUDE.md.]

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
