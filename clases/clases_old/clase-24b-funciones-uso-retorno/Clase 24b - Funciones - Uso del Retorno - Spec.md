# Clase 24b — Funciones (uso del retorno: guardar y reutilizar)

**Estado:** Spec aprobada — 2026-08-19
**Clase Picuino:** N° 19 — Definición de funciones (refuerzo/consolidación — no avanza a N°20)
**URL Picuino:** https://www.picuino.com/es/python-funciones.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo lo de Clase 24a — `def`, parámetros, argumentos, llamar la función, `return` (incl. que sin `return` la función devuelve `None`, y que `return` corta la ejecución) — además de todo lo anterior (booleanos y comparaciones, if/elif/else, for + range, for anidado, continue/break, while).
- **Contenidos nuevos:** ninguno de sintaxis. Esta clase profundiza/consolida `def` + parámetros + `return`, con foco en dos puntos de quiebre detectados en la sala: (1) el patrón general de guardar siempre el resultado de una función en una variable antes de usarlo (`variable = funcion(argumento)`), y (2) qué queda guardado cuando una función usa `print()` en vez de `return`, o no tiene `return` (aparece `None`).
- **Contextos temáticos:** función neutra/genérica de repaso de sintaxis (Haz Ahora), Feria de Emprendimiento del liceo (Guiada), biblioteca del liceo, radio escolar y torneo interno de un club (Independiente) — mezcla variada (regla 3).
- **Nota de alcance:** esta clase reemplaza el diseño anterior de "Clase 24b — valores por omisión" (Picuino N°20). Diagnóstico de Diego tras dictar Clase 24a: los estudiantes se trabaron desde el Ejercicio 1 de la Independiente incluso con un ICN ya simplificado, señal de que el modelo mental base de funciones (definir vs. llamar, parámetro vs. argumento, `return` vs. `print`, usar el valor devuelto) todavía no estaba consolidado. Se decidió sacar valores por omisión de esta sesión — se postergó sin fecha fija, a diseñar como clase nueva cuando el patrón de funciones esté realmente consolidado — y usar el jueves para reforzar el contenido base.

## Objetivo

Usar funciones con `return`, guardando siempre su resultado en una variable antes de utilizarlo en un cálculo o mensaje posterior, con método.

## Propósito

El método es seguir siempre el mismo paso, sin importar el caso, para no improvisar a mitad de camino. Hoy lo practicamos guardando siempre en una variable lo que devuelve una función, antes de usarlo.

## Estructura de la clase

### 1. Haz Ahora (6 min)

Un estudiante de otro curso, que recién está aprendiendo a programar, encontró este código y les pide ayuda para entenderlo — quiere programar algo parecido para un proyecto propio, pero antes quiere tener clara la lógica:

```python
def operacion(dato1, dato2):
    return dato1 + dato2

resultado = operacion(10, 5)
print("Resultado:", resultado)
```

1. ¿Cómo llamamos al lugar que ocupan los valores `10` y `5` dentro de la función?
2. ¿Cuál línea entrega el resultado del cálculo de vuelta, en vez de solo mostrarlo en pantalla?
3. ¿En qué variable queda guardado ese resultado?
4. Si la función tuviera `print(dato1 + dato2)` en vez de `return dato1 + dato2`, ¿qué valor quedaría guardado en `resultado`?

**Respuestas esperadas:**
1. Los parámetros (`dato1` y `dato2`).
2. `return dato1 + dato2`.
3. En `resultado`.
4. `None`.

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: `return` vs. `print()` — qué queda realmente guardado**
- Definición: `print()` solo muestra un valor en pantalla; `return` es lo único que entrega ese valor de vuelta a quien llamó la función, para que pueda guardarse y usarse después. Si una función no tiene `return`, devuelve `None` aunque haya usado `print()` por dentro.
- Ejemplo:
  ```python
  def saluda(nombre):
      print("Hola,", nombre)

  valor = saluda("Camila")
  print(valor)
  ```
  ```
  >> Hola, Camila
  >> None
  ```
- Idea clave: que una función "muestre algo en pantalla" no significa que ese algo quede disponible para usarlo después — solo `return` lo deja disponible.

