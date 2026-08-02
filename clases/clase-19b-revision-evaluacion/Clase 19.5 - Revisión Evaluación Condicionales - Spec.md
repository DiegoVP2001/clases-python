# Clase 19.5 — Condicionales: independientes, excluyentes y anidadas

**Estado:** Spec aprobada — 2026-08-01
**Clase Picuino:** N/A — clase de cierre formativo (retoma N°11 *if anidadas* y N°12 *elif*, e introduce el contraste con `if` independientes)
**URL Picuino:** —

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Fecha prevista:** lunes 3 de agosto de 2026
- **Contenidos previos asumidos:** booleanos y comparaciones (Clase 8a), operadores lógicos (Clase 8b), análisis de condiciones (Clase 8c), `if`/`else` (Clase 11), `if` anidadas (Clase 13), `elif` (Clase 14), `input()` y conversión de tipos (Clase 7)
- **Contenidos nuevos:** varios `if` independientes seguidos, contrastados explícitamente con `elif` y con el anidamiento; probar el valor del borde como hábito de verificación
- **Contextos temáticos:** app de hábitos de estudio, torneo de equipos, micro Isla de Maipo–Talagante, alcancía digital en dólares
- **Tema breve (Form):** condicionales independientes

## Objetivo

Distinguir si dos condiciones son independientes, excluyentes o dependientes, escribir la forma de `if` que corresponde a cada caso y comprobarla en el valor del borde, con rigurosidad.

## Propósito

La rigurosidad es revisar justo el caso donde algo puede fallar, en vez de confiar en que salió bien porque funcionó una vez. Hoy la practicamos probando el valor exacto del borde de cada condición.

## OAs MINEDUC

`OA1, OA3 | OAd`

- **OA1** — el eje de la clase es análisis de soluciones alternativas: tres formas posibles para el mismo par de preguntas, y decidir cuál corresponde.
- **OA3** — escriben un programa completo con condicionales y lo comprueban en los valores del borde.
- **OAd** — justifican por escrito cuál de dos versiones de un mismo programa está bien y por qué, y qué dato lo demuestra.

---

## Apertura (4 min)

Bloque propio, antes del Haz Ahora. **No se entrega nada ni se menciona la evaluación** (decisión del 2026-08-02: la entrega de los Colabs de devolución quedó postergada por dos casos de sospecha de copia todavía abiertos). El encuadre es simplemente que hay una forma de escribir condicionales que no se ha visto y que explica un error que aparece harto.

Al no haber entrega, este bloque se acorta y los ~4 minutos quedan de holgura para la Práctica Independiente, que con 20 min va justa.

> Cuando los cuadernos se entreguen —en otra clase— sí conviene abrirlos ~2 minutos en silencio y **no revisar ítem por ítem en voz alta**: al tramo alto la Sección 2 no le dejó nada que corregir (97-100%), así que una corrección proyectada los desperdiciaría.

## Estructura de la clase

### 1. Haz Ahora (7 min)

> Nota de conducción: el timer del PPT cubre solo este tramo de trabajo autónomo (`⚡ Haz Ahora <<7:00>>`). La revisión en conjunto de las respuestas toma ~5 min adicionales y la conduce Diego sin reloj.

Tres programas que tienen algo mal: cada uno hace casi lo que debía, pero no del todo. Están en celdas ejecutables: se corren, no se adivinan. Debajo de cada uno está la pregunta y el espacio para responderla.

**Programa 1 — La app de hábitos de estudio**

*Lo que debía hacer:* clasificar tu racha de días seguidos estudiando en una de cuatro categorías. Con 14 días o más es *Racha de élite*; con 7 o más, *Buena constancia*; con 3 o más, *Racha en marcha*; y con menos que eso, *Recién empezando*.

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

1. Ejecuta el Programa 1. ¿Qué imprime? ¿Y qué debería imprimir con una racha de 12 días?

[[respuesta]]

**Programa 2 — El torneo de equipos**

*Lo que debía hacer:* decir si un equipo clasifica a semifinales. Clasifica cuando su puntaje **alcanza** el mínimo exigido, que en este torneo es de 18 puntos.

