---
name: disenar-ayudantia-ejercicios
description: Diseña propuestas de ejercicios de práctica para ayudantías, organizados como Jupyter notebooks (uno para estudiantes, uno de solucionario). Usa esta skill cuando Diego pida preparar, proponer o diseñar ejercicios para una ayudantía, sesión de refuerzo o práctica autónoma. Produce una propuesta aprobable en chat y luego un JSON en ayudantias/propuestas/.
---

# Skill: Diseñar ejercicios para ayudantía

## Propósito

Proponer ejercicios de práctica organizados por clases foco. Esta skill solo diseña y espera aprobación; la generación de notebooks la hace `generar-ayudantia-ejercicios`.

## Cuándo usar el path Dodona en vez de este

Esta skill cubre el **path por defecto** del workflow de ayudantías: salida en Jupyter/Colab. Si Diego pide explícitamente que los ejercicios vayan a la plataforma Dodona ("súbelo a Dodona", "para Dodona", "que quede autocorregible en la plataforma"), no actives esta skill — activa `disenar-dodona-ejercicios` en su lugar. Ante cualquier duda, confirma con Diego cuál es el destino antes de proponer.

## Flujo obligatorio

1. **Identificar clases foco.** Si Diego no las indicó, pregunta. Acepta nombres de carpeta (`clase-07-input`), números Picuino o temas.
2. **Leer evidencia local.** Revisa `Spec.md`, `Ejercicios propuesta.md` y notebooks de esas clases. Consulta `referencia-curriculo` para verificar contenidos vistos. **Consulta `referencia-intereses-estudiantes` y `referencia-isla-de-maipo` antes de redactar enunciados** — los contextos deben ser significativos.
3. **Fijar alcance.** Pregunta solo lo esencial si falta: cantidad de ejercicios, propósito (`refuerzo`, `avance autónomo`, `evaluación corta`, `desafío`) y dificultad (`base`, `mixta`, `con desafíos`).
4. **Proponer en chat.** Presenta cada ejercicio con el formato definido abajo.
5. **Esperar aprobación explícita.** No generes archivos hasta que Diego apruebe.
6. **Guardar JSON aprobado** en `ayudantias/propuestas/<slug>.json`. Ese JSON es la fuente de verdad.
7. **Avisar** que el siguiente paso es activar `generar-ayudantia-ejercicios`.
8. **Confirmar registro en historial.** Después de que `generar-ayudantia-ejercicios` produzca los notebooks, verifica que haya quedado registrado en `ayudantias/<slug>/historial.md` (fecha + descripción del set generado y de cualquier feedback aplicado).

## Criterios pedagógicos

- No copies literalmente ejercicios de Colab; cambia contexto o datos.
- Usa solo conceptos vistos hasta la clase foco más avanzada.
- Español de Chile, variables `snake_case`, contextos cercanos al curso.
- Ejercicios pequeños y autocontenidos: un objetivo claro por ejercicio.
- Para clases 1-18, prefiere tipo `io` (entrada/salida por consola).
- Incluye al menos un caso visible y uno oculto para el solucionario.
- Marca los casos ocultos con `"hidden": true` en el JSON.

## Formato de enunciado aprobado

```
[Narrativa de 3-4 líneas: situación concreta, contexto real, casos borde explicados en lenguaje natural. Sin mencionar operadores ni nombres de variables.]

Tu programa pedirá con `input()` N datos en este orden:

1. [Descripción del dato].
   Respuestas posibles: `si` o `no` / cualquier número entero (ejemplo: `440`).

Según lo que respondió el usuario, tu programa debe imprimir:

| Situación | Lo que imprime tu programa |
|---|---|
| [descripción natural] | `[texto exacto]` |
| [descripción natural] | `[texto exacto]` |

No escribas texto dentro del `input()`, o sea déjalo vacío.
```

**Reglas del enunciado:**
- No mencionar operadores (`and`, `or`, `if`, etc.) ni nombres de variables.
- No incluir bloque `**Ejemplo:**` inline — los casos van en el campo `sample` del JSON.
- La tabla de output no debe incluir comparadores numéricos (≤ 450, > 0); la narrativa los explica.
- Ejercicios triviales de introducción: formato más liviano, sin tabla.

## Formato de propuesta en chat

```markdown
## Propuesta ayudantía — [nombre del set]

Clases foco: [...]
Propósito: [...]
Conceptos cubiertos: [...]

### Ejercicio N — [título]
- Clase foco: [...]
- Dificultad: trivial | base | media | media-alta | alta
- Objetivo: [...]
- Enunciado:

  [narrativa + sección inputs + tabla output]

- Casos visibles: [...]
- Casos ocultos: [...]
- Solución esperada: [código Python]
```
