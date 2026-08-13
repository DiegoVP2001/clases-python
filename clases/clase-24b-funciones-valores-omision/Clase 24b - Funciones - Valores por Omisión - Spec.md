# Clase 24b — Funciones (valores por omisión)

**Estado:** Spec aprobada — 2026-08-13
**Clase Picuino:** N° 20 — Parámetros con valores por omisión
**URL Picuino:** https://www.picuino.com/es/python-funciones-argumentos.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** booleanos y comparaciones, if/elif/else, for + range, for anidado, continue/break, while, y de Clase 24a: `def`, parámetros, argumentos, `return` (incl. que sin `return` la función devuelve `None`). Aún sin strings (indexing/métodos) ni listas.
- **Contenidos nuevos:** parámetros con valores por omisión (`def funcion(parametro, opcional=valor):`), qué pasa al omitir o indicar el argumento al llamar, regla de orden (los parámetros opcionales siempre van a la derecha de los obligatorios).
- **Contextos temáticos:** videojuego del liceo (menú de nueva partida), cuenta de Instagram del CEE, sonido del aniversario del liceo, torneo de e-sports del CEE — mezcla variada (regla 3).
- **Nota de alcance:** última clase del bloque Abstracción antes de pasar a Strings (Clase 25). Por eso, además del contenido nuevo (valores por omisión), la Práctica Independiente cierra con una síntesis que integra `def` + parámetros + `return` + valor por omisión + condicional, ya visto todo desde Clase 24a y clases anteriores.

## Objetivo

Diseñar funciones con parámetros con valores por omisión para el caso de uso más frecuente, con anticipación.

## Propósito

Anticipar es pensar de antemano en lo que la otra persona necesitará, para tenerlo listo antes de que lo pida. Hoy lo practicamos dejando valores por defecto en nuestras funciones, para el caso más común.

## Estructura de la clase

### 1. Haz Ahora (6 min)

El equipo de estudiantes que programa un videojuego para jugar en los recreos está armando el menú de "nueva partida". Casi todos los jugadores dejan la dificultad en "normal" sin tocar nada, salvo quienes eligen explícitamente otra. Sabiendo que ustedes programan, el equipo les pide ayuda para automatizar esto — pero antes quiere que tengan clara la lógica:

1. Si alguien crea una partida nueva y no toca la configuración de dificultad, ¿en qué dificultad empieza?
2. Si alguien sí elige "difícil" antes de empezar, ¿en qué dificultad queda esa partida?
3. De los dos datos de esta configuración —el nombre del jugador y la dificultad— ¿cuál es el que casi nunca hace falta escribir, porque ya tiene un valor pensado de antemano?

**Respuestas esperadas:**
1. Normal.
2. Difícil.
3. La dificultad.

### 2. Introducción al Contenido Nuevo (20 min)

**Concepto 1: Qué es un valor por omisión**
- Definición: un parámetro puede tener un valor "por omisión" (o "por defecto") escrito en la propia definición de la función. Si quien la llama no indica ese argumento, Python usa automáticamente ese valor.
- Ejemplo:
  ```python
  def saludo(nombre="María"):
      print("Hola,", nombre)

  saludo()
  saludo("Camila")
  ```
  ```
  >> Hola, María
  >> Hola, Camila
  ```
- Idea clave: un valor por omisión anticipa el caso más común, para que quien usa la función no tenga que escribir siempre el mismo dato.

**Concepto 2: Sintaxis — declarar el valor por omisión**
- Definición: se escribe con `=` justo después del nombre del parámetro, dentro de los paréntesis de `def`: `def funcion(parametro, opcional=valor):`.
- Ejemplo:
  ```python
  def nueva_partida(nombre_jugador, dificultad="normal"):
      print("Jugador:", nombre_jugador, "- Dificultad:", dificultad)
  ```
- Idea clave: el `=` dentro de `def` no es una comparación ni una asignación común — define el valor que se usa cuando el argumento se omite.

**Concepto 3: Omitir o indicar el argumento al llamar**
- Definición: al llamar la función, se puede omitir el argumento que tiene valor por omisión (y se usa ese valor) o indicarlo explícitamente (y ese valor reemplaza al de por omisión, solo para esa llamada).
- Ejemplo:
  ```python
  nueva_partida("Fernanda")
  nueva_partida("Benjamín", "difícil")
  ```
  ```
  >> Jugador: Fernanda - Dificultad: normal
  >> Jugador: Benjamín - Dificultad: difícil
  ```
