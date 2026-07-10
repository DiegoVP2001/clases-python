# Clase 14 — elif

**Estado:** Spec aprobada — 2026-06-30
**Clase Picuino:** N°12 — Sentencia elif
**URL Picuino:** https://www.picuino.com/es/python-if-elif.html

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** `input()`, booleanos (`True`/`False`, operadores de comparación), operadores lógicos (`and`, `or`, `not`), análisis de condiciones, `if`/`else`, `if` anidadas
- **Contenidos nuevos:** `elif`, encadenamiento de condiciones alternativas, orden de evaluación, condiciones mutuamente excluyentes
- **Contextos temáticos:** fondo colectivo del viaje de estudio (Haz Ahora + Guiada + Ejercicio 1), batería del celular (Ejercicio 2), minijuego de reflejos (Ticket de Salida)

## Objetivo

Aplicar la sentencia `elif` en Python para construir programas que clasifiquen entre múltiples condiciones mutuamente excluyentes, con orden al definir los caminos posibles antes de escribir código.

## Propósito

El orden es la capacidad de pensar los caminos posibles antes de ponerse a escribir — organizarlos de mayor a menor urgencia, de forma que no se pisen entre sí. Hoy la vas a ejercitar diseñando con `elif` un sistema que le dice a tu curso qué actividad organizar para juntar plata, según cuánto llevan en el fondo común.

## Estructura de la clase

### 1. Haz Ahora (6 min)

**Propósito:** Activar la intuición de múltiples caminos excluyentes en lenguaje natural — la "regla implícita" que los estudiantes ya conocen por experiencia, sin revelar `elif` ni ninguna sintaxis nueva.

**Actividad:** Hace algunos años, cursos que ya hicieron el viaje de estudio aprendieron por experiencia qué actividad funciona mejor según cuánto lleva el fondo. Con ese aprendizaje acumulado, crearon esta tabla:

| Si el fondo lleva… | La actividad recomendada es… |
|---|---|
| Menos de $250.000 | Bingo |
| Entre $250.000 y $499.999 | Rifa |
| Entre $500.000 y $749.999 | Feria en el liceo |
| Entre $750.000 y $999.999 | Vender colaciones en recreos |
| $1.000.000 o más | ¡Meta cumplida! |

Responde en tu cuaderno:

1. El fondo lleva $380.000 — ¿qué actividad harían?
2. El fondo lleva $720.000 — ¿cambia la actividad?
3. El fondo lleva $50.000 — ¿qué harían ahora?
4. El fondo lleva $1.020.000 — ¿qué dice el sistema?
5. En tus propias palabras, escribe la regla de decisión que seguirías para elegir la actividad correcta según el monto del fondo.

**Respuestas esperadas:**
1. Rifa
2. Vender colaciones en recreos
3. Bingo
4. ¡Meta cumplida!
5. Respuesta libre. Ejemplo: "Si el fondo tiene menos de $250.000, organizo un bingo. Si tiene entre $250.000 y $499.999, una rifa. Si tiene entre $500.000 y $749.999, una feria. Si tiene entre $750.000 y $999.999, vendo colaciones. Si ya llegué a $1.000.000, no necesito nada más."

### 2. Introducción al Contenido Nuevo (18 min)

Ejemplos con temperatura del día (neutros — el viaje llega recién en la Guiada).

**Concepto 1: Sintaxis de `elif`**
- Definición: `elif` es una condición alternativa que se evalúa solo si las condiciones anteriores resultaron `False`. Se puede encadenar tantos `elif` como sean necesarios, y al final se agrega un `else` para cubrir todos los casos restantes.
- Ejemplo:
  ```python
  temperatura = 25

  if temperatura < 10:
      print("Frío — lleva abrigo.")
  elif temperatura < 20:
      print("Fresco — una chaqueta basta.")
  elif temperatura < 30:
      print("Cálido — manga corta.")
  else:
      print("Caliente — usa protector solar.")
  ```
  ```
  >> Cálido — manga corta.
  ```
- Idea clave: `elif` reemplaza la pirámide de `if` anidados cuando las condiciones son excluyentes — cada rama cubre un rango distinto.

**Concepto 2: Solo una rama se ejecuta**
- Definición: Python evalúa las condiciones en orden, de arriba hacia abajo. En cuanto encuentra la primera que resulta `True`, ejecuta ese bloque y salta todo lo que viene después — aunque otras condiciones también sean `True`.
- Ejemplo:
  ```python
  temperatura = 25

  if temperatura < 10:
      print("Frío.")       # False — se salta
  elif temperatura < 20:
      print("Fresco.")     # False — se salta
  elif temperatura < 30:
      print("Cálido.")     # True — EJECUTA ESTO y para
  else:
      print("Caliente.")   # no llega acá
  ```
  ```
  >> Cálido.
  ```
- Idea clave: Aunque `temperatura = 25` también cumple `temperatura < 30`, Python ya entró al primer `elif` verdadero y no sigue evaluando.

