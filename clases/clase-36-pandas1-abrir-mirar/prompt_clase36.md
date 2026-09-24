Sigo con el proyecto de Cierre de Octubre (4to medio, clases-python-4tomedio/clases/clases-octubre/).

Contexto: ya está cerrado el diseño completo (objetivo, rúbricas, calendario 14 sesiones,
instrumentos), con dos rediseños posteriores:

1. **Simplificación 2026-09-23:** código del proyecto sin funciones propias, pregunta base de una
   sola dimensión, calendario dividido 05-oct/06-oct.
2. **Rediseño 2026-09-24 (este):** se cortó la antigua N°36 "Listas — iteración y métodos" — la
   intuición de pandas se construye directamente sobre pandas (pizarra + diagramas + "Escríbelo tú"),
   no con una réplica manual en listas que nunca se vuelve a usar. El bloque de pandas pasó de 3 a 5
   sesiones: **N°36 Pandas 1 · N°37 y N°38 dividen lo que era una sola "Pandas 2a" densa (limpiar+
   normalizar+filtrar) · N°39 deriva/agrupa/ordena · N°40 grafica.** La Evaluación
   Funciones+Strings+Listas quedó **sin fecha fija** — antes 8-oct, ese día ahora lo ocupa Graficar;
   Diego todavía no decide si la aplica, la cambia de formato, o le busca otro día.

Lee primero la memoria del proyecto (busca "project-cierre-octubre-proyecto-abp") y
`clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` para el estado completo antes de
hacer nada.

**Clase a producir: N°36 — Pandas 1: abrir y mirar (martes 29-sep).**

**Depende de:** N°35 aprobada y dictada.

✅ **Numeración confirmada 2026-09-24** — esta es la carpeta oficial (`clase-36-pandas1-abrir-mirar`,
renombrada desde `clase-36-listas-metodos`; el contenido viejo de esa carpeta quedó archivado en
`_archivo-2026-09-24-contenido-cortado/`). No hace falta resolver nada en el Paso 1 de
`disenar-clase` salvo la confirmación de rutina de siempre.

**Alcance ya aprobado por Diego (vista previa liviana en esta misma carpeta, úsala como contrato de
qué debe quedar consolidado, no te desvíes sin consultarle):** el `.ipynb` que está junto a este
archivo.

**Contenido:** `pd.read_csv(...)` (con `sep=`/`encoding=` cuando la base los necesite), `.head()`,
`.shape`, `.columns`, elegir columnas, `.isna().sum()` y `.notna()` (contar y filtrar vacíos — misma
técnica de filtrar filas, con esta condición). **Sin funciones propias en ningún punto** — ver
`Catastro de Bases y Banco de Preguntas - Proyecto Octubre.md` §6 para las 10 operaciones canónicas
y por qué se decidió así.

⚠️ Decir explícito en la clase que pandas NO entra en la Evaluación de Funciones+Strings+Listas
(fecha pendiente) — para no generar ansiedad antes de la prueba.

**Flujo:** `disenar-clase` → `generar-colab-clase` → `generar-ppt-clase` (flujo normal de clase
regular).

No produzcas ningún archivo antes de que yo apruebe cada etapa — sigue el flujo de gates normal
del proyecto (ver CLAUDE.md de `clases-python-4tomedio`).
