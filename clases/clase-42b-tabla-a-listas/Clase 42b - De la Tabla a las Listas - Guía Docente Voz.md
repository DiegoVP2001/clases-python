# Clase 42b — Guía docente: ChatGPT Voice como colega

**Solo para ti (no se sube a Classroom ni se proyecta).** Lunes 9-nov-2026 · 80 min · 3ro medio.

La voz es **un colega que plantea el escenario y verifica comprensión**, no un cuello de botella: tú explicas y programas con el curso; ella hace de encargado de informática y pregunta. **Solo habla cuando tú la activas.** La opera solo tu cuenta; los estudiantes no necesitan cuenta.

## 1. Antes de la clase (5 min)

- [ ] Cuenta de profesor abierta en ChatGPT, **modo de voz probado** con el parlante de la sala (volumen y eco).
- [ ] **Conexión estable.** Si la red del liceo es inestable, ten el celular como respaldo.
- [ ] **Pega el prompt de arranque** (sección 2) y espera su confirmación («Listo, Colega al aire»). Después **silencia el micrófono**: ella responde ante cualquier pausa o ruido, así que no dependas solo del prompt.
- [ ] Colab de la clase abierto y proyectado (el objetivo, el diagrama del 80 / 20, la tabla y los verificadores viven ahí). **Ejecuta tú antes la celda «Verificador automático»** para comprobar que scikit-learn carga sin problemas.
- [ ] Slides animadas abiertas en otra pestaña: https://clases-ia-mario-bertero.vercel.app/clase-42b/
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
> 7. Si alguien se equivoca, no lo corriges de inmediato: preguntas «¿cómo podemos comprobarlo con la tabla?».
>
> **Datos de la clase de hoy (úsalos tal cual, no agregues otros):**
>
> - Objetivo: convertir una tabla de datos en listas de entradas y etiquetas para entrenar y evaluar un modelo, con atención.
> - Historia de la clase: el wifi del liceo. Los datos son ficticios. Tú eres el encargado de informática: quieres saber si la red se cae durante una fila de clases. En tu cuaderno, por cada fila anotaste seis cosas: dispositivos conectados, estudiantes viendo video, horas desde el último reinicio del router, temperatura de la sala, hora del bloque (del 1 al 8) y día del mes. La etiqueta es 1 si el wifi se cayó y 0 si aguantó. Tienes 20 filas anotados.
> - Definiciones: una *fila* de la tabla se escribe como una lista, `[dato1, dato2, dato3]`, y cada coma separa una columna; la *tabla* son varias filas separadas por coma dentro de otro par de corchetes; las *etiquetas* van en otra lista, en el mismo orden que las filas; con el 80 % de las filas (16) la computadora *aprende* (train) y el 20 % restante (4) se guarda para *probarla* (test); el *accuracy* son los aciertos divididos por el total.
> - La etiqueta responde tu pregunta «¿se cayó el wifi?»: 1 significa sí y 0 significa no (el 1 es «sí», no «bueno»). Cuando pregunto cómo presentarías la respuesta en código, tú no la das: esperas al curso.
> - Al principio no sabes cuáles columnas sirven. No des tu opinión sobre cuáles elegir; pregunta al curso.
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos de la voz (las frases de activación son sugerencias y pueden variar)

| # | Cuándo | Frase de activación | Qué hace la voz | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida** (min 0–5) | «Colega, da la bienvenida al curso.» | Saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo. | Activas el micrófono, dejas que el curso salude, silencias, y cuando alguien lee el objetivo (desde el Colab) tomas la clase. | Tú saludas y pides que alguien lea el objetivo. |
| 2 | **Haz Ahora** (5–13) | «Colega, plantea el diagnóstico.» | Hace de **encargado de informática del liceo**, cuenta que trae su cuaderno con 6 columnas por fila y plantea las **4 preguntas una por una**, esperando al curso. La **pregunta 3** es: «Al final de cada registro tengo otra columna que se llama **¿Se cayó el wifi?**. ¿Cómo representarían esa respuesta con una **etiqueta** binaria, en código?». La **pregunta 2** es: «¿Cuáles son las 3 que descartaron y por qué?». | Das la palabra al curso entre pregunta y pregunta (micrófono silenciado) y anotas en la pizarra: columnas que creen útiles, cuál parece no tener relación, la etiqueta (**1 = sí, 0 = no**), cuántos filas guardar. **Después del Haz Ahora fijas las 3 columnas de la clase** y comparas con lo que propuso el curso. | Lees las 4 preguntas del Colab. |
| 3 | **ICN (cierre)**, 2 min | «Colega, verifica comprensión de las listas.» | Pregunta a dos estudiantes: «¿para qué guardamos 4 filas aparte?» y «¿qué cambia si una etiqueta queda en otra posición?»; resuelve dudas. | Silencias entre respuestas; repites en voz alta lo que dicen si la voz no los escucha. | Haces tú esas dos preguntas. |
| 4 | **En cualquier momento** | «Colega, responde la pregunta de…» | Responde una pregunta abierta de un estudiante, sin inventar y sin adelantar la neurona. | Repites la pregunta con claridad y silencias después. | Respondes tú. |
| — | Práctica guiada, ticket y cierre | — | **No es protagonista.** | Disponible si se te ocurre sumarla. | — |

**Frases de apoyo (no son guion):** si el curso no responde, «¿Alguien se anima a intentarlo con sus palabras?»; si se equivocan, «¿Cómo podemos comprobarlo con la tabla?».

