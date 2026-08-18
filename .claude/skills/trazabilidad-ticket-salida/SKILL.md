# Skill: Trazabilidad de Tickets de Salida

## Propósito

Mantener actualizado `clases/Ticket de Salida - Trazabilidad.xlsx`, el registro acumulativo de cómo respondió cada estudiante las preguntas de alternativas de cada Ticket de Salida (Google Form), clase a clase.

## Cuándo usar esta skill

- Cuando Diego pida "actualiza la trazabilidad del Ticket de Salida", "registra las respuestas del último ticket", "cruza el ticket de salida de hoy" o similar, después de haber dictado una clase con Ticket de Salida.
- Es una rutina **on-demand**, nunca en cron ni automática: solo corre cuando Diego la dispara explícitamente.

## Prerrequisito

La clase debe tener ya generado su `Clase NN - Tema - Ticket de Salida Respuestas.json` (lo produce `generar-colab-clase`, ver la regla 17 del `CLAUDE.md` del proyecto).

## Flujo

1. **Leer la Google Sheet de respuestas** (destino del Form recurrente) vía la herramienta de Google Drive conectada:
   - Link: `https://docs.google.com/spreadsheets/d/1cgaKAJUsUU87u_4tTOGTNAred09Ctq-dkF7NqTa5svU/edit`
   - Usa `mcp__claude_ai_Google_Drive__read_file_content` con ese fileId (`1cgaKAJUsUU87u_4tTOGTNAred09Ctq-dkF7NqTa5svU`).
2. **Identificar filas nuevas** comparando la columna "Marca temporal" (única por envío) contra las ya registradas en `tools/tds_trazabilidad/respuestas_brutas.json`. Agrega solo las filas nuevas al array — nunca reordenes ni edites las existentes.
   - Cada fila: `{"marca_temporal", "nombre", "tema", "r1", "r2", "r3", "r4", "comprension"}` — copia "Nombre" y "Tema de la clase de hoy" tal cual aparecen en la Sheet (con errores de tipeo incluidos; el script normaliza el texto).
   - `"comprension"` viene de la 8va columna del Form/Sheet: *"Del 1 al 5, donde 1 es "no entendí" y 5 es "entendí todo", ¿cuánto entendiste el objetivo de hoy?"* — pregunta fija agregada al Form desde el 2026-08-04, sin proyectar (el estudiante la responde directo en el Form, no aparece en el `Ticket de Salida.pptx`) y sin respuesta correcta (autoevaluación, no MCQ). Copia el valor tal cual ("1".."5"); filas anteriores a esa fecha no tienen esta columna en la Sheet — deja `"comprension": ""` para esas.
3. **Correr el motor** desde la raíz del repo:
   ```
   python tools/tds_trazabilidad/actualizar_trazabilidad.py
   ```
   Reconstruye el Excel completo desde cero cada vez. **Nunca edites `clases/Ticket de Salida - Trazabilidad.xlsx` a mano.**
4. **Revisar la salida en consola**:
   - `⚠️ ... sin match de clase` → el "Tema" de esa fila no calzó con ningún `Ticket de Salida Respuestas.json` con suficiente similitud (umbral 0.35 en `difflib`). Revisa la fila en la hoja `Detalle` (queda marcada "revisar manualmente") y **pregunta a Diego a qué clase corresponde** (no lo asumas por similitud de texto sola — la marca temporal y el orden de llegada suelen ser la pista real) antes de tocar nada.
     - Si Diego confirma la clase, **no reemplaces el texto original** — edita el `tema` en `respuestas_brutas.json` agregando el tema oficial delante, entre paréntesis conservas lo que el estudiante escribió: `"for y range (tener en concepto el for)"`. Esto sube la similitud sobre el umbral sin perder el registro de qué escribió realmente (útil para detectar patrones de estudiantes que no leen bien el "Tema de la clase de hoy").
     - Si de verdad no corresponde a ninguna clase, se deja como "revisar manualmente" sin forzar nada.
   - `ℹ️ ... con tema escrito distinto al oficial` → el nombre del estudiante no matcheó exacto contra la nómina (se usó el más parecido). Confirma que el estudiante asignado es el correcto antes de dar por buena la corrida.
   - **Ayudantías: revisa incluso sin warning.** Los estudiantes suelen escribir el tema de una ayudantía de forma coloquial (ej. "ayudantia for") en vez del `tema` oficial del Ticket de Salida Respuestas.json (ej. "ejercitación ciclos") — eso puede quedar bajo el umbral 0.35 (sin match) **o, peor, matchear por error contra otra clase que comparte una palabra clave** (ej. "ayudantia for anidado" ganándole a "for avanzado" en vez de a "ejercitación ciclos", sin disparar ningún warning). Después de correr el script, si hubo una ayudantía en el lote, verifica en la hoja `Detalle` que todas sus filas cayeron en la clase correcta — no confíes solo en la ausencia de `⚠️`/`ℹ️`.
