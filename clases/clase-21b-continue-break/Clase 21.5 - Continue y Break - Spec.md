# Clase 21.5 — continue y break

**Estado:** Spec aprobada — 2026-08-07
**Clase Picuino:** N° 15 — Sentencia continue + N° 16 — Sentencia break
**URL Picuino:** https://www.picuino.com/es/python-for-continue.html / https://www.picuino.com/es/python-for-break.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo hasta Clase N°21 inclusive — `for`, `range()`, `for` anidado, ya ejercitados en la Ayudantía N°21 del lunes 2026-08-10
- **Contenidos nuevos:** `continue` (saltar el resto del cuerpo de una vuelta y seguir con la próxima iteración), `break` (cortar el ciclo por completo), patrón de "bandera" (variable que guarda si algo se encontró antes de un `break`, para consultarla después del ciclo) — `for...else` queda explícitamente fuera de alcance
- **Contextos temáticos:** torneo de Free Fire con código de acceso (Haz Ahora y Guiada comparten el mismo escenario), playlist de música (Ejercicio 1), entrenamiento deportivo (Ejercicio 2), notificaciones de redes sociales (Ejercicio 3, desafío)
- **Tema breve (Form):** continue y break

## Objetivo

Construir programas con ciclos `for` que salten iteraciones con `continue` y corten búsquedas o intentos con `break`, con método.

## Propósito

El método es seguir un procedimiento ordenado, sabiendo exactamente cuándo saltar un caso y cuándo detenerte. Hoy lo practicamos con `continue`, para saltar iteraciones, y `break`, para detener una búsqueda o unos intentos a tiempo.

## OAs MINEDUC

`OA1, OA3`

- **OA1** — usar `continue` o `break` exige decidir con criterio cuándo saltar una vuelta y cuándo cortar el ciclo completo, y anticipar qué pasa con el flujo del programa después de esa decisión.
- **OA3** — se programan algoritmos de filtrado y búsqueda (filtrar canciones, encontrar el primer resultado que cumple una condición, validar intentos limitados) usando control de flujo.

## Estructura de la clase

### 1. Haz Ahora (6 min)
Un estudiante del curso organiza un torneo de Free Fire para sus compañeros. Para que no entre cualquiera a la sala de la partida, puso un código de acceso y decidió que cada persona solo puede intentar adivinarlo un número limitado de veces. Ese estudiante, que sabe programar en Python, les pide ayuda para automatizar esa verificación — pero antes, quiere que tengan clara la lógica:

1. Si alguien acierta el código al segundo intento, ¿tiene sentido seguir pidiéndole el intento 3 y el 4?
2. Según lo que decidió, ¿cuántos intentos como máximo tiene cada persona antes de quedar fuera?
3. Si alguien falla en el intento 1 y acierta en el intento 2, ¿en qué intento se detiene el proceso?
4. Si alguien agota todos sus intentos sin acertar, ¿qué debería pasar?

**Respuestas esperadas:**
1. No, debería detenerse ahí y no pedir más intentos.
2. 4 intentos.
3. En el intento 2.
4. Debería avisarle que el acceso fue denegado.

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: `continue`**
- Definición: cuando el programa encuentra `continue` dentro de un `for`, deja de ejecutar lo que sigue en esa vuelta y salta directo a la siguiente iteración — el ciclo sigue corriendo con normalidad.
- Ejemplo:
  ```python
  for numero in range(1, 11):
      if numero % 3 == 0:      # ej: si numero vale 3, 3 % 3 == 0 → se cumple, se salta
          continue
      print("Número:", numero)
  ```
- Idea clave: `continue` no termina el ciclo, solo se salta el resto de esa vuelta.

**Concepto 2: `break`**
- Definición: cuando el programa encuentra `break`, termina el ciclo de inmediato — no revisa las vueltas que faltaban — y sigue con el código que viene después del `for`.
- Ejemplo:
  ```python
  for numero in range(1, 11):
      if numero % 7 == 0:      # ej: si numero vale 7, 7 % 7 == 0 → se cumple, aquí se corta
          print("Encontré un múltiplo de 7:", numero)
          break
  ```
- Idea clave: `break` sí agrega algo que un `if` solo no puede: detener el ciclo antes de que termine su recorrido completo.

