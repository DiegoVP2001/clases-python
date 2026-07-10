# Clase 16 — for + range()

**Estado:** Spec aprobada — 2026-07-08
**Clase Picuino:** N° 13 (Sentencia for) + N° 14 (La función range())
**URL Picuino:** https://www.picuino.com/es/python-for.html

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** `input()`/`print()`, tipos de datos, variables, booleanos, comparaciones, operadores lógicos, `if`/`else`, `if` anidadas, `elif`. Programación por bloques (bucle "contar con VARIABLE desde X hasta Y de a Z").
- **Contenidos nuevos:** sentencia `for`, función `range(inicio, fin, salto)` con sus valores por defecto, patrón acumulador dentro de un bucle.
- **Contextos temáticos:** Mundial 2026 (resultados reales al 7 de julio de 2026: Suiza elimina a Colombia en octavos por penales 4-3; cuartos de final Francia/Marruecos vs España/Bélgica y Noruega/Inglaterra vs Argentina/Suiza; semifinal el 19 de julio en MetLife Stadium).

## Objetivo

Construir programas en Python que utilicen la sentencia `for` y la función `range()` para repetir instrucciones y generar secuencias numéricas controladas, con orden.

## Propósito

El orden es la capacidad de escribir y organizar el código de manera clara, estructurada y fácil de seguir. Esa habilidad nos sirve en cualquier proceso real que se repita muchas veces, donde la claridad evita errores costosos. Hoy la vamos a ejercitar con `for` y `range()`, construyendo bucles ordenados para generar secuencias como las fechas de un campeonato.

## Estructura de la clase

### 1. Haz Ahora (5-8 min)

**Propósito:** Recordar el bloque "contar con VARIABLE desde X hasta Y de a Z hacer" que ya vieron en programación por bloques, para anclar la idea de repetición controlada antes de traducirla a `range()`.

¿Se acuerdan del bloque que usábamos para contar en programación por bloques?

![Bloque "contar con VARIABLE desde X hasta Y de a Z hacer"](assets/bloque_for.png)

Con ese bloque en mente, respondan en papel: si quisiéramos contar, uno por uno, los partidos que faltan del Mundial (desde el número 1 hasta el número 7), ¿cuántas veces se repetiría el bloque? ¿Qué números tocaría en cada vuelta?

**Respuestas esperadas:**
1. El bloque se repetiría 7 veces.
2. Tocaría los números 1, 2, 3, 4, 5, 6, 7 — nunca llega al 8, porque el bloque se detiene ANTES del valor "hasta".

### 2. Introducción al Contenido Nuevo (15-20 min)

**Comparación: `for` y `range(inicio, fin, salto)` lado a lado**

| 🔁 `for` | 🔢 `range(inicio, fin, salto)` |
|---|---|
| El ciclo `for` repite un bloque de código una vez por cada valor de una secuencia.<br><br>La variable cambia automáticamente en cada vuelta. | Genera la secuencia de números que `for` va a recorrer: empieza en `inicio`, termina ANTES de `fin` (el `fin` nunca se incluye), avanzando de a `salto` en cada vuelta. |
| <pre style="white-space:pre-wrap;">for numero_partido in range(1, 8, 1):<br>    print("Partido número", numero_partido)</pre> | <pre style="white-space:pre-wrap;">range(1, 8, 1)<br>inicio = 1<br>fin    = 8   (no incluido)<br>salto  = 1</pre> |
| **Idea clave:** todo lo que esté indentado bajo el `for` se repite una vez por cada valor de la variable iteradora. | **Idea clave:** `fin` nunca se incluye — por eso `range(1, 8)` se detiene en 7, no en 8. Si se omite `inicio`, el valor por defecto es 0; si se omite `salto`, el valor por defecto es 1. Es la traducción directa a Python del bloque "contar con VARIABLE desde X hasta Y de a Z" que ya conocían. |
</tr>
</table>

- Ejemplo:
  ```python
  for numero_partido in range(1, 8, 1):
      print("Partido número", numero_partido)
  # >> Partido número 1
  # >> Partido número 2
  # >> Partido número 3
  # >> Partido número 4
  # >> Partido número 5
  # >> Partido número 6
  # >> Partido número 7
  ```

**Concepto 1: Acumulador dentro de un bucle**
- Definición: una variable "acumuladora" se inicializa en 0 ANTES del `for`, fuera del bloque indentado, y dentro del bucle se le suma un valor en cada vuelta para ir guardando un total.
- Ejemplo:
  ```python
  goles_totales = 0
  for numero_partido in range(1, 5):
      goles_totales = goles_totales + 2
  print("Goles totales estimados:", goles_totales)
  # >> Goles totales estimados: 8
  ```
- Idea clave: si la variable acumuladora se inicializa DENTRO del bucle, se reinicia en cada vuelta y nunca acumula de verdad.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Esperar que el `fin` de `range()` se incluya | El bucle se detiene un valor antes de lo esperado | Recordar: `fin` nunca se incluye, igual que la Y del bloque no se contaba |
| Olvidar la indentación del bloque bajo `for` | El código no se repite, se ejecuta solo una vez | Verificar que todo lo que debe repetirse esté indentado |
| Inicializar el acumulador dentro del bucle | El total se reinicia en cada vuelta, nunca acumula | Mover la inicialización (`= 0`) antes del `for` |