**Concepto 3: El orden de las condiciones importa**
- Definición: Si una condición más amplia aparece antes que una más específica, la específica nunca se alcanza. Las condiciones deben ir ordenadas de forma que cada rango quede bien delimitado.
- Ejemplo:
  ```python
  # ⚠️ Orden incorrecto
  temperatura = 5

  if temperatura < 30:    # demasiado amplia — captura casi todo
      print("Cálido.")
  elif temperatura < 10:  # nunca llega acá
      print("Frío.")
  ```
  ```
  >> Cálido.
  ```
  ```python
  # ✅ Orden correcto
  temperatura = 5

  if temperatura < 10:
      print("Frío.")
  elif temperatura < 30:
      print("Cálido.")
  ```
  ```
  >> Frío.
  ```
- Idea clave: Ordena siempre de lo más específico a lo más general — o de menor a mayor (o mayor a menor), de forma consistente.

**Errores típicos:**

| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Primera condición demasiado amplia | Todos los valores entran al primer `if` y nunca llegan al `elif` | Ordenar las condiciones de menor a mayor (o mayor a menor) de forma consistente |
| `elif` después de `else` | `SyntaxError` — Python no acepta `elif` después del `else` | El `else` siempre va al final, después de todos los `elif` |
| Olvidar el `else` final | Si ninguna condición se cumple, el programa no imprime nada | Agregar un `else` que cubra todos los casos restantes |

### 3. Práctica Guiada (22 min)

**Situación:** El fondo del viaje de estudio de tu curso lleva $380.000 de una meta de $1.000.000. Según la tabla que ya conocen, el programa debe recomendar automáticamente la actividad correcta.

<table>
<tr>
  <th>Fondo actual</th>
  <th>Actividad recomendada</th>
</tr>
<tr><td>Menos de $250.000</td><td>Bingo</td></tr>
<tr><td>$250.000 – $499.999</td><td>Rifa</td></tr>
<tr><td>$500.000 – $749.999</td><td>Feria en el liceo</td></tr>
<tr><td>$750.000 – $999.999</td><td>Vender colaciones en recreos</td></tr>
<tr><td>$1.000.000 o más</td><td>¡Meta cumplida! 🎉</td></tr>
</table>

**Variables:**
```python
fondos_reunidos = 380000
meta = 1000000
```

**Pasos guiados:**
1. Crea una variable con el total que lleva el fondo del curso
2. Crea otra variable con la meta total del viaje
3. Antes de escribir el `elif`, escribe en palabras los 5 caminos posibles según los rangos de la tabla
4. Verifica si los fondos ya alcanzan o superan la meta — si es así, imprime el mensaje de celebración
5. Si no llegaron a la meta, verifica si están en el rango más alto (entre $750.000 y $999.999) e imprime la recomendación correspondiente
6. Agrega las condiciones para los rangos intermedios en orden descendente
7. Cierra con el caso del fondo más bajo (menos de $250.000)

**Resultado esperado:**
```
El fondo lleva 380000 pesos de 1000000 .
Recomendación: Organicen una rifa. ¡Van bien!
```

- Solución:
  ```python
  fondos_reunidos = 380000
  meta = 1000000

  if fondos_reunidos >= meta:
      print("El fondo lleva", fondos_reunidos, "pesos de", meta, ".")
      print("Recomendación: ¡Meta cumplida! El viaje está confirmado. 🎉")
  elif fondos_reunidos >= 750000:
      print("El fondo lleva", fondos_reunidos, "pesos de", meta, ".")
      print("Recomendación: Vendan colaciones en los recreos. ¡Ya casi!")
  elif fondos_reunidos >= 500000:
      print("El fondo lleva", fondos_reunidos, "pesos de", meta, ".")
      print("Recomendación: Organicen una feria en el liceo. ¡Están bien!")
  elif fondos_reunidos >= 250000:
      print("El fondo lleva", fondos_reunidos, "pesos de", meta, ".")
      print("Recomendación: Organicen una rifa. ¡Van bien!")
  else:
      print("El fondo lleva", fondos_reunidos, "pesos de", meta, ".")
      print("Recomendación: Organicen un bingo. ¡A juntar plata!")
  ```

### 4. Práctica Independiente (26 min)

**Ejercicio 1 — Estado de cuotas del viaje**

El encargado del viaje registra cuántas cuotas ha pagado cada estudiante y necesita saber en qué estado está cada uno. El liceo definió cuatro categorías según las cuotas pagadas: quienes no han pagado ninguna están en estado crítico; quienes llevan una o dos están atrasados; quienes llevan tres o cuatro están al día; y quienes llevan cinco o más van adelantados.

**El programa debe:**
- Registrar el **número de cuotas pagadas** como variable al inicio
- Clasificar el estado del estudiante usando **cuatro categorías** según el rango de cuotas
- Imprimir un **mensaje claro** con el estado y una indicación de qué hacer

<details><summary>💡 Pista 1 — Sin input()</summary>
Para este ejercicio define el valor directamente como variable al inicio: `cuotas_pagadas = 3`. Prueba cambiándolo a 0, 1, 5, etc. para verificar los distintos casos.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>cuotas_pagadas = 0</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>cuotas_pagadas = 5</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Estado: Crítico. Habla con tu apoderado lo antes posible.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Estado: Adelantado. ¡Gracias por tu compromiso!</pre></td>
</tr>
</table>

