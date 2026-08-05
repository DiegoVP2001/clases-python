# Clase 20 — For Anidado (v2 — enunciados acotados)

**Estado:** Spec aprobada — 2026-08-05 (versión v2, sin sobreescribir la v1 aprobada el 2026-07-28)
**Clase Picuino:** N° 17 — Sentencias for anidadas
**URL Picuino:** https://www.picuino.com/es/python-for-anidados.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Condicionales completos (if/else, if anidadas, elif) y ciclos `for` con `range()` (Clase N°16, incluyendo `range()` con paso negativo)
- **Contenidos nuevos:** Ciclos `for` anidados (ciclo dentro de otro ciclo), relación filas/columnas entre ciclo externo e interno, sangría de dos niveles, construcción de salida por fila usando `print(..., end=...)` y `print()` vacío para el salto de línea
- **Contextos temáticos:** Cinemark del Mall Plaza Oeste (Haz Ahora, ICN y Guiada comparten el mismo escenario), torneo de tenis de mesa (Ejercicio 1), tablero de ajedrez (Ejercicio 2), revisión en zigzag del propio Cinemark (Ejercicio 3 — desafío)
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

### 3. Práctica Guiada (20 min)
El sistema del Cinemark quiere automatizar la lista de revisión que usa el equipo de aseo: en vez de anotarla a mano, el programa debe imprimir en pantalla cada asiento a revisar en la Sala 4, agrupado por fila.

**El programa debe:**
- Recorrer las 3 filas de la Sala 4
- Por cada fila, recorrer sus 5 asientos y mostrarlos uno junto al otro en la misma línea
- Saltar a una nueva línea al terminar cada fila

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

### 4. Práctica Independiente (18 min)

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

def verificar_ejercicio_1():
    esperadas = []
    for ronda in range(1, 6):
        for partido in range(1, ronda + 1):
            esperadas.append("Ronda " + str(ronda) + " - Partido " + str(partido))
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    esperadas = []
    for fila in range(1, 9):
        linea = ""
        for columna in range(1, 9):
            if (fila + columna) % 2 == 0:
                linea = linea + "Clara "
            else:
                linea = linea + "Oscura "
        esperadas.append(linea.strip())
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    esperadas = []
    for fila in range(1, 5):
        if fila % 2 == 1:
            asientos = list(range(1, 6))
        else:
            asientos = list(range(5, 0, -1))
        linea = "Fila " + str(fila) + ": " + " ".join(str(a) for a in asientos)
        esperadas.append(linea)
    _revisar("# Tu solución — Ejercicio 3", esperadas)
```

**Ejercicio 1 — Torneo de tenis de mesa**
El campeonato entre cursos tiene 5 rondas, y en cada ronda se juegan tantos partidos como el número de la ronda. La organización necesita la lista completa para pegarla en el diario mural.

**El programa debe:**
- Recorrer las 5 rondas del campeonato
- Por cada ronda, recorrer sus partidos (tantos como el número de la ronda)
- Mostrar una línea por partido, con su ronda y su número

**Resultado esperado:**
```
Ronda 1 - Partido 1
Ronda 2 - Partido 1
Ronda 2 - Partido 2
Ronda 3 - Partido 1
...
Ronda 5 - Partido 5
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 1 — puedes correrlo las veces que quieras
verificar_ejercicio_1()
```

- Solución:
  ```python
  for ronda in range(1, 6):
      for partido in range(1, ronda + 1):
          print("Ronda", ronda, "- Partido", partido)
  ```

**Ejercicio 2 — Tablero de ajedrez**
El taller de carpintería quiere revisar el patrón de un tablero de 8×8 antes de fabricarlo: una casilla es clara si la suma de su fila y su columna es par, y oscura si es impar.

**El programa debe:**
- Recorrer las 8 filas del tablero
- Por cada fila, recorrer sus 8 columnas
- Mostrar si cada casilla es clara u oscura
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

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 2 — puedes correrlo las veces que quieras
verificar_ejercicio_2()
```

- Solución:
  ```python
  for fila in range(1, 9):
      for columna in range(1, 9):
          if (fila + columna) % 2 == 0:
              print("Clara", end=" ")
          else:
              print("Oscura", end=" ")
      print()
  ```

