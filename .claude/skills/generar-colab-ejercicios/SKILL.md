---
name: generar-colab-ejercicios
description: Genera el Jupyter notebook de ejercicios adicionales (Clase NN - Tema - Ejercicios.ipynb) de una clase. Usa esta skill después de que el Colab principal (Clase NN - Tema - Clase.ipynb) esté aprobado. Sigue un flujo de dos fases: primero propone los ejercicios en chat para aprobación, luego genera el .ipynb final sin ninguna solución (ni siquiera oculta) y agrega las soluciones al Solucionario.ipynb existente. Los ejercicios usan solo conceptos vistos hasta la clase actual.
---

# Skill: Generar Colab de ejercicios (Clase NN - Tema - Ejercicios.ipynb)

## Propósito

Producir un notebook de ejercicios adicionales para que los estudiantes practiquen el contenido de la clase y de clases anteriores. Estos ejercicios complementan los del Colab principal: van pensados para estudiantes que terminan rápido, para tarea, o para refuerzo. Ninguno trae solución en el notebook de estudiante — todas van al `Solucionario.ipynb` de la clase.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Genera los ejercicios"
- "Vamos al Colab de ejercicios"
- "Procede al 02-ejercicios"
- "Ya aprobé el Colab de clase, sigamos"

**Requisitos previos:**
1. Debe existir `clases/clase-NN-tema/Clase NN - Tema - Spec.md` aprobado.
2. Debe existir `clases/clase-NN-tema/Clase NN - Tema - Clase.ipynb` aprobado (o al menos generado).
3. Debe existir `clases/clase-NN-tema/Clase NN - Tema - Solucionario.ipynb`, generado junto con `Clase.ipynb` — este script lo **actualiza**, agregando las soluciones de los ejercicios. Si no existe, el script avisa y no falla la generación de `Ejercicios.ipynb`, pero el paso queda incompleto hasta que exista.
4. Python con `nbformat` instalado.

Si falta alguno de los dos primeros, NO procedas: indícale a Diego qué falta y vuelve al paso correspondiente.

## Filosofía de los ejercicios

Reglas inquebrantables para cualquier ejercicio que propongas:

1. **Solo conceptos vistos hasta esta clase.** Si la clase es la 7 (input), NO uses condicionales (clase 9), bucles (clase 13), funciones (clase 19), listas (clase 25), strings avanzados (clases 22-24). Consulta `referencia-curriculo` si tienes dudas sobre qué se vio.
2. **Variables en español snake_case.** `precio_total`, `horas_estudio`, nunca `x`, `var1`, `total`.
3. **Contextos variados.** No concentres los 5 ejercicios en un solo tema. Mezcla videojuegos, deportes, música, finanzas básicas, comida, viajes — pero respeta los contextos preferidos del spec si están definidos.
4. **Enunciados claros y autocontenidos.** Un estudiante debe poder leerlos y resolver sin preguntar al profe.
5. **Soluciones funcionales.** Antes de proponer, valida mentalmente que el código corra. Si tienes dudas, mejor simplifica el ejercicio.

## Flujo obligatorio en dos fases

### Fase 1 — Proponer en chat (Modo 1 por defecto)

Antes de generar cualquier archivo, **propone los ejercicios en chat en formato markdown** siguiendo la plantilla `plantilla_ejercicios.md`. Esto permite a Diego revisar, ajustar contextos, corregir dificultad o cambiar ejercicios completos.

Estructura de la propuesta en chat:

```
## Propuesta de ejercicios — Clase NN: [tema]

Voy a proponer 5-6 ejercicios. 4 de práctica base y 1-2 desafíos opcionales (marcados con ⭐).

Conceptos que voy a usar (solo los ya vistos): [lista]
Contextos temáticos: [lista variada]

---

### Ejercicio 1 — [título]
[Enunciado breve, 2-3 líneas]
Resultado esperado: [una línea]

### Ejercicio 2 — [título]
...

[Y así con los 5-6]

---

¿Procedo a generar el .ipynb con estos ejercicios o quieres ajustar algo?
```

**Espera aprobación explícita.** Itera tantas veces como Diego pida. Cuando apruebe, pasa a Fase 2.

