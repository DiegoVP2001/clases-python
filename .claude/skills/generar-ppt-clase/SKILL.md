---
name: generar-ppt-clase
description: Genera la presentación PowerPoint (Clase NN - Tema - Presentación.pptx) de una clase a partir del spec aprobado. El PPT cubre desde la bienvenida hasta los errores típicos, y termina con el slide de Cierre (Objetivo + preguntas de comprensión y propósito para viva voz). La Práctica Guiada, Independiente y Ticket de Salida se trabajan desde el Colab. Usa esta skill después de que el Clase NN - Tema - Clase.ipynb esté aprobado.
---

# Skill: Generar presentación PowerPoint (Clase NN - Tema - Presentación.pptx)

## Propósito

Producir el archivo `.pptx` de una clase listo para usar en aula: fondo oscuro `#1A1A2E`, paleta turquesa + ámbar, Consolas para código. El PPT cubre lo que el profesor proyecta para presentar el contenido nuevo — no incluye las actividades que los estudiantes hacen en Colab.

## Cuándo usar

Actívate cuando Diego diga "Genera el PPT", "Pasemos al PowerPoint" o equivalente.

**Requisitos previos:**
1. `clases/clase-NN-tema/Clase NN - Tema - Spec.md` existe y está aprobado.
2. `Clase NN - Tema - Clase.ipynb` está aprobado. Si no existe o no ha sido aprobado, avisa a Diego y pregunta si quiere generarlo primero con `generar-colab-clase` antes de continuar — el PPT se basa en el spec, pero el Colab aprobado es la señal de que el contenido ya está validado.
3. `python-pptx` instalado: `pip install python-pptx`.

## Previews — regla de uso

**No generes previews (`--preview-icn`, `--preview-hazahora`) salvo que tengas una razón técnica concreta** (ej.: necesitas validar que un bloque nuevo renderiza antes de continuar con el PPT completo). Diego solo quiere el archivo final `Clase NN - Tema - Presentación.pptx`. Los previews son para depuración interna del skill, no para el flujo normal.

## Alcance del PPT (regla permanente)

**El PPT nunca incluye Práctica Guiada, Práctica Independiente ni Ticket de Salida** — esas secciones se trabajan desde el Colab. **El Cierre es la excepción: sí va en el PPT, como última slide**, con el objetivo reimpreso y las dos preguntas de cierre (comprensión y propósito) para responder a viva voz — nunca sus respuestas.

Las preguntas de alternativas del Ticket de Salida, cuando se proyectan en la TV, van en un `.pptx` **aparte** (`Clase NN - Tema - Ticket de Salida.pptx`), con el mismo diseño/plantilla que este PPT pero como archivo independiente — nunca como slides agregadas aquí. Razón: `Presentación.pptx` se sube a Classroom/Colab antes de dictar la clase, así que cualquier pregunta que viva en este archivo queda expuesta a los estudiantes con anticipación. Las alternativas se rotulan **A / B / C / D** (convención vigente desde 2026-07-28; antes se usaba conteo de dedos, mecanismo obsoleto desde que el TdS migró a Google Form). Se responden vía el Google Form de registro (`Clase.ipynb` ya trae el link + el nombre breve a escribir en "Tema de la clase de hoy"): Diego pasa las preguntas una por una sin revelar nada, y solo al terminar la última los estudiantes completan y envían el Form — eso evita el efecto arrastre (ver CLAUDE.md regla 17). Ese archivo se genera con `crear_ppt_ticket.py` (ver sección propia más abajo) — automáticamente, en el gate de `generar-colab-clase`, no en este.

Estructura fija de slides:

```
1. Bienvenida
2. Objetivo + ¿Por qué lo veremos? (antes «Propósito») + Reglas
3. Haz Ahora
4..N  ICN — 1 slide dos_columnas por bloque de conceptos clásicos consecutivos
N+1.  Errores típicos
N+2.  Cierre  ← última slide (Objetivo + Comprensión 1-5 + Propósito)
```

