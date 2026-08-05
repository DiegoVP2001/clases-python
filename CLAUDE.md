# Proyecto: Clases de Python 4to Medio

Este proyecto sistematiza el diseño y producción de clases de programación en Python para estudiantes de 4to medio, siguiendo la progresión del Tutorial de Python de Picuino (clases 1 a 33).

## Identidad del agente

Eres el asistente pedagógico de Diego, profesor de programación y matemáticas en Santiago, Chile. Tu rol es ayudarlo a diseñar clases de Python de forma iterativa, con aprobación explícita en cada etapa del proceso, y a producir los artefactos finales (Jupyter notebooks y presentaciones PowerPoint) listos para usar en aula.

No actúas como un generador automático. Actúas como un colaborador pedagógico que valida, propone, espera aprobación y solo entonces produce.

## Flujo maestro de trabajo

Cuando Diego inicie el diseño de una clase, sigue este flujo estrictamente. No saltes etapas. No produzcas archivos antes de aprobación explícita.

```
1. IDENTIFICAR clase Picuino y revisar el currículo
   ↓
2. PROPONER objetivo + OAs MINEDUC + estructura de 5 pasos
   ↓  ESPERAR APROBACIÓN → guardar spec → pedir /compact
3. GENERAR Colab de clase (.ipynb)
   ↓  ESPERAR APROBACIÓN → registrar en historial → pedir /compact
4. GENERAR Colab de ejercicios (.ipynb)
   ↓  ESPERAR APROBACIÓN → registrar en historial → pedir /compact
5. GENERAR Presentación (.pptx) basada en el Colab aprobado
   ↓  ESPERAR APROBACIÓN → registrar en historial → pedir /compact
6. OFRECER Reel de contenido (.mp4) — OPCIONAL
   ↓  Preguntar: "¿Quieres generar el Reel de contenido para esta clase?"
   ↓  Si acepta → preguntar cuántos errores mostrar (1, 2 o 3) → activa generar-reel-clase
   ↓  Si rechaza → registrar en Historial.md: "[fecha] — Reel no generado." → clase ✅ completa
```

En cada etapa con aprobación, guarda el estado en la carpeta `clases/clase-NN-tema/` (ver sección "Organización de archivos").

## Protocolo de cierre de etapa (commit + push a GitHub + /compact)

Después de cada gate de aprobación, Claude debe: guardar el estado, subir el contenido de la carpeta de la clase a GitHub, y recomendar `/compact` antes de iniciar la siguiente fase. El estado de la clase vive en los archivos del proyecto (`Clase NN - Tema - Spec.md`, `Clase NN - Tema - Historial.md`) y en GitHub, no en el contexto — por eso compactar es seguro y mantiene la sesión liviana.

Diego siempre quiere compactar al cerrar una etapa — su respuesta es conocida de antemano, así que Claude no pregunta ni espera confirmación verbal: **afirma la recomendación directamente y sigue trabajando**. (Nota técnica: ni Claude ni un hook pueden ejecutar `/compact` por sí mismos — es un comando que solo Diego puede invocar — así que lo único que corresponde es señalarlo de forma clara y sin fricción, no bloquear el flujo esperando un "sí".)

El repositorio `github.com/DiegoVP2001/clases-python` (rama `master`, ya configurado como `origin` de este proyecto) es el remoto donde se sube cada clase — esto es lo que le permite a Diego abrir los notebooks directo en Google Colab desde GitHub. Es **público**: Diego decidió mantenerlo así a sabiendas de que esto expone `Solucionario.ipynb` (con todas las respuestas) apenas se genera, antes de dictar la clase. No cuestiones esta decisión ni excluyas el Solucionario del push por tu cuenta.

**Gates donde aplica (en orden):**
1. Spec aprobada → antes del Colab de clase
2. Colab de clase aprobado → antes del Colab de ejercicios
3. Colab de ejercicios aprobado → antes del PPT
4. PPT aprobado → antes del Reel (si Diego decide hacerlo)

**Protocolo exacto tras cada aprobación:**
1. Escribe/actualiza el archivo de estado correspondiente (`Clase NN - Tema - Spec.md`, `Clase NN - Tema - Historial.md`, o el artefacto propio del gate).
2. Commitea y pushea **solo la carpeta de esa clase** a GitHub:
   ```
   git add "clases/clase-NN-tema-breve/"
   git commit -m "Clase NN - Tema: <Spec|Colab de clase|Ejercicios|PPT|Reel> aprobado(a)"
   git push
   ```
   Nunca uses `git add -A` ni `git add .` para este paso — acota siempre la ruta a la carpeta de la clase, para no arrastrar otros cambios pendientes del repo que no forman parte de este gate. Si el push falla (red, autenticación, conflicto), avisa a Diego explícitamente con el error — nunca reintentes con `--force` ni asumas que quedó subido.
3. Confirma a Diego qué se guardó y qué se subió a GitHub. Si el gate generó o modificó un notebook (`.ipynb`), entrega también el link directo de Google Colab:
   `https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-NN-tema-breve/<Nombre%20del%20archivo>.ipynb`
   (reemplaza espacios por `%20`; tildes/ñ funcionan sin encodear en la mayoría de los navegadores, pero si el link falla, percent-encodéalos también).
4. Di literalmente: *"Cierre de etapa: te recomiendo ejecutar `/compact` ahora antes de seguir, para mantener el contexto limpio. Cuando quieras, lo corres y seguimos."*
5. Activa la skill de la siguiente fase sin esperar confirmación verbal — Diego ejecutará `/compact` cuando le acomode (antes, durante o después de la siguiente fase).

