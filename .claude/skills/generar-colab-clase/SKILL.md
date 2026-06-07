---
name: generar-colab-clase
description: Genera el Jupyter notebook principal de una clase (Clase NN - Tema - Clase.ipynb) a partir de un Clase NN - Tema - Spec.md aprobado. Usa esta skill solo después de que la skill disenar-clase haya producido y Diego haya aprobado el spec. Produce un .ipynb listo para subir a Google Colab con la estructura estándar de 5 pasos (Haz Ahora, ICN, Práctica Guiada, Práctica Independiente, Ticket).
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
| 1 | Markdown | Objetivo, propósito, contenidos previos/nuevos |
| 2 | Markdown | Sección "1️⃣ Haz Ahora" con la actividad |
| 3 | Code | Espacio en blanco para notas del estudiante |
| 4 | Markdown | Sección "2️⃣ ICN" con conceptos numerados |
| 5+ | Code | Ejemplos ejecutables del ICN (uno o varios) |
| n | Markdown | Tabla de errores típicos |
| n+1 | Markdown | Sección "3️⃣ Práctica Guiada" con situación y pasos |
| n+2 | Code | Espacio en blanco para construir el código |
| n+3 | Markdown | Solución oculta con `<details>` |
| n+4 | Markdown | Sección "4️⃣ Práctica Independiente" |
| ... | MD+Code alternados | Cada ejercicio con su enunciado y celda vacía |
| ... | Markdown | Sección "5️⃣ Ticket de Salida" |
| ... | Code | Espacio vacío para la respuesta del ticket |
| último | Markdown | Cierre y preguntas de reflexión |

## Después de generar

1. Confirma a Diego que el archivo se creó y dónde está.
2. **Recomienda subirlo a Google Colab** para revisarlo en el entorno real antes de aprobar:
   - Abrir https://colab.research.google.com
   - `Archivo` → `Subir cuaderno`
   - Seleccionar el `.ipynb` recién generado
3. **Espera el feedback de Diego antes de avanzar al Colab de ejercicios.**
4. Cuando Diego apruebe, registra en `Clase NN - Tema - Historial.md`:

```markdown
## [fecha] — Colab de clase aprobado
- Archivo: Clase NN - Tema - Clase.ipynb
- Generado con la skill generar-colab-clase
- [notas de iteraciones si las hubo]
```

5. Después de registrar, di: *"Antes de continuar al Colab de ejercicios, ejecuta `/compact` para limpiar el contexto. Avísame cuando estés listo."* Cuando Diego confirme, activa la skill `generar-colab-ejercicios`.

## Iteración sobre el .ipynb

Si Diego pide cambios:

- **Cambios cosméticos** (corregir typo, ajustar emoji, mejorar redacción puntual): edita directamente el `.ipynb` con la herramienta de edición.
- **Cambios estructurales** (modificar un ejercicio, cambiar el ticket): primero **actualiza el `Clase NN - Tema - Spec.md`**, luego regenera el `.ipynb` con el script. NUNCA edites el spec y el notebook como dos cosas separadas: el spec es la fuente de verdad.
- **Cambios sistémicos** (algo que debería aplicar a todas las clases futuras, ej: "los Haz Ahora deben tener 2 celdas de código en vez de 1"): edita el script `crear_colab.py` y avísale a Diego que el cambio aplicará a todas las clases que regeneres a partir de ahora.

## Reglas críticas

1. **El spec es la fuente de verdad.** Si hay discrepancia entre spec y notebook, gana el spec. Regenera el notebook.
2. **Nunca cargues ejemplos de código fuera del spec.** Si el spec define 3 ejercicios, el notebook tiene 3 ejercicios. No agregues por iniciativa propia.
3. **Soluciones siempre ocultas con `<details>`.** Nunca pongas la solución de un ejercicio visible antes de que el estudiante intente.
4. **Si el script falla en parsear alguna sección**, NO inventes contenido. Avisa a Diego que esa sección quedó vacía y pregunta cómo proceder (la causa típica es que el spec no sigue el formato esperado).

## Principios de diseño del notebook

Verificar que el spec cumpla estos principios antes de generar. Si no los cumple, corregir el spec sin preguntar.

**Encabezado y metadatos**
- Curso por defecto: `"3ro y 4to medio"` (no solo "4to medio").

**Haz Ahora**
- Incluir celda markdown de respuestas con slots numerados según los ítems del Haz Ahora (conteo dinámico — no hardcodear 6).
- Las respuestas esperadas del Haz Ahora van SOLO en la sección "📋 Soluciones" dentro de un `<details>` — nunca en el cuerpo del notebook ni como nota o pie de página al final de la sección Haz Ahora.
- En el spec, marcar las respuestas con `**Respuestas esperadas:** ...` al final de la sección — el parser las extrae automáticamente.
- NO revelar operadores, funciones ni sintaxis de hoy — ni en los enunciados ni en columnas de tabla.

**Propósito**
- El encabezado de la sección es `## 💡 Propósito` — nunca `¿Para qué te sirve?`.
- El propósito va en blockquote `>` y debe ser breve, orientado a la habilidad o actitud de la clase.

**Enunciados**
- Ejemplos de input en lenguaje natural: "si alguien ingresa un saldo de $80.000" — nunca `saldo_cuenta_rut = 80000`.
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

**Ejemplos en ejercicios independientes y ticket**
- Los ejemplos de ejecución van en blockquote `>` separados del enunciado con `---`.
- Formato: `> *Ejemplo: si alguien...*` + `>` + `> ` ``` + output + ` ``` `.
- Esta convención aplica tanto a los ejercicios de Práctica Independiente como al Ticket de Salida.

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
- Todas las soluciones (Haz Ahora + Guiada + ejercicios + ticket) van al final en sección "📋 Soluciones" con `<details>` individuales — nunca inline.
- Sin tiempos `(N min)` en los títulos de sección del notebook.
- Lenguaje "tú" en todo el texto — nunca "los estudiantes" ni "el profesor revela".

**Workflow**
- Solo preguntar a Diego en gates formales de aprobación (objetivo, estructura, Colab de clase, Colab de ejercicios, PPT).
- Correcciones técnicas intermedias: ejecutar sin preguntar.

## Limitaciones conocidas

- El script asume que el spec sigue el formato estándar generado por la skill `disenar-clase`. Si Diego editó el spec manualmente y cambió encabezados o estructura, el parser puede fallar silenciosamente en alguna sección. En ese caso, valida el output y corrige.
- Si el spec tiene ejemplos de código con triple backtick anidados, el parser puede confundirse. Esto es raro pero conviene saberlo.
- El regex del cierre estructurado usa `(?=\n\*\*|\Z)` para no cortar en bold inline — no usar `(?=\*\*|\Z)` que cortaría en medio de una frase con negrita.
