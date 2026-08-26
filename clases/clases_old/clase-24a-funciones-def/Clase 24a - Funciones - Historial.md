# Historial — Clase 24a

## 2026-08-12 — Especificación aprobada
- Objetivo: Construir funciones propias con `def` que resuelvan una tarea puntual, con claridad.
- Actitud elegida tras iterar dos rondas de opciones: Claridad (descartadas: Orden, Método, Precisión, Criterio, Responsabilidad, Autonomía).
- Objetivo ajustado por Diego: se quitó la mención a "sin leer el código interno" y a "parámetros y return" del enunciado del objetivo — quedó centrado en `def` + tarea puntual + claridad, sin enumerar toda la sintaxis.
- Estructura de 5 pasos aprobada con dos rondas de ajuste de contexto:
  - Ronda 1: propuesta completa con Haz Ahora/Guiada en la Feria de las Pulgas (descuento a socios del club de coleccionistas) y Ejercicio 2 en el kiosco del liceo (cálculo de vuelto).
  - Ronda 2 (aprobada): Haz Ahora/Guiada se movieron al kiosco del liceo (descuento CEE) y el Ejercicio 2 pasó a Club Deportivo de Isla de Maipo (cuota mensual × meses atrasados, sin condicional) para no duplicar la lógica de descuento por categoría que ya cubre la Guiada.
- **Cambio sistémico registrado en el `CLAUDE.md` raíz (reglas 15/16/20), vigente desde esta clase en adelante:** Práctica Independiente pasa de 2 obligatorios + 1 desafío a **3 obligatorios (2 directos + 1 contextualizado/complejo) + 1 desafío opcional**; la Práctica Guiada sube su nivel de dificultad para igualar al Ejercicio 3. Motivación de Diego: que esta clase sirva de modelo directo para el Control del Lunes Estándar de Funciones (24-ago).
- Ajuste explícito de Diego: sin ninguna conexión textual entre esta clase y el Lunes Estándar — se diseñó de forma autónoma, sin alusiones.
- Pendiente: Clase 24b (Picuino N°20 — valores por omisión), a diseñar como clase separada para el jueves 20-ago.

## 2026-08-13 — Colab de clase aprobado
- Archivos: `Clase 24a - Funciones - Clase.ipynb`, `Clase 24a - Funciones - Solucionario.ipynb`, `Clase 24a - Funciones - Ticket de Salida Respuestas.json`.
- Generados con la skill `generar-colab-clase`. Notebook ejecutado sin errores (`nbconvert --execute`); outputs del ICN verificados contra el spec.
- **Bug de parser corregido en el spec (técnico, no cambia contenido):** las 4 tablas "Resultado esperado" con `input()` (Guiada, Ejercicios 1-3) estaban escritas como tabla markdown (`| Ejemplo 1 | Ejemplo 2 |`), formato que el generador no reconoce y descarta en silencio — se convirtieron a la tabla HTML canónica (mismos datos), sin lo cual esas cuatro secciones habrían quedado vacías en el notebook de estudiante.
- **Mismo bug detectado en la Clase 22 ya publicada** (sus Ejercicios 1-4 perdieron el "Resultado esperado" en el `.ipynb` subido) — pendiente que Diego decida si corregirla también.

## 2026-08-13 — Ticket de Salida (PPT) aprobado
- Archivo: `Clase 24a - Funciones - Ticket de Salida.pptx` (8 slides: portada + 3 preguntas + pantalla del Form + 3 slides de revisión).
- Generado con `crear_ppt_ticket.py`. Respuestas correctas: P1=B, P2=C, P3=A.
- **No se commitea ni pushea a GitHub todavía** — regla fija de la skill (repo público, el archivo expone preguntas y respuestas): se sube recién después de dictada la clase.

