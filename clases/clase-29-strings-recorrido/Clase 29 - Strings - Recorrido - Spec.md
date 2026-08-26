# Clase 29 — Strings: recorriendo texto con for

**Estado:** Spec aprobada — 2026-08-26
**Clase Picuino:** N° 22 — Índices de cadenas de texto (recorrido, separado de N°28 — ver "Decisiones de diseño relevantes")
**URL Picuino:** https://www.picuino.com/es/python-textos-indices.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual (no se menciona en el notebook — ver regla del CLAUDE.md)
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo hasta N°28 inclusive (Ciclos completo: `for`, `range()`, `for` anidado, `continue`/`break`, `while`; Funciones N°24a/24b; Strings — indexing y slicing con acceso por índice positivo/negativo y rebanadas, N°28)
- **Contenidos nuevos:** recorrido de una cadena de texto con `for` directo (`for caracter in texto`), recorrido con índice combinando `range(len(texto))` y `texto[i]`, y combinación de recorrido con rebanada para generar ventanas móviles de texto
- **Contextos temáticos:** estacionamiento con cámara lectora de patentes en la barrera de entrada y pantalla angosta en la barrera de salida (continuación literal del escenario de patentes de la Clase 28 — mismo escenario en Haz Ahora, ICN y Guiada); pantalla del estacionamiento del mall (Guiada), app de transporte compartido (Ejercicio 2), cámara que confunde "O" con "0" (Ejercicio 3), patente capicúa (Ejercicio 4)
- **Tema breve (Form):** strings recorrido con for

## Objetivo

Construir programas que recorran cadenas de texto con `for` —directo o por índice— y los combinen con rebanadas para generar progresiones y ventanas de texto, con constancia.

## Propósito

La constancia es repetir el mismo paso, vuelta tras vuelta, sin saltarte ninguno. Hoy la practicamos recorriendo un texto carácter por carácter con `for`.

## OAs MINEDUC

`OA2, OA3`

## Estructura de la clase

### 1. Haz Ahora (6 min)
La cámara de la barrera del estacionamiento escanea la patente `BRTZ21` leyendo un carácter a la vez, de izquierda a derecha. El guardia, sabiendo que ya saben programar, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:

1. ¿Cuál es el primer carácter que lee la cámara?
2. ¿Cuántas veces tiene que "mirar" la cámara para terminar de leer toda la patente?
3. Si la cámara falla justo al leer el 3er carácter que escanea, ¿qué carácter de la patente es ese?
4. La pantalla angosta de la barrera de salida solo alcanza a mostrar 4 caracteres a la vez de la patente completa. ¿Qué 4 caracteres muestra en la primera imagen, contando desde el inicio?
5. Cuando la pantalla se desliza una posición y deja de mostrar la "B", ¿qué carácter nuevo aparece al final?

**Respuestas esperadas:**
1. "B".
2. 6 veces.
3. "T".
4. "BRTZ".
5. "2".

### 2. Introducción al Contenido Nuevo (18 min)

Contexto de ejemplos: patente de auto del estacionamiento — mismo escenario del Haz Ahora, para que el "aha" sea inmediato.

**Concepto 1: Recorrido directo, carácter por carácter**
- Definición: un `for` puede recorrer una cadena de texto directamente, entregando en cada vuelta un carácter distinto, en el mismo orden en que aparecen en el texto. Sirve cuando solo necesitas el carácter en sí, no en qué posición está.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  for caracter in patente:
      print(caracter)
  # >> B
  # >> R
  # >> T
  # >> Z
  # >> 2
  # >> 1
  ```
- Idea clave: cuando solo necesitas el carácter y no su posición, `for caracter in texto` alcanza.

**Concepto 2: Recorrido con índice**
- Definición: combinando `range(len(texto))` con el acceso por índice ya conocido, un `for` puede recorrer una cadena entregando en cada vuelta la posición (`i`) en vez del carácter — y desde ahí acceder al carácter con `texto[i]` cuando se necesite. Es la misma sintaxis `for`+`range()` ya usada con números, solo que ahora sirve para movernos posición por posición dentro de un texto.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  for i in range(len(patente)):
      print("Posición", i, "->", patente[i])
  # >> Posición 0 -> B
  # >> Posición 1 -> R
  # >> Posición 2 -> T
  # >> Posición 3 -> Z
  # >> Posición 4 -> 2
  # >> Posición 5 -> 1
  ```
