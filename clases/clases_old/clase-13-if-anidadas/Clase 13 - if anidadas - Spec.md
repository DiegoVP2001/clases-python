# Clase 13 — if anidadas

**Estado:** Spec aprobada — 2026-06-29
**Clase Picuino:** N°11 — Sentencias if anidadas
**URL Picuino:** https://www.picuino.com/es/python-if-anidados.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** `input()`, booleanos (True/False, operadores de comparación), operadores lógicos (`and`, `or`, `not`), análisis de condiciones, `if`/`else`
- **Contenidos nuevos:** `if` dentro de `if`, `if` dentro de `else`, indentación de dos niveles, variables y operaciones dentro de bloques `if`, cuándo anidar vs. cuándo usar `and`
- **Contextos temáticos:** ciber café (práctica guiada), plataforma de streaming (ejercicio 1), torneo deportivo de básquetbol (ejercicio 2), museo (ticket de salida)

## Objetivo

Aplicar sentencias `if` anidadas en Python para construir programas que tomen decisiones en secuencia — evaluando una condición solo si la anterior se cumplió — con perseverancia ante los errores de indentación.

## Propósito

La perseverancia es la capacidad de seguir intentando cuando algo no funciona a la primera — leer el error con calma, ajustar y volver a probar. Esa habilidad te sirve en cualquier proyecto que te importe: aprender algo nuevo, sacar adelante un trabajo en equipo, construir algo tuyo. Hoy la vas a ejercitar escribiendo `if` anidados, donde un solo espacio mal puesto rompe todo.

## Estructura de la clase

### 1. Haz Ahora (6 min)

**Propósito:** Activar la lógica de decisiones secuenciales — la intuición de que a veces una pregunta solo tiene sentido si la anterior ya se cumplió — sin mostrar código Python.

**Actividad (papel o chat del Colab):** "Una sala de videojuegos tiene esta regla: *solo abre los fines de semana*, y *solo puedes entrar si eres socio*. Sin escribir código, describe en orden los pasos que seguirías para decidir si alguien puede entrar. ¿Cuántas preguntas necesitas hacer, y en qué orden importa?"

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: if anidado básico**
- Definición: Un `if` anidado es un `if` que vive dentro del bloque de otro `if`. La condición interior solo se evalúa si la exterior ya resultó `True`.
- Ejemplo:
  ```python
  sala_abierta = True
  es_socio = True

  if sala_abierta:
      if es_socio:
          print("Puedes entrar a jugar.")
  ```
  ```
  >> Puedes entrar a jugar.
  ```
- Idea clave: La segunda condición no existe para el programa si la primera falla.

**Concepto 2: else en cada nivel**
- Definición: Cada nivel de anidamiento puede tener su propio `else`, lo que permite cubrir todos los caminos posibles de la decisión.
- Ejemplo:
  ```python
  sala_abierta = True
  es_socio = False

  if sala_abierta:
      if es_socio:
          print("Puedes entrar a jugar.")
      else:
          print("La sala está abierta, pero necesitas ser socio.")
  else:
      print("La sala está cerrada en este momento.")
  ```
  ```
  >> La sala está abierta, pero necesitas ser socio.
  ```
- Idea clave: Un `if` anidado con `else` en cada nivel tiene tres o más caminos posibles — nunca uno solo.

**Concepto 3: La sangría como jerarquía**
- Definición: Cada nivel de anidamiento agrega 4 espacios de sangría. El código que está "más adentro" pertenece al bloque que lo contiene.
- Ejemplo:
  ```python
  condicion_exterior = True
  condicion_interior = True

  if condicion_exterior:       # nivel 1 — 0 espacios extra
      if condicion_interior:   # nivel 2 — 4 espacios
          print("Ambas OK")    # nivel 3 — 8 espacios
      else:
          print("Solo la exterior")
  else:
      print("Ninguna se cumplió")
  ```
- Idea clave: Un solo espacio mal puesto cambia a qué bloque pertenece una línea — Python es estricto con esto.