**Concepto 2: el patrón general — guardar antes de usar**
- Definición: existe una regla general que ordena cualquier programa que use una función, en 4 partes: primero **definir** la función, después **consultar** los datos que necesita, luego **evaluarla** guardando su resultado en una variable (`variable = funcion(argumento)`), y recién ahí **imprimir** o usar ese resultado.
- Ejemplo:
  ```python
  # DEFINICIÓN
  def ganancia_venta(precio_venta, costo_producto):
      return precio_venta - costo_producto

  # CONSULTA
  precio_ingresado = 1200
  costo_ingresado = 700

  # EVALUACIÓN
  ganancia_helado = ganancia_venta(precio_ingresado, costo_ingresado)

  # IMPRESIÓN
  print("Ganancia de esa venta:", ganancia_helado)
  ```
- Idea clave: esta regla general —definición, consulta, evaluación, impresión— ordena cualquier programa que use una función, y evita el error de usar un resultado antes de haberlo guardado.

**Concepto 3: reutilizar el valor guardado**
- Definición: una vez guardado en una variable, ese resultado puede usarse como parte de un cálculo posterior — no se "pierde" después de imprimirse.
- Ejemplo:
  ```python
  ganancia_bebida = ganancia_venta(900, 400)
  ganancia_total = ganancia_helado + ganancia_bebida
  print("Ganancia total:", ganancia_total)
  ```
- Idea clave: encadenar cálculos usando variables guardadas es la base de programas más largos — cada resultado se convierte en el insumo del siguiente paso.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Llamar la función directo dentro de un `print()`, sin guardarla en una variable | El resultado se muestra una vez, pero no queda disponible para usarlo en un paso posterior | Guardar siempre el llamado en una variable, aunque el siguiente paso sea solo imprimirlo |
| Asumir que una función sin `return` "de todas formas entrega algo" porque usa `print()` internamente | La variable que la recibe queda en `None`, y cualquier cálculo posterior con ella falla o da un resultado sin sentido | Revisar si la función tiene `return`; si no lo tiene, agregarlo antes de intentar usar su resultado |

### 3. Práctica Guiada (24 min)

La Feria de Emprendimiento del liceo tiene puestos que venden distintos productos. Cada puesto quiere calcular la ganancia de una venta (precio de venta menos costo del producto), y después de dos ventas del día, saber si alcanzó la meta de recaudación que se fijó la Feria.

**El programa debe:**
- Definir una función que reciba el precio de venta y el costo del producto, y devuelva la ganancia de esa venta con `return`.
- Pedir precio y costo de dos ventas distintas, llamar la función para cada una y guardar cada resultado en su propia variable.
- Sumar esas dos ganancias guardadas para obtener la ganancia total del día.
- Pedir la meta de recaudación, comparar la ganancia total con la meta, y mostrar un mensaje distinto según si la alcanzó o no.

**Resultado esperado:**
```
Ganancia total: 1000
¡Meta alcanzada!
```

- Solución:
  ```python
  def ganancia_venta(precio_venta, costo_producto):
      return precio_venta - costo_producto

  precio_1 = int(input("¿Precio de venta del primer producto? "))
  costo_1 = int(input("¿Costo del primer producto? "))
  ganancia_1 = ganancia_venta(precio_1, costo_1)

  precio_2 = int(input("¿Precio de venta del segundo producto? "))
  costo_2 = int(input("¿Costo del segundo producto? "))
  ganancia_2 = ganancia_venta(precio_2, costo_2)

  ganancia_total = ganancia_1 + ganancia_2
  print("Ganancia total:", ganancia_total)

  meta_recaudacion = int(input("¿Cuál es la meta de recaudación? "))
  if ganancia_total >= meta_recaudacion:
      print("¡Meta alcanzada!")
  else:
      print("Todavía no se alcanza la meta.")
  ```

