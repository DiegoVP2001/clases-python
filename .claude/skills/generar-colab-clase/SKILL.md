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
5. **Si la clase podría usar autochequeo, pregúntaselo a Diego antes de escribirlo.** Ver "Autochequeo" más abajo — es opcional y su inclusión la decide él, no Claude.
6. **Los conceptos del spec corresponden a la clase Picuino indicada.** Consulta `referencia-curriculo` para confirmar que no se adelantan contenidos fuera de la progresión 1 a N (ver restricción permanente "No adelantes contenidos no vistos" en `CLAUDE.md`). Si detectas un desajuste, avisa a Diego antes de generar.

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
| n+3 | Markdown | Sección "4️⃣ Práctica Independiente" (2 ejercicios obligatorios — default desde Clase 20) |
| ... | MD+Code alternados | Cada ejercicio con su enunciado y celda vacía |
| n+k | Markdown | Sección "🎫 Ticket de Salida" — anuncio de que se proyecta en la tele + link al Form + nombre breve a escribir en "Tema de la clase de hoy", sin preguntas (ver regla abajo) |
| último | Markdown | Cierre y preguntas de reflexión |

**Este notebook NO contiene ninguna solución, ni siquiera oculta con `<details>`.** Ni el Ticket de Salida, ni las respuestas del Haz Ahora, ni la solución de la Guiada, ni las de Independiente. Todo eso se genera en un segundo archivo, `Clase NN - Tema - Solucionario.ipynb`, en el mismo paso — ver sección "Solucionario (todas las soluciones)" más abajo. Si la clase tiene Ticket de Salida, además se genera un tercer archivo liviano, `Clase NN - Tema - Ticket de Salida Respuestas.json`, solo con las respuestas correctas — ver sección "JSON de respuestas del Ticket de Salida" más abajo.

**Práctica Guiada — nunca lleva celda "Mis respuestas".** Diego siempre escribe el código directamente en la celda de código (`# Tu programa`), nunca respuestas de texto aparte. El notebook pasa directo del enunciado/pasos guiados a la celda de código vacía. (Esto es específico de la Guiada — la celda "Mis respuestas — Parte A" de ejercicios Independiente con análisis de error, y la celda "Mis respuestas" del Haz Ahora y del Cierre, no cambian.)

**Ticket de Salida — placeholder en el Colab de clase.** El Colab de clase SÍ incluye una sección `## 🎫 Ticket de Salida` justo antes del Cierre, pero solo con un aviso de que las preguntas se proyectan en la tele — nunca las preguntas ni alternativas, que siguen viviendo exclusivamente en `Solucionario.ipynb`. Esa sección incluye además el link directo al Google Form recurrente de registro (`https://forms.gle/sjRpbgmQzrpkEBsH9`) y el nombre breve que cada estudiante debe escribir en el campo "Tema de la clase de hoy" del Form — el generador lo deriva solo del slug de la carpeta de la clase (`clase-16-for-range` → "for range"), sin que Diego tenga que indicarlo en el spec. La dinámica: las preguntas se proyectan una por una sin revelar nada, y solo al final los estudiantes completan y envían el Form; recién ahí se revisan las respuestas correctas en conjunto.

## Después de generar

