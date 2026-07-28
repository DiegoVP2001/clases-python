---
name: generar-colab-clase
description: Genera el Jupyter notebook principal de una clase (Clase NN - Tema - Clase.ipynb) a partir de un Clase NN - Tema - Spec.md aprobado. Usa esta skill solo después de que la skill disenar-clase haya producido y Diego haya aprobado el spec. Produce un .ipynb sin ninguna solución, listo para subir a Google Colab, con Haz Ahora, ICN, Práctica Guiada, Práctica Independiente y Cierre, y además genera/inicia Clase NN - Tema - Solucionario.ipynb con TODAS las soluciones (Haz Ahora, Guiada, Independiente y las preguntas MCQ del Ticket de Salida) — solo para el profesor.
---

# Skill: Generar Colab de clase (Clase NN - Tema - Clase.ipynb)

## Propósito

Transformar un `Clase NN - Tema - Spec.md` aprobado en un Jupyter notebook (`.ipynb`) listo para subir a Google Colab. El notebook generado tiene la estructura estándar de las clases de Python 3ro y 4to medio y es consistente entre todas las clases del programa.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Genera el Colab de clase"
- "Procede al notebook"
- "Vamos al .ipynb"
- "Ya aprobé el spec, sigamos"

**Requisito previo obligatorio:** debe existir un archivo `Clase NN - Tema - Spec.md` aprobado en la carpeta `clases/clase-NN-tema/`. Si no existe, NO procedas: indica a Diego que primero debe diseñar la clase con la skill `disenar-clase`.

## Verificaciones antes de generar

Antes de ejecutar el script, valida:

1. **Existe el spec.** Confirma que `clases/clase-NN-tema/Clase NN - Tema - Spec.md` está presente.
2. **El spec está aprobado.** El estado en el archivo debe decir "Spec aprobada".
3. **Python y nbformat disponibles.** Verifica con `python --version` y `python -c "import nbformat"`. Si falla nbformat, ejecuta `pip install nbformat` (en Windows con Python del sistema, normalmente funciona sin más; en sistemas con `pip` restringido puede necesitarse `pip install --user nbformat`).
4. **No existe ya un `Clase NN - Tema - Clase.ipynb` con cambios manuales.** Si existe, pregunta a Diego si quiere sobrescribir.
5. **Los conceptos del spec corresponden a la clase Picuino indicada.** Consulta `referencia-curriculo` para confirmar que no se adelantan contenidos fuera de la progresión 1 a N (ver restricción permanente "No adelantes contenidos no vistos" en `CLAUDE.md`). Si detectas un desajuste, avisa a Diego antes de generar.

## Cómo se ejecuta

La generación se hace con el script Python `crear_colab.py` que vive en esta misma carpeta de skill. El script:

1. Lee el `Clase NN - Tema - Spec.md` y parsea sus secciones.
2. Construye un objeto notebook con `nbformat`.
3. Lo escribe como `.ipynb` en la ruta indicada.

Comando estándar de ejecución (desde la raíz del proyecto):

```powershell
python -X utf8 ".claude/skills/generar-colab-clase/crear_colab.py" "clases/clase-NN-tema/Clase NN - Tema - Spec.md" "clases/clase-NN-tema/Clase NN - Tema - Clase.ipynb"
```

**Nota Windows:** usar siempre `-X utf8` para evitar `UnicodeEncodeError`. Los nombres de archivo con tildes y espacios requieren comillas.

## Estructura del notebook generado

El script produce un notebook con esta estructura fija (las skills posteriores como `generar-ppt-clase` asumen este orden):

| Celda | Tipo | Contenido |
|---|---|---|
| 0 | Markdown | Encabezado con número de clase, tema, curso, duración |
| 1 | Markdown | Objetivo y contenidos previos/nuevos (sin propósito — ver regla abajo) |
| 2 | Markdown | Sección "1️⃣ Haz Ahora" con la actividad |
| 3 | Code | Espacio en blanco para notas del estudiante |
| 4 | Markdown | Sección "2️⃣ ICN" con conceptos numerados |
| 5+ | Code | Ejemplos ejecutables del ICN (uno o varios) |
| n | Markdown | Tabla de errores típicos |
| n+1 | Markdown | Sección "3️⃣ Práctica Guiada" con situación y pasos (SIN celda "Mis respuestas" — ver regla abajo) |
| n+2 | Code | Espacio en blanco para construir el código |
| n+3 | Markdown | Sección "4️⃣ Práctica Independiente" (1 ejercicio obligatorio + 1 bonus) |
| ... | MD+Code alternados | Cada ejercicio con su enunciado y celda vacía |
| n+k | Markdown | Sección "🎫 Ticket de Salida" — anuncio de que se proyecta en la tele + link al Form + nombre breve a escribir en "Tema de la clase de hoy", sin preguntas (ver regla abajo) |
| último | Markdown | Cierre y preguntas de reflexión |

