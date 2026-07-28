# Esquema de propuesta Dodona aprobada

Guardar propuestas aprobadas como JSON UTF-8 en `dodona/propuestas/<slug>.json`.
La salida generada debe escribirse en el repo externo `dodona-ejercicios-profesor/`.

## Estructura

```json
{
  "set_slug": "ayudantia-input-booleanos",
  "set_title": "Ayudantia - input y booleanos",
  "source_classes": [
    "clases/clase-07-input",
    "clases/clase-08a-booleano-comparaciones"
  ],
  "purpose": "refuerzo",
  "exercises": [
    {
      "slug": "distancia-estadio",
      "title": "Distancia al estadio",
      "focus_class": "clase-07-input",
      "type": "io",
      "difficulty": "base",
      "topics": ["input", "int", "print"],
      "statement_md": "Escribe un programa que lea...",
      "sample": {
        "stdin": "Valparaiso\n120\n",
        "stdout": "Desde Valparaiso el estadio queda a 120 km.\n"
      },
      "tests": [
        {
          "name": "caso visible",
          "stdin": "Valparaiso\n120\n",
          "stdout": "Desde Valparaiso el estadio queda a 120 km.\n"
        },
        {
          "name": "caso oculto",
          "stdin": "Santiago\n15\n",
          "stdout": "Desde Santiago el estadio queda a 15 km.\n",
          "hidden": true
        }
      ],
      "solution_py": "ciudad = input()\ndistancia_km = int(input())\nprint(\"Desde\", ciudad, \"el estadio queda a\", distancia_km, \"km.\")\n"
    }
  ]
}
```

## Tipos de ejercicios

- `io`: programa completo que lee desde `stdin` y escribe a `stdout`. Cada test debe tener `stdin` y `stdout`.
- `function`: el estudiante define una función. Cada test debe tener `expression` y `return`; puede incluir `stdout` si el objetivo lo requiere.

## Reglas

- `slug` debe estar en kebab-case ASCII.
- `statement_md` no debe incluir la solución.
- `solution_py` debe ser código Python ejecutable.
- `stdout` no vacío debe terminar con salto de línea.
- Para `io`, usa inputs sin prompts para reducir fragilidad.
- Marca los casos ocultos con `"hidden": true`; el generador los ubica en un tab oculto de TESTed.
