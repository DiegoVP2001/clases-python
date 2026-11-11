# Noviembre IA · 3ro medio — Checklist y traspaso entre sesiones

**Actualizado:** 2026-11-04 (Clase 42 lista y publicada: ver «Estado Clase 42») (ajustes de la Clase 41 tras usarla: ver «Avance de actividades»). **Para quién:** la próxima sesión de Claude Code que diseñe la **Clase 42** (y las siguientes). Léelo completo antes de proponer nada.

## 0. Cómo partir (orden de lectura)

1. Este archivo.
2. `Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` → §3 (calendario), §5 (condiciones de los Colabs), §6 (evaluaciones) y **§10** (integración con el proyecto; manda sobre el v2 donde difieran).
3. `clases/clase-41-mapa-ia-pipeline/` como **modelo de referencia**: `Clase 41 - Mapa IA - Spec.md` (formato de spec), `Historial.md`, `Guía Docente Voz.md`, `fuentes/` y `generar_clase.py`.
4. `CLAUDE.md` raíz del proyecto: reglas 2, 7, 8, 13, 14, 15, 21 y 24, y la sección «Bloque IA de noviembre».
5. Según el flujo de `disenar-clase`: **confirmar el contexto con Diego y ofrecerle 3-4 actitudes para que elija una** antes de redactar objetivo (no asumir la actitud).

## 1. Estado de las clases

