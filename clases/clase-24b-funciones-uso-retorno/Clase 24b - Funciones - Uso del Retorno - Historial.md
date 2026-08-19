# Historial — Clase 24b

## 2026-08-19 — Rediseño completo: "valores por omisión" reemplazado por "uso del retorno"
- **Motivo:** tras dictar Clase 24a (2026-08-18), Diego reportó que los estudiantes se trabaron desde el Ejercicio 1 de la Independiente incluso con un ICN simplificado en vivo (patrón DEFINICIÓN/CONSULTA/EVALUACIÓN/IMPRESIÓN) y que quienes avanzaron al Ejercicio 2 tampoco lograron destrabarse solos. Diagnóstico: el problema no era el contenido de 24b (valores por omisión, Picuino N°20) sino que el modelo mental base de funciones de 24a todavía no estaba consolidado.
- **Decisión:** sacar valores por omisión de esta sesión (postergado sin fecha fija) y usar el jueves para reforzar `def`+parámetros+`return`, con foco en dos puntos de quiebre reales: (1) el patrón `variable = funcion(argumento)` — guardar antes de usar — y (2) el caso `None` cuando una función usa `print()` en vez de `return`, o no tiene `return`.
- **Carpeta y archivos renombrados:** `clase-24b-funciones-valores-omision/` → `clase-24b-funciones-uso-retorno/`; Tema pasa de "Valores por Omisión" a "Uso del Retorno" en todos los nombres de archivo.
- **Artefactos del diseño anterior eliminados** (quedan solo como registro en las entradas de historial de abajo, con fecha 2026-08-13): `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json`, `Ticket de Salida.pptx` (estaban en git, se removieron con `git rm`) y `Clase Impresa.tex`/`.pdf` (nunca llegaron a comitearse, se borraron directo). Se regenerarán desde cero con el nuevo Spec.
- **Diseño iterado en chat en varias rondas:**
  - Ángulo elegido entre 4 propuestos (trazado de ejecución, funciones que llaman a otras funciones, usar el retorno en un cálculo posterior, bajar el ritmo): "usar el retorno en un cálculo posterior", extendido por Diego a un patrón general obligatorio en todos los ejercicios.
  - Actitud elegida entre 4 opciones (Método, Verificación, Precisión, Constancia): Método.
  - Haz Ahora iterado 3 veces: v1 era narrativo sin código (descartado porque Diego quería repaso directo de sintaxis ya vista); v2 mostraba directamente la función real de la Feria (`ganancia_venta`) trazada con preguntas — descartado porque dejaba la Guiada como simple copia de lo ya mostrado; v3 (aprobada) usa una función neutra/genérica (`operacion(dato1, dato2)`) envuelta en una mini-narrativa ("un estudiante de otro curso les pide ayuda"), dejando la Feria íntegra para la Guiada. Pregunta 1 ajustada de "¿cuál valor ocupa el lugar de...?" a "¿cómo llamamos al lugar que ocupan...?" para pedir el término (parámetros), no solo el emparejamiento de valores.
  - Guiada ajustada para que programen la función de la Feria desde cero en vivo (no reutilizar una ya dada), reiterando el proceso completo sin copiar del Haz Ahora.
- **Cambio sistémico aplicado en la misma sesión (no exclusivo de esta clase):** pistas desplegables (`<details>`) pasan a ser default siempre en toda Práctica Independiente, 1-2 por ejercicio a criterio de quien diseña — antes eran "solo donde aplica". Actualizado en `CLAUDE.md` (regla 15.3) y en los SKILL.md de `disenar-clase`, `generar-colab-clase`, `generar-colab-ejercicios` y su plantilla.
- `Historial-Curricular.md` actualizado en la misma sesión (Tema, Picuino de referencia, Carpeta, Estado). Valores por omisión queda sin clase asignada — a diseñar más adelante.

## 2026-08-19 — Colab de clase aprobado
- Archivos: `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json` — generados con la skill `generar-colab-clase` a partir del Spec nuevo, sin errores de parseo (3 conceptos ICN, 4 pasos guiada, 4 ejercicios independientes).
- `Ticket de Salida.pptx` generado en el mismo paso (8 slides, 3 preguntas, respuestas B/A/C) — queda solo local hasta dictar la clase.
- `Clase.ipynb` y `Solucionario.ipynb` ejecutados con `nbconvert --execute` sin errores; outputs fuera del ICN limpiados con `limpiar_outputs_haz_ahora.py` (solo los 3 ejemplos de código del ICN conservan output).
- Aprobado por Diego tras dos rondas de ajuste al Concepto 2 (ver entradas siguientes).

## 2026-08-19 — Ajuste: Concepto 2 destaca las 4 etiquetas DEFINICIÓN/CONSULTA/EVALUACIÓN/IMPRESIÓN
- Diego pidió resaltar en el Concepto 2 ("el patrón general — guardar antes de usar") el procedimiento en 4 partes que ya venía usando en vivo con el curso.
- Se agregó como comentarios explícitos en el ejemplo de código (función `ganancia_venta` de la Feria), con valores fijos en la parte CONSULTA (no `input()` real) para mantener la celda ejecutable de una sola pasada dentro del ICN.
- `Clase.ipynb`/`Solucionario.ipynb` regenerados y reejecutados sin errores; outputs fuera del ICN limpiados de nuevo.
- Ajuste fino: Diego pidió que el texto lo presentara como "una regla general", no como "algo que siempre hay que hacer" (framing de hábito). Se reescribió la definición y la idea clave del Concepto 2 con ese lenguaje ("existe una regla general que ordena cualquier programa que use una función..."). Regenerado y reejecutado de nuevo sin errores.