5. **Reportar a Diego** un resumen breve: cuántas respuestas nuevas se agregaron, de qué clase(s), y algún hallazgo destacable (pregunta más difícil del curso, estudiante con acierto bajo si es relevante mencionarlo).

## Diseño del Excel de salida

`clases/Ticket de Salida - Trazabilidad.xlsx`, 3 hojas, todas recalculadas por completo en cada corrida:

- **Detalle**: una fila por (estudiante, pregunta respondida, clase). Columnas: Fecha, Clase, Tema, Estudiante, Pregunta, Respuesta, Respuesta correcta, Acierto (✅/❌), Nota. La autoevaluación de comprensión aparece como una fila más con `Pregunta = "Comprensión objetivo (1-5)"`, `Respuesta` = valor 1-5, y `Respuesta correcta`/`Acierto` en "—" (no aplica, no tiene respuesta correcta).
- **Resumen por estudiante**: estudiante × clase, % de acierto, más columna de % global — y a continuación, mismo patrón para comprensión: promedio 1-5 por estudiante × clase, más columna de promedio global. **Última fila, "Promedio curso"** (fondo naranja, cursiva): promedio del curso completo por cada columna (acierto y comprensión, por clase y global) — sirve para comparar a un estudiante puntual contra el curso sin cambiar de hoja.
- **Resumen por clase**: clase × pregunta, % de acierto del curso (para ver qué preguntas costaron más) — más dos columnas finales: promedio de comprensión (1-5) del curso y N° de respuestas recibidas para esa pregunta. **Última fila, "Promedio general"** (fondo naranja, cursiva): acierto agregado por posición de pregunta (Pregunta 1, 2, 3...) y comprensión promedio, a través de todas las clases — vista rápida de qué posición de pregunta es sistemáticamente más difícil en el curso.

Las respuestas marcadas "No se preguntó" (cuando un Ticket tuvo menos de 4 preguntas) se excluyen de todos los cálculos. Las filas sin dato de comprensión (`"comprension": ""`, típicamente submissions previas al 2026-08-04) simplemente no generan fila de comprensión — no se cuentan como "—" ni afectan el promedio.

**Nota técnica — orden de clases mixto int/str:** el campo `"clase"` de los `Ticket de Salida Respuestas.json` no siempre es `int` (ej. `Clase 19.5 - Revisión Evaluación Condicionales` usa `"clase": "19.5"` como string). El script ordena con el helper `clave_orden_clase()` (intenta `float()`, si falla manda al final) — nunca ordenes por `ct[0]` directo en un `sorted()` nuevo, revienta con `TypeError: '<' not supported between instances of 'str' and 'int'`.

## Fuente de verdad

El script `tools/tds_trazabilidad/actualizar_trazabilidad.py` + `tools/tds_trazabilidad/respuestas_brutas.json` + los `Ticket de Salida Respuestas.json` de cada clase + la nómina en `.claude/skills/referencia-estudiantes/lista-estudiantes.md`. El `.xlsx` es 100% derivado — nunca es fuente de verdad, no se edita a mano.

## Privacidad

Diego confirmó explícitamente que este dato (nombres reales + respuestas) puede vivir en el repo público de GitHub sin restricción — no aplica el criterio estricto de otras evaluaciones (ver regla de `revision/` en el `CLAUDE.md`).
