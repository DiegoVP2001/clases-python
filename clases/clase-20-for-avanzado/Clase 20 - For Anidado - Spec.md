# Clase 20 — For Anidado

**Estado:** Spec aprobada — 2026-07-28 (revisada 2026-07-29)
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
- **Contextos temáticos:** Cinemark del Mall Plaza Oeste (Haz Ahora, ICN y Guiada comparten el mismo escenario), torneo de tenis de mesa (Ejercicio 1), tablero de ajedrez (Ejercicio 2)
- **Tema breve (Form):** for avanzado

## Objetivo

Construir programas con ciclos `for` anidados que generen tablas y patrones organizados en filas y columnas, con orden.

## Propósito

El orden es organizar el trabajo en pasos claros, uno dentro de otro, sin mezclarlos. Hoy lo practicamos anidando ciclos `for`.

## OAs MINEDUC

`OA1, OA3`

- **OA1** — construir un `for` anidado exige descomponer el problema en dos niveles (por cada fila, todas sus columnas) y decidir con criterio cuál ciclo va afuera y cuál adentro.
- **OA3** — se programan algoritmos que generan patrones y tablas completas (asientos de cine, rondas de un torneo, casillero de ajedrez) a partir de una regla repetitiva.

## Estructura de la clase

### 1. Haz Ahora (6 min)
Terminada la última función de la noche en el Cinemark del Mall Plaza Oeste, el equipo de aseo entra a la Sala 4 a revisar que no haya quedado basura ni objetos olvidados. La sala tiene 3 filas de butacas, con 5 asientos cada una, y el equipo revisa fila por fila: primero completa todos los asientos de una fila, y recién ahí pasa a la siguiente. El equipo del cine, sabiendo de sus habilidades de programación, les pide ayuda para automatizar ese recorrido — pero antes de escribir código, quiere que primero tengan clara la lógica:

1. Si ya revisó los 5 asientos de la Fila 1, ¿cuál asiento revisa justo después?
2. ¿Cuántos asientos en total revisa el equipo en toda la sala?
3. ¿Cuántas veces vuelve a partir desde el asiento 1 mientras revisa toda la sala?

**Respuestas esperadas:**
1. El asiento 1 de la Fila 2.
2. 15 (3 filas × 5 asientos).
3. 3 veces, una por cada fila.

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
El sistema del Cinemark quiere automatizar la lista de revisión que usa el equipo de aseo: en vez de anotarla a mano, el programa debe imprimir en pantalla el detalle de cada asiento a revisar en la Sala 4 (3 filas, 5 asientos), agrupado por fila.

**El programa debe:**
- Recorrer las 3 filas de la Sala 4
- Por cada fila, recorrer sus 5 asientos y mostrarlos uno junto al otro en la misma línea
- Saltar a una nueva línea al terminar cada fila, antes de pasar a la siguiente

**Resultado esperado:**
```
Fila 1 - Asiento 1  Fila 1 - Asiento 2  Fila 1 - Asiento 3  Fila 1 - Asiento 4  Fila 1 - Asiento 5
Fila 2 - Asiento 1  Fila 2 - Asiento 2  Fila 2 - Asiento 3  Fila 2 - Asiento 4  Fila 2 - Asiento 5
Fila 3 - Asiento 1  Fila 3 - Asiento 2  Fila 3 - Asiento 3  Fila 3 - Asiento 4  Fila 3 - Asiento 5
```

- Solución:
  ```python
  filas_sala = 3
  asientos_por_fila = 5

  for fila in range(1, filas_sala + 1):
      for asiento in range(1, asientos_por_fila + 1):
          print("Fila", fila, "- Asiento", asiento, end="  ")
      print()
  ```

### 4. Práctica Independiente (16 min)
**Ejercicio 1 — Torneo de tenis de mesa (obligatorio)**
Un campeonato de tenis de mesa entre cursos tiene 5 rondas, y en cada ronda se juegan tantos partidos como el número de la ronda: la ronda 1 tiene 1 partido, la ronda 2 tiene 2 partidos, y así sucesivamente hasta la ronda 5. La organización quiere el programa que imprima cada partido de cada ronda, para pegarlo en el diario mural del gimnasio.

**El programa debe:**
- Recorrer las 5 rondas del campeonato
- Por cada ronda, recorrer sus partidos (tantos como el número de ronda)
- Mostrar el número de ronda y el número de partido de cada uno

**Resultado esperado:**
```
Ronda 1 - Partido 1
Ronda 2 - Partido 1
Ronda 2 - Partido 2
Ronda 3 - Partido 1
...
Ronda 5 - Partido 5
```

- Solución:
  ```python
  cantidad_rondas = 5

  for ronda in range(1, cantidad_rondas + 1):
      for partido in range(1, ronda + 1):
          print("Ronda", ronda, "- Partido", partido)
  ```

**Ejercicio 2 — Diseño de un tablero de ajedrez (obligatorio)**
Un tablero de ajedrez tiene 8 filas y 8 columnas, y sus casillas alternan entre claras y oscuras según su posición: si sumas el número de fila y el número de columna de una casilla, el resultado indica si es clara (par) u oscura (impar). Antes de fabricar tableros nuevos, el taller de carpintería quiere un programa que recorra el patrón completo, casilla por casilla, para verificar que la alternancia quede correcta en las 64 casillas.

**El programa debe:**
- Recorrer las 8 filas del tablero
- Por cada fila, recorrer sus 8 columnas
- Mostrar si cada casilla es clara u oscura, según si la suma de su fila y columna es par o impar
- Saltar de línea al terminar cada fila

