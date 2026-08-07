# Clase 22 — While

**Estado:** Spec aprobada — 2026-08-07
**Clase Picuino:** N° 18 — Sentencia `while`
**URL Picuino:** https://www.picuino.com/es/python-while.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** `for`, `range()`, `for` anidado, `continue` y `break` (todo hasta N°21.5 inclusive)
- **Contenidos nuevos:** `while`, contraste `for` vs `while`, patrón `while True` + `break`, riesgo de bucle infinito
- **Contextos temáticos:** Liceo Bicentenario Mario Bertero Cevasco (buzón de sugerencias del Centro de Estudiantes, aforo del gimnasio en el Aniversario/Fiesta Criolla, cupos de un taller piloto de fotografía, préstamo de notebooks del laboratorio de computación)

## Objetivo

Construir programas con ciclos `while` que repitan un proceso hasta cumplir una condición, evitando bucles infinitos, con perseverancia.

## Propósito

La perseverancia es seguir intentando algo hasta lograrlo, sin detenerte a la primera dificultad. Hoy la practicamos programando ciclos `while` que repiten un proceso hasta que se cumple lo que buscamos.

## Estructura de la clase

### 1. Haz Ahora (6 min)

La directora Rossana le pidió al Centro de Estudiantes armar un buzón de sugerencias para mejorar el liceo. Cada persona puede escribir tantas sugerencias como quiera, una por una, hasta que sienta que ya no tiene más que decir — nadie sabe de antemano si van a llegar 2 sugerencias o 20.

El Centro de Estudiantes, sabiendo que ustedes programan, les pide ayuda para automatizar este buzón — pero antes, quiere que tengan clara la lógica:

1. Si alguien escribe tres sugerencias y después dice que ya terminó, ¿cuántas sugerencias se recibieron en total?
2. ¿Qué tiene que pasar para que se deje de pedir sugerencias?
3. Si esa señal de "ya terminé" nunca llega, ¿cuántas veces se sigue pidiendo una sugerencia más?

**Respuestas esperadas:**
1. Tres.
2. Que la persona avise que no quiere escribir más.
3. Para siempre — no hay forma de que el proceso se detenga solo.

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: `while`**
- Definición: `while` repite un bloque de código mientras una condición sea verdadera. A diferencia de `for`, la condición se revisa antes de cada vuelta y puede depender de algo que cambia mientras el programa corre.
- Ejemplo:
  ```python
  contador = 0
  while contador < 3:
      print("Vuelta", contador)
      contador = contador + 1
  ```
- Idea clave: `while` revisa la condición ANTES de cada vuelta — si la condición nunca se vuelve falsa, el ciclo no termina.

**Concepto 2: `for` vs `while` — ¿cuál corresponde?**
- Definición: se usa `for` cuando se sabe de antemano cuántas repeticiones habrá (recorrer un rango, una lista). Se usa `while` cuando eso depende de una condición que solo se conoce mientras el programa corre.
- Ejemplo:
  ```python
  for numero in range(5):
      print(numero)

  respuesta = input("Sigue jugando? (si/no): ")
  while respuesta == "si":
      respuesta = input("Sigue jugando? (si/no): ")
  ```
- Idea clave: "¿Sé de antemano cuántas repeticiones habrá?" — si sí, `for`; si no, `while`.

**Concepto 3: `while True` + `break`**
- Definición: `while True` crea un ciclo que se repite indefinidamente; `break` lo detiene apenas se cumple una condición interna, sin tener que ponerla en el encabezado del `while`.
- Ejemplo:
  ```python
  while True:
      sugerencia = input("Escribe una sugerencia (o 'fin' para terminar): ")
      if sugerencia == "fin":
          break
      print("Sugerencia registrada:", sugerencia)
  ```
- Idea clave: `while True` + `break` sirve cuando conviene revisar la condición de salida en medio del proceso, no antes de empezar.

**Concepto 4: bucle infinito**
- Definición: si la condición del `while` nunca se vuelve falsa (o nunca se llega al `break`), el programa se repite para siempre.
- Ejemplo:
  ```python
  contador = 0
  while contador < 5:
      print("Esto se repite para siempre")
      # falta actualizar contador
  ```
- Idea clave: todo `while` necesita algo que, tarde o temprano, haga falsa la condición (o dispare el `break`) — si no, el programa nunca termina.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Olvidar actualizar la variable de la condición | Bucle infinito | Revisar que dentro del `while` haya una línea que cambie esa variable |
| Confundir `while` con `if` | El bloque se ejecuta una sola vez en vez de repetirse | Verificar que realmente haga falta repetir |
| Usar `while` cuando la cantidad de repeticiones ya se sabe | Código más largo y propenso a error | Preferir `for` con `range()` en ese caso |

**Regla crítica para escribir el ICN (y todo el spec):** Cualquier mención a código Python o términos técnicos va entre backticks `así`.

### 3. Práctica Guiada (23 min)

