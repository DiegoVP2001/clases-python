---
name: revisar-evaluacion
description: Orquesta la revisión completa de una evaluación Python — desde preparar las entregas (submissions) hasta calibrar la rúbrica, revisar en lotes, generar el resumen final y el feedback individual en Excel. Usa esta skill cuando Diego diga que quiere revisar, calificar o corregir entregas, evaluaciones o notebooks de estudiantes (ej. "revisemos las entregas de Classroom", "quiero calificar los notebooks").
---

# Skill: revisar-evaluacion

## Propósito

Orquestar la revisión completa de una evaluación Python: desde la lectura de notebooks de estudiantes hasta generar el resumen final (md, csv, xlsx) y el feedback individual en Excel.

## Cuándo activar

Cuando Diego diga algo como "vamos a revisar la evaluación", "quiero calificar los notebooks" o "revisemos las entregas de Classroom".

---

## Flujo de trabajo

### Fase 0 — Preparar submissions

1. Leer los notebooks de estudiantes en `clases/<carpeta-evaluacion>/cuadernos_ev_estudiantes/`
2. Ejecutar `tools/review_eval/preparar_submissions.py` para crear `revision/puntajes.json` con la estructura inicial de todos los estudiantes.
3. Verificar que `puntajes.json` tiene todos los estudiantes del curso.

### Fase 1 — Calibrar rúbrica

**Esta fase es obligatoria antes de calificar el primer batch.**

1. Leer el solucionario de la evaluación (ubicado en la carpeta de la evaluación).
2. Calibrar los criterios ejercicio por ejercicio con Diego. Preguntar por:
   - Puntaje máximo de cada ejercicio
   - Criterios de puntaje parcial (¿qué vale la mitad?, ¿qué vale cero?)
   - Casos borde esperados (ej: variable de actualización vs. múltiples variables)
3. Guardar la calibración en `revision/criterios_calibracion.json`.
4. **No calificar ningún notebook antes de terminar esta fase.**

> La rúbrica NO es estática. Cada evaluación tiene su propio solucionario y sus propios criterios. Nunca asumir criterios de evaluaciones anteriores.

### Fase 2 — Revisar en batches

Revisar los notebooks de a grupos pequeños (3-6 estudiantes por batch) para mantener el contexto manejable.

Por cada batch:
1. Un subagente lee el contenido de los notebooks del batch.
2. Diego y Claude calibran los puntajes usando los criterios de Fase 1.
3. Ejecutar `tools/review_eval/actualizar_batch.py` con el batch calificado.
4. El script actualiza `revision/puntajes.json`.
5. Pedir `/compact` antes del siguiente batch si el contexto está pesado.

Formato de batch para `actualizar_batch.py`:
```python
BATCH_N = {
    "Nombre Estudiante": {
        "ej1": {"obtenido": X, "maximo": Y, "comentario": "..."},
        "ej2": {"obtenido": X, "maximo": Y, "comentario": "..."},
        # ...
    }
}
```

### Fase 3 — Calcular notas

Ejecutar `tools/review_eval/calcular_notas.py` para agregar los totales y notas al `puntajes.json`.

Fórmula chilena (dos tramos lineales):
- `nota_min = 2.0`, `nota_aprobacion = 4.0`, `nota_max = 7.0`
- Exigencia por defecto: **50%**
- Si Diego indica otra exigencia, usar esa.

### Fase 4 — Generar resumen final

Ejecutar `tools/review_eval/generar_resumen_final.py`.

**Exclusiones obligatorias:**
- Estudiantes ausentes (total == 0)
- Estudiantes excluidos por deshonestidad académica (configurar en `EXCLUDED` del script)

> Nota: las exclusiones por deshonestidad son específicas de cada evaluación. No son permanentes. Verificar con Diego cuáles aplican.

Genera:
- `revision/resumen_final.md` — tabla markdown con puntajes y estadísticas
- `revision/resumen_final.csv` — importable a Google Sheets
- `revision/resumen_final.xlsx` — Excel formateado con color coding

### Fase 5 — Generar feedback individual

Ejecutar `tools/review_eval/generar_feedback.py`.

Genera `revision/feedback_estudiantes.xlsx`:
- Hoja "Bienvenida": lista alfabética de nombres con hipervínculo a la hoja del estudiante
- Una hoja por estudiante, nombradas anónimamente ("Estudiante 1", "Estudiante 2", …) ordenadas por puntaje descendente
- Dentro de cada hoja: tabla de ejercicios, total, nota, mensaje motivacional según nivel
- Sin nombre del estudiante dentro de la hoja individual (privacidad)

Mensajes motivacionales según nivel:
- **Aprobado (nota ≥ 4.0):** celebrar la dedicación, proyectar hacia el futuro
- **Medio (total ≥ 30, nota < 4.0):** validar el avance, señalar que la aprobación está cerca
- **Reprobado (total < 30):** no desanimar, expresar confianza del profesor, normalizar el error como aprendizaje

---

## Archivos del sistema

| Archivo | Propósito |
|---|---|
| `tools/review_eval/preparar_submissions.py` | Inicializa `puntajes.json` con todos los estudiantes |
| `tools/review_eval/actualizar_batch.py` | Ingresa puntajes de un batch al JSON |
| `tools/review_eval/calcular_notas.py` | Calcula totales y notas |
| `tools/review_eval/generar_resumen_final.py` | Genera md, csv, xlsx del curso |
| `tools/review_eval/generar_feedback.py` | Genera Excel de feedback individual |
| `revision/puntajes.json` | Fuente de verdad de la revisión |
| `revision/criterios_calibracion.json` | Rúbrica calibrada para la evaluación actual |

---

## Defaults

| Parámetro | Valor |
|---|---|
| Exigencia | 50% |
| Escala | 2.0 – 7.0 (nota de aprobación: 4.0) |
| Formato feedback | Excel (hoja por estudiante) |
| Formato resumen | md + csv + xlsx |

---

## Reglas críticas

1. **Calibrar siempre antes de calificar.** No asumas criterios de evaluaciones anteriores.
2. **Nunca incluir ausentes en el resumen final.** Filtrar por `total == 0`.
3. **Exclusiones por deshonestidad son específicas de cada evaluación.** Confirmar con Diego cuáles aplican.
4. **Mantener batches pequeños** (3-6 estudiantes) para no perder contexto.
5. **No mostrar el nombre del estudiante dentro de su hoja de feedback** — solo en la hoja de Bienvenida.
6. **`NAME_OVERRIDES`** en los scripts permite corregir nombres mal escritos o nicknames (ej: "Estudiante Profesor Diego 1" → "Alex").