**Concepto 3: el patrón de "bandera"**
- Definición: como `break` corta el ciclo apenas se cumple algo, conviene guardar esa información en una variable (una "bandera") justo antes de romper el ciclo, para poder consultarla después y decidir qué mensaje mostrar.
- Ejemplo:
  ```python
  encontrado = False
  for numero in range(1, 11):
      if numero % 7 == 0:      # ej: si numero vale 7, 7 % 7 == 0 → se cumple, guardamos el hallazgo
          encontrado = True
          break

  if encontrado == True:       # se pregunta explícitamente por el valor de la bandera
      print("Sí hay un múltiplo de 7 en el rango")
  else:
      print("No hay ningún múltiplo de 7 en el rango")
  ```
- Idea clave: la bandera se define antes del ciclo, se actualiza justo antes del `break`, y se consulta recién después de que el ciclo completo termina.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Usar `break` cuando correspondía `continue` (o al revés) | El ciclo corta completo cuando solo se quería saltar una vuelta, o al revés no se detiene cuando debía | Preguntarse: ¿quiero saltarme solo esta vuelta, o terminar el ciclo entero? |
| Esperar que el código después de `continue` igual se ejecute en esa vuelta | Ese código nunca corre en la vuelta donde se activó `continue` | Todo lo que va después de `continue`, dentro del cuerpo del ciclo, se salta esa vuelta |
| Olvidar actualizar la bandera justo antes del `break`, o revisarla dentro del ciclo | El mensaje final queda incorrecto o se muestra antes de tiempo | Actualizar la bandera justo antes del `break` y consultarla recién después de que el ciclo completo termina |

### 3. Práctica Guiada (23 min)
Retoma el torneo de Free Fire: el estudiante que lo organiza ahora quiere que el programa reciba los intentos de una persona y avise apenas acierte, sin seguir preguntando después de eso.

**El programa debe:**
- Guardar el código secreto y el máximo de intentos.
- Pedir, intento por intento, que se ingrese un número.
- Detener la verificación apenas el intento coincida con el código, avisando en qué intento ocurrió.
- Si se agotan los intentos sin acertar, avisar que el acceso fue denegado.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>

📥 *El usuario ingresa*
<pre>
1111
4821
</pre>
📤 *El programa imprime*
<pre>
Intento 1 - código incorrecto
Intento 2 - acceso concedido
</pre>

</td>
<td>

📥 *El usuario ingresa*
<pre>
1111
2222
3333
5555
</pre>
📤 *El programa imprime*
<pre>
Intento 1 - código incorrecto
Intento 2 - código incorrecto
Intento 3 - código incorrecto
Intento 4 - código incorrecto
Acceso denegado. Se acabaron los intentos.
</pre>

</td>
</tr>
</table>

- Solución:
  ```python
  codigo_secreto = 4821
  max_intentos = 4
  acceso_concedido = False

  for intento in range(1, max_intentos + 1):
      numero_ingresado = int(input("Ingresa el código: "))
      if numero_ingresado == codigo_secreto:
          acceso_concedido = True
          print("Intento", intento, "- acceso concedido")
          break
      else:
          print("Intento", intento, "- código incorrecto")

  if acceso_concedido == False:
      print("Acceso denegado. Se acabaron los intentos.")
  ```

### 4. Práctica Independiente (18 min)

En cada ejercicio escribe tu programa dentro de la celda que ya trae el comentario `# Tu solución — Ejercicio N` — no borres esa primera línea, el verificador la usa para encontrar tu código. Tampoco necesitas usar nombres de variable en particular: el verificador revisa lo que tu programa imprime, no cómo llamaste tus variables.