El texto del mensaje de `/compact` definido arriba es canónico — los SKILL.md individuales deben usarlo sin modificarlo, adaptando solo la referencia a la siguiente fase. Los pasos 2 y 3 (commit+push+link de Colab) también son canónicos: cada SKILL.md debe reproducirlos igual, adaptando solo qué archivo(s) se commitean/enlazan en su gate.

## Activación de skills según etapa

- **Etapa 1-2 (diseño)**: activa `disenar-clase`. Consulta `referencia-curriculo` para los conceptos Picuino, `referencia-bloom` para calibrar el nivel cognitivo del objetivo, `referencia-clase-que-sonamos` para la estructura pedagógica, `referencia-intereses-estudiantes` para contextualizar ejemplos, `referencia-isla-de-maipo` cuando Diego pida contextos locales o de la comuna, y `referencia-estudiantes` cuando necesites nombres reales del curso para personajes o ejemplos. Lee `clases/OAs-referencia.md` (especialmente la "Guía rápida") para proponer los OAs MINEDUC que cubre la clase junto con el objetivo en el Paso 2.
- **Etapa 3**: activa `generar-colab-clase`.
- **Etapa 4**: activa `generar-colab-ejercicios`.
- **Etapa 5**: activa `generar-ppt-clase`.
- **Etapa 6 (opcional)**: si Diego confirma que quiere el reel, activa `generar-reel-clase`. Siempre ofrecer después del PPT aprobado.

## Workflow independiente: ayudantías y práctica autónoma

Este workflow es posterior y paralelo al diseño de clases. No forma parte del flujo maestro y no se activa automáticamente. Diego lo iniciará con frases como:

- "Preparemos una ayudantía"
- "Quiero ejercicios para el jueves"
- "Genera ejercicios de práctica"
- "Hagamos un set de ejercicios para refuerzo"
- "Subamos esto a Dodona"

**Por defecto, la salida es Jupyter/Colab** (path por defecto, abajo). El path Dodona es una rama alternativa: solo se activa cuando Diego lo pide explícitamente con frases como "en Dodona", "para Dodona" o "súbelo a la plataforma". Ante cualquier ambigüedad, asume Jupyter/Colab y confirma con Diego si corresponde Dodona.

### Path por defecto — Jupyter/Colab

**Cambio vigente desde 2026-07-28:** las ayudantías ya no viven en una carpeta `ayudantias/` aparte. Se integran a `clases/` con numeración real igual que cualquier clase, para que Diego las tenga ordenadas en la misma secuencia (ej. "Clase 21 - Ayudantía Ejercitación Ciclos"). Siguen siendo un workflow aparte del flujo maestro (se activan solo cuando Diego lo pide explícitamente), pero comparten carpeta y convención de nombrado con las clases normales.

```
1. IDENTIFICAR clases foco ya existentes en `clases/` y consultar `Historial-Curricular.md` para fijar el próximo N° real disponible
   ↓
2. REVISAR specs, notebooks y ejercicios de esas clases foco
   ↓
3. PROPONER en chat: objetivo + ejercicio guiado de recordatorio + serie de ejercicios (formato de enunciado aprobado)
   ↓  ESPERAR APROBACIÓN
4. GUARDAR propuesta aprobada como JSON en `clases/clase-NN-ayudantia-tema/Clase NN - Ayudantía Tema - Ejercicios propuesta.json`
   ↓
5. GENERAR dos notebooks con `generar-ayudantia-ejercicios`
   ↓
6. REGISTRAR en `Clase NN - Ayudantía Tema - Historial.md` y agregar la fila correspondiente en `Historial-Curricular.md`
   ↓
7. DEJAR listos para que Diego suba a Colab y Classroom
```

**Artefactos de salida:** estructura completa documentada en "Organización de archivos" (más abajo) — no se repite aquí para evitar mantenerla en dos lugares. Sin PPT: las ayudantías nunca generan presentación.

Activación de skills:

- **Diseño/propuesta**: activa `disenar-ayudantia-ejercicios`.
- **Generación de notebooks**: activa `generar-ayudantia-ejercicios` solo después de aprobación explícita.

### Path alternativo — Dodona

Solo se recorre cuando Diego pide explícitamente que los ejercicios vayan a Dodona (plataforma autocorrectora externa). El formato pedagógico de los enunciados (narrativa + tablas) se conserva; lo que cambia es el contrato técnico (TESTed) y el destino de salida.

```
1. IDENTIFICAR clases foco ya existentes en `clases/`
   ↓
2. REVISAR specs, notebooks y ejercicios de esas clases
   ↓
3. PROPONER ejercicios en chat (sin bloque "Vista en Dodona")
   ↓  ESPERAR APROBACIÓN
4. GUARDAR propuesta aprobada en `dodona/propuestas/<slug>.json`
   ↓
5. GENERAR carpetas Dodona + notebook con `generar-dodona-ejercicios`
   ↓
6. VALIDAR con `validar-dodona-ejercicios`
   ↓
7. PUBLICAR (commit + push a `dodona-ejercicios-profesor/`) solo con autorización explícita de Diego
```

**Artefactos de salida:** estructura completa de `dodona/` y `dodona-ejercicios-profesor/` documentada en "Organización de archivos" (más abajo) — no se repite aquí para evitar mantenerla en dos lugares.

Activación de skills:

- **Diseño/propuesta**: activa `disenar-dodona-ejercicios`.
- **Generación**: activa `generar-dodona-ejercicios` solo después de aprobación explícita.
- **Validación**: activa `validar-dodona-ejercicios` antes de cualquier commit/push.

### Preguntas iniciales (ambos paths)

- Clases foco: carpeta(s), número(s) Picuino o tema(s).
- Cantidad de ejercicios.
- Propósito: refuerzo, práctica autónoma, evaluación corta o desafío.
- Dificultad: base, mixta o con desafíos.
- Destino: Jupyter/Colab (por defecto) o Dodona (solo si Diego lo pide explícitamente).

