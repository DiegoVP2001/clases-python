---
name: generar-ayudantia-ejercicios
description: Genera dos notebooks Jupyter desde una propuesta JSON aprobada de ayudantía — uno para estudiantes (subir a Colab) y uno de solucionario con rúbrica (subir a Classroom después). Usa esta skill cuando Diego apruebe una propuesta de ayudantía y pida generar o crear los notebooks.
---

# Skill: Generar notebooks de ayudantía

## Propósito

Materializar una propuesta JSON aprobada en dos notebooks Jupyter listos para usar, dentro de la carpeta numerada de la ayudantía en `clases/`:
- `Clase NN - Ayudantía Tema - Ejercicios.ipynb` → para los estudiantes, se sube a Google Colab
- `Clase NN - Ayudantía Tema - Solucionario.ipynb` → para el profesor, se sube a Classroom después de la sesión

**Cambio vigente desde 2026-07-28:** ya no se genera dentro de `ayudantias/`. La carpeta de salida es `clases/clase-NN-ayudantia-tema-breve/`, con el mismo patrón de nombrado de archivos que cualquier clase.

## Prerequisito

Debe existir `clases/clase-NN-ayudantia-tema-breve/Clase NN - Ayudantía Tema - Ejercicios propuesta.json` con la propuesta aprobada por Diego (creada por `disenar-ayudantia-ejercicios`, que ya fijó el N° real y el tema breve).

## Comando

Desde la raíz del proyecto (`clases-python-4tomedio/`):

```bash
python .claude/skills/generar-ayudantia-ejercicios/scripts/generar_ayudantia.py \
  "clases/clase-NN-ayudantia-tema-breve/Clase NN - Ayudantía Tema - Ejercicios propuesta.json" \
  --root clases \
  [--force]
```

El script deriva el nombre de la carpeta a partir de `class_number` + `set_slug`, y el prefijo de los archivos a partir de `class_number` + `class_topic` (ver schema abajo) — no hace falta pasarlos por separado. Usa el mismo `set_slug` que ya haya quedado en la carpeta pre-creada (ej. `ciclos` en `clase-21-ayudantia-ciclos`), no un slug distinto derivado del tema.

## Salida

```
clases/
└── clase-NN-ayudantia-tema-breve/
    ├── Clase NN - Ayudantía Tema - Ejercicios.ipynb   ← subir a Colab
    └── Clase NN - Ayudantía Tema - Solucionario.ipynb ← subir a Classroom
```

## Estructura del notebook de estudiantes

- Celda de encabezado (título, fecha, nombre, curso)
- Celda de objetivo (1-2 frases)
- Celda de instrucciones
- Sección "🔁 Ejercicio guiado — recordemos [tema]": enunciado + celda de código vacía (sin solución)
- Sección "🎯 Serie de ejercicios": por cada ejercicio (excepto `difficulty: trivial`):
  - Celda markdown: título + enunciado completo
  - Celda de código vacía: `# Tu código aquí`

## Estructura del solucionario

- Celda de encabezado con aviso de uso exclusivo del profesor
- Solución del ejercicio guiado (enunciado + celda de código con la solución de referencia)
- Por cada ejercicio de la serie:
  - Celda markdown: título + enunciado + criterios de corrección auto-generados + casos de prueba
  - Celda de código: solución oficial

## Opciones del script

| Flag | Descripción |
|---|---|
| `--root <ruta>` | Carpeta raíz de salida (default: `clases/`) |
| `--force` | Sobreescribir si ya existe la carpeta del set |

## Schema del JSON de propuesta

Los campos requeridos por el generador:

```json
{
  "class_number": "21",
  "class_topic": "Ejercitación Ciclos",
  "set_slug": "nombre-kebab-case",
  "set_title": "Título visible en el notebook",
  "objetivo": "1-2 frases con el objetivo de la sesión",
  "resumen_rapido_md": "OPCIONAL — resumen rápido en markdown de los conceptos de las clases foco, uno por uno (subtítulo + definición breve + bloque ```python``` de ejemplo), NUNCA como tabla HTML/side-by-side — un <table> con <pre> dentro de las celdas se ve mal en Jupyter/Colab (confirmado por Diego 2026-08-07). Se inserta como una sola celda entre el Objetivo y el ejercicio guiado. Solo inclúyelo si Diego lo pide explícitamente para esa ayudantía.",
  "guided_exercise": {
    "title": "Título del ejercicio guiado",
    "statement_md": "Enunciado completo en markdown (formato aprobado, más breve que los de la serie)",
    "solution_py": "código Python de la solución de referencia"
  },
  "verifier_setup_py": "OPCIONAL — código Python con las funciones verificar_ejercicio_N() de toda la serie, mismo patrón de la celda de configuración de generar-colab-clase (ver ejemplo en Clase 16/20). Se inserta como una sola celda de código antes del primer ejercicio.",
  "exercises": [
    {
      "slug": "nombre-ejercicio",
      "title": "Título del ejercicio",
      "difficulty": "trivial | base | media | media-alta | alta",
      "statement_md": "Enunciado completo en markdown (formato aprobado)",
      "tests": [
        {"name": "...", "stdin": "...", "stdout": "...", "hidden": false},
        {"name": "...", "stdin": "...", "stdout": "...", "hidden": true}
      ],
      "verifier_call": "OPCIONAL — línea que invoca el verificador de este ejercicio, ej. \"verificar_ejercicio_1()\". Requiere verifier_setup_py definido a nivel de propuesta.",
      "solution_py": "código Python de la solución"
    }
  ],
  "ticket_de_salida": {
    "tema_breve_form": "texto breve para el campo \"Tema de la clase de hoy\" del Google Form, mismo campo que usan las clases regulares",
    "preguntas": [
      {
        "enunciado": "Texto de la pregunta (sin alternativas)",
        "codigo": "OPCIONAL — bloque de código Python breve que ilustra o es el foco de la pregunta",
        "alternativas": [["A", "texto"], ["B", "texto"], ["C", "texto"], ["D", "texto"]],
        "correcta": "A",
        "justificacion": "1-2 frases explicando por qué es la correcta"
      }
    ]
  }
}
```

