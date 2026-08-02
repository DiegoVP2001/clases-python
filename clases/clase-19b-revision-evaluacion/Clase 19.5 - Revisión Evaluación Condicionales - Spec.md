# Clase 19.5 — Revisión Evaluación Condicionales

**Estado:** Spec aprobada — 2026-08-01
**Clase Picuino:** N/A — clase de cierre formativo (retoma N°11 *if anidadas* y N°12 *elif*, e introduce el contraste con `if` independientes)
**URL Picuino:** —

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** parejas cruzadas (un estudiante de cada tramo de rendimiento por pareja)
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Fecha prevista:** lunes 3 de agosto de 2026
- **Contenidos previos asumidos:** booleanos y comparaciones (Clase 8a), operadores lógicos (Clase 8b), análisis de condiciones (Clase 8c), `if`/`else` (Clase 11), `if` anidadas (Clase 13), `elif` (Clase 14), `input()` y conversión de tipos (Clase 7)
- **Contenidos nuevos:** varios `if` independientes seguidos, contrastados explícitamente con `elif` y con el anidamiento; probar el valor del borde como hábito de verificación
- **Contextos temáticos:** los mismos ítems de la Evaluación 2 (app de hábitos de estudio, torneo de equipos, micro Isla de Maipo–Talagante, alcancía digital en dólares)

## Objetivo

Distinguir si dos condiciones son independientes, excluyentes o dependientes, escribir la forma de `if` que corresponde a cada caso y comprobarla en el valor del borde, con rigurosidad.

## Propósito

La rigurosidad es revisar justo el caso donde algo puede fallar, en vez de confiar en que salió bien porque funcionó una vez. Hoy la practicamos probando el valor exacto del borde de cada condición.

## OAs MINEDUC

`OA1, OA3 | OAd`

- **OA1** — el eje de la clase es análisis de soluciones alternativas: tres formas posibles para el mismo par de preguntas, y decidir cuál corresponde.
- **OA3** — ambos tramos escriben o depuran programas completos con condicionales.
- **OAd** — el tramo alto justifica por qué un caso límite rompe un programa; el otro tramo, por qué una rama va anidada y no suelta.

---

## Apertura (4 min)

Bloque propio, antes del Haz Ahora. Se entregan los Colabs de devolución de la Evaluación 2 y se dice de frente, en una frase: **la nota está cerrada, no hay recuperativa, y hoy no se negocian puntos.** El encuadre es que la prueba ya cumplió su función de medir, y lo que queda es el error que le costó puntos a casi todo el curso — al tramo alto también.

Los cuadernos se abren y se miran ~2 minutos en silencio. **No se revisa ítem por ítem en voz alta**: al tramo alto la Sección 2 no le dejó nada que corregir (97-100%), así que una corrección proyectada los desperdiciaría.

## Estructura de la clase

### 1. Haz Ahora (7 min)

> Nota de conducción: el timer del PPT cubre solo este tramo de trabajo autónomo (`⚡ Haz Ahora <<7:00>>`). La revisión en conjunto de las respuestas toma ~5 min adicionales y la conduce Diego sin reloj.

Tres programas de la prueba que estuvieron mal resueltos, tal como quedaron. Están en celdas ejecutables: se corren, no se adivinan.

**Programa 1**

```python
racha_dias_estudio = 12

if racha_dias_estudio >= 3:
    mensaje_racha = "Racha en marcha: no la cortes."
elif racha_dias_estudio >= 7:
    mensaje_racha = "Buena constancia."
elif racha_dias_estudio >= 14:
    mensaje_racha = "Racha de élite."
else:
    mensaje_racha = "Recién empezando."

print("Categoría de tu racha:", mensaje_racha)
```

**Programa 2**

```python
puntaje_equipo = 18
puntaje_minimo_clasificacion = 18

if puntaje_equipo > puntaje_minimo_clasificacion:
    mensaje_torneo = "El equipo clasifica a semifinales."
else:
    mensaje_torneo = "El equipo queda eliminado."

print("Resultado del torneo:", mensaje_torneo)
```