```python
puntaje_equipo = 18
puntaje_minimo_clasificacion = 18

if puntaje_equipo > puntaje_minimo_clasificacion:
    mensaje_torneo = "El equipo clasifica a semifinales."
else:
    mensaje_torneo = "El equipo queda eliminado."

print("Resultado del torneo:", mensaje_torneo)
```

2. Ejecuta el Programa 2. Después cambia el puntaje a 19 y ejecútalo otra vez. ¿En cuál de los dos casos el resultado quedó equivocado?

[[respuesta]]

**Programa 3 — La micro a Talagante**

*Lo que debía hacer:* decidir cómo sube una persona al micro que va de Isla de Maipo a Talagante. Si tiene pase escolar vigente, sube gratis y no hay nada más que revisar. Si no lo tiene, se mira si el saldo de su tarjeta bip alcanza los \$800 que cuesta el pasaje.

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

3. Ejecuta el Programa 3. ¿Cuántas líneas imprime? ¿Pueden ser verdaderas las dos al mismo tiempo?

[[respuesta]]

**Para cerrar**

4. De los tres programas, ¿cuál te costó más darte cuenta de qué estaba mal? ¿Qué fue lo que te hizo verlo?

[[respuesta]]

**Respuestas esperadas:**
1. Imprime `"Racha en marcha: no la cortes."`. Debería imprimir `"Buena constancia."`, porque 12 días ya pasó los 7.
2. El resultado quedó equivocado con 18: dice que queda eliminado, pero 18 es exactamente el mínimo para clasificar. Con 19 el resultado está bien.
3. Imprime dos líneas. No pueden ser verdaderas las dos: si sube gratis con su pase, la pregunta del saldo ni siquiera corresponde hacerla.
4. Registro personal, sin respuesta única. Sirve para que cada uno nombre qué le costó ver y con qué lo vio (ejecutar, cambiar un dato, leerlo de nuevo). Se comparte a viva voz solo si Diego lo pide.

### 2. Introducción al Contenido Nuevo (15 min)

Se proyecta el material ya terminado `Clase 19.5 - Revisión Evaluación Condicionales - Tres Formas.html` (los tres casos representados como ríos animados). Cada pregunta que quedó abierta en el Haz Ahora se cierra con una tarjeta del HTML.

Frase de entrada al pasar del Haz Ahora al HTML: *"dos de estas tres formas ya las conocen. La tercera no la hemos visto nunca — y es la que explica por qué el tercer programa se comportó así."*

**Concepto 1: Independientes — varios `if` seguidos**
- Definición: Cuando dos preguntas no tienen nada que ver entre sí, cada una va en su propio `if`. Python revisa todos, uno por uno, sin que el resultado de uno afecte al siguiente.
- Ejemplo:
  ```python
  bateria_baja = True
  hay_wifi_disponible = True

  if bateria_baja == True:
      print("Queda poca batería.")
  >> Queda poca batería.

  if hay_wifi_disponible == True:
      print("Hay wifi disponible.")
  >> Hay wifi disponible.
  ```
- Idea clave: Cada `if` se revisa por su cuenta. Pueden cumplirse los dos, uno solo o ninguno.

**Concepto 2: Excluyentes — `if / elif / else`, y el orden decide**
- Definición: Cuando las preguntas son distintas versiones de lo mismo y solo una puede ser la respuesta, van encadenadas con `elif`. El primer `elif` que se cumple se lleva todo y los de más abajo ni siquiera se revisan.
- Ejemplo:
  ```python
  racha_dias_estudio = 12

  if racha_dias_estudio >= 14:
      print("Categoría de tu racha:", "Racha de élite")
  elif racha_dias_estudio >= 7:
      print("Categoría de tu racha:", "Buena constancia")
  elif racha_dias_estudio >= 3:
      print("Categoría de tu racha:", "Racha en marcha")
  else:
      print("Categoría de tu racha:", "Recién empezando")
  >> Categoría de tu racha: Buena constancia
  ```