| N° | Fecha | Tema | Estado |
|---|---|---|---|
| **41** | lun 2 y mar 3-nov | Mapa de la IA + pipeline | ✅ Aprobada por Diego y **desplegada** (https://clases-ia-mario-bertero.vercel.app/clase-41/). **Pusheada a GitHub el 2026-10-31** (commits `13cc600` y `a9e2c86`). |
| **42** | jue 5-nov | Primer clasificador ML | ✅ **Spec, Colab, Solucionario, Guía Voz y slides animadas listos y pusheados (2026-11-04).** Siguiente: N°43. |
| **43** | lun 9-nov | Construir una neurona | ✅ **Aprobada por Diego y publicada (2026-11-04):** Colab, Solucionario, Guía del colega y página pusheados y desplegados; Ticket PPT solo local. Ver «Estado Clase 43». |
| **44** | mar 10-nov | La computadora ajusta sola: una neurona con `fit`/`partial_fit`, más datos, `accuracy` | ☐ Por diseñar. Brief en «Estado Clase 43». |
| 45 | jue 12-nov | Mini-LLM (generador de juguete; se evalúa en E2) | ☐ |
| 46 | lun 16-nov | Prompting con ChatGPT | ☐ (bloqueada por permisos/edad, ver §7) |
| — | mar 17-nov | **Sin clase** (ausencia docente) | — |
| 47 | jue 19-nov | **E1** (45 min, alcance 41–44) + revisión | ☐ |
| 48 | lun 23-nov | Prompting: conversación real e iteración | ☐ (bloqueada por permisos/edad y contingencia) |
| 49 | mar 24-nov | Repaso de mini-LLM y prompting + intro a ética | ☐ |
| 50 | jue 26-nov | **E2** (45 min) + revisión | ☐ |
| 51 | lun 30-nov | Ética y 4D | ☐ (necesita las definiciones 4D: ver §7) |
| 52 | mar 1-dic | Integración (práctica sin nota) | ☐ |
| 53 | jue 3-dic | **E3** (60–65 min) | ☐ |

> ⚠️ **CALENDARIO v6 (2026-11-10) SUPERA ESTA TABLA, LA v4 Y LA v5** (ver sección «Calendario v6» al final).

> (Nota histórica) **CALENDARIO v5 (2026-11-07) SUPERABA ESTA TABLA Y LA v4.** Ver la sección «Calendario v5 y reajuste de contenido (2026-11-07)» al final de este archivo: el jueves 12 no hay clase, entra la N°42b (tabla → listas), la N°43 se rehace como «v2» (la computadora aprende sola con `fit`) y las evaluaciones pasan a 2 pruebas de 60 min. La tabla de arriba se conserva solo como historial.

**Calendario v4 (2026-11-04, acordado con Diego): las evaluaciones van siempre los jueves; se agregó la N°44 «la computadora ajusta sola» y el resto se corrió (E1 jue 19, E2 jue 26, E3 jue 3-dic; último día para notas: 10-dic; feriados no verificados). Esta tabla manda sobre las fechas del plan v3.** La numeración 41–53 sigue la del `Historial-Curricular.md` (el N°41 antiguo, evaluación Funciones+Strings+Listas, quedó eliminado el 2026-10-07 y el número se reutilizó). Las filas 42–51 **ya están en el Historial** como «Por diseñar».

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
- **Avance de actividades (cambia desde 2026-11-03):** ya no hay código por actividad; completar bien una abre la siguiente. Única contraseña: la del ticket de salida (N°41 = 725). El esquema (mapa/pipeline) queda fijo arriba en una franja. El juego de apertura está oculto (`JUEGO_ACTIVO = false`). M2 es de filas fijas, sin arrastre.
- **ChatGPT Voice como colega** (criterio completo en la memoria `feedback-voz-codocente-chatgpt-criterio`): solo habla cuando Diego la activa («Colega, …»); **bienvenida** (espera el saludo del curso y pide que alguien lea el objetivo), **Haz Ahora** y **verificación de comprensión del contenido nuevo**; **no es protagonista** en práctica guiada, independiente ni cierre. Cada clase lleva su `Guía Docente Voz.md` (prompt de arranque, tabla momento → frase de activación → qué dice → plan B, y aviso de silenciar el micrófono entre intervenciones).
- **Ejemplos genéricos:** no afirmar que un producto concreto usa una técnica sin evidencia (v2 §4).

## 3. Cómo se produjo la N°41 (patrón a reutilizar)

Carpeta `clases/clase-41-mapa-ia-pipeline/`:

| Archivo | Para qué | Cómo se regenera |
|---|---|---|
| `Clase 41 - Mapa IA - Spec.md` | Contrato aprobado | A mano, con aprobación de Diego |
| `fuentes/diagramas.py` | Diagramas SVG (mapa y pipeline) y helpers (`tira`, `tabla`, `bloque_*`) | Editar y correr `construir.py` |
| `fuentes/diapositivas.py` | 14 diapositivas del pipeline + notas | Ídem |
| `fuentes/plantilla_interactivo.html` | HTML interactivo (3 páginas, 8 actividades en cadena, solo el ticket con código en `CODIGOS`) | Ídem |
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

> ⚠️ **Numeración y fechas superadas por el calendario v4 (2026-11-04):** el contenido de cada fila sigue vigente, pero la tabla de arriba (§1) manda. Equivalencias: «44 `MLPClassifier` + `accuracy`» → N°44 «la computadora ajusta sola» (martes 10-nov, una sola neurona); «45 mini-LLM» → jue 12-nov; «46 E1» → N°47 (jue 19-nov); «47 prompting» → N°46 y N°48; «48 E2» → N°50 (jue 26-nov); «49 ética y 4D» → N°51; «50 integración» → N°52; «51 E3» → N°53 (jue 3-dic).

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
| P8 | Spec N°42 | ✅ |
| P9 | Colab + Solucionario N°42 | ✅ |
| P10 | Guía Docente Voz N°42 + gate + push | ✅ |
| P11 | Spec N°43 | ✅ aprobada |
| P12 | Colab + Solucionario N°43 (neurona, LaTeX, `check_*`) | ✅ aprobados y publicados |
| P13 | Guía Docente Voz N°43 + gate + push | ✅ 2026-11-04 |
| P14 | `Historial-Curricular.md` (41–51) | ✅ filas agregadas; actualizar estado al cerrar cada clase |
| P15 | Memorias (criterio de la voz, sin Propósito, proyecto noviembre) | ✅ |
| P16 | Actualizar `disenar-clase` y `generar-ppt-clase` (sin Propósito) | 🟡 `generar-ppt-clase` ✅ (2026-10-31, probado con una spec real); `disenar-clase/SKILL.md` ☐ cuando Diego lo decida |
| P17 | Rúbricas E1/E2/E3, contingencia de E2, 4D, caso de ética | ☐ (v2 §9, ítems A, B, D) |

## 9. Cierre de etapa (recordatorio del `CLAUDE.md`)

Tras cada gate aprobado: guardar estado → `git add "clases/clase-NN-tema/"` (y `sitio-hub/` si cambió) → `git commit` → `git push` (**solo con autorización de Diego**, nunca `-A` ni `.`) → entregar el link de Colab (`https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-NN-tema/<Archivo%20con%20%20%20espacios>.ipynb`) → decir literalmente *«Cierre de etapa: te recomiendo ejecutar `/compact` ahora antes de seguir, para mantener el contexto limpio. Cuando quieras, lo corres y seguimos.»*

## Estado Clase 42 (2026-11-04)

- Slides animadas: https://clases-ia-mario-bertero.vercel.app/clase-42/ (`sitio-hub/clase-42/`), enlazadas en el Colab. Patrón replicable para N°43+: pestañas por clase + resumen animado que muestre también la deficiencia del modelo.
- Colab: 0/1 de las etiquetas lo elegimos nosotros; recuadro «Ojo»: corte en 4 km vs regla real 5 km = falta de datos cerca del corte (con días en 4 y 4,5 km pasa a 4,75). Train/test se aborda después (el `fit` usa todos los datos).
- Pendientes: pestañas en `sitio-hub/clase-41/`; `Ticket de Salida.pptx` de la 42 está solo local (se subió por error en 604a217 y se retiró en 976dadc; sigue en el historial público).

## Estado Clase 43 (2026-11-04)

- Carpeta `clases/clase-43-neurona/`: Spec v2 (aprobada), `generar_clase.py`, `Clase.ipynb`, `Solucionario.ipynb`, `Guía Docente Voz.md` (el colega del profesor), `Historial.md`, `diagramas/` y `Ticket de Salida.pptx` (solo local). Página `sitio-hub/clase-43/index.html` (10 slides: recordatorio, paso a paso, laboratorio con entrenamiento/prueba, tus pesos vs. los de la computadora, escala) y pestaña/tarjeta en `clase-42/` e `index.html`. **Aprobada por Diego y publicada el 2026-11-04 (GitHub + Vercel); el `Ticket de Salida.pptx` queda solo local hasta después de dictar la clase.**
- Decisiones de Diego: objetivo «Crear nuestra primera inteligencia artificial: una neurona, con asombro.»; actitud asombro; historia de las **colmenas**; el «¿Por qué lo veremos?» lo dice el **colega del profesor**; Haz Ahora enfocado en automatizar algo que no conocen (qué patrones revisarían); **recordatorio puente** ayer → hoy → próxima clase; **caja lista primero** (iterar desde el inicio); evaluador **preparado** (programan la neurona, no los errores; justifican); **entrenamiento y prueba** siempre; desafío = mejor combinación en un set de 12 días con un día raro (11 de 12 es el máximo; verificado) y luego prueba; sin perceptrón/Nobel/mosca.
- Reglas guardadas en `disenar-clase/SKILL.md` («Reglas vigentes desde 2026-11-04») y en la memoria (no en `CLAUDE.md`).
- Cómo se publicó (y cómo repetirlo si se edita): `git add "clases/clase-43-neurona/"` (sin el `Ticket de Salida.pptx`) y `sitio-hub/` + commit con pathspec + push (con autorización) y `npx vercel deploy --prod --yes --scope diegovp2001` desde `sitio-hub/` (el Colab enlaza `https://clases-ia-mario-bertero.vercel.app/clase-43/`).
- Pendientes: confirmar OAs (propuestos OA1, OA3 | OAd; Diego aprobó la clase sin confirmarlos explícitamente); pestañas en `sitio-hub/clase-41/`; diseñar la N°44.

### Brief para la N°44 (mar 10-nov) — la computadora ajusta sola

- Mismas colmenas con **más datos** (p. ej., ~40 días). `MLPClassifier(hidden_layer_sizes=(), activation="logistic")` **es una sola neurona** (verificado: `coefs_` de forma (3, 1), `predict` coincide con `z >= 0`). `.fit()` con `solver="lbfgs"` da pesos ≈ `[3,77, −3,83, −9,53]` y sesgo ≈ `−45,2` con las colmenas de la 43 (8 de 8; 3 de 4 en la prueba; falla el mismo día que la neurona a mano).
- **Ver el entrenamiento paso a paso:** `partial_fit` con `solver="sgd"` y datos escalados; con `learning_rate_init=0.1` los aciertos suben de 4 a 7 de 8 en ~100 vueltas y a 8 de 8 en ~3.000 (con 0,01 es mucho más lento: buen ejercicio de «cambia un número y mira»). Los pesos de ese modo están en datos escalados: no comparar numéricamente con los de mano; comparar con la versión `lbfgs`.
- **`accuracy` = aciertos / total evaluado** en la prueba, calculada por los estudiantes con un `for`.
- **`hidden_layer_sizes`:** mencionarlo como el argumento que define cuántas neuronas más; su valor se decide por **prueba y error** y hoy existen sistemas complejos que **automatizan esa búsqueda**; en línea con la N°43 **seguimos con una sola neurona** (`()`). Con `(3,)` el caso «calor o néctar pero no ambos» pasa de 2 a 4 de 4 (verificado): opcional como curiosidad, no como contenido.
- Matiz honesto: la neurona de scikit-learn entrena con activación logística (suave) y predice con la misma regla `z >= 0` que nuestro escalón.
- Aplicar las reglas de `disenar-clase`: recordatorio puente (ayer = neurona a mano, hoy = la computadora ajusta, después = …), entrenamiento y prueba, colega del profesor, caja lista primero.

## Calendario v5 y reajuste de contenido (2026-11-07)

**Origen:** entrevista con Diego tras la N°42. Diagnóstico: el curso entendió *crear → entrenar → evaluar*, pero **no qué significa cada coma dentro de un corchete ni cada grupo de corchetes**; y la N°43 (v1) parte ajustando pesos a mano, cuando el mensaje de Diego es **dejar que la computadora aprenda los patrones de los datos**. Prefiere consolidar a avanzar por avanzar. Plan completo: `C:\Users\diego\.claude\plans\necsito-hacer-una-o-vast-mochi.md`.

### Calendario v5 (manda sobre v3 y v4)

| Fecha | N° | Contenido | Estado |
|---|---|---|---|
| lun 9-nov | **42b** | De la tabla a las listas (wifi del liceo) | ☐ |
| mar 10-nov | **43 v2** | Neurona con `fit`/`predict`/`accuracy` + «está ponderando» + desplegable árbol vs. neurona | ☐ (la v1 queda intacta, sin dictar) |
| jue 12-nov | — | **Sin clase** | — |
| lun 16-nov | 44 | Mini-LLM **o** prompting (decide Diego: checkpoint C1) | ☐ |
| mar 17-nov | — | Sin clase (ausencia docente) | — |
| jue 19-nov | 45 | **Prueba 1** (60 min, ML) + revisión en clase | ☐ |
| lun 23-nov | 46 | Prompting (o mini-LLM) | ☐ |
| mar 24-nov | 47 | Segundo tema de IA si se mantienen ambos (C1) | ☐ |
| jue 26-nov | 48 | Ética y 4D | ☐ |
| lun 30-nov | 49 | Integración / colchón (según C1) | ☐ |
| mar 1-dic | 50 | Colchón | ☐ |
| jue 3-dic | 51 | **Prueba 2** (60 min) + revisión en clase | ☐ |

Feriados sin verificar. La N°44 antigua («la computadora ajusta sola») queda **absorbida por la 43 v2**. Sin clases de ejercitación.

### Decisiones nuevas (no reabrir sin que Diego lo pida)

- **42b:** una sola clase nueva, sin ponderar ni if/else, recordando que el ML encuentra patrones solo. **Las listas se escriben a mano** copiando del cuaderno (tabla en markdown): se muestra la estructura (`[dato1, dato2, dato3]` por fila; filas separadas por coma y envueltas en otro corchete), **sin índices, sin `for`/`append`, sin slicing**. Enfoque intuitivo, no automatizable.
- **Elección de columnas:** en la 42b eligen 3 de 6 (3 claras, 2 medias, 1 sin relación). Desde ahí, cada clase dice «el problema tenía X columnas, pero [personaje] les pide trabajar con estas Z».
- **Regla de datos:** filas divisibles por 5; por defecto **20 = 16 *train* (las primeras) + 4 *test* (las últimas)**, nombres en inglés. El split lo hacen a mano. Se formaliza en código el «esto debería dar 1/0»: se predice el *test* y se cuenta con `accuracy_score`.
- **43 v2:** sin ajuste manual de pesos; `MLPClassifier(hidden_layer_sizes=())` desde el inicio; al final «abrir la caja» (`coefs_`, `intercepts_`) para mostrar que pondera; desplegable corto con la receta árbol vs. neurona para copiar y pegar.
- **Slides animadas en Vercel en cada clase** (inicio / durante / después del contenido nuevo).
- **Evaluaciones:** 2 pruebas de 60 min revisadas en clase = 2 notas directas (reemplaza E1/E2/E3). Prueba 1 = ML (tabla → elegir 3 columnas → split → árbol y neurona con `crear-fit-predict-accuracy` → cuál es mejor y por qué; con pocos días de *test*, un acierto de diferencia dice poco). Prueba 2 = lo que quede (+ ética).
- **Mini-LLM vs. prompting:** decide Diego más adelante (C1, a más tardar jue 12). **Ética sí va.**

### Checklist v5

| ID | Tarea | Estado |
|---|---|---|
| R1 | Este traspaso actualizado | ✅ 2026-11-07 |
| R2 | `Historial-Curricular.md`: filas 42b y 43 v2 | ✅ 2026-11-07 |
| R3 | `disenar-clase/SKILL.md`: reglas nuevas (columnas, sin ajuste a mano, split, slides, filas, Revisar, slides por concepto, ticket al Form) | ✅ 2026-11-08 (reglas 1-11) |
| R4 | Memorias de feedback y de proyecto | ✅ 2026-11-08 |
| R5 | `CLAUDE.md`: sección «Bloque IA» (calendario v5, molde, slides por concepto, ticket) | ✅ 2026-11-08 |
| A1 | Dataset micro 20×6 verificado | 🟡 en búsqueda |
| A2 | Spec 42b → gate | 🟡 Spec v1 escrita, falta gate de Diego |
| A3 / A3b | Colab + Solucionario + Guía + slides 42b → gate | ✅ aprobado por Diego 2026-11-08 |
| A4 | Push + deploy 42b (antes del lun 9) | ✅ 2026-11-08 |
| B1 | Dataset colmenas 20 filas verificado | ☐ |
| B2 | Spec 43 v2 → gate | ☐ |
| B3 / B3b | Colab v2 + Solucionario v2 + Guía + slides v2 → gate | ☐ |
| B4 | Push + deploy 43 v2 (antes del mar 10) | ☐ |
| C1 | Diego decide mini-LLM / prompting | ☐ |
| E1 / E2 | Prueba 1 y Prueba 2 (puntajes y descriptores antes de los ítems) | ☐ |

## Estado al cierre de sesión (2026-11-08) — léelo primero

**✅ N°42b «De la tabla a las listas» (lun 9-nov): aprobada por Diego, pusheada y desplegada.**
- Carpeta `clases/clase-42b-tabla-a-listas/`: Spec v3, `Clase.ipynb`, `Solucionario.ipynb`, `Guía Docente Voz.md`, `Historial.md`, `Ticket de Salida Respuestas.json` (D, B, C, A), `generar_clase.py`, `construir_slides.py`, `crear_ticket_ppt.py`, datos verificados (`datos_*.json`) y `diagramas/`.
- Colab: https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-42b-tabla-a-listas/Clase%2042b%20-%20De%20la%20Tabla%20a%20las%20Listas%20-%20Clase.ipynb
- Slides (11, una por concepto): https://clases-ia-mario-bertero.vercel.app/clase-42b/ · regenerar con `py -3 construir_slides.py` y desplegar desde `sitio-hub/`.
- **`Ticket de Salida.pptx` de la 42b está SOLO local** (no se pushea hasta después de dictar la clase; repo público). Pendiente de Diego: subirlo al repo tras el lunes 9 si quiere.
- Dataset wifi 20×6 (semilla 16393): fila a fila en `datos_wifi_verificados.json`; trío elegido por la clase = dispositivos, video, horas desde reinicio; árbol `max_depth=3`, 4/4 en el test.

**Reglas nuevas de Diego que valen para toda clase siguiente** (están en `disenar-clase/SKILL.md` 1–11, en el `CLAUDE.md` y en la memoria):
1. La computadora aprende sola (sin ajuste manual); 2. listas tipeadas a mano, sin índices/`for`/slicing; 3. 20 filas = 16 *train* + 4 *test*; 4. «el problema tenía X columnas, el personaje pide estas Z»; 5. **«filas» / «filas de datos», nunca «bloques»**; 6. todo el ICN con el ejemplo del escenario de la clase (nada de ejemplos ajenos); 7. concepto final «Revisar» (dos viñetas: leer el árbol con *features* + ver la precisión) y detalles de hiperparámetros en un `<details>` oculto; 8. la guiada es el único ejercicio obligatorio, los demás son extras; 9. **una slide animada por concepto del ICN** + partes del Haz Ahora + «Para pensar» + resumen en viñetas, rotuladas «Concepto N del cuaderno»; 10. **el Colab termina con el link al Google Form del ticket y NUNCA trae las preguntas** (van en el PPT del ticket y el Solucionario); 11. etiqueta binaria definida en el Haz Ahora con la pregunta del personaje (1 = sí, 0 = no).

**Lo siguiente (orden):**
1. **N°43 v2 — «La neurona aprende sola»** (mar 10-nov). Spec v2 no escrita aún. Usar la 42b como molde: misma tabla→listas→train/test→receta, cambiando una línea (`MLPClassifier(hidden_layer_sizes=(), activation="logistic", solver="lbfgs", random_state=0)` = una neurona); «abrir la caja» con `coefs_`/`intercepts_` (pondera: $z = w_1x_1 + w_2x_2 + w_3x_3 + b$; el calor suma, el viento y la lluvia restan); desplegable final árbol vs. neurona (`crear→fit→predict→accuracy` en ~10 líneas). **Dataset nuevo de las colmenas: 20 filas (16/4) y 5–6 columnas con 3 usadas, por diseñar y verificar** (que `lbfgs` converja sin escalar, que los signos se lean bien y que árbol y neurona no den lo mismo en el test). Archivos con sufijo `v2` en `clases/clase-43-neurona/` (la v1 queda archivada y su página sigue en línea). Slides en `sitio-hub/clase-43-v2/` (una por concepto), Ticket al Form + PPT local + JSON de respuestas. Nombres de las *features* en el mismo orden que las columnas.
2. **C1 (jue 12 como máximo):** Diego decide mini-LLM, prompting o ambos para el lun 16.
3. **Prueba 1** (jue 19-nov, 60 min): puntajes y descriptores antes de los ítems; no pedir elegir columnas desde cero, sino justificar un trío dado.
4. Prueba 2, ética y 4D (pendientes de A, B, D del v2).

**Trampas técnicas nuevas:** en este equipo las herramientas de Bash/PowerShell en heredocs de Python pueden mal-interpretar `\n`: escribir scripts con la herramienta de archivos y ejecutarlos; la consola de Windows necesita `PYTHONIOENCODING=utf-8` para imprimir emojis; el `.gitignore` ya excluye `__pycache__`.


## Calendario v6 (2026-11-10) — manda sobre v3, v4 y v5

**Origen:** lun 30-nov y mar 1-dic no hay clase (se rinde la PAES). Se acorta el calendario; Diego quiere 2 notas: **Prueba 1 técnica** y **Prueba 2 ética y análisis**. Aprobado por Diego.

| Fecha | N° | Contenido | Bloque |
|---|---|---|---|
| mar 10-nov | 43 v2 | Neurona; **modificada**: mismo pipeline del árbol (wifi), BBDD ya cargada, solo cambia el modelo y su análisis | Técnico |
| jue 12-nov | — | Sin clase | |
| lun 16-nov | 44 | **Mini-LLM** (contenido nuevo simple y al grano: tokens, predicción de la siguiente palabra) | Técnico |
| mar 17-nov | — | Sin clase (ausencia docente) | |
| jue 19-nov | 45 | **Prueba 1: técnica** (60 min) + revisión en clase | |
| lun 23-nov | 46 | **Prompting** (usar y evaluar bien una IA) | Análisis |
| mar 24-nov | 47 | **Ética y 4D** | Ético |
| jue 26-nov | 48 | **Análisis de casos** + repaso (colchón y ensayo de la Prueba 2) | Análisis |
| lun 30-nov / mar 1-dic | — | Sin clase (PAES) | |
| jue 3-dic | 49 | **Prueba 2: ética y análisis** (60 min) + revisión en clase | |
| hasta 10-dic | — | Último día para ingresar notas | |

**Decisiones:** C1 resuelto → mini-LLM el 16, prompting el 23. Prueba 1 = clases 41–44 (pipeline, listas, train/test, fit/predict/accuracy, neurona, pocos ítems de mini-LLM). Prueba 2 = clases 46–48, por casos; Diego quiere que se rinda **promptando a ChatGPT y entregando links de compartir** (pendiente de diseñar). Entregables pedidos: Colab de clases técnicas restantes (43 modificada + 44), Colab de prompting + ética/4D + análisis de casos, y borradores de ambas pruebas con solución.

### Entregables de la sesión del 2026-11-10 (Calendario v6)

- **Prueba 1 técnica** (`clase-45-prueba-1-tecnica/`): `Prueba.ipynb`, `Solucionario.ipynb`, `Temario.tex/.pdf` (1 plana, oficio), `generar_pruebas.py` (fuente de verdad; también genera la Prueba 2). Base piscina (20×6 numéricas), árbol 1.0 / neurona 0.75 / árbol con otras columnas 0.5. Imports en la primera celda.
- **Prueba 2 prompting y ética** (`clase-49-prueba-2-prompting-etica/`): `Prueba.ipynb`, `Guía de Corrección.ipynb`, `Temario.tex/.pdf`. Caso único: reconocimiento facial; partes A y B con ChatGPT, C sin IA con texto fijo y fallas intencionales.
- **Prompts para diseñar las clases:** `clase-43-neurona/Prompt v2.md` (hoy), `clase-44-mini-llm/`, `clase-46-prompting/`, `clase-47-etica-4d/`, `clase-48-analisis-casos/`.
- **No se pushea nada de las pruebas hasta después de rendidas** (repo público): P1 después del jue 19-nov, P2 después del jue 3-dic. Los temarios sí se pueden entregar antes.
- **Pendientes:** alinear las 4 partes del prompt con la Clase 46 y las 4D con la 47 (§7); (✅ hecho 2026-11-11: Parte D de P1 alineada con la 44) decidir si se muestran `coefs_` en la 43 v2 (ver su Prompt).


## Estado Clase 44 (2026-11-11) — cierre de etapa

**✅ N°44 «Cómo funciona ChatGPT» (lun 16-nov): Colab, Solucionario y slides aprobados por Diego y publicados** (commit a GitHub + deploy a Vercel).
- Carpeta `clases/clase-44-mini-llm/`: `Spec.md` (v2 + ajustes v3/v4 en su encabezado), `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json` (C, D, B, A), `generar_clase.py`, `construir_slides.py`, `crear_ticket_ppt.py`, `Historial.md`. **`Ticket de Salida.pptx` queda SOLO local** (repo público; se sube después de dictar la clase).
- Colab: https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-44-mini-llm/Clase%2044%20-%20Mini%20LLM%20-%20Clase.ipynb · Slides: https://clases-ia-mario-bertero.vercel.app/clase-44/ (8 slides, `sitio-hub/clase-44/`).
- **Estructura (4 conceptos, sin programar: solo se ejecutan celdas):** 1 LLM = *Large Language Model* y **estocástico** · 2 tokens (fichas) · 3 **probabilidad y azar: la bolsa de fichas** (con bajada «las respuestas de un LLM son azarosas; el proceso para verlo es…»; palabra nunca vista = saca una ficha al azar entre las que sí conoce) · 4 **evidenciarlo en la práctica** (el profesor envía dos veces «Explica las diferencias entre ChatGPT, Claude y Gemini»). Práctica guiada = **réplica de la Parte D de la Prueba 1** (texto «hoy toca mate…», D1–D4, se responde a mano y se comprueba ejecutando). Ticket de 4 preguntas, una por concepto. Verificamos lo aprendido: 2 preguntas por concepto.
- **Decisiones de Diego (vigentes para el resto del bloque de IA):** (1) el término es **«estocástico»**, nunca «probabilístico»: sistema cuyo comportamiento no se puede predecir con total exactitud, o sea tiene azar; (2) **no separar** el mini modelo («determinístico») del LLM real: **todo es estocástico**; «determinístico» solo como contraste con la calculadora; (3) imagen única: **bolsa de fichas** (más fichas = más probable, sin garantía; «la más probable no es la segura»); (4) lo que responde un modelo depende del azar y de las probabilidades con que se entrenó; (5) se descartó el interactivo final; (6) sin referencias a la prueba dentro del Colab (solo el aviso de logística en el Cierre).
- **Alineación hecha (sin pushear):** `clase-45-prueba-1-tecnica/generar_pruebas.py` (D3 acepta «sí, pero al azar, sin base»; nota de alineación con la 44) y `clase-49-prueba-2-prompting-etica/` (rúbrica B2 y Temario con «estocástico»; PDF recompilado, 1 plana); `Prompt.md` de las clases 46 y 48 con el vocabulario de la 44.
- **Pendientes de la N°44:** Guía Docente Voz y confirmar OAs (propuestos OA1, OA3); dictar el lunes 16 y, después, subir el `Ticket de Salida.pptx`; el `Ticket de Salida - Trazabilidad` cuando haya respuestas del Form.
- **Siguiente:** repaso de la Prueba 1 y **Prueba 1** (jue 19; no se pushea hasta después de rendida) → N°46 prompting (lun 23) → N°47 ética y 4D (mar 24) → N°48 análisis de casos y repaso (jue 26) → **Prueba 2** (jue 3-dic). Pendientes abiertos (§7): alinear las 4 partes del prompt con la 46 y las 4D con la 47.
