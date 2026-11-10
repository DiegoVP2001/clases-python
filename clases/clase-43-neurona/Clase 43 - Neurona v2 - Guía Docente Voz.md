# Clase 43 v2 — Guía docente: ChatGPT Voice como colega

**Solo para ti (no se sube a Classroom ni se proyecta).** Martes 10-nov-2026 · 80 min · 3ro medio.

La voz es **un colega que plantea el escenario y verifica comprensión**, no un cuello de botella: tú explicas y programas con el curso; ella hace de encargado de informática y pregunta. **Solo habla cuando tú la activas.**

## 1. Antes de la clase (5 min)

- [ ] ChatGPT con **modo de voz probado** en el parlante de la sala; celular como respaldo de conexión.
- [ ] **Pega el prompt de arranque** (sección 2), espera «Listo, Colega al aire» y **silencia el micrófono**.
- [ ] Colab abierto y proyectado. **Regla de hoy: los `import` raros van SIEMPRE en la primera celda, ejecutada primero.** Ejecuta tú antes las dos primeras celdas («🔧 Ejecuta esta celda primero» y el verificador) y repítelo en voz alta al curso.
- [ ] Slides: https://clases-ia-mario-bertero.vercel.app/clase-43-v2/ (9 slides; la 1 tiene deslizadores de importancia 0–10).
- [ ] Plan B: esta guía impresa o en otra pantalla.

## 2. Prompt de arranque (copiar y pegar)

> Eres «Colega», un colega docente que me acompaña en una clase de 3ro medio en un liceo de Isla de Maipo, Chile. Hablas español de Chile, con tono cercano y simple, para estudiantes de 16 y 17 años.
>
> **Reglas:**
>
> 1. Solo hablas cuando te lo pido con la frase «Colega, …». Si no te hablo, guardas silencio total.
> 2. Tus intervenciones duran como máximo 20 a 30 segundos.
> 3. Te diriges al curso («curso» o «estudiantes»), no a mí.
> 4. Haces preguntas al curso y esperas la respuesta. No las respondes tú.
> 5. No inventas datos sobre el liceo, el curso ni las personas. Si no sabes algo, lo dices.
> 6. No das discursos ni resumes la clase si no te lo pido.
> 7. Si alguien se equivoca, no lo corriges de inmediato: preguntas «¿cómo podemos comprobarlo?».
>
> **Datos de la clase de hoy (úsalos tal cual, no agregues otros):**
>
> - Objetivo: crear, entrenar y evaluar una neurona con la misma receta del árbol y comparar ambos resultados, con sorpresa.
> - Historia: el wifi del liceo (datos ficticios). Eres el encargado de informática. Tu cuaderno tenía 6 columnas, pero hoy pides trabajar con 3: dispositivos conectados, estudiantes viendo video y horas desde el último reinicio del router. La etiqueta es 1 si el wifi se cayó y 0 si aguantó. Tienes 20 filas de datos: 16 para que la computadora aprenda y 4 para probarla.
> - Ayer el árbol acertó las 4 filas de prueba. Hoy quieres probar una neurona: recibe las 3 columnas, pondera cada una (le da más o menos importancia), las suma y decide 0 o 1; los pesos los ajusta sola la computadora.
> - El *accuracy* son los aciertos divididos por el total; con 4 filas, cada fila vale 25 %.
> - No des tu opinión sobre cuál columna pesa más; pregunta al curso.
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos de la voz (las frases de activación son sugerencias)

| # | Cuándo | Frase de activación | Qué hace la voz | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida** (0–5) | «Colega, da la bienvenida al curso.» | Saluda, **espera que el curso la salude** y pide que alguien lea el objetivo. | Dejas que el curso salude, silencias y, cuando alguien lee el objetivo, tomas la clase. | Tú saludas y pides leer el objetivo. |
| 2 | **Haz Ahora** (5–12) | «Colega, plantea el diagnóstico.» | Hace de **encargado de informática**: «el cuaderno tenía 6 columnas, pero hoy les pido trabajar con estas 3» y plantea las **4 preguntas una por una**, esperando al curso. La **pregunta 1** es de ponderación: «¿qué nota de 0 a 10 le pondrían a cada una de las 3 columnas y por qué?». | Das la palabra al curso (micrófono silenciado) y anotas: la columna con la nota más alta (sin dar la respuesta), 100 %, 25 puntos por fila, 3 filas. | Lees las 4 preguntas del Colab. |
| 3 | **ICN, tras el concepto 4** (~2 min) | «Colega, verifica comprensión de los pesos.» | Pregunta a dos estudiantes: «¿por qué cambian los pesos si usamos otra semilla?» y «¿los pesos los escribimos nosotros o los ajustó la computadora?». | Silencias entre respuestas y repites lo que dicen. | Haces tú esas dos preguntas. |
| 4 | **En cualquier momento** | «Colega, responde la pregunta de…» | Responde una pregunta abierta, sin inventar. | Repites la pregunta con claridad y silencias. | Respondes tú. |
| — | Guiada, ticket y cierre | — | **No es protagonista.** | — | — |

