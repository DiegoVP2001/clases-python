# Noviembre IA · 3ro medio — Checklist y traspaso entre sesiones

**Actualizado:** 2026-10-31 (cierre de la sesión que produjo la Clase 41). **Para quién:** la próxima sesión de Claude Code que diseñe la **Clase 42** (y las siguientes). Léelo completo antes de proponer nada.

## 0. Cómo partir (orden de lectura)

1. Este archivo.
2. `Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` → §3 (calendario), §5 (condiciones de los Colabs), §6 (evaluaciones) y **§10** (integración con el proyecto; manda sobre el v2 donde difieran).
3. `clases/clase-41-mapa-ia-pipeline/` como **modelo de referencia**: `Clase 41 - Mapa IA - Spec.md` (formato de spec), `Historial.md`, `Guía Docente Voz.md`, `fuentes/` y `generar_clase.py`.
4. `CLAUDE.md` raíz del proyecto: reglas 2, 7, 8, 13, 14, 15, 21 y 24, y la sección «Bloque IA de noviembre».
5. Según el flujo de `disenar-clase`: **confirmar el contexto con Diego y ofrecerle 3-4 actitudes para que elija una** antes de redactar objetivo (no asumir la actitud).

## 1. Estado de las clases

| N° | Fecha | Tema | Estado |
|---|---|---|---|
| **41** | lun 2-nov | Mapa de la IA + pipeline | ✅ Aprobada por Diego y **desplegada** (https://clases-ia-mario-bertero.vercel.app/clase-41/). **Pusheada a GitHub el 2026-10-31** (commits `13cc600` y `a9e2c86`). |
| **42** | mar 3-nov | Primer clasificador ML | ☐ **Por diseñar — es lo siguiente.** Brief en §4. |
| **43** | jue 5-nov | Construir una neurona | ☐ Por diseñar. Brief en §5. |
| 44 | lun 9-nov | Entrenar una red (`MLPClassifier`) y medir aciertos (`accuracy`) | ☐ |
| 45 | mar 10-nov | Mini-LLM (generador de juguete; se evalúa en E2) | ☐ |
| 46 | jue 12-nov | **E1** (45 min) + revisión + intro a prompting | ☐ |
| 47 | lun 16-nov | Prompting con ChatGPT (Colab de registro) | ☐ (bloqueada por permisos/edad, ver §7) |
| — | mar 17-nov | **Sin clase** (ausencia docente) | — |
| 48 | jue 19-nov | **E2** (45 min) + revisión + intro a ética | ☐ (bloqueada por permisos/edad y contingencia) |
| 49 | lun 23-nov | Ética y 4D | ☐ (necesita las definiciones 4D: ver §7) |
| 50 | mar 24-nov | Integración (práctica sin nota) | ☐ |
| 51 | jue 26-nov | **E3** (60–65 min) | ☐ |

La numeración 41–51 sigue la del `Historial-Curricular.md` (el N°41 antiguo, evaluación Funciones+Strings+Listas, quedó eliminado el 2026-10-07 y el número se reutilizó). Las filas 42–51 **ya están en el Historial** como «Por diseñar».

## 2. Decisiones vigentes (no reabrir sin que Diego lo pida)

**Del plan v2 (ChatGPT, cerradas):** calendario de 11 sesiones; trabajo individual con entrada autónoma para quien falte; Python simple hasta listas, **sin pandas**; clasificación **binaria** (sin multiclase ni matriz de confusión); `MLPClassifier` y `accuracy` el 9; mini-LLM el 10 pero se evalúa en E2; E1 y E2 al inicio de la sesión; dos notas (promedio de E1 y E2, y E3).

**Tomadas con Diego (2026-10-31):**
- **Flujo liviano:** Spec → *gate* → Colab + Solucionario (+ HTML si aplica) → *gate* → commit/push de la carpeta. Sin PPT principal ni `Ejercicios.ipynb`, ni Ticket por Google Form. (Para N°41 Diego pidió además un PPT paso a paso del pipeline: es una excepción pedida, no un default.)
- **Práctica y ticket autorrevisados:** Diego **no recolecta resultados**. Todos los ejercicios llevan **pistas**; los Colabs de N°42 en adelante llevan **autochequeo `check_*()`** (✅/⚠️ + pista, sin mostrar la solución) en los ejercicios clave.
- **Sin sección «Propósito»; «¿Por qué lo veremos?»** en lugar de «¿Para qué sirve?» (vale para **todas** las clases; regla 24 del `CLAUDE.md`). La actitud queda como etiqueta del spec y como pregunta de cierre.
- **Curso en el encabezado: «3ro medio»** (4to ya egresó).
- **Dos ejemplos en una misma clase:** lo que Diego explica usa el **riego automatizado de una viña de Isla de Maipo, como Santa Ema**; las actividades usan el **sistema de climatización de las bodegas donde fermenta la uva**. Datos ficticios. En N°42–43 decidir en la spec cuál va en cada parte (regla de contextos variados).
- **Terminología:** «set de entrenamiento» («aquí la computadora aprende») y «set de prueba» («aquí vemos si es capaz de predecir»).
- **4D:** no entran hasta la clase de ética (23-nov). Antes se puede hablar de «revisar si algo es confiable» sin nombrarlas.
- **Cambio de página con código:** en N°41 cada actividad del HTML se abre con un código de 3 números que entrega Diego; no es seguridad.
- **ChatGPT Voice como colega** (criterio completo en la memoria `feedback-voz-codocente-chatgpt-criterio`): solo habla cuando Diego la activa («Colega, …»); **bienvenida** (espera el saludo del curso y pide que alguien lea el objetivo), **Haz Ahora** y **verificación de comprensión del contenido nuevo**; **no es protagonista** en práctica guiada, independiente ni cierre. Cada clase lleva su `Guía Docente Voz.md` (prompt de arranque, tabla momento → frase de activación → qué dice → plan B, y aviso de silenciar el micrófono entre intervenciones).
- **Ejemplos genéricos:** no afirmar que un producto concreto usa una técnica sin evidencia (v2 §4).

## 3. Cómo se produjo la N°41 (patrón a reutilizar)

Carpeta `clases/clase-41-mapa-ia-pipeline/`:

| Archivo | Para qué | Cómo se regenera |
|---|---|---|
| `Clase 41 - Mapa IA - Spec.md` | Contrato aprobado | A mano, con aprobación de Diego |
| `fuentes/diagramas.py` | Diagramas SVG (mapa y pipeline) y helpers (`tira`, `tabla`, `bloque_*`) | Editar y correr `construir.py` |
| `fuentes/diapositivas.py` | 14 diapositivas del pipeline + notas | Ídem |
| `fuentes/plantilla_interactivo.html` | HTML interactivo (3 páginas, 8 actividades, códigos en `CODIGOS`) | Ídem |
| `fuentes/construir.py` | Arma el HTML, exporta los PNG con Edge, genera el `.pptx` y copia todo a `sitio-hub/clase-41/` | `cd fuentes && py -3 construir.py` |
| `generar_clase.py` | Genera `Clase 41 - Mapa IA - Clase.ipynb` (JSON directo, sin `nbformat`) | `py -3 generar_clase.py` |
| `Guía Docente Voz.md`, `Historial.md` | Docentes / registro | A mano |

**Nunca editar a mano** el `.html`, los `.png`, el `.pptx` ni el `.ipynb` generados: se editan las fuentes y se regenera.

**Deploy (hub en Vercel):** proyecto `clases-ia-mario-bertero` en el equipo Personal `diegovp2001`. Para publicar cambios: regenerar con `construir.py` y luego, desde `sitio-hub/`, `npx vercel deploy --prod --yes --scope diegovp2001`. Cada clase nueva con interactivo agrega `sitio-hub/clase-NN/index.html` y una tarjeta en `sitio-hub/index.html`. **No volver a conectar el proyecto con GitHub** (`vercel link` lo hace solo; se deshizo con `vercel git disconnect`, y un push podría pisar el sitio con un deploy desde la raíz del repo).

**Trampas técnicas de este equipo (Windows):**
- Python se invoca con **`py -3`** (`python` no existe). `nbformat` está instalado a medias (le falta `traitlets`): los notebooks se escriben como JSON a mano.
- Para exportar SVG → PNG se usa **Edge headless** (`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`), no hay otra librería.
- El generador del Colab de las clases regulares (`.claude/skills/generar-colab-clase/crear_colab.py`) **no** sirve tal cual para este flujo liviano; ya acepta el título «¿Por qué lo veremos?» (cambio del 2026-10-31).
- En el HTML, el atributo `hidden` pierde frente a `display:flex`: se añadió `[hidden]{display:none!important}`.
- Ver la guía de verificación en navegador: levantar `py -3 -m http.server <puerto> --bind 127.0.0.1` dentro de `sitio-hub/` y probar con Chrome; cerrar pestaña y servidor al terminar.

## 4. Brief para la Clase 42 — Primer clasificador ML (mar 3-nov)

**Fuente:** v2 §3 fila 2 y §5.

- **Objetivo del v2:** entrenar un clasificador binario y usarlo con entradas nuevas.
- **Contenidos nuevos esenciales:** entradas y etiquetas en **listas**; `fit()` como entrenamiento y `predict()` como predicción.
- **Evidencia:** Colab con datos pequeños simulados, entrenamiento y **al menos 3 predicciones nuevas**; modificar una entrada y explicar un resultado. **No** exigir todavía el cálculo de `accuracy`.
- **Condiciones del Colab (v2 §5):** objetivo, requisitos mínimos, **recapitulación breve** y datos incluidos (quien faltó a N°41 debe poder partir sin haber hecho nada), instrucciones de ejecución, bloques «Escríbelo tú», experimentación y conclusión individual. Importaciones y partes complejas ya preparadas. Ejecutable de arriba abajo desde una sesión nueva, con semillas. Sin descargas frágiles, GPU, claves API ni pandas.
- **Momentos de la voz (decididos por Diego para N°42):** bienvenida; **Haz Ahora con la voz como cliente** que pide el clasificador (ej. «¿llevo paraguas?» o el riego) y el curso decide qué datos pedirle (variables y etiqueta); **humano vs. voz vs. modelo** ante un caso nuevo (el curso predice a ojo, la voz predice, después se corre `predict()` y se comparan los tres); **explicar un error** (cuando el modelo se equivoca, la voz explica y el curso juzga si cuadra con los datos); verificación de comprensión de `fit` vs. `predict` tras el contenido nuevo. Práctica guiada, independiente y cierre: la voz no es protagonista.
- **Sin sección «Propósito»**; sí «¿Por qué lo veremos?» (máx. 2 frases, ligada a lo que se practica).
- **Formato de ejercicios:** el canónico del `CLAUDE.md` (narrativa, «El programa debe:», pistas `<details>` 1–2 por ejercicio, resultado esperado con ícono + `<em>` + `<pre>`, celda de código vacía). Pistas siempre; `check_*()` en los ejercicios clave.
- **Entregables (flujo liviano):** `Clase 42 - Primer Clasificador - Spec.md` → gate → `Clase.ipynb` + `Solucionario.ipynb` + `Guía Docente Voz.md` + `Historial.md` → gate → commit/push + link de Colab.

**Decisiones que quedan abiertas para la spec de N°42 (proponer con recomendación y que Diego decida):**
- Actitud (ofrecer 3–4 opciones).
- Qué algoritmo de scikit-learn usar para el primer clasificador (el v2 no lo fija; debe funcionar con listas pequeñas y dar resultados interpretables; fijar `random_state`).
- Qué contexto va en la parte explicada y cuál en los ejercicios (riego de la viña / bodega / uno nuevo), y que no todos los ejercicios sean del mismo tema.
- Si los datos van **escritos en el propio Colab** (recomendado: sin archivos) y cuántas filas (evitar aciertos triviales; v2 §5).

## 5. Brief para la Clase 43 — Construir una neurona (jue 5-nov)

- **Objetivo del v2:** explicar cómo entradas, pesos y sesgo producen una salida.
- **Contenidos:** suma ponderada, sesgo, activación simple (escalón), idea de error y ajuste de pesos.
- **Evidencia:** Colab donde el estudiante **escribe el cálculo de una neurona**, cambia pesos y compara salidas, y explica qué cambió. Ajuste **manual** exploratorio: **sin retropropagación**.
- **Fórmulas:** LaTeX en markdown (Colab usa MathJax); `\$` escapado si aparece dinero.
- **Voz:** criterio general (Haz Ahora, verificación del contenido nuevo); afinar en el gate de la spec. Idea sugerida por la sesión anterior (no decidida): que la voz calcule en voz alta una salida con entradas y pesos dictados y el curso la **verifique con su código**.
- Misma estructura de entregables y condiciones de Colab que N°42.

## 6. Clases 44–51 (resumen del v2)

| N° | Contenido nuevo | Producto individual |
|---|---|---|
| 44 | `MLPClassifier`; separación entrenamiento/prueba; aprendizaje como ajuste de pesos; **`accuracy` = aciertos / total evaluado** | Colab con `fit()`, `predict()`, `accuracy` sobre prueba y un cambio controlado; explicar un error y por qué no garantiza desempeño futuro. No usar prueba para elegir cambios. |
| 45 | Tokens, siguiente token, probabilidades, errores de generación | Colab con generador de juguete («mini-LLM»: no presentarlo como transformer ni LLM a escala); completar, modificar corpus u opción de generación, explicar una limitación. Contenido de E2. |
| 46 (E1) | Ningún contenido durante el control; después, intro a prompting | Control individual en Colab de 45 min (interpretación + código acotado); alcance: mapa IA, pipeline, clasificación, `fit/predict`, neurona, pesos, red, `accuracy`. **No** incluye mini-LLM ni prompting. |
| 47 | Rol, tarea, contexto, formato, restricciones; iteración y verificación | Colab de registro: prompt inicial → respuesta real → mejora → nueva respuesta → juicio justificado. Código pequeño solo para organizar evidencia (no medir calidad por longitud). |
| 48 (E2) | Ningún contenido durante el control; después, intro a ética | Conversación real iniciada para la actividad, enlace compartido revisado, iteraciones y análisis individual + preguntas del mini-LLM. |
| 49 | Privacidad, sesgos, responsabilidad y 4D | Caso ficticio con código simple; decisión individual argumentada con las 4D. |
| 50 | Sin temario nuevo | Colab autocontenido de práctica sin nota. |
| 51 (E3) | Ninguno | Evaluación individual de 60–65 min (código breve, interpretación, prompting y decisión con 4D). |

**Evaluaciones:** definir puntajes y descriptores **antes** de generar ítems; no inventar ponderaciones; rúbrica parcelada con evidencia → nivel → razón → mejora; solucionario separado y **sin publicarlo** mientras haya recuperaciones. Conversión de puntajes a nota según la política del liceo (escala 2,0–7,0, exigencia 50% como el resto del curso, salvo que Diego indique otra cosa).

## 7. Pendientes abiertos (no bloquean N°42–43)

- **Edades, consentimiento y acceso a ChatGPT** de los estudiantes (v2 §7); bloquea el uso real de N°47 y E2 (N°48), no la preparación con datos ficticios.
- **Contingencia de E2** y **canal de entrega** de la conversación compartida.
- **Marco 4D**: denominaciones y definiciones exactas (el contexto de asesoría las lista como AI Fluency: Delegación, Descripción, Discernimiento, Diligencia); confirmar con Diego antes de redactar rúbricas.
- **Caso real de ética** (el contexto proponía 2 globales + 1 local).
- **Política de recuperación** por ausencias y tratamiento de pendientes.
- **Cantidad real de estudiantes** (el «15» es un tope estimado).
- Si hay clases en diciembre y qué pasa con Picuino N°29–33 (en pausa).
- **Herramientas del proyecto aún con «Propósito»:** `disenar-clase/SKILL.md` conserva la plantilla de spec antigua; actualizarlo cuando Diego lo decida. (El generador del PPT y el del Colab ya aceptan «¿Por qué lo veremos?»: el PPT rotula así el recuadro del slide de Objetivo; hecho el 2026-10-31.)
- ✅ La etapa de N°41 ya está en GitHub (2026-10-31). Recordar que el repo es público y que el HTML contiene las respuestas de las actividades y los códigos.
- **Carpeta que no se pudo borrar:** `clases/clase-41-mapa-ia-pipeline/fuentes/_slides/` quedó con un permiso bloqueado (la creó Edge al exportar diapositivas); está en el `.gitignore` de `fuentes/` y `construir.py` ya no la usa (escribe en la carpeta temporal del sistema). Diego puede borrarla desde el Explorador de archivos.
- **Link de Colab de la N°41:** https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-41-mapa-ia-pipeline/Clase%2041%20-%20Mapa%20IA%20-%20Clase.ipynb

## 8. Checklist trazable

| ID | Tarea | Estado |
|---|---|---|
| P1 | Plan v3 con sección de integración (v2 intacto) | ✅ |
| P2 | Spec N°41 | ✅ aprobada |
| P3 | HTML interactivo N°41 | ✅ desplegado |
| P4 | Colab guía N°41 con link al hub | ✅ generado (Diego lo sube) |
| P5 | Guía Docente Voz N°41 | ✅ |
| P6 | Sitio-hub `clases-ia-mario-bertero` en Vercel | ✅ producción |
| P7 | Gate N°41 → commit/push de la carpeta | ✅ 2026-10-31 (link de Colab abajo) |
| — | PPT paso a paso del pipeline (pedido por Diego) | ✅ |
| P8 | Spec N°42 | ☐ **siguiente** |
| P9 | Colab + Solucionario N°42 (`Escríbelo tú`, pistas, `check_*`) | ☐ |
| P10 | Guía Docente Voz N°42 + gate + push | ☐ |
| P11 | Spec N°43 | ☐ |
| P12 | Colab + Solucionario N°43 (neurona, LaTeX, `check_*`) | ☐ |
| P13 | Guía Docente Voz N°43 + gate + push | ☐ |
| P14 | `Historial-Curricular.md` (41–51) | ✅ filas agregadas; actualizar estado al cerrar cada clase |
| P15 | Memorias (criterio de la voz, sin Propósito, proyecto noviembre) | ✅ |
| P16 | Actualizar `disenar-clase` y `generar-ppt-clase` (sin Propósito) | 🟡 `generar-ppt-clase` ✅ (2026-10-31, probado con una spec real); `disenar-clase/SKILL.md` ☐ cuando Diego lo decida |
| P17 | Rúbricas E1/E2/E3, contingencia de E2, 4D, caso de ética | ☐ (v2 §9, ítems A, B, D) |

## 9. Cierre de etapa (recordatorio del `CLAUDE.md`)

Tras cada gate aprobado: guardar estado → `git add "clases/clase-NN-tema/"` (y `sitio-hub/` si cambió) → `git commit` → `git push` (**solo con autorización de Diego**, nunca `-A` ni `.`) → entregar el link de Colab (`https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-NN-tema/<Archivo%20con%20%20%20espacios>.ipynb`) → decir literalmente *«Cierre de etapa: te recomiendo ejecutar `/compact` ahora antes de seguir, para mantener el contexto limpio. Cuando quieras, lo corres y seguimos.»*