**Programa 3**

```python
tiene_pase_escolar = "si"
saldo_tarjeta_bip = 200

if tiene_pase_escolar == "si":
    print("Sube gratis con su pase escolar.")

if saldo_tarjeta_bip >= 800:
    print("Paga el pasaje con la tarjeta bip.")
else:
    print("No le alcanza el saldo para el pasaje.")
```

1. Ejecuta el Programa 1. ¿Qué imprime? ¿Y qué debería imprimir con una racha de 12 días?
2. Ejecuta el Programa 2. Después cambia el puntaje a 19 y ejecútalo otra vez. ¿En cuál de los dos casos el resultado quedó equivocado?
3. Ejecuta el Programa 3. ¿Cuántas líneas imprime? ¿Pueden ser verdaderas las dos al mismo tiempo?
4. De los tres programas, ¿cuál se parece a un error que cometiste tú en la prueba?

**Respuestas esperadas:**
1. Imprime `"Racha en marcha: no la cortes."`. Debería imprimir `"Buena constancia."`, porque 12 días ya pasó los 7.
2. El resultado quedó equivocado con 18: dice que queda eliminado, pero 18 es exactamente el mínimo para clasificar. Con 19 el resultado está bien.
3. Imprime dos líneas. No pueden ser verdaderas las dos: si sube gratis con su pase, la pregunta del saldo ni siquiera corresponde hacerla.
4. Registro personal, sin respuesta única. Se responde mirando el Colab de devolución que acaban de recibir.

### 2. Introducción al Contenido Nuevo (15 min)

Se proyecta el material ya terminado `Clase 19.5 - Revisión Evaluación Condicionales - Tres Formas.html` (los tres casos representados como ríos animados). Cada pregunta que quedó abierta en el Haz Ahora se cierra con una tarjeta del HTML.

Frase de entrada al pasar del Haz Ahora al HTML: *"dos de estos tres los reconocen de la prueba. El tercero no lo hemos visto nunca — y es el que explica por qué el tercer programa se comportó así."*

**Concepto 1: Independientes — varios `if` seguidos**
- Definición: cuando dos preguntas no tienen nada que ver entre sí, cada una va en su propio `if`. Python revisa todos, uno por uno, sin que el resultado de uno afecte al siguiente.
- Ejemplo:
  ```python
  if bateria_baja == True:
      print("Queda poca batería.")

  if hay_wifi_disponible == True:
      print("Hay wifi disponible.")
  ```
- Idea clave: cada `if` se revisa por su cuenta. Pueden cumplirse los dos, uno solo o ninguno.

**Concepto 2: Excluyentes — `if / elif / else`, y el orden decide**
- Definición: cuando las preguntas son distintas versiones de lo mismo y solo una puede ser la respuesta, van encadenadas con `elif`. El primer `elif` que se cumple se lleva todo y los de más abajo ni siquiera se revisan.
- Ejemplo:
  ```python
  if racha_dias_estudio >= 14:
      print("Categoría de tu racha:", "Racha de élite")
  elif racha_dias_estudio >= 7:
      print("Categoría de tu racha:", "Buena constancia")
  elif racha_dias_estudio >= 3:
      print("Categoría de tu racha:", "Racha en marcha")
  else:
      print("Categoría de tu racha:", "Recién empezando")
  ```
- Idea clave: la condición más exigente va primero. Si la más amplia va arriba, se lleva el agua de todas las de abajo y esas ramas nunca se alcanzan.

**Concepto 3: Una depende de la otra — `if` anidado**
- Definición: cuando la segunda pregunta solo tiene sentido si la primera resultó de cierta manera, la segunda va escrita **dentro** de la primera.
- Ejemplo:
  ```python
  if tiene_pase_escolar == "si":
      print("Sube gratis con su pase escolar.")
  else:
      if saldo_tarjeta_bip >= 800:
          print("Paga el pasaje con la tarjeta bip.")
      else:
          print("No le alcanza el saldo para el pasaje.")
  ```