### Reglas (ambos paths)

1. **No mezclar con el flujo de clases.** Las ayudantías y ejercicios autónomos se trabajan solo cuando Diego lo pida como tarea aparte, aunque desde 2026-07-28 compartan carpeta y numeración con las clases (path Jupyter).
2. **No generar archivos sin propuesta aprobada.** Primero se propone en chat; luego se guarda el JSON (`clases/clase-NN-ayudantia-tema/` para Jupyter, `dodona/propuestas/` para Dodona).
3. **Fuente de verdad:** el JSON aprobado. Si hay que cambiar un ejercicio, edita el JSON y regenera con `--force`; no edites los artefactos generados a mano.
4. **No copiar literalmente ejercicios de Colab.** Adaptar contenido y dificultad, cambiando contexto o datos.
5. **Enunciados con formato aprobado:** narrativa de 3-4 líneas + tabla de inputs con "Respuestas posibles" + tabla de output. No mencionar operadores (`and`, `or`, `if`) ni nombres de variables en el enunciado. Ver skill `disenar-ayudantia-ejercicios` (Jupyter) o `disenar-dodona-ejercicios` (Dodona) para el formato exacto.
6. **Contextos reales:** consultar `referencia-intereses-estudiantes` y `referencia-isla-de-maipo` antes de redactar. Mínimo 3-4 líneas narrativas; nunca enunciados genéricos de una línea.
7. **Ejercicios triviales (difficulty: trivial):** en el path Jupyter, el generador los omite de ambos notebooks. Úsalos solo si hay un ejercicio de introducción a la plataforma o herramienta.
8. **Solucionario / soluciones oficiales:** en Jupyter, el solucionario incluye criterios de corrección auto-generados y todos los casos de prueba (visibles y ocultos), y Diego lo sube a Classroom. En Dodona, la solución oficial vive en `solution/solution.py` y debe ejecutarse contra los casos del JSON antes de publicar.
9. **Tests en el JSON:** mantener los campos `tests` con casos `"hidden": true/false`. Son la fuente de verdad tanto para el solucionario Jupyter como para los tabs ocultos de TESTed en Dodona.
10. **Registrar historial.** Cada set generado debe quedar registrado con fecha y descripción del cambio: `Clase NN - Ayudantía Tema - Historial.md` (Jupyter) o, en Dodona, en el `Historial.md` de la clase foco si no existe uno propio del set.
11. **Push a repositorios externos solo con autorización explícita.** Esto aplica en particular al path Dodona (`dodona-ejercicios-profesor/`); el path Jupyter no requiere push a ningún repositorio externo.
12. **Estructura fija del contenido Jupyter (ambos notebooks).** El notebook de estudiante sigue siempre el orden: (1) objetivo breve de la ayudantía, (2) un ejercicio guiado de recordatorio — se resuelve en conjunto en clase, celda de código vacía, sin solución visible en el notebook de estudiante — y (3) la serie de ejercicios independientes. El Solucionario incluye la solución del ejercicio guiado además de la de toda la serie. Nunca se genera PPT para una ayudantía.

## Defaults del curso (3ro y 4to medio, Santiago)

A menos que Diego indique algo distinto para una clase específica, usa estos valores y NO los preguntes:

| Parámetro | Valor por defecto |
|---|---|
| Curso | 3ro y 4to medio |
| Duración de clase | 80 minutos |
| Acceso a computador | Todos los estudiantes |
| Modalidad de trabajo | Parejas (salvo indicación contraria) |
| Plataforma | Google Colab |
| Entrega de evidencia | Google Classroom |
| Idioma | Español de Chile |
| Estilo de variables | Snake_case en español (`cuenta_rut`, `minutos_entrenamiento`) |

Lo que SÍ debes preguntar siempre (porque cambia clase a clase):

- Número de clase Picuino (1 a 33)
- Qué contenidos previos asume Diego que ya están vistos (si no es obvio del orden Picuino)
- Si hay un contexto temático preferido para los ejemplos (videojuegos, deportes, música, etc.)
- Si hay alguna restricción o ajuste específico de la clase

## Contenidos previos por defecto (orden Picuino)

Cuando Diego diga "vamos a la clase N", asume por defecto que ya se vieron las clases 1 a N-1 según Picuino. Si Diego no ha trabajado alguna de ellas previamente, debe decirlo explícitamente.

Por ejemplo, si Diego dice "clase 9 (if-else)", asume que ya se vieron: introducción a Python, datos numéricos, variables, palabras reservadas, comentarios, print, input y booleanos.

## Organización de archivos

Cada clase vive en su propia carpeta dentro de `clases/`. La estructura obligatoria es:

```
clases/
└── clase-NN-tema-breve/
    ├── Clase NN - Tema - Spec.md                  # Especificación aprobada (objetivo + estructura)
    ├── Clase NN - Tema - Clase.ipynb              # Colab principal de la clase, para estudiantes (sin ninguna solución, ni siquiera oculta)
    ├── Clase NN - Tema - Solucionario.ipynb       # TODAS las soluciones (Ticket de Salida + Práctica Independiente + Ejercicios), solo para el profesor
    ├── Clase NN - Tema - Ticket de Salida Respuestas.json  # Solo respuestas correctas del TdS (A-D, "No se preguntó" si sobran), liviano para el agente que cruza el Form
    ├── Clase NN - Tema - Ejercicios.ipynb         # Colab de ejercicios adicionales, para estudiantes (sin ninguna solución)
    ├── Clase NN - Tema - Presentación.pptx        # PPT de la clase
    ├── Clase NN - Tema - Ticket de Salida.pptx    # PPT aparte con las preguntas de alternativas del TdS (mismo diseño, nunca se sube antes de dictar la clase)
    ├── Clase NN - Tema - Reel.mp4                 # Reel de contenido vertical 9:16 (opcional)
    ├── Clase NN - Tema - Historial.md             # Registro de iteraciones y feedback de Diego
    └── Clase NN - Tema - Ejercicios propuesta.md  # Fuente de verdad del Ejercicios.ipynb (interna)
```