- Idea clave: La condición más exigente va primero. Si la más amplia va arriba, se lleva el agua de todas las de abajo y esas ramas nunca se alcanzan.

**Concepto 3: Una depende de la otra — `if` anidado**
- Definición: Cuando la segunda pregunta solo tiene sentido si la primera resultó de cierta manera, la segunda va escrita **dentro** de la primera.
- Ejemplo:
  ```python
  tiene_pase_escolar = "si"
  saldo_tarjeta_bip = 200

  if tiene_pase_escolar == "si":
      print("Sube gratis con su pase escolar.")
  else:
      if saldo_tarjeta_bip >= 800:
          print("Paga el pasaje con la tarjeta bip.")
      else:
          print("No le alcanza el saldo para el pasaje.")
  >> Sube gratis con su pase escolar.
  ```
- Idea clave: Son los **mismos datos** del Programa 3 del Haz Ahora, y ahora imprime una sola línea. Si escribes las dos preguntas sueltas, la segunda se hace siempre — incluso a quien ya subió con su pase.

**Concepto 4: Probar el valor del borde**
- Definición: El borde es el valor exacto donde una condición cambia de resultado. Un programa puede funcionar con todos los ejemplos que le probaste y fallar solo ahí.
- Ejemplo:
  ```python
  puntaje_equipo = 18
  puntaje_minimo_clasificacion = 18

  if puntaje_equipo >= puntaje_minimo_clasificacion:
      print("Resultado del torneo:", "El equipo clasifica a semifinales.")
  else:
      print("Resultado del torneo:", "El equipo queda eliminado.")
  >> Resultado del torneo: El equipo clasifica a semifinales.
  ```
- Idea clave: Cuando termines de escribir, prueba el valor exacto del borde. En estos programas son 14, 7, 3, 18 y 800.

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

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario ingresa</em><pre>12
si</pre></td>
  <td>📥 <em>El usuario ingresa</em><pre>0
no
4</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Categoría de tu racha: Buena constancia</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Categoría de tu racha: Recién empezando
Aviso: todavía no registras estudio de hoy.
Todavía puedes retomar la racha anterior.</pre></td>
</tr>
</table>

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

Trabajo en parejas, **los mismos dos ejercicios para todo el curso**. Antes de empezar, ejecuta la celda de configuración de abajo: deja listos los verificadores con los que van a revisar su propio trabajo, sin tener que esperar a que el profe pase por el puesto.

**Celda de configuración:**

