# Rúbricas y Evaluación — Proyecto Cierre Octubre (v5)

> **v5 — 2026-10-20 (giro plug-and-play).** Reemplaza a `clases-octubre/Rúbricas y Evaluación - Proyecto Cierre Octubre.md` (v4, 2026-10-19), que queda como registro. Cambios: **§4** «Archivo usable» pasa a **«Conoce su base»** (5 pts por el mínimo + 10 por la originalidad de las preguntas) y se agrega el mapa de dónde se corrige cada criterio en los cuadernos de Código y de Texto; **§6** los errores de la Defensa van en los espacios de la receta y en la receta; **§7** hitos de Proceso con la 37b como **nota de progreso**; **§11** equipos y bases. Las partes no mencionadas (§1-§3, §5, §8, §9) no cambian. Lo marcado **(propuesta)** está por confirmar con Diego. Versión para estudiantes: `Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb`.

> **Sesión A del orden de planificación pendiente** (`Proyecto Cierre Octubre - Plan y Pendientes.md` §7, orden 1). Cierra: pesos y rúbrica de las 4 notas, política de IA, logística de la defensa técnica, uso de auto/co/heteroevaluación, y evidencia individual vs. grupal. Sesión del 2026-09-23.
>
> **ACTUALIZADO 2026-10-19 (Calendario v4):** §5 (Presentación: 6 diapositivas, 7 min fijos) y §6 (Defensa técnica: 30 min, en parejas, 4 secciones) fueron reescritas. El factor individual de §9 se extiende ahora también a la Defensa. Ver `Calendario v4 - Proyecto Cierre Octubre.md`.
>
> **No fija fechas ni calendario propio, salvo donde se indica explícitamente.** La Sesión 2 (calendario definitivo) ya cerró el 2026-09-23 usando este documento como insumo — ver `Plan y Pendientes.md` sección 3 para las 14 fechas. Este documento se actualizó en dos puntos con la fecha ya resuelta: §6 (Defensa técnica → 26-oct, con corte de tiempo) y §10.

## Cómo se usa este documento

1. **§1 Consolidación y pipeline de nota** — cómo las 4 notas se combinan en una sola.
2. **§2 Pesos de las 4 notas.**
3. **§3 Mapeo de criterios** (Catastro §8) a las 4 notas — con qué quedó cerrado y por qué.
4. **§4-§7 Detalle de cada nota** — componentes, puntaje, descripción.
5. **§8 Política de IA.**
6. **§9 Mecanismos transversales** — factor individual, retro formativa, buzón, ausencias.
7. **§10 Pendiente explícito, para después.**

---

## 1. Consolidación y pipeline de nota

Las 4 notas se combinan en una sola **"Nota de Proyecto"**, registrada con **peso 2** en el promedio semestral (vale el doble de una evaluación normal — coherente con que el proyecto ocupa ~7 sesiones, no una).

**Pipeline de cálculo:**
1. Cada una de las 4 notas se puntúa sobre **100 pts** de forma independiente.
2. Se combinan con los pesos de §2 → un puntaje único sobre 100.
3. Se aplica **exigencia 50%** una sola vez, sobre el puntaje combinado → nota final **2.0-7.0**.

La exigencia no se aplica nota por nota — solo al final, sobre el resultado ya ponderado.

---

## 2. Pesos de las 4 notas

| Nota | Peso | Carácter |
|---|---|---|
| **Producto — Colab narrado** | 35% | Grupal (+ factor individual, ver §9) |
| **Presentación** | 20% | Individual dentro del grupo (ronda de preguntas) |
| **Defensa técnica — código intervenido** | 30% | Grupal (pareja) + factor individual — v4 |
| **Proceso — bitácora e hitos** | 15% | Grupal (+ factor individual, ver §9) |