### 3. Práctica Guiada (20-25 min)

**Situación:** La semana pasada ya sabíamos todos los resultados hasta los octavos de final del Mundial 2026. Ahora entramos a la recta final: quedan por jugarse los partidos de cuartos, semifinales y la gran final — 7 partidos en total. Vamos a contarlos uno por uno con `range()`, tal como lo hacíamos con el bloque que ya conocíamos, y armar además una cuenta regresiva de los días que faltan para la final.

**Variables:**
```python
partidos_contados = 0
```

**Pasos guiados (tabla):**

- Paso 1: Crea una variable que registre cuántos partidos llevas contados, comenzando en cero, antes de empezar a repetir nada.
  Resultado:
  ```
  (todavía no hay output — es solo la variable inicial)
  ```

- Paso 2: Construye un bucle que recorra los números del 1 al 7 — los partidos que faltan del Mundial — usando `range()` con inicio, fin y salto, igual que el bloque "desde X hasta Y de a Z" que ya conocías. En cada vuelta, suma 1 a la variable que cuenta los partidos y muestra en pantalla en qué número de partido vas.
  Resultado:
  ```
  Partido 1 de los que quedan
  Partido 2 de los que quedan
  ...
  Partido 7 de los que quedan
  ```

- Paso 3: Después del bucle (sin indentación), muestra en pantalla el total de partidos contados.
  Resultado:
  ```
  Total de partidos que quedan: 7
  ```

- Paso 4: Construye un segundo bucle que recorra, en cuenta regresiva, los días que faltan para la final: desde 11 hasta 1, mostrando en cada vuelta cuántos días faltan.
  Resultado:
  ```
  Faltan 11 días para la final
  Faltan 10 días para la final
  ...
  Faltan 1 días para la final
  ```

- Solución:
  ```python
  partidos_contados = 0
  for numero_partido in range(1, 8, 1):
      partidos_contados = partidos_contados + 1
      print("Partido", numero_partido, "de los que quedan")
  print("Total de partidos que quedan:", partidos_contados)

  for dias_para_la_final in range(11, 0, -1):
      print("Faltan", dias_para_la_final, "días para la final")
  ```

### 4. Práctica Independiente (15-18 min)

**Ejercicio 1 — Racha goleadora**

Un equipo llegó a cuartos de final con una racha goleadora que todos comentan. La pareja quiere armar un programa que, sabiendo cuántos partidos jugó ese equipo en el torneo y cuántos goles anota en promedio por partido, vaya mostrando cuánto lleva acumulado después de cada partido, hasta llegar al total estimado.

**El programa debe:**
- **Pedir** cuántos partidos jugó el equipo en el torneo.
- **Pedir** el promedio de goles que anota por partido.
- **Recorrer** cada partido uno por uno, acumulando el total de goles estimado.
- **Mostrar**, después de cada partido, cuántos goles lleva acumulados el equipo hasta ese momento.
- **Mostrar** al final el total de goles estimado en todo el torneo.

<table>
<tr><th></th><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario escribe</em></td>
<td><pre>4
2</pre></td>
<td><pre>3
3</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em></td>
<td><pre>Después del partido 1 : 2 goles acumulados
Después del partido 2 : 4 goles acumulados
Después del partido 3 : 6 goles acumulados
Después del partido 4 : 8 goles acumulados
Total estimado en el torneo: 8 goles</pre></td>
<td><pre>Después del partido 1 : 3 goles acumulados
Después del partido 2 : 6 goles acumulados
Después del partido 3 : 9 goles acumulados
Total estimado en el torneo: 9 goles</pre></td>
</tr>
</table>

- Solución:
  ```python
  partidos_jugados = int(input("¿Cuántos partidos jugó el equipo en el torneo? "))
  promedio_goles = int(input("¿Cuál es su promedio de goles por partido? "))

  goles_acumulados = 0
  for numero_partido in range(1, partidos_jugados + 1):
      goles_acumulados = goles_acumulados + promedio_goles
      print("Después del partido", numero_partido, ": ", goles_acumulados, "goles acumulados")

  print("Total estimado en el torneo:", goles_acumulados, "goles")
  ```

**Ejercicio 2 — Cuenta regresiva personalizada (Bonus — décimas extra, solo si terminaron el Ejercicio 1)**

Hay un partido de esta recta final que la pareja no se quiere perder. Si indican cuántos días faltan para ese partido, el programa debe armar la cuenta regresiva completa, día por día, hasta anunciar que por fin llegó el día.

**El programa debe:**
- **Pedir** cuántos días faltan para el partido que quieren ver.
- **Recorrer** la cuenta regresiva completa, mostrando cuántos días faltan en cada vuelta.
- **Mostrar**, al llegar a cero, un mensaje especial anunciando que el partido es hoy.

