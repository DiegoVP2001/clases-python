# Clase 46 — Prompting: guiar a la IA y evaluar bien su respuesta

**Estado:** Spec v3 **pendiente de gate de Diego** (2026-11-11). Cambios (Diego): objetivo reescrito; **se descartaron por completo las «Instrucciones personalizadas» de ChatGPT** (de esta clase y de las futuras: alterarían las respuestas de la Prueba 2); el ICN vuelve a 4 conceptos.
**Clase Picuino:** N/A — fila de IA (calendario v6) · **Fecha:** lun 23-nov-2026 · **Curso:** 3ro medio · **Duración:** 80 min
**Flujo:** liviano (Spec → Colab + Solucionario + Guía Docente Voz + slides + laboratorio + Ticket al Form → gate → push de la carpeta; el `Ticket de Salida.pptx` NO se pushea antes de dictar).
**Modalidad:** no se menciona en ningún material; la anuncia Diego.
**Regla de la clase:** hay **ChatGPT en vivo** (cada estudiante con su cuenta) y mucha interactividad: laboratorio en el sitio, constructor de prompt y duelo de prompts. El único código es el verificador `check_evidencia()`; lo demás es escribir prompts y analizar respuestas.

## Objetivo
Escribir prompts de IA de forma correcta con flexibilidad.

**OAs:** OA1, OA3 (por confirmar). **Actitud: Flexibilidad** (Diego, 2026-11-11): si la primera forma de pedir no funcionó, cambio mi prompt en vez de insistir con el mismo.

## ¿Por qué lo veremos?
Pedirle a ChatGPT que te ayude a estudiar sirve o no según cómo se lo pidas. Como ChatGPT responde con azar (lo vimos ayer), **tu prompt es lo que guía el camino**.

## Estructura de un buen prompt (4 partes mínimas; mismos nombres que el Temario y la Prueba 2)
- **Rol:** quién es la IA. · **Contexto:** situación, para qué, a quién. · **Formato:** lista, tabla, extensión, tono. · **Restricción:** qué debe respetar o evitar.

## Escenario continuo
**Una estudiante ficticia prepara la prueba de Biología del jueves y le pide ayuda a ChatGPT.** Tema distinto al de la Prueba 2 (nada de reconocimiento facial, cámaras ni asistencia).
- **Débil 1 (Haz Ahora, ICN, laboratorio):** «Explícame la fotosíntesis». Falta Rol, Contexto y Formato → respuesta genérica, larga y de nivel universitario.
- **Débil 2 (guiada, espejo de la Parte A de la prueba):** «¿Es mejor estudiar de noche o de día? Dame una recomendación.» Falta Contexto y Restricción → postura sin matices.
- **Débil 3 (duelo en vivo):** «Hazme preguntas para la prueba de historia». Falta nivel, cantidad y formato.

## Mapa de tiempos (80 min)
Bienvenida 5 (colega) · Haz Ahora 7 · Puente 3 · ICN 25 · Guiada 20 · Duelo 8 · Ticket 5 · Cierre 5 (≈78). Extras sin tiempo.

## Estructura

### Haz Ahora (colega como la compañera que pide ayuda; sin código)
Se proyecta el débil 1 y una respuesta de ejemplo (preparada). Preguntas cerradas:
1. ¿La respuesta dice para qué curso o nivel es?
2. ¿Menciona para cuándo es la prueba?
3. ¿Cuántos párrafos tiene?
4. ¿La entenderías en 5 minutos de estudio?

### Recordatorio puente
🔁 **Ayer (44):** ChatGPT predice la siguiente palabra y es estocástico · 🔀 **Hoy es distinto:** como tiene azar, el **prompt guía el camino** · ➡️ **Próxima clase (mar 24):** ética y 4D.