**Por qué esta distribución:** Presentación + Defensa técnica (individuales) suman 50%, igual que Producto + Proceso (grupales) — da tanto peso a la responsabilidad individual como al trabajo colectivo, coherente con el objetivo central del proyecto contra el mal uso de IA (Defensa técnica es la nota más alta después de Producto, precisamente porque es la más difícil de falsificar). Proceso queda con el menor peso porque, tras acotar su alcance, mide cumplimiento más que profundidad analítica — el freno real contra la improvisación de último minuto es la Defensa técnica, no el peso de Proceso.

---

## 3. Mapeo de criterios (Catastro §8) a las 4 notas — CERRADO

Los 9 criterios del inventario abierto quedan así:

| # | Criterio (Catastro §8) | Nota | Dónde vive |
|---|---|---|---|
| 1 | Formular pregunta respondible + descartadas | Proceso | Bitácora |
| 2 | Archivo crudo usable | Producto | Colab |
| 3 | Operación justificada | Producto | Colab |
| 4 | Evidencia que responde la pregunta | Producto (+ Presentación, restatement oral) | Colab / diapos |
| 5 | Narrar el razonamiento por escrito | Producto | Colab |
| 6 | Traducir el hallazgo a lenguaje humano | Producto | Nota de prensa |
| 7 | Declarar límites del dato | Producto (escrito) + Presentación (oral) | Colab / diapos |
| 8 | Sostener conclusión ante audiencia | Presentación | Diapos + Q&A |
| 9 | Responder por el propio código | Defensa técnica | Instrumento propio |

**Decisiones que resuelven las dudas abiertas en Catastro §8:**
- **La nota de prensa NO es un instrumento de evaluación aparte** — es un componente más dentro de Producto (§5). Crear un 5° instrumento para algo que se corrige en el mismo acto de leer el Colab habría sido carga sin ganancia real de información.
- **Proceso mide solo lo que NO es visible en el Colab final** — cumplimiento de hitos, incorporación de feedback, la pregunta inicial y las descartadas. Evita duplicar corrección sobre el mismo markdown que ya se lee para calificar Producto.
- **Presentación es una restatement oral con función distinta, no una repetición redundante:** el contenido se solapa con el Colab a propósito — lo que se evalúa ahí no es "hicieron el análisis" (ya evaluado en Producto), sino "pueden comunicarlo y defenderlo en vivo, individualmente, ante audiencia real y bajo preguntas".

---

## 4. Producto — Colab narrado (100 pts, 35% del total) — v5

**Estructura: Colab (100 pts) + Nota de prensa (15 pts) = 115 pts, todavía sin normalizar** (ver §10). El Colab narrado son los dos cuadernos juntos: 🧑‍💻 Código + ✍️ Texto, que se unen por pareja.

| Criterio | Pts | Qué se evalúa |
|---|---|---|
| **Conoce su base** *(reemplaza a «Archivo usable»)* | 15 | Ver detalle abajo: **5 pts por el mínimo + 10 pts por una pregunta distinta**. |
| **Operación justificada** | 20 | Los pasos de la receta están contados **en palabras**, cada uno con **por qué responde la pregunta** (no solo qué hace el código). |
| **Evidencia construida** | 25 | El gráfico y las cifras del top responden efectivamente la pregunta y sostienen la conclusión; se citan **cifras de la tabla**. |
| **Narración completa** | 20 | Se lee como un documento coherente, **en este orden: pregunta → base → evidencia → límites → conclusión**, y cierra con una conclusión que responde la pregunta inicial. |
| **Límites del dato declarados** | 20 | Se dice por escrito qué NO se puede concluir, apoyado en un dato real de su tabla (filas perdidas, filas detrás de cada barra, promedio de promedios…), no en una frase de relleno. |
| **Nota de prensa** | 15 | Escrita como noticia real, con **titular, bajada, entrada, desarrollo y cierre** (modelo: la nota del LUN). Reutiliza lo escrito en las secciones 2 a 7 del cuaderno de Texto. **Sin versión corregida con IA (v5).** |

### Conoce su base (15 pts)