<table>
<tr><th></th><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario escribe</em></td>
<td><pre>4</pre></td>
<td><pre>2</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em></td>
<td><pre>Faltan 4 días
Faltan 3 días
Faltan 2 días
Faltan 1 días
¡Hoy se juega!</pre></td>
<td><pre>Faltan 2 días
Faltan 1 días
¡Hoy se juega!</pre></td>
</tr>
</table>

- Solución:
  ```python
  dias_para_el_partido = int(input("¿Cuántos días faltan para el partido que quieres ver? "))

  for dias_restantes in range(dias_para_el_partido, 0, -1):
      print("Faltan", dias_restantes, "días")

  print("¡Hoy se juega!")
  ```

### 5. Ticket de Salida (5-8 min)

**Pregunta 1:** ¿Qué valores imprime este código?
```python
for numero in range(2, 9, 2):
    print(numero)
```
- A) 2, 4, 6, 8
- B) 2, 4, 6, 8, 9
- C) 2, 4, 6
- D) 0, 2, 4, 6, 8

**Respuesta correcta:** A
**Justificación:** `range(2, 9, 2)` empieza en 2, avanza de 2 en 2, y se detiene ANTES de llegar a 9 — por eso el último valor es 8, no 9.

**Pregunta 2:** ¿Cuántas veces se ejecuta el `print()` de este código?
```python
for partido in range(6):
    print("Partido", partido)
```
- A) 5 veces
- B) 6 veces
- C) 7 veces
- D) Ninguna, porque falta el inicio

**Respuesta correcta:** B
**Justificación:** cuando `range()` recibe un solo argumento, el `inicio` por defecto es 0 y el `salto` por defecto es 1, entonces genera 0,1,2,3,4,5 — son 6 valores en total.

**Pregunta 3:** Un compañero escribió este código para sumar los goles estimados de 3 partidos, pero el resultado siempre muestra el mismo número que el último partido, no la suma total. ¿Cuál es el error?
```python
for partido in range(1, 4):
    goles_totales = 0
    goles_totales = goles_totales + 2
print(goles_totales)
```
- A) El `range()` está mal escrito
- B) La variable `goles_totales` se inicializa dentro del bucle, así que se reinicia en cada vuelta
- C) Falta el `print()` dentro del bucle
- D) La variable `partido` no se está usando

**Respuesta correcta:** B
**Justificación:** `goles_totales = 0` debe ir una sola vez, antes del `for`. Si queda indentado dentro del bucle, se reinicia en cada vuelta y nunca acumula.

### Cierre (5 min)

**Objetivo de la clase**

Construir programas en Python que utilicen la sentencia `for` y la función `range()` para repetir instrucciones y generar secuencias numéricas controladas, con orden.

**Pregunta 1 — Metacognición (escala 1-5)**

¿Qué tan seguro/a te sientes usando `for` y `range()` para repetir tareas, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro**

¿En qué proceso de tu vida diaria u otro ramo el orden al organizar pasos repetidos evitaría errores?

## Decisiones de diseño relevantes

- El Haz Ahora usa la imagen real del bloque "contar con VARIABLE desde X hasta Y de a Z hacer" recortada de `clases/for_bloques.pdf` (`assets/bloque_for.png`), en vez de una recreación en HTML — la primera versión con `<div>`/`<span>` no se veía bien en Colab. El generador (`crear_colab.py`) ahora incrusta automáticamente cualquier imagen local referenciada en el spec como base64, así el `.ipynb` queda autocontenido sin depender de subir archivos aparte.
- El ICN presenta `for` y `range(inicio, fin, salto)` como una tabla comparativa lado a lado (nuevo tipo de item `**Comparación:**` soportado por el generador, análogo a `**Concepto:**`/`**Demostración:**`), mostrando de inmediato la estructura `range(inicio, fin, salto)` — así calza 1:1 con el bloque "desde X hasta Y de a Z" que el curso ya conocía. No hay sobrecarga de contenidos porque `for` y `range()` son, en este punto del curso, una sola habilidad con dos piezas de sintaxis inseparables (aún no se han visto listas).
- La situación de la Guiada usa el framing "la semana pasada ya sabíamos los resultados hasta octavos" para no depender de resultados específicos que puedan cambiar antes de que Diego dicte la clase la semana siguiente (cuando algunos partidos de cuartos ya se habrán jugado).
- Los pasos guiados usan el nuevo formato de tabla de 2 columnas (`**Pasos guiados (tabla):**`, soportado en `crear_colab.py`), reemplazando la lista numerada + bloque de resultado único de las clases anteriores. Los pasos originales 2 y 3 (construir el bucle + sumar y mostrar dentro de él) se fusionaron en una sola fila, porque separados el paso de "construir el bucle" quedaba sin resultado propio que mostrar en la tabla. El resultado esperado de cada fila también se acortó con `...` para no ser tan largo.
- Práctica Independiente: 1 ejercicio obligatorio + 1 bonus (décimas extra), alineado con el nuevo default de trabajo en parejas — Diego revisa el obligatorio en vivo trayendo a una pareja a explicarlo al curso.
- Todas las soluciones de esta clase (Haz Ahora, Guiada, Independiente, Ticket) van únicamente a `Clase 16 - for + range() - Solucionario.ipynb`, que se genera junto con el Colab de clase.
