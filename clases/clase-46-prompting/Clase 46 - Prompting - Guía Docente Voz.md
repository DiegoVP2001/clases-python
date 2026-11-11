# Clase 46 — Guía docente: ChatGPT Voice como colega

**Solo para ti (no se sube a Classroom ni se proyecta).** Lunes 23-nov-2026 · 80 min · 3ro medio.

La voz es **un colega que plantea el escenario y verifica comprensión**, no un cuello de botella: tú explicas y los estudiantes trabajan con **su propio ChatGPT**; ella hace de la compañera que pide ayuda y pregunta. **Solo habla cuando tú la activas.** Nunca es protagonista en la práctica guiada, el duelo ni el cierre.

## 1. Antes de la clase (5 min)

- [ ] ChatGPT con **modo de voz probado** en el parlante de la sala; celular como respaldo de conexión.
- [ ] **Pega el prompt de arranque** (sección 2), espera «Listo, Colega al aire» y **silencia el micrófono**.
- [ ] Colab abierto y proyectado; ejecuta tú antes la celda «🔧 Ejecuta esta celda primero».
- [ ] **Prueba tú el botón Compartir** de ChatGPT y ábrelo en incógnito (así puedes mostrarlo al curso). Los estudiantes necesitan cuenta; **no** usar instrucciones personalizadas (regla permanente del bloque).
- [ ] Página de la clase (**un solo lugar**): https://clases-ia-mario-bertero.vercel.app/clase-46/ (7 pasos; cada uno con 🎬 para mostrar y 🧪 actividad; incluye el constructor de prompt y un **Plan B** con respuestas preparadas). El Colab es solo para escribir.
- [ ] **Duelo (opcional):** si sobra tiempo, elige a dos estudiantes y deja listo cómo proyectar sus respuestas.
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
> - Objetivo: escribir prompts de IA de forma correcta, con flexibilidad.
> - Ayer vimos que ChatGPT predice la siguiente palabra y es estocástico; hoy, como tiene azar, el prompt guía el camino.
> - Historia: una estudiante de tu curso (ficticia) prepara la prueba de Biología del jueves y le pidió ayuda a ChatGPT con el prompt «Explícame la fotosíntesis». La respuesta fue de tres párrafos muy técnicos, sin decir para qué curso ni para cuándo.
> - Un buen prompt tiene 4 partes: Rol (quién es la IA), Contexto (situación, para qué, a quién), Formato (lista, tabla, extensión, tono) y Restricción (qué debe respetar o evitar).
> - Un buen diagnóstico dice qué parte falta, qué consecuencia se nota en la respuesta y cita una frase de ella.
> - No des tu opinión sobre cuál parte es más importante; pregunta al curso.
>
> Responde solo: «Listo, Colega al aire».

## 3. Momentos de la voz (las frases de activación son sugerencias)

| # | Cuándo | Frase de activación | Qué hace la voz | Qué haces tú | Plan B |
|---|---|---|---|---|---|
| 1 | **Bienvenida** (0–5) | «Colega, da la bienvenida al curso.» | Saluda, **espera que el curso la salude** y pide que alguien lea el objetivo. | Dejas que el curso salude, silencias y, cuando alguien lee el objetivo, tomas la clase. | Tú saludas y pides leer el objetivo. |
| 2 | **Haz Ahora** (5–12) | «Colega, plantea el caso de la estudiante.» | Cuenta la historia de la estudiante de Biología y plantea las **4 preguntas una por una** (¿dice el nivel?, ¿dice cuándo es la prueba?, ¿cuántos párrafos?, ¿se entiende en 5 minutos?), esperando al curso. | Das la palabra al curso (micrófono silenciado), muestras en la slide 1 los botones de apoyo y anotas: no / no / 3 párrafos / palabras sin explicar. | Lees las 4 preguntas del Colab. |
| 3 | **ICN, tras el paso 3** (~2 min) | «Colega, verifica comprensión del diagnóstico.» | Pregunta a dos estudiantes: «¿qué tres cosas tiene un buen diagnóstico?» y «¿por qué sirve más una cita que decir que la respuesta es mala?». | Silencias entre respuestas y repites lo que dicen. | Haces tú esas dos preguntas. |
| 4 | **En cualquier momento** | «Colega, responde la pregunta de…» | Responde una pregunta abierta, sin inventar. | Repites la pregunta con claridad y silencias. | Respondes tú. |

**La voz NO participa** en: paso 1 (el curso trabaja con su ChatGPT), paso 2, paso 4, práctica guiada, duelo, ticket ni cierre.

## 4. Cómo conducir la clase (80 min)

| Min | Momento | Qué haces |
|---|---|---|
| 0–5 | Bienvenida (colega) | Ver momento 1. |
| 5–12 | Haz Ahora (colega) | Ver momento 2; respuestas en el Solucionario. |
| 12–15 | Puente | Ayer: estocástico · Hoy: el prompt guía el camino · Martes 24: ética y 4D. |
| 15–23 | **Paso 1 · ¿Qué es un prompt?** | Defines *prompt* en la página. Todos envían «Explícame la fotosíntesis» **dos veces** (conversaciones nuevas). Colab: qué cambió, qué se mantuvo, por qué (sin citas). |
| 23–33 | **Paso 2 · Las 4 partes** | Construyes el prompt **con el curso** en la página (preguntas guía por parte; tú escribes lo que decidan). Lo pegan en ChatGPT. El prompt modelo **no se muestra** (está en el Solucionario). |
| 33–41 | **Paso 3 · Qué le falta** | Actividad en la página: marcan lo que falta (una, varias o ninguna) y eligen la cita. Colab: su diagnóstico del Paso 1. Aquí va la verificación del colega. |
| 41–53 | **Paso 4 · Otra situación** | Correo al profesor jefe por tres pruebas el mismo jueves: envían el débil, arman su prompt en el constructor, lo envían y comparan. Colab: antes / ahora / qué falta. |
| 53–68 | **Práctica guiada** | **5 preguntas en orden** (link 1 · diagnóstico · prompt mejorado · link 2 · ¿funcionó?), cada una con su cuadro en el Colab y sus instrucciones en la página; `check_evidencia()` revisa solo la forma. Revisión a viva voz. *(Duelo de prompts: opcional si sobra tiempo.)* |
| 68–73 | Ticket | Proyectas `Ticket de Salida.pptx` (solo local) y luego el Form. |
| 73–78 | Cierre | Comprensión 1–5; «¿En qué momento cambiaste tu forma de pedir y qué pasó con la respuesta?». |

## 5. Si algo falla

- **Un estudiante no puede usar ChatGPT:** que trabaje con las **respuestas de ejemplo preparadas** de la página (desplegable «Plan B») o las proyectes tú; el diagnóstico y la mejora se hacen igual.
- **El link pide permiso:** pedir que lo abra en incógnito; si falla, volver a compartir.
- **Respuestas de ChatGPT muy distintas a las del ejemplo:** es esperable (es estocástico): lo que importa es que citen **su** respuesta.
- **Datos personales:** recuerda no escribir nombre completo, RUT ni dirección en los prompts: el link los muestra.
