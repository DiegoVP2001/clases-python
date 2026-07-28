# Clase 20 — For Anidado

**Estado:** Spec aprobada — 2026-07-28
**Clase Picuino:** N° 17 — Sentencias for anidadas
**URL Picuino:** https://www.picuino.com/es/python-for-anidados.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Condicionales completos (if/else, if anidadas, elif) y ciclos `for` con `range()` (Clase N°16)
- **Contenidos nuevos:** Ciclos `for` anidados (ciclo dentro de otro ciclo), relación filas/columnas entre ciclo externo e interno, sangría de dos niveles, construcción de salida por fila usando `print(..., end=...)` y `print()` vacío para el salto de línea
- **Contextos temáticos:** Sala de cine (Haz Ahora + ICN), talleres extraprogramáticos del colegio (Guiada), torneo de tenis de mesa (Ejercicio 1), tablero de ajedrez (Ejercicio 2 — bonus)

## Objetivo

Construir programas con ciclos `for` anidados que generen tablas y patrones organizados en filas y columnas, con orden.

## Propósito

El orden es organizar el trabajo en pasos claros, uno dentro de otro, sin mezclarlos. Hoy lo practicamos anidando ciclos `for`.

## Estructura de la clase

### 1. Haz Ahora (6 min)
Propósito: activar la intuición de "repetir un patrón, y dentro de cada repetición, repetir otro patrón más chico" — sin código, en papel — antes de nombrarlo como concepto. Es spoiler sutil de la lógica de anidar, en lenguaje cotidiano, sin revelar sintaxis.

Actividad: Una sala de cine tiene 4 filas de butacas, y cada fila tiene 5 asientos. En una celda markdown, respondiendo en un par de palabras, se les pide que describan cómo numerarían todos los asientos de la sala, butaca por butaca, sin saltarse ninguno — describiendo el "para cada fila... y dentro de cada fila...".

### 2. Introducción al Contenido Nuevo (18 min)

Contexto de ejemplos: sala de cine (butacas en filas y columnas) — mismo contexto del Haz Ahora, para que el "aha" sea inmediato.

**Concepto 1: Ciclo `for` anidado**
- Definición: Un ciclo `for` dentro de otro ciclo `for`. El ciclo de adentro se ejecuta completo por cada vuelta del ciclo de afuera.
- Ejemplo:
  ```python
  for fila in range(1, 3):
      for asiento in range(1, 4):
          print("Fila", fila, "- Asiento", asiento)
  ```
- Idea clave: por cada vuelta del ciclo externo, el ciclo interno corre entero antes de que el externo avance.

**Concepto 2: Filas y columnas**
- Definición: en un `for` anidado, la variable del ciclo externo suele representar las filas, y la variable del ciclo interno representa las columnas dentro de cada fila.
- Ejemplo:
  ```python
  for fila in range(1, 3):
      for columna in range(1, 4):
          print("(", fila, ",", columna, ")")
  ```
- Idea clave: pensar "primero fijo la fila, después recorro todas sus columnas" ayuda a decidir cuál `for` va afuera y cuál va adentro.

**Concepto 3: Sangría de dos niveles**
- Definición: cada nivel de anidamiento exige su propia sangría. El cuerpo del `for` interno va indentado dentro del cuerpo del `for` externo.
- Ejemplo:
  ```python
  for fila in range(1, 3):
      print("Fila", fila)
      for asiento in range(1, 4):
          print("  Asiento", asiento)
  ```
- Idea clave: perder la sangría del ciclo interno rompe la relación de anidamiento — Python deja de entender que uno está "dentro" del otro.

**Concepto 4: Construir la salida por fila**
- Definición: usar `print(..., end=...)` dentro del ciclo interno mantiene los valores en la misma línea; un `print()` vacío después del ciclo interno (pero dentro del externo) salta a la siguiente línea al terminar cada fila.
- Ejemplo:
  ```python
  for fila in range(1, 3):
      for asiento in range(1, 4):
          print(asiento, end=" ")
      print()
  ```
- Idea clave: sin el `print()` vacío al cierre de cada fila, toda la sala quedaría impresa en una sola línea corrida.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| El ciclo interno no queda indentado dentro del externo | Ambos ciclos corren "en paralelo", no anidados — el resultado no forma una tabla | Verificar que el `for` interno esté un nivel de sangría más adentro que el externo |
| Usar el mismo nombre de variable en ambos ciclos | La variable externa se sobrescribe y el conteo de filas se pierde | Usar nombres distintos para el índice de fila y el de columna |
| Olvidar el salto de línea entre filas | Todos los asientos quedan impresos en una sola línea corrida | Agregar un `print()` vacío al terminar cada vuelta del ciclo externo |

### 3. Práctica Guiada (22 min)
**Situación:** El colegio va a abrir inscripciones para talleres extraprogramáticos y necesita imprimir la grilla de horarios: hay 4 días de la semana con talleres, y cada día tiene 3 bloques horarios disponibles.

**Variables:**
```python
dias_con_talleres = 4
bloques_por_dia = 3
```

**Pasos guiados (tabla):**