**Celda de configuración:**
```python
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)

import io, re, contextlib, unicodedata
from IPython import get_ipython

def _fuente_solucion(marca):
    for fuente in reversed(get_ipython().user_ns.get("In", [])):
        if fuente.strip().startswith(marca):
            return fuente
    return None

def _normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()

def _revisar(marca, esperadas):
    fuente = _fuente_solucion(marca)
    if fuente is None:
        print("⬜ No encuentro tu solución. Ejecuta la celda de arriba sin borrar")
        print("   su primera línea:", marca)
        return
    if not [l for l in fuente.splitlines()[1:] if l.strip()]:
        print("⬜ Tu celda de solución todavía está vacía. Escribe tu programa y ejecútala.")
        return
    salida = io.StringIO()
    try:
        with contextlib.redirect_stdout(salida):
            exec(compile(fuente, "<tu solución>", "exec"), {"__name__": "__main__"})
    except Exception as error:
        print("❌ Tu programa se detuvo con un error:", type(error).__name__, "-", error)
        return
    obtenidas = [l.rstrip() for l in salida.getvalue().splitlines() if l.strip()]
    correctas, primer_error = 0, None
    for i, esperada in enumerate(esperadas):
        obtenida = obtenidas[i] if i < len(obtenidas) else ""
        if _normalizar(obtenida) == _normalizar(esperada):
            correctas += 1
        elif primer_error is None:
            primer_error = (i + 1, esperada, obtenida)
    print("Líneas correctas:", correctas, "de", len(esperadas))
    if primer_error is None and len(obtenidas) == len(esperadas):
        print("✅ ¡Perfecto! Tu programa imprime exactamente lo que se pedía.")
        return
    if len(obtenidas) > len(esperadas):
        print("⚠️ Tu programa imprimió", len(obtenidas) - len(esperadas), "línea(s) de más.")
    if primer_error:
        numero, esperada, obtenida = primer_error
        print("❌ La primera diferencia está en la línea", numero)
        print("   Se esperaba:", esperada)
        print("   Tu programa dio:", obtenida if obtenida else "(nada)")

def verificar_ejercicio_1():
    esperadas = ["Canción: " + str(numero) for numero in range(1, 26) if numero % 4 != 0]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    print("Para revisar, ingresa los mismos tiempos del Ejemplo 1: 6, 7, 9")
    esperadas = [
        "Serie 1 - 6 minutos",
        "Serie 2 - 7 minutos",
        "Serie 3 - 9 minutos",
        "Serie 3 superó la meta de 8 minutos",
    ]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    print("Para revisar, ingresa los mismos datos del Ejemplo 1: normal, silenciada, urgente")
    esperadas = [
        "Notificación 1 - normal",
        "Notificación 3 - urgente",
        "Notificación 3 es urgente. Se detiene la revisión.",
    ]
    _revisar("# Tu solución — Ejercicio 3", esperadas)
```

**Ejercicio 1 — Playlist**
Una app de música numera las canciones de una playlist del 1 al 25, según el orden en que se agregaron. Pero cada 4 canciones cae una versión instrumental que el sistema no debe mostrar en la lista de reproducción visible. Necesitas armar el listado que sí se le muestra a quien escucha.

**El programa debe:**
- Recorrer los números de canción del 1 al 25.
- Omitir del listado las canciones que sean múltiplos de 4 (las versiones instrumentales).
- Mostrar el número de cada canción que sí queda en la lista visible.

**Resultado esperado:**
📤 *El programa imprime:*
```
Canción: 1
Canción: 2
Canción: 3
Canción: 5
...
Canción: 25
```

**Celda de verificación:**
```python
verificar_ejercicio_1()
```

- Solución:
  ```python
  for numero_cancion in range(1, 26):
      if numero_cancion % 4 == 0:
          continue
      print("Canción:", numero_cancion)
  ```

**Ejercicio 2 — Entrenamiento**
Un atleta hace hasta 6 series de entrenamiento y anota cuánto duró cada una, en minutos. Si alguna serie se pasa de los 8 minutos, quieres avisar altiro y no seguir preguntando por las que faltan.

**El programa debe:**
- Pedir el tiempo de cada serie, una por una (máximo 6).
- Detenerse apenas una serie supere los 8 minutos, avisando en cuál ocurrió.
- Si ninguna se pasa, avisar que todas quedaron dentro de la meta.

<details>
<summary>💡 Pista — recuerda la bandera</summary>
Necesitas saber, después del ciclo, si alguna serie superó la meta o no. Usa una variable como la del Concepto 3: defínela antes del ciclo, actualízala justo antes del `break`, y revísala recién cuando el ciclo termine.
</details>

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>

📥 *El usuario ingresa*
<pre>
6
7
9
</pre>
📤 *El programa imprime*
<pre>
Serie 1 - 6 minutos
Serie 2 - 7 minutos
Serie 3 - 9 minutos
Serie 3 superó la meta de 8 minutos
</pre>

</td>
<td>

📥 *El usuario ingresa*
<pre>
5
6
7
6
5
7
</pre>
📤 *El programa imprime*
<pre>
Serie 1 - 5 minutos
Serie 2 - 6 minutos
Serie 3 - 7 minutos
Serie 4 - 6 minutos
Serie 5 - 5 minutos
Serie 6 - 7 minutos
El atleta se mantuvo dentro de la meta en todas las series
</pre>