| Componente | Pts | Dónde se corrige | Qué se evalúa |
|---|---|---|---|
| **Mínimo** | 5 | Texto 2 · Código Paso 1 | Explica qué es una fila de su base, cuántas filas y columnas tiene, y qué columnas usó y con qué rol (🔎 filtrar · 🧺 agrupar · 🔢 resumir). |
| **Originalidad de las preguntas** | 10 | Texto 3 (un bloque por análisis) · Código (análisis) | Se mide la pregunta **más original que esté bien explicada**: qué la hace distinta del ejemplo de su base, qué encontró (con una cifra) y su límite. Pueden hacer todos los análisis que quieran copiando y pegando la receta; la cantidad no suma. |

Niveles de **Originalidad** *(propuesta)*:
- ✅ **10 pts:** la pregunta **cambia la comparación** respecto del ejemplo de su base (otra columna para filtrar, agrupar o resumir, otro tipo de resumen) **o** usa una columna fuera de las 5 sugeridas.
- ⚠️ **5 pts:** solo cambia un **valor** (otra comuna, otro año) o el `N`.
- ❌ **0 pts:** es el ejemplo tal cual.

**Reglas v5 (2026-10-20):**
- **Sin tope de análisis:** pueden copiar y pegar la receta las veces que quieran. **Cada análisis debe tener su bloque de preguntas en el Texto (sección 3); un análisis sin explicación no suma.**
- **Cuenta la calidad, no la cantidad:** los 10 pts se miden en la pregunta más original que esté bien explicada.
- **Análisis principal (⭐):** cada equipo marca el suyo. De él salen las diapositivas 3 a 5, la nota de prensa y los **3 errores de la Defensa**. Los demás análisis no afectan Evidencia, Límites ni Defensa.
- **Corrección acotada:** se corrigen el principal y el más original (pueden ser el mismo); los demás se leen sin puntaje.
- Quien se queda en las 5 columnas sugeridas y en el ejemplo cumple el mínimo (5 pts): no se castiga, solo no se premia. **Los ejemplos de la galería van plegados** en el cuaderno de Código; entregarlos tal cual vale 0 en originalidad.

### Dónde se corrige cada criterio

| Criterio | Cuaderno de Código | Cuaderno de Texto |
|---|---|---|
| Conoce su base | Paso 1 y análisis | Secciones 2 y 3 |
| Operación justificada | Paso 2 (receta) | Sección 3 («cómo lo investigamos») |
| Evidencia | Paso 2 (gráfico y cifras) | Sección 3 («hallazgo») |
| Narración completa | — | Todo, en orden (secciones 1 a 4) |
| Límites | Paso 3 | Sección 3 («límites») |
| Nota de prensa | — | Sección 5 |

**Por qué «Archivo usable» ya no está:** desde la v3 las bases llegan limpias (números ya como números, columnas derivadas ya calculadas), así que limpiar dejó de ser parte del proyecto. Quien limpió por su cuenta en la 37b queda reconocido en la nota de progreso (§7).

**Por qué el orden pregunta → base → evidencia → límites → conclusión es obligatorio:** es el mismo orden de la Presentación (§5): cada sección del cuaderno de Texto es una diapositiva, así que armar el PPT es pasar a diapositivas lo ya escrito.

---

## 5. Presentación (100 pts, 20% del total) — v4, 6 diapositivas, 7 min fijos

> **Actualizado 2026-10-19 (Calendario v4).** Reemplaza la estructura anterior de §5. Ante el curso y, si pueden asistir, miembros de la dirección. Cada criterio está atado a una diapositiva específica.

**Formato:** 7 min por equipo, sin preguntas después de cada uno. Las preguntas van al final del día, agrupadas: una pregunta dirigida por nombre a un integrante de cada equipo, más las de dirección si las hay. Cada integrante habla en al menos 2 diapositivas. Máximo ~25 palabras por diapositiva.