- Idea clave: `range(len(texto))` genera exactamente las posiciones válidas del texto, y `texto[i]` entrega el carácter que está ahí.

**Concepto 3: Combinar recorrido + rebanada (ventana móvil)**
- Definición: dentro de un `for` con índice, en vez de pedir un solo carácter (`texto[i]`) se puede pedir una rebanada que empiece en `i` (`texto[i:i+ancho]`). Cada vuelta del ciclo desplaza esa "ventana" una posición, mostrando siempre la misma cantidad de caracteres consecutivos.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  ancho = 4
  for i in range(len(patente) - ancho + 1):
      print(patente[i:i+ancho])
  # >> BRTZ
  # >> RTZ2
  # >> TZ21
  ```
- Idea clave: el rango no llega hasta `len(texto)` — hay que restarle el ancho de la ventana y sumarle 1, para que la última ventana no se salga del texto.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Usar `for caracter in patente` cuando se necesita reportar la posición de un carácter | No hay forma de saber en qué posición quedó ese carácter | Usar `for i in range(len(patente))` y trabajar con `patente[i]` |
| Olvidar el `+1` (o restar mal el ancho) al calcular el rango de la ventana móvil | La última ventana queda corta, o el ciclo se detiene una vuelta antes de lo esperado | Probar con un caso chico a mano: `range(len(texto) - ancho + 1)` debe generar exactamente `largo - ancho + 1` ventanas |
| Confundir `patente[i]` (un carácter) con `patente[i:i+n]` (un trozo de varios caracteres) | El programa imprime un solo carácter donde se esperaba un trozo, o al revés | Revisar si el corchete tiene un solo índice o dos separados por `:` |

### 3. Práctica Guiada (22 min)
El estacionamiento del mall tiene una pantalla aún más angosta en su barrera de salida, que solo muestra 3 caracteres a la vez. Antes de instalarla, el encargado quiere probar cómo se vería la patente `"FGHT58"` recorriendo esa pantalla.

**El programa debe:**
- Guardar la patente en una variable
- Calcular cuántas "fotos" de 3 caracteres se necesitan para recorrer toda la patente
- Mostrar cada foto, una por línea, deslizándose de a una posición hacia la derecha

**Resultado esperado:**
```
FGH
GHT
HT5
T58
```

- Solución:
  ```python
  patente = "FGHT58"
  ancho = 3
  cantidad_fotos = len(patente) - ancho + 1

  for i in range(cantidad_fotos):
      print(patente[i:i+ancho])
  ```

### 4. Práctica Independiente (17 min)

Resuelve los siguientes ejercicios. Si te traban, pregunta al profe.

- Antes de empezar, ejecuta la celda de configuración de abajo: deja listos los verificadores para que revises tu propio trabajo sin esperar a que el profe pase por el puesto.
- No necesitas usar nombres de variable específicos: el verificador revisa lo que tu programa imprime, no cómo llamaste tus variables.
- Después de cada ejercicio, ejecuta su celda de revisión: vuelve a correr tu programa y lo compara, línea por línea, con el resultado esperado.
- Ojo: no borres el comentario de la primera línea de cada celda de solución — es lo que usa el verificador para encontrar tu código.

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

def verificar_ejercicio_0a():
    esperadas = ["Carácter: J", "Carácter: K", "Carácter: L", "Carácter: M", "Carácter: 5", "Carácter: 2"]
    _revisar("# Tu solución — Ejercicio 0a", esperadas)

def verificar_ejercicio_0b():
    esperadas = ["Posición 0 -> N", "Posición 1 -> P", "Posición 2 -> Q", "Posición 3 -> R", "Posición 4 -> 8", "Posición 5 -> 4"]
    _revisar("# Tu solución — Ejercicio 0b", esperadas)

def verificar_ejercicio_1():
    esperadas = ["Cargando: D", "Cargando: DF", "Cargando: DFR", "Cargando: DFRT", "Cargando: DFRT3", "Cargando: DFRT39"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    esperadas = ["Revelando: 8", "Revelando: 68", "Revelando: P68", "Revelando: QP68", "Revelando: NQP68", "Revelando: MNQP68"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    esperadas = ["Posición con posible O: 1", "Posición con posible O: 3"]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

def verificar_ejercicio_4():
    esperadas = ["¿Es una patente capicúa? True"]
    _revisar("# Tu solución — Ejercicio 4", esperadas)
```