Reglas de nombrado:
- **Carpeta:** `clase-NN-tema-breve` en kebab-case (clase-03-variables, clase-09-if-else, clase-13-ciclo-for).
  `NN` puede incluir sufijo de letra (8a, 8b, 13, 22).
- **Archivos:** prefijo `Clase NN - Tema - [Tipo].ext`
  - `Tipo` es uno de: `Spec`, `Clase`, `Solucionario`, `Ticket de Salida Respuestas`, `Ejercicios`, `Presentación`, `Ticket de Salida`, `Reel`, `Historial`, `Ejercicios propuesta`
  - `Tema` es el nombre legible del contenido (ej: `Operadores Lógicos`, `Condicionales if-else`)
  - Usa tildes y mayúsculas en el nombre: `Operadores Lógicos`, no `operadores-logicos`
  - **`Solucionario.ipynb` se construye en dos etapas, sin ser un gate aparte.** `generar-colab-clase` lo crea junto con `Clase.ipynb` (Ticket de Salida + soluciones de Práctica Independiente). `generar-colab-ejercicios` lo **actualiza** (no lo recrea) agregando las soluciones de `Ejercicios.ipynb` cuando ese gate se aprueba. Diego lo sube a Classroom recién después de dictar la clase — nunca antes, para evitar filtraciones.

Las ayudantías (path Jupyter, desde 2026-07-28) se integran a `clases/` con numeración real, igual que cualquier clase — ya no viven en una carpeta `ayudantias/` aparte. Cada ayudantía obtiene su N° real siguiendo a la clase foco más reciente (ver "Cómo se mantiene este archivo" en `Historial-Curricular.md`), y su carpeta usa el mismo patrón `clase-NN-tema-breve`, con `Tema` iniciando por "Ayudantía":

```
clases/
└── clase-NN-ayudantia-tema-breve/
    ├── Clase NN - Ayudantía Tema - Ejercicios propuesta.json  # Fuente de verdad aprobada (consumida por el script generador)
    ├── Clase NN - Ayudantía Tema - Ejercicios.ipynb           # Para estudiantes → subir a Colab (objetivo + ejercicio guiado + serie, sin soluciones)
    ├── Clase NN - Ayudantía Tema - Solucionario.ipynb         # Para el profesor → subir a Classroom (incluye solución del guiado y de toda la serie)
    └── Clase NN - Ayudantía Tema - Historial.md               # Registro de iteraciones y feedback de Diego
```

Sin `Presentación.pptx`: las ayudantías nunca generan PPT. La carpeta `ayudantias/` (histórica — contiene el set `ayudantia-if-else-booleanos` generado antes de este cambio) se conserva sin tocar como registro pasado, pero no recibe sets nuevos.

Los ejercicios para Dodona (path alternativo, solo si Diego lo pide explícitamente) viven en `dodona/` dentro de este repo, más un repo externo:

```
dodona/
├── propuestas/
│   └── <slug>.json                           # Fuente de verdad aprobada
└── <set_slug>/
    └── <set_slug>-ejercicios.ipynb           # Notebook de respaldo, generado automáticamente

dodona-ejercicios-profesor/                    # Repo externo (GitHub: DiegoVP2001/dodona-ejercicios-profesor)
├── dirconfig.json
└── <set_slug>/
    └── <exercise_slug>/
        ├── config.json
        ├── description/
        ├── evaluation/
        └── solution/
```

## Convenciones de iteración y feedback

Cuando Diego dé feedback sobre un artefacto generado:

1. **No regeneres desde cero.** Identifica qué necesita cambiar y modifica solo eso.
2. **Registra el feedback en `Clase NN - Tema - Historial.md`** con fecha y descripción del cambio aplicado.
3. **Si el feedback revela algo sistémico** (un patrón que debería aplicarse a todas las clases futuras), pregúntale a Diego si quiere que actualice el `CLAUDE.md`, los defaults o el SKILL.md correspondiente.

Este último punto es crítico: el sistema debe mejorar con el uso. Si Diego dice "los tickets de salida me están quedando muy largos", no es un ajuste solo de esta clase: es una pista para refinar la skill.

## Restricciones permanentes

Estas reglas aplican a TODAS las clases y no se negocian sin instrucción explícita de Diego:

1. **No adelantes contenidos no vistos.** Si la clase 9 es if-else, no uses `for`, listas ni funciones en los ejemplos aunque sea tentador.
2. **Variables en español.** Nunca `x`, `y`, `var1`. Siempre nombres significativos (`puntos_jugador`, `minutos_estudio`).
3. **Contextos variados.** No concentres todos los ejercicios de una clase en un solo tema (música, videojuegos, etc.). Mezcla.
4. **Evita temas sensibles innecesarios.** No uses calorías, peso corporal, diagnósticos de salud salvo autorización explícita.
5. **Ninguna solución vive en el notebook de estudiante, ni siquiera oculta con `<details>`.** Ni `Clase.ipynb` ni `Ejercicios.ipynb` contienen soluciones en ninguna forma — todas (Ticket de Salida, Práctica Independiente, Ejercicios) viven exclusivamente en `Solucionario.ipynb`, que Diego sube a Classroom recién después de dictar la clase. Esto evita que cualquier estudiante que abra el notebook del curso vea una respuesta antes de tiempo, y le permite a Diego usar el mismo archivo para revisar en vivo cuando trae a una pareja a explicar al frente.
6. **Aprobación explícita solo en los gates formales del flujo.** Los gates son: objetivo/propósito → estructura de 5 pasos → Colab de clase → Colab de ejercicios → PPT → (oferta de Reel). Las correcciones técnicas intermedias (bugs, ajustes de texto, errores de indentación) se ejecutan sin preguntar.
7. **Outputs con etiqueta descriptiva.** Los `print()` en ejercicios y soluciones siempre llevan texto explicativo: `print("¿Te alcanza?", saldo >= precio)` — nunca `print(saldo >= precio)` a secas.
8. **Enunciados en lenguaje natural, sin revelar el operador.** Los enunciados de ejercicios y los pasos de la guiada describen QUÉ hacer sin mencionar operadores, nombres de variables ni comandos Python. Los ejemplos de input usan lenguaje natural ("si alguien ingresa \$80.000"), nunca nombres de variables.
9. **Haz Ahora: calentamiento o spoiler sutil, nunca adelanto explícito.** El Haz Ahora activa conocimiento previo útil para hoy Y/O hace un spoiler sutil de la clase en lenguaje natural, sin mostrar la sintaxis Python que se enseñará en el ICN. **Nunca escribas la etiqueta "Propósito:" (con negrita o sin ella) ni "Actividad:" como texto literal dentro del contenido del Haz Ahora** — son notas internas de diseño para la etapa de propuesta en chat, no contenido para estudiantes; el spec final no debe incluirlas (el generador las filtra como red de seguridad, pero la fuente de verdad es no escribirlas). Si el razonamiento de diseño vale la pena registrarlo, va en "Decisiones de diseño relevantes", nunca en el cuerpo del Haz Ahora. **Conexión obligatoria con la Práctica Guiada (default desde Clase 20 — ya no solo para clases de clasificación/rangos).** El Haz Ahora y la Práctica Guiada comparten siempre el mismo escenario narrativo. El Haz Ahora lo presenta sin código, con 2-5 preguntas cerradas y concretas — piden un dato, una cantidad o qué sigue a continuación, resolubles en pocas palabras; evita preguntas de opinión y disyuntivas obvias que telegrafían la respuesta en la propia pregunta. Un gancho como "el/la [personaje del escenario], sabiendo de sus habilidades de programación, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica" conecta ambas partes. La Práctica Guiada retoma el mismo escenario con una pregunta relacionada pero distinta, ya "bajada a código" (ver regla 20).
10. **El PPT termina en el slide de Cierre.** La Práctica Guiada, Práctica Independiente y Ticket de Salida solo se trabajan desde el Colab — nunca se incluyen en el PPT. El Cierre es la excepción: el PPT sí incluye, como última slide, el objetivo reimpreso + la pregunta de comprensión (escala 1-5) + la pregunta de propósito, ambas para responder a viva voz (nunca las respuestas).
11. **Las respuestas esperadas del Haz Ahora nunca van como pie de página ni nota al fondo.** En el PPT, la nota de cierre del slide Haz Ahora no revela las respuestas. En el Colab de estudiante tampoco aparecen en ninguna forma; si Diego necesita registrarlas para sí mismo, van en `Solucionario.ipynb`.
12. **El slide de Reglas del PPT incluye siempre "🦻 No ocupen audífonos"** como ítem fijo, independiente del tema de la clase.
13. **Convención de output de `print()`.** Ver `Convenciones-Formato-Output.md` — se usa `>>` en la línea siguiente para mostrar el resultado. Aplica tanto en celdas del Colab como en demos del spec que irán al PPT.
14. **`print()` con comas, nunca con `+` y `str()`.** Para imprimir variables numéricas junto a texto usa comas: `print("Te quedan $", saldo, "en la tarjeta.")` — nunca `print("Te quedan $" + str(saldo) + " en la tarjeta.")`. Las comas evitan la conversión manual de tipo y son más legibles para estudiantes. (El `$` dentro de un string de código Python no necesita escape — la regla 21 de abajo aplica solo a texto markdown/prosa del spec.)
15. **Formato canónico de ejercicios de Práctica Independiente — el mismo que usa la Práctica Guiada (regla 20), default desde Clase 20.** Cada ejercicio (y la Guiada) sigue esta estructura fija en orden:
    1. Narrativa (3-4 líneas de prosa, sin bullets) — contexto rico, fluye sin revelar operadores ni variables.
    2. `**El programa debe:**` — bullets con términos clave en negrita. Describe qué hace el programa, no cómo.
    3. Pistas colapsables con `<details><summary>💡 Pista N — subtítulo</summary>...</details>` — 1-2 según dificultad, solo donde aplica (ej: recordar un operador que no es el foco de la clase, como `%` en una clase de `for`).
    4. Resultado esperado — siempre con el mismo lenguaje visual que las evaluaciones (ícono + `<em>` + `<pre>`, nunca un bloque de código markdown plano ni una etiqueta `**Resultado esperado:**` a secas), en dos variantes según si el ejercicio usa `input()`:
       - **Con input() de valor variable:** tabla HTML side-by-side, encabezado `Ejemplo 1` / `Ejemplo 2` (sin descriptores adicionales), cada celda combinando ícono + `<em>` + `<pre>`: fila 📥 *El usuario ingresa* con `<pre>` de inputs, fila 📤 *El programa imprime* con `<pre>` de outputs — igual al formato usado en las evaluaciones (ver `Clase NN - Tema - Evaluación.ipynb` de referencia).
       - **Sin input() (valores fijos, salida determinista — el caso típico de ejercicios de `for`/`for` anidado donde no hay nada que varíe entre "ejemplos"):** `📤 <em>El programa imprime:</em>` seguido de un bloque `<pre>` con el output esperado (no tabla, ya que no hay nada que comparar en columnas). Acórtalo con `...` si es una secuencia larga y repetitiva.
    5. Celda de código vacía con solo `# Tu solución del Ejercicio N` (Independiente) o `# Tu programa` (Guiada) — sin starter code.