1. **Ejecuta el notebook para verificar que el código corre sin errores**, antes de presentárselo a Diego:
   ```bash
   jupyter nbconvert --to notebook --execute --output <mismo-archivo> "Clase NN - Tema - Clase.ipynb"
   ```
   Si una celda lanza una excepción (`NameError`, `SyntaxError`, etc.) o el output no calza con el `>>` documentado en el spec, corrige el notebook y vuelve a ejecutar — no se lo muestres a Diego con errores sin detectar. Esto atrapa bugs de variables mal escritas o lógica incorrecta antes de que lleguen al aula. Si `nbconvert`/`nbclient` no está disponible, instala con `pip install nbconvert` o avisa a Diego.

   **Cada celda de ejemplo del ICN debe ser autocontenida:** define sus propias variables, sin depender de que se haya ejecutado una celda anterior. Un ejemplo que arranca directo con `if bateria_baja == True:` revienta con `NameError` y además obliga al estudiante a ejecutar en orden estricto. Si el spec trae un ejemplo así, agrégale las asignaciones al inicio (es una corrección técnica: se hace en el spec y se regenera, sin preguntar).

   **Después de ejecutar, limpia los outputs que no correspondan:**
   ```bash
   python -X utf8 ".claude/skills/generar-colab-clase/limpiar_outputs_haz_ahora.py" "clases/clase-NN-tema/Clase NN - Tema - Clase.ipynb"
   ```
   La ejecución de verificación deja los outputs guardados dentro del `.ipynb`. **Solo el ICN debe conservarlos** (el estudiante lee el ejemplo junto a su resultado, sin depender de haber ejecutado en orden); el script limpia todas las demás secciones. Un Haz Ahora cuyo trabajo es *ejecutar y observar* pierde el sentido si el resultado ya viene impreso, y una celda de verificación que trae su salida invita a leerla en vez de correrla.
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

**Haz Ahora — celdas de código ejecutables (desde Clase 19.5)**
Si la sección `### 1. Haz Ahora` del spec trae bloques ` ```python `, cada uno sale como **celda de código ejecutable** y el texto intermedio queda en celdas markdown, en el orden del spec (`generar_celdas_haz_ahora()` en `crear_colab.py`). Es el formato indicado cuando el Haz Ahora consiste en correr programas con un error y observar qué imprimen — en vez de pedir "predice sin ejecutar", que es justo lo que no corresponde en un Colab. Si el spec no trae bloques de código, sale una sola celda markdown como siempre. Recuerda limpiarles el output después de la ejecución de verificación (ver "Después de generar").

**Cada programa lleva su propio enunciado.** Si el Haz Ahora muestra código de una prueba o actividad anterior, no basta con rotularlo `**Programa N**`: nadie —tampoco Diego— se acuerda de qué tenía que hacer ese programa. Va un título con el escenario (`**Programa 1 — La app de hábitos de estudio**`) y debajo una línea `*Lo que debía hacer:* …` describiendo el comportamiento correcto en lenguaje natural. Sin eso, la pregunta "¿qué debería imprimir?" no se puede contestar.

**Espacios de respuesta intercalados: `[[respuesta]]`.** Una línea con solo `[[respuesta]]` inserta ahí una celda markdown editable (`📝 **Tu respuesta**`). Úsala para dejar el espacio pegado a cada pregunta, justo debajo del bloque de código que la motiva — es lo que corresponde cuando el Haz Ahora alterna programa → pregunta → programa → pregunta. Si el spec usa este marcador, el generador **no** agrega la celda única de "Mis respuestas" al final; si no lo usa, el comportamiento es el de siempre (una celda con un slot numerado por pregunta).

**Haz Ahora**
- Incluir celda markdown de respuestas con slots numerados según los ítems del Haz Ahora (conteo dinámico real — nunca forzar un piso artificial. Bug detectado y corregido en Clase 20: el código forzaba mínimo 3 blancos aunque el spec tuviera menos preguntas; ahora `num_items` usa el conteo real, con fallback de 1 solo si no detecta ninguna).
- Las respuestas esperadas del Haz Ahora van SOLO en `Solucionario.ipynb` — nunca en el cuerpo del notebook de estudiante ni como nota o pie de página al final de la sección Haz Ahora.
- En el spec, marcar las respuestas con `**Respuestas esperadas:** ...` al final de la sección — el parser las extrae automáticamente.
- NO revelar operadores, funciones ni sintaxis de hoy — ni en los enunciados ni en columnas de tabla.
- **NO incluir las etiquetas `Propósito:` ni `Actividad:` del Haz Ahora en el notebook.** Son notas internas de diseño del spec, no contenido para estudiantes. `disenar-clase` ya no debe escribirlas en el spec final (ver su propio SKILL.md) — pero el generador igual las filtra como red de seguridad, acepte o no negrita (`generar_seccion_haz_ahora()` en `crear_colab.py`; bug corregido en Clase 20: el filtro original solo reconocía `**Propósito:**` con negrita exacta, y un spec que la escribió sin negrita se filtró al notebook de estudiante).

**Propósito**
- El propósito de la sección `## Propósito` del spec **SÍ se incluye** en el notebook, como `## 💡 Propósito` en blockquote `>`, inmediatamente después del objetivo. Es contenido para estudiantes.
- Lo que **NO se incluye** es la etiqueta `Propósito:` (con o sin negrita) dentro de la sección Haz Ahora del spec — ver punto anterior.

