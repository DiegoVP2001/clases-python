# Historial — Clase 34: Control Strings Métodos y Búsqueda

## 2026-09-11 — Diseño completo aprobado y notebooks generados

**Contexto previo:** la Clase 33 (Strings — búsqueda) no alcanzó a dictarse el martes 08-sep y se dicta recién el lunes 14-sep. El martes 15-sep hay que aplicar un Control que cubra Clase 32 (métodos) y Clase 33 (búsqueda), que quedaron fuera del Control N°31 (acotado a N°28 y N°29). No es un "lunes estándar" (sin sesión de parejas el día anterior), pero se diseñó siguiendo la misma mecánica: primero el Control, después la Ejercitación espejo.

**Decisiones tomadas con Diego vía `AskUserQuestion` (dos rondas):**
- Actitud: **Rigor** (la misma de la Clase 33, dictada el día anterior).
- Cierre de actitud: pregunta **#5 — Contraste entre partes** ("¿En qué parte del control te costó más sostener el rigor que en el resto? Cuenta por qué ahí y no en otra parte."), rotando a la familia hoy-comparación — evita repetir la #2 (Clases 25/27) y la #3 (Control 31).
- Reparto de ítems: **3 ítems / 100 pts — 30 (Clase 32) + 30 (Clase 33) + 40 (cierre mixto)**.
- Escenario: **Los Mellis Al Paso** en todo (Control y Ejercitación), con situaciones nuevas dentro del mismo negocio.
- Textos fijos por ítem: **mixto** — 1 texto en el Ítem 1 (se autoverifica bien con un solo registro), 2 textos en los Ítems 2 y 3 (el segundo es el único que permite evaluar el caso "no está" → `False`/`-1`, el error típico de la Clase 33). Se mostraron previews concretas de las 3 opciones (mixta/corta/larga) antes de decidir.
- Ejercitación: **con** verificador automático ejecutable.
- Tiempos (80 min): 35 ejercitación / 25 control / 10 revisión + 10 de holgura.
- Sin `input()` (valores fijos escritos en el enunciado, mismo criterio del Control 31). Sin Ejercicios "0" en el Control (regla permanente).

**Ítems del Control (100 pts, 25 min, exigencia 50%):**
1. Etiqueta de despacho (30 pts) — `strip()` + `split()` con asignación múltiple + `title()` + `upper()`, 1 registro.
2. Comentarios de clientes (30 pts) — normalizar con `.lower()` + `in` + `find()`, 2 comentarios (uno con la palabra, otro sin ella).
3. Pedido por WhatsApp (40 pts, cierre mixto) — `split()` + corrección de tipeo + `title()` combinado con búsqueda normalizada dentro de la nota ya extraída, 2 pedidos.

**Ejercitación (35 min, sin nota):** guiado (`resumen` de Los Mellis, puente C32+C33) + Ejercicios 0a/0b (práctica pelada de métodos y de búsqueda) + 3 ejercicios hermanos de los ítems del Control (contextos distintos: boleta de chirimoya, comentarios de clientes, pedidos con nota). 1-2 pistas por ejercicio (salvo los "0"). Cierra con `## 🔓 Soluciones` colapsadas.

**Generado:**
- `Clase 34 - Control Strings Métodos y Búsqueda - Propuesta.json` (fuente de verdad)
- `generar_control.py`, adaptado de `clase-31-lunes-control-strings/generar_lunes.py`: solo se cambió la constante `PROPUESTA` y se corrigió `bloque_ejemplo()` para que no muestre un bloque "📥 El usuario ingresa" vacío cuando `stdin` es `[]` (artefacto visible en el Control 31 aplicado, que este Control tampoco necesita al no usar `input()`).
- Los 4 notebooks (`Ejercitación`, `Control`, `Control Solucionario Docente`, `Control Solucionario Estudiantes`), generados con `python generar_control.py`.

**Verificado:**
- `--check`: 9/9 soluciones correctas (guiado + 5 ejercicios + 3 ítems) y puntajes cuadrados (30+30+40=100, cada ítem con sus componentes sumando exacto).
- `Ejercitación.ipynb`: no menciona modalidad de trabajo en ninguna celda (se revisó el notebook completo, no solo la intro).
- `Control.ipynb`: sin ninguna solución en las celdas de código; sin bloques "El usuario ingresa" vacíos; la reflexión de cierre queda después del Ítem 3 y antes del checklist "Antes de entregar".
- `Control Solucionario Docente.ipynb`: tabla de distribución 30/30/40, rúbrica parcelada por ítem, bloque de criterios para el agente corrector.
- `Control Solucionario Estudiantes.ipynb`: solo tabla de puntaje por ítem (sin rúbrica ni criterios); cada ítem cierra con `🔎 **Qué se revisó:**`.

**Pendiente:**
- Publicación: la Ejercitación puede subirse al repo apenas esté aprobada. `Control.ipynb` y ambos Solucionarios **no se pushean hasta después de aplicado el control** (martes 15-sep, una vez corregido) — repo público, mismo criterio que todos los controles anteriores.
- Bookkeeping de la renumeración 2026-09-11 (carpeta de Listas renombrada a N°35, `Historial-Curricular.md` y `Plan Cierre...md` actualizados) — ver detalle en `Prompt.md`.