**Ejercicio 0a — Práctica directa: deletrear sin índice**
Aplica el recorrido directo sobre el siguiente texto guardado.

**El programa debe:**
- Guardar el texto `"JKLM52"` en una variable
- Recorrerlo con `for` sin usar índice
- Imprimir cada carácter en su propia línea, con una etiqueta clara

**Resultado esperado:**
```
Carácter: J
Carácter: K
Carácter: L
Carácter: M
Carácter: 5
Carácter: 2
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 0a — puedes correrlo las veces que quieras
verificar_ejercicio_0a()
```

- Solución:
  ```python
  patente = "JKLM52"
  for caracter in patente:
      print("Carácter:", caracter)
  ```

**Ejercicio 0b — Práctica directa: deletrear con índice**
Ahora aplica el recorrido con índice sobre el mismo tipo de texto.

**El programa debe:**
- Guardar el texto `"NPQR84"` en una variable
- Recorrerlo con `for` usando `range(len(...))`
- Imprimir cada posición junto a su carácter, con una etiqueta clara

**Resultado esperado:**
```
Posición 0 -> N
Posición 1 -> P
Posición 2 -> Q
Posición 3 -> R
Posición 4 -> 8
Posición 5 -> 4
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 0b — puedes correrlo las veces que quieras
verificar_ejercicio_0b()
```

- Solución:
  ```python
  patente = "NPQR84"
  for i in range(len(patente)):
      print("Posición", i, "->", patente[i])
  ```

**Ejercicio 1 — Pantalla de la barrera cargando**
Mientras la cámara del estacionamiento termina de escanear una patente, la pantalla del sistema muestra la patente apareciendo progresivamente de izquierda a derecha —un efecto "cargando"— agregando un carácter más en cada línea, hasta mostrarla completa. La patente de esta vez es `"DFRT39"`.

**El programa debe:**
- Guardar la patente en una variable
- Recorrerla con índice
- En cada vuelta, mostrar el trozo de patente "cargado hasta ahora" (siempre desde el inicio), agregando un carácter más que en la vuelta anterior

<details>
<summary>💡 Pista — la rebanada siempre parte en el inicio</summary>
Lo que cambia en cada vuelta no es el inicio de la rebanada, sino dónde termina: usa el índice del ciclo para extender el final un carácter más cada vez.
</details>

**Resultado esperado:**
```
Cargando: D
Cargando: DF
Cargando: DFR
Cargando: DFRT
Cargando: DFRT3
Cargando: DFRT39
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 1 — puedes correrlo las veces que quieras
verificar_ejercicio_1()
```

- Solución:
  ```python
  patente = "DFRT39"
  for i in range(len(patente)):
      print("Cargando:", patente[0:i+1])
  ```

**Ejercicio 2 — App de transporte compartido**
La app de un servicio de transporte compartido muestra la patente del vehículo asignado revelándose de derecha a izquierda —agregando un carácter más a la izquierda en cada línea—, porque recomienda verificar primero los últimos caracteres. La patente asignada es `"MNQP68"`.

**El programa debe:**
- Guardar la patente en una variable
- Recorrerla con índice
- En cada vuelta, mostrar el trozo de patente que llega "hasta el final", partiendo cada vez una posición más a la izquierda

<details>
<summary>💡 Pista — esta vez el final es fijo</summary>
Al revés que en el Ejercicio 1: ahora es el inicio de la rebanada el que se acerca al comienzo del texto en cada vuelta, mientras el final de la rebanada siempre llega hasta el final de la patente.
</details>

**Resultado esperado:**
```
Revelando: 8
Revelando: 68
Revelando: P68
Revelando: QP68
Revelando: NQP68
Revelando: MNQP68
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 2 — puedes correrlo las veces que quieras
verificar_ejercicio_2()
```

- Solución:
  ```python
  patente = "MNQP68"
  largo = len(patente)
  for i in range(largo):
      print("Revelando:", patente[largo - 1 - i:])
  ```