<details>
<summary>💡 Pista — el operador módulo</summary>
El operador `%` entrega el resto de una división. Por ejemplo, `7 % 2` da `1` (sobra 1), y `8 % 2` da `0` (no sobra nada). Si el resto de dividir un número por 2 es `0`, el número es par; si es `1`, es impar.
</details>

**Resultado esperado:**
```
Clara Oscura Clara Oscura Clara Oscura Clara Oscura
Oscura Clara Oscura Clara Oscura Clara Oscura Clara
...
```

- Solución:
  ```python
  filas_tablero = 8
  columnas_tablero = 8

  for fila in range(1, filas_tablero + 1):
      for columna in range(1, columnas_tablero + 1):
          if (fila + columna) % 2 == 0:
              print("Clara", end=" ")
          else:
              print("Oscura", end=" ")
      print()
  ```

### 5. Ticket de Salida (6 min)
**Pregunta 1:**
```python
for fila in range(1, 4):
    for asiento in range(1, 6):
        print(fila, asiento)
```
¿Qué pasa con el ciclo `for asiento` cada vez que el ciclo `for fila` avanza una vuelta?
- A: Se ejecuta completo, desde su inicio hasta su fin
- B: Se ejecuta una sola vez en total, sin importar el ciclo externo
- C: Se salta automáticamente
- D: Se ejecuta al revés, de atrás hacia adelante

**Respuesta correcta:** A
**Justificación:** Es la esencia del anidado: por cada vuelta del externo, el interno corre entero antes de que el externo avance.

**Pregunta 2:**
```python
for dia in range(1, 3):
    print("Día", dia)
for bloque in range(1, 3):
    print("Bloque", bloque)
```
¿Qué diferencia hay entre este código y un `for` anidado?
- A: Nada, es exactamente lo mismo
- B: Este código tiene un error de sintaxis
- C: Aquí el segundo `for` no está dentro del primero — ambos ciclos corren uno después del otro, no uno dentro del otro
- D: El segundo `for` reemplaza al primero

**Respuesta correcta:** C
**Justificación:** Python anida por sangría, no por intención: al no estar indentado dentro del primero, el segundo `for` es un bloque aparte que corre después.

**Pregunta 3:**
```python
for fila in range(1, 3):
    for asiento in range(1, 4):
        print(asiento, end=" ")
    print()  # <- esta línea
```
Si se elimina la línea marcada, ¿qué cambia en el resultado?
- A: Nada, el resultado es idéntico
- B: El programa deja de funcionar y lanza un error
- C: Solo se imprimiría la primera fila
- D: Todos los asientos de todas las filas quedarían impresos en una sola línea corrida

**Respuesta correcta:** D
**Justificación:** Sin ese `print()` vacío, nunca se salta de línea entre filas.

### Cierre (5 min)
**Objetivo de la clase:** Construir programas con ciclos `for` anidados que generen tablas y patrones organizados en filas y columnas, con orden.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes construyendo un `for` dentro de otro `for`? (1 = no entendí nada, 5 = puedo explicárselo a otro)

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación de tu vida (fuera de la programación) tendrías que organizar algo en filas y columnas, paso a paso y sin mezclar niveles?

## Decisiones de diseño relevantes

- **Alcance recortado a solo for anidado.** La clase originalmente planificada cubría continue + break + for anidado (Picuino N°15, 16, 17), pero Diego decidió en el diseño enfocarla 100% en for anidado, considerando continue/break "accesorios" frente a la importancia de que quede bien afianzada la lógica de anidamiento. Continue y break quedan como contenido pendiente para una clase futura, sin fecha ni número asignado aún — anotado como recordatorio, sin urgencia ni renumeración de las clases siguientes.
- **Actitud "Orden"** elegida entre varias opciones (Precisión, Paciencia, Método) por su calce natural con la organización de niveles de anidamiento (filas dentro de columnas, sangría de dos niveles).
- **Propósito acortado** a solo definición de la actitud + conexión con el contenido de hoy, sin la frase intermedia de proyección "más allá del liceo" del formato canónico de 3 frases — decisión explícita de Diego para esta clase.
- **Ticket de Salida con alternativas A/B/C/D.** Cambio de convención aplicado desde esta clase en adelante (antes: conteo de dedos en vivo) — actualizado también en `CLAUDE.md` regla 17, ya que el mecanismo de respuesta migró a Google Form y dejó de tener sentido mostrar dedos.
- **Revisión 2026-07-29 (Haz Ahora → Ticket de Salida):** el Haz Ahora original (actividad abierta única, sin preguntas numeradas, con una nota interna "Propósito:" que se filtró al notebook de estudiante por un bug del generador) se reemplazó por una narrativa del Cinemark del Mall Plaza Oeste con 3 preguntas cerradas. La Práctica Guiada dejó el escenario de "talleres extraprogramáticos" y pasó a compartir el mismo escenario Cinemark del Haz Ahora, en el formato canónico de ejercicio (narrativa + "El programa debe" + resultado) en vez de la tabla de pasos de 2 columnas. La Práctica Independiente pasó de "1 obligatorio + 1 bonus" a **2 ejercicios obligatorios**, ambos en el mismo formato canónico; el Ejercicio 2 (ajedrez) agregó una pista `<details>` sobre el operador módulo, ya que antes ese operador solo aparecía en la versión bonus. El Ticket de Salida pasó de 2 a 3 preguntas fijas, cada una con un bloque de código breve (como foco o como referencia), con las respuestas correctas repartidas en letras distintas (A, C, D) para no clusterizarlas.