**Este notebook NO contiene ninguna solución, ni siquiera oculta con `<details>`.** Ni el Ticket de Salida, ni las respuestas del Haz Ahora, ni la solución de la Guiada, ni las de Independiente. Todo eso se genera en un segundo archivo, `Clase NN - Tema - Solucionario.ipynb`, en el mismo paso — ver sección "Solucionario (todas las soluciones)" más abajo.

**Práctica Guiada — nunca lleva celda "Mis respuestas".** Diego siempre escribe el código directamente en la celda de código (`# Tu programa`), nunca respuestas de texto aparte. El notebook pasa directo del enunciado/pasos guiados a la celda de código vacía. (Esto es específico de la Guiada — la celda "Mis respuestas — Parte A" de ejercicios Independiente con análisis de error, y la celda "Mis respuestas" del Haz Ahora y del Cierre, no cambian.)

**Ticket de Salida — placeholder en el Colab de clase.** El Colab de clase SÍ incluye una sección `## 🎫 Ticket de Salida` justo antes del Cierre, pero solo con un aviso de que las preguntas se proyectan en la tele — nunca las preguntas ni alternativas, que siguen viviendo exclusivamente en `Solucionario.ipynb`. Esa sección incluye además el link directo al Google Form recurrente de registro (`https://forms.gle/sjRpbgmQzrpkEBsH9`) y el nombre breve que cada estudiante debe escribir en el campo "Tema de la clase de hoy" del Form — el generador lo deriva solo del slug de la carpeta de la clase (`clase-16-for-range` → "for range"), sin que Diego tenga que indicarlo en el spec. La dinámica: las preguntas se proyectan una por una sin revelar nada, y solo al final los estudiantes completan y envían el Form; recién ahí se revisan las respuestas correctas en conjunto.

## Después de generar

1. **Ejecuta el notebook para verificar que el código corre sin errores**, antes de presentárselo a Diego:
   ```bash
   jupyter nbconvert --to notebook --execute --output <mismo-archivo> "Clase NN - Tema - Clase.ipynb"
   ```
   Si una celda lanza una excepción (`NameError`, `SyntaxError`, etc.) o el output no calza con el `>>` documentado en el spec, corrige el notebook y vuelve a ejecutar — no se lo muestres a Diego con errores sin detectar. Esto atrapa bugs de variables mal escritas o lógica incorrecta antes de que lleguen al aula. Si `nbconvert`/`nbclient` no está disponible, instala con `pip install nbconvert` o avisa a Diego.
2. Confirma a Diego que el archivo se creó, se ejecutó sin errores, y dónde está. Confirma también que `Clase NN - Tema - Solucionario.ipynb` se generó (o actualizó) junto con él, y recuérdale que ese archivo es exclusivamente para él — el Ticket de Salida se proyecta en clase, y el resto (Haz Ahora, Guiada, Independiente) recién se sube a Classroom después de dictar la clase, nunca antes.
3. **Recomienda subirlo a Google Colab** para revisarlo en el entorno real antes de aprobar:
   - Abrir https://colab.research.google.com
   - `Archivo` → `Subir cuaderno`
   - Seleccionar el `.ipynb` recién generado
4. **Espera el feedback de Diego antes de avanzar al Colab de ejercicios.**
5. Cuando Diego apruebe, registra en `Clase NN - Tema - Historial.md`:

```markdown
## [fecha] — Colab de clase aprobado
- Archivo: Clase NN - Tema - Clase.ipynb
- Generado con la skill generar-colab-clase
- [notas de iteraciones si las hubo]
```

6. Commitea y pushea **solo la carpeta de esta clase** a GitHub (ver "Protocolo de cierre de etapa" en el `CLAUDE.md` raíz) — incluye `Clase.ipynb` y `Solucionario.ipynb`:

```
git add "clases/clase-NN-tema-breve/"
git commit -m "Clase NN - Tema: Colab de clase aprobado"
git push
```

Si el push falla, avisa a Diego con el error explícito — no reintentes con `--force`.

7. Confirma qué se subió a GitHub y entrega el link directo de Google Colab para `Clase.ipynb`:
   `https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-NN-tema-breve/Clase%20NN%20-%20Tema%20-%20Clase.ipynb`
   Con esto, la recomendación de subida manual del paso 3 ya no es necesaria para futuras aperturas — el link de GitHub reemplaza el `Archivo → Subir cuaderno`.