El Centro de Estudiantes también quiere saber cuántas sugerencias llegaron en total, no solo registrarlas una por una.

**El programa debe:**
- Pedir sugerencias una por una, mientras la persona quiera seguir escribiendo.
- Detenerse apenas la persona escriba "fin".
- Mostrar cuántas sugerencias se recibieron en total (sin contar la palabra "fin").

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`Más wifi en el patio`<br>`Bebederos de agua nuevos`<br>`fin` | 📥 *El usuario ingresa:*<br>`fin` |
| 📤 *El programa imprime:*<br>`Se registraron 2 sugerencias.` | 📤 *El programa imprime:*<br>`Se registraron 0 sugerencias.` |

- Solución:
  ```python
  total_sugerencias = 0
  while True:
      sugerencia = input("Escribe una sugerencia (o 'fin' para terminar): ")
      if sugerencia == "fin":
          break
      total_sugerencias = total_sugerencias + 1
  print("Se registraron", total_sugerencias, "sugerencias.")
  ```

### 4. Práctica Independiente (17 min)

**Ejercicio 1 — Aforo del gimnasio**
El profesor de Educación Física quiere controlar cuántas personas van entrando al gimnasio durante el ensayo de la Fiesta Criolla del Aniversario, hasta llegar al aforo máximo de 150 personas. Cada vez que entra un grupo, el encargado de la puerta anota cuántas personas venían en ese grupo.

**El programa debe:**
- Ir sumando la cantidad de personas que van entrando, grupo por grupo.
- Detenerse en cuanto se alcance o supere el aforo máximo.
- Mostrar cuántas personas quedaron finalmente registradas.

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`50`<br>`60`<br>`45` | 📥 *El usuario ingresa:*<br>`100`<br>`100` |
| 📤 *El programa imprime:*<br>`Aforo alcanzado con 155 personas.` | 📤 *El programa imprime:*<br>`Aforo alcanzado con 200 personas.` |

- Solución:
  ```python
  personas_registradas = 0
  aforo_maximo = 150
  while personas_registradas < aforo_maximo:
      personas_grupo = int(input("¿Cuántas personas entraron en este grupo? "))
      personas_registradas = personas_registradas + personas_grupo
  print("Aforo alcanzado con", personas_registradas, "personas.")
  ```

**Ejercicio 2 — Cupos del taller nuevo**
La directora Rossana quiere abrir un taller piloto de fotografía este semestre, pero el liceo solo cuenta con 3 cámaras disponibles para prestar, así que los cupos son limitados. A medida que van llegando las solicitudes, alguien tiene que ir anotando quién se inscribe.

**El programa debe:**
- Pedir el nombre de cada estudiante que se inscribe.
- Contar cuántos se han inscrito hasta el momento.
- Detenerse apenas se llenen los cupos disponibles.
- Mostrar cuántos estudiantes quedaron inscritos.

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`Matías`<br>`Camila`<br>`Josefa` | 📥 *El usuario ingresa:*<br>`Diego`<br>`Valentina`<br>`Ignacio` |
| 📤 *El programa imprime:*<br>`Taller lleno. Quedaron inscritos: 3 estudiantes.` | 📤 *El programa imprime:*<br>`Taller lleno. Quedaron inscritos: 3 estudiantes.` |

- Solución:
  ```python
  cupos_disponibles = 3
  inscritos = 0
  while inscritos < cupos_disponibles:
      nombre = input("Nombre de quien se inscribe: ")
      inscritos = inscritos + 1
  print("Taller lleno. Quedaron inscritos:", inscritos, "estudiantes.")
  ```

**Ejercicio 3 — Desafío: préstamo de notebooks del laboratorio** *(opcional, para quien termine antes)*
El encargado del laboratorio de computación quiere automatizar el préstamo de notebooks para los recreos. Hay una cantidad limitada disponible, y el préstamo se detiene si se acaban los notebooks o si el encargado escribe "cerrar" porque ya terminó el recreo — lo que ocurra primero.

**El programa debe:**
- Partir con una cantidad de notebooks disponibles.
- Ir registrando, uno por uno, a quién se le presta un notebook.
- Detenerse si se acaban los notebooks o si se ingresa "cerrar" en vez de un nombre.
- Mostrar cuántos notebooks se prestaron y cuántos quedaron disponibles.

<details>
<summary>💡 Pista — dos formas de terminar</summary>
Este ciclo tiene dos motivos distintos para detenerse. Revisa ambos antes de pedir un nombre.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`Fernanda`<br>`Tomás`<br>(con 2 notebooks disponibles) | 📥 *El usuario ingresa:*<br>`Antonia`<br>`cerrar`<br>(con 5 notebooks disponibles) |
| 📤 *El programa imprime:*<br>`Notebooks prestados: 2 . Disponibles: 0` | 📤 *El programa imprime:*<br>`Notebooks prestados: 1 . Disponibles: 4` |

