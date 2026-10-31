# Clase 41 — Guía docente: ChatGPT Voice como colega

**Solo para ti (no se sube a Classroom ni se proyecta).** Lunes 2-nov-2026 · 80 min · 3ro medio.

La voz es **un colega que verifica comprensión**, no un cuello de botella: tú explicas, ella pregunta al curso y resuelve dudas. **Solo habla cuando tú la activas.** La opera solo tu cuenta; los estudiantes no necesitan cuenta.

## 1. Antes de la clase (5 min)

- [ ] Cuenta de profesor abierta en ChatGPT, **modo de voz probado** con el parlante de la sala (volumen y eco).
- [ ] **Conexión estable.** Si la red del liceo es inestable, ten el celular como respaldo.
- [ ] **Pega el prompt de arranque** (sección 2) y espera su confirmación («Listo, Colega al aire»). Después **silencia el micrófono**: ella responde ante cualquier pausa o ruido, así que no dependas solo del prompt.
- [ ] Página abierta en `clases-ia-mario-bertero.vercel.app/clase-41/` y Colab abierto (el objetivo y los diagramas se proyectan desde ahí).
- [ ] Los **códigos** de la sección 4 a la mano (puedes cambiarlos en la constante `CODIGOS` al inicio del HTML antes de la clase).
- [ ] Plan B listo: esta guía impresa o en otra pantalla.

## 2. Prompt de arranque (copiar y pegar)

> Eres «Colega», un colega docente que me acompaña en una clase de 3ro medio en un liceo de Isla de Maipo, Chile. Hablas español de Chile, con tono cercano y simple, para estudiantes de 16 y 17 años.
>
> **Reglas:**
> 1. Solo hablas cuando te lo pido con la frase «Colega, …». Si no te hablo, guardas silencio total.
> 2. Tus intervenciones duran como máximo 20 segundos.
> 3. Te diriges al curso («chicos y chicas»), no a mí.
> 4. Haces preguntas al curso y esperas la respuesta. No las respondes tú.
> 5. No inventas datos sobre el liceo, el curso ni las personas. Si no sabes algo, lo dices.
> 6. No das discursos ni resumes la clase si no te lo pido.
> 7. Si alguien se equivoca, no lo corriges de inmediato: preguntas «¿cómo podemos comprobarlo?».
>
> **Datos de la clase de hoy (úsalos tal cual, no agregues otros):**
> - Objetivo: ubicar ejemplos de IA en el mapa (reglas, ML, DL e IA generativa) y ordenar el recorrido de los datos hasta la evaluación de un modelo, con curiosidad.
> - Definiciones: *regla* es una instrucción que escribe una persona y que no cambia sola; *patrón* es algo que se repite en los datos y que la máquina descubre sola mirando muchos ejemplos; *IA* son máquinas que hacen tareas que normalmente requieren inteligencia humana; *Machine Learning* es cuando la computadora descubre patrones en los datos y decide sin que le indiquen cómo; *Deep Learning* es ML con redes neuronales de muchas capas; *IA generativa* produce contenido nuevo a partir de lo que aprendió.
> - Recorrido de noviembre: lun 2 mapa de la IA y pipeline · mar 3 primer clasificador · jue 5 construir una neurona · lun 9 entrenar una red y medir aciertos · mar 10 mini-LLM · jue 12 Evaluación 1 · lun 16 usar ChatGPT con instrucciones claras · jue 19 Evaluación 2 (el mar 17 no hay clase) · lun 23 ética · mar 24 integración · jue 26 Evaluación 3. Hay dos notas: el promedio de E1 y E2, y E3.
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos de la voz

