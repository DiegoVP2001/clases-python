---
name: disenar-ayudantia-ejercicios
description: Diseña propuestas de ejercicios de práctica para ayudantías, organizados como Jupyter notebooks (uno para estudiantes, uno de solucionario). Usa esta skill cuando Diego pida preparar, proponer o diseñar ejercicios para una ayudantía, sesión de refuerzo o práctica autónoma. Produce una propuesta aprobable en chat y luego un JSON dentro de la carpeta de la ayudantía en clases/.
---

# Skill: Diseñar ejercicios para ayudantía

## Propósito

Proponer ejercicios de práctica organizados por clases foco. Esta skill solo diseña y espera aprobación; la generación de notebooks la hace `generar-ayudantia-ejercicios`.

## Cuándo usar el path Dodona en vez de este

Esta skill cubre el **path por defecto** del workflow de ayudantías: salida en Jupyter/Colab. Si Diego pide explícitamente que los ejercicios vayan a la plataforma Dodona ("súbelo a Dodona", "para Dodona", "que quede autocorregible en la plataforma"), no actives esta skill — activa `disenar-dodona-ejercicios` en su lugar. Ante cualquier duda, confirma con Diego cuál es el destino antes de proponer.

## Ubicación (desde 2026-07-28): la ayudantía es una clase numerada más

Las ayudantías ya no viven en `ayudantias/`. Se integran a `clases/` con numeración real, igual que cualquier clase — carpeta `clase-NN-ayudantia-tema-breve/`, archivos con el prefijo `Clase NN - Ayudantía Tema - [Tipo].ext`. El N° real se determina en el Paso 1, igual que para una clase normal.

## Flujo obligatorio

1. **Identificar clases foco y fijar el N° real.** Lee primero `clases/Historial-Curricular.md` — es la fuente de verdad de qué clases existen, en qué orden real se dictaron (puede no coincidir con la numeración Picuino), y cuál es el próximo N° real disponible. Si Diego no indicó las clases foco, pregunta usando esa lista como referencia. Acepta nombres de carpeta (`clase-07-input`), números reales o temas. Confirma con Diego el N° real y el tema breve que tendrá la ayudantía (ej. "Clase 21 - Ayudantía Ejercitación Ciclos") antes de seguir.
2. **Leer evidencia local.** Revisa `Spec.md`, `Ejercicios propuesta.md` y notebooks de esas clases. Consulta `referencia-curriculo` para verificar contenidos vistos. **Consulta `referencia-intereses-estudiantes` y `referencia-isla-de-maipo` antes de redactar enunciados** — los contextos deben ser significativos.
3. **Fijar alcance.** Pregunta solo lo esencial si falta: cantidad de ejercicios de la serie, propósito (`refuerzo`, `avance autónomo`, `evaluación corta`, `desafío`) y dificultad (`base`, `mixta`, `con desafíos`).
4. **Proponer en chat.** La propuesta siempre trae tres piezas, en este orden (ver "Estructura de la ayudantía" abajo):
   - Objetivo breve de la sesión.
   - Un ejercicio guiado de recordatorio (se resuelve en conjunto en clase).
   - La serie de ejercicios independientes, cada uno con el formato definido abajo.
5. **Esperar aprobación explícita.** No generes archivos hasta que Diego apruebe.
6. **Guardar JSON aprobado** en `clases/clase-NN-ayudantia-tema-breve/Clase NN - Ayudantía Tema - Ejercicios propuesta.json`. Ese JSON es la fuente de verdad; créalo antes de invocar el generador si la carpeta de la clase aún no existe.

   **Regla de naming del slug interno** (`set_slug` dentro del JSON, usado por el script): basa el slug en el **tema o las clases foco** del set (ej. `if-else-booleanos`, `loops-for-range`). **Nunca incluyas el día de la semana ni la fecha** (nada de `-jueves`, `-martes`, `-06-06`) — el slug debe seguir siendo válido sin importar cuándo se dicte la sesión, y la fecha ya queda registrada en el historial.
7. **Avisar** que el siguiente paso es activar `generar-ayudantia-ejercicios`.
8. **Confirmar registro en historial.** Después de que `generar-ayudantia-ejercicios` produzca los notebooks, verifica que haya quedado registrado en `Clase NN - Ayudantía Tema - Historial.md` (fecha + descripción del set generado y de cualquier feedback aplicado) **y** que se haya agregado o actualizado la fila correspondiente en la tabla principal de `clases/Historial-Curricular.md` (no en "Ayudantías realizadas" — esa tabla queda como registro histórico de los sets generados antes de 2026-07-28).

## Estructura de la ayudantía (fija, no preguntar)

1. **Objetivo** — 1-2 frases, qué se espera reforzar o consolidar en la sesión.
2. **Ejercicio guiado de recordatorio** — un único ejercicio que se resuelve en conjunto en clase para reactivar lo que se va a ejercitar. Mismo formato de enunciado que los de la serie, pero más breve. Sin solución visible en el notebook de estudiante (celda de código vacía) — la solución de referencia va solo en el Solucionario.
3. **Serie de ejercicios** — los ejercicios independientes propiamente tales, en el formato aprobado de abajo.

Nunca se genera PPT para una ayudantía.

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
## Propuesta ayudantía — Clase NN - Ayudantía [Tema]

Clases foco: [...]
Propósito: [...]
Conceptos cubiertos: [...]

### 🎯 Objetivo
[1-2 frases]

### 🔁 Ejercicio guiado — recordemos [tema]
- Enunciado:

  [narrativa + sección inputs + tabla output, más breve que los de la serie]

- Solución esperada: [código Python]

### Serie de ejercicios

#### Ejercicio N — [título]
- Clase foco: [...]
- Dificultad: trivial | base | media | media-alta | alta
- Objetivo: [...]
- Enunciado:

  [narrativa + sección inputs + tabla output]

- Casos visibles: [...]
- Casos ocultos: [...]
- Solución esperada: [código Python]
```