**Ejercicio 3 — Carácter dudoso**
La cámara del estacionamiento a veces confunde la letra "O" con el número "0". Para la patente `"ROTOR25"`, el guardia necesita saber en qué posición (o posiciones) aparece la letra "O", para revisarlas a mano antes de guardar el registro.

**El programa debe:**
- Guardar la patente en una variable
- Recorrerla con índice
- Cada vez que el carácter en esa posición sea la letra "O", imprimir esa posición con una etiqueta clara

<details>
<summary>💡 Pista — necesitas la posición, no solo el carácter</summary>
Como el programa debe reportar en qué posición aparece la letra, recórrela con índice (`for i in range(len(patente))`) — un recorrido directo con `for caracter in patente` no te entrega esa posición.
</details>

<details>
<summary>💡 Pista — compara antes de imprimir</summary>
Dentro del ciclo, compara el carácter que está en esa posición con la letra `"O"` — solo cuando coincidan, imprime esa posición.
</details>

**Resultado esperado:**
```
Posición con posible O: 1
Posición con posible O: 3
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 3 — puedes correrlo las veces que quieras
verificar_ejercicio_3()
```

- Solución:
  ```python
  patente = "ROTOR25"
  for i in range(len(patente)):
      if patente[i] == "O":
          print("Posición con posible O:", i)
  ```

**Ejercicio 4 — Desafío: patente capicúa**
Algunos conductores creen que una patente "capicúa" (se lee igual al derecho y al revés) trae buena suerte. El sistema del estacionamiento debe comprobarlo con un ciclo con índice que compare cada carácter con su posición simétrica desde el final — sin importar cuántos caracteres tenga la patente. La patente a revisar es `"AB22BA"`.

**El programa debe:**
- Guardar la patente en una variable
- Recorrer con índice solo la primera mitad del texto
- En cada vuelta, comparar el carácter de esa posición con el de su posición simétrica desde el final
- Guardar si la patente es capicúa según si todas esas comparaciones coincidieron, e imprimirlo con una etiqueta clara

<details>
<summary>💡 Pista — la posición simétrica</summary>
La posición `i` se compara con la posición `largo - 1 - i`: cuando `i` es 0 compara el primer carácter con el último, cuando `i` es 1 compara el segundo con el penúltimo, y así sigue.
</details>

<details>
<summary>💡 Pista — no necesitas llegar hasta el final</summary>
Basta recorrer hasta la mitad del texto (`largo // 2`) — después de ese punto ya estarías repitiendo las mismas comparaciones al revés.
</details>

**Resultado esperado:**
```
¿Es una patente capicúa? True
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 4 — puedes correrlo las veces que quieras
verificar_ejercicio_4()
```

- Solución:
  ```python
  patente = "AB22BA"
  largo = len(patente)
  es_capicua = True

  for i in range(largo // 2):
      if patente[i] != patente[largo - 1 - i]:
          es_capicua = False

  print("¿Es una patente capicúa?", es_capicua)
  ```

### 5. Ticket de Salida (6 min)
**Pregunta 1:**
```python
patente = "AB12"
for c in patente:
    print(c)
```
¿Qué imprime este programa?
- A: Cada carácter en su propia línea, en el mismo orden: `A`, `B`, `1`, `2`
- B: `A B 1 2`, todo en una sola línea
- C: `AB12` una sola vez, sin separar caracteres
- D: Cada carácter en su propia línea, pero en orden invertido: `2`, `1`, `B`, `A`

**Respuesta correcta:** A
**Justificación:** `for c in patente` recorre cada carácter en el orden en que aparece en el texto, y cada `print(c)` genera su propia línea — nunca junta todo en una sola línea ni invierte el orden.

**Pregunta 2:**
```python
patente = "XY45"
for i in range(len(patente)):
    print(i, patente[i])
```
¿Qué imprime este programa?
- A: Empieza en 1 en vez de 0: `1 X`, `2 Y`, `3 4`, `4 5`
- B: `0 X`, `1 Y`, `2 4`, `3 5`
- C: Invierte el orden de los argumentos de `print`: `X 0`, `Y 1`, `4 2`, `5 3`
- D: Solo imprime la última vuelta: `3 5`

**Respuesta correcta:** B
**Justificación:** `range(len(patente))` genera las posiciones 0, 1, 2 y 3 (el texto tiene 4 caracteres), y `print(i, patente[i])` imprime primero la posición y luego el carácter en esa posición, una línea por cada vuelta del ciclo.

