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

Las preguntas de alternativas del Ticket de Salida, cuando se proyectan en la TV, van en un `.pptx` **aparte** (`Clase NN - Tema - Ticket de Salida.pptx`), con el mismo diseño/plantilla que este PPT pero como archivo independiente — nunca como slides agregadas aquí. Razón: `Presentación.pptx` se sube a Classroom/Colab antes de dictar la clase, así que cualquier pregunta que viva en este archivo queda expuesta a los estudiantes con anticipación. Las alternativas se rotulan **A / B / C / D** (convención vigente desde 2026-07-28; antes se usaba conteo de dedos, mecanismo obsoleto desde que el TdS migró a Google Form). Se responden vía el Google Form de registro (`Clase.ipynb` ya trae el link + el nombre breve a escribir en "Tema de la clase de hoy"): Diego pasa las preguntas una por una sin revelar nada, y solo al terminar la última los estudiantes completan y envían el Form — eso evita el efecto arrastre (ver CLAUDE.md regla 17). (Generación de este PPT aparte: aún no automatizada en este skill — por ahora es solo la convención de archivo/diseño documentada en el CLAUDE.md del proyecto, regla 17.)

Estructura fija de slides:

```
1. Bienvenida
2. Objetivo + Propósito + Reglas
3. Haz Ahora
4..N  ICN — 1 slide dos_columnas por bloque de conceptos clásicos consecutivos
N+1.  Errores típicos
N+2.  Cierre  ← última slide (Objetivo + Comprensión 1-5 + Propósito)
```

Fuente de datos del slide de Cierre: la misma sección `### Cierre` del spec que ya consume `generar-colab-clase` (Objetivo de la clase + Pregunta 1 — Metacognición + Pregunta 2 — Actitud proyectada). No hay que duplicar contenido en el spec — el parser de `crear_ppt.py` reutiliza el mismo formato estructurado.

## Arquitectura del generador

El generador tiene tres capas:

1. **Parser** (`parsear_spec` en `crear_ppt.py`) — lee el spec y produce una estructura semántica. Los demos (`**Demostración:**`) se parsean en el cuerpo de cada concepto para que queden asociados al concepto que los precede en el spec.

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

**Metadata que se elimina antes de parsear** (no aparece en el PPT): `**Propósito:**`, `**Actividad:**`, `**Respuestas esperadas:**`, líneas de minutos `(N min)`.

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

## Archivos en esta carpeta

| Archivo | Rol |
|---|---|
| `SKILL.md` | Este archivo |
| `crear_ppt.py` | Orquestador: parser + renderizador + constructores de slide |
| `planificar_slides.py` | Capa de planificación pedagógica (cuántos slides, qué composición) |
| `construir_plantilla.py` | Define paleta, tipografías y helpers visuales; regenera `plantilla_marca.pptx` |
| `plantilla_marca.pptx` | Plantilla con slides modelo (bienvenida, objetivo, tabla, anatomía, analogía, apilado, etc.) |

## Limitaciones conocidas

- **Haz Ahora con código Python y preguntas asociadas (`codigo_preguntas`):** el planificador no tiene un tipo dedicado para esto todavía. Si el spec trae un Haz Ahora de este tipo, el generador lo trata como tipo `libre` (todo el texto en una sola caja con borde ámbar). Si el resultado queda apretado o poco legible, avisa a Diego — puede que convenga reformular el Haz Ahora como `situaciones` o `libre` en el spec, o pausar para implementar el tipo dedicado en `planificar_slides.py`.

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