**Práctica Guiada — mismo formato canónico que Independiente (default desde Clase 20)**
La Guiada comparte escenario con el Haz Ahora (ver arriba) y se escribe como un solo ejercicio guiado: narrativa libre (sin necesidad de etiqueta `**Situación:**`) + `**El programa debe:**` en bullets + pista(s) `<details>` opcionales + `**Resultado esperado:**`. El parser detecta este formato buscando `**El programa debe:**` en la sección; si lo encuentra, toma todo el texto libre anterior como narrativa (con o sin la etiqueta `**Situación:**` — ambas funcionan). Formato canónico en el spec:
```markdown
[Narrativa — retoma el escenario del Haz Ahora, con una pregunta distinta ya "bajada a código"]

**El programa debe:**
- [requisito 1, en lenguaje natural de alto nivel]
- [requisito 2]

**Resultado esperado:**
```
[output esperado — un solo bloque si no hay input() con valores variables; acórtalo con `...` si es largo y repetitivo]
```

- Solución:
  ```python
  [código de referencia]
  ```
```
Los backticks dentro de los bullets de "El programa debe" se convierten automáticamente a `<code>` — no hace falta escribir `<code>` a mano en el spec.

**Formato antiguo (retrocompatible, solo para regenerar clases anteriores a Clase 20):** `**Situación:**` + `**Pasos guiados (tabla):**`, con un bloque por paso que trae su propio resultado — el generador arma una tabla HTML de 2 columnas (`Qué debe hacer tu programa` | `Resultado esperado`):
```markdown
**Situación:** [contexto narrativo]

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
```
Agrupa en una misma fila los pasos que van juntos (ej: "construye el bucle" + "dentro del bucle, suma y muestra") cuando separarlos dejaría una fila sin resultado propio que mostrar. El resultado de cada fila puede acortarse con `...` si es una secuencia larga y repetitiva. Existe también un formato aún más antiguo (`**Pasos guiados:**` con lista numerada + `**Resultado esperado:**` único al final). El parser detecta automáticamente cuál de los tres formatos usa el spec — no hace falta indicarlo.

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

**Ticket de Salida — 3 preguntas fijas, con código, solo en el Solucionario**
Las preguntas y alternativas del Ticket de Salida nunca se renderizan en `Clase.ipynb`. El parser las extrae (`**Pregunta N:**` + bloque `` ```python...``` `` opcional + alternativas `- A:`..`- D:` + `**Respuesta correcta:**` + `**Justificación:**`) desde la sección `### 5. Ticket de Salida` del spec y las escribe únicamente en `Clase NN - Tema - Solucionario.ipynb`. **Cantidad fija: 3 preguntas siempre** (default desde Clase 20 — antes dependía de la cantidad de conceptos del ICN). Cada pregunta trae opcionalmente un bloque de código breve (justo después de `**Pregunta N:**`, antes del enunciado) — el parser lo detecta automáticamente vía `parsear_ticket_mcq()` en `crear_colab.py` y lo antepone al enunciado en el Solucionario; si la pregunta no trae código, se omite ese bloque sin problema (retrocompatible con specs anteriores). **Reparte la respuesta correcta en una letra distinta por pregunta** — nunca las 3 en la misma alternativa. Las alternativas se rotulan A/B/C/D (convención vigente desde 2026-07-28 — antes se rotulaban por cantidad de dedos, mecanismo obsoleto desde que el TdS migró a Google Form); se responden vía el Google Form de registro (no en voz alta, ni antes de terminar la última pregunta) — ver CLAUDE.md regla 17. En `Clase.ipynb`, si el spec tiene `ticket_mcq`, se agrega automáticamente una sección `## 🎫 Ticket de Salida` justo antes del Cierre con el aviso de que se proyecta en la tele, el link al Google Form de registro y el nombre breve a escribir en "Tema de la clase de hoy" — no requiere nada en el spec, el generador la arma sola (ver `derivar_tema_breve_form()` y `generar_seccion_ticket_placeholder()` en `crear_colab.py`). Ese nombre breve sale del slug de la carpeta (`clase-16-for-range` → `for range`); si el nombre de la carpeta no sirve de cara a los estudiantes, el spec puede declarar el suyo en el Contexto con `- **Tema breve (Form):** ...` y ese manda. Cambiarlo ahí es preferible a renombrar la carpeta, porque los links de Colab ya pusheados a GitHub apuntan a la ruta vieja. Ver sección "Solucionario (todas las soluciones)" más abajo.