8. Después de confirmar, di: *"Antes de continuar al Colab de ejercicios, ejecuta `/compact` para limpiar el contexto. Avísame cuando estés listo."* Cuando Diego confirme, activa la skill `generar-colab-ejercicios`.

## Iteración sobre el .ipynb

Si Diego pide cambios:

- **Cambios cosméticos** (corregir typo, ajustar emoji, mejorar redacción puntual): edita directamente el `.ipynb` con la herramienta de edición.
- **Cambios estructurales** (modificar un ejercicio, cambiar el ticket): primero **actualiza el `Clase NN - Tema - Spec.md`**, luego regenera el `.ipynb` con el script. NUNCA edites el spec y el notebook como dos cosas separadas: el spec es la fuente de verdad.
- **Cambios sistémicos** (algo que debería aplicar a todas las clases futuras, ej: "los Haz Ahora deben tener 2 celdas de código en vez de 1"): edita el script `crear_colab.py` y avísale a Diego que el cambio aplicará a todas las clases que regeneres a partir de ahora.

## Reglas críticas

1. **El spec es la fuente de verdad.** Si hay discrepancia entre spec y notebook, gana el spec. Regenera el notebook.
2. **Nunca cargues ejemplos de código fuera del spec.** Si el spec define 3 ejercicios, el notebook tiene 3 ejercicios. No agregues por iniciativa propia.
3. **Ninguna solución en el notebook de estudiante, ni siquiera oculta con `<details>`.** Todas las soluciones (Haz Ahora, Guiada, Independiente, Ticket) van exclusivamente a `Solucionario.ipynb`.
4. **Si el script falla en parsear alguna sección**, NO inventes contenido. Avisa a Diego que esa sección quedó vacía y pregunta cómo proceder (la causa típica es que el spec no sigue el formato esperado).

## Principios de diseño del notebook

Verificar que el spec cumpla estos principios antes de generar. Si no los cumple, corregir el spec sin preguntar.

**Encabezado y metadatos**
- Curso por defecto: `"3ro y 4to medio"` (no solo "4to medio").

**Haz Ahora**
- Incluir celda markdown de respuestas con slots numerados según los ítems del Haz Ahora (conteo dinámico — no hardcodear 6).
- Las respuestas esperadas del Haz Ahora van SOLO en `Solucionario.ipynb` — nunca en el cuerpo del notebook de estudiante ni como nota o pie de página al final de la sección Haz Ahora.
- En el spec, marcar las respuestas con `**Respuestas esperadas:** ...` al final de la sección — el parser las extrae automáticamente.
- NO revelar operadores, funciones ni sintaxis de hoy — ni en los enunciados ni en columnas de tabla.
- **NO incluir la línea `**Propósito:**` del Haz Ahora en el notebook.** Es una nota interna de diseño del spec (para Diego al planificar), no contenido para estudiantes. El generador la filtra automáticamente — el spec puede mantenerla sin problema.

**Propósito**
- El propósito de la sección `## Propósito` del spec **SÍ se incluye** en el notebook, como `## 💡 Propósito` en blockquote `>`, inmediatamente después del objetivo. Es contenido para estudiantes.
- Lo que **NO se incluye** es la línea `**Propósito:**` dentro de la sección Haz Ahora del spec — esa es una nota interna de diseño para Diego y el generador la filtra automáticamente.

**Práctica Guiada — pasos y resultado en tabla de 2 columnas (default)**
Los pasos guiados y su resultado esperado se escriben en el spec como `**Pasos guiados (tabla):**`, con un bloque por paso que trae su propio resultado — no como lista numerada + un bloque de resultado único al final. El generador arma automáticamente una tabla HTML de 2 columnas (`Qué debe hacer tu programa` | `Resultado esperado`). Formato canónico en el spec:
```markdown
**Pasos guiados (tabla):**

- Paso 1: [texto del paso, en lenguaje natural, sin revelar variable/operador]
  Resultado:
  ```
  [output esperado, o una nota tipo "(todavía no hay output — es solo la variable inicial)" si el paso no produce output propio]
  ```

- Paso 2: [texto del paso]
  Resultado:
  ```
  [output esperado]
  ```
```
Agrupa en una misma fila los pasos que van juntos (ej: "construye el bucle" + "dentro del bucle, suma y muestra") cuando separarlos dejaría una fila sin resultado propio que mostrar — no hace falta que el número de filas de la tabla coincida 1:1 con cada micro-paso de la situación. El resultado de cada fila puede acortarse con `...` si es una secuencia larga y repetitiva (ver "Errores típicos" más abajo no aplica aquí — es solo para mantener la tabla legible).

