# Clase 46 — Prompting: guiar a la IA y evaluar bien su respuesta

**Estado:** Spec v4 (2026-11-11). v3 aprobada por Diego; **v4 = reestructura pedida por Diego** (pendiente de gate junto con el Colab): (1) el paso 1 define qué es un prompt y es con ChatGPT (mismo prompt dos veces, **sin citas**); (2) el paso 2 se **construye con el curso** (el prompt modelo queda solo en el Solucionario); (3) el paso 3 es de identificar qué falta (una, varias o ninguna parte); (4) el paso 4 es **otra situación** para probar ahora; (5) **un solo lugar**: la página `clase-46/` es el guion (🎬 para mostrar + 🧪 actividad) y el **Colab es solo para escribir**, con una hoja de ruta; (6) el duelo pasa a **opcional**.
**Clase Picuino:** N/A — fila de IA (calendario v6) · **Fecha:** lun 23-nov-2026 · **Curso:** 3ro medio · **Duración:** 80 min
**Flujo:** liviano. **Modalidad:** no se menciona en ningún material; la anuncia Diego. **Regla permanente:** sin «Instrucciones personalizadas» de ChatGPT.

## Objetivo
Escribir prompts de IA de forma correcta con flexibilidad.

**OAs:** OA1, OA3 (por confirmar). **Actitud: Flexibilidad:** si la primera forma de pedir no funcionó, cambio mi prompt en vez de insistir con el mismo.

## ¿Por qué lo veremos?
Pedirle a ChatGPT que te ayude a estudiar sirve o no según cómo se lo pidas. Como ChatGPT responde con azar (lo vimos ayer), **tu prompt es lo que guía el camino**.

## Dónde se hace cada cosa (un solo lugar)
- **Página `https://clases-ia-mario-bertero.vercel.app/clase-46/`** = el guion de la clase. Cada paso tiene **🎬 Para mostrar** (lo proyecta Diego) y **🧪 Actividad** (lo hacen los estudiantes, con enlaces `#p1`…`#guiada`). Incluye el constructor de prompt (botón Copiar), las actividades de «qué falta» y un **Plan B** con respuestas preparadas.
- **Colab** = solo para escribir las respuestas; abre con una **hoja de ruta** (Paso → qué hacemos → página / ChatGPT / Colab).
- **ChatGPT** = cada estudiante con su cuenta, en otra pestaña, siempre en **conversación nueva**.

## Escenario
Una estudiante ficticia prepara la **prueba de Biología del jueves** y le pide ayuda a ChatGPT. Ningún tema toca cámaras, reconocimiento facial ni asistencia (Prueba 2).
- **Pasos 1–3:** «Explícame la fotosíntesis» (respuesta de ejemplo técnica, 3 párrafos).
- **Paso 4:** el curso tiene **tres pruebas el mismo jueves** y quiere pedirle al **profesor jefe** que cambie una → «Escribe un correo para cambiar una prueba».
- **Guiada:** «¿Es mejor estudiar de noche o de día? Dame una recomendación.» (espejo de la Parte A).
- **Duelo (opcional):** «Hazme preguntas para la prueba de historia».

## Mapa de tiempos (80 min)
Bienvenida 5 (colega) · Haz Ahora 7 · Puente 3 · Paso 1: 8 · Paso 2: 10 · Paso 3: 8 · Paso 4: 12 · Guiada 15 · Ticket 5 · Cierre 5 (≈78). Duelo y extras sin tiempo.

## Estructura

### Haz Ahora (colega como la compañera que pide ayuda; sin código)
Se proyecta «Explícame la fotosíntesis» y la respuesta de ejemplo. Preguntas: ¿dice para qué curso o nivel es? · ¿menciona para cuándo es la prueba? · ¿cuántos párrafos? · ¿la entenderías en 5 minutos? Respuestas en el Colab.

### Puente
🔁 Ayer: ChatGPT predice la siguiente palabra y es estocástico · 🔀 Hoy: como tiene azar, el prompt guía el camino · ➡️ Martes 24: ética y 4D.

### ICN (4 pasos; cada uno con Idea clave; verificación del colega; sin código)
1. **¿Qué es un prompt?** Definición: *el texto que le escribes a una IA para pedirle algo*. Cada estudiante envía **«Explícame la fotosíntesis»** en **dos conversaciones nuevas**. Colab: **qué cambió, qué se mantuvo y por qué** («estocástico»). **Sin citas.**
2. **Las 4 partes (Rol, Contexto, Formato, Restricción): se construye con el curso.** En la página, Diego pregunta al curso por cada parte («¿quién queremos que sea la IA?»…) y escribe lo que decidan; el prompt modelo («Eres un profesor de Biología…») **no se muestra**, queda solo en el Solucionario. Los estudiantes pegan el prompt armado en una conversación nueva. Colab: el prompt y **qué cambió** frente a la primera respuesta.
3. **¿Qué le falta a este prompt?** Qué parte falta + qué consecuencia + **cita**. Actividad en la página: ① marcan lo que falta en 4 prompts (**una parte, varias o ninguna**); ② eligen la cita que prueba la consecuencia. Colab: su diagnóstico de la respuesta del Paso 1 (con cita).
4. **Otra situación: mejorar y comprobar.** Se envía el prompt débil de la situación nueva, cada estudiante **arma su prompt** en el constructor (campos vacíos), lo envía en otra conversación nueva y compara. Colab: cita de antes, prompt con las 4 partes, cita de ahora, **qué mejoró** y **qué falta aún**.
- **Resumen tabla** y **errores típicos** en el Colab (con «no creer que el link sirve si pide permiso» y «no parafrasear»).

### Práctica guiada (único ejercicio obligatorio, 15 min)
El ciclo completo de la Parte A con «noche o día»: Link 1 → Diagnóstico → Prompt mejorado → Link 2 → ¿Funcionó? Se escribe **en la celda de código** (variables con triples comillas) y `check_evidencia()` revisa solo la forma (links `https://chatgpt.com/share/…` y citas entre comillas). Pistas 1–2. Revisión a viva voz.

### Duelo de prompts (opcional, si sobra tiempo)
Dos estudiantes mejoran por separado «Hazme preguntas para la prueba de historia»; el curso vota cuál resolvió mejor con una cita.

### Extras (sin tiempo)
1. Ciclo completo con el prompt de historia. 2. Flexibilidad: cambiar una sola parte.

### Ticket de Salida (Form + PPT local)
Link `https://forms.gle/sjRpbgmQzrpkEBsH9`, tema «Prompting». 3 preguntas A–D (respuestas D, C, A): qué parte falta · qué cita prueba la consecuencia · qué evidencia es válida. + autoevaluación 1–5 solo en el Form. Nunca en el Colab.

### Cierre (a viva voz)
Comprensión 1–5; «¿En qué momento cambiaste tu forma de pedir y qué pasó con la respuesta?».

## Colega
Solo habla cuando Diego la activa: bienvenida, Haz Ahora, verificación tras el paso 3. Nunca en la guiada, el duelo ni el cierre. Nombre en material de estudiantes: «el colega del profesor».

## Pendientes para el gate
- Confirmar OAs (OA1, OA3).
- Confirmar con ChatGPT real el prefijo de los links compartidos.
- Deploy a Vercel y commit/push tras la aprobación (el `Ticket de Salida.pptx` queda solo local).