**Frases de apoyo:** «¿Alguien se anima a intentarlo con sus palabras?»; «¿Cómo lo comprobamos con los datos?».

## 4. Qué tiene el Colab para ti

- **Concepto 2:** el Colab trae dos diagramas (la neurona y el nivel de activación, umbral 0,5); las slides 3 y 4 los animan. **`hidden_layer_sizes=()`** está en un desplegable justo debajo del código del concepto 3.
- **Orden:** celda de `import` → verificador → Haz Ahora → puente → ICN (5 conceptos) → guiada → ticket (solo link) → cierre → extras.
- **Verificadores:** `check_icn()` (concepto 3), `check_comparar()` (concepto 5), `check_guiada()` y `check_ej0a()`, `check_ej1()`, `check_ej2()`. Dan ✅/⚠️ sin mostrar la solución. Los modelos deben llamarse `modelo` (ICN) y `modelo_arbol` / `modelo_neurona` (guiada).
- **Números verificados (scikit-learn 1.9.1):** árbol **1,0** (4/4); neurona **0,75** (3/4; falla la **fila 18**: 117 dispositivos, 0 video). Con `random_state=0` los pesos son `[-0.035, 0.376, 0.098]` y el sesgo `-0.048`; con `random_state=1`, `[-0.001, 0.767, -0.099]`, y el accuracy de **train** baja de 0,875 a 0,75 (el de test se mantiene).
- **Semilla (concepto 4):** muéstralo en vivo cambiando `semilla` de 0 a 1 y volviendo a 0. Insiste: **en las pruebas siempre `random_state=0`**. Una línea y sin profundizar: los números también pueden variar por otras razones técnicas que no veremos.
- **No leas los pesos como verdad absoluta:** «dispositivos» sale casi en cero aunque sea una columna clara. Quédate con que **existen y los ajusta la computadora**.
- **Guiada (el único obligatorio):** entrenar árbol y neurona y escribir 2 líneas (cuál usarías y por qué con sus números; por qué 4 filas dan poca seguridad). Es el mismo recorrido de la Prueba 1 (B, C1, C3). Revisión con una pareja al frente.
- **Tiempos (80 min):** bienvenida 5 · Haz Ahora 7 · puente 3 · ICN 30 · guiada 20 (12 + 8) · ticket 5 · cierre 5.
- **El ticket NO está en el Colab:** solo el link al Form. Proyecta `Ticket de Salida.pptx` (**no se pushea antes de dictar**); respuestas **B, D, A**. Tema a escribir: «La neurona aprende sola».
- **Cierre (a viva voz):** comprensión 1–5; «¿qué te sorprendió hoy de la neurona y por qué?»; anticipo del **lunes 16: mini-LLM**.
- El `Solucionario.ipynb` tiene todo ejecutable. **No lo subas a Classroom antes de dictar la clase.**

## 5. Reglas de uso de la voz

- Es una voz más, no una fuente de verdad: si dice algo dudoso, «¿cómo lo comprobamos?».
- Nada de datos personales en lo que se le dice a la voz; la conversación vive en tu cuenta.
- Los estudiantes **no** usan ChatGPT hoy.

## 6. Plan B general

| Si pasa… | Haces… |
|---|---|
| Se cae la conexión o la voz no responde | Lees tú las preguntas (columna «Plan B»); la clase no depende de la voz. |
| La voz habla sin que la actives | Silencias; si insiste, cierras la sesión de voz y sigues solo. |
| La voz se equivoca | Úsalo como momento de pensamiento crítico. |
| Alguien no ejecutó los `import` | `NameError`: recuerda la regla de la primera celda y ejecuta de nuevo. |
| Los pesos de un estudiante difieren en decimales | Normal si la versión de scikit-learn es distinta; lo que importa es el accuracy 0,75. |

## 7. Después de la clase

- [ ] Anota cuántos llegaron a la guiada y cómo salió la revisión con la pareja al frente.
- [ ] Anota si «pondera» y «los pesos los ajusta la computadora» quedaron claros (insumo para la Prueba 1).
- [ ] Anota si hubo errores por no ejecutar los `import` primero.