**JSON de respuestas del Ticket de Salida (`Clase NN - Tema - Ticket de Salida Respuestas.json`)**
Si el spec tiene `ticket_mcq`, el generador también escribe un JSON aparte junto al Solucionario, vía `construir_ticket_respuestas()` en `crear_colab.py`. Es intencionalmente liviano — solo las respuestas correctas, sin enunciado ni justificación — para que el agente que cruce las respuestas del Google Form (ver [[tds-trazabilidad-sheet]] en memoria) lo lea rápido sin abrir el Solucionario ni el `.py`. Formato fijo:
```json
{
  "clase": 16,
  "tema": "for range",
  "respuestas": {
    "Respuestas a ticket [1]": "2",
    "Respuestas a ticket [2]": "1",
    "Respuestas a ticket [3]": "No se preguntó",
    "Respuestas a ticket [4]": "No se preguntó"
  }
}
```
`tema` es el mismo nombre breve que se le pide al estudiante escribir en el Form (`tema_breve_form`), así el cruce hace match directo por texto. Las llaves de `respuestas` replican tal cual el nombre de columna que el Form genera en la Sheet ("Respuestas a ticket [1]".."[4]") — así el agente que cruza matchea columna-a-llave sin traducir nada. `respuestas` siempre trae las 4 llaves — las preguntas reales ocupan las primeras en orden y las que sobran (si la clase tuvo menos de 4 preguntas) quedan como `"No se preguntó"`, nunca se omiten, para que el agente que cruza no tenga que manejar casos de llaves faltantes.

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

**Formato canónico de ejercicios (Práctica Independiente y Práctica Guiada — mismo formato, default desde Clase 20)**

**2 ejercicios obligatorios** (fijo, no preguntar — reemplaza el esquema anterior "1 obligatorio + 1 bonus/décimas extra"). Ambos con la misma exigencia de narrativa, ninguno se marca como bonus. La Guiada usa este mismo formato como un ejercicio único guiado (ver más arriba). Cada ejercicio sigue esta estructura fija en orden, implementada en `parsear_independiente()` / `generar_ejercicio_independiente()` (y su equivalente `parsear_guiada()` / `generar_seccion_guiada_intro()` para la Guiada) en `crear_colab.py`:

1. **Narrativa** — 3-4 líneas de prosa, sin bullets. Contexto rico, fluye sin revelar operadores ni nombres de variables. Es todo el texto libre antes de `**El programa debe:**` — no necesita ninguna etiqueta.
2. **`**El programa debe:**`** — bullets con términos clave en **negrita**. Describe qué hace el programa, no cómo. El parser corta este bloque en la primera línea que empieza con `-` hasta encontrar `Resultado esperado:` (con o sin negrita) o el final de la sección.
3. **Pistas colapsables** — 1-2 según dificultad, solo donde el ejercicio lo justifica (ej: recordar un operador que no es el foco de la clase). El parser las extrae completas vía regex (`<details>.*?</details>`) desde cualquier punto del bloque y las renderiza justo después de los bullets, antes del resultado — no importa en qué línea exacta del spec estén escritas. Formato:
   ```html
   <details>
   <summary>💡 Pista N — subtítulo</summary>
   texto orientador + bloque de código si aplica
   </details>
   ```