- Idea clave: el valor por omisión no es fijo para siempre — solo se usa cuando esa llamada específica no trae ese argumento.

**Concepto 4: Regla de orden — opcionales a la derecha**
- Definición: los parámetros con valor por omisión siempre se escriben después de los parámetros obligatorios. Python no permite lo contrario.
- Ejemplo:
  ```python
  def funcion_valida(obligatorio, opcional=10):
      return obligatorio + opcional

  def funcion_invalida(opcional=10, obligatorio):
      return obligatorio + opcional
  ```
  ```
  >> SyntaxError: non-default argument follows default argument
  ```
- Idea clave: si un parámetro obligatorio pudiera ir después de uno opcional, Python no sabría a cuál de los dos corresponde un argumento dado sin nombre.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Escribir el parámetro opcional antes del obligatorio | `SyntaxError: non-default argument follows default argument` | Ordenar los parámetros: obligatorios primero, opcionales al final |
| Pensar que el valor por omisión sigue aplicando aunque se pase un argumento distinto | El valor pasado reemplaza al de por omisión solo para esa llamada — no cambia la definición de la función | Recordar que cada llamada es independiente; el valor por omisión solo se usa si se omite el argumento |
| Confundir "parámetro opcional" con "parámetro que no importa" | Si se decide omitirlo, igual afecta el resultado (usa el valor por omisión, no `None` ni vacío) | Verificar cuál es el valor por omisión y si tiene sentido para el caso que se está probando |

### 3. Práctica Guiada (25 min)

El equipo de desarrollo quiere que la misma función de bienvenida también calcule cuántos puntos de bono parte teniendo el jugador según la dificultad elegida: quienes juegan en difícil parten con más puntos de bono, quienes juegan en fácil parten con menos, y en normal con un valor intermedio.

**El programa debe:**
- Definir una función con el nombre del jugador (obligatorio) y la dificultad (opcional, con "normal" como valor por omisión).
- Calcular el bono de puntos iniciales: más en difícil, menos en fácil, un valor intermedio en normal.
- Devolver ese bono de puntos con `return`.
- Llamar la función dos veces —una sin indicar dificultad, otra indicando una distinta— y mostrar el mensaje de bienvenida con el bono de cada jugador.

**Resultado esperado:**
```
Bienvenido, Fernanda. Partes con 20 puntos de bono.
Bienvenido, Benjamín. Partes con 50 puntos de bono.
```

- Solución:
  ```python
  def nueva_partida(nombre_jugador, dificultad="normal"):
      if dificultad == "difícil":
          return 50
      elif dificultad == "normal":
          return 20
      else:
          return 5

  bono_fernanda = nueva_partida("Fernanda")
  print("Bienvenido, Fernanda. Partes con", bono_fernanda, "puntos de bono.")

  bono_benjamin = nueva_partida("Benjamín", "difícil")
  print("Bienvenido, Benjamín. Partes con", bono_benjamin, "puntos de bono.")
  ```

### 4. Práctica Independiente (18 min)

**Ejercicio 1 — Cuenta de Instagram del CEE**

La cuenta de Instagram del Centro de Estudiantes publica un mensaje de bienvenida cada vez que llega alguien nuevo a seguirla. Casi siempre usan el mismo emoji de fiesta, pero en fechas especiales —el aniversario del liceo, un campeonato ganado— quieren poder cambiar el emoji sin tocar el resto del mensaje.

**El programa debe:**
- Definir una función que reciba el nombre de quien sigue la cuenta (obligatorio) y el emoji a usar (opcional, con 🎉 como valor por omisión).
- Devolver el mensaje de bienvenida armado con el nombre y el emoji, usando `return`.
- Llamar la función para dos seguidores —uno sin indicar emoji, otro indicando un emoji distinto— y mostrar ambos mensajes.

**Resultado esperado:**
```
¡Bienvenido/a, Valentina! 🎉
¡Bienvenido/a, Matías! 🏆
```

- Solución:
  ```python
  def mensaje_bienvenida(nombre_seguidor, emoji="🎉"):
      return "¡Bienvenido/a, " + nombre_seguidor + "! " + emoji

  print(mensaje_bienvenida("Valentina"))
  print(mensaje_bienvenida("Matías", "🏆"))
  ```

**Ejercicio 2 — Sonido del aniversario del liceo**