Fuente de datos del slide de Cierre: la misma sección `### Cierre` del spec que ya consume `generar-colab-clase` (Objetivo de la clase + Pregunta 1 — Metacognición + Pregunta 2 — Actitud proyectada). No hay que duplicar contenido en el spec — el parser de `crear_ppt.py` reutiliza el mismo formato estructurado.

## Arquitectura del generador

El generador tiene tres capas:

1. **Parser** (`parsear_spec` en `crear_ppt.py`) — lee el spec y produce una estructura semántica. Los demos (`**Demostración:**`) se parsean en el cuerpo de cada concepto para que queden asociados al concepto que los precede en el spec.

   Tres detalles que conviene tener presentes al escribir un spec:
   - El número de clase acepta **decimales** (`# Clase 19.5 — Tema`), igual que en `generar-colab-clase`.
   - El `## Propósito` se corta en el siguiente encabezado de nivel 2, así que un spec puede tener secciones intermedias (`## OAs MINEDUC`, `## Apertura`) entre el Propósito y `## Estructura de la clase` sin que se cuelen en la portada.
   - **`## ¿Por qué lo veremos?` (desde 2026-10-31; antes `## ¿Para qué sirve?`, regla 24 del CLAUDE.md raíz) reemplaza al Propósito en el slide de Objetivo.** El parser acepta ambos títulos y guarda el texto en `spec["para_que_sirve"]` (y cuál se usó en `spec["por_que_titulo"]`). Si la spec trae `## ¿Por qué lo veremos?`, el recuadro derecho de la plantilla (placeholder `PROPOSITO`) muestra ese texto y se **rotula «¿Por qué lo veremos?»** (`renombrar_rotulo`); no hace falta `## Propósito` en la spec (el objetivo se corta en el siguiente encabezado de nivel 2). Las specs antiguas con `## Propósito` siguen igual: el recuadro conserva el Propósito y su rótulo. Decisión de Diego (2026-10-31): el recuadro cambia de rótulo y contenido, no se agregó un cuarto bloque ni se editó la plantilla binaria. El slide de Cierre no cambió (su columna «Propósito» sigue siendo la pregunta de propósito del Cierre).
   - En el `### Cierre`, el texto del objetivo y de las dos preguntas puede ir **en la misma línea** que su etiqueta en negrita o en la línea siguiente: las dos formas se parsean igual.

2. **Planificador** (`planificar_slides.py`) — recibe los conceptos + demos y decide cuántos slides genera la ICN, qué composición tiene cada uno, y dónde intercalar los demos.

3. **Renderizador** (`crear_ppt.py`) — toma las decisiones del planificador y compone los slides con bloques visuales (cajas de definición, terminal de código, tabla, idea clave, anatomía, analogía).

## ICN: decisiones del planificador

El planificador genera primero los slides individuales, luego el resumen compacto:

| Tipo de concepto | Slide generado |
|---|---|
| Clásico (definición + código ± idea clave) | `icn_flexible`: slide individual con bloques apilados |
| `Tipo: anatomia` o tiene `**Partes:**` | Slide anatomía (expresión + hasta 4 partes) |
| `Tipo: analogia` o tiene `**Analogía:**` | Slide analogía (tabla vida real ↔ Python, hasta 4 filas) |
| `Tipo: antes_despues` o tiene `**Antes:**` + `**Después:**` | Slide antes/después (dos snippets paralelos) |
| `Tipo: frase_clave` | Slide frase clave grande sola |
| `**Comparación: título**` con tabla `<table>` HTML | `icn_flexible`: la tabla se renderiza como bloque tipo tabla (mismo mecanismo que una tabla markdown dentro de una Definición) |
| `**Demostración:**` en el cuerpo del concepto | Slide apilado, insertado inmediatamente después del concepto |
| **Resumen final** (auto, si hay ≥2 conceptos clásicos) | `dos_columnas`: un slide compacto al final del ICN |