```python
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)

import unicodedata


def _normalizar(texto):
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(letra for letra in texto if not unicodedata.combining(letra))


def _version_1(esta_inscrito, trae_autorizacion, cupos_disponibles):
    salida = []
    if esta_inscrito == "si":
        salida.append("Puedes entrar al taller.")
    else:
        if trae_autorizacion == "si":
            salida.append("Entras con autorización firmada.")
        else:
            salida.append("No puedes entrar: falta autorización.")

    if cupos_disponibles < 5:
        salida.append("Quedan pocos cupos disponibles.")
    else:
        salida.append("Todavía quedan cupos de sobra.")
    return salida


def _version_2(esta_inscrito, trae_autorizacion, cupos_disponibles):
    salida = []
    if esta_inscrito == "si":
        salida.append("Puedes entrar al taller.")

    if trae_autorizacion == "si":
        salida.append("Entras con autorización firmada.")
    else:
        salida.append("No puedes entrar: falta autorización.")

    if cupos_disponibles < 5:
        salida.append("Quedan pocos cupos disponibles.")
    else:
        salida.append("Todavía quedan cupos de sobra.")
    return salida


def comparar_versiones(esta_inscrito, trae_autorizacion, cupos_disponibles):
    salida_1 = _version_1(esta_inscrito, trae_autorizacion, cupos_disponibles)
    salida_2 = _version_2(esta_inscrito, trae_autorizacion, cupos_disponibles)
    print("Datos probados -> inscrito:", esta_inscrito,
          "| autorización:", trae_autorizacion,
          "| cupos:", cupos_disponibles)
    print()
    print("--- Versión 1 ---")
    for linea in salida_1:
        print(linea)
    print()
    print("--- Versión 2 ---")
    for linea in salida_2:
        print(linea)
    print()
    if salida_1 == salida_2:
        print("🔎 Las dos versiones imprimieron exactamente lo mismo. Prueba con otros datos.")
    else:
        print("🎯 Encontraste un caso donde las dos versiones NO se comportan igual.")
        print("   Anótalo y explica cuál de las dos está bien y por qué.")


_NIVEL_ESPERADO = {10: "En camino", 30: "Buen ahorro", 60: "Excelente semana"}


def verificar_bordes(con_10="", con_30="", con_60=""):
    entregado = {10: con_10, 30: con_30, 60: con_60}
    correctas = 0
    for monto in (10, 30, 60):
        respuesta = _normalizar(entregado[monto])
        if respuesta == "":
            print("⬜ Con", monto, "dólares todavía no escribiste qué mostró tu programa.")
        elif _normalizar(_NIVEL_ESPERADO[monto]) in respuesta:
            print("✅ Con", monto, "dólares tu programa clasifica bien.")
            correctas += 1
        else:
            print("❌ Con", monto, "dólares tu programa no clasifica como corresponde.")
            print("   Revisa el orden de tus condiciones y qué pasa justo en ese valor.")
    print()
    if correctas == 3:
        print("🎉 Los tres bordes quedaron correctos: tu cadena está bien ordenada.")
    else:
        print("Te faltan", 3 - correctas, "borde(s). El borde es justo donde una cadena mal ordenada se rompe.")
```

**Ejercicio 1 — Las dos versiones del taller de robótica (obligatorio)**

El taller de robótica del liceo tiene un sistema en la entrada que hace dos cosas a la vez: decide si la persona puede pasar y, además, avisa cómo va la disponibilidad de cupos para la próxima sesión. Dos compañeros lo programaron por separado y los dos juran que el suyo funciona. Con casi todos los datos que han probado imprimen exactamente lo mismo — pero uno de los dos está mal.

Así debía funcionar: si la persona **está inscrita** en el taller, pasa directo. Si **no está inscrita**, recién ahí se revisa si trae la **autorización firmada**. Aparte de eso, y sin importar quién sea la persona, el sistema avisa si quedan **menos de 5 cupos** para la próxima sesión.

<table>
<tr>
  <th>Versión 1</th>
  <th>Versión 2</th>
</tr>
<tr>
<td><pre>if esta_inscrito == "si":
    print("Puedes entrar al taller.")
else:
    if trae_autorizacion == "si":
        print("Entras con autorización firmada.")
    else:
        print("No puedes entrar: falta autorización.")

if cupos_disponibles &lt; 5:
    print("Quedan pocos cupos disponibles.")
else:
    print("Todavía quedan cupos de sobra.")</pre></td>
<td><pre>if esta_inscrito == "si":
    print("Puedes entrar al taller.")

if trae_autorizacion == "si":
    print("Entras con autorización firmada.")
else:
    print("No puedes entrar: falta autorización.")

if cupos_disponibles &lt; 5:
    print("Quedan pocos cupos disponibles.")
else:
    print("Todavía quedan cupos de sobra.")</pre></td>
</tr>
</table>

**El trabajo debe:**
- Encontrar **un dato con el que las dos versiones NO impriman lo mismo**. Para probar, cambia los tres valores de la celda de abajo y ejecútala las veces que necesites.
- Seguir probando hasta que el verificador diga que encontraste el caso. Ojo: hay **varios** datos que sirven, no uno solo.
- Escribir tus conclusiones en la celda de respuesta: con qué dato dejaron de comportarse igual, qué imprimió cada versión, y **cuál de las dos está bien y por qué**. Con tus palabras, no hace falta que sea largo.

<details>
<summary>💡 Pista — por dónde empezar a probar</summary>
Fíjate en el enunciado: la pregunta de la autorización solo tiene sentido para cierto tipo de persona. Prueba primero con alguien a quien esa pregunta <em>no</em> debería hacérsele, y mira si las dos versiones se la hacen igual.
</details>

