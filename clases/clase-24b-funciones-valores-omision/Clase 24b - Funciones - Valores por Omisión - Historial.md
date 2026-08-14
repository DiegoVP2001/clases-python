# Historial — Clase 24b

## 2026-08-13 — Especificación aprobada
- Objetivo: Diseñar funciones con parámetros con valores por omisión para el caso de uso más frecuente, con anticipación.
- Alcance decidido con Diego: valores por omisión (Picuino N°20) + síntesis de todo el bloque Abstracción en los Ejercicios 3-4 de la Independiente (integrando def+parámetros+return+valor por omisión+condicional), ya que es la última clase antes de Strings.
- Actitud elegida entre 4 opciones (Criterio, Simplicidad, Anticipación, Practicidad): Anticipación.
- Iteración de diseño: la Guiada se corrigió a mitad de proceso — el primer borrador quedaba al mismo nivel que los Ejercicios 1-2 (sin condicional); Diego pidió confirmar la regla 20 del CLAUDE.md (Guiada = nivel del Ejercicio 3) y se ajustó para que combine valor por omisión + `return` + condicional de 3 vías.
- Contextos: videojuego del liceo (Haz Ahora/Guiada), Instagram del CEE y sonido del aniversario (Ejercicios 1-2), torneo de e-sports del CEE (Ejercicios 3-4, este último extiende el 3 con un `while`).

## 2026-08-13 — Colab de clase aprobado
- Archivos: Clase 24b - Funciones - Valores por Omisión - Clase.ipynb, Solucionario.ipynb, Ticket de Salida Respuestas.json.
- Generados con la skill generar-colab-clase.
- Iteración: el ICN original tenía 4 conceptos (definición, sintaxis, omitir/indicar, regla de orden) y duplicaba la regla de orden también en Errores típicos. Diego pidió condensar a 3 conceptos como máximo. Se fusionó definición+sintaxis en un solo Concepto 1, se mantuvo omitir/indicar como Concepto 2, regla de orden como Concepto 3, y se eliminó la fila redundante de Errores típicos (quedaron solo las 2 filas que no repetían contenido de un concepto).
- Notebook ejecutado sin errores inesperados (el único error es el `SyntaxError` intencional del Concepto 3, que ilustra la regla de orden).

## 2026-08-13 — Corrección: autochequeo agregado + tabla del Ejercicio 3 reparada
- Diego pidió revisar el Colab de clase contra las consideraciones agregadas hoy mismo a la skill (`disenar-clase`/`generar-colab-clase`): autorevisor y correcta indicación de lo que necesita el programa.
- Hallazgo 1: el spec no tenía `**Celda de configuración:**` ni `**Celda de verificación:**` en ningún ejercicio — la política de autochequeo-siempre se fijó justo hoy, después de que este Colab ya estaba aprobado.
- Hallazgo 2: la tabla "Resultado esperado" del Ejercicio 3 usaba un formato de 3 columnas no canónico (columna izquierda con 📥/📤 como etiqueta de fila en vez de dentro de cada celda `Ejemplo 1`/`Ejemplo 2`) — el parser no la reconoció y el Ejercicio 3 quedó en `Clase.ipynb` sin ningún ejemplo de qué debía ingresar/imprimir el programa (mismo tipo de bug que Clase 22, con una forma de tabla distinta).
- Corrección aplicada en el spec: tabla del Ejercicio 3 reescrita al formato canónico de 2 columnas; agregada `**Celda de configuración:**` + 4 `**Celda de verificación:**` (una por ejercicio).
- Decisión de Diego: para los Ejercicios 3 y 4 (usan `input()`), el autochequeo usa el mecanismo estándar "Verificador por salida" (no "Chequeo de bordes por texto") — primer uso de esta combinación. El estudiante reingresa los valores del Ejemplo 1 del enunciado al verificar.
- Validado contra un kernel IPython real (mismo motor de Jupyter/Colab): confirmado que el prompt de `input()` no se captura por `redirect_stdout`, solo lo que el programa imprime con `print()` — el diseño de `esperadas` (solo líneas de `print()`, sin texto de prompts) es correcto.
- `Clase.ipynb` y `Solucionario.ipynb` regenerados con `crear_colab.py`, ejecutados sin errores inesperados (único error: el `SyntaxError` intencional del Concepto 3) y con outputs limpiados fuera del ICN.

## 2026-08-13 — Ticket de Salida.pptx generado
- Archivo: Clase 24b - Funciones - Valores por Omisión - Ticket de Salida.pptx (8 slides, 3 preguntas, respuestas B/C/D).
- Generado con `crear_ppt_ticket.py` a pedido explícito de Diego, adelantado antes del Colab de ejercicios y del PPT principal.
- **Queda solo local — no se commitea ni pushea hasta después de dictar la clase** (repo público, contiene preguntas y respuestas correctas).
