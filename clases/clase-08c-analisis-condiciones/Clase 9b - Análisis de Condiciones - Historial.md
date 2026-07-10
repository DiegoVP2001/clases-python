# Historial — Clase 9b: Análisis de Condiciones

## 2026-06-02 — Especificación aprobada

- **Objetivo:** Analizar condiciones Python incorrectas o imprecisas para identificar el error lógico y corregirlo, con rigor.
- **Habilidad:** Bloom 4 (Análisis) — leer y corregir condiciones con caso límite como evidencia
- **Actitud:** Rigor
- Estructura aprobada tras diseño iterativo: propuesta de habilidad (3 opciones) → ticket de salida de muestra → actitud (3 opciones, 1 palabra) → estructura completa
- Esta clase se inserta entre 8a (comparadores) y 8b (operadores lógicos)
- Primera clase del currículo que usa el nuevo formato de objetivo: `[verbo] [contenido] [para + propósito], [actitud]`

## 2026-06-02 — Colab v1 generado

- **Archivo:** `Clase 9b - Análisis de Condiciones - Clase.ipynb`
- **Generado con:** skill `generar-colab-clase` v5
- **Ajustes al spec antes de generar:**
  - Corregido formato del cierre (sin dos puntos, contenido en línea siguiente)
  - Cambiado `**Dinámica:**` → `**Pasos guiados:**` en guiada
  - `>> output` en ejemplos del ICN convertido a `# >> output`
  - Agregado `**Código con error:**` con Python real en guiada, 3 ejercicios y ticket
  - Rediseñados ejercicios 2 y 3 para usar errores de caso límite limpios (`<=` vs `<`, `>=` vs `>`)
  - Agregadas soluciones a todos los ejercicios
- **Cambio en `crear_colab.py`:** soporte para campo `codigo_error` en guiada, ejercicios y ticket (genera celda ejecutable con el código erróneo antes de la celda de solución)

## 2026-06-03 — Colab v3 regenerado (nuevo enfoque pedagógico: lenguaje natural → código)

- **Feedback aplicado:**
  - Eliminado el código de muestra ("código con error") de todos los ejercicios — ahora el estudiante parte siempre desde el enunciado en lenguaje natural
  - Las preguntas de análisis inducen hacia el operador sin nombrarlo explícitamente
  - Los enunciados mencionan al "usuario que ingresa" para implicar `input()` sin decirlo
  - Contextos actualizados a CyberDay (evento de esta semana) + intereses del curso (Steam, Discord, Spotify, tienda gaming, Cuenta RUT)
  - Pregunta 2 de la guiada: eliminado el hint "`>` o `>=`" — ahora solo pregunta "¿Qué operador lo representa mejor?"
- **Cambios en `crear_colab.py`:**
  - `parsear_ticket`: extrae `preguntas` numeradas del tarea para generar celda de respuestas editable
  - `generar_seccion_guiada_intro`: header de pasos cambiado a "**Antes de escribir código, analiza el enunciado:**"
  - `construir_notebook` guiada: agrega celda de respuestas editables proporcional al número de pasos
  - `construir_notebook` ticket: agrega celda de respuestas editables si hay preguntas numeradas
  - `construir_notebook` independiente: renombrado "# Tu código — Parte A" (era "# Pregunta 4...")
- **Resultado:** 40 celdas. Sin código de muestra en ninguna parte. Celda de respuestas editables en guiada (3 slots), ejercicios independientes (3 slots por Parte A) y ticket (2 slots).
- **Estado:** Colab de clase aprobado — 2026-06-03

## 2026-06-03 — PPT generado

- **Archivo:** `Clase 9b - Análisis de Condiciones - Presentación.pptx`
- **Generado con:** skill `generar-ppt-clase` v5 + `crear_ppt.py`
- **Slides:** Bienvenida → Objetivo/Propósito/Reglas → Haz Ahora → ICN×3 → Errores típicos (7 slides)
- **ICN:** 3 conceptos clásicos (sin fusión — densidad individual ~11 filas c/u)
  - Concepto 1: condición correcta para todos los datos (definición + ejemplo 4 líneas + idea clave)
  - Concepto 2: caso límite (definición + ejemplo comparativo 4 líneas + idea clave)
  - Concepto 3: errores frecuentes (texto breve + tabla de operadores 5 filas + idea clave)
- **Fix aplicado en `crear_ppt.py`:** función `_para_ppt()` que strips `**bold**` / `*italic*` markdown para display en PPT. Se aplica solo en puntos de render (Haz Ahora, definiciones, ideas, objetivo/propósito) — no en el texto estructural que el parser necesita intacto.
- **Estado:** PPT aprobado — 2026-06-03

## 2026-06-03 — Colab de ejercicios generado

- **Archivo:** `Clase 9b - Análisis de Condiciones - Ejercicios.ipynb`
- **Generado con:** skill `generar-colab-ejercicios` + `crear_colab_ejercicios.py`
- **Total ejercicios:** 5 (4 de práctica base + 1 desafío opcional ⭐)
- **Contextos:** Brawl Stars, micro escolar, estacionamiento de mall, tarifa del bus, torneo de esports
- **Errores cubiertos:** `>→>=` (Ej1), `<→<=` (Ej2), `>=→>` (Ej3), `<=→<` (Ej4), `>` con dos inputs (Ej5⭐)
- Misma estructura pedagógica del Colab de clase: situación en lenguaje natural → análisis → escritura desde cero
- Las 3 preguntas de análisis están embebidas en el enunciado (no como celda separada)
- **Estado:** Colab de ejercicios generado — 2026-06-03

## 2026-06-02 — Colab v2 regenerado (ejercicios Parte A/B)

- **Feedback aplicado:**
  - Ejercicios rediseñados con estructura Parte A (análisis) + Parte B (escritura desde cero)
  - Eliminados `> *` blockquotes en ejercicios independientes
  - `\$` escapado en Haz Ahora, Ticket y Ejercicio 3 para evitar LaTeX en Colab
- **Nuevos ejercicios:** Torneo de gaming (ELO), App de transporte (bus), Sistema de fidelidad (\$20.000)
- **Cambios en `crear_colab.py`:**
  - `parsear_independiente`: soporte para `parte_a`, `parte_b`, `solucion_a`, `solucion_b`
  - `construir_notebook`: rama Parte A/B (6 celdas por ejercicio: código error + Parte A markdown + respuestas editable + code Pregunta 4 + Parte B markdown + code Parte B)
  - `generar_ejercicio_independiente`: eliminado `> *` blockquote, formato limpio para "Ejemplo:"
  - `generar_seccion_soluciones`: `<details>` separados para Parte A y Parte B
- **Resultado:** 43 celdas, 6 bloques de soluciones por ejercicios (Ej1A, Ej1B, Ej2A, Ej2B, Ej3A, Ej3B)