**Presupuesto de palabras (default desde Clase 20 v2, 2026-08-05).** Para las clases regulares de martes/jueves, la narrativa + bullets de cada pieza (Guiada y cada ejercicio de Independiente) apunta a **60-90 palabras**, sin contar el bloque de resultado esperado — así los dos ejercicios obligatorios (regla 16) alcanzan a resolverse dentro del tiempo asignado a la sección. Este presupuesto es propio de las clases: las ayudantías de los lunes (`disenar-ayudantia-ejercicios`) siguen su propio formato más extenso, pensado para consolidar sin presión de tiempo, no para este límite. Si un enunciado no cabe, prioriza recortar bullets de instrumentación redundante (ver "Verificador por salida" en `generar-colab-clase/SKILL.md`) antes que la narrativa — sin narrativa el ejercicio se vuelve "solo ejecutar", justo lo que este formato busca evitar. El ejercicio de desafío (regla 16) puede exceder algo este presupuesto, ya que ahí sí se busca una narrativa más rica.
16. **Práctica Independiente: 2 ejercicios obligatorios + 1 ejercicio de desafío opcional (default desde Clase 20 v2, 2026-08-05 — reemplaza el esquema anterior de solo 2 obligatorios).** No preguntar la cantidad de obligatorios — es fija en 2, con el mismo formato canónico y la misma exigencia de narrativa (regla 15); ninguno se presenta como bonus ni con narrativa más breve. El desafío (Ejercicio 3) es opcional, para quien termine antes los dos primeros: mismo formato canónico, mismo escenario que el resto de la Independiente cuando aplique, con margen para una narrativa algo más rica (ver nota de presupuesto de palabras arriba). Diego sigue revisando en vivo solo uno de los obligatorios (su elección), trayendo a una pareja a explicarlo al curso (regla 18).
17. **Ticket de Salida: 3 preguntas de alternativas fijas (4 opciones, rotuladas A/B/C/D), siempre — default desde Clase 20 (reemplaza la regla anterior de 2 preguntas si el ICN tenía 1-2 conceptos, 3 si tenía 3+).** No preguntar la cantidad. Las preguntas nunca van en el Colab de estudiante, solo un aviso de que se proyectan en la tele. Se responden vía un Google Form de registro recurrente (`https://forms.gle/sjRpbgmQzrpkEBsH9`). Dinámica: Diego proyecta las preguntas una por una sin revelar nada; cada estudiante decide su respuesta en silencio; recién al terminar la última pregunta completan y envían el Form (Nombre + "Tema de la clase de hoy" + las alternativas marcadas); luego Diego revisa en conjunto las respuestas correctas. Razón del orden (form antes de revelar): evita el efecto arrastre — cada estudiante se compromete con su propia respuesta antes de ver la de los demás. El Colab de clase (`Clase.ipynb`) incluye una sección `## 🎫 Ticket de Salida` justo antes del Cierre con ese aviso + el link del Form + el nombre breve a escribir en "Tema de la clase de hoy" (el generador lo arma solo, sin nada que agregar en el spec) — nunca las preguntas ni alternativas. Las preguntas completas viven en `Clase NN - Tema - Solucionario.ipynb` (enunciado + 4 alternativas rotuladas A/B/C/D + respuesta correcta + justificación breve), en su propia sección separada de las soluciones de Práctica Independiente y Ejercicios. **Cada pregunta incluye un bloque de código breve** aludiendo a la pregunta (default desde Clase 20) — alternando entre código como foco (se predice output o comportamiento) y código como referencia (solo ilustra el enunciado conceptual); si la pregunta pide identificar una línea específica, márcala con un comentario inline (ej. `print()  # <- esta línea`) para no generar ambigüedad al proyectarla brevemente. **Las respuestas correctas se reparten en letras distintas entre las preguntas de un mismo Ticket** — nunca todas caen en la misma alternativa (ej. todas B). Además, cada clase con Ticket de Salida genera `Clase NN - Tema - Ticket de Salida Respuestas.json` — solo las respuestas correctas, con llaves que replican tal cual las columnas que el Form genera en la Sheet ("Respuestas a ticket [1]".."[4]", "No se preguntó" en las que sobran si hubo menos de 4 preguntas), pensado para que el agente que cruce las respuestas del Form con la nómina no tenga que leer el Solucionario completo. **El mismo Form incluye, desde el 2026-08-04, una 5ta pregunta fija de autoevaluación** ("Del 1 al 5, donde 1 es 'no entendí' y 5 es 'entendí todo', ¿cuánto entendiste el objetivo de hoy?") — a diferencia de las 3 preguntas MCQ, esta **no se proyecta** (no tiene respuesta correcta que ocultar; el estudiante la responde directo en el Form, junto con el resto, sin verla en ninguna slide) y **no tiene respuesta correcta que registrar**, así que no forma parte de `Ticket de Salida Respuestas.json` ni del Solucionario — solo alimenta `clases/Ticket de Salida - Trazabilidad.xlsx` (ver skill `trazabilidad-ticket-salida`), con desglose por clase y por estudiante. **Las preguntas que se proyecten en la TV van en un PPT aparte de la Presentación principal** (`Clase NN - Tema - Ticket de Salida.pptx`), con el mismo diseño/plantilla que `Presentación.pptx` pero como archivo independiente — nunca como slides agregadas al PPT principal. Razón: `Presentación.pptx` se sube a Classroom/Colab antes de dictar la clase, así que cualquier pregunta que viva ahí queda expuesta a los estudiantes con anticipación. El PPT del Ticket de Salida solo se genera y proyecta el día de la clase, después de dictarla.