| N.º | Diapositiva | Tiempo | Criterio | Pts |
|---|---|---|---|---|
| 1 | Contexto, pregunta e hipótesis | 1:00 | *(sin nota — se califica en Proceso vía bitácora)* Qué fenómeno, por qué importa, qué esperaban encontrar. | — |
| 2 | Datos | 0:45 | *(sin nota)* Fuente, qué contiene la base, qué columnas usaron. | — |
| 3 | Cómo lo investigamos | 1:45 | **Operación justificada y evidencia (parte 1):** 3-4 pasos en palabras, cada uno con su porqué (filtré X porque…). Sin pegar código. | 25 (junto con la 4) |
| 4 | Hallazgo y evidencia | 1:45 | **Claridad del hallazgo (10):** el título es la frase que responde la pregunta, sin términos técnicos sin explicar. **Evidencia (parte 2, dentro de los 25):** un gráfico o tabla del Colab, con la parte que respalda la afirmación resaltada. | 10 + 25 |
| 5 | Límites | 0:45 | **Explicación oral de límites (20):** una limitación específica de su base, cómo afecta la confianza, coherente con el Producto. | 20 |
| 6 | Conclusión y próximo paso | 1:00 | **Conclusión argumentada (15):** responde la pregunta, vuelve a la hipótesis, descarta al menos una explicación alternativa y propone un próximo paso. | 15 |
| — | Preguntas (ronda final) | — | **Manejo de preguntas (20):** responde él o ella, con criterio propio, sin memorizar; si no sabe, lo reconoce. | 20 |
| Transversal | Formalidad | — | No leen las diapositivas, tono y ritmo, contacto visual, todos participan. | 10 |

Suma: 10 + 25 + 20 + 15 + 20 + 10 = 100.

**Sin criterio de diseño.** El foco es contenido y comunicación.

**Descuento aparte (fuera de los 100 pts, sobre la nota final):** -0,1 por cada 3 faltas de ortografía en el total de diapositivas, con tope de -1,0.

**Ensayo previo (formativo, sin nota):** martes 27-oct, en grupos de 2-3 equipos en paralelo, si alcanza el tiempo, con la plantilla "Lo que funciona / Lo que falla / Lo que falta pulir".

---

## 6. Defensa técnica — código intervenido (100 pts, 30% del total) — v4

> **Actualizado 2026-10-19 (Calendario v4).** Pasa de individual a **en parejas (nota grupal)** y de 30 + 70 pts a 4 secciones. Diego aceptó que en pareja deja de medir lo estrictamente individual, a cambio de terminar rápido y que trabajen colaborativamente. Los equipos individuales la rinden solos.

**Instrumento escrito, no entrevista oral.** Cada equipo recibe una copia de su propio Colab final con **3 errores deliberados** (mezcla de lógicos y de sintaxis), generada por IA con criterios claros y revisada por Diego. Copias distintas entre equipos.

| Sección | Pts | Qué se evalúa |
|---|---|---|
| **A. Explicar código propio** | 15 | En palabras, qué hace 1 bloque marcado del Colab. |
| **B. Predecir qué cambia** | 20 | Si se cambia un parámetro (la columna, el valor del filtro, el n), qué resultado esperan y por qué. Sin ejecutar. |
| **C. Errores intervenidos** | 45 | Por cada uno de los 3 errores (15 pts c/u): ¿lo encontró?, ¿explica por qué es error y su consecuencia?, ¿lo corrige? |
| **D. Proceso** | 20 | 2 preguntas cortas de decisiones de trabajo: p. ej. qué columna tenía datos sucios y cómo lo notaron, qué decisión cambiaron en el camino y por qué. |

**Sin código nuevo.** Solo explicar, predecir y corregir código dado.

**v5 — dónde van los 3 errores:** en los **6 espacios** de la receta (columna mal escrita, `VALOR` que deja 0 filas, `RESUMEN` equivocado, `N`) o en la **receta misma** (`ascending` invertido, `head` sin `N`, filtro con `=` en vez de `==`) **de su análisis principal**. Los errores más probables y su consecuencia quedan como banco para el corrector *(pendiente de armar, §10)*. En la sección B se predice qué cambia al modificar un espacio (por ejemplo `VALOR = "Maipú"` por `"Providencia"`).

