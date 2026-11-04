# Clase 43 — Construir una neurona

**Estado:** Spec v2 aprobada — 2026-11-04 (gate 1 + ajustes de diseño acordados con Diego el mismo día: «colega del profesor», Haz Ahora de automatización, recordatorio puente, caja lista primero, evaluador preparado, set de entrenamiento y de prueba, desafío con día raro). Colab, Solucionario, Guía y página generados; a la espera de la revisión de Diego ya renderizados.
**Clase Picuino:** N/A — bloque de IA (Plan Noviembre v3, sesión 3)
**Fuente del diseño:** `clases-znoviembre/Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` (§3 fila 3, §5 y §10) y `Plan Noviembre - Checklist y traspaso entre sesiones.md` §5
**Flujo:** liviano (Spec → Colab + Solucionario + Guía Docente Voz + página web → gate; sin Ejercicios.ipynb, sin Ticket por Form, sin PPT principal). *Calendario v4 (2026-11-04): esta clase se dicta el **lunes 9-nov**; la N°44 (la computadora ajusta sola) es el martes 10-nov.*

## Contexto

- **Curso:** 3ro medio · **Duración:** 80 min · **Fecha:** lun 9-nov-2026
- **Modalidad:** individual como piso (no se menciona en ningún material; la anuncia Diego en vivo)
- **Plataforma:** Google Colab. **Entrega:** ninguna; práctica y ticket **autorrevisados** (`check_*()`), Diego no recolecta resultados
- **Contenidos previos asumidos:** Python hasta listas y `for` (sin pandas, sin numpy). De la N°42: entradas y etiquetas en listas, `fit()` entrena, `predict()` predice, el modelo solo sabe lo que hay en los datos. **Quien faltó a la N°42 parte igual:** el Colab trae recapitulación y datos propios.
- **Contenidos nuevos:** suma ponderada (entradas × pesos), sesgo, activación escalón, error de una predicción y ajuste **manual** de pesos. **Set de entrenamiento y set de prueba** (primera vez en código): se ajusta mirando solo el entrenamiento y la prueba se mira una sola vez. **No** hay retropropagación ni entrenamiento automático (llega en N°44 con `MLPClassifier(hidden_layer_sizes=())`, una sola neurona).
- **Historia continua (toda la clase):** **las colmenas de un apicultor de Isla de Maipo.** Quiere saber si sus abejas saldrán hoy a buscar néctar. Datos ficticios. *Historia nueva decidida por Diego (2026-11-04); reemplaza a la micro de la N°42.*
- **Colega del profesor** (ChatGPT Voice operada solo por Diego; así se nombra en todo material de estudiantes; ver «Guion del colega»).

## Objetivo

Crear nuestra primera inteligencia artificial: una neurona, con asombro.

*Verbo Bloom: crear/construir (aplicar). Calcular con entradas, pesos y sesgo y ajustar los pesos a mano es el camino; «explicar qué cambió» es la evidencia del Ej. 3. La actitud (asombro) va en el objetivo por decisión de Diego.*

**OAs:** OA1, OA3 | OAd (mismos que la N°42; confirmar contra `OAs-referencia.md` en el gate)

**Actitud: Asombro** (elegida por Diego, 2026-11-04; se retoma en el cierre). Se logra con una idea simple: lo que hoy escriben en unas pocas líneas es la **misma pieza** con que funcionan las IA que usan todos los días, incluida la voz que nos acompaña en la clase.

## ¿Por qué lo veremos?

**Lo dice el colega del profesor (ChatGPT Voice), no Diego** (decisión de Diego, 2026-11-04), para asombrar y entusiasmar: los estudiantes construirán los cimientos de lo que ella es. En el Colab aparece el texto como cita de la voz; en clase el colega lo dice en su intervención de bienvenida (ver «Guion de la voz»).

> «Yo estoy hecha de miles de millones de piezas pequeñas llamadas neuronas. Hoy ustedes van a construir la primera, desde cero. Con ella van a poner los cimientos de lo que yo soy.»