## 2026-08-13 — Retrofit de autochequeo en la Práctica Independiente
- Esta clase se generó (2026-08-13) antes de que el autochequeo pasara a ser default en `disenar-clase`/`generar-colab-clase` (mismo día, cambio de política aplicado después). Diego pidió corregirlo.
- Spec actualizado: `**Celda de configuración:**` (preámbulo reutilizable del "Verificador por salida") + una `**Celda de verificación:**` por ejercicio (Ejercicios 1-4, incluido el desafío).
- Ejercicios 1-3 y el desafío usan `input()`: cada `verificar_ejercicio_N()` imprime primero un aviso pidiendo reingresar los mismos datos del Ejemplo 1 (o del ejemplo único del desafío), igual que el patrón ya usado en `clase-21b-continue-break`.
- `Clase.ipynb` y `Solucionario.ipynb` regenerados con `generar-colab-clase`, ejecutados sin errores. Probado además con las 4 soluciones de referencia (input hardcodeado en vez de `input()` real) contra sus verificadores: los 4 dieron "✅ ¡Perfecto!".

## 2026-08-17 — Clase Impresa (versión PDF sin computador) — v1 rechazada, rediseño aprobado
- **v1:** transcripción casi literal del `Clase.ipynb` completo a `.tex`/`.pdf` (7 páginas, compiló bien con tectonic, tildes/ñ correctas). Diego evaluó que una copia textual **no sirve como material de estudio** y pidió un rediseño de contenido y de sistema visual (tomando como referencia `a_tex_Guía Final Funciones Trigonométricas.tex` + `logo.png`). Quedó documentado en `Clase 24a - Funciones - Prompt Rediseño Impresa.md` para que otra sesión lo retomara.
- **Rediseño (esta sesión), decisiones acordadas con Diego vía interview + maquetas de texto antes de escribir el `.tex`:**
  - Haz Ahora fusionado (sin las 4 preguntas separadas) como párrafo narrativo expandido: explica el enredo concreto del descuento del kiosco y por qué el contenido de la clase (funciones) lo resuelve — a pedido explícito de Diego, con foco en que el cálculo se repite igual para cada persona de la fila.
  - Objetivo + Propósito en la portada.
  - Práctica Guiada fusionada con el ICN: viene después de explicar los 4 conceptos, como un `estrategiabox` verde con "Paso 1/2/3" + programa completo armado (mismo código que sería la solución de la Guiada) — implica que esta estudiante ve la solución completa de la Guiada en papel, algo que sus compañeros no ven en `Clase.ipynb` (se acordó como diferencia deliberada: ella estudia sola, sin el andamiaje de la clase en vivo).
  - Errores típicos como `alertabox` roja.
  - Nota agregada tras el título de "Práctica Independiente": revisar respuestas en el celular contra el Solucionario subido a Classroom.
  - Cierre motivacional corto y cercano al final del documento (nuevo default, pedido en esta sesión) — sin nombrar a la estudiante ni su situación.
  - Sin Ticket de Salida ni Cierre reflexivo del Colab, en ninguna forma.
  - Arquitectura: `.tex` redactado a mano (no por script) — decisión explícita de Diego, dado que el contenido requiere criterio editorial por clase.
- **Motor LaTeX confirmado con tectonic:** `fontspec` + `babel[spanish,es-noshorthands]` (no `inputenc`/`fontenc`, sin probar), `tcolorbox[most]`, `fancyvrb` para código, `fancyhdr`, `titlesec`, a4paper. Cajas nuevas: `formulabox` (azul, vocabulario), `alertabox` (roja, errores), `estrategiabox` (verde, ejemplo guiado) — mismo sistema de color que la guía de trigonometría.
- **Bug encontrado y corregido:** una coma dentro del título de un `tcolorbox` (`\begin{estrategiabox}[texto, con coma]`) rompe la compilación — tcolorbox la interpreta como separador de opciones (`pgfkeys Error`). Se resolvió reemplazando la coma por "---".
- Archivo final: `Clase 24a - Funciones - Clase Impresa.tex`/`.pdf` (7 páginas), reemplaza a la v1 con el mismo nombre.
- **Aprobado por Diego.** Se formalizó como flujo permanente: nueva skill `generar-clase-impresa` (`.claude/skills/generar-clase-impresa/SKILL.md`) + nuevo workflow opcional/on-demand documentado en el `CLAUDE.md` raíz del proyecto (§ "Workflow opcional: versión impresa de una clase", nuevo Tipo `Clase Impresa` en "Organización de archivos"). No se genera automáticamente para cada clase — se activa solo cuando un estudiante puntual lo necesita.
