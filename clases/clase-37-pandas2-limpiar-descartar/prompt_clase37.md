Sigo con el proyecto de Cierre de Octubre (4to medio, clases-python-4tomedio/clases/clases-octubre/).

Contexto: rediseño 2026-09-24 — la antigua "Pandas 2a" (limpiar a número + normalizar categorías +
filtrar, las 3 en una sola sesión) tenía demasiada sintaxis densa junta (`.astype()`, el accesor
`.str`, `errors="coerce"`, `.replace()` con diccionario) y se dividió en 2 clases. Esta es la primera.
Lee primero la memoria del proyecto (busca "project-cierre-octubre-proyecto-abp") y
`clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` para el estado completo antes de
hacer nada.

**Clase a producir: N°37 — Pandas 2, Clase 1 (A+C): limpiar a número + descartar filas sucias
(fecha provisoria: jueves 01-oct).**

**Depende de:** N°36 aprobada y dictada.

✅ **Numeración confirmada 2026-09-24** — carpeta oficial `clase-37-pandas2-limpiar-descartar` (nueva,
reemplaza a la antigua `clase-37-pandas1-abrir-mirar`, cuyo contenido se movió a N°36).

**Alcance ya aprobado por Diego (vista previa liviana en esta misma carpeta, úsala como contrato de
qué debe quedar consolidado, no te desvíes sin consultarle):** el `.ipynb` que está junto a este
archivo.

**Contenido:**
- Limpiar a número: `pd.to_numeric(serie.str.replace(...), errors="coerce")` — la técnica más densa
  del bloque completo, se le da la sesión completa sin compartirla con nada más.
- Descartar filas sucias, **pero solo por esta columna** (`cantidad_guaguas.notna()`) — el descarte
  combinado con la columna de categorías normalizadas (que todavía no existe) se hace recién al
  abrir N°39, como puente entre las dos clases de limpieza.

**Sin funciones propias en ningún punto** — ver `Catastro de Bases y Banco de Preguntas - Proyecto
Octubre.md` §6 para las 10 operaciones canónicas.

⚠️ **Pendiente de resolver antes de dictar:** la fecha real de esta sesión. El bloque de pandas pasó
de 4 a 5 sesiones y el calendario 29-sep→08-oct ya no tiene un día libre — ver
`Proyecto Cierre Octubre - Plan y Pendientes.md` §3 para el detalle de qué se movió.

**Flujo:** `disenar-clase` → `generar-colab-clase` → `generar-ppt-clase` (flujo normal de clase
regular).

No produzcas ningún archivo antes de que yo apruebe cada etapa — sigue el flujo de gates normal
del proyecto (ver CLAUDE.md de `clases-python-4tomedio`).