## Material para el asombro (sin historia lejana: todo ligado a lo que ellos usan)

| Idea | Uso en la clase | Verificación |
|---|---|---|
| **«El colega que ven está hecho de esta misma pieza.»** Los modelos como el de ChatGPT Voice funcionan con pesos como los de hoy, ajustados por la computadora, en cantidades enormes (miles de millones). | Bienvenida (el colega lo dice de sí mismo), cierre | Usar solo la afirmación general («miles de millones de pesos»); **sin cifras de un modelo concreto** (v2 §4) |
| **Lo que programan en 80 minutos es la unidad básica**: suma, número y un `if`. | Cierre y página | — |
| **Escala:** 1 neurona (hoy) → red de varias → cerebro humano (~86 mil millones de neuronas, cifra estándar de la neurociencia). | Última slide de la página | Confirmar la cifra y citar la fuente antes de publicar |

*Quitado en esta versión:* el perceptrón de 1958, el Nobel 2024 y la mosca conectoma (Diego: «out of nowhere»). Quedan disponibles como curiosidad para otra clase si se piden.

## Datos de la clase (escritos en el Colab, sin archivos)

Variables por día: `temperatura` (°C a las 9:00) · `viento` (km/h) · `lluvia` (mm). Etiqueta: `1` = las abejas **salieron**, `0` = **se quedaron**. Los 12 días se separan:

```python
dias = [[24, 5, 0], [28, 10, 0], [19, 3, 0], [30, 20, 0],
        [22, 8, 0], [26, 6, 4], [14, 4, 0], [25, 28, 0]]   # ENTRENAMIENTO (8 días)
etiquetas = [1, 1, 1, 0, 1, 0, 0, 0]
dias_prueba = [[27, 12, 0], [18, 6, 0], [21, 10, 0], [29, 24, 0]]   # PRUEBA (4 días nuevos)
etiquetas_prueba = [1, 0, 1, 0]
```

Neurona de partida (**verificada con Python**): `pesos = [1, -0.5, -2]`, `sesgo = -13` → **6 de 8** en entrenamiento (falla el día 4, mucho viento, y el día 6, viento y lluvia; ambos dicen «salen») y **2 de 4** en la prueba. **Subir la importancia del viento (peso `-1`) arregla los dos días: 8 de 8** en entrenamiento y **3 de 4** en la prueba (falla el día 3, de etiqueta 1): acertar el entrenamiento no garantiza acertar días nuevos. Subir solo la lluvia a `-3` arregla únicamente el día 6 (7 de 8). **Revelación de cierre:** una neurona entrenada con `MLPClassifier(hidden_layer_sizes=())` encuentra pesos `[3,77, −3,83, −9,53]` y sesgo `−45,22`: 8 de 8 y 3 de 4, **fallando el mismo día de la prueba**; los números difieren pero el patrón se parece (calor y viento pesan casi igual con signo contrario; la lluvia pesa más).

## Mapa de tiempos (80 min)

| Bloque | Min | Quién lidera |
|---|---|---|
| 1. Bienvenida + «¿Por qué lo veremos?» | 6 | Colega |
| 2. Haz Ahora (automatizar algo que no conocen) | 8 | Colega plantea, Diego modera |
| 3. Recordatorio puente (ayer → hoy → después) | 3 | Diego |
| 4. ICN: caja lista + abrir la caja (conceptos 1-3) + ajuste con justificación + prueba | 28 | Diego + curso · colega lanza retos (3) |
| 5. Práctica guiada | 10 | Curso, con Diego |
| 6. Práctica independiente | 13 | Curso, con `check_*()` |
| 7. Ticket de salida (en el Colab) | 5 | Cada estudiante, en silencio |
| 8. Cierre (con el asombro) | 7 | Diego (a viva voz) |

## Estructura de la clase

### 1. Bienvenida (6 min)
El colega saluda, **espera a que el curso le devuelva el saludo** y dice él mismo el «¿Por qué lo veremos?» (arriba). Diego pregunta: *¿qué creen que tiene adentro una IA?* y pide que alguien lea el objetivo (en el Colab).