- Idea clave: si escribes las dos preguntas sueltas, la segunda se hace siempre — incluso a quien ya subió con su pase. Es exactamente el Programa 3 del Haz Ahora.

**Concepto 4: Probar el valor del borde**
- Definición: el borde es el valor exacto donde una condición cambia de resultado. Un programa puede funcionar con todos los ejemplos que le probaste y fallar solo ahí.
- Ejemplo:
  ```python
  puntaje_equipo = 18
  puntaje_minimo_clasificacion = 18

  if puntaje_equipo >= puntaje_minimo_clasificacion:
      print("Resultado del torneo:", "El equipo clasifica a semifinales.")
  else:
      print("Resultado del torneo:", "El equipo queda eliminado.")
  ```
- Idea clave: cuando termines de escribir, prueba el valor exacto del borde. En estos programas son 14, 7, 3, 18 y 800.

**Errores típicos:**

| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Cadena de `elif` ordenada de menor a mayor | La condición más amplia se cumple primero y se lleva todos los casos. Las ramas más exigentes nunca se alcanzan. | Ordenar de mayor a menor exigencia, y probar un valor de cada franja. |
| Dos preguntas dependientes escritas como `if` sueltos | La segunda pregunta se hace siempre, aunque la primera ya haya resuelto el caso. Salen dos mensajes que se contradicen. | Escribir la segunda pregunta dentro del `if` o del `else` de la primera. |
| Usar `>` donde correspondía `>=` (o al revés) | El programa funciona con todos los ejemplos menos con el valor exacto del borde. | Probar siempre el valor del borde antes de dar el programa por terminado. |

### 3. Práctica Guiada (18 min)

La app de hábitos de estudio del Programa 1 no clasifica nada más: solo entrega la categoría de la racha. La versión completa tiene que hacer tres cosas a la vez, y cada una se relaciona distinto con las demás. Hoy la construimos entera.

**El programa debe:**
- Pedir la **racha de días seguidos** estudiando y si **ya estudió hoy**.
- Mostrar **una sola** categoría de racha, de la más exigente a la más básica.
- Mostrar **aparte** un aviso cuando todavía no registra estudio de hoy, sin que ese aviso dependa de la categoría que le tocó.
- **Solo si la racha viene en cero**, preguntar además hace cuántos días fue la última sesión, y avisar si todavía alcanza a retomar la racha anterior (menos de una semana) o si parte de nuevo.

<details>
<summary>💡 Pista — dónde va la pregunta de la última sesión</summary>
Si la escribes junto a las otras dos preguntas del principio, el programa se la hace a todo el mundo. Fíjate en qué momento esa pregunta recién tiene sentido, y escríbela ahí.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa* <pre>12<br>si</pre> | 📥 *El usuario ingresa* <pre>0<br>no<br>4</pre> |
| 📤 *El programa imprime* <pre>Categoría de tu racha: Buena constancia</pre> | 📤 *El programa imprime* <pre>Categoría de tu racha: Recién empezando<br>Aviso: todavía no registras estudio de hoy.<br>Todavía puedes retomar la racha anterior.</pre> |

- Solución:
  ```python
  racha_dias_estudio = int(input("¿Cuántos días seguidos llevas estudiando? "))
  estudio_hoy = input("¿Ya estudiaste hoy? (si/no): ")

  if racha_dias_estudio >= 14:
      print("Categoría de tu racha:", "Racha de élite")
  elif racha_dias_estudio >= 7:
      print("Categoría de tu racha:", "Buena constancia")
  elif racha_dias_estudio >= 3:
      print("Categoría de tu racha:", "Racha en marcha")
  else:
      print("Categoría de tu racha:", "Recién empezando")

  if estudio_hoy == "no":
      print("Aviso: todavía no registras estudio de hoy.")

  if racha_dias_estudio == 0:
      dias_ultima_sesion = int(input("¿Hace cuántos días fue tu última sesión? "))
      if dias_ultima_sesion < 7:
          print("Todavía puedes retomar la racha anterior.")
      else:
          print("Empiezas una racha nueva desde cero.")
  ```

