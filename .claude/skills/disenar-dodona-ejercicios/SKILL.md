---
name: disenar-dodona-ejercicios
description: Diseña propuestas de ejercicios autocorregibles para Dodona a partir de clases foco del curso Python. Usa esta skill cuando Diego pida subir, preparar, proponer, diseñar o planificar ejercicios para Dodona, ayudantías, práctica autónoma o avance individual en plataforma, antes de generar carpetas o archivos Dodona.
---

# Skill: Diseñar ejercicios para Dodona

## Propósito

Proponer ejercicios autocorregibles para Dodona usando clases ya diseñadas como fuente pedagógica. Esta skill solo diseña y pide aprobación; no crea carpetas Dodona finales.

## Flujo obligatorio

1. **Identificar clases foco.** Pregunta cuáles clases quiere usar Diego como foco si no lo dijo. Acepta nombres de carpeta (`clase-07-input`), números Picuino o temas.
2. **Leer evidencia local.** Revisa los `Spec.md`, `Ejercicios propuesta.md`, `Ejercicios.ipynb` o notebooks disponibles de esas clases. Consulta `referencia-curriculo` para verificar contenidos vistos. **Consulta también `referencia-intereses-estudiantes` y `referencia-isla-de-maipo` antes de redactar los enunciados** — los contextos deben ser significativos para los estudiantes.
3. **Fijar alcance.** Si falta información, pregunta solo lo esencial: cantidad de ejercicios por clase, propósito (`refuerzo`, `avance autonomo`, `evaluacion corta`, `desafio`) y dificultad (`base`, `mixta`, `con desafios`).
4. **Proponer en chat.** Presenta cada ejercicio con el formato de propuesta definido más abajo. No incluyas un bloque de preview tipo "Vista en Dodona" — el enunciado, los casos y la solución bastan para que Diego apruebe.
5. **Esperar aprobación explícita.** No generes archivos finales ni llames a `generar-dodona-ejercicios` hasta que Diego apruebe.
6. **Guardar contrato aprobado.** Cuando apruebe, crea un JSON en `dodona/propuestas/` siguiendo `references/propuesta-schema.md`. Ese JSON será la fuente de verdad para la generación.
7. **Usar repo externo para salida.** Los ejercicios generados deben escribirse en `dodona-ejercicios-profesor/`, que apunta a `https://github.com/DiegoVP2001/dodona-ejercicios-profesor.git`.

## Criterios pedagógicos

- No copies literalmente ejercicios de Colab; conserva contenido y nivel, pero cambia contexto o datos.
- Usa solo conceptos vistos hasta la clase foco más avanzada.
- Mantén español de Chile, variables `snake_case` y contextos cercanos al curso.
- Prioriza ejercicios pequeños y autocontenidos: Dodona corrige una tarea por ejercicio.
- Para clases 1-18, prefiere tipo `io` con `stdin`/`stdout`.
- Desde funciones en adelante, prefiere tipo `function` con `expression`/`return`.
- Evita que la corrección dependa de prompts largos de `input()`. Recomienda no usar prompt en `input()` o ignorar el prompt en los criterios visibles.
- Incluye siempre al menos un caso visible y uno oculto cuando el ejercicio lo justifique.
- En el JSON aprobado, marca los casos ocultos con `"hidden": true`; el generador los separa en un tab oculto de TESTed.
- El piloto `piloto-ayudantia-input-booleanos-if` ya fue generado, pusheado y visto en Dodona; puede usarse como referencia de nivel y formato.
- **`statement_md` no debe incluir el bloque `**Ejemplo:**` inline.** El ejemplo va en el campo `sample`; Dodona lo renderiza nativamente en la plataforma. El generador tampoco lo incluye en el `.md`.
- **Los enunciados deben tener mínimo 3-4 líneas** con una situación concreta y contexto real. Evita enunciados de una sola línea genérica. Describe el escenario, el personaje o la situación antes de explicar qué debe hacer el programa.

## Formato de propuesta en chat

```markdown
## Propuesta Dodona - [nombre del set]

Clases foco: [...]
Propósito: [...]
Conceptos permitidos: [...]

### Ejercicio N - [titulo]
- Clase foco: [...]
- Tipo: io | function
- Objetivo: [...]
- Enunciado visible:

  [3-4 líneas mínimo con situación concreta. Sin bloque Ejemplo inline.]

- Casos visibles: [...]
- Casos ocultos: [...]
- Solución esperada: [código Python]
```

## Recursos

- Lee `references/propuesta-schema.md` antes de guardar el JSON aprobado.
- Después de guardar el JSON aprobado, indica a Diego que el siguiente paso es activar `generar-dodona-ejercicios` con salida en `dodona-ejercicios-profesor/`.