**Logística:**
- Martes 27-oct, **30 min**, en clase, todos a la vez, en silencio.
- Las copias se generan entre el lunes 26 a las 23:59 (cierre del buzón) y el martes antes de clase. Quien no entregó el lunes usa la última copia fechada del buzón.
- Corrección con el pipeline del curso (extractor + rúbrica parcelada ✅/⚠️/❌ + `revisar-evaluacion`). Corregir primero a los de 4to (notas cierran el 30-oct).
- Seguimiento oral solo para casos dudosos.
- La responsabilidad individual queda cubierta por la ronda de preguntas de la Presentación y por el factor individual (§9).

---

## 7. Proceso — bitácora e hitos (100 pts, 15% del total)

| Criterio | Pts | Qué se evalúa |
|---|---|---|
| **Pregunta inicial y descartadas** | 15 | Evidencia de indagación real antes de comprometerse con una pregunta (no la primera idea que se les ocurrió). |
| **Cumplimiento de hitos** | 50 | Proporcional: (hitos cumplidos con avance real / hitos totales) × 50. **Hitos v5: 37b (nota de progreso), 38, 38b y entrega del 26-oct** → 12,5 pts cada uno. |
| **Incorporación de feedback** | 20 | Cambios visibles después de un comentario (ensayo del 27-oct o clase). *El círculo de crítica formal se cortó en v3; cómo se mide sigue abierto (§10).* |
| **Rastro de avance incremental (buzón)** | 15 | El registro fechado (ver §9) muestra construcción sesión a sesión, no todo entregado de golpe al final. |

### Hito 37b — nota de progreso *(propuesta, por confirmar antes de calcular)*

Se evalúa el cuaderno que cada equipo dejó el **lunes 19-oct** (Clase 37b). Nadie llegó al Paso 4, así que se mide **cuánto avanzó**, no si estaba perfecto.

- **Qué cuenta:** el **código** y el **texto** de cada Paso 1-6 = hasta 12 componentes. **Un intento visible cuenta como logrado, aunque tenga errores** que el equipo no haya notado.
- **Por pareja:** se junta lo que hicieron los cuadernos de sus integrantes (uno pudo escribir el texto y el otro el código, o uno solo hizo todo). Hay que mirar cada pareja completa antes de calcular.
- **Escala lineal:** la **pareja que más avanzó marca el máximo (7,0)**, aunque sus resultados tuvieran errores; un cuaderno sin nada = 2,0; el resto, proporcional a lo avanzado.
- **Dentro de Proceso:** el porcentaje de avance respecto del máximo multiplica los 12,5 pts del hito 37b.
- **Ausentes del 19-oct:** heredan la nota de su pareja si ella vino; si no vino ninguno de los dos, el hito queda **«Pendiente»**.
- **Insumos:** los cuadernos de `clase-37b-aplicacion-mi-tabla/CUADERNOS ESTUDIANTES/` (contienen código real de estudiantes: **no subir a git**).

---

## 8. Política de IA — 3 niveles

> **v5 (2026-10-20):** la nota de prensa ya **no lleva versión corregida con IA**, así que el nivel «Documentado» queda sin uso. Rigen solo «Restrictivo — 0 IA» (código y todos los textos, nota de prensa incluida) y «Permisivo» (diseño de la presentación). La tabla de abajo es la de v4, conservada como registro.

**Principio central:** el uso de IA no se persigue ni se detecta — se verifica indirectamente a través de la Defensa técnica (§6) y el Q&A de la Presentación (§5). Lo que se evalúa nunca es "si usaron IA", sino si **pueden responder por lo que entregan**.