Nota de conducción: el Ejemplo 1 usa **racha = 12**, el mismo valor del Programa 1 del Haz Ahora. Vale la pena hacerlo notar al terminar: es el mismo dato que hace media hora entregaba la categoría equivocada.

### 4. Práctica Independiente (20 min)

**Trabajo diferenciado en parejas cruzadas** — un estudiante de cada tramo por pareja. Ambas rutas trabajan sobre las **mismas dos especificaciones** (los ítems 2.2 y 2.3 de la Evaluación 2), desde lados opuestos: una las escribe, la otra las rompe.

Distribución del tiempo: **12 min de trabajo propio + 8 min de cruce.**

El emparejamiento es simétrico y hay que decirlo así al curso: quien diseña casos necesita un programa que probar, y quien repara necesita saber si su arreglo aguanta. **La Ruta A no hace de ayudantía de la Ruta B.**

---

#### Ruta A — para quienes ya resolvieron la Sección 2 completa

**Ejercicio 1 — La batería que rompe programas (obligatorio)**

Un programa que pasa todos los ejemplos que le probaste no es un programa correcto: es un programa que todavía no encuentras cómo romper. Tu trabajo hoy no es escribir programas, es escribir los casos que los hacen caer. Vas a preparar la batería de pruebas para las dos especificaciones de abajo, y en unos minutos se la vas a aplicar al programa de tu pareja.

**Especificación 1 — Micro a Talagante:** el sistema revisa primero si la persona tiene pase escolar vigente; si no lo tiene, revisa si el saldo de su tarjeta bip alcanza los \$800 del pasaje. Tres caminos posibles: sube gratis con su pase / paga el pasaje con la bip / no le alcanza el saldo.

**Especificación 2 — Ahorro semanal en dólares:** clasifica el monto ahorrado en la semana (puede tener decimales) en cuatro niveles: menos de 10 → *Recién empezando*; de 10 a menos de 30 → *En camino*; de 30 a menos de 60 → *Buen ahorro*; 60 o más → *¡Excelente semana!*

**El trabajo debe:**
- Entregar **al menos 3 casos por especificación**, cada uno con qué se ingresa, qué debería imprimir, y qué error estaría cazando.
- Incluir el **valor exacto del borde** de cada frontera: los \$800 de la micro, y el 10, el 30 y el 60 del ahorro.
- Incluir **al menos un caso donde un programa correcto y uno con las preguntas sueltas den resultados distintos** — el que distingue el anidado de dos `if` sueltos.

Formato de entrega, una tabla por especificación:

| Qué se ingresa | Qué debería imprimir | Qué error estaría cazando |
|---|---|---|
| | | |

**Ejercicio 2 — Probar el programa de tu pareja (obligatorio)**

Cuando tu pareja termine, pásale la batería completa y córranla juntos, caso por caso.

**El trabajo debe:**
- Anotar **cuál caso cayó** y qué imprimió en vez de lo esperado.
- Después de que tu pareja arregle el programa, **volver a correr la batería entera** — no solo el caso que falló. Un arreglo puede romper un caso que antes pasaba.
- Cerrar con una frase: ¿el programa aguanta ahora la batería completa, sí o no?

---

#### Ruta B — para quienes dejaron esos ejercicios sin terminar

Los dos ejercicios que quedaron en blanco, otra vez — pero esta vez decidiendo la estructura **antes** de escribir código. Completa primero la tabla de decisión y recién después abre la celda de código.

**Ejercicio 1 — Micro a Talagante (obligatorio)**

Para subir al micro que va desde Isla de Maipo hasta Talagante, el sistema revisa primero si la persona tiene pase escolar vigente. Si no lo tiene, recién ahí revisa si el saldo de su tarjeta bip alcanza para pagar el pasaje, que cuesta \$800. Según esos datos, el programa muestra cómo puede subir la persona.

**Antes de programar, completa esta tabla:**

