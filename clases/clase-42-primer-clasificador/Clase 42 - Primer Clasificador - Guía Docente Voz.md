# Clase 42 — Guía docente: ChatGPT Voice como colega

**Solo para ti (no se sube a Classroom ni se proyecta).** Martes 3-nov-2026 · 80 min · 3ro medio.

La voz es **un colega que verifica comprensión y plantea el escenario**, no un cuello de botella: tú explicas y programas con el curso; ella hace de cliente, compara su predicción con la del modelo y pregunta. **Solo habla cuando tú la activas.** La opera solo tu cuenta; los estudiantes no necesitan cuenta.

## 1. Antes de la clase (5 min)

- [ ] Cuenta de profesor abierta en ChatGPT, **modo de voz probado** con el parlante de la sala (volumen y eco).
- [ ] **Conexión estable.** Si la red del liceo es inestable, ten el celular como respaldo.
- [ ] **Pega el prompt de arranque** (sección 2) y espera su confirmación («Listo, Colega al aire»). Después **silencia el micrófono**: ella responde ante cualquier pausa o ruido, así que no dependas solo del prompt.
- [ ] Colab de la clase abierto y proyectado (el objetivo, los datos y los autochequeos viven ahí).
- [ ] Ejecuta tú antes la **celda de autochequeos** del Colab para comprobar que scikit-learn carga sin problemas.
- [ ] Plan B listo: esta guía impresa o en otra pantalla.

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
> 7. Si alguien se equivoca, no lo corriges de inmediato: preguntas «¿cómo podemos comprobarlo con los datos?».
>
> **Datos de la clase de hoy (úsalos tal cual, no agregues otros):**
>
> - Objetivo: entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico.
> - Historia de la clase: la micro de las 7:00 que va de La Islita a Santiago. Los datos son ficticios. Cada día se anotan tres cosas: la lluvia de la madrugada en milímetros, los kilómetros de taco en la Ruta 78 a las 6:45 y las personas esperando en el paradero. La etiqueta es 1 si la micro llegó atrasada y 0 si llegó puntual.
> - Definiciones: un *árbol de decisión* es una lista de preguntas de sí/no que se encadenan hasta llegar a una respuesta; *entrenar* (`fit`) es mostrarle al modelo días anteriores con sus etiquetas para que descubra qué preguntas los separan; *predecir* (`predict`) es preguntarle por un día nuevo que no estaba en los datos.
> - El árbol que se obtiene pregunta primero si los km de taco son 4 o menos; si sí, mira si la lluvia es 8 mm o menos (puntual) o más (atrasada); si hay más de 4 km de taco, predice atrasada. **No usó la cantidad de pasajeros.**
> - Casos para comparar: 0 mm, 2 km, 12 pasajeros → puntual; 7 mm, 4 km, 15 pasajeros → puntual; 5 mm, 1 km, 40 pasajeros → puntual (el árbol no usó los pasajeros y sus datos no tienen días con tanta gente).
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos de la voz (las frases de activación son sugerencias y pueden variar)

