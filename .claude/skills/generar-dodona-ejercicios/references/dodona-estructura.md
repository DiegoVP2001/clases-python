# Estructura Dodona usada por el workflow

## Configuracion

Cada ejercicio tiene `config.json`:

```json
{
  "description": {
    "names": {
      "es": "Titulo",
      "en": "Titulo"
    }
  },
  "evaluation": {
    "handler": "tested",
    "test_suite": "suite.yaml"
  },
  "programming_language": "python",
  "access": "private"
}
```

Cada carpeta organizadora puede tener `dirconfig.json` para defaults compartidos.

## Carpetas por ejercicio

```text
ejercicio/
  config.json
  description/
    description.es.md
    description.en.md
  evaluation/
    suite.yaml
  solution/
    solution.py
```

## Suites TESTed

Ejercicio de entrada/salida:

```yaml
- tab: "Casos"
  contexts:
    - testcases:
        - stdin: "10\n20\n"
          stdout: "Total: 30\n"
```

Ejercicio de funciones:

```yaml
- tab: "Casos"
  testcases:
    - expression: "doble(5)"
      return: 10
```

Reglas importantes:

- Un contexto con `stdin` representa una ejecucion independiente.
- `stdin` y argumentos solo se usan una vez por contexto.
- `stdout` no vacio debe terminar con salto de linea.
- Usar `function` cuando el contenido del curso ya permite `def` y `return`.