| ¿Qué se pregunta? | ¿Depende de otra pregunta? | ¿Qué imprime? |
|---|---|---|
| ¿Tiene pase escolar vigente? | No — es la primera | `"Sube gratis con su pase escolar."` |
| ¿El saldo alcanza los \$800? | *(completar)* | *(completar)* |
| ¿Y si el saldo no alcanza? | *(completar)* | *(completar)* |

**El programa debe:**
- Pedir si la persona **tiene pase escolar vigente** (responde exactamente `"si"` o `"no"`).
- Si **no** tiene pase, pedir además el **saldo de la tarjeta bip**, un número entero en pesos.
- Verificar **primero** el pase escolar; solo si no lo tiene, verificar si el saldo **alcanza** los \$800.
- Mostrar el mensaje que corresponda a cada uno de los tres caminos.

<details>
<summary>💡 Pista — cuándo se pide el saldo</summary>
Si el saldo se pide al principio junto con el pase, el programa se lo pregunta también a quien va a subir gratis. Fíjate en tu tabla: la fila del saldo dice que depende de la primera pregunta, así que el `input()` del saldo va escrito dentro de esa rama.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa* <pre>si</pre> | 📥 *El usuario ingresa* <pre>no<br>500</pre> |
| 📤 *El programa imprime* <pre>Sube gratis con su pase escolar.</pre> | 📤 *El programa imprime* <pre>No le alcanza el saldo para el pasaje.</pre> |

- Solución:
  ```python
  tiene_pase_escolar = input("¿Tiene pase escolar vigente? (si/no): ")

  if tiene_pase_escolar == "si":
      print("Sube gratis con su pase escolar.")
  else:
      saldo_tarjeta_bip = int(input("Ingresa el saldo de la tarjeta bip: "))
      if saldo_tarjeta_bip >= 800:
          print("Paga el pasaje con la tarjeta bip.")
      else:
          print("No le alcanza el saldo para el pasaje.")
  ```

**Ejercicio 2 — Ahorro semanal en dólares (obligatorio)**

Una alcancía digital lleva el registro de cuánto ahorras en dólares cada semana — varias personas en Chile prefieren ahorrar en esta moneda para protegerse de la fluctuación del peso. Dado el monto ahorrado, el programa muestra el nivel que corresponde: menos de 10 dólares es *Recién empezando*; de 10 a menos de 30 es *En camino*; de 30 a menos de 60 es *Buen ahorro*; y de 60 en adelante es *¡Excelente semana!*

**Antes de programar, completa esta tabla.** El orden de las filas es el orden en que tu programa va a hacer las preguntas, así que decídelo ahora:

| Orden | Condición (en palabras) | Qué imprime |
|---|---|---|
| 1° | *(completar)* | *(completar)* |
| 2° | *(completar)* | *(completar)* |
| 3° | *(completar)* | *(completar)* |
| 4° — el caso que sobra | *(completar)* | *(completar)* |

**El programa debe:**
- Pedir el **monto ahorrado esta semana en dólares**, que puede tener decimales.
- Clasificar el monto en los **cuatro niveles**, mostrando uno solo.
- Respetar el orden que escribiste en la tabla, de modo que las cuatro franjas queden bien delimitadas: sin huecos y sin que un monto caiga en dos niveles.

<details>
<summary>💡 Pista — probar el borde</summary>
Cuando termines, prueba tu programa con 10, con 30 y con 60 exactos. Esos tres valores son los que separan un nivel del siguiente, y son justo donde una cadena mal ordenada se rompe sin avisar.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa* <pre>15</pre> | 📥 *El usuario ingresa* <pre>62.5</pre> |
| 📤 *El programa imprime* <pre>Nivel: En camino.</pre> | 📤 *El programa imprime* <pre>Nivel: ¡Excelente semana!</pre> |

- Solución:
  ```python
  monto_ahorrado_semana = float(input("Ingresa cuántos dólares ahorraste esta semana: "))

  if monto_ahorrado_semana < 10:
      print("Nivel: Recién empezando.")
  elif monto_ahorrado_semana < 30:
      print("Nivel: En camino.")
  elif monto_ahorrado_semana < 60:
      print("Nivel: Buen ahorro.")
  else:
      print("Nivel: ¡Excelente semana!")
  ```