</td>
</tr>
</table>

**Celda de verificación:**
```python
verificar_ejercicio_2()
```

- Solución:
  ```python
  max_series = 6
  supero_la_meta = False

  for serie in range(1, max_series + 1):
      tiempo = int(input("Tiempo de la serie " + str(serie) + ": "))
      print("Serie", serie, "-", tiempo, "minutos")
      if tiempo > 8:
          supero_la_meta = True
          print("Serie", serie, "superó la meta de 8 minutos")
          break

  if supero_la_meta == False:
      print("El atleta se mantuvo dentro de la meta en todas las series")
  ```

**Ejercicio 3 — Desafío: Notificaciones** *(opcional)*
Una app de notificaciones revisa, una por una, hasta 8 notificaciones nuevas. Las que llegan silenciadas no cuentan como revisadas y deben saltarse sin más trámite, sin gastar una revisión. Pero apenas aparece una notificación marcada como urgente, el programa debe avisar y dejar de revisar el resto.

**El programa debe:**
- Revisar hasta 8 notificaciones, pidiendo para cada una si es "silenciada", "urgente" o "normal".
- Saltar sin mostrar nada las que sean silenciadas, sin frenar la revisión del resto.
- Detener la revisión completa apenas aparezca una urgente, avisando en qué número de notificación ocurrió.
- Si se revisan las 8 sin encontrar ninguna urgente, avisar que no hubo urgencias.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>

📥 *El usuario ingresa*
<pre>
normal
silenciada
urgente
</pre>
📤 *El programa imprime*
<pre>
Notificación 1 - normal
Notificación 3 - urgente
Notificación 3 es urgente. Se detiene la revisión.
</pre>

</td>
<td>

📥 *El usuario ingresa (8 notificaciones, ninguna urgente)*
<pre>
normal
silenciada
normal
silenciada
normal
normal
silenciada
normal
</pre>
📤 *El programa imprime*
<pre>
Notificación 1 - normal
Notificación 3 - normal
Notificación 5 - normal
Notificación 6 - normal
Notificación 8 - normal
No hubo notificaciones urgentes
</pre>

</td>
</tr>
</table>

**Celda de verificación:**
```python
verificar_ejercicio_3()
```

- Solución:
  ```python
  max_notificaciones = 8
  hubo_urgente = False

  for numero in range(1, max_notificaciones + 1):
      tipo = input("Tipo de la notificación " + str(numero) + ": ")
      if tipo == "silenciada":
          continue
      print("Notificación", numero, "-", tipo)
      if tipo == "urgente":
          hubo_urgente = True
          print("Notificación", numero, "es urgente. Se detiene la revisión.")
          break

  if hubo_urgente == False:
      print("No hubo notificaciones urgentes")
  ```

### 5. Ticket de Salida (8 min)

**Pregunta 1:**
```python
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
```
¿Qué imprime este programa?
- A: 1 2 3 4 5
- B: 1 2 4 5
- C: 1 2
- D: 1 2 3 4 5, pero el 3 se imprime dos veces

**Respuesta correcta:** B
**Justificación:** `continue` salta solo el `print()` de la vuelta donde `numero` vale 3; el ciclo sigue corriendo con normalidad en las vueltas siguientes.

**Pregunta 2:**
```python
for intento in range(1, 5):
    print("Revisando intento", intento)
    if intento == 2:
        break
print("Fin del programa")
```
¿Qué imprime este programa?
- A: "Revisando intento 1", "Revisando intento 2", "Fin del programa"
- B: "Revisando intento 1", "Revisando intento 2", "Revisando intento 3", "Revisando intento 4", "Fin del programa"
- C: "Revisando intento 1", "Revisando intento 2" — el programa nunca llega a imprimir "Fin del programa"
- D: Solo "Revisando intento 1"

**Respuesta correcta:** A
**Justificación:** `break` corta el ciclo `for` apenas `intento` llega a 2, pero el `print("Fin del programa")` está fuera del ciclo, así que igual se ejecuta después.