**Celda de verificación:**

```python
# Cambia estos tres datos y ejecuta la celda las veces que necesites
comparar_versiones(esta_inscrito="no", trae_autorizacion="si", cupos_disponibles=8)
```

**Solución de referencia:**

Las dos versiones se comportan igual siempre que `esta_inscrito` sea `"no"`. **Difieren en cualquier caso donde la persona esté inscrita**, porque la Versión 2 le hace igual la pregunta de la autorización. Los dos casos que sirven:

| Dato | Versión 1 | Versión 2 |
|---|---|---|
| inscrito `"si"`, autorización `"no"` | `Puedes entrar al taller.` + el aviso de cupos | agrega `No puedes entrar: falta autorización.` — **se contradice consigo misma** |
| inscrito `"si"`, autorización `"si"` | `Puedes entrar al taller.` + el aviso de cupos | agrega `Entras con autorización firmada.` — redundante, dos permisos para una misma persona |

La correcta es la **Versión 1**: la pregunta de la autorización solo corresponde hacérsela a quien no está inscrito, así que va escrita **dentro** del `else` de la primera. El aviso de cupos, en cambio, sí es independiente y por eso va suelto en las dos versiones — lo que confirma que el problema no es tener varios `if` seguidos, sino tenerlos cuando las preguntas dependen una de otra. Si un estudiante solo prueba con gente no inscrita, nunca ve la diferencia: ese es el punto de la clase.

**Celda de respuesta:** markdown

**Plantilla de respuesta:**

*Con qué dato las dos versiones dejaron de comportarse igual, qué imprimió cada una, y cuál de las dos está bien y por qué:*

**Ejercicio 2 — La alcancía en dólares (obligatorio)**

Una alcancía digital lleva el registro de cuánto ahorras en dólares cada semana — varias personas en Chile prefieren ahorrar en esta moneda para protegerse de la fluctuación del peso. Además del nivel que alcanzaste, la app tiene que avisarte si esta semana compartiste la alcancía con alguien, para que no se te olvide repartir lo juntado. Ese aviso no tiene nada que ver con cuánto ahorraste: aparece igual, te haya ido bien o mal.

**El programa debe:**
- Pedir el **monto ahorrado esta semana en dólares**, que puede tener decimales.
- Pedir si esta semana **compartiste la alcancía** con alguien (se responde exactamente `"si"` o `"no"`).
- Mostrar **un solo** nivel según el monto: menos de 10 es *Recién empezando*; de 10 a menos de 30 es *En camino*; de 30 a menos de 60 es *Buen ahorro*; de 60 en adelante es *¡Excelente semana!*
- Mostrar **aparte** el recordatorio de repartir lo ahorrado cuando la alcancía fue compartida, **sin que dependa** del nivel que salió.
- Antes de darlo por listo, ejecutarlo con **10, 30 y 60 exactos** y comprobar los tres con la celda de verificación.

<details>
<summary>💡 Pista — el orden de la cadena</summary>
Las cuatro franjas se revisan en cadena, así que el orden decide todo. Escribe primero la condición más exigente y baja desde ahí; si partes por la más amplia, esa se lleva todos los casos y las de abajo nunca se alcanzan.
</details>

**Resultado esperado:**

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario ingresa</em><pre>15
no</pre></td>
  <td>📥 <em>El usuario ingresa</em><pre>60
si</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Nivel: En camino.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Nivel: ¡Excelente semana!
Recuerda repartir lo ahorrado con quien compartiste la alcancía.</pre></td>
</tr>
</table>

**Celda de verificación:**

```python
# Ejecuta tu programa con 10, con 30 y con 60, y escribe aquí el nivel que mostró cada vez
verificar_bordes(con_10="", con_30="", con_60="")
```