**Concepto 4: El cuerpo de un if es código normal**
- Definición: Dentro de un `if` no solo cabe otro `if`. Puedes crear variables, hacer cálculos, concatenar texto — cualquier código Python válido.
- Ejemplo:
  ```python
  puntaje = 850

  if puntaje >= 500:
      categoria = "Nivel avanzado"
      bonus = puntaje * 2
      print("Categoría:", categoria)
      print("Bonus acumulado:", bonus)
  ```
  ```
  >> Categoría: Nivel avanzado
  >> Bonus acumulado: 1700
  ```
- Idea clave: El `if` define *cuándo* se ejecuta el código, no *qué tipo* de código puede ser.

**Errores típicos:**

| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Segundo `if` al mismo nivel que el primero | Se evalúan como independientes, no anidados | Verificar que el `if` interior tenga 4 espacios más que el exterior |
| Olvidar el `else` del `if` exterior | Si la primera condición falla, el programa no dice nada | Agregar `else` para cubrir ese camino |
| Anidar cuando basta con `and` | Código más largo sin necesidad | Preguntar: "¿La segunda condición depende de la primera, o se pueden verificar juntas?" |

### 3. Práctica Guiada (22 min)

**Situación:** Un ciber café necesita verificar dos cosas antes de asignar un computador: primero si hay puestos disponibles, y luego si el cliente tiene saldo suficiente para al menos una hora.

*(Dato del día: los cibers fueron durante años la única forma que tenía la mayoría de los jóvenes en Chile de jugar online o navegar — llegaron a ser miles a principios de los 2000. Era como ir al arcade pero con Counter-Strike.)*

**Variables:**
```python
hay_computadores = True
saldo_cliente = 1500
precio_hora = 1200
```

**Pasos guiados:**
1. Crea una variable que indique si hay puestos disponibles en el ciber
2. Crea una variable con el saldo actual del cliente y otra con el precio mínimo por una hora
3. Verifica si hay disponibilidad; si no hay, muestra un mensaje específico
4. Dentro del caso en que sí hay disponibilidad, verifica si el saldo alcanza para al menos una hora
5. Imprime un mensaje distinto para cada uno de los casos posibles

**Resultado esperado:**
```
Hay un computador disponible.
Tu saldo alcanza. ¡Bienvenido al ciber!
```

- Solución:
  ```python
  hay_computadores = True
  saldo_cliente = 1500
  precio_hora = 1200

  if hay_computadores:
      if saldo_cliente >= precio_hora:
          print("Hay un computador disponible.")
          print("Tu saldo alcanza. ¡Bienvenido al ciber!")
      else:
          print("Hay un computador disponible.")
          print("Tu saldo no alcanza para una hora.")
  else:
      print("No hay computadores disponibles en este momento.")
  ```

### 4. Práctica Independiente (26 min)

**Ejercicio 1 — Plataforma de streaming**

Lanzaste una plataforma de streaming para estudiantes de tu colegio. Para proteger las cuentas, el acceso se verifica en dos pasos: primero el sistema comprueba si el nombre de usuario ingresado existe en la plataforma, y solo si es correcto, verifica si la contraseña también coincide. Así, si alguien no conoce el usuario, nunca llega siquiera a intentar la contraseña.

**El programa debe:**
- Pedir el **nombre de usuario** y la **contraseña** al inicio
- Verificar primero si el **usuario existe** en la plataforma
- Solo si el usuario es correcto, verificar si la **contraseña coincide**
- Mostrar un **mensaje específico** para cada caso posible

<details><summary>💡 Pista 1 — ¿Cuántos caminos hay?</summary>
Antes de escribir código, cuenta cuántos resultados distintos puede tener este programa. Dibújalos o escríbelos en palabras — eso te dice cuántos `if`, `else` y mensajes necesitas.
</details>

<details><summary>💡 Pista 2 — El else exterior</summary>
El `else` del `if` exterior cubre el caso en que el usuario no existe. No necesitas llegar al `if` interior para manejar ese camino.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>usuario: profe_diego
contraseña: wrong123</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>usuario: fantasma99
contraseña: python2024</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Contraseña incorrecta.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Usuario no encontrado.</pre></td>
</tr>
</table>

- Solución:
  ```python
  usuario_correcto = "profe_diego"
  contrasena_correcta = "python2024"

  usuario = input("Usuario: ")
  contrasena = input("Contraseña: ")

  if usuario == usuario_correcto:
      if contrasena == contrasena_correcta:
          print("Acceso concedido. ¡Bienvenido/a!")
      else:
          print("Contraseña incorrecta.")
  else:
      print("Usuario no encontrado.")
  ```