**Ejercicio 3 — Desafío: revisión en zigzag**
Al equipo de aseo del Cinemark se le ocurrió una forma más rápida de revisar la sala: en vez de volver caminando hasta el asiento 1 cada vez que empieza una fila nueva, revisa la Fila 1 de izquierda a derecha, sigue de inmediato con la Fila 2 pero de derecha a izquierda, y así va alternando el sentido en cada fila. El supervisor quiere probar el programa en la Sala 6 (4 filas de 5 asientos) antes de aplicar el mismo truco en el resto de las salas.

**El programa debe:**
- Recorrer las 4 filas de la sala
- Recorrer los 5 asientos de cada fila, cambiando el sentido en las filas pares
- Mostrar los asientos de cada fila en una sola línea, en el orden en que se revisan

**Resultado esperado:**
```
Fila 1: 1 2 3 4 5
Fila 2: 5 4 3 2 1
Fila 3: 1 2 3 4 5
Fila 4: 5 4 3 2 1
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 3 — puedes correrlo las veces que quieras
verificar_ejercicio_3()
```

- Solución:
  ```python
  for fila in range(1, 5):
      print("Fila", fila, end=": ")
      if fila % 2 == 1:
          for asiento in range(1, 6):
              print(asiento, end=" ")
      else:
          for asiento in range(5, 0, -1):
              print(asiento, end=" ")
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

- **Esta es la v2 de la Clase 20**, generada sin sobreescribir la v1 aprobada el 2026-07-28 (que sigue en la carpeta raíz de la clase). Motivo: Diego evaluó que el formato extenso de v1 (narrativa larga + bullets de instrumentación del verificador + Nota de nombres exactos) funciona bien para las ayudantías de los lunes, pero no calza con el ritmo de una clase de martes/jueves de 80 min — el objetivo es que alcance para resolver los ejercicios de Independiente, no solo para leerlos.
- **Verificador rediseñado: compara la salida impresa, no las variables internas.** El verificador de v1 leía variables del estudiante desde `globals()` por nombre exacto, lo que obligaba a dictar 6-7 nombres de variable por ejercicio dentro del enunciado (más de la mitad de sus bullets) y a agregar una `Nota:` repetida explicando por qué. Además, sin `input()`, hacía varios chequeos puntuales dentro de una sola corrida (denominador = cantidad de chequeos), un patrón distinto al de Clase 16 (que sí usa `input()` y acumula un contador `_casos_ej1 = set()` con denominador hardcodeado en 5 — ahí es donde salió el mensaje confuso "Casos distintos superados: 1 / 5" que Diego vio en clase). El nuevo verificador vuelve a ejecutar la celda de solución del estudiante (ubicándola en el historial `In` de IPython por el comentario de su primera línea) y compara su salida real, línea por línea, contra el resultado esperado — sin pedir ningún nombre de variable. Esto cierra ambos problemas a la vez: el enunciado se acorta porque ya no hay instrumentación que dictar, y el veredicto usa un denominador real y alcanzable en una sola corrida (cantidad de líneas esperadas), nunca una meta de "5 casos" imposible de cumplir de una vez.
- **Cierre adicional del punto ciego del tablero simétrico.** La v1 necesitó un chequeo puntual extra (`primera_casilla_es_clara`) porque comparar solo conteos de claras/oscuras no detectaba invertir la condición de paridad en un tablero 8×8 (32/32 en ambos sentidos). El nuevo verificador compara el patrón línea por línea, así que ese error se detecta solo, en la primera fila — no hizo falta ningún chequeo adicional.
- **Ejercicio 3 (desafío) agregado**, a pedido explícito de Diego: retoma el escenario Cinemark del Haz Ahora/Guiada con un giro real (recorrido en zigzag), exigiendo `for` anidado + `if` + `range()` con paso negativo (ya visto en Clase 16, así que no adelanta contenido). No es obligatorio — está pensado para quien termine antes los dos primeros.
- **Tiempos ajustados:** Guiada 22→20 min, Independiente 16→18 min, para dejar margen a los tres ejercicios sin recortar el Haz Ahora, el ICN ni el Ticket de Salida (que no cambian respecto a v1).
- El resto de las decisiones de diseño (actitud "Orden", propósito acortado, Ticket con alternativas A/B/C/D, escenario Cinemark compartido) se mantienen idénticas a v1 — ver su Historial para el detalle completo.