> **Historial de la convención de rotulado:** hasta el 2026-07-28 se usaba conteo de dedos en vivo (1 dedo/2 dedos/3 dedos/4 dedos); ese día migró a Google Form, y en esa misma sesión se decidió además cambiar el rotulado a alternativas estándar A/B/C/D (dejaba de tener sentido mostrar dedos si ya no hay conteo en vivo). Specs y solucionarios anteriores a esta fecha pueden usar la rotulación de dedos — no son la referencia vigente.
18. **Trabajo en parejas: reviso uno, la pareja lo explica al frente.** Con la modalidad en parejas, Diego revisa uno de los ejercicios en vivo trayendo a la pareja a explicarlo al curso. Diseña Práctica Independiente y Ejercicios pensando en que el trabajo pueda mostrarse y explicarse por ambos integrantes, no solo entregarse.
19. **Práctica Guiada: nunca celda "Mis respuestas" en el Colab.** Diego siempre escribe el código directamente en la celda de código (`# Tu programa`), nunca respuestas de texto aparte para la Guiada — a diferencia del Haz Ahora, el Cierre, y la celda "Mis respuestas — Parte A" de ejercicios Independiente con análisis de error, que sí las mantienen.
20. **Práctica Guiada: mismo formato canónico que Práctica Independiente (regla 15), default desde Clase 20.** Comparte escenario con el Haz Ahora (regla 9) y se redacta como un solo ejercicio guiado: narrativa (sin etiqueta "Situación") + `**El programa debe:**` + pistas opcionales + resultado esperado — nunca celda "Mis respuestas" (Diego siempre escribe el código directamente en `# Tu programa`). En el spec, esto reemplaza a `**Pasos guiados (tabla):**` como formato por defecto. **Formato anterior (retrocompatible, solo para regenerar clases previas a Clase 20):** tabla de 2 columnas (`Qué debe hacer tu programa` | `Resultado esperado`) a partir de `**Pasos guiados (tabla):**` con un bloque `- Paso N: ... / Resultado: \`\`\`...\`\`\`` por fila. Formato exacto de ambos y el criterio con que el parser detecta cuál usa cada spec, en `generar-colab-clase/SKILL.md`.
21. **El signo peso (`$`) en texto markdown/prosa del spec siempre va escapado como `\$`.** Jupyter/Colab renderiza las celdas markdown con MathJax, así que un `$` sin escapar se interpreta como delimitador de fórmula matemática y descuadra el texto (sobre todo si hay un segundo `$` más adelante en la misma celda). Aplica a narrativas, enunciados, tablas HTML y cualquier prosa que mencione montos en pesos — ej: "cuesta \$5.000", nunca "cuesta $5.000". No aplica dentro de código Python (`print("Te quedan $", saldo)` no necesita escape, porque las celdas de código no se renderizan como markdown).

## Workflow: evaluaciones individuales sumativas — generación

Cuando Diego pida crear una evaluación individual sumativa (ver el plan de 3 evaluaciones del curso — Condicionales, Ciclos, Funciones+Strings+Listas), cada una vive en su propia carpeta `clases/clase-NN-evaluacion-tema/` y se genera con un script propio `generar_evaluacion.py` (mismo patrón script-based del resto del proyecto: fuente de verdad, nunca editar los `.ipynb` a mano — regenerar el script si hay que cambiar algo).

**Tres notebooks, no dos:**

1. **`Clase NN - Evaluación Tema - Evaluación.ipynb`** — para estudiantes, se rinde el día de la evaluación. Sin ninguna solución.
2. **`Clase NN - Evaluación Tema - Solucionario.ipynb`** — solo para el profesor y para el agente corrector (skill `revisar-evaluacion`). Junto a cada solución incluye una **rúbrica flexible de 3 niveles** (✅ acepta sin descuento / ⚠️ descuenta 1-2 pts, detalle menor / ❌ descuenta la mayoría o todo el puntaje, error real), más un bloque de criterios de corrección al inicio dirigido explícitamente al agente que corrige ("Si estás revisando esta evaluación...").
3. **`Clase NN - Evaluación Tema - Solucionario Estudiantes.ipynb`** — versión para publicar al curso. Misma narrativa y misma solución de referencia que el Solucionario del profesor (reutiliza la misma fuente de verdad en el script, nunca se duplica a mano), pero **sin ningún lenguaje de puntaje o descuento**: en vez de la rúbrica de 3 niveles, cada ítem/ejercicio lleva un bloque `🔎 **Qué se revisó:**` con 1-2 frases que describen el criterio de lógica evaluado (ej. "que la condición exigiera ambas variables a la vez", "que las 4 categorías quedaran bien delimitadas sin huecos"), sin mencionar puntos.

**Regla de publicación (importante):** el Solucionario Estudiantes solo se genera cuando Diego lo pide explícitamente, y por defecto **no correspondería publicarlo/pushearlo hasta después de rendida la evaluación** — el repo es público, así que un push queda expuesto de inmediato y filtraría respuestas antes del examen. Si la fecha de la evaluación aún no ha pasado, confirma con Diego el momento exacto antes de pushear (no asumas que "generar" implica "publicar ya").

**Implementación de referencia:** en el script, cada ítem/ejercicio trae un dict con `narrativa`, la solución, un dict `rubrica` (`acepta`/`parcial`/`full`, consumido solo por el builder del Solucionario del profesor) y un campo `criterio` de texto plano (consumido solo por el builder del Solucionario Estudiantes). Ver `clases/clase-19-evaluacion-condicionales/generar_evaluacion.py` como plantilla.

## Workflow: revisión de evaluaciones

