# Historial — Clase 37

## 2026-09-24 — Especificación aprobada
- Objetivo: Convertir una columna numérica sucia en datos confiables, descartando solo las filas que de verdad no se puedan recuperar, con perseverancia.
- Actitud elegida: Perseverancia (segunda tanda de opciones — la primera, más orientada a "cuidado técnico", se sintió muy parecida entre sí).
- **Antes de proponer objetivo/estructura**, se detectó y resolvió un hallazgo técnico bloqueante: `pd.read_csv()` sin más convertía en silencio la columna `n` de `bbdd_guaguas.csv` a `float64`, corrompiendo valores con punto de miles (ej. `"2.908"` leído como 2.908 en vez de 2908) sin ningún error ni `NaN`. Se resolvió con `dtype={"n": "str"}` al leer — verificado sin pérdida de datos (4.293 nulos antes = 4.293 después de limpiar). No requirió tocar `maquillar_guaguas.py` ni regenerar archivos. Registrado también en `clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` §6, con nota para N°39 (necesitará el mismo fix al reabrir el archivo).
- El Concepto 1 original de la vista previa (la cadena completa `dtype`+`strip`+`replace`+`to_numeric` en un solo bloque) se dividió en 5 conceptos graduales a pedido de Diego, cada uno agregando una sola pieza sobre el código del anterior (patrón "Escríbelo tú").
- Estructura aprobada en 4 iteraciones: (1) objetivo/propósito con las funciones nombradas explícitamente → Diego pidió sacarlas del objetivo; (2) estructura inicial con el ICN en un solo concepto denso → Diego pidió graduarlo en pasos; (3) actitud, dos tandas de opciones; (4) aprobación final.
- Vista Previa de N°37 (`Vista Previa - Pandas 2 Clase 1 (A+C) Limpiar y Descartar.ipynb`) actualizada con el código corregido antes de este gate.