### 2. Haz Ahora (8 min) — el colega como apicultor, sin código
El colega hace de **apicultor** que quiere automatizar algo que los estudiantes **no conocen** (cuándo salen sus abejas). Preguntas cerradas, una por una, con celda de texto (opcional, sin revisión):

1. Tú no sabes nada de abejas. ¿Qué le pedirías al apicultor para empezar a descubrir cuándo salen?
2. Con esos registros, ¿qué patrón buscarías primero entre los días en que salen y los días en que se quedan?
3. Si ves que «con mucho viento casi nunca salen», ¿cómo convertirías eso en un número que un programa pueda usar? *(prepara «peso»)*
4. ¿Cómo comprobarías que tu regla funciona antes de dársela al apicultor? *(prepara «set de prueba»)*

### 3. Recordatorio puente (3 min) — regla nueva para toda clase
**🔁 Ayer:** el árbol de decisión aprendió solo una cadena de preguntas sí/no. **🔀 Hoy es distinto:** la neurona no hace preguntas, hace una suma de datos × importancia, y la regla la armamos nosotros moviendo pesos y sesgo. **➡️ La próxima clase:** la computadora aprenderá sola esos mismos números y compararemos con los nuestros. Con mini-tabla Árbol vs. Neurona (cómo decide · quién armó la regla · qué se puede mover). Línea para decir en voz alta: *árbol = preguntas · neurona = suma de importancias · la próxima clase = la computadora ajusta los números.*

### 4. ICN (28 min) — «caja lista» primero, después «abrimos la caja»

Los datos y una **celda de evaluador preparada** (`evaluar_entrenamiento()` y `evaluar_prueba()`; el estudiante solo la ejecuta) vienen escritos. El evaluador muestra la regla actual, una tabla día por día (salida, etiqueta, error, ✅/❌) y «Aciertos en ENTRENAMIENTO: x de 8»; si se mira la prueba más de una vez avisa que «la prueba deja de ser prueba».

| # | Qué pasa | Qué hace el estudiante |
|---|---|---|
| **0** | **Caja lista (3 min):** la neurona ya está escrita; solo se cambian `pesos` y `sesgo`. Se explican entrenamiento (8 días, «aquí ajustamos») y prueba (4 días, «aquí vemos si predice días que no vio»). Diagrama de la neurona. | Mueve los números y mira cuántos días acierta (¿8 de 8?). Puede jugar en la página en paralelo. |
| 1 | **Suma ponderada** $z = w_1x_1 + w_2x_2 + w_3x_3$ | **Escríbelo tú:** calcula `z` del primer día |
| 2 | **Sesgo** $z = \ldots + b$ · *Reto del colega 1* | **Escríbelo tú:** suma el sesgo |
| 3 | **Activación escalón** `z >= 0` → 1 · *paso a paso en la página* · *Reto del colega 2* | **Escríbelo tú:** convierte `z` en 0/1 |
| 4 | **Ajusta tú** (error = etiqueta − salida; la neurona viene empaquetada en `neurona(dia)`): cambia **un** peso a la vez mirando el **entrenamiento**; **justifica su mejor resultado** con marco de frase; luego **mira la prueba una sola vez** y compara. *Reto del colega 3* | Edita solo `pesos`/`sesgo`; escribe la justificación (entrenamiento y prueba por separado) |

Cada concepto con Idea clave, Instrucción y Punto de partida acumulativo; Ejemplos autocontenidos en el Solucionario. Errores típicos: olvidar el sesgo, signo de un peso, `>` vs `>=`, cambiar varios pesos a la vez, **ajustar mirando la prueba**.

**Retos del colega (con respuesta):** 1) 10 °C sin viento ni lluvia: sesgo ≥ −10. 2) Peso del viento en 0: cambian los días 7 y 8 del entrenamiento. 3) «Cambié dos pesos a la vez y acierta 8 de 8, ¿cuál hizo el trabajo?»: cambiar uno a la vez; el del viento (−1) ya arregla los dos días. **Verificación (2 personas):** ¿qué hace el sesgo?, ¿para qué sirve la prueba y por qué no se mira mientras se ajusta?