**Criterio de logro:** Ruta A entrega una batería que efectivamente hace caer un programa mal estructurado, incluyendo los valores exactos del borde. Ruta B entrega dos programas que producen la salida correcta en los tres caminos de la micro y en las cuatro franjas del ahorro, incluidos los bordes.

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
puntaje_equipo = int(input("Puntaje del equipo: "))

if puntaje_equipo >= 18:
    mensaje_torneo = "El equipo clasifica a semifinales."
else:
    mensaje_torneo = "El equipo queda eliminado."

print("Resultado del torneo:", "El equipo clasifica a semifinales.")  # <- esta línea
```
Si alguien ingresa un puntaje de 5, ¿qué imprime este programa?
- A: `Resultado del torneo: El equipo queda eliminado.`
- B: `Resultado del torneo: El equipo clasifica a semifinales.`
- C: No imprime nada, porque la condición no se cumple.
- D: Da error, porque `mensaje_torneo` nunca se usa.

**Respuesta correcta:** B
**Justificación:** el `if` calcula bien el mensaje y lo guarda en `mensaje_torneo`, pero el `print()` no usa esa variable: imprime un texto fijo escrito a mano. El programa dice siempre lo mismo, sin importar el puntaje que se ingrese.

**Pregunta 2:**
```python
saldo_tarjeta_bip = input("Ingresa el saldo de la tarjeta bip: ")

if saldo_tarjeta_bip >= 800:
    print("Paga el pasaje con la tarjeta bip.")
else:
    print("No le alcanza el saldo para el pasaje.")
```
Si alguien ingresa 1500, ¿qué pasa?
- A: Imprime `Paga el pasaje con la tarjeta bip.`
- B: Imprime `No le alcanza el saldo para el pasaje.`
- C: El programa se detiene con un error, porque está comparando texto con un número.
- D: Imprime las dos líneas.

**Respuesta correcta:** C
**Justificación:** `input()` siempre entrega texto, aunque escribas números. Sin `int()`, Python no puede comparar el texto `"1500"` con el número `800` y el programa se cae. La forma correcta es `int(input(...))`.

**Pregunta 3:**
```python
# La app avisa dos cosas del estado de tu teléfono:
if bateria_baja == True:
    print("Queda poca batería.")

if hay_wifi_disponible == True:
    print("Hay wifi disponible.")