- Solución:
  ```python
  monto_ahorrado_semana = float(input("Ingresa cuántos dólares ahorraste esta semana: "))
  alcancia_compartida = input("¿Compartiste la alcancía esta semana? (si/no): ")

  if monto_ahorrado_semana < 10:
      print("Nivel: Recién empezando.")
  elif monto_ahorrado_semana < 30:
      print("Nivel: En camino.")
  elif monto_ahorrado_semana < 60:
      print("Nivel: Buen ahorro.")
  else:
      print("Nivel: ¡Excelente semana!")

  if alcancia_compartida == "si":
      print("Recuerda repartir lo ahorrado con quien compartiste la alcancía.")
  ```

**Criterio de logro:** en el Ejercicio 1, identificar un dato que separe a las dos versiones y justificar que la correcta es la Versión 1, porque la pregunta de la autorización solo corresponde hacérsela a quien no está inscrito. En el Ejercicio 2, un programa que entrega el nivel correcto en las cuatro franjas —incluidos los bordes 10, 30 y 60— y que muestra el recordatorio de forma independiente del nivel.

### 5. Ticket de Salida (6 min)

> Los tres contextos son deliberadamente **distintos** a los de la clase y a los de la Evaluación 2 (racha de estudio, torneo, micro a Talagante, ahorro en dólares, batería/wifi): el Ticket mide si el concepto se transfiere a una situación nueva, no si recuerdan el ejercicio.

**Pregunta 1:**
```python
espacio_libre_mb = int(input("¿Cuántos MB libres te quedan? "))

if espacio_libre_mb >= 1200:
    mensaje_instalacion = "El juego se puede instalar."
else:
    mensaje_instalacion = "Necesitas liberar espacio primero."

print("Estado:", "El juego se puede instalar.")  # <- esta línea
```
Si alguien ingresa 300, ¿qué imprime este programa?
- A: `Estado: Necesitas liberar espacio primero.`
- B: No imprime nada, porque la condición no se cumple.
- C: `Estado: El juego se puede instalar.`
- D: Da error, porque `mensaje_instalacion` nunca se usa.

**Respuesta correcta:** C
**Justificación:** el `if` calcula bien el mensaje y lo guarda en `mensaje_instalacion`, pero el `print()` no usa esa variable: imprime un texto fijo escrito a mano. El programa dice siempre lo mismo, sin importar cuánto espacio se ingrese.

**Pregunta 2:**
```python
precio_entrada = input("¿Cuánto cuesta la entrada al partido? ")

if precio_entrada <= 12000:
    print("Te alcanza para ir al partido.")
else:
    print("Esta vez te quedas fuera.")
```
Si alguien ingresa 8000, ¿qué pasa?
- A: El programa se detiene con un error, porque está comparando texto con un número.
- B: Imprime `Te alcanza para ir al partido.`
- C: Imprime `Esta vez te quedas fuera.`
- D: Imprime las dos líneas.

**Respuesta correcta:** A
**Justificación:** `input()` siempre entrega texto, aunque escribas números. Sin `int()`, Python no puede comparar el texto `"8000"` con el número `12000` y el programa se cae. La forma correcta es `int(input(...))`.

**Pregunta 3:**
```python
# El juego muestra dos avisos mientras juegas:
if vida_baja == True:
    print("¡Cuidado! Te queda poca vida.")

if amigo_conectado == True:
    print("Un amigo tuyo acaba de conectarse.")
```
¿Por qué estos dos avisos van con dos `if` separados y no encadenados con `elif`?
- A: Porque `elif` solo funciona con números, no con `True` y `False`.
- B: Porque `elif` siempre necesita un `else` al final y aquí no hace falta.
- C: Porque el orden de los avisos cambiaría si se usara `elif`.
- D: Porque son independientes: pueden ser verdaderas las dos a la vez, y con `elif` el segundo aviso nunca aparecería junto al primero.

**Respuesta correcta:** D
**Justificación:** que te quede poca vida no cambia si un amigo se conecta. Son preguntas sin relación, así que cada una necesita su propio `if`. Encadenadas con `elif`, apenas se cumpliera la primera, la segunda ni siquiera se revisaría.

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