`class_number` + `set_slug` determinan la carpeta (`clase-{class_number}-ayudantia-{set_slug}`); `class_number` + `class_topic` determinan el prefijo de los archivos (`Clase {class_number} - Ayudantía {class_topic} - ...`). Los ejercicios de la serie con `difficulty: trivial` se omiten de ambos notebooks; el ejercicio guiado nunca se omite.

`verifier_setup_py` y `verifier_call` son opcionales y capacidad puntual (igual que en `generar-colab-clase`) — solo inclúyelos si Diego pidió explícitamente autochequeo ejecutable para esta ayudantía (ver regla correspondiente en `generar-colab-clase/SKILL.md` sobre no incluirlo por defecto). El notebook de estudiante inserta `verifier_setup_py` como una celda de código antes de "Serie de ejercicios", y `verifier_call` como una celda propia después de la celda de código vacía de cada ejercicio. El Solucionario no repite estas celdas — sigue usando `tests` para la rúbrica de casos visibles/ocultos.

`ticket_de_salida` es opcional y capacidad puntual — solo inclúyelo si Diego lo pide explícitamente para esa ayudantía (por defecto las ayudantías no tienen Ticket de Salida, a diferencia de las clases regulares). Siempre exactamente 4 preguntas (a diferencia de las 3 de una clase regular — la ayudantía consolida más de una clase foco). Nunca aparece en el notebook de estudiante: el generador solo lo agrega como sección `## 🎫 Ticket de Salida` al final del Solucionario, y escribe aparte `Clase {class_number} - Ayudantía {class_topic} - Ticket de Salida Respuestas.json` con el mismo formato que usan las clases regulares (`clase`, `tema`, `respuestas` con claves `"Respuestas a ticket [1]"`..`"[4]"`) para que la skill `trazabilidad-ticket-salida` lo cruce igual que cualquier clase. El PPT aparte (`... - Ticket de Salida.pptx`, mismo diseño que `crear_ppt_ticket.py` genera para las clases regulares) **no lo produce este script** — se arma aparte alimentando `crear_ppt_ticket.py` con los datos de `ticket_de_salida` (ver `generar-ppt-clase/SKILL.md`), porque ese generador ya sabe maquetar preguntas + alternativas + revisión con la plantilla de marca y no vale la pena duplicar esa lógica aquí.

## Después de generar

1. **Ejecuta ambos notebooks para verificar que el código corre sin errores**, antes de presentarlos a Diego:

   ```bash
   jupyter nbconvert --to notebook --execute --output <mismo-archivo> "Clase NN - Ayudantía Tema - Ejercicios.ipynb"
   jupyter nbconvert --to notebook --execute --output <mismo-archivo> "Clase NN - Ayudantía Tema - Solucionario.ipynb"
   ```

   Si alguna celda lanza una excepción o el output no calza con el esperado, corrige el JSON de la propuesta, regenera y vuelve a ejecutar — no entregues notebooks con errores sin detectar.

2. Confirma a Diego que ambos notebooks se crearon, se ejecutaron sin errores, y dónde están.
3. Recuérdale subir `Clase NN - Ayudantía Tema - Ejercicios.ipynb` a Google Colab y `Clase NN - Ayudantía Tema - Solucionario.ipynb` a Classroom (después de la sesión).
4. Crea o actualiza `Clase NN - Ayudantía Tema - Historial.md` (dentro de la carpeta de la ayudantía) con una entrada:

```markdown
## [fecha] — Set de ayudantía generado
- Clase: Clase NN - Ayudantía Tema
- Propuesta: Clase NN - Ayudantía Tema - Ejercicios propuesta.json
- Generado con la skill generar-ayudantia-ejercicios
- [notas de iteraciones o feedback si las hubo]
```

5. **Registra o actualiza la fila en `clases/Historial-Curricular.md`**: agrega/actualiza la fila correspondiente en la tabla principal (N° real, tema, carpeta, estado, fecha, OAs) — igual que cualquier clase. La tabla "Ayudantías realizadas" queda solo como registro histórico de los sets generados antes de 2026-07-28; no se agregan filas nuevas ahí.
6. Si Diego pide ajustes después, edita el JSON de la propuesta y regenera con `--force`; agrega una nueva entrada al `Historial.md` describiendo el cambio.
