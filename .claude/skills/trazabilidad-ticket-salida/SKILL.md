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
   - Cada fila: `{"marca_temporal", "nombre", "tema", "r1", "r2", "r3", "r4"}` — copia "Nombre" y "Tema de la clase de hoy" tal cual aparecen en la Sheet (con errores de tipeo incluidos; el script normaliza el texto).
3. **Correr el motor** desde la raíz del repo:
   ```
   python tools/tds_trazabilidad/actualizar_trazabilidad.py
   ```
   Reconstruye el Excel completo desde cero cada vez. **Nunca edites `clases/Ticket de Salida - Trazabilidad.xlsx` a mano.**
4. **Revisar la salida en consola**:
   - `⚠️ ... sin match de clase` → el "Tema" de esa fila no calzó con ningún `Ticket de Salida Respuestas.json` con suficiente similitud (umbral 0.35 en `difflib`). Revisa la fila en la hoja `Detalle` (queda marcada "revisar manualmente") y decide si hay que ajustar el `tema` en `respuestas_brutas.json` o si de verdad no corresponde a ninguna clase.
   - `ℹ️ ... con tema escrito distinto al oficial` → el nombre del estudiante no matcheó exacto contra la nómina (se usó el más parecido). Confirma que el estudiante asignado es el correcto antes de dar por buena la corrida.
5. **Reportar a Diego** un resumen breve: cuántas respuestas nuevas se agregaron, de qué clase(s), y algún hallazgo destacable (pregunta más difícil del curso, estudiante con acierto bajo si es relevante mencionarlo).

## Diseño del Excel de salida

`clases/Ticket de Salida - Trazabilidad.xlsx`, 3 hojas, todas recalculadas por completo en cada corrida:

- **Detalle**: una fila por (estudiante, pregunta respondida, clase). Columnas: Fecha, Clase, Tema, Estudiante, Pregunta, Respuesta, Respuesta correcta, Acierto (✅/❌), Nota.
- **Resumen por estudiante**: estudiante × clase, % de acierto, más columna de % global.
- **Resumen por clase**: clase × pregunta, % de acierto del curso (para ver qué preguntas costaron más).

Las respuestas marcadas "No se preguntó" (cuando un Ticket tuvo menos de 4 preguntas) se excluyen de todos los cálculos.

## Fuente de verdad

El script `tools/tds_trazabilidad/actualizar_trazabilidad.py` + `tools/tds_trazabilidad/respuestas_brutas.json` + los `Ticket de Salida Respuestas.json` de cada clase + la nómina en `.claude/skills/referencia-estudiantes/lista-estudiantes.md`. El `.xlsx` es 100% derivado — nunca es fuente de verdad, no se edita a mano.

## Privacidad

Diego confirmó explícitamente que este dato (nombres reales + respuestas) puede vivir en el repo público de GitHub sin restricción — no aplica el criterio estricto de otras evaluaciones (ver regla de `revision/` en el `CLAUDE.md`).