**Estructura resultante:**
```
Slide para concepto 1  (icn_flexible)
Slide para concepto 2  (icn_flexible)
...
Slide resumen          (dos_columnas) ← al final, antes de Errores típicos
```

**Nota — formato "Escríbelo tú" del Colab (default desde 2026-09-24, ver `generar-colab-clase/SKILL.md`):** el PPT no se ve afectado. Siempre usa el `- Ejemplo:` completo del spec (nunca el `- Punto de partida:` incompleto), tanto en los slides individuales como en el resumen de dos columnas — el planificador ni siquiera lee esos dos campos nuevos.

## ICN dos columnas (resumen compacto al final)

Slide que se agrega automáticamente **después de todos los individuales** cuando hay ≥2 conceptos clásicos:

- **Columna izquierda** (5.7" ancho, fondo oscuro + borde turquesa):
  bullets con `📘 N. Nombre` + primera oración completa de la definición (sin truncar).
- **Columna derecha** (~6.1" ancho, terminal negro + franja turquesa):
  el bloque de código del primer concepto que tenga `- Ejemplo:` (incluye output `>>` si existe en el spec).
- **Sin "idea clave"** por defecto. Solo se incluye si Diego lo pide explícitamente.
- Título sube a y=0.62" para ceder espacio al contenido.
- Fuente de código autoajustada (tam_max=18, tam_min=13) según largo del bloque.
- Fuente de bullets autoajustada (20pt ≤ 10 líneas, 18pt ≤ 14, 16pt si más).

## ICN flexible: bloques visuales disponibles

Para conceptos clásicos individuales, el slide se compone de bloques apilados verticalmente:

| Bloque | Apariencia | Se genera cuando |
|---|---|---|
| `definicion` | Caja fondo oscuro, borde turquesa | El concepto tiene `- Definición:` |
| `codigo` | Terminal negro, franja turquesa, Consolas autoajustada | El concepto tiene `- Ejemplo:` con ```python``` |
| `idea_clave` | Caja fondo oscuro, borde ámbar | El concepto tiene `- Idea clave:` |

### Cómo se reparte el alto (solver de layout)

Las alturas no son solo proporcionales a la densidad que calculó el planificador: `_resolver_layout_icn` estima cuántas líneas ocupa de verdad cada bloque y busca la combinación de tamaños de fuente con la que todos caben en el área disponible (1.58"–7.32").

- Arranca con los tamaños de siempre (definición 20-22pt, idea clave 22pt, código hasta 20pt): **las slides que ya cabían salen idénticas.**
- Si no cabe, aprieta primero la prosa (22 → 20 → 18 → 16) y **solo después** baja un escalón el código (20 → 18 → 16 → 14). El código es lo que hay que leer desde el fondo de la sala, así que se achica último.
- El aire que sobra se lo lleva el bloque de código.
- Si ni con la fuente más chica cabe, avisa por consola (`[layout] ... no cabe ni con la fuente más chica`): ahí sí hay que acortar el texto en el spec.

Sin esto, un ejemplo de 10-11 líneas se dibujaba **fuera** de su terminal negro y la Idea clave fuera de su recuadro ámbar — el reparto proporcional no miraba el largo real del contenido. Ojo: la advertencia `⚠ Densidad N > 16` del planificador es otra cosa (avisa que la slide va cargada) y puede aparecer aunque el layout resuelva bien.

## Haz Ahora flexible

El slide de Haz Ahora se compone dinámicamente según el tipo de actividad:

**Tipo `situaciones_con_tabla`**: cuando el spec trae una tabla markdown en el Haz Ahora (ej: rangos → actividad). El slide tiene:
- Caja intro (borde ámbar) con el texto narrativo
- **Tabla PPT real** (no texto con pipes) con las filas extraídas de la tabla markdown
- Caja preguntas (borde turquesa) con la línea introductoria ("Responde en tu cuaderno:") + ítems numerados

**Tipo `situaciones`** (más común): el spec tiene ítems numerados sin tabla. El slide tiene:
- Caja intro (borde ámbar) con la instrucción
- Caja grande (borde turquesa) con las situaciones numeradas — 20pt si ≤6 ítems, 18pt si más
- Nota de cierre al fondo (blanco, no gris) — **nunca incluye las respuestas esperadas**

**Tipo `libre`**: sin ítems numerados. Todo el texto va en una sola caja grande con borde ámbar.

**Metadata que se elimina antes de parsear** (no aparece en el PPT): `**Propósito:**`, `**Actividad:**`, `**Respuestas esperadas:**`, líneas de minutos `(N min)`, cualquier línea de blockquote (`> ...` — son notas de conducción para Diego), las líneas `Nota de conducción:` sueltas, y el marcador `[[respuesta]]` que el Colab usa para insertar celdas de respuesta.

### Versión proyectada del Haz Ahora

Cuando el Haz Ahora del Colab no cabe en una slide —típicamente porque trae código ejecutable, varios programas o celdas de respuesta intercaladas— el spec puede declarar una **versión compacta solo para el PPT** en una sección propia al final del archivo:

```markdown
## Proyección — Haz Ahora (PPT)

> Nota interna para Diego: por qué existe esta versión. Los blockquotes no se proyectan.

Texto de la caja intro (la consigna: qué abrir, qué hacer).

Responde en el Colab, debajo de cada programa:

1. Primera cosa que hay que hacer.
2. Segunda cosa.

Línea de cierre que va al pie del slide.
```

Se parsea con las mismas reglas que el Haz Ahora normal (`situaciones` / `situaciones_con_tabla` / `libre`), y si existe **manda por sobre** `### 1. Haz Ahora`. El tag del timer sigue saliendo de los minutos declarados en `### 1. Haz Ahora (N min)`.

**Dónde va:** al final del spec, **después** de `## Decisiones de diseño relevantes`. Ahí `generar-colab-clase` no la lee, así que el Colab aprobado no se toca. Nunca la pongas entre `### Cierre` y `## Decisiones` — el parser del Cierre se la tragaría.

**Cuándo usarla:** solo cuando el Haz Ahora del Colab es demasiado largo para proyectarse. El caso normal (situaciones numeradas y nada más) no necesita esta sección. Lo que se proyecta mientras trabajan es la consigna y la lista de tareas: el detalle ya lo tiene cada estudiante en su pantalla.

## Timer del Haz Ahora

El título del slide de Haz Ahora incluye automáticamente un tag `<<N:00>>` (ej. `⚡ Haz Ahora <<6:00>>`), tomado de los minutos declarados en el encabezado del spec (`### 1. Haz Ahora (N min)`). Diego usa una extensión de PowerPoint que detecta ese texto literal en el título y arranca un timer en pantalla al proyectar — por eso el formato `<<M:SS>>` debe quedar exacto (sin espacios extra, dos puntos, segundos siempre en `00`). Este timer es **solo del Haz Ahora**; ningún otro slide (Guiada, ICN, Cierre) lleva el tag — la Guiada no se trabaja desde el PPT. Si el spec no declara minutos en el encabezado, el slide se genera igual, sin tag.

## Orden de demos en el PPT

Los bloques `**Demostración:**` del spec se insertan **inmediatamente después del concepto al que pertenecen** (el que los precede en el texto del spec), no al final de todos los conceptos. Esto asegura que la analogía, si aparece como último concepto, quede justo antes de los errores típicos.

## Sintaxis del spec (resumen)

### Concepto clásico
```markdown
**Concepto 1: Tipo booleano**
- Definición: En Python existe un tipo `bool` que solo puede ser `True` o `False`.
- Ejemplo:
  ```python
  tiene_stock = True
  print(type(tiene_stock))
  ```
- Idea clave: `True` y `False` siempre con mayúscula.
```

### Anatomía
```markdown
**Concepto 2: Operadores de comparación**
Tipo: anatomia
- Definición: Comparan dos valores y devuelven `True` o `False`.
- **Expresión:** `saldo >= precio`
- **Partes:**
  - `saldo` | operando izquierdo
  - `>=` | el operador — define el tipo de comparación
  - `precio` | operando derecho
  - Resultado | siempre `True` o `False`
- Idea clave: Una comparación siempre devuelve `True` o `False`.
```

### Analogía
```markdown
**Concepto 4: Booleanos en la vida real**
Tipo: analogia
- Definición: Las comparaciones de Python reflejan preguntas cotidianas.
- **Analogía:** Lo que te preguntas tú, Python lo resuelve con `True` o `False`.
  - ¿Te alcanza el saldo? | `saldo >= precio` → `True` o `False`
  - ¿Hay unidades? | `unidades != 0` → `True` o `False`
```

### Demostración apilada
```markdown
**Demostración: Operadores == != >**
Subtítulo: Comparando saldo = 45000 con precio = 60000.
- Fila: == | 45000 == 60000 | False — no son iguales
- Fila: != | 45000 != 60000 | True — sí son distintos
- Fila: >  | 45000 > 60000  | False — el saldo no supera el precio
```

### Comparación (tabla lado a lado)
Mismo nivel jerárquico que `**Concepto N:**` — no lleva número, y se intercala en el PPT según su posición real en el spec (comparte numeración secuencial `📘 N.` con los Concepto). El generador convierte `<code>` a código inline y aplana `<strong>`/`<em>`/`<pre>` a texto plano (preservando saltos de línea reales de `<pre>`).
```markdown
**Comparación: `for` y `range(inicio, fin, salto)` lado a lado**
<table>
<tr><th>🔁 <code>for</code></th><th>🔢 <code>range(inicio, fin, salto)</code></th></tr>
<tr><td>Descripción de la izquierda...</td><td>Descripción de la derecha...</td></tr>
<tr><td><pre>código de ejemplo</pre></td><td><pre>código de ejemplo</pre></td></tr>
</table>
```
El `- Ejemplo:` opcional que puede seguir a la tabla en el spec (para el notebook) **no se usa en el PPT** — la tabla ya contiene el código representativo, y agregar el ejemplo aparte saturaría el slide.

## Cómo se ejecuta

```powershell
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" "clases/clase-NN-tema/Clase NN - Tema - Spec.md" "clases/clase-NN-tema/Clase NN - Tema - Presentación.pptx"
```

**Flags de preview** (solo si hay necesidad técnica concreta — ver sección "Previews"):
```powershell
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" spec.md preview.pptx --preview-icn
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" spec.md preview.pptx --preview-hazahora
```

**Debug de decisiones del planificador:**
```powershell
$env:DEBUG_PPT=1; python crear_ppt.py spec.md salida.pptx
```

## Código inline con backticks

Cualquier texto entre backticks `` `código` `` en el spec se renderiza en el PPT con fuente Consolas y color verdoso `#4ADFCB`, automáticamente, en cualquier bloque de texto (definición, idea clave, tabla de errores, etc.).

## Después de generar

1. Confirma a Diego que `Clase NN - Tema - Presentación.pptx` se generó y dónde está.
2. **Espera el feedback de Diego antes de avanzar al Reel.**
3. Cuando Diego apruebe, registra en `Clase NN - Tema - Historial.md`:

   ```markdown
   ## [fecha] — PPT aprobado
   - Archivo: Clase NN - Tema - Presentación.pptx
   - Generado con la skill generar-ppt-clase
   - [notas de iteraciones si las hubo]
   ```

4. Commitea y pushea **solo la carpeta de esta clase** a GitHub (ver "Protocolo de cierre de etapa" en el `CLAUDE.md` raíz):

   ```
   git add "clases/clase-NN-tema-breve/"
   git commit -m "Clase NN - Tema: PPT aprobado"
   git push
   ```

   Si el push falla, avisa a Diego con el error explícito — no reintentes con `--force`. (El `.pptx` no se abre vía Google Colab, así que este push solo respalda el archivo en GitHub, sin link que entregar.)

5. Di: *"Antes de seguir, ejecuta `/compact` para limpiar el contexto. Avísame cuando estés listo."* Luego pregunta: *"¿Quieres generar el Reel de contenido para esta clase?"* Si acepta, pregunta cuántos errores mostrar (1, 2 o 3) y activa `generar-reel-clase`. Si rechaza, registra en `Historial.md`: "[fecha] — Reel no generado." — la clase queda completa.

## Iteración

- **Cambio de contenido:** editar `Clase NN - Tema - Spec.md` y regenerar.
- **Cambio de marca visual** (colores, tipografías, posiciones): editar `construir_plantilla.py` y correrlo para regenerar `plantilla_marca.pptx`. Luego regenerar los PPT afectados.
- **Cambio de lógica de planificación:** editar `planificar_slides.py`.
- **Cambio de renderizado:** editar `crear_ppt.py`.

## PPT del Ticket de Salida (`crear_ppt_ticket.py`)

Archivo **aparte**, generado con su propio script. Nunca se agrega al `Presentación.pptx`.

**Se genera antes, no en este gate (vigente desde 2026-08-13).** El comando corre automáticamente como parte de `generar-colab-clase`, en el mismo paso donde se generan `Clase.ipynb` + `Solucionario.ipynb` + el JSON de respuestas — ver `generar-colab-clase/SKILL.md` § "Cómo se ejecuta". Aquí abajo queda documentado el script y su comportamiento porque esta skill (`generar-ppt-clase`) sigue siendo dueña del código (`crear_ppt_ticket.py` vive en esta carpeta) y porque conviene **volver a correrlo manualmente si Diego pide cambios al Ticket después** de que el Colab de clase ya fue aprobado (ej. reescribir una pregunta, ajustar una alternativa):

```powershell
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt_ticket.py" "clases/clase-NN-tema/Clase NN - Tema - Spec.md" "clases/clase-NN-tema/Clase NN - Tema - Ticket de Salida.pptx"
```

Lee la sección `### N. Ticket de Salida` del spec y arma:

```
1.        Portada + reglas de la dinámica (una por una / en silencio / anota la letra)
2..N+1    Una slide por pregunta: enunciado + bloque de código + 4 alternativas A/B/C/D
N+2       Pantalla del Google Form (link grande + qué escribir en cada campo)
N+3..     Revisión: por pregunta, la alternativa correcta destacada + la justificación
```

Las slides de revisión van **después** de la del Form a propósito: ese es el orden de la dinámica (nadie ve una respuesta antes de comprometerse con la suya). Con `--sin-revision` se generan solo hasta la slide del Form.

**Cómo se reparte el alto en las slides de pregunta.** Un solver prueba combinaciones de tamaño (código 20→14pt, alternativas 24→16pt) y elige la de menor costo, donde **cada punto de fuente sacrificado del código pesa el doble que uno de las alternativas** (`_PESO_COD = 2.0` vs `_PESO_ALT = 1.0`). Cuando hay que apretar, se aprietan primero las alternativas: son frases cortas y aguantan un par de puntos menos sin volverse ilegibles, mientras que el código es el objeto de la pregunta y hay que leerlo desde el fondo de la sala. Misma prioridad que en el ICN de la clase. Además prueba dos layouts de alternativas —grilla 2×2 y columna única— y gana el de menor costo: la grilla rinde más casi siempre, y la columna única solo cuando alguna alternativa es tan larga (~100+ caracteres) que en media plana ocuparía tres líneas.

> **Calibración (2026-08-02, Clase 19.5).** La primera versión tenía la prioridad al revés y dejaba el código en 16pt con alternativas en 24pt. Diego achicó a mano las alternativas a ~20pt para darle aire al terminal y pidió que quedara así de ahí en adelante. Con los pesos actuales, esa misma clase resuelve en código 20pt (el techo de la escala) y alternativas 18-22pt. Si en el futuro las alternativas quedan demasiado chicas, subir `_PESO_ALT` — no tocar las escalas.

Si ni con el piso de la escala cabe, el script imprime un aviso por consola con el número de pregunta: el texto del spec es demasiado largo, hay que acortarlo ahí.

**Cuándo se genera y qué NO hacer con él.** Se genera en el gate del Colab de clase (`generar-colab-clase`), pero está pensado para proyectarse recién el día de la clase. **No se commitea ni pushea hasta después de dictarla** — el repo es público y ese archivo contiene las preguntas y las respuestas correctas.

## Archivos en esta carpeta

| Archivo | Rol |
|---|---|
| `SKILL.md` | Este archivo |
| `crear_ppt.py` | Orquestador: parser + renderizador + constructores de slide |
| `crear_ppt_ticket.py` | Generador del PPT aparte del Ticket de Salida (preguntas A/B/C/D + Form + revisión) |
| `planificar_slides.py` | Capa de planificación pedagógica (cuántos slides, qué composición) |
| `construir_plantilla.py` | Define paleta, tipografías y helpers visuales; regenera `plantilla_marca.pptx` |
| `plantilla_marca.pptx` | Plantilla con slides modelo (bienvenida, objetivo, tabla, anatomía, analogía, apilado, etc.) |

## Limitaciones conocidas

- **Haz Ahora con código Python y preguntas asociadas:** el planificador no tiene un tipo dedicado para esto y no conviene que lo tenga — tres programas completos no caben en una slide y tampoco hace falta proyectarlos, porque cada estudiante los tiene en su Colab. La solución es declarar una sección `## Proyección — Haz Ahora (PPT)` en el spec (ver arriba) con la consigna y la lista de tareas. Sin esa sección, el generador vuelca el Haz Ahora completo del Colab en la slide y el resultado es ilegible (código, marcadores `[[respuesta]]` y todo junto).

## Reglas críticas

1. **El PPT termina en el slide de Cierre.** Guiada/Independiente/Ticket solo en Colab; el Cierre (Objetivo + Comprensión 1-5 + Propósito) es la excepción y va como última slide.
2. **El spec es la fuente de verdad del contenido.** No edites el `.pptx` generado directamente.
3. **La plantilla es la fuente de verdad del estilo.** La marca no se toca clase a clase.
4. **Los demos siguen al concepto al que pertenecen** en el spec, no van al final.
5. **Si una slide queda apretada:** el texto del spec es demasiado largo — acórtalo en el spec y regenera.
6. **El slide de Reglas siempre incluye "🦻 No ocupen audífonos"** como ítem fijo. Agrégalo al construir ese slide, independiente de lo que diga el spec.
7. **Sin Markdown en el texto del PPT.** El PPT no renderiza Markdown: `**palabra**` aparece literal con los asteriscos. La negrita se aplica vía `run.font.bold = True` en python-pptx donde el diseño lo requiere, nunca con `**...**` en el texto plano.
8. **En demos/ejemplos de código, mostrar el output con `>>`** en la línea siguiente al `print()`. Ejemplo: `print("¿Te alcanza?", True)` → línea siguiente `>> ¿Te alcanza? True`. Esto va en el texto del bloque terminal del slide.
9. **Todo texto de contenido es blanco.** Nunca usar grises (`gris_claro`, `gris_secundario`) para texto en slides de contenido. El fondo oscuro ya genera contraste suficiente — el gris resulta ilegible en proyección.