### 4. Práctica Independiente (18 min)

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
    print("Para revisar, ingresa los mismos datos del Ejemplo 1: 5, 200")
    esperadas = ["Debe pagar de multa: 500"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    print("Para revisar, ingresa los mismos datos del Ejemplo 1: 4, 3, 60")
    esperadas = ["Bloques necesarios: 5"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    print("Para revisar, ingresa los mismos datos del Ejemplo 1: 4, 0")
    esperadas = ["Puntaje final: 55"]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

def verificar_ejercicio_4():
    print('Para revisar, ingresa: 1200, 700, 900, 400, listo (mismo orden del enunciado)')
    esperadas = [
        "Ganancia de esa venta: 500",
        "Ganancia de esa venta: 500",
        "Ganancia acumulada del día: 1000",
    ]
    _revisar("# Tu solución — Ejercicio 4", esperadas)
```

**Ejercicio 1 — Biblioteca del liceo**

La biblioteca del liceo cobra una multa por cada día de atraso en la devolución de un libro. A quienes se atrasan por primera vez, la encargada les hace un descuento fijo de \$500 sobre la multa calculada, para no desanimarlos de seguir pidiendo libros — nunca menos de \$0.

**El programa debe:**
- Definir una función que reciba los días de atraso y el valor de la multa por día, y devuelva el monto total de la multa con `return`.
- Pedir los días de atraso y el valor por día, llamar la función y guardar el resultado en una variable.
- Restarle a ese resultado guardado el descuento de \$500 (sin bajar de \$0) y mostrar el monto final a pagar.

<details>
<summary>💡 Pista — Multa nunca bajo cero</summary>
Si al restar el descuento el monto queda negativo, usa 0 como monto final a pagar.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`5`<br>`200` | 📥 *El usuario ingresa:*<br>`1`<br>`200` |
| 📤 *El programa imprime:*<br>`Debe pagar de multa: 500` | 📤 *El programa imprime:*<br>`Debe pagar de multa: 0` |

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 1 — cuando te pida los datos, ingresa 5 y 200 (Ejemplo 1)
verificar_ejercicio_1()
```

- Solución:
  ```python
  def calcula_multa(dias_atraso, valor_por_dia):
      return dias_atraso * valor_por_dia

  dias = int(input("¿Cuántos días de atraso tiene el libro? "))
  valor_dia = int(input("¿Cuál es el valor de la multa por día? "))
  multa = calcula_multa(dias, valor_dia)

  multa_final = multa - 500
  if multa_final < 0:
      multa_final = 0
  print("Debe pagar de multa:", multa_final)
  ```

**Ejercicio 2 — Radio escolar**

La radio escolar arma bloques de canciones para el recreo. Cada bloque dura una cantidad de minutos según cuántas canciones tenga y el promedio de duración de cada una. Quieren saber cuántos bloques iguales necesitan para llegar a la meta de minutos de transmisión del día.

**El programa debe:**
- Definir una función que reciba la cantidad de canciones y la duración promedio por canción, y devuelva la duración total del bloque con `return`.
- Pedir esos dos datos, llamar la función y guardar el resultado.
- Pedir la meta de minutos del día y usar el resultado guardado para calcular cuántos bloques iguales se necesitan (división entera) para alcanzarla, mostrando ese número.

<details>
<summary>💡 Pista — División entera</summary>
Usa `//` para calcular cuántos bloques completos se necesitan.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`4`<br>`3`<br>`60` | 📥 *El usuario ingresa:*<br>`5`<br>`2`<br>`40` |
| 📤 *El programa imprime:*<br>`Bloques necesarios: 5` | 📤 *El programa imprime:*<br>`Bloques necesarios: 4` |

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 2 — cuando te pida los datos, ingresa 4, 3 y 60 (Ejemplo 1)
verificar_ejercicio_2()
```

- Solución:
  ```python
  def duracion_bloque(cantidad_canciones, duracion_promedio):
      return cantidad_canciones * duracion_promedio

  canciones = int(input("¿Cuántas canciones tiene el bloque? "))
  duracion = int(input("¿Cuál es la duración promedio de cada canción? "))
  minutos_bloque = duracion_bloque(canciones, duracion)

  meta_minutos = int(input("¿Cuál es la meta de minutos del día? "))
  print("Bloques necesarios:", meta_minutos // minutos_bloque)
  ```

**Ejercicio 3 — Torneo interno del club de ajedrez**

El club de ajedrez del liceo organiza un torneo interno y quiere calcular el puntaje final de cada jugador: puntos por partidas ganadas, más un bono si terminó invicto (sin perder ninguna).

**El programa debe:**
- Definir una función que reciba las partidas ganadas y devuelva el puntaje base con `return` (cada partida ganada vale 10 puntos).
- Pedir las partidas ganadas y las partidas perdidas, llamar la función y guardar el puntaje base.
- Si las partidas perdidas son 0, sumarle al puntaje guardado un bono de 15 puntos por terminar invicto; si no, dejarlo igual.
- Mostrar el puntaje final del jugador.

<details>
<summary>💡 Pista — El bono se suma al valor ya guardado</summary>
No vuelvas a llamar la función para agregar el bono — súmalo directo a la variable donde ya guardaste el puntaje base.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`4`<br>`0` | 📥 *El usuario ingresa:*<br>`3`<br>`1` |
| 📤 *El programa imprime:*<br>`Puntaje final: 55` | 📤 *El programa imprime:*<br>`Puntaje final: 30` |

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 3 — cuando te pida los datos, ingresa 4 y 0 (Ejemplo 1)
verificar_ejercicio_3()
```

- Solución:
  ```python
  def puntaje_base(partidas_ganadas):
      return partidas_ganadas * 10

  ganadas = int(input("¿Cuántas partidas ganó?"))
  perdidas = int(input("¿Cuántas partidas perdió?"))
  puntaje = puntaje_base(ganadas)

  if perdidas == 0:
      puntaje = puntaje + 15

  print("Puntaje final:", puntaje)
  ```

**Ejercicio 4 — Desafío: Feria de Emprendimiento (todas las ventas del día)** *(opcional)*

El mismo puesto de la Feria de Emprendimiento de la Práctica Guiada ahora quiere repetir el cálculo de ganancia para todas las ventas del día, sin cerrar el programa entre una venta y otra, y saber la ganancia acumulada al final.

**El programa debe:**
- Reutilizar la misma función de ganancia de una venta (precio de venta menos costo del producto).
- Repetir el cálculo para distintas ventas hasta que se escriba `"listo"` en vez de un precio.
- Ir acumulando la ganancia de cada venta guardada en una variable de total, y mostrarla al terminar.

**Resultado esperado:**
```
¿Precio de venta? (o "listo" para terminar) 1200
¿Costo del producto? 700
Ganancia de esa venta: 500
¿Precio de venta? (o "listo" para terminar) 900
¿Costo del producto? 400
Ganancia de esa venta: 500
¿Precio de venta? (o "listo" para terminar) listo
Ganancia acumulada del día: 1000
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 4 — ingresa 1200, 700, 900, 400 y luego listo (mismo orden del enunciado)
verificar_ejercicio_4()
```

- Solución:
  ```python
  def ganancia_venta(precio_venta, costo_producto):
      return precio_venta - costo_producto

  precio_ingresado = input('¿Precio de venta? (o "listo" para terminar) ')
  ganancia_acumulada = 0

  while precio_ingresado != "listo":
      precio = int(precio_ingresado)
      costo = int(input("¿Costo del producto? "))
      ganancia = ganancia_venta(precio, costo)
      print("Ganancia de esa venta:", ganancia)
      ganancia_acumulada = ganancia_acumulada + ganancia
      precio_ingresado = input('¿Precio de venta? (o "listo" para terminar) ')

  print("Ganancia acumulada del día:", ganancia_acumulada)
  ```

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
def cuadrado(numero):
    print(numero * numero)

resultado = cuadrado(4)
print(resultado)
```
¿Qué imprime este programa en total?
- A: 16 y 16
- B: 16 y None
- C: None y 16
- D: Error, no se puede guardar el resultado de una función sin `return`

**Respuesta correcta:** B
**Justificación:** `cuadrado` imprime 16 por dentro con `print()`, pero no tiene `return`, así que `resultado` guarda `None` — y el segundo `print()` imprime ese `None`.

**Pregunta 2:**
```python
def bono_puntos(puntos):
    return puntos + 5

puntaje_ronda1 = bono_puntos(10)
puntaje_ronda2 = bono_puntos(20)
total = puntaje_ronda1 + puntaje_ronda2
print("Total:", total)
```
¿Qué imprime este programa?
- A: Total: 40
- B: Total: 15
- C: Total: 25
- D: Total: 30

**Respuesta correcta:** A
**Justificación:** `bono_puntos(10)` guarda 15 y `bono_puntos(20)` guarda 25 en variables distintas; al sumarlas, `total` = 15 + 25 = 40.

**Pregunta 3:**
```python
def ganancia(precio, costo):
    return precio - costo

ganancia(1000, 600)
print(ganancia_1)
```
¿Qué ocurre al ejecutar este programa?
- A: Imprime 400
- B: Imprime `None`
- C: Error, porque `ganancia_1` nunca se definió
- D: Imprime el mismo valor que devolvió la función, sin nombre de variable

**Respuesta correcta:** C
**Justificación:** la función se llamó sin guardar el resultado en ninguna variable — `ganancia_1` nunca se creó, así que `print(ganancia_1)` lanza `NameError`. Este es justamente el error que el patrón "guardar antes de usar" evita.

### Cierre (5 min)

**Objetivo de la clase:** Usar funciones con `return`, guardando siempre su resultado en una variable antes de utilizarlo en un cálculo o mensaje posterior, con método.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan claro te quedó por qué siempre hay que guardar el resultado de una función en una variable antes de usarlo?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación —dentro o fuera de la programación— seguir siempre el mismo paso, sin saltártelo, evita errores más adelante?

## Decisiones de diseño relevantes

- **Reemplaza el diseño anterior de esta misma clase (Picuino N°20, valores por omisión).** Diagnóstico del 2026-08-19: tras dictar Clase 24a, los estudiantes se trabaron desde el Ejercicio 1 de la Independiente incluso con el ICN simplificado que Diego probó en vivo (patrón DEFINICIÓN/CONSULTA/EVALUACIÓN/IMPRESIÓN). Quienes avanzaron al Ejercicio 2 tampoco lograron destrabarse solos. Se concluyó que el problema no era valores por omisión en sí, sino que el modelo mental base de funciones (definir vs. llamar, parámetro vs. argumento, `return` vs. `print`, usar el valor devuelto) todavía no estaba consolidado. Valores por omisión queda postergado sin fecha fija.
- **Foco elegido por Diego:** consolidar el patrón `variable = funcion(argumento)` antes de usar el resultado, y anclar temprano el caso `None` (función sin `return`, o con `print()` en su lugar) — dos puntos de quiebre reales observados en la sala.
- **Haz Ahora sin conexión narrativa con la Guiada (desviación intencional de la regla "mismo escenario", vigente desde Clase 20).** A pedido explícito de Diego, el Haz Ahora usa una función neutra/genérica (`operacion(dato1, dato2)`) para repasar sintaxis ya vista (parámetro/argumento, `return`, guardar en variable, caso `None`) mediante código real, no narrativa disfrazada — justificado porque este contenido ya se enseñó en Clase 24a, así que no hay nada que "espoilear". El escenario real (Feria de Emprendimiento) se reserva íntegro para la Guiada.
- **La Guiada programa la función desde cero, en vivo, sin copiar nada del Haz Ahora.** Ajuste pedido por Diego: que la Guiada reitere el proceso completo (`def` + parámetros + `return` + llamar + guardar + reutilizar), no que reutilice una función ya dada. La función de la Feria (`ganancia_venta`) se define por primera vez en la Guiada; el llamado se repite dos veces sobre datos nuevos (reitera la sintaxis sin ser copia) y la suma + comparación con la meta es lógica que el Haz Ahora nunca mostró.
- **Los 4 ejercicios de la Independiente comparten el mismo patrón obligatorio** (guardar en variable → reutilizar en un cálculo posterior), en contextos distintos: biblioteca (Ej. 1, resta un descuento), radio escolar (Ej. 2, usa el valor guardado en una división), club de ajedrez (Ej. 3, combina el valor guardado con un condicional), Feria de Emprendimiento extendida a ciclo con acumulador (Ej. 4, desafío).
- **Pistas desplegables ahora default siempre (no solo "donde aplica"), decisión tomada en esta misma sesión** — ver regla 15.3 del `CLAUDE.md` raíz, actualizada el 2026-08-19. Cada ejercicio de esta Independiente lleva al menos una.
- **Actitud elegida: Método** — conecta directo con la idea de seguir siempre el mismo paso (guardar antes de usar) sin importar el caso particular, en vez de decidir caso a caso si conviene guardar el resultado.
- **Concepto 2 destaca el patrón en 4 etiquetas — DEFINICIÓN / CONSULTA / EVALUACIÓN / IMPRESIÓN — que Diego ya venía usando en vivo para simplificar el procedimiento.** Se incorporó como comentarios explícitos en el código del ejemplo, mapeados a la función de la Feria, para que el "mismo orden siempre" (actitud Método) tenga una forma visual concreta y reconocible de la clase anterior. Se usan valores fijos en vez de `input()` real en este ejemplo del ICN (a diferencia de la Guiada/Independiente) para mantener la celda simple y ejecutable de una sola pasada.
- **Ticket de Salida diseñado para cubrir ambos puntos de quiebre diagnosticados:** Pregunta 1 (caso `None`), Pregunta 2 (guardar y reutilizar dos resultados distintos), Pregunta 3 (el error real de no guardar en variable — `NameError` al intentar usar un nombre que nunca se creó).