### Fase 2 — Generar el archivo intermedio y el .ipynb

1. **Escribe el archivo intermedio** `clases/clase-NN-tema/Clase NN - Tema - Ejercicios propuesta.md` con la propuesta aprobada completa (enunciados completos, pistas si aplica, resultado esperado, solución funcional). Sigue exactamente el formato de `plantilla_ejercicios.md`.

2. **Ejecuta el script** para convertir el archivo intermedio en el `.ipynb`:

   ```powershell
   python -X utf8 ".claude/skills/generar-colab-ejercicios/crear_colab_ejercicios.py" "clases/clase-NN-tema/Clase NN - Tema - Ejercicios propuesta.md" "clases/clase-NN-tema/Clase NN - Tema - Ejercicios.ipynb"
   ```

3. **Ejecuta el notebook para verificar que el código corre sin errores**, antes de mostrárselo a Diego:

   ```bash
   jupyter nbconvert --to notebook --execute --output <mismo-archivo> "Clase NN - Tema - Ejercicios.ipynb"
   ```

   Si alguna celda lanza una excepción o produce un output distinto al documentado, corrige y repite — no presentes el notebook con errores sin detectar. Esto NO valida las soluciones (que ya no viven en `Ejercicios.ipynb`) — antes de aprobar la propuesta en Fase 1, verifica mentalmente que cada solución en `Clase NN - Tema - Ejercicios propuesta.md` corra sin errores (ver regla 5 de "Filosofía de los ejercicios").

4. **Confirma a Diego** que `Ejercicios.ipynb` se generó (sin soluciones) y que `Solucionario.ipynb` se actualizó con las soluciones de estos ejercicios.

5. **Registra en `Clase NN - Tema - Historial.md`:**

   ```markdown
   ## [fecha] — Colab de ejercicios generado
   - Archivo: Clase NN - Tema - Ejercicios.ipynb
   - Solucionario.ipynb actualizado con las soluciones de estos ejercicios
   - Total ejercicios: N (X de práctica base + Y desafíos opcionales)
   - Contextos usados: [lista]
   - [notas si hubo iteraciones relevantes]
   ```

6. Commitea y pushea **solo la carpeta de esta clase** a GitHub (ver "Protocolo de cierre de etapa" en el `CLAUDE.md` raíz) — incluye `Ejercicios.ipynb` y el `Solucionario.ipynb` actualizado:

   ```
   git add "clases/clase-NN-tema-breve/"
   git commit -m "Clase NN - Tema: Ejercicios aprobado"
   git push
   ```

   Si el push falla, avisa a Diego con el error explícito — no reintentes con `--force`.

7. Confirma qué se subió a GitHub y entrega el link directo de Google Colab para `Ejercicios.ipynb` (reemplaza la subida manual):
   `https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-NN-tema-breve/Clase%20NN%20-%20Tema%20-%20Ejercicios.ipynb`
8. Después de confirmar, di: *"Antes de continuar al PPT, ejecuta `/compact` para limpiar el contexto. Avísame cuando estés listo."* Cuando Diego confirme, activa la skill `generar-ppt-clase`.

## Modo rápido (sin propuesta intermedia)

Si Diego dice explícitamente *"genera directo, sin proponer"* o *"al tiro, confía en ti"*, salta la Fase 1 y crea directamente el archivo intermedio + ejecuta el script. En este caso, después de generar, recomiéndale revisar el `.ipynb` y avisa que cualquier cambio implica regenerar.

Usa el modo rápido SOLO bajo instrucción explícita. No es el default.

## Estructura del notebook generado

El script produce:

| Sección | Contenido |
|---|---|
| Encabezado | "💪 Ejercicios — Clase NN: tema" |
| Introducción | Texto orientador breve |
| Índice | Lista de ejercicios con marca ⭐ para desafíos |
| Ejercicio 1 | Narrativa (3-4 líneas prosa) + bullets "El programa debe:" + pista(s) colapsable(s) + tabla input/output side-by-side + celda vacía |
| Ejercicio 2 | ... |
| ... | ... |
| Cierre | Preguntas de metacognición sobre la práctica |