- Solución:
  ```python
  cuotas_pagadas = 0

  if cuotas_pagadas == 0:
      print("Estado: Crítico. Habla con tu apoderado lo antes posible.")
  elif cuotas_pagadas <= 2:
      print("Estado: Atrasado. Quedan cuotas por ponerse al día.")
  elif cuotas_pagadas <= 4:
      print("Estado: Al día. ¡Sigue así!")
  else:
      print("Estado: Adelantado. ¡Gracias por tu compromiso!")
  ```

**Ejercicio 2 — Batería del celular**

Tu celular muestra el porcentaje de batería restante y quieres que un programa te avise en qué estado está. Los técnicos de soporte usan cuatro niveles: si queda un 10% o menos, la batería es crítica; entre 11% y 30%, está baja; entre 31% y 70%, está normal; y sobre el 70%, está cargada.

**El programa debe:**
- Registrar el **porcentaje de batería** como variable al inicio
- Clasificar el nivel usando **cuatro categorías**
- Imprimir un **mensaje con el estado y una recomendación**

<details><summary>💡 Pista 1 — Orden de las condiciones</summary>
Decide si vas de menor a mayor o de mayor a menor — pero mantén un orden consistente en todos los `elif` para que los rangos no se traslapen.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>porcentaje_bateria = 8</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>porcentaje_bateria = 45</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Batería crítica — conéctala ya.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Batería normal — vas bien.</pre></td>
</tr>
</table>

- Solución:
  ```python
  porcentaje_bateria = 8

  if porcentaje_bateria <= 10:
      print("Batería crítica — conéctala ya.")
  elif porcentaje_bateria <= 30:
      print("Batería baja — busca un cargador pronto.")
  elif porcentaje_bateria <= 70:
      print("Batería normal — vas bien.")
  else:
      print("Batería cargada — sin preocupaciones.")
  ```

### 5. Ticket de Salida (8 min)

En un minijuego de reflejos, el sistema mide cuántos milisegundos tardaste en reaccionar. Escribe un programa que clasifique el nivel del jugador según estos rangos:

* más de 500 ms → Novato
* entre 300 y 500 ms → Intermedio
* entre 150 y 299 ms → Experto
* menos de 150 ms → Pro

**El programa debe:**
- Registrar el tiempo de reacción como variable al inicio (sin `input()`)
- Clasificar el nivel usando `elif`
- Imprimir un mensaje con la categoría obtenida

**Entrega:** `+ Text` en Colab con el código escrito.

- Solución:
  ```python
  tiempo_ms = 220

  if tiempo_ms > 500:
      print("Nivel: Novato — sigue practicando.")
  elif tiempo_ms >= 300:
      print("Nivel: Intermedio — buen tiempo.")
  elif tiempo_ms >= 150:
      print("Nivel: Experto — reflejos rápidos.")
  else:
      print("Nivel: Pro — velocidad de élite.")
  ```

### Cierre (5 min)

**Objetivo de la clase**
Aplicar la sentencia `elif` en Python para construir programas que clasifiquen entre múltiples condiciones mutuamente excluyentes, con orden al definir los caminos posibles antes de escribir código.

**Pregunta 1 — Metacognición (escala 1-5)**
"¿Qué tan seguro/a te sientes usando `elif` para clasificar entre múltiples opciones? (1 = no entendí nada, 5 = puedo explicárselo a otro)"

**Pregunta 2 — Actitud proyectada al futuro**
"¿Antes de escribir el código de la Guiada, cuánto te ayudó pensar primero los caminos en palabras? ¿En qué otra situación de tu vida podrías aplicar ese orden antes de actuar?"

## Decisiones de diseño relevantes

- **Haz Ahora con tabla explícita:** la regla de rangos se muestra antes de programar para que los estudiantes la usen como referencia. La pregunta 5 ("escribe la regla en tus palabras") conecta directamente con la actitud "orden" del objetivo — externalizar la lógica antes de codificarla.
- **ICN con temperatura (neutro):** los ejemplos del ICN no usan el viaje deliberadamente. Así, cuando aparece el fondo del viaje en la Guiada, los estudiantes reconocen que están aplicando `elif` a algo que ya conocen — el momento de revelación tiene más peso.
- **Solo 3 conceptos en ICN (sintaxis, una sola rama, orden):** se omite el contraste explícito con `if` anidados para no alargar el ICN. El error típico "primera condición demasiado amplia" cubre esa intuición de forma más eficiente.
- **Ejercicio 1 del viaje, Ejercicio 2 distinto:** mantiene el hilo conductor sin agotar el mismo contexto. La batería del celular tiene rangos igualmente naturales y cercanos a los estudiantes.
- **Sin Colab de ejercicios:** decisión de Diego para esta clase.
- **Secuencia C13 → C14:** los `if` anidados (C13) mostraron el problema; `elif` (C14) es la solución. El error típico "anidar cuando basta con `and`" de C13 ya preparó el terreno.