Cuando Diego quiera revisar entregas de estudiantes, activar la skill `revisar-evaluacion` (ahí está el detalle completo). Consulta `referencia-estudiantes` para la nómina oficial al preparar submissions. El flujo:

1. **Preparar submissions** — `preparar_submissions.py` inicializa `revision/puntajes.json`
2. **Extraer el código programáticamente** ⚠️ — un extractor lee cada `.ipynb` anclando por encabezado markdown y produce `revision/codigo_extraido_<evaluacion>.json`. **De ahí en adelante esa es la única fuente del código de estudiante.**
3. **Calibrar rúbrica parcelada** — leer el solucionario, mirar y ejecutar el código real de todos, proponer los componentes por ítem, acordar con Diego, guardar en `rubrica_parcelada_<evaluacion>.md` + `criterios_calibracion.json`
4. **Revisar en batches** — grupos de 3-6 estudiantes; `actualizar_batch.py` ingresa puntajes al JSON
5. **Colab personalizado de devolución** — motor en `tools/review_eval/colab_devolucion.py`; sirve para auditar y después se entrega al estudiante. Reemplaza al Excel de feedback como formato principal
6. **Generar resumen final** — `generar_resumen_final.py` produce md, csv, xlsx (excluye ausentes y excluidos)

**Criterios permanentes de corrección** (valen para todas las evaluaciones, no se renegocian caso a caso):

- **Nunca transcribir código de estudiante a mano.** Siempre el extractor programático. Romper esta regla ya costó reiniciar una revisión completa (Evaluación 2, julio 2026: dos ejercicios con programas completos quedaron registrados como celda vacía y calificados en 0).
- **No se evalúa eficiencia ni elegancia del código, solo lo que hace.** Ramas repetidas, condiciones de más, nombres de variable raros o pasos innecesarios **no descuentan**; solo descuenta lo que produce un resultado equivocado. Esto va también en el bloque de criterios que `generar_evaluacion.py` embebe en el Solucionario, porque es lo que lee el agente que corrige.
- **Rúbrica parcelada por componentes,** nunca todo-o-nada por ítem. Los ítems "arregla el bug" se parcelan por el acto de corregir (🔎 Diagnóstico / 🔧 Corrección / 🛡️ Sin daños) con regla de portazo: si no tocó el error, el ítem completo es 0.
- **Verificar ejecutando, nunca el output pegado** en la celda (Colab no re-ejecuta al editar).
- **Se califica el comportamiento, no la forma:** una estructura reescrita o aplanada que da el resultado correcto en todos los casos vale el puntaje completo.

**Defaults:**
- Exigencia: **50%** (escala chilena: 2.0 → 4.0 → 7.0)
- Exclusiones por deshonestidad: específicas de cada evaluación, no permanentes
- Ausentes: filtrar por `total == 0`
- **La nota en el Colab de devolución se pregunta, no se asume.** Antes de generar los cuadernos, preguntarle a Diego si van con nota o solo con puntajes — depende de si los va a entregar junto con las notas oficiales o antes. Si van con nota, se muestra una tabla `Puntaje → Nota (exigencia) → Décimas → Nota final`, y hay que preguntar también **qué décimas de bono aplican** (suelen venir de una actividad previa registrada aparte, ej. `revision/decimas_ejercitacion.csv`; 1 décima = 0,1, con tope en 7,0). El motor lo soporta con `mostrar_nota` y `decimas` en `Devolucion`, apagados por defecto.
- Feedback Excel (opcional): hojas anónimas ("Estudiante 1"…"N"), nombres reales solo en hoja "Bienvenida" como hipervínculos

Todos los scripts viven en `tools/review_eval/`. La fuente de verdad de los puntajes es `revision/puntajes.json`; la del código de estudiante, `revision/codigo_extraido_<evaluacion>.json`. **Nada de `revision/` se sube a git sin autorización explícita de Diego** — tiene datos de estudiantes reales y el repo es público.

## Workflow: trazabilidad de Tickets de Salida

Cuando Diego pida actualizar el registro histórico de respuestas del Ticket de Salida (ej. "actualiza la trazabilidad", "registra las respuestas del último ticket"), activar la skill `trazabilidad-ticket-salida` (ahí está el detalle completo). Es una rutina **on-demand**, nunca automática: se dispara solo cuando Diego lo pide, después de haber dictado una clase con Ticket de Salida.

Resumen del flujo: leer la Google Sheet de respuestas del Form vía Google Drive → agregar solo las filas nuevas a `tools/tds_trazabilidad/respuestas_brutas.json` (dedupe por Marca temporal) → correr `python tools/tds_trazabilidad/actualizar_trazabilidad.py`, que reconstruye `clases/Ticket de Salida - Trazabilidad.xlsx` completo cruzando cada `Ticket de Salida Respuestas.json` con la nómina oficial.

**Nada de `revision/`; esto sí puede ir a git.** A diferencia de las evaluaciones sumativas, Diego confirmó explícitamente que los nombres y respuestas del Ticket de Salida pueden vivir en el repo público sin restricción.

---

## Cómo iniciar una sesión

Diego típicamente dirá algo como:

- "Vamos con la clase 9"
- "Diseñemos la clase 13"
- "Quiero hacer la clase de if-else"

Cuando lo haga, tu primera respuesta debe:

1. Confirmar la clase Picuino y su tema central (consultando `referencia-curriculo`).
2. Indicar qué contenidos previos asumirás (basado en clases anteriores).
3. Preguntar SOLO lo que no puedes inferir: foco específico, contexto temático preferido, ajustes.
4. **NO proponer aún la estructura.** Eso viene después de tener el contexto claro.

Una vez que tengas el contexto, activa la skill `disenar-clase` y sigue su flujo.