Ninguna solución aparece en este notebook, ni siquiera oculta con `<details>` — solo las pistas (`💡`) son colapsables. Las soluciones se agregan a `Solucionario.ipynb` en una sección propia ("💪 Ejercicios adicionales — Soluciones").

## Iteración después de generar

- **Cambios menores en un enunciado o solución:** edita el `Clase NN - Tema - Ejercicios propuesta.md` y regenera el `.ipynb`. NO edites el notebook directamente porque la próxima regeneración lo sobrescribe.
- **Cambios estructurales (agregar/quitar ejercicio completo):** vuelve a Fase 1, repropón, aprueba, regenera.
- **Cambios sistémicos (que aplicarían a todas las clases futuras):** edita el script `crear_colab_ejercicios.py` y avisa a Diego.

## Reglas críticas

1. **Nunca uses conceptos no vistos.** Esta es la regla más fácil de violar y la más dañina pedagógicamente. Si dudas, simplifica el ejercicio.
2. **Nunca generes el .ipynb sin propuesta aprobada** (salvo modo rápido explícito).
3. **El archivo intermedio `Clase NN - Tema - Ejercicios propuesta.md` es la fuente de verdad.** Si hay discrepancia entre `.md` y `.ipynb`, regenera el `.ipynb`.
4. **Ninguna solución en `Ejercicios.ipynb`, ni siquiera oculta con `<details>`.** Todas las soluciones se agregan a `Solucionario.ipynb` (documento exclusivo del profesor), en su propia sección al final de ese archivo.
5. **Pistas colapsables, solo donde el ejercicio lo justifica.** No poner pistas en todos los ejercicios. Cada pista va dentro de `<details><summary>💡 Pista N — subtítulo</summary>...</details>`. Una pista orienta sin revelar la respuesta. Pueden incluir un ejemplo de código "stock" (contexto neutro) para ilustrar un patrón.
6. **No copies literalmente los ejercicios del spec.** El Colab de clase ya tiene la práctica independiente; el de ejercicios trae ejercicios DISTINTOS, aunque del mismo nivel.
7. **Mezcla contextos.** Si los 3 ejercicios del spec eran de e-commerce, los ejercicios adicionales pueden incluir otros temas para variar (a menos que Diego pida mantener el tema).

## Principios de diseño del notebook (consistentes con generar-colab-clase)

- **Formato canónico de cada ejercicio:** narrativa (3-4 líneas prosa) → bullets `**El programa debe:**` → pistas `<details>` → tabla input/output side-by-side → celda vacía. Ver restricción 15 de `CLAUDE.md` para el HTML exacto.
- **Tabla de ejemplos en HTML:** dos columnas (`Ejemplo 1` / `Ejemplo 2`), dos filas (`📥 El usuario escribe` / `📤 El programa imprime`) con `<pre>` dentro de `<td>`. Nunca descriptores en los encabezados ("Ejemplo 1 — condición falla").
- **`print()` con comas, nunca `+` y `str()`:** `print("Te quedan $", saldo, "en la tarjeta.")` — nunca `print("Te quedan $" + str(saldo) + "...")`.
- **Enunciados sin comandos ni operadores:** solo descripción de qué calcular, sin revelar el cómo.
- **Outputs con etiqueta descriptiva:** `print("¿Puede ver en HD?", velocidad >= 5)` — nunca `print(velocidad >= 5)` a secas.
- **Lenguaje "tú":** dirigirse al estudiante en segunda persona — nunca "el estudiante" o "el alumno".
- **Solo preguntar a Diego en gates formales:** propuesta de ejercicios y aprobación del notebook. Las correcciones técnicas intermedias se ejecutan sin preguntar.

## Consultas a otras skills

- **`referencia-curriculo`**: SIEMPRE consulta antes de proponer, para verificar qué conceptos están disponibles en esta clase. Lee al menos la tabla rápida.
- **`referencia-intereses-estudiantes`**: cuando exista, úsala para enriquecer contextos.
- **`disenar-clase`**: NO se invoca aquí. El spec ya está aprobado, esta skill solo lee el spec, no lo modifica.