### 5. Práctica guiada (10 min)
**¿Habrá enjambre?** Entradas: temperatura, humedad, horas de sol; 6 días de entrenamiento + 3 de prueba. El estudiante **escribe la función `neurona`**, la evalúa con el evaluador preparado, cambia un peso a la vez (partida 3 de 6; subir horas de sol a 2 da 6 de 6 y 3 de 3 en la prueba), mira la prueba una vez y explica en un comentario. Formato canónico.

### 6. Práctica independiente (13 min)
Pistas 1-2 y `check_*()` (✅/⚠️ sin mostrar la solución). El evaluador preparado sirve en los ejercicios con entrenamiento y prueba.

| Ejercicio | Escenario | Qué se pide |
|---|---|---|
| **0a** (directo, sin narrativa) | Consigna pelada | Neurona de 2 entradas: `z`, escalón, variable e impresión con etiqueta |
| **1** | Naltagua: ¿sale hoy el otro apiario? | Función `neurona`, 5 días (hay días con `z = 0`: `>=`); `check_ej1()` |
| **2** | Cerezos en flor: ¿conviene llevar las colmenas? | Función + `for` mostrando `z` y salida; `check_ej2()` |
| **3** | Miel para la feria de la Casona del Maipo | 7 semanas de entrenamiento + 3 de prueba; ajustar de a un peso (un arreglo rompe otro día), mirar la prueba una vez y **justificar**; `check_ej3()` |
| **4** (desafío) | Apiario del cerro | **12 días de entrenamiento con un día raro** + 4 de prueba: encontrar **la mejor combinación** (11 de 12 es lo máximo posible; verificado), mirar la prueba una vez y justificar; `check_ej4()` |

> Presupuesto: 60-90 palabras por ejercicio (3 y 4 pueden exceder). Si el tiempo apremia, 3 y 4 quedan como tarea.

### 7. Ticket de salida (5 min) — en el Colab, autorrevisado
4 alternativas A–D con `check_ticket()`; respuestas correctas **B, D, A, C**: 1) suma ponderada y sesgo (z = 2), 2) escalón con z = −0,5 y z = 0, 3) peso negativo más negativo, 4) **entrenamiento vs. prueba** (8 de 8 y 2 de 4: acertar el entrenamiento no garantiza días nuevos).

### 8. Cierre (7 min)
Objetivo reimpreso, escala 1-5, *«una neurona es una suma, un número y un `if`, y el colega que nos acompañó está hecho de piezas así: ¿qué fue lo que más te sorprendió?»*, «¿en qué se nos notó el asombro?» y anticipo: **la próxima clase la computadora ajusta sola los pesos**. En la página, revelación «tus pesos vs. los de la computadora».

## Guion del colega (detalle en `Clase 43 - Neurona - Guía Docente Voz.md`)

| Momento | Rol del colega | Frase de activación |
|---|---|---|
| Bienvenida + ¿Por qué lo veremos? | Saluda, espera respuesta, dice el «¿Por qué lo veremos?» y pide leer el objetivo | «Colega, da la bienvenida al curso.» |
| Haz Ahora | Hace de apicultor y plantea las 4 preguntas | «Colega, plantea el diagnóstico.» |
| ICN, tras concepto 2 / 3 / 4 | Retos 1, 2 y 3 | «Colega, plantea un reto.» |
| ICN (cierre) | Verifica comprensión (sesgo; para qué sirve la prueba) | «Colega, verifica comprensión de la neurona.» |
| En cualquier momento | **Preguntas abiertas** de los estudiantes, sin inventar, sin adelantar el ajuste automático | «Colega, responde la pregunta de…» |
| Práctica, ticket y cierre | No es protagonista | — |

## Colab — `Clase 43 - Neurona - Clase.ipynb`