### ICN (4 conceptos; cada uno con Idea clave y fila de Resumen tabla)
Sin código Python: el «Escríbelo tú» consiste en escribir prompts.
1. **Misma pregunta, dos respuestas.** Cada estudiante envía el débil 2 en **dos conversaciones nuevas** y anota una cosa que cambió y una que se mantuvo, con cita entre comillas, usando «estocástico». *(Ensayo de la Parte B.)*
2. **Las 4 partes de un buen prompt.** Rol, Contexto, Formato, Restricción, con el débil 1 reescrito. → **Laboratorio A1:** clasificar frases en las 4 partes.
3. **Diagnosticar un prompt débil.** Qué parte falta + qué consecuencia se nota + **una cita** de la respuesta. Marco: «Le falta ___; por eso la respuesta ___, por ejemplo: "___"». → **Laboratorio A2 y A3:** elegir la parte que falta y la cita que lo prueba. *(Verificación del colega.)*
4. **Mejorar, comprobar y dejar evidencia.** *(Cierre del ciclo y puente a la guiada.)* Reescribir con el **Constructor de prompt** (4 casillas + botón Copiar), reenviar, citar lo que mejoró y decir **qué falta aún**; botón *Compartir* y comprobar que el link abre sin pedir permiso.
- **Resumen tabla (ICN):** Misma pregunta, dos respuestas · Rol / Contexto / Formato / Restricción · Diagnóstico (falta + consecuencia + cita) · Mejora y comprobación · Evidencia (link + cita).
- **Errores típicos:** decir «es mala» sin nombrar la parte · citar algo que no prueba nada · cambiar todo a la vez · link que pide permiso · parafrasear en vez de citar entre comillas.
- **Verificamos lo aprendido:** 2 preguntas por concepto en el Colab; respuestas solo en el Solucionario.

### Práctica guiada (único ejercicio obligatorio, 20 min)
El ciclo completo de la Parte A con el débil 2: **Link 1 → Diagnóstico → Prompt mejorado → Link 2 → ¿Funcionó?** (cita + qué falta aún). Formato canónico: narrativa + «El programa debe» (aquí «Tu entrega debe») + pistas 1–2 en `<details>` + resultado esperado (ejemplo de entrega, no la respuesta modelo). Celdas de texto abiertas para escribir; celda de código con `check_evidencia()` **opcional** que solo verifica la forma: el link empieza con `https://chatgpt.com/share/`, y diagnóstico y análisis tienen al menos una cita entre comillas (✅/⚠️ + pista; no juzga calidad). Respuestas modelo solo en el Solucionario. Revisión a viva voz con una pareja al frente.

### Duelo de prompts en vivo (8 min, sin código)
Dos estudiantes mejoran el **débil 3** por separado con el Constructor; Diego proyecta ambas respuestas; el curso vota cuál resolvió mejor el problema, justificando con **una cita**.

### Extras (sin tiempo, con pistas)
1. Ciclo completo con el débil 1. 2. Flexibilidad: cambiar **una sola** parte del prompt y anotar qué cambió en la respuesta.

### Ticket de Salida (Form + PPT local)
Colab: solo el link `https://forms.gle/sjRpbgmQzrpkEBsH9` y el tema «Prompting». **3 preguntas A–D con respuestas en letras distintas**, con bloque breve: (1) dado un prompt, qué parte falta; (2) dado un prompt débil y un fragmento de respuesta, qué cita prueba la consecuencia; (3) qué evidencia es válida (link que abre + cita textual). + autoevaluación 1–5 solo en el Form (no se proyecta). Genera `Ticket de Salida Respuestas.json`.

### Cierre (a viva voz)
Comprensión 1–5; «¿En qué momento cambiaste tu forma de pedir y qué pasó con la respuesta?»; aviso de logística: próxima clase ética y 4D.

## Colega (detalle en la Guía Docente Voz)
Solo habla cuando Diego la activa: bienvenida, Haz Ahora como la compañera que pide ayuda, verificación tras el concepto 3 («¿qué tres cosas tiene un buen diagnóstico?»). Nunca protagonista en guiada, duelo ni cierre. No inventa datos ni cifras. Nombre en material de estudiantes: «el colega del profesor».

## Interactivos — `sitio-hub/clase-46/`
- **Slides animadas** (modelo 42b/44): Haz Ahora · una por concepto 1–4 («Concepto N del cuaderno») · «Para pensar» · resumen en viñetas.
- **Laboratorio** (actividades en cadena, completar una abre la siguiente, sin contraseñas): **A1** clasificar frases en Rol/Contexto/Formato/Restricción · **A2** ¿qué parte falta? (débiles 1 y 3) · **A3** elegir la cita que prueba la consecuencia · **A4 Constructor de prompt** (4 casillas que arman el prompt completo + Copiar, para pegarlo en ChatGPT). Respuestas de ejemplo preparadas y rotuladas como tales; sirven de **plan B** si a alguien no le funciona ChatGPT.

## Pendientes para el gate
- Confirmar OAs (OA1, OA3).
- Confirmar que el lunes todos tienen acceso a ChatGPT (Diego dijo que sí; el plan B queda igual).
- Las respuestas de ejemplo del laboratorio se redactan a mano y se rotulan como preparadas.
- **Regla permanente (Diego, 2026-11-11):** no se enseñan ni se usan las instrucciones personalizadas de ChatGPT en ninguna clase del bloque ni en las pruebas (cambiarían las respuestas que se diagnostican y comparan en la Prueba 2). La Prueba 2 no se modifica.