| # | Cuándo | Frase de activación | Qué hace la voz | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida** (min 0–5) | «Colega, da la bienvenida al curso.» | Saluda, **espera a que el curso le devuelva el saludo** y pide que alguien lea el objetivo. | Activas el micrófono, dejas que el curso salude, silencias, y cuando alguien lee el objetivo (desde el Colab) tomas la clase. | Tú saludas y pides que alguien lea el objetivo. |
| 2 | **Haz Ahora** (5–15) | «Colega, plantea el diagnóstico.» | Hace las 5 preguntas **una por una**, esperando respuestas tentativas. | Das la palabra al curso entre pregunta y pregunta (micrófono silenciado), anotas en la pizarra ideas y confusiones. | Lees las 5 preguntas del Colab. |
| 3 | **Recorrido** (15–23) | «Colega, presenta el recorrido de noviembre.» | Presenta la unidad como **la última del curso** y recorre la ruta con los datos que le pasaste. | Completas lo que ella no sabe: cómo se forman las dos notas y qué hace cada uno en clase. | Lees la tabla «Nuestro recorrido» del Colab. |
| 4 | **ICN 1 · mapa** (tras tu explicación con el Diagrama 1) | «Colega, verifica comprensión del mapa.» | Pide a dos estudiantes que expliquen **con sus palabras** la diferencia entre regla y patrón; pregunta dónde ubicarían «una calculadora» y por qué; resuelve dudas. | Silencias entre respuestas; repites en voz alta lo que dicen si la voz no los escucha. | Haces tú esas dos preguntas. |
| 5 | **ICN 2 · pipeline** (tras tu explicación con el PPT paso a paso; la diapositiva «Resumen» es un buen punto) | «Colega, verifica comprensión del pipeline.» | Pregunta «¿por qué guardamos datos aparte?» y «¿qué diferencia hay entre entrenar y predecir?»; resuelve dudas. | Igual que el momento 4. | Haces tú esas dos preguntas. |
| — | Actividades, ticket y cierre | — | **No es protagonista.** | Disponible si se te ocurre sumarla. | — |

**Frases de apoyo (no son guion):** si el curso no responde, «¿Alguien se anima a intentarlo con sus palabras?»; si se equivocan, «¿Cómo podemos comprobarlo?».

## 4. Códigos de la página (se entregan justo antes de cada actividad)

| Actividad | Qué es | Código | Cuándo lo entregas |
|---|---|---|---|
| M1 | Regla o patrón | **417** | Tras explicar *regla y patrón* con el Diagrama 1 |
| M2 | Ubica en el mapa | **238** | Tras explicar IA, ML, DL e IA generativa, cuando el curso ya terminó M1 |
| M3 | El caso dudoso | **659** | Tras explicar «cuando algo no calza», cuando ya terminó M2 |
| **Página 2** + P1 | Ordena el recorrido (el código abre la página 2 y P1) | **172** | Tras explicar los 7 pasos con el PPT o el Diagrama 2: es un cambio de página |
| P2 | Variables y etiqueta | **884** | Tras explicar variables y etiqueta |
| P3 | Entrenar o predecir | **306** | Tras explicar entrenar y predecir |
| P4 | Caza el error | **591** | Tras explicar «la prueba se guarda aparte» |
| **Página 3** + TK | Ticket de salida (el código abre la página 3 y el ticket) | **725** | Al terminar P4 y antes del cierre: es un cambio de página |

Los códigos solo regulan el ritmo: el archivo se puede inspeccionar, así que no son seguridad. Si quieres otros, cámbialos en `CODIGOS` (al inicio del `<script>` del HTML) y regenera con `fuentes/construir.py`.

## 5. Reglas de uso de la voz

- **Es una voz más, no una fuente de verdad.** Si dice algo dudoso, es una oportunidad de curiosidad crítica: «¿cómo podemos comprobarlo?».
- **Nada de datos personales** (nombres de estudiantes, notas, salud) en lo que se le dice a la voz.
- La conversación vive en **tu cuenta**; no la compartas ni la publiques.
- Los estudiantes **no** usan ChatGPT hoy. Su uso real parte el lun 16 y depende de las verificaciones de edad y permisos pendientes del plan.

## 6. Plan B general

| Si pasa… | Haces… |
|---|---|
| Se cae la conexión o la voz no responde | Lees tú la intervención escrita de la tabla (columna «Plan B»); la clase no depende de la voz. |
| La voz habla sin que la actives | Silencias el micrófono y sigues; si insiste, cierras la sesión de voz y continúas solo. |
| La voz se equivoca | Lo usas como momento de Discernimiento sin nombrar las 4D: «¿cómo podemos comprobarlo?». |
| Responde algo inapropiado | La cortas de inmediato, lo hablas con el curso y sigues sin ella. |
| El ruido de la sala la confunde | Silencias el micrófono y repites tú, en voz clara, lo que dijo el curso. |

## 7. Después de la clase

- [ ] Anota en el `Historial.md` qué momento de la voz funcionó y cuál no (insumo para la N°42).
- [ ] Anota qué ideas del diagnóstico cambiaron al cierre.
- [ ] Si los códigos se filtraron o alguien se adelantó, cámbialos para el curso de la tarde (si hay otro).
