---
name: generar-colab-clase
description: Genera el Jupyter notebook principal de una clase (01-clase.ipynb) a partir de un 00-spec.md aprobado. Usa esta skill solo después de que la skill disenar-clase haya producido y Diego haya aprobado el spec. Produce un .ipynb listo para subir a Google Colab con la estructura estándar de 5 pasos (Haz Ahora, ICN, Práctica Guiada, Práctica Independiente, Ticket).
---

# Skill: Generar Colab de clase (01-clase.ipynb)

## Propósito

Transformar un `00-spec.md` aprobado en un Jupyter notebook (`.ipynb`) listo para subir a Google Colab. El notebook generado tiene la estructura estándar de las clases de Python 4to medio y es consistente entre todas las clases del programa.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Genera el Colab de clase"
- "Procede al notebook"
- "Vamos al .ipynb"
- "Ya aprobé el spec, sigamos"

**Requisito previo obligatorio:** debe existir un archivo `00-spec.md` aprobado en la carpeta `clases/clase-NN-tema/`. Si no existe, NO procedas: indica a Diego que primero debe diseñar la clase con la skill `disenar-clase`.

## Verificaciones antes de generar

Antes de ejecutar el script, valida:

1. **Existe el spec.** Confirma que `clases/clase-NN-tema/00-spec.md` está presente.
2. **El spec está aprobado.** El estado en el archivo debe decir "Spec aprobada".
3. **Python y nbformat disponibles.** Verifica con `python --version` y `python -c "import nbformat"`. Si falla nbformat, ejecuta `pip install nbformat` (en Windows con Python del sistema, normalmente funciona sin más; en sistemas con `pip` restringido puede necesitarse `pip install --user nbformat`).
4. **No existe ya un `01-clase.ipynb` con cambios manuales.** Si existe, pregunta a Diego si quiere sobrescribir.

## Cómo se ejecuta

La generación se hace con el script Python `crear_colab.py` que vive en esta misma carpeta de skill. El script:

1. Lee el `00-spec.md` y parsea sus secciones.
2. Construye un objeto notebook con `nbformat`.
3. Lo escribe como `.ipynb` en la ruta indicada.

Comando estándar de ejecución (desde la raíz del proyecto):

```bash
python .claude/skills/generar-colab-clase/crear_colab.py clases/clase-NN-tema/00-spec.md clases/clase-NN-tema/01-clase.ipynb
```

**Importante en Windows:** las rutas pueden necesitar comillas si tienen espacios. Si Diego está en una ruta como `G:\Mi unidad\...`, ejecuta desde PowerShell con comillas:

```powershell
python ".claude/skills/generar-colab-clase/crear_colab.py" "clases/clase-NN-tema/00-spec.md" "clases/clase-NN-tema/01-clase.ipynb"
```

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
4. Cuando Diego apruebe, registra en `historial.md`:

```markdown
## [fecha] — Colab de clase aprobado
- Archivo: 01-clase.ipynb
- Generado con la skill generar-colab-clase
- [notas de iteraciones si las hubo]
```

## Iteración sobre el .ipynb

Si Diego pide cambios:

- **Cambios cosméticos** (corregir typo, ajustar emoji, mejorar redacción puntual): edita directamente el `.ipynb` con la herramienta de edición.
- **Cambios estructurales** (modificar un ejercicio, cambiar el ticket): primero **actualiza el `00-spec.md`**, luego regenera el `.ipynb` con el script. NUNCA edites el spec y el notebook como dos cosas separadas: el spec es la fuente de verdad.
- **Cambios sistémicos** (algo que debería aplicar a todas las clases futuras, ej: "los Haz Ahora deben tener 2 celdas de código en vez de 1"): edita el script `crear_colab.py` y avísale a Diego que el cambio aplicará a todas las clases que regeneres a partir de ahora.

## Reglas críticas

1. **El spec es la fuente de verdad.** Si hay discrepancia entre spec y notebook, gana el spec. Regenera el notebook.
2. **Nunca cargues ejemplos de código fuera del spec.** Si el spec define 3 ejercicios, el notebook tiene 3 ejercicios. No agregues por iniciativa propia.
3. **Soluciones siempre ocultas con `<details>`.** Nunca pongas la solución de un ejercicio visible antes de que el estudiante intente.
4. **Si el script falla en parsear alguna sección**, NO inventes contenido. Avisa a Diego que esa sección quedó vacía y pregunta cómo proceder (la causa típica es que el spec no sigue el formato esperado).

## Principios de diseño del notebook (establecidos en clase 8a)

Verificar que el spec cumpla estos principios antes de generar. Si no los cumple, corregir el spec sin preguntar.

**Haz Ahora**
- Incluir siempre una celda markdown debajo del enunciado para que los estudiantes escriban sus respuestas (numerada según las situaciones).
- Puede tener celda de código si es pertinente (para activar conocimiento previo con código).
- NO revelar operadores, funciones ni sintaxis de hoy — ni en los enunciados ni en columnas de tabla.

**Enunciados**
- Ejemplos de input en lenguaje natural: "si alguien ingresa un saldo de $80.000" — nunca `saldo_cuenta_rut = 80000`.
- Enunciados de Independiente sin comandos (`input()`, operadores, nombres de variables) en el markdown — solo descripción de qué calcular.
- Pasos de Guiada en lenguaje natural de alto nivel: "Crea una variable que registre el saldo" — sin revelar nombre exacto ni operador.

**Outputs**
- Los `print()` de ejercicios y soluciones siempre llevan texto descriptivo: `print("¿Te alcanza?", saldo >= precio)`.
- El resultado esperado muestra el output con etiqueta, no solo `True` o `False`.

**Estructura**
- Todas las soluciones (Guiada + ejercicios + ticket) van al final en sección "📋 Soluciones" con `<details>` individuales — nunca inline.
- Sin tiempos `(N min)` en los títulos de sección del notebook.
- Lenguaje "tú" en todo el texto — nunca "los estudiantes" ni "el profesor revela".

**Workflow**
- Solo preguntar a Diego en gates formales de aprobación (objetivo, estructura, Colab de clase, Colab de ejercicios, PPT).
- Correcciones técnicas intermedias: ejecutar sin preguntar.

## Limitaciones conocidas

- El script asume que el spec sigue el formato estándar generado por la skill `disenar-clase`. Si Diego editó el spec manualmente y cambió encabezados o estructura, el parser puede fallar silenciosamente en alguna sección. En ese caso, valida el output y corrige.
- Si el spec tiene ejemplos de código con triple backtick anidados, el parser puede confundirse. Esto es raro en clases de 4to medio pero conviene saberlo.
