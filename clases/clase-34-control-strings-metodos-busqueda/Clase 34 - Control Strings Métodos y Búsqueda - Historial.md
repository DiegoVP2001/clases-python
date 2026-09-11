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

## 2026-09-11 (más tarde) — Rediseño tras revisión de Diego

Feedback textual de Diego sobre la versión recién generada: *"defineles de antemano las variables con el texto que deban trabajar [en Control y Ejercitación] para así solo enfocarse en lo que deben hacer con los textos. además en el control simplificaría el asunto a un solo texto de verificación y además no usaría ';' sino ',' que trabajamos en clases. por último las siento bastante largas cada pregunta para el control rápido, prefiero que sea bien focadas"*. Además pidió que el resultado esperado quede explícito por caso, sin dejar nada a interpretación.

**Decisiones tomadas (vía `AskUserQuestion`):**
- **Un texto por ítem** en el Control (no un único texto compartido por los 3).
- **Ítem 2** repensado: en vez de 2 comentarios largos con roles simétricos, pasa a **1 comentario principal + 1 comentario brevísimo** (`"Todo joya, gracias"`), solo de ejemplo para forzar el caso "no está". Esto **reemplaza** la decisión "textos fijos por ítem: mixto" de la sesión anterior — este mismo día se probó y se descartó.
- **Ejercitación:** el Ejercicio 3 baja a 1 solo texto (espejo del nuevo Ítem 3); el **Ejercicio 2 mantiene los 2 comentarios completos** (ahí se sigue entrenando el contraste True/False que el Control ya no mide con la misma amplitud).
- Se fija como **default para los próximos lunes estándar** (actualizado en el `CLAUDE.md` raíz del proyecto, sección "Workflow: lunes estándar"): variables predefinidas, un texto por ítem, resultado esperado explícito y segmentado por caso.

**Cambios de contenido:**
- **Ítem 1 (30 pts):** sin cambios de fondo, solo `setup_py` con `etiqueta = "  ana soto,delivery  "` y enunciado ajustado para referenciar la variable en vez de decir "ya guardada".
- **Ítem 2 (30 pts):** `comentario_1` (sin cambios) + `comentario_2` nuevo, brevísimo. Resultado esperado segmentado por comentario (`secciones`). Rúbrica ajustada solo en el componente de salida.
- **Ítem 3 (40 pts):** de **2 pedidos separados por `;`** a **1 solo pedido separado por `,`** (`pedido = "  chorrillana especiall,SIN cebolla por favor  "`). De 7 a 5 bullets. Rúbrica rediseñada: los componentes con parcial "correcto en uno pero no en el otro" desaparecen (ya no hay 2 pedidos); nuevos componentes 6+8+8+8+10=40.
- **Ejercicio 3** de la Ejercitación: mismo criterio que el Ítem 3 (1 registro, coma).
- Todos los enunciados (guiado + 5 ejercicios + 3 ítems) pierden el bullet "Guardar X en una variable" (ya no aplica) y el "con etiqueta clara" (el bloque de resultado esperado es el contrato).

**Cambios al generador (`generar_control.py`):**
- `code_cell_solucion(marca, setup_py)`: nueva celda de solución con marcador + variables predefinidas + centinela `# ── Escribe tu programa desde aquí ──`.
- `_revisar()` (dentro de `VERIFICADOR_BASE`): el chequeo de "celda vacía" ahora mira el contenido después del centinela, no después de la primera línea — probado con una simulación completa (solución correcta ✅, celda vacía ⬜).
- `bloque_ejemplo()`: encabezado explícito "Tu programa debe imprimir exactamente estas líneas"; soporta `secciones` (lista de `{"caso", "n_lineas"}`) para partir el mismo `stdout` en sub-bloques por texto trabajado, sin duplicarlo.
- `validar_setup()`: nueva validación — cada `setup_py` debe aparecer tal cual dentro de `solution_py`, o no se escribe ningún notebook.

**Verificado:**
- `--check`: 9/9 soluciones OK, `setup_py` consistente con `solution_py` en las 9 piezas, puntajes cuadrados (30+30+40=100).
- Los 4 notebooks regenerados. Confirmado a ojo: ninguna celda de datos contiene `;`, ninguna celda menciona modalidad de trabajo, el Solucionario Estudiantes sigue sin rúbrica de puntos.
- Simulación del verificador de la Ejercitación con una celda resuelta y una vacía: ambos casos funcionan como se espera.
- **Sigue pendiente aplicar el control** — no se pushea `Control.ipynb` ni los Solucionarios hasta después del martes 15-sep.
