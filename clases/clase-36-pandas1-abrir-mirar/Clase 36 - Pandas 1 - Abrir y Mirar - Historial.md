# Historial — Clase 36

## 2026-09-24 — Especificación aprobada
- Objetivo: explorar una base de datos real con pandas (abrir, tamaño, columnas, elegir columnas, valores faltantes), con curiosidad.
- Actitud elegida entre 4 opciones (Curiosidad, Orden, Atención al detalle, Precisión): **Curiosidad** — primera clase de pandas, antes de limpiar/filtrar se mira la tabla con curiosidad genuina.
- Alcance ya venía acotado por la vista previa aprobada (`Vista Previa - Pandas 1 Abrir y Mirar.ipynb`): `read_csv` (+ `sep=`/`encoding=`), `.head()`/`.shape`/`.columns`, elegir columnas, `.isna().sum()`/`.notna()`. Sin funciones propias.
- Estructura completa aprobada en una sola iteración, con un agregado a pedido de Diego: **tabla markdown de vista previa** en el Concepto 1 (así se ve `bbdd_guaguas.csv` ya abierto, con filas reales de Mateo/Emma/Sofía retomando el ejemplo de la Clase 35) — Diego pidió dejarlo como default para toda clase que abra un dataset real por primera vez; actualizado en `disenar-clase/SKILL.md`.
- Dataset real (`guaguas_maquillada.csv`, 858.782 filas, con nulos reales en `sexo`/`n`) renombrado en el código a `bbdd_guaguas.csv` para mantener la convención de nombre de N°35. No se commitea a esta carpeta por tamaño (~23 MB) — pendiente definir mecanismo de distribución al generar el Colab.
- Se crearon dos archivos chicos de apoyo en esta carpeta: `horario_buses_isla.csv` (demo de `sep=";"`, Concepto 2) e `inscripciones_taller.csv` (Ejercicio 4, mismo síntoma sin avisar).
- Se descartó explícitamente filtrar por valor específico (`tabla[tabla["col"]==valor]`) — es contenido propio de N°38 ("el regalo"), no se adelanta aquí.