| Nivel | Dónde aplica | Regla |
|---|---|---|
| **Restrictivo — 0 IA** | Código completo (limpieza, filtros, gráficos) + Colab narrado completo (justificación, razonamiento, conclusión) | Nada de esto se corrige ni se genera con IA. Es donde vive la habilidad Python que el curso certifica y el análisis que se defiende en la Defensa técnica — no se publica ni se muestra a nadie fuera del curso. |
| **Documentado** | Solo la **nota de prensa** | Se entrega en dos versiones: **borrador propio** (sin corregir, puede tener faltas) + **versión corregida con IA**, con **registro de qué se le pidió y qué respondió**. Es el único artefacto del proyecto que se publica físicamente (diario mural) ante público, por eso es el único con este nivel intermedio. |
| **Permisivo** | Diseño de presentación y recursos visuales similares | Pueden usar plantillas o recursos de internet, siempre citados al final con el formato: **"Descripción propia o título del documento — Autor/Plataforma — Link"** (ej. *"Plantilla de diapositivas minimalista — Slidesgo — https://..."*). |

**Por qué el Colab queda 100% restrictivo y no en el nivel documentado (a diferencia de la nota de prensa):** el corte no es "análisis vs. redacción", es **qué se publica ante público vs. qué queda como trabajo interno**. La nota de prensa es lo único que sale del aula; el Colab es el documento de trabajo que sostiene todo lo demás, y ahí no hay corrección de IA de ningún tipo.

---

## 9. Mecanismos transversales

### Factor individual (evidencia individual dentro de notas grupales)

ABP §6 (`guia-operativa-abp-para-agentes.md`): nunca se puede poner la misma nota a todo el grupo sin evidencia de aporte individual. Producto, Proceso y (desde v4) **Defensa técnica** son notas grupales — necesitan este ajuste; **Presentación no lo necesita** (la ronda de preguntas diferencia individualmente).

Al cierre del proyecto, un único instrumento breve: cada estudiante autoevalúa/coevalúa el aporte de cada integrante (incluido el propio) en una escala simple con justificación de una línea. El resultado se convierte en un **factor individual** (ej. 0.85×-1.1×) que ajusta la nota grupal de Proceso, Producto y Defensa técnica por estudiante. Una sola vez, al final — no en cada hito.

**Equipos individuales (✅ actualizado 2026-09-24 — el criterio de equipos pasó a individual o pareja, a elección):** un estudiante que trabajó solo no completa este instrumento (no hay a quién coevaluar) y su factor individual queda en 1.0× por defecto — la nota grupal de Proceso y Producto es, para él, directamente su nota individual, sin ajuste.

### Retroalimentación formativa (sin nota, formato fijo — CERRADO 2026-09-23)

No se califica la calidad de la crítica que da cada grupo — solo si el grupo *usó* la retro recibida (eso ya es parte de Proceso, "Incorporación de feedback", §7). Pero para que "incorporación de feedback" tenga sentido, la crítica que se recibe debe ser específica, no un trámite ("se ve bien") — eso se resuelve con **formato**, no con una rúbrica nueva:

**"Lo que funciona / Lo que falla / Lo que falta pulir"** — cada grupo completa esta plantilla sobre el trabajo del otro, una línea por categoría:
- **Lo que funciona** — qué parte ya responde bien lo que se pide; qué no tocarían.
- **Lo que falla** — algo incorrecto o que no cuadra con lo que se pide.
- **Lo que falta pulir** — algo que puede estar bien pero mal ejecutado o poco claro.

- **Círculo de crítica entre grupos**, a mitad de la fase de indagación, sobre el Colab en construcción: "lo que funciona" = evidencia/análisis que ya responde la pregunta; "lo que falla" = operación mal elegida, conclusión que la evidencia no sostiene, límite del dato no declarado; "lo que falta pulir" = código sin comentar, markdown que no explica la decisión, gráfico ilegible.
- **Ensayo de presentación**, en grupos de 2-3 equipos por sesión, en paralelo dentro de una misma clase: "lo que funciona" = qué parte de la exposición ya se entiende clara; "lo que falla" = una afirmación que la evidencia no sostiene, un límite no mencionado; "lo que falta pulir" = leen la diapositiva, tono monótono, nadie mira al público.

La plantilla completada queda en el buzón (no se corrige a diario) — respaldo si "incorporación de feedback" deja dudas sobre si el grupo ignoró una buena crítica o si la crítica que recibió era floja.