4. **`**Nota:**` (opcional, desde 2026-08-04)** — una frase breve que se renderiza en cursiva justo después de las pistas y antes del resultado esperado. Pensada para lo que no cabe en un bullet de "El programa debe" ni en una pista: típicamente, explicarle al estudiante por qué esta vez sí se le exigen nombres de variable exactos (excepción a la regla 8 del `CLAUDE.md`, necesaria cuando el ejercicio trae autochequeo). El parser (`parsear_independiente()` / `parsear_guiada()`) la extrae con `\*\*Nota:\*\*` antes de correr el filtro de bullets — si se escribe como texto suelto sin la etiqueta, se pierde en silencio igual que le pasaba antes a cualquier bloque HTML sin `**Resultado esperado:**` delante.
5. **Resultado esperado** — el generador SIEMPRE lo renderiza con el mismo lenguaje visual que las evaluaciones (ícono + `<em>` + `<pre>`), nunca como bloque de código markdown plano ni como etiqueta `**Resultado esperado:**` a secas — aunque en el spec se escriba como bloque simple (`**Resultado esperado:**` seguido de un bloque ` ``` `), es el generador (`generar_ejercicio_independiente()` / `generar_seccion_guiada_intro()`) el que lo transforma al renderizar. Dos variantes según si el ejercicio usa `input()` con valores que varían:
   - **Sin input() (caso típico de `for`/`for` anidado — valores fijos, salida determinista):** `📤 <em>El programa imprime:</em>` seguido de `<pre>...</pre>` con el output esperado. Acórtalo con `...` si es una secuencia larga y repetitiva (ver Clase 20 como referencia).
   - **Con input() de valor variable:** tabla HTML side-by-side — dos columnas, dos filas de datos:
     ```html
     <table>
     <tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
     <tr>
     <td>📥 <em>El usuario ingresa</em><pre>valores de input...</pre></td>
     <td>📥 <em>El usuario ingresa</em><pre>valores de input...</pre></td>
     </tr>
     <tr>
     <td>📤 <em>El programa imprime</em><pre>output del programa...</pre></td>
     <td>📤 <em>El programa imprime</em><pre>output del programa...</pre></td>
     </tr>
     </table>
     ```
     Encabezados siempre `Ejemplo 1` y `Ejemplo 2` — sin descriptores adicionales. Cada celda combina ícono + `<em>` + `<pre>` (igual al formato usado en las evaluaciones, ej. `Clase 19 - Evaluación Condicionales - Evaluación.ipynb`). **Implementado desde Clase 19.5** (`extraer_resultado_tabla()` en `crear_colab.py`): en el spec se escribe `**Resultado esperado:**` seguido del `<table>` HTML crudo — el generador se queda con la tabla y descarta la etiqueta, para que quede igual que en las evaluaciones. Los saltos de línea dentro de un `<pre>` van como saltos reales, no como `<br>`. Si el spec usa una tabla markdown (`| … |`) en vez del `<table>`, el parser no la reconoce y el resultado esperado **se pierde en silencio** — usa siempre HTML.
6. **Celda de código vacía** — solo `# Tu solución del Ejercicio N` (Independiente) o `# Tu programa` (Guiada). Sin starter code.

**Práctica Independiente diferenciada por rutas (desde Clase 19.5)**
Cuando la clase reparte trabajo distinto según el tramo, el spec agrupa los ejercicios bajo encabezados `#### Ruta X — descripción`, cada ruta con su propia numeración desde 1 (`parsear_independiente_estructura()`). El generador emite un bloque `### 🧭 Ruta X — …` por ruta con su párrafo introductorio, y etiqueta las celdas de respuesta como `Ruta A — Ejercicio 1` para que no se confundan entre rutas; en el Solucionario los títulos quedan como `Ruta A · Ejercicio 1 — …`. Si no hay encabezados `#### Ruta`, el comportamiento es el de siempre (lista plana).

**Rótulos de ruta: neutros, nunca por rendimiento.** El notebook lo abre el curso entero, así que los títulos de ruta describen **el trabajo** ("Diseñar los casos que rompen programas" / "Escribir los programas"), nunca a quién le toca ("para quienes dejaron los ejercicios sin terminar"). Quién va en qué ruta lo dice Diego en la sala; en el spec eso se registra como `Nota de conducción:`.

**Directivas por ejercicio** (todas opcionales, útiles sobre todo en clases diferenciadas):
- `**El trabajo debe:**` — alias de `**El programa debe:**` para ejercicios cuyo producto no es un programa (ej. una batería de casos de prueba). Se renderiza con la misma etiqueta que trae el spec.
- `**Celda de respuesta:**` — `código` (default), `markdown`, o `markdown + código`. Define qué celda(s) recibe el estudiante para responder. Un ejercicio que se entrega como tabla necesita `markdown`; uno que exige decidir la estructura antes de programar, `markdown + código`.
- `**Plantilla de respuesta:**` — markdown (típicamente una tabla con filas en blanco) que se copia dentro de la celda editable del estudiante. Es la forma canónica de dar andamiaje sin romper la regla de "celda de código siempre vacía": la tabla de decisión va en la celda de respuesta, no como starter code. **Va siempre al final del bloque del ejercicio**, antes de `- Solución:` — se captura hasta el fin del bloque, así admite varias tablas seguidas.
- `**Solución de referencia:**` — respuesta modelo en markdown para ejercicios que no tienen `- Solución:` en python. Va solo al Solucionario. Termina en la siguiente línea que empiece con `**`, así que colócala antes de `**Celda de respuesta:**`.

- `**Celda de verificación:**` + bloque ` ```python ` — la llamada al autochequeo que el estudiante ejecuta para saber solo/a si le quedó bien. Sale como celda de código propia. Su posición depende de para qué sirve, y el generador lo resuelve solo: si el ejercicio se responde **escribiendo código**, la verificación revisa ese código y va **después**; si se responde en **markdown**, es la herramienta con la que explora antes de escribir su conclusión y va **antes**.

Orden obligatorio dentro del bloque de un ejercicio: narrativa → `**El programa/trabajo debe:**` → `<details>` → `**Nota:**` → `**Resultado esperado:**` → `**Celda de verificación:**` → `**Solución de referencia:**` → `**Celda de respuesta:**` → `**Plantilla de respuesta:**` → `- Solución:`. El parser trunca el bloque en `- Solución:`, así que cualquier cosa escrita después se pierde.

**Autochequeo: `**Celda de configuración:**` (desde Clase 19.5)**

> ⚠️ **Pregúntale siempre a Diego antes de incluirlo.** El autochequeo NO es parte del formato por defecto de una clase: es una capacidad opcional que se agrega solo cuando él lo pide. Antes de escribir cualquier celda de configuración o de verificación en un spec, pregúntale explícitamente si quiere incluir el verificador en esta clase, y espera su respuesta. Esta es una excepción deliberada a la regla general de "aprobación solo en los gates formales" (`CLAUDE.md` restricción 6): agregar el verificador cambia cómo se trabaja la Práctica Independiente en aula y cuesta tiempo de clase, así que la decisión es suya, no una elección de diseño que Claude pueda tomar por su cuenta.
>
> Cuándo tiene sentido ofrecerlo: cuando la Práctica Independiente exige comprobar algo concreto (valores del borde, comparar dos programas, casos límite) y Diego no alcanza a pasar por cada puesto. Cuándo no: ejercicios de escritura libre donde no hay un resultado único contra el cual chequear.

En la intro de `### 4. Práctica Independiente`, un bloque `**Celda de configuración:**` + ` ```python ` se emite como celda de código justo después del texto introductorio de la sección. Es donde viven las funciones `verificar_*` / `comparar_*` que después llaman las celdas de verificación de cada ejercicio. Convención heredada de la Clase 17: primera línea `#@title 🔧 … (no la edites)`, que en Colab colapsa la celda a solo el título — importante, porque adentro suele estar la lógica correcta.

Sirve para que los estudiantes se autorrevisen sin esperar a que el profe pase por el puesto. Dos formas que ya están probadas:
- **Comparador**: recibe unos datos, corre internamente dos versiones de un programa y dice si se comportaron igual o distinto. Convierte "encuentra el caso que rompe este programa" en algo verificable sin que el estudiante tenga nada que escribir todavía.
- **Chequeo de bordes**: recibe lo que el programa del estudiante imprimió para ciertos valores y lo compara. Normaliza el texto (minúsculas, sin tildes) y matchea por subcadena, así un `Nivel: ¡Excelente semana!` calza con `Excelente semana` — sin eso, cualquier diferencia de puntuación da un falso ❌.

Como todavía no se enseñan funciones, el estudiante solo **llama** a estas funciones con datos; nunca las escribe ni las lee.

**Formato antiguo (retrocompatible, solo para regenerar clases anteriores a Clase 20):** narrativa + `Ejemplo:` inline + bloque de código de output, sin bullets "El programa debe" ni pistas. El generador detecta automáticamente cuál formato usa cada ejercicio (`el_programa_debe` presente o no) y no hace falta indicarlo.

**Solucionario (todas las soluciones)**
`Clase NN - Tema - Solucionario.ipynb` se genera automáticamente junto con `Clase.ipynb` (mismo comando, mismo gate de aprobación) siempre que haya algún contenido de solución en el spec. Contiene, en este orden: respuestas del Haz Ahora, solución de la Práctica Guiada, soluciones de Práctica Independiente, y las preguntas MCQ del Ticket de Salida (enunciado + 4 alternativas rotuladas A/B/C/D + la correcta marcada con ✅ + justificación). Es exclusivamente para el profesor: el Ticket se proyecta y responde a viva voz en clase; el resto Diego lo sube a Classroom recién **después** de dictar la clase. `generar-colab-ejercicios` actualiza este mismo archivo más adelante, agregando las soluciones de `Ejercicios.ipynb` — nunca crea un segundo solucionario.

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
- Lenguaje "tú"/"ustedes" en todo el texto — nunca "los estudiantes" ni "el profesor revela". **Nunca mencionar la modalidad de trabajo (pareja/individual) dentro del notebook** (ni en la intro de Independiente ni en las narrativas de los ejercicios) — desde 2026-08-04 Diego decide y anuncia la modalidad en vivo, en clase; el notebook no debe asumirla ni con "ustedes" referido a dos personas ni con "la pareja" como sujeto de la narrativa.

**Workflow**
- Solo preguntar a Diego en gates formales de aprobación (objetivo, estructura, Colab de clase, Colab de ejercicios, PPT).
- Correcciones técnicas intermedias: ejecutar sin preguntar.

**Notas internas del spec que nunca llegan al notebook**
`limpiar_notas_internas()` borra las líneas que empiezan con `Propósito:`, `Objetivo:` o `Nota de conducción:` — con o sin negrita, con o sin blockquote (`> `). `Actividad:` solo pierde la etiqueta. Se aplica al Haz Ahora, a la narrativa de la Guiada y a la intro de la Práctica Independiente. Usa `Nota de conducción:` en el spec para cualquier cosa dirigida a Diego que viva dentro de una sección que sí se renderiza (timers del PPT, a quién le toca qué ruta, qué conviene hacer notar al cerrar).

## Limitaciones conocidas

- El script asume que el spec sigue el formato estándar generado por la skill `disenar-clase`. Si Diego editó el spec manualmente y cambió encabezados o estructura, el parser puede fallar silenciosamente en alguna sección. En ese caso, valida el output y corrige.
- Si el spec tiene ejemplos de código con triple backtick anidados, el parser puede confundirse. Esto es raro pero conviene saberlo.
- El regex del cierre estructurado usa `(?=\n\*\*|\Z)` para no cortar en bold inline — no usar `(?=\*\*|\Z)` que cortaría en medio de una frase con negrita.
