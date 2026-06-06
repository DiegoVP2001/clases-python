---
name: generar-ayudantia-ejercicios
description: Genera dos notebooks Jupyter desde una propuesta JSON aprobada de ayudantía — uno para estudiantes (subir a Colab) y uno de solucionario con rúbrica (subir a Classroom después). Usa esta skill cuando Diego apruebe una propuesta de ayudantía y pida generar o crear los notebooks.
---

# Skill: Generar notebooks de ayudantía

## Propósito

Materializar una propuesta JSON aprobada en dos notebooks Jupyter listos para usar:
- `<slug>-ejercicios.ipynb` → para los estudiantes, se sube a Google Colab
- `<slug>-solucionario.ipynb` → para el profesor, se sube a Classroom después de la sesión

## Prerequisito

Debe existir `ayudantias/propuestas/<slug>.json` con la propuesta aprobada por Diego.

## Comando

Desde la raíz del proyecto (`clases-python-4tomedio/`):

```bash
python .claude/skills/generar-ayudantia-ejercicios/scripts/generar_ayudantia.py \
  ayudantias/propuestas/<slug>.json \
  --root ayudantias \
  [--force]
```

## Salida

```
ayudantias/
└── <slug>/
    ├── <slug>-ejercicios.ipynb   ← subir a Colab
    └── <slug>-solucionario.ipynb ← subir a Classroom
```

## Estructura del notebook de estudiantes

- Celda de encabezado (título, fecha, nombre, curso)
- Celda de instrucciones
- Por cada ejercicio (excepto `difficulty: trivial`):
  - Celda markdown: título + enunciado completo
  - Celda de código vacía: `# Tu código aquí`

## Estructura del solucionario

- Celda de encabezado con aviso de uso exclusivo del profesor
- Por cada ejercicio:
  - Celda markdown: título + enunciado + criterios de corrección auto-generados + casos de prueba
  - Celda de código: solución oficial

## Opciones del script

| Flag | Descripción |
|---|---|
| `--root <ruta>` | Carpeta raíz de salida (default: `ayudantias/`) |
| `--force` | Sobreescribir si ya existe la carpeta del set |

## Schema del JSON de propuesta

Los campos requeridos por el generador:

```json
{
  "set_slug": "nombre-kebab-case",
  "set_title": "Título visible en el notebook",
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
      "solution_py": "código Python de la solución"
    }
  ]
}
```

Los ejercicios con `difficulty: trivial` se omiten de ambos notebooks (son ejercicios de demo/introducción que no aplican para la ayudantía en Jupyter).