## 2026-08-13 — Especificación aprobada (diseño anterior, reemplazado el 2026-08-19 — ver entrada de arriba)
- Objetivo: Diseñar funciones con parámetros con valores por omisión para el caso de uso más frecuente, con anticipación.
- Alcance decidido con Diego: valores por omisión (Picuino N°20) + síntesis de todo el bloque Abstracción en los Ejercicios 3-4 de la Independiente (integrando def+parámetros+return+valor por omisión+condicional), ya que es la última clase antes de Strings.
- Actitud elegida entre 4 opciones (Criterio, Simplicidad, Anticipación, Practicidad): Anticipación.
- Iteración de diseño: la Guiada se corrigió a mitad de proceso — el primer borrador quedaba al mismo nivel que los Ejercicios 1-2 (sin condicional); Diego pidió confirmar la regla 20 del CLAUDE.md (Guiada = nivel del Ejercicio 3) y se ajustó para que combine valor por omisión + `return` + condicional de 3 vías.
- Contextos: videojuego del liceo (Haz Ahora/Guiada), Instagram del CEE y sonido del aniversario (Ejercicios 1-2), torneo de e-sports del CEE (Ejercicios 3-4, este último extiende el 3 con un `while`).

## 2026-08-13 — Colab de clase aprobado (diseño anterior, archivos eliminados el 2026-08-19)
- Archivos: Clase 24b - Funciones - Valores por Omisión - Clase.ipynb, Solucionario.ipynb, Ticket de Salida Respuestas.json.
- Generados con la skill generar-colab-clase.
- Iteración: el ICN original tenía 4 conceptos (definición, sintaxis, omitir/indicar, regla de orden) y duplicaba la regla de orden también en Errores típicos. Diego pidió condensar a 3 conceptos como máximo. Se fusionó definición+sintaxis en un solo Concepto 1, se mantuvo omitir/indicar como Concepto 2, regla de orden como Concepto 3, y se eliminó la fila redundante de Errores típicos (quedaron solo las 2 filas que no repetían contenido de un concepto).
- Notebook ejecutado sin errores inesperados (el único error es el `SyntaxError` intencional del Concepto 3, que ilustra la regla de orden).

## 2026-08-13 — Corrección: autochequeo agregado + tabla del Ejercicio 3 reparada (diseño anterior, reemplazado el 2026-08-19)
- Diego pidió revisar el Colab de clase contra las consideraciones agregadas hoy mismo a la skill (`disenar-clase`/`generar-colab-clase`): autorevisor y correcta indicación de lo que necesita el programa.
- Hallazgo 1: el spec no tenía `**Celda de configuración:**` ni `**Celda de verificación:**` en ningún ejercicio — la política de autochequeo-siempre se fijó justo hoy, después de que este Colab ya estaba aprobado.
- Hallazgo 2: la tabla "Resultado esperado" del Ejercicio 3 usaba un formato de 3 columnas no canónico (columna izquierda con 📥/📤 como etiqueta de fila en vez de dentro de cada celda `Ejemplo 1`/`Ejemplo 2`) — el parser no la reconoció y el Ejercicio 3 quedó en `Clase.ipynb` sin ningún ejemplo de qué debía ingresar/imprimir el programa (mismo tipo de bug que Clase 22, con una forma de tabla distinta).
- Corrección aplicada en el spec: tabla del Ejercicio 3 reescrita al formato canónico de 2 columnas; agregada `**Celda de configuración:**` + 4 `**Celda de verificación:**` (una por ejercicio).
- Decisión de Diego: para los Ejercicios 3 y 4 (usan `input()`), el autochequeo usa el mecanismo estándar "Verificador por salida" (no "Chequeo de bordes por texto") — primer uso de esta combinación. El estudiante reingresa los valores del Ejemplo 1 del enunciado al verificar.
- Validado contra un kernel IPython real (mismo motor de Jupyter/Colab): confirmado que el prompt de `input()` no se captura por `redirect_stdout`, solo lo que el programa imprime con `print()` — el diseño de `esperadas` (solo líneas de `print()`, sin texto de prompts) es correcto.
- `Clase.ipynb` y `Solucionario.ipynb` regenerados con `crear_colab.py`, ejecutados sin errores inesperados (único error: el `SyntaxError` intencional del Concepto 3) y con outputs limpiados fuera del ICN.

## 2026-08-13 — Ticket de Salida.pptx generado (diseño anterior, archivo eliminado el 2026-08-19)
- Archivo: Clase 24b - Funciones - Valores por Omisión - Ticket de Salida.pptx (8 slides, 3 preguntas, respuestas B/C/D).
- Generado con `crear_ppt_ticket.py` a pedido explícito de Diego, adelantado antes del Colab de ejercicios y del PPT principal.
- **Queda solo local — no se commitea ni pushea hasta después de dictar la clase** (repo público, contiene preguntas y respuestas correctas).
