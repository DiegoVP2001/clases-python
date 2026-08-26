# 📋 Temario — Evaluación Individual: Condicionales

**Fecha:** martes 21 de julio, 2026
**Modalidad:** individual
**OAs:** OA1, OA3 | OAd
**Clases que cubre:** 8a, 8b, 8c, 11 (if/else real), 13, 14, 17

## Conocimiento previo (no se evalúa directamente, pero se usa en los ejercicios)
- Tipos de datos: `bool`, `int`, `float`, `str`
- Captura de datos con `input()`, convertido con `int()` o `float()` según corresponda

## Bloque 1 — Booleanos y comparaciones (Clase 8a)
- El tipo `bool`: `True` / `False` como valores de dato
- Operadores de comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Las comparaciones funcionan tanto con números como con texto (ej: `dia == "sabado"`)
- La función `bool()` para convertir números a booleano
- Error típico: usar `=` en vez de `==` para comparar

## Bloque 2 — Operadores lógicos (Clase 8b)
- `and`: verdadero solo si **ambas** condiciones son verdaderas
- `or`: verdadero si **al menos una** condición es verdadera
- `not`: invierte el valor booleano
- Combinar operadores con paréntesis, en distintos órdenes: `var and (var2 or var3)`, `(var and var2) or var3`, `not (var) and (var2 and var3)`
- Errores típicos: confundir `and`/`or`, mayúsculas, alcance de `not` sin paréntesis

## Bloque 3 — Análisis de condiciones (Clase 8c)
- "Funciona con mis datos de prueba" ≠ "funciona siempre"
- El **caso límite**: el valor exacto donde `>`/`>=` (o `<`/`<=`) dan resultados distintos
- Identificar y corregir el operador incorrecto en una condición dada

## Bloque 4 — if / else (Clase 11 real)
- Sintaxis de `if` y cláusula `else`
- La indentación como sintaxis obligatoria
- Errores típicos: falta de `:`, falta de indentación, `else` sin `if`

## Bloque 5 — if anidados (Clase 13)
- Un `if` dentro de otro `if`; la condición interior solo se evalúa si la exterior fue `True`
- `else` en cada nivel de anidamiento
- La sangría como jerarquía
- Criterio: ¿cuándo anidar vs. cuándo basta con `and`?

## Bloque 6 — elif (Clase 14)
- Sintaxis de `elif`: condiciones alternativas mutuamente excluyentes
- Solo se ejecuta **una** rama — la primera que resulte `True`
- El orden de las condiciones importa (de más específica a más general)
- Errores típicos: condición demasiado amplia primero, `elif` después de `else`, olvidar el `else` final

## Bloque 7 — Criterio de selección (Clase 17, ejercitación)
- Reconocer cuál estructura usar: `if/else` simple, anidados, `elif`, o combinaciones
- Combinar estructuras (ej: `elif` con un `if/else` anidado dentro de una rama)

## Formato sugerido de la evaluación
- Predicción de output (dado un código, ¿qué imprime?)
- Identificación y corrección de errores (sintaxis, indentación, operador incorrecto)
- Escritura de un programa completo desde un enunciado

---

## Notas de revisión (2026-07-13)

- Se revisó también el diagnóstico de medio semestre (`clases/compu/evaluacion_medio_semestre.md`, banco Enseña Chile, clases 7–14) para contrastar cobertura.
- Se descartó incluir el contraste "`if` independientes en cadena vs. cadena `elif`" (probado en la pregunta 18 de ese diagnóstico) porque no se practicó a profundidad en clase.
- Se amplió el Bloque 2 con más variantes de combinación de paréntesis (`and`/`or`/`not`) y se agregó la comparación de strings al Bloque 1, ambas confirmadas por ese mismo diagnóstico.
- 2026-07-13: generado el PDF de estudio para estudiantes a partir de este temario (`Clase 17.5 - Evaluación Condicionales - Temario de Evaluación.pdf`, vía `generar_guia_estudio.py`), sin "Clases que cubre" ni referencias a clases Picuino en los subtítulos, y sin la sección de formato de evaluación. Listo para compartir y subir a Classroom.
- 2026-07-13: generado además `clases/Clase-17-apoyo-individual/Clase-17-apoyo-individual.ipynb`, un Colab de repaso exprés de los mismos 7 bloques (teoría condensada + ejemplo resuelto + ejercicio con valores de prueba concretos por bloque + desafío final + soluciones plegables al fondo), pensado para que un estudiante puntual se ponga al día rápido antes de la evaluación. El notebook es genérico — no nombra a ningún estudiante ni su situación — para poder subirlo sin problema al repo público.