El equipo de sonido del aniversario del liceo maneja el volumen del parlante bluetooth para cada canción. Para la mayoría dejan el volumen en un nivel estándar, pero para el himno del liceo o durante los discursos necesitan bajarlo o subirlo, sin tener que recordar el número exacto cada vez.

**El programa debe:**
- Definir una función que reciba el nombre de la canción (obligatorio) y el volumen (opcional, con 70 como valor por omisión).
- Devolver un mensaje indicando qué canción suena y a qué volumen, usando `return`.
- Llamar la función para dos canciones —una sin indicar volumen, otra indicando un volumen distinto— y mostrar ambos mensajes.

**Resultado esperado:**
```
Rayando el Sol está sonando a volumen 70
Himno del Liceo está sonando a volumen 40
```

- Solución:
  ```python
  def reproducir_cancion(nombre_cancion, volumen=70):
      return nombre_cancion + " está sonando a volumen " + str(volumen)

  print(reproducir_cancion("Rayando el Sol"))
  print(reproducir_cancion("Himno del Liceo", 40))
  ```

**Ejercicio 3 — Torneo de e-sports del CEE**

El Centro de Estudiantes organiza un torneo de videojuegos para recaudar fondos para la gira de estudios. La inscripción individual tiene un precio fijo, pero quienes se inscriben en pareja reciben un descuento — normalmente el mismo monto, salvo en fechas de promoción especial donde el descuento sube. El encargado de las inscripciones ya se equivocó calculando el descuento a mano más de una vez.

**El programa debe:**
- Definir una función con el precio de inscripción y si la persona se inscribe en pareja (obligatorios), y el monto del descuento como dato opcional (con \$1.000 como valor por omisión).
- Si la persona se inscribe en pareja, restar el descuento del precio; si no, dejarlo igual.
- Devolver el precio final con `return`.
- Pedir el precio de inscripción y si la persona va en pareja; llamar la función sin indicar descuento, y mostrar cuánto debe pagar.

**Resultado esperado:**

| | Ejemplo 1 | Ejemplo 2 |
|---|---|---|
| 📥 *El usuario ingresa* | `8000`, `si` | `8000`, `no` |
| 📤 *El programa imprime* | `Debe pagar: 7000` | `Debe pagar: 8000` |

- Solución:
  ```python
  def costo_inscripcion(precio_base, en_pareja, descuento=1000):
      if en_pareja:
          return precio_base - descuento
      return precio_base

  precio_torneo = int(input("¿Cuál es el precio de inscripción individual? "))
  inscripcion_pareja = input("¿Se inscribe en pareja? (si/no) ") == "si"

  total_a_pagar = costo_inscripcion(precio_torneo, inscripcion_pareja)
  print("Debe pagar:", total_a_pagar)
  ```

**Ejercicio 4 — Desafío: Torneo de e-sports del CEE (recaudación completa)** *(opcional)*

El día del torneo, el encargado de las inscripciones recibe varios equipos seguidos en la puerta. Quiere repetir el cálculo del Ejercicio 3 para cada equipo sin cerrar el programa entre uno y otro, y saber al final cuánto se recaudó en total.

**El programa debe:**
- Reutilizar la misma lógica de la función de inscripción (precio, si va en pareja, descuento opcional).
- Repetir el cálculo para distintos equipos hasta que el encargado escriba "listo" en vez del precio.
- Ir acumulando el total recaudado de todas las inscripciones y mostrarlo al terminar.

**Resultado esperado:**
```
¿Precio de inscripción? (o "listo" para terminar) 8000
¿Se inscribe en pareja? (si/no) si
Ese equipo debe pagar: 7000
¿Precio de inscripción? (o "listo" para terminar) 6000
¿Se inscribe en pareja? (si/no) no
Ese equipo debe pagar: 6000
¿Precio de inscripción? (o "listo" para terminar) listo
Total recaudado: 13000
```

- Solución:
  ```python
  def costo_inscripcion(precio_base, en_pareja, descuento=1000):
      if en_pareja:
          return precio_base - descuento
      return precio_base

  precio_ingresado = input('¿Precio de inscripción? (o "listo" para terminar) ')
  total_recaudado = 0

  while precio_ingresado != "listo":
      precio_equipo = int(precio_ingresado)
      en_pareja = input("¿Se inscribe en pareja? (si/no) ") == "si"
      pago_equipo = costo_inscripcion(precio_equipo, en_pareja)
      print("Ese equipo debe pagar:", pago_equipo)
      total_recaudado = total_recaudado + pago_equipo
      precio_ingresado = input('¿Precio de inscripción? (o "listo" para terminar) ')

  print("Total recaudado:", total_recaudado)
  ```

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
def calcula_puntaje(base, bono=10):
    return base + bono