| # | Cuándo | Frase de activación | Qué hace la voz | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida** (min 0–5) | «Colega, da la bienvenida al curso.» | Saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo. | Activas el micrófono, dejas que el curso salude, silencias, y cuando alguien lee el objetivo (desde el Colab) tomas la clase. | Tú saludas y pides que alguien lea el objetivo. |
| 2 | **Haz Ahora** (5–15) | «Colega, plantea el diagnóstico.» | Hace de **dirigente de la junta de vecinos de La Islita** y pide un sistema que avise si la micro de las 7:00 llegará atrasada; plantea las **4 preguntas una por una**, esperando al curso. | Das la palabra al curso entre pregunta y pregunta (micrófono silenciado) y anotas en la pizarra: variables propuestas, cuáles son medibles, qué se anotaría cada día. | Lees las 4 preguntas del Colab. |
| 3 | **ICN, concepto 3** (tras `predict()`), caso `[7, 4, 15]` | «Colega, ¿qué predices para este día?» | Dice una predicción para 7 mm, 4 km de taco y 15 pasajeros **antes** de que el modelo responda, y la justifica en una frase. | Pides al curso su predicción a ojo, luego activas la voz, y **recién después** corres `predict()`: comparas curso, voz y modelo. | Tú dices una predicción a ojo en voz alta y la comparas con el modelo. |
| 4 | **ICN, concepto 4** (con el árbol a la vista), caso `[5, 1, 40]` | «Colega, explica por qué predijo eso.» | Explica por qué el modelo predijo «puntual» con 40 pasajeros esperando. **Puede equivocarse** (ej. «los pasajeros no importan»). | Pides al curso que **juzgue si la explicación cuadra con las preguntas del árbol** (que no usa pasajeros). | Lees tú una explicación con un error plausible y el curso la juzga. |
| 5 | **ICN (cierre)**, 3 min | «Colega, verifica comprensión de fit y predict.» | Pregunta a dos estudiantes: «¿qué diferencia hay entre `fit` y `predict`?» y «¿por qué el árbol ignoró los pasajeros?»; resuelve dudas. | Silencias entre respuestas; repites en voz alta lo que dicen si la voz no los escucha. | Haces tú esas dos preguntas. |
| — | Práctica guiada, independiente, ticket y cierre | — | **No es protagonista.** | Disponible si se te ocurre sumarla. | — |

**Frases de apoyo (no son guion):** si el curso no responde, «¿Alguien se anima a intentarlo con sus palabras?»; si se equivocan, «¿Cómo podemos comprobarlo con los datos?».

## 4. Qué tiene el Colab para ti

- **Un solo cuaderno, sin página web ni contraseñas.** La práctica y el ticket se autorrevisan con `check_*()` (✅/⚠️ sin mostrar la solución); no recolectas resultados.
- Los autochequeos buscan el árbol del estudiante en una variable llamada **`modelo`**: dilo en voz alta cuando lleguen a la Guiada.
- El ticket está **en el propio Colab** (4 preguntas A–D; respuestas correctas C, A, D, B). En el cuaderno de estudiantes las letras correctas están guardadas como huellas y las explicaciones codificadas, pero alguien con ganas podría descifrarlas: es práctica sin nota, no una evaluación.
- Si el tiempo apremia: el **Ejercicio 3** y el **Ejercicio 4** pasan a tarea; el Ejercicio 0a, el 1 y el 2 alcanzan para consolidar.
- El `Solucionario.ipynb` tiene todo el código ejecutable. **No lo subas a Classroom antes de dictar la clase.**

## 5. Reglas de uso de la voz

- **Es una voz más, no una fuente de verdad.** Si dice algo dudoso, es una oportunidad de pensamiento crítico: «¿cómo lo comprobamos con los datos?».
- **Nada de datos personales** (nombres de estudiantes, notas, salud) en lo que se le dice a la voz.
- La conversación vive en **tu cuenta**; no la compartas ni la publiques.
- Los estudiantes **no** usan ChatGPT hoy. Su uso real parte el lun 16 y depende de las verificaciones de edad y permisos pendientes del plan.

## 6. Plan B general

| Si pasa… | Haces… |
|---|---|
| Se cae la conexión o la voz no responde | Lees tú la intervención escrita de la tabla (columna «Plan B»); la clase no depende de la voz. |
| La voz habla sin que la actives | Silencias el micrófono y sigues; si insiste, cierras la sesión de voz y continúas solo. |
| La voz se equivoca | Lo usas como momento de pensamiento crítico: «¿cómo podemos comprobarlo con los datos?». |
| Responde algo inapropiado | La cortas de inmediato, lo hablas con el curso y sigues sin ella. |
| El ruido de la sala la confunde | Silencias el micrófono y repites tú, en voz clara, lo que dijo el curso. |
| scikit-learn no carga en Colab | Reinicia el entorno de ejecución y vuelve a correr la celda de autochequeos; si persiste, proyecta el Solucionario (salidas ya calculadas). |

## 7. Después de la clase

- [ ] Anota en el `Historial.md` qué momento de la voz funcionó y cuál no (insumo para la N°43).
- [ ] Anota si la explicación de la voz en el momento 4 generó discusión útil.
- [ ] Anota cuántos llegaron al Ejercicio 3 (para decidir si queda como tarea otra vez).