**Pregunta 3:**
```python
encontrado = False
for numero in range(2, 10):
    if numero % 7 == 0:
        encontrado = True
        break

if encontrado == True:
    print("Se encontró un múltiplo de 7")
else:
    print("No se encontró")
```
¿Qué imprime este programa?
- A: "No se encontró"
- B: El programa lanza un error porque `encontrado` no existe fuera del ciclo
- C: "Se encontró un múltiplo de 7"
- D: Nada, porque el `if` de después del ciclo nunca se ejecuta

**Respuesta correcta:** C
**Justificación:** `range(2, 10)` incluye el 7, que es múltiplo de 7: la bandera `encontrado` pasa a `True` justo antes del `break`, y el `if` de después del ciclo sí la lee correctamente.

### Cierre (5 min)
**Objetivo de la clase:** Construir programas con ciclos `for` que salten iteraciones con `continue` y corten búsquedas o intentos con `break`, con método.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes usando `continue` y `break` dentro de un ciclo `for`? (1 = no entendí nada, 5 = puedo explicárselo a otro)

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra tarea repetitiva (fuera de la programación) te serviría saltarte los casos que no aplican, o detenerte apenas encuentras lo que buscabas?

## Decisiones de diseño relevantes

- **Resuelve el pendiente anotado el 2026-07-28**, cuando Diego dejó continue/break fuera del alcance de Clase 20 (For Anidado) por considerarlos "accesorios" frente a la lógica de anidamiento. Discusión completa y decisión de mantener la clase (en vez de absorber solo `break` dentro de la clase de `while`) en `Plan Semana 2026-08-10 - Cierre de Ciclos.md`.
- **Numeración decimal (21.5)**, mismo patrón que N°19.5, para no correr en cascada la numeración de `while` (N°22) y todo lo posterior.
- **`for...else` queda fuera de alcance**, mismo criterio que usó Clase 20 para recortar contenido — Picuino lo marca como "uso avanzado, requiere ejemplo visual". En su lugar se enseña el patrón de "bandera" (Concepto 3), que resuelve el mismo problema (saber qué pasó después del ciclo) con una herramienta ya conocida (variables booleanas).
- **Actitud "Método"** elegida por Diego entre Criterio, Método, Precisión y Perseverancia — encaja con el patrón ordenado de revisar caso por caso y saber exactamente cuándo saltar o detenerse.
- **Guiada usa el patrón de "intentos limitados"** (más rico para construir con el curso) en vez del patrón de "búsqueda que se detiene"; este segundo patrón se reserva para el Ejercicio 2 de Independiente, así ambos patrones de `break` sugeridos en la planificación quedan cubiertos sin repetirse.
- **Contexto Free Fire** (torneo con código de acceso) pedido explícitamente por Diego para Haz Ahora y Guiada, en reemplazo de la propuesta inicial (Brawl Stars).
- **Contextos del resto de la clase variados a propósito** (música, deporte, redes sociales) para no concentrar toda la Práctica Independiente en videojuegos, ya que ese contexto ya está cubierto por la Guiada.
- **Autochequeo incluido (verificador por salida), confirmado por Diego al generar el Colab (2026-08-07).** Los 3 ejercicios de Independiente llevan `verificar_ejercicio_N()`. Como el Ejercicio 2 y el Ejercicio 3 usan `input()`, cada verificador imprime primero un aviso pidiendo ingresar los mismos datos del Ejemplo 1 del enunciado — así la comparación queda determinística contra un caso de prueba fijo, en vez de intentar adivinar cualquier combinación de entradas.
- **Corrección técnica: se reemplazó el patrón `print("Etiqueta", variable, ":", resto)` por `print("Etiqueta", variable, "-", resto)` en la Guiada y en los Ejercicios 2 y 3.** Con coma antes de `":"` como argumento aparte, `print()` agrega un espacio extra antes del dos puntos (`"Intento 1 : acceso concedido"` en vez de `"Intento 1: acceso concedido"`), lo que no calzaba con el resultado esperado documentado. El guion evita el problema sin recurrir a `+`/`str()` (regla 14 del CLAUDE.md). Ajuste ejecutado sin gate de aprobación, por CLAUDE.md regla 6 (corrección técnica intermedia).
- **Corrección técnica: el Ejercicio 2 pasó de `float(input(...))` a `int(input(...))`.** Los ejemplos del enunciado siempre usan minutos enteros (6, 7, 9...); con `float()` el resultado esperado real habría sido `6.0` en vez de `6`, otro desajuste entre el código y el resultado documentado.
