# Prompt — Sesión 1: Kahoot diagnóstico post-vacaciones

## Contexto para Claude

Genera las preguntas para un Kahoot diagnóstico de 12 preguntas para estudiantes de 4to medio que acaban de volver de ~3,5 semanas de vacaciones.

El objetivo **no** es evaluar: es activar la memoria y ver rápidamente qué recuerdan. Tono liviano, sin consecuencias de nota.

## Contenidos a cubrir (toda la materia vista)

1. Variables y tipos de datos (`int`, `float`, `str`, `bool`)
2. `print()` e `input()`
3. Comparaciones: `==`, `!=`, `<`, `>`, `<=`, `>=`
4. Operadores lógicos: `and`, `or`, `not`
5. `if / else` — estructura, indentación, predicción de output

## Distribución de preguntas (12 en total)

| Bloque | N° preguntas | Tipos de pregunta |
|---|---|---|
| Variables y tipos | 3 | ¿Qué tipo es `"hola"`? / ¿Qué guarda `x = 10 + 5`? / ¿Qué imprime este `print()`? |
| Booleanos y comparaciones | 3 | `5 > 3` → ¿True o False? / `10 == "10"` → ? / ¿qué operador falta para que dé True? |
| Operadores lógicos | 2 | `True and False` → ? / `True or False` → ? |
| if / else | 4 | Predicción de output / detectar bug de indentación / ¿qué rama se ejecuta? / completar el `else` |

## Formato de salida

Entregar las 12 preguntas en texto con esta estructura por pregunta:

```
**Pregunta N:** [enunciado o bloque de código]
A) ...
B) ...
C) ...
D) ...
✅ Respuesta correcta: [letra]
⏱ Tiempo sugerido: [15 o 20 segundos]
```

Luego, generar también el Excel importable a Kahoot con estas columnas exactas:
`Question`, `Answer 1`, `Answer 2`, `Answer 3`, `Answer 4`, `Time Limit (sec)`, `Correct Answer`

## Restricciones

- No usar `elif`, funciones, listas, ciclos ni ningún contenido no visto.
- Variables con nombres en español snake_case (`puntos`, `saldo`, `edad`, `nombre`).
- Contextos cotidianos chilenos (precios en CLP, situaciones reales para el estudiante).
- Tiempo por pregunta: 20 seg para predicción de código, 15 seg para preguntas conceptuales.
- 4 alternativas siempre. Opciones incorrectas plausibles (no distractores absurdos).