### Buzón — registro pasivo

Cada grupo guarda una copia fechada de su Colab al cierre de cada sesión de proyecto. **No se revisa a diario** — es rastro que solo se consulta en dos momentos: al calificar Proceso (¿hubo avance real sesión a sesión?), y si la Defensa técnica deja dudas sobre un estudiante puntual.

### Ausencias

Misma convención que los controles de lunes estándar: **ausente = 2.0**, con **2 semanas para rendir atrasada** ("Pendiente" mientras tanto). Aplica en particular a Presentación y Defensa técnica, que son actos únicos de una sesión específica.

---

## 10. Pendiente explícito, para después

- ~~**Calendario definitivo** (Sesión 2, `Plan y Pendientes.md` §7): número y fechas de los hitos de Proceso, fecha de la Defensa técnica, cuántos días de Presentación, destino de la sesión del 19-oct.~~ **✅ CERRADO 2026-09-23.** Resuelto en `Plan y Pendientes.md` sección 3: hitos = cierre de cada una de las 4 sesiones de proyecto (13, 15, 19, 20-oct); Defensa técnica = 26-oct; Presentación = 2 días (27 y 29-oct, por sorteo); la sesión del 19-oct ya no existe como tal — la IA responsable se integró a la presentación de rúbricas del 13-oct.
- **Pendiente real que queda:** confirmar presencia de dirección en ambos días de Showcase (ver `Plan y Pendientes.md` §8) — no bloquea el calendario, es logística externa.

### Pendientes abiertos en v5 (2026-10-20)

- **Normalizar Producto:** suma 115 pts (100 del Colab + 15 de nota de prensa). Hay que decidir si se reescala a 100 o se ajustan pesos.
- **Niveles de «Originalidad»** (§4): confirmar los tres niveles propuestos y quién decide si una pregunta «cambia la comparación» (el corrector, comparando con el ejemplo de la base).
- **Cálculo de la nota de progreso 37b** (§7): confirmar escala, qué cuenta como «intento visible» y la mapeo a puntos de Proceso.
- **Cómo medir «Incorporación de feedback»** (heredado de v4).
- **Banco de errores de la Defensa** sobre la receta (§6).
- **Ticket de Salida de la N°38:** pendiente (sigue en `old/clase-38-pandas3-responder-con-datos/`); ojo con que el ICN nuevo agrega `RESUMEN` y `.agg(...)`.
- **Base del trío** Diego Cifuentes + Alain Moyano + Julián Aravena: sin definir.

---

## 11. Equipos y bases (v5)

Tabla que ven los estudiantes (viene de la 37b, tal como se publicó el 19-oct):

| Base elegida | Equipos |
|---|---|
| 🚗 Siniestros de tránsito (CONASET) | Santino García y Tomás Díaz · Benjamín Mejías · Felipe Román |
| 🎓 Puntajes de corte (DEMRE) | Maura Muñoz y Simón Abrahams · Eduardo Pacco y Damián Flores · Diego Peña y Felipe Aravena · Vicente Benítez y Vicente Narváez · Martín Sánchez |
| 💼 Empleabilidad e ingresos (SIES) | Francisca Parra y Julián Sandoval · Sebastián Ulloa |
| 🏥 Estadísticas hospitalarias | Francisco Vega y Héctor Vergara · Alex Saravia y Diego Donoso |
| 📝 SIMCE 2° medio por establecimiento | Cristóbal Muñoz y Luckas Letelier |
| 🏫 Matrícula por establecimiento | Diego Vargas y Benjamín Díaz |

**Ojo, hay diferencias con el Calendario v4** *(a confirmar con Diego)*: el v4 deja **fuera** del proyecto a Benjamín Mejías, Nacor Pardo y Paula Inzunza (aquí Benjamín Mejías aparece en CONASET); y no están en esta tabla la pareja mixta **Lucas Valenzuela + Víctor Olguín** ni el **trío** Cifuentes + Moyano + Julián Aravena (sin base). Esta tabla se corrige apenas Diego entregue la lista actual.