- Solución:
  ```python
  notebooks_disponibles = 2
  notebooks_prestados = 0
  while True:
      if notebooks_disponibles == 0:
          break
      nombre = input("Nombre de quien retira un notebook (o 'cerrar' para terminar): ")
      if nombre == "cerrar":
          break
      notebooks_prestados = notebooks_prestados + 1
      notebooks_disponibles = notebooks_disponibles - 1
  print("Notebooks prestados:", notebooks_prestados, ". Disponibles:", notebooks_disponibles)
  ```

### 5. Ticket de Salida (8 min)

**Pregunta 1:**
```python
contador = 0
while contador < 3:
    print("Vuelta", contador)
    contador = contador + 1
```
¿Qué imprime este programa?
- A: `Vuelta 0` / `Vuelta 1` / `Vuelta 2`
- B: `Vuelta 1` / `Vuelta 2` / `Vuelta 3`
- C: `Vuelta 0` / `Vuelta 1` / `Vuelta 2` / `Vuelta 3`
- D: `Vuelta 3` (una sola vez)
**Respuesta correcta:** A
**Justificación:** `contador` parte en 0 y la condición `contador < 3` se cumple para 0, 1 y 2; se hace falsa recién cuando `contador` llega a 3, así que se imprime 3 veces empezando en 0.

**Pregunta 2:**
```python
intentos = 0
while intentos < 5:
    print("Intentando...")
```
¿Qué pasa al ejecutar este programa?
- A: Imprime "Intentando..." 5 veces y termina.
- B: Imprime "Intentando..." una vez y termina.
- C: Nunca termina — se repite para siempre.
- D: Muestra un error porque falta el `break`.
**Respuesta correcta:** C
**Justificación:** `intentos` nunca se actualiza dentro del ciclo, así que la condición `intentos < 5` siempre es verdadera — bucle infinito.

**Pregunta 3:**
```python
while True:
    clave = input("Ingresa la clave: ")
    if clave == "1234":
        break  # <- esta línea
    print("Clave incorrecta, intenta de nuevo")
print("Acceso concedido")
```
¿Cuándo se ejecuta la línea marcada?
- A: Cada vez que se pide la clave, sin excepción.
- B: Solo cuando la clave ingresada es igual a "1234".
- C: Solo la primera vez que se ejecuta el programa.
- D: Nunca, porque está dentro de un `if`.
**Respuesta correcta:** B
**Justificación:** `break` solo se ejecuta cuando se cumple la condición del `if` (clave correcta); mientras la clave sea incorrecta, el ciclo sigue pidiendo.

### Cierre (5 min)

**Objetivo de la clase:** Construir programas con ciclos `while` que repitan un proceso hasta cumplir una condición, evitando bucles infinitos, con perseverancia.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes programando ciclos `while`, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación de tu vida —no solo programando— te ha tocado perseverar repitiendo algo hasta lograrlo, sin saber de antemano cuántos intentos te tomaría?

## Decisiones de diseño relevantes

- **Actitud:** Perseverancia — elegida por Diego entre Método, Precisión, Criterio y Perseverancia. Conecta con "repetir hasta lograrlo", coherente con el patrón `while True` + `break` ("repetir hasta que pase algo").
- **Objetivo ajustado:** la primera versión mencionaba explícitamente "`while True`" y "actualizando bien la variable de control" — Diego pidió sacar ambas menciones literales del objetivo, dejando el énfasis en "evitando bucles infinitos" sin prescribir la sintaxis exacta de la solución.
- **Contexto temático:** anclado en el Liceo Bicentenario Mario Bertero Cevasco y la directora Rossana (real, confirmado en `referencia-isla-de-maipo`), a pedido explícito de Diego ("algo para nuestro liceo"). Escenario compartido de Haz Ahora + Guiada: buzón de sugerencias del Centro de Estudiantes (calza con el ejemplo Picuino "repetir hasta que la respuesta sea fin" y con el patrón `while True` + `break`). Independiente: aforo del gimnasio (calza con el ejemplo Picuino "sumar hasta llegar a 1000"), cupos de un taller piloto de fotografía, y desafío de préstamo de notebooks del laboratorio (combina dos condiciones de salida distintas).
- **Corrección de nombre:** Diego pidió referirse siempre a "directora Rossana", nunca solo "Rossana" — aplicado en Haz Ahora y Ejercicio 2.
- **Ejercicio 2 — narrativa alargada:** la primera versión era demasiado directa ("El programa debe ir anotando...", redundante con la sección `**El programa debe:**` que viene después). Se reescribió para dar contexto (3 cámaras disponibles como razón del cupo limitado) sin adelantar la tarea, subiendo de 60 a 73 palabras.
- **Presupuesto de palabras verificado:** Guiada 47 palabras (bajo el rango, sin problema — el rango es un techo), Ejercicio 1: 76, Ejercicio 2: 73, Ejercicio 3 (desafío): 88 — todos dentro o cerca del rango 60-90 acordado.