resultado = calcula_puntaje(50)
print("Puntaje:", resultado)
```
¿Qué imprime este programa?
- A: Puntaje: 50
- B: Puntaje: 60
- C: Puntaje: 10
- D: Error, falta indicar el segundo argumento

**Respuesta correcta:** B
**Justificación:** como no se indicó el segundo argumento, Python usa el valor por omisión (10), y la función devuelve 50+10=60.

**Pregunta 2:**
```python
def calcula_puntaje(base, bono=10):
    return base + bono

resultado = calcula_puntaje(50, 30)
print("Puntaje:", resultado)
```
¿Qué imprime este programa?
- A: Puntaje: 50
- B: Puntaje: 60
- C: Puntaje: 80
- D: Error, no se puede reemplazar un valor por omisión

**Respuesta correcta:** C
**Justificación:** al indicar 30 explícitamente, ese valor reemplaza al de por omisión solo en esta llamada: 50+30=80.

**Pregunta 3:**
```python
def calcula_total(cantidad, precio_unitario=1000, iva):
    return cantidad * precio_unitario * iva
```
¿Qué ocurre al intentar definir esta función?
- A: Se define bien, pero falla recién al llamarla sin indicar `iva`
- B: Se define sin problema, porque Python permite cualquier orden de parámetros
- C: Se define bien, y `iva` toma automáticamente el valor por omisión de `precio_unitario`
- D: Python lanza un error al definirla, porque el parámetro obligatorio `iva` está después del parámetro opcional `precio_unitario`

**Respuesta correcta:** D
**Justificación:** los parámetros obligatorios deben ir siempre antes que los que tienen valor por omisión; Python lanza `SyntaxError` apenas se intenta definir la función, sin llegar a ejecutar nada.

### Cierre (5 min)

**Objetivo de la clase:** Diseñar funciones con parámetros con valores por omisión para el caso de uso más frecuente, con anticipación.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan claro te quedó cuándo Python usa el valor por omisión de un parámetro y cuándo usa el que tú le indicas?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación —dentro o fuera de la programación— anticipar lo que la otra persona necesitará (dejando un valor por defecto razonable) le ahorraría trabajo a ambos?

## Decisiones de diseño relevantes

- **Guiada calibrada al nivel del Ejercicio 3 (regla 20, default desde Clase 24):** combina valor por omisión + `return` + condicional de 3 vías (difícil/normal/fácil), mismo escenario del Haz Ahora (videojuego), con una pregunta relacionada pero distinta (bono de puntos en vez de dificultad por defecto).
- **Ejercicios 1-2 sin condicional interno** (mismo patrón de diseño que 24a): verifican el mecanismo de valor por omisión de forma aislada. Ejercicio 1 devuelve una concatenación de strings (sin necesidad de `str()`, ambos operandos ya son texto); Ejercicio 2 devuelve un string que mezcla texto y un número vía `str()` — válido porque la regla 14 del CLAUDE.md ("comas, nunca `+` y `str()`") aplica explícitamente solo a `print()`, no a `return`.
- **Ejercicios 3 y 4 cierran el bloque Abstracción** combinando `def` + parámetros + `return` + valor por omisión + condicional (Ejercicio 3) y agregando el `while` ya visto en Clase 22 (Ejercicio 4) — respondiendo al pedido de Diego de que esta clase sintetice todo lo de funciones antes de pasar a Strings (Clase 25).
- **Ejercicio 4 reutiliza la misma función del Ejercicio 3** dentro de un ciclo con centinela `"listo"` (mismo patrón que el desafío de Clase 24a), para practicar valor por omisión junto con el acumulador ya visto.
- **Actitud elegida: Anticipación** — conecta directamente con la esencia de un valor por omisión (pensar de antemano en el caso más común de uso, para que la otra persona no tenga que especificarlo siempre).
- **Contextos:** videojuego (Haz Ahora/Guiada), Instagram del CEE y sonido del aniversario (Ejercicios 1-2), torneo de e-sports del CEE (Ejercicios 3-4) — variedad respecto a los contextos ya usados en 24a (kiosco CEE, huerto, club deportivo, peña de la vendimia, escuela de rock).