- Paso 1: Crea una variable que registre cuántos días de la semana tienen talleres, y otra que registre cuántos bloques horarios hay por día.
  Resultado:
  ```
  (todavía no hay output — son solo las cantidades iniciales)
  ```

- Paso 2: Construye un ciclo que recorra cada día de la semana.
  Resultado:
  ```
  (todavía no hay output — el ciclo externo aún no imprime nada por sí solo)
  ```

- Paso 3: Dentro de ese ciclo, construye otro ciclo que recorra cada bloque horario de ese día, mostrando en pantalla el número de día y el número de bloque, uno junto al otro en la misma línea.
  Resultado:
  ```
  Día 1 - Bloque 1  Día 1 - Bloque 2  Día 1 - Bloque 3
  ```

- Paso 4: Al terminar de recorrer todos los bloques de un día, salta a una nueva línea antes de pasar al día siguiente.
  Resultado:
  ```
  Día 1 - Bloque 1  Día 1 - Bloque 2  Día 1 - Bloque 3
  Día 2 - Bloque 1  Día 2 - Bloque 2  Día 2 - Bloque 3
  Día 3 - Bloque 1  Día 3 - Bloque 2  Día 3 - Bloque 3
  Día 4 - Bloque 1  Día 4 - Bloque 2  Día 4 - Bloque 3
  ```

### 4. Práctica Independiente (16 min)
**Ejercicio 1 — Torneo de tenis de mesa (obligatorio)**
Un campeonato de tenis de mesa entre cursos tiene 5 rondas, y en cada ronda se juegan tantos partidos como el número de la ronda (ronda 1 tiene 1 partido, ronda 2 tiene 2 partidos, y así). El programa debe mostrar cada partido de cada ronda, identificando el número de ronda y el número de partido dentro de esa ronda.
Resultado esperado: una tabla creciente, donde la ronda 1 muestra 1 línea, la ronda 2 muestra 2 líneas, hasta la ronda 5 con 5 líneas.

**Ejercicio 2 — Diseño de un tablero de ajedrez (Bonus — décimas extra)**
Un tablero de ajedrez tiene 8 filas y 8 columnas, alternando casillas claras y oscuras. El programa debe recorrer todas las casillas del tablero, fila por fila, mostrando en pantalla si cada casilla es clara u oscura según su posición.
Resultado esperado: 8 líneas, cada una mostrando el patrón alternado de 8 casillas de esa fila.

### 5. Ticket de Salida (6 min)
**Pregunta 1:** ¿Qué pasa con el ciclo interno cada vez que el ciclo externo avanza una vuelta?
- A: Se ejecuta una sola vez en total, sin importar el ciclo externo
- B: Se ejecuta completo, desde su inicio hasta su fin
- C: Se salta automáticamente
- D: Se ejecuta al revés, de atrás hacia adelante

**Respuesta correcta:** B
**Justificación:** Es la esencia del anidado: por cada vuelta del externo, el interno corre entero antes de que el externo avance a la siguiente vuelta.

**Pregunta 2:** Si el ciclo interno de un `for` anidado pierde su sangría y queda al mismo nivel que el externo, ¿qué ocurre?
- A: Da error y el programa no corre
- B: Ambos ciclos se ejecutan uno después del otro, ya no anidados
- C: El ciclo externo desaparece
- D: El programa igual construye la tabla correctamente

**Respuesta correcta:** B
**Justificación:** Python no anida por intención, sino por sangría — sin ella, ambos `for` quedan al mismo nivel y se ejecutan en secuencia, no uno dentro del otro.

### Cierre (5 min)
**Objetivo de la clase:** Construir programas con ciclos `for` anidados que generen tablas y patrones organizados en filas y columnas, con orden.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes construyendo un `for` dentro de otro `for`? (1 = no entendí nada, 5 = puedo explicárselo a otro)

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación de tu vida (fuera de la programación) tendrías que organizar algo en filas y columnas, paso a paso y sin mezclar niveles?

## Decisiones de diseño relevantes

- **Alcance recortado a solo for anidado.** La clase originalmente planificada cubría continue + break + for anidado (Picuino N°15, 16, 17), pero Diego decidió en el diseño enfocarla 100% en for anidado, considerando continue/break "accesorios" frente a la importancia de que quede bien afianzada la lógica de anidamiento. Continue y break quedan como contenido pendiente para una clase futura, sin fecha ni número asignado aún — anotado como recordatorio, sin urgencia ni renumeración de las clases siguientes.
- **Actitud "Orden"** elegida entre varias opciones (Precisión, Paciencia, Método) por su calce natural con la organización de niveles de anidamiento (filas dentro de columnas, sangría de dos niveles).
- **Propósito acortado** a solo definición de la actitud + conexión con el contenido de hoy, sin la frase intermedia de proyección "más allá del liceo" del formato canónico de 3 frases — decisión explícita de Diego para esta clase.
- **Ticket de Salida con alternativas A/B/C/D.** Cambio de convención aplicado desde esta clase en adelante (antes: conteo de dedos en vivo) — actualizado también en `CLAUDE.md` regla 17, ya que el mecanismo de respuesta migró a Google Form y dejó de tener sentido mostrar dedos.