```
¿Por qué estas dos preguntas van con dos `if` separados y no encadenadas con `elif`?
- A: Porque `elif` solo funciona con números, no con `True` y `False`.
- B: Porque `elif` siempre necesita un `else` al final y aquí no hace falta.
- C: Porque el orden de los avisos cambiaría si se usara `elif`.
- D: Porque son independientes: pueden ser verdaderas las dos a la vez, y con `elif` el segundo aviso nunca aparecería junto al primero.

**Respuesta correcta:** D
**Justificación:** que quede poca batería no cambia si hay wifi. Son preguntas sin relación, así que cada una necesita su propio `if`. Encadenadas con `elif`, apenas se cumpliera la primera, la segunda ni siquiera se revisaría.

### Cierre (5 min)

**Objetivo de la clase:** Distinguir si dos condiciones son independientes, excluyentes o dependientes, escribir la forma de `if` que corresponde a cada caso y comprobarla en el valor del borde, con rigurosidad.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes decidiendo si dos condiciones van encadenadas con `elif` o en `if` separados?, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro".

**Pregunta 2 — Actitud proyectada al futuro:** Fuera de la programación, ¿en qué situación revisas siempre el caso del borde antes de dar algo por bueno?

---

## Decisiones de diseño relevantes

**Por qué la revisión se come el Haz Ahora.** La primera versión de esta spec abría con un escenario inventado (una corrida familiar) que compartía narrativa con la Guiada. Se descartó: en una clase de revisión, el calentamiento tiene que ser la revisión misma. Los tres programas del Haz Ahora son ítems reales de la Evaluación 2 tal como quedaron mal resueltos, y cada uno deja una pregunta abierta que responde una tarjeta del HTML. Ese es el puente entre la revisión y el contenido nuevo.

**El mapa fragmento → tarjeta que ordena la clase:**

| Programa del Haz Ahora | Ítem real | % logro | Tarjeta del HTML que lo cierra |
|---|---|---|---|
| Racha de estudio con los `elif` al revés | 1B.5 | 48% | Tarjeta 2 — Excluyentes (mismo escenario, mismos umbrales 14/7/3) |
| Torneo: `>` teniendo el puntaje justo | 1B.2 | 82% | Cierre del HTML — probar el valor del borde |
| Micro escrita como dos `if` sueltos | 2.2 | 61% | Tarjeta 3 + el par de escenas de contraste |
| *(ninguno)* | — | — | Tarjeta 1 — Independientes |

La tarjeta 1 es la única sin error asociado **porque nunca se enseñó** — verificado contra la spec de la Clase 14, donde se enseñó "solo una rama se ejecuta" y "el orden importa", pero siempre dentro de `elif`, nunca contrastado con `if` independientes. Ese es el giro de la clase y hay que decirlo textual al pasar al HTML.

**El Programa 3 muestra `if` sueltos, que es el contenido nuevo — a propósito.** Se muestra como error, sin nombrarlo ni explicarlo. El HTML es el que después revela que esa misma forma es la correcta cuando las preguntas no dependen entre sí. Es un spoiler sutil, no un adelanto explícito de sintaxis.

**Los fragmentos van como celdas ejecutables, no como código para leer.** No se pide predecir sin ejecutar. Que ejecuten es mejor: ven salir el resultado equivocado con sus propios ojos, y la pregunta que importa —*qué debería imprimir*— no se puede contestar corriendo el programa. En el Programa 2 son ellos los que mueven el número de 18 a 19, así que tocan el borde con las manos antes de que exista la palabra "borde".

**La pregunta 4 del Haz Ahora hace que los Colabs de devolución se usen.** Se entregan en la Apertura y sin esa pregunta quedarían abiertos de adorno. Va escrita y privada; levantar manos al revisar queda a criterio de Diego en el momento.

**El ICN puede durar solo 15 min** porque el Haz Ahora hace trabajo real: llegan al HTML con tres preguntas ya vividas en su propia pantalla, así que las tarjetas 2, 3 y el cierre del borde consolidan en vez de introducir.

**Andamiaje de la Ruta B: tabla de decisión, no starter code.** Se evaluaron las dos opciones. Se descartó el esqueleto con condiciones en blanco porque les regala la estructura, que es exactamente lo que fallaron: no vieron que la segunda pregunta iba dentro de la primera. La tabla de decisión los obliga a comprometerse con la estructura antes de escribir, y respeta la regla del proyecto de celda de código siempre vacía.

**La Ruta A no hace de ayudantía.** Al tramo alto la Sección 2 no le dejó nada que reforzar (97-100%), así que una clase de repaso general los desperdiciaría. Su trabajo propio —diseñar los casos límite— es genuinamente más difícil que reescribir los programas, y el cruce es simétrico: quien diseña casos necesita un programa que probar, y quien repara necesita saber si su arreglo aguanta.

**Cierre formativo, no recuperativa.** La nota está cerrada. Se dice al abrir para que la clase no se vuelva negociación de puntos.

**Convención `== True` explícito.** Toda condición sobre una variable booleana se escribe `if bateria_baja == True:`, nunca la forma idiomática de Python. Aplica al HTML, al ICN y a la Pregunta 3 del Ticket. Las comparaciones numéricas y de texto quedan tal cual. Decisión pedagógica deliberada de Diego — no corregirla.

**Actitud elegida: Rigurosidad** (por sobre Criterio, Método y Autocrítica). Calza con la herramienta transversal de la clase —probar el valor del borde— y es la que se puede volver observable en el Ticket de Salida.