Si el `paso` o el `resultado` de una fila incluyen código entre backticks (`` `range()` ``), el generador los convierte automáticamente a `<code>` — Jupyter/Colab NO reprocesa markdown inline dentro de un bloque `<table>` crudo, así que los backticks sin convertir quedarían literales en vez de renderizarse con estilo de código. No hace falta escribir `<code>` a mano en el spec, basta con backticks como en cualquier otra sección.

Formato antiguo (retrocompatible, solo para regenerar clases anteriores a este cambio): `**Pasos guiados:**` con lista numerada + `**Resultado esperado:**` con un bloque de código único al final. El parser detecta cuál formato usa el spec automáticamente.

**Práctica Guiada — tabla de rangos o clasificación**
Cuando la situación de la guiada incluye una tabla de correspondencia (ej: rango de monto → actividad recomendada, temperatura → categoría, etc.), esa tabla se escribe en el spec y aparece en el notebook como **tabla HTML** con encabezados `<th>`, NO como bloque de código de texto plano con `────` o `→`. Formato canónico:
```html
<table>
<tr>
  <th>Categoría de entrada</th>
  <th>Resultado o acción</th>
</tr>
<tr><td>Rango o valor</td><td>Descripción</td></tr>
...
</table>
```
Esto garantiza que se renderice correctamente en Colab y tenga el mismo nivel visual que las tablas de los ejercicios independientes.

**Ticket de Salida — preguntas solo en el Solucionario, placeholder en Clase.ipynb**
Las preguntas y alternativas del Ticket de Salida nunca se renderizan en `Clase.ipynb`. El parser las extrae (`**Pregunta N:**` + alternativas `- 1 dedo:`..`- 4 dedos:` + `**Respuesta correcta:**` + `**Justificación:**`) desde la sección `### 5. Ticket de Salida` del spec y las escribe únicamente en `Clase NN - Tema - Solucionario.ipynb`. Las alternativas se rotulan por cantidad de dedos (no A/B/C/D) porque se responden mostrando los dedos todos al mismo tiempo tras un conteo, no en voz alta — ver CLAUDE.md regla 17. En `Clase.ipynb`, si el spec tiene `ticket_mcq`, se agrega automáticamente una sección `## 🎫 Ticket de Salida` justo antes del Cierre con el aviso de que se proyecta en la tele, el link al Google Form de registro y el nombre breve a escribir en "Tema de la clase de hoy" — no requiere nada en el spec, el generador la arma sola (ver `derivar_tema_breve_form()` y `generar_seccion_ticket_placeholder()` en `crear_colab.py`). Ver sección "Solucionario (todas las soluciones)" más abajo.

**Haz Ahora — respuestas esperadas multiline**
El campo `**Respuestas esperadas:**` en el spec captura todo el texto hasta el fin de la sección Haz Ahora (no solo la primera línea). Escríbelas con items numerados, uno por línea. El generador las mueve automáticamente a `Solucionario.ipynb`.

**Enunciados**
- Ejemplos de input en lenguaje natural: "si alguien ingresa un saldo de \$80.000" — nunca `saldo_cuenta_rut = 80000`. El `$` siempre escapado como `\$` en texto markdown/prosa del spec — sin escapar, Colab lo interpreta como delimitador de fórmula MathJax y descuadra el texto.
- Enunciados de Independiente sin comandos (`input()`, operadores, nombres de variables) — solo descripción de qué calcular.
- Pasos de Guiada en lenguaje natural de alto nivel: "Crea una variable que registre el saldo" — sin revelar nombre exacto ni operador.
- Evitar temas sensibles en variables de la Guiada (ej: "restricción de edad", "calorías", "diagnóstico"). Usar variantes neutras ("bloqueado en país", "contenido exclusivo").

**Outputs**
- Los `print()` de ejercicios y soluciones siempre llevan texto descriptivo.
- El resultado esperado muestra el output con etiqueta, no solo `True` o `False`.
- En celdas de ejemplo del ICN y la Guiada, muestra el resultado de cada `print()` en la línea siguiente con `>>`. Ejemplo:
  ```python
  print("¿Te alcanza?", saldo >= precio)
  >> ¿Te alcanza? False
  ```

**Formato canónico de ejercicios (Práctica Independiente)**

1 ejercicio obligatorio + 1 ejercicio bonus (fijo, no preguntar), formato "revisión rápida": narrativa breve (2-3 líneas) y normalmente sin pistas `<details>` — solo si el ejercicio realmente lo amerita. El Ejercicio 2 se marca explícitamente como bonus/décimas extra, a resolver solo si la pareja terminó el obligatorio. Cada ejercicio sigue esta estructura fija en orden:

1. **Narrativa** — 3-4 líneas de prosa, sin bullets. Contexto rico, fluye sin revelar operadores ni nombres de variables.
2. **`**El programa debe:**`** — bullets con términos clave en **negrita**. Describe qué hace el programa, no cómo.
3. **Pistas colapsables** — 1-2 según dificultad, solo donde el ejercicio lo justifica. Formato:
   ```html
   <details>
   <summary>💡 Pista N — subtítulo</summary>
   texto orientador + bloque de código si aplica
   </details>
   ```
4. **Tabla HTML side-by-side** — dos columnas, dos filas de datos:
   ```html
   <table>
   <tr><th></th><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
   <tr>
   <td>📥 <em>El usuario escribe</em></td>
   <td><pre>valores de input...</pre></td>
   <td><pre>valores de input...</pre></td>
   </tr>
   <tr>
   <td>📤 <em>El programa imprime</em></td>
   <td><pre>output del programa...</pre></td>
   <td><pre>output del programa...</pre></td>
   </tr>
   </table>
   ```
   Encabezados siempre `Ejemplo 1` y `Ejemplo 2` — sin descriptores adicionales.
5. **Celda de código vacía** — solo `# Tu solución del Ejercicio N`. Sin starter code.

**Solucionario (todas las soluciones)**
`Clase NN - Tema - Solucionario.ipynb` se genera automáticamente junto con `Clase.ipynb` (mismo comando, mismo gate de aprobación) siempre que haya algún contenido de solución en el spec. Contiene, en este orden: respuestas del Haz Ahora, solución de la Práctica Guiada, soluciones de Práctica Independiente, y las preguntas MCQ del Ticket de Salida (enunciado + 4 alternativas rotuladas 1-4 dedos + la correcta marcada con ✅ + justificación). Es exclusivamente para el profesor: el Ticket se proyecta y responde a viva voz en clase; el resto Diego lo sube a Classroom recién **después** de dictar la clase. `generar-colab-ejercicios` actualiza este mismo archivo más adelante, agregando las soluciones de `Ejercicios.ipynb` — nunca crea un segundo solucionario.

**Cierre estructurado** (clases con actitud explícita en el objetivo)
- El spec debe incluir una sección `### Cierre` con estos tres sub-bloques:
  - `**Objetivo de la clase**` + texto del objetivo
  - `**Pregunta 1 — Metacognición (escala 1-5)**` + pregunta en formato "donde 1 es... y 5 es..."
  - `**Pregunta 2 — Actitud proyectada al futuro**` + pregunta de actitud
- El notebook renderiza: objetivo reimpreso + preguntas numeradas 1. y 2. en un bloque + UNA sola celda editable `### 📝 Mis respuestas` con slots `1.` y `2.`.
- Si el spec usa el formato antiguo (lista numerada), el generador lo maneja automáticamente (retrocompatible).

**Error típico a anticipar en clases con `input()` y respuesta "si/no"**
- Siempre incluir en errores típicos: escribir `"sí"` con tilde hace que `respuesta == "si"` devuelva `False`. Solución: `respuesta == "si" or respuesta == "sí"`.

**Estructura**
- Todas las soluciones (Haz Ahora + Guiada + ejercicios + ticket) van exclusivamente a `Solucionario.ipynb` — el notebook de estudiante no las contiene en ninguna forma, ni siquiera con `<details>`.
- Sin tiempos `(N min)` en los títulos de sección del notebook.
- Lenguaje "tú"/"ustedes" en todo el texto — nunca "los estudiantes" ni "el profesor revela". Con la modalidad en parejas, los enunciados de Independiente pueden usar "ustedes"/"la pareja" cuando ayude a la claridad.

**Workflow**
- Solo preguntar a Diego en gates formales de aprobación (objetivo, estructura, Colab de clase, Colab de ejercicios, PPT).
- Correcciones técnicas intermedias: ejecutar sin preguntar.

## Limitaciones conocidas

- El script asume que el spec sigue el formato estándar generado por la skill `disenar-clase`. Si Diego editó el spec manualmente y cambió encabezados o estructura, el parser puede fallar silenciosamente en alguna sección. En ese caso, valida el output y corrige.
- Si el spec tiene ejemplos de código con triple backtick anidados, el parser puede confundirse. Esto es raro pero conviene saberlo.
- El regex del cierre estructurado usa `(?=\n\*\*|\Z)` para no cortar en bold inline — no usar `(?=\*\*|\Z)` que cortaría en medio de una frase con negrita.