---

**Ejercicio 2 — Torneo de básquetbol**

El club deportivo de tu ciudad organiza un torneo regional de básquetbol. Para mantener el nivel de competencia, el sistema verifica dos requisitos en orden: primero, si el jugador está formalmente inscrito en el club esta temporada, y si lo está, si su puntaje acumulado en los partidos de práctica supera el mínimo requerido de 50 puntos.

**El programa debe:**
- Registrar si el jugador **está inscrito** y su **puntaje acumulado**
- Verificar primero la **inscripción al club**
- Solo si está inscrito, verificar si el **puntaje supera el mínimo**
- Mostrar un **mensaje claro** para cada resultado posible

<details><summary>💡 Pista 1 — Valores de prueba</summary>
Para este ejercicio no necesitas `input()`. Define los valores directamente como variables al inicio del programa y prueba cambiándolos a mano para verificar los distintos casos.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>inscrito: True
puntaje: 65</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>inscrito: True
puntaje: 30</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Clasificado al torneo. ¡Buena suerte!</pre></td>
  <td>📤 <em>El programa imprime</em><pre>No alcanzas el puntaje mínimo. Sigue practicando.</pre></td>
</tr>
</table>

- Solución:
  ```python
  inscrito = True
  puntaje = 65
  minimo = 50

  if inscrito:
      if puntaje >= minimo:
          print("Clasificado al torneo. ¡Buena suerte!")
      else:
          print("No alcanzas el puntaje mínimo. Sigue practicando.")
  else:
      print("No estás inscrito en el club esta temporada.")
  ```

### 5. Ticket de Salida (8 min)

**Tarea:** Un museo está abierto de martes a domingo. Los visitantes menores de 12 años entran gratis; el resto paga entrada. Escribe el programa que, dado el día de la semana y la edad del visitante, imprima el mensaje que corresponde: si el museo está cerrado, si entra gratis o si debe pagar.

**Entrega:** `+ Text` en Colab con el código escrito.

- Solución:
  ```python
  dia = input("Día de la semana: ")
  edad = int(input("Edad del visitante: "))

  if dia != "lunes":
      if edad < 12:
          print("El museo está abierto. Entrada: gratis.")
      else:
          print("El museo está abierto. Debe pagar entrada.")
  else:
      print("El museo está cerrado los lunes.")
  ```

### Cierre (5 min)

**Objetivo de la clase**
Aplicar sentencias `if` anidadas en Python para construir programas que tomen decisiones en secuencia — evaluando una condición solo si la anterior se cumplió — con perseverancia ante los errores de indentación.

**Pregunta 1 — Metacognición (escala 1-5)**
"¿Qué tan seguro/a te sientes leyendo y escribiendo `if` anidados? (1 = no entendí nada, 5 = puedo explicárselo a otro)"

**Pregunta 2 — Actitud proyectada**
"¿Hubo algún momento hoy en que algo no te resultó a la primera? ¿Cómo lo resolviste?"

## Decisiones de diseño relevantes

- **Contexto guiada — ciber café:** permite un throwback cultural auténtico (los cibers de los 2000) que conecta con la historia de la tecnología en Chile y da pie a un dato del día breve. El escenario (disponibilidad de puesto + saldo) es una aplicación directa y natural de if anidados.
- **Concepto 4 (cuerpo del if es código normal):** agregado a petición de Diego para recordar que dentro de los bloques se pueden hacer operaciones y crear variables, no solo anidar más ifs.
- **Ticket — museo:** escenario diferente a los ejercicios, con condición booleana implícita (día ≠ lunes) que los estudiantes deben identificar por sí mismos. Evalúa comprensión genuina sin apoyarse en el contexto de los ejercicios anteriores.
- **Secuencia C13 → C14:** los if anidados van antes que `elif` deliberadamente. C13 muestra el problema (pirámide de sangrías, múltiples else anidados); C14 llega con `elif` como la solución. El error típico "anidar cuando basta con `and`" ya insinúa que hay mejores formas, sin adelantar la sintaxis.