**Pregunta 3:**
```python
patente = "KLMN73"
ancho = 4
for i in range(len(patente) - ancho + 1):
    print(patente[i:i+ancho])
```
¿Qué imprime este programa?
- A: El ciclo se detiene una vuelta antes de lo esperado: `KLMN`, `LMN7`
- B: El programa no se ejecuta ninguna vez, porque `range(...)` queda vacío
- C: `KLMN`, `LMN7`, `MN73`
- D: El ciclo sigue de más, con trozos cada vez más cortos: `KLMN`, `LMN7`, `MN73`, `N73`, `73`, `3`

**Respuesta correcta:** C
**Justificación:** `range(len(patente) - ancho + 1)` genera exactamente 3 posiciones de inicio (0, 1 y 2) — la cantidad justa de ventanas de 4 caracteres que caben en un texto de 6. Sin el `+1` el ciclo se detendría una vuelta antes (alternativa A); usando `range(len(patente))` sin restar el ancho seguiría de más, generando trozos cada vez más cortos hasta salirse del rango (alternativa D).

### Cierre (5 min)
**Objetivo de la clase:** Construir programas que recorran cadenas de texto con `for` —directo o por índice— y los combinen con rebanadas para generar progresiones y ventanas de texto, con constancia.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes recorriendo un texto con `for` (directo o con índice) y combinándolo con rebanadas? (1 = no entendí nada, 5 = puedo explicárselo a otro)

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación real hay que repetir el mismo paso, uno por uno, sin saltarse ninguno — igual que hoy recorriendo un texto carácter por carácter?

## Decisiones de diseño relevantes

- **Origen de la clase (ver `Prompt.md`):** el recorrido de cadenas con `for` se sacó de la Clase 28 (indexing/slicing) para no diluir su foco, y se convirtió en clase propia porque había suficiente contenido: recorrido directo, recorrido con índice, y su combinación con rebanadas — más las actividades de Picuino N°22 (deletrear con/sin índice, impresión progresiva, ventana móvil) que quedaban sin usar.
- **Escenario continuado desde la Clase 28, a pedido explícito de Diego (sesión 2026-08-26):** se descartó una primera propuesta de escenario nuevo ("letrero LED/marcador deportivo" con el mensaje `"CAMPEONES"`, que Diego encontró confuso) y se reemplazó por la continuación literal del escenario de patentes/Registro Civil de la Clase 28 — mismo dato (`"BRTZ21"`) reutilizado en el Haz Ahora y el ICN, ahora extendido a un estacionamiento con cámara lectora en la entrada y pantalla angosta en la salida, que da pie natural a la ventana móvil (Concepto 3).
- **No se adelanta sintaxis no vista:** el Ejercicio 4 (patente capicúa) generaliza el Ejercicio 4 desafío de la Clase 28 —que comparaba solo 2 pares fijos para un código de 4 caracteres, evitando `for` porque el recorrido de cadenas todavía no se había enseñado— ahora sí con un ciclo con índice que funciona para una patente de cualquier largo. Se evitó deliberadamente `texto[::-1]` (slicing con paso), que no forma parte del contenido de esta clase ni de la anterior.
- **Ejercicios 0a/0b — se usan los 2:** la clase tiene dos matices claramente separables que ameritan drill aparte antes de pasar a los ejercicios contextualizados — recorrido directo (0a) y recorrido con índice (0b) — mismo criterio que ya se aplicó en la Clase 28 con índice/rebanada.
- **Ejercicios 1 y 2 como espejo simétrico:** ambos aplican el mismo concepto (recorrido + rebanada progresiva) pero en direcciones opuestas — de izquierda a derecha (pantalla "cargando") y de derecha a izquierda (app de transporte)— para que la Independiente refuerce que el "ancla" de la ventana puede ser el inicio o el final del texto, sin introducir sintaxis nueva entre uno y otro.
- **Ejercicio 3 combina recorrido con índice + `if` ya visto (contextualizado, fija el techo de dificultad junto con la Guiada):** obliga a decidir que un recorrido directo no basta cuando se necesita la posición, y reutiliza el condicional simple ya consolidado desde Condicionales.