Encabezado «Clase 43 — Construir una neurona» · 3ro medio · 🎯 Objetivo · 🔎 ¿Por qué lo veremos? (cita del colega) · 1️⃣ Haz Ahora + «Mis respuestas» · 🔁 Ayer → 🔀 Hoy → ➡️ Después · 2️⃣ ICN (paso 0 datos + diagrama + caja lista; conceptos 1-3 con LaTeX; ajuste con justificación; prueba una vez; 📌 resumen; ⚠️ errores) · 3️⃣ Guiada · 4️⃣ Independiente con `#@title 🔧 Verificador automático` · 🎫 Ticket · 🎯 Cierre. Sin modalidad de trabajo, sin soluciones, sin respuestas del ticket, sin la palabra «ChatGPT» ni «la voz».

## Página web — `sitio-hub/clase-43/index.html`

Pestañas Clase 41 · 42 · 43 · Inicio. **Parte A (paso a paso):** 1 Ayer → Hoy → Después · 2 el diagrama (3 datos con pesos → neurona → salida) · 3 entra un día · 4 dato × peso · 5 suma + sesgo · 6 se evalúa y se activa (o no) · 7 los 8 días del entrenamiento (6 de 8). **Parte B:** 8 laboratorio (perillas de datos, pesos y sesgo; tabla de entrenamiento en vivo; prueba oculta tras un botón «una sola vez» que avisa si cambian los pesos después de mirarla). **Parte C:** 9 tus pesos vs. los de la computadora (misma tabla de aciertos) · 10 escala (1 neurona → red pequeña → cerebro humano, ~86 mil millones, Azevedo et al. 2009) y la nota de que más neuronas se decide por prueba y error y hoy hay sistemas que automatizan esa búsqueda, pero seguimos con una sola.

## Decisiones de diseño relevantes

- **Asombro** (actitud): el «¿Por qué lo veremos?» lo dice el colega; revelación final «a mano vs. computadora»; sin perceptrón/Nobel/mosca.
- **Caja lista primero (iterar desde el inicio)** y evaluador preparado: el estudiante programa la neurona, no el recorrido de errores; se evalúa la justificación.
- **Entrenamiento y prueba** en todo ejercicio donde se ajuste (regla nueva de las skills): la prueba se mira una sola vez.
- **Diagrama = espejo del código** (3 datos con pesos → 1 neurona → salida).
- **Una sola neurona** (como en la N°42 se trabajó un solo modelo): `hidden_layer_sizes` y «más neuronas» se mencionan como decisión por prueba y error, con sistemas que la automatizan, pero no se usan.
- **Datos finales** de cada ejercicio: ver `Historial.md`.

## Brief para la Clase 44 (mar 10-nov) — la computadora ajusta sola

Misma historia de las colmenas con **más datos** (p. ej., ~40 días entrenamiento + prueba). `MLPClassifier(hidden_layer_sizes=(), activation="logistic")` = **una sola neurona**; `.fit()` encuentra pesos y sesgo (`coefs_`, `intercepts_`), contraste con los pesos a mano y `accuracy` = aciertos / total en la prueba. **Ver el entrenamiento paso a paso con `partial_fit`** (celda preparada; datos escalados; los aciertos suben de 4 a 7 de 8 en ~100 vueltas y a 8 de 8 en ~3.000; cambiar `learning_rate_init`). Mencionar que `hidden_layer_sizes` es el argumento que define cuántas neuronas más, se decide por prueba y error y hoy hay sistemas que automatizan esa búsqueda, pero seguimos con **una sola**. Aclarar que la neurona de scikit-learn entrena con activación logística (suave) y predice con la misma regla `z >= 0`.

## Pendientes para el gate

- [ ] Revisión de Diego del Colab y de la página ya renderizados (y Colab en vivo).
- [ ] Confirmar OAs: OA1, OA3 | OAd (mismos que la N°42).
- [ ] Autorizar commit + push de la carpeta y deploy del hub en Vercel (el Colab enlaza `/clase-43/`).