## 4. Qué tiene el Colab para ti

- **Un solo cuaderno + slides animadas** (`/clase-42b/`). Los verificadores son `check_icn()`, `check_guiada()` y `check_ej0a()`, `check_ej0b()`, `check_ej1()`, `check_ej2()`, `check_ej3()`; dan ✅/⚠️ sin mostrar la solución. No recolectas resultados.
- **Las 3 columnas ya vienen elegidas por la clase** (dispositivos, video, horas desde el reinicio): los estudiantes solo escriben una **justificación** (por qué esas 3 sí y las otras 3 no). Si el curso propuso otras en el Haz Ahora (p. ej. temperatura), usa la tabla comparativa del Solucionario / la slide 10 como evidencia.
- **`check_icn()`** revisa que las listas coincidan con la tabla (en el orden dispositivos, video, horas), que `nombres_variables` esté en el mismo orden que las columnas y que `exactitud` sea la esperada. No muestra la solución.
- **`max_depth` (concepto 5):** «cuánto le dejamos pensar al computador»; con estos datos 1 → se equivoca en 2 de 16 filas, 2 → 1 de 16, 3 → 0 de 16 y 4 → igual que 3; por eso usamos 3 (el menor valor que no empeora los resultados). La slide 7 lo muestra con botones.
- **Concepto 6 (Revisar):** leer el árbol con `export_text` y los nombres de las **features** (las columnas que le dimos al modelo, en el mismo orden que en las listas) y después el accuracy. La slide 8 sigue el camino de la fila 17 por el árbol.
- **Mensaje honesto de la clase:** con solo 4 filas de test, un trío con una columna floja puede sacar 4/4 igual que el sensato (dispositivos, video, temperatura saca 4/4, pero tiene 0,70 de validación cruzada contra 0,90). Acertar 4 de 4 no prueba que el modelo es bueno. El Solucionario tiene la tabla comparativa.
- **Tiempos (80 min):** bienvenida 5 · Haz Ahora 8 · puente 3 · **ICN 34 (tipeo completo: 6–8 min de tipeo en total)** · **guiada 20 (12 de trabajo + 8 de revisión con una pareja al frente)** · ticket 5 · cierre 5.
- **La Práctica guiada es el ejercicio obligatorio.** Los Ejercicios 0a, 0b, 1, 2, 3 y 4 están al final del Colab como extras (tarea u opcionales).
- Los verificadores buscan las listas por nombre: **`entradas_train`, `etiquetas_train`, `entradas_test`, `etiquetas_test`**, los nombres de las features en **`nombres_variables`** y el accuracy en **`exactitud`**. Dilo en voz alta cuando lleguen al concepto 3.
- **El ticket NO está en el Colab:** el cuaderno termina con el link al Google Form. Proyecta las preguntas desde `Ticket de Salida.pptx` (carpeta de la clase; **no se pushea antes de dictar**) y al terminar revisan juntos las respuestas correctas (**D, B, C, A**). El tema a escribir en el Form: «De la tabla a las listas».
- El `Solucionario.ipynb` tiene todo el código ejecutable. **No lo subas a Classroom antes de dictar la clase.**

## 5. Reglas de uso de la voz

- **Es una voz más, no una fuente de verdad.** Si dice algo dudoso, es una oportunidad de pensamiento crítico: «¿cómo lo comprobamos con la tabla?».
- **Nada de datos personales** (nombres de estudiantes, notas, salud) en lo que se le dice a la voz.
- La conversación vive en **tu cuenta**; no la compartas ni la publiques.
- Los estudiantes **no** usan ChatGPT hoy. Su uso real depende de las verificaciones de edad y permisos pendientes del plan.

## 6. Plan B general

| Si pasa… | Haces… |
|---|---|
| Se cae la conexión o la voz no responde | Dictas tú el fila y lees las preguntas de la tabla (columna «Plan B»); la clase no depende de la voz. |
| La voz habla sin que la actives | Silencias el micrófono y sigues; si insiste, cierras la sesión de voz y continúas solo. |
| La voz se equivoca (cambia un nombre de columna o un dato) | Úsalo como momento de atención: «¿quién notó que cambió algo? ¿cómo lo comprobamos con la tabla?». |
| Responde algo inapropiado | La cortas de inmediato, lo hablas con el curso y sigues sin ella. |
| El ruido de la sala la confunde | Silencias el micrófono y repites tú, en voz clara, lo que dijo el curso. |
| scikit-learn no carga en Colab | Reinicia el entorno de ejecución y vuelve a correr la celda del verificador; si persiste, proyecta el Solucionario (salidas ya calculadas). |
| El tipeo se alarga más de 8 min | Pasa directo a la guiada con las listas del ICN a medio terminar: quien aún no termina el test puede copiar solo los 4 últimos filas. |

## 7. Después de la clase

- [ ] Anota en el `Historial.md` cuánto demoró el tipeo completo (insumo para decidir si la N°43 v2 debe traer el train ya tipeado).
- [ ] Anota qué columnas propuso el curso en el Haz Ahora y si la justificación escrita fue clara.
- [ ] Anota qué porcentaje terminó la guiada y cómo salió la revisión con la pareja al frente.
- [ ] Anota si `max_depth` («cuánto le dejamos pensar») quedó claro o si hubo que repetirlo (insumo para la N°43 v2 y la Prueba 1).