**Se descartó la diferenciación por rutas cruzadas.** La primera versión repartía trabajo distinto según el tramo de rendimiento, con parejas cruzadas: un lado escribía los programas y el otro diseñaba los casos que los rompían. Se descartó por inviable en aula, y la razón de fondo no fue la diferenciación sino **la dependencia**: quien diseñaba casos no podía empezar a probar hasta que su pareja tuviera un programa funcionando — y esa pareja era justo el tramo que había dejado esos ejercicios en blanco. A eso se sumaba armar las parejas antes de la clase y sostener dos bloques paralelos en un mismo notebook.

**La diferenciación ahora ocurre sola, sin repartir a nadie.** Los mismos dos ejercicios para todo el curso. El Ejercicio 1 tiene techo alto sin costarle tiempo muerto a nadie: el código está dado, así que cualquiera puede empezar de inmediato, pero encontrar el dato que separa a las dos versiones es difícil de verdad — y hay varios datos que sirven, no uno solo. El Ejercicio 2 parte con la celda de código vacía para todos.

**El verificador reemplaza a la pareja.** Lo que en la versión descartada aportaba el compañero —un programa real que probar, y alguien que confirmara si el arreglo aguantaba— ahora lo entrega una celda de configuración con dos funciones. `comparar_versiones()` corre internamente ambas versiones del taller y dice si se comportaron igual o distinto; `verificar_bordes()` recibe lo que el programa del estudiante imprimió en 10, 30 y 60 y lo compara. Se autorrevisan sin esperar a que el profe pase por el puesto, y sin depender del ritmo de nadie más.

**Los contextos del Ticket son nuevos a propósito.** Espacio del celular, entrada a un partido y avisos de un videojuego — ninguno aparece en la clase ni en la Evaluación 2. El Ticket mide si el concepto se transfiere a una situación que no vieron, no si recuerdan el ejercicio con el que se enseñó. La Práctica Independiente hace lo contrario y también a propósito: el Ejercicio 2 retoma el ítem 2.3 de la prueba, porque ahí sí lo que se busca es cerrar una brecha concreta.

**Cierre formativo, no recuperativa.** La nota está cerrada. Se dice al abrir para que la clase no se vuelva negociación de puntos.

**Convención `== True` explícito.** Toda condición sobre una variable booleana se escribe `if bateria_baja == True:`, nunca la forma idiomática de Python. Aplica al HTML, al ICN y a la Pregunta 3 del Ticket. Las comparaciones numéricas y de texto quedan tal cual. Decisión pedagógica deliberada de Diego — no corregirla.

**Actitud elegida: Rigurosidad** (por sobre Criterio, Método y Autocrítica). Calza con la herramienta transversal de la clase —probar el valor del borde— y es la que se puede volver observable en el Ticket de Salida.

---

## Proyección — Haz Ahora (PPT)

> Sección que consume **solo** `generar-ppt-clase`; el Colab ignora esta parte del spec. El Haz Ahora del Colab trae los tres programas completos en celdas ejecutables, y eso no cabe en una slide — ni hace falta, porque cada estudiante lo tiene en su propia pantalla. Lo que se proyecta mientras trabajan es la consigna y la lista de lo que hay que hacer.

Abre el Colab de la clase. Vas a encontrar tres programas que tienen algo mal: ejecútalos, no los adivines. Debajo de cada uno está la pregunta y el espacio para responderla.

Responde en el Colab, debajo de cada programa:

1. Programa 1 — La app de hábitos de estudio: ¿qué imprime? ¿Y qué debería imprimir con una racha de 12 días?
2. Programa 2 — El torneo de equipos: ejecútalo, cambia el puntaje a 19 y ejecútalo otra vez. ¿En cuál de los dos casos el resultado quedó equivocado?
3. Programa 3 — La micro a Talagante: ¿cuántas líneas imprime? ¿Pueden ser verdaderas las dos al mismo tiempo?
4. ¿Cuál de los tres te costó más? ¿Qué fue lo que te hizo darte cuenta?

Cuando se acabe el tiempo las revisamos juntos.
