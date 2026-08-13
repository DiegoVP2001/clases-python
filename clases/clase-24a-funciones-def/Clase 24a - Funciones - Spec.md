# Clase 24a — Funciones (def, parámetros, return)

**Estado:** Spec aprobada — 2026-08-12
**Clase Picuino:** N° 19 — Definición de funciones
**URL Picuino:** https://www.picuino.com/es/python-funciones.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** booleanos y comparaciones, if/elif/else, for + range, for anidado, continue/break, while. Aún sin strings (indexing/métodos) ni listas.
- **Contenidos nuevos:** definir funciones con `def`, parámetros, llamar la función con argumentos, `return` (incl. que sin `return` la función devuelve `None`, y que `return` corta la ejecución).
- **Contextos temáticos:** kiosco del liceo (CEE), huerto escolar, Club Deportivo de Isla de Maipo, Peña de la Vendimia, Escuela de Rock — mezcla variada (regla 3).
- **Nota de alcance:** esta clase (parte 1, martes 18-ago) cubre solo `def`, parámetros y `return`. Los valores por omisión (Picuino N°20) se diseñan después como Clase 24b (parte 2, jueves 20-ago).
- **Ajuste explícito de Diego:** sin ninguna conexión ni alusión al Lunes Estándar de Funciones del 24-ago — clase diseñada de forma normal, independiente de esa dinámica.

## Objetivo

Construir funciones propias con `def` que resuelvan una tarea puntual, con claridad.

## Propósito

La claridad es explicar algo de forma que la otra persona entienda sin tener que adivinar ni preguntar de nuevo. Hoy la practicamos nombrando funciones y parámetros que dejan clara su tarea, sin que haga falta leer lo que hacen por dentro.

## Estructura de la clase

### 1. Haz Ahora (6 min)

El kiosco del liceo cobra normal a todos, pero a quienes están inscritos en el Centro de Estudiantes (CEE) les da un descuento fijo de \$300 en cualquier compra. Con la fila del recreo, ya se ha equivocado más de una vez calculando a mano.

Sabiendo que ustedes programan, el kiosco les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:

1. Si algo cuesta \$1.200 y la persona está inscrita en el CEE, ¿cuánto paga?
2. Si esa misma persona no estuviera inscrita, ¿cuánto pagaría?
3. ¿Qué dos datos necesita saber antes de calcular cuánto cobrar?
4. Si arma una "receta" para repetir este cálculo con cualquier comprador, ¿qué tiene que devolverle esa receta al final?

**Respuestas esperadas:**
1. \$900
2. \$1.200
3. El precio del producto y si la persona está inscrita en el CEE.
4. El precio final a cobrar.

### 2. Introducción al Contenido Nuevo (20 min)

**Concepto 1: Qué es una función y por qué usarla**
- Definición: un bloque de código con nombre propio que agrupa una tarea, para no repetirla escrita completa cada vez que se necesita.
- Ejemplo:
  ```python
  # Sin función: el mismo cálculo repetido
  print(8000 - 1500)
  print(5000 - 1500)
  print(12000 - 1500)
  ```
- Idea clave: una función se define una vez y se usa todas las veces que haga falta.

**Concepto 2: Definir con `def` y parámetros**
- Definición: `def nombre_funcion(parametro1, parametro2):` abre el bloque; el cuerpo va indentado debajo. Los parámetros son variables que la función espera recibir.
- Ejemplo:
  ```python
  def descuento_socio(precio, es_socia):
      if es_socia:
          return precio - 1500
      return precio
  ```
- Idea clave: definir la función no la ejecuta — solo queda "guardada la receta" hasta que alguien la llama.

**Concepto 3: Llamar la función: argumentos**
- Definición: llamar la función es escribir su nombre con paréntesis y los valores reales (argumentos) que ocupan el lugar de los parámetros.
- Ejemplo:
  ```python
  precio_final = descuento_socio(8000, True)
  print("Paga:", precio_final)
  ```
- Idea clave: parámetro es el nombre en la definición; argumento es el valor que se manda al llamar.

**Concepto 4: `return`: devolver un resultado**
- Definición: `return` entrega un valor de vuelta a quien llamó la función y termina la ejecución en ese punto. Sin `return`, la función devuelve `None`.
- Ejemplo:
  ```python
  def saluda(nombre):
      print("Hola,", nombre)

  resultado = saluda("Camila")
  print(resultado)
  ```
  ```
  >> Hola, Camila
  >> None
  ```
- Idea clave: `print()` muestra algo en pantalla, pero solo `return` deja el valor disponible para usarlo después.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Llamar la función sin paréntesis (`descuento_socio`) | No ejecuta nada, solo referencia a la función | Agregar `()` con los argumentos |
| Confundir `print()` interno con `return` | La función "muestra" el resultado pero no lo entrega — la variable que la recibe queda en `None` | Usar `return` si el valor se necesita después |
| Esperar que una variable definida dentro de la función exista afuera | `NameError` al intentar usarla fuera | Devolver el valor con `return` y guardarlo en una variable afuera |
| Escribir código después de un `return` esperando que se ejecute | Ese código nunca corre | Recordar que `return` corta la función ahí mismo |

### 3. Práctica Guiada (25 min)

El kiosco quiere una función que reciba el precio de un producto y si la persona está inscrita en el CEE, y le entregue de vuelta cuánto debe cobrar.

**El programa debe:**
- Definir una función con dos parámetros: el precio del producto y si la persona está inscrita en el CEE.
- Dentro de la función, aplicar el descuento fijo solo si está inscrita; si no, dejar el precio igual.
- Devolver ese precio final con `return`.
- Pedir el precio de un producto y si la persona está inscrita en el CEE, llamar la función, y mostrar cuánto debe pagar.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario ingresa</em><pre>1200
si</pre></td>
<td>📥 <em>El usuario ingresa</em><pre>800
no</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em><pre>Debe pagar: 900</pre></td>
<td>📤 <em>El programa imprime</em><pre>Debe pagar: 800</pre></td>
</tr>
</table>

- Solución:
  ```python
  def calcula_cobro(precio, inscrita_cee):
      if inscrita_cee:
          return precio - 300
      return precio

  precio_producto = int(input("¿Cuánto cuesta el producto? "))
  inscrita = input("¿Está inscrita en el CEE? (si/no) ") == "si"

  total = calcula_cobro(precio_producto, inscrita)
  print("Debe pagar:", total)
  ```

### 4. Práctica Independiente (18 min)

**Ejercicio 1 — Huerto escolar**

El huerto del liceo organiza brigadas de cosecha y junta los tomates en cajones de 12 para venderlos en la feria del sábado. Cada brigadista anota cuántos tomates cosechó, pero armar los cajones a mano y contar los que sobran ya generó más de un error.

**El programa debe:**
- Definir una función que reciba la cantidad de tomates cosechados y devuelva cuántos cajones completos de 12 se pueden armar.
- Pedir la cantidad cosechada.
- Llamar la función y mostrar el resultado.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario ingresa</em><pre>50</pre></td>
<td>📥 <em>El usuario ingresa</em><pre>137</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em><pre>Cajones completos: 4</pre></td>
<td>📤 <em>El programa imprime</em><pre>Cajones completos: 11</pre></td>
</tr>
</table>

- Solución:
  ```python
  def cajones_completos(tomates_cosechados):
      return tomates_cosechados // 12

  cosechados = int(input("¿Cuántos tomates cosechaste? "))
  print("Cajones completos:", cajones_completos(cosechados))
  ```

**Ejercicio 2 — Club Deportivo de Isla de Maipo**

El Club Deportivo cobra una cuota mensual fija, y algunos socios llegan atrasados varios meses. Quieren calcular rápido cuánto deben pagar en total.

**El programa debe:**
- Definir una función con dos parámetros (cuota mensual, meses atrasados) que devuelva el total a pagar.
- Pedir esos dos datos.
- Llamar la función y mostrar el total.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario ingresa</em><pre>5000
3</pre></td>
<td>📥 <em>El usuario ingresa</em><pre>8000
2</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em><pre>Total a pagar: 15000</pre></td>
<td>📤 <em>El programa imprime</em><pre>Total a pagar: 16000</pre></td>
</tr>
</table>

- Solución:
  ```python
  def total_a_pagar(cuota_mensual, meses_atrasados):
      return cuota_mensual * meses_atrasados

  cuota = int(input("¿Cuál es la cuota mensual? "))
  meses = int(input("¿Cuántos meses debe? "))
  print("Total a pagar:", total_a_pagar(cuota, meses))
  ```

**Ejercicio 3 — Peña de la Vendimia**

La Peña de la Vendimia, la fiesta típica de Isla de Maipo, cobra entrada general en la puerta, pero los niños menores de 12 años entran liberados y las personas de 65 años o más pagan la mitad. El organizador anota mal los cobros cuando hay mucha gente esperando y quiere automatizarlo.

**El programa debe:**
- Definir una función que reciba la edad de la persona y el precio general, y devuelva cuánto debe pagar.
- Aplicar las tres categorías: menores de 12 (liberado), 65 o más (mitad de precio), el resto (precio general).
- Pedir la edad de un asistente y el precio general, llamar la función, y mostrar cuánto debe pagar.

**Resultado esperado:**

<table>
<tr><th>Ejemplo 1</th><th>Ejemplo 2</th></tr>
<tr>
<td>📥 <em>El usuario ingresa</em><pre>8
5000</pre></td>
<td>📥 <em>El usuario ingresa</em><pre>70
5000</pre></td>
</tr>
<tr>
<td>📤 <em>El programa imprime</em><pre>Debe pagar: 0</pre></td>
<td>📤 <em>El programa imprime</em><pre>Debe pagar: 2500</pre></td>
</tr>
</table>

- Solución:
  ```python
  def cobro_entrada(edad, precio_general):
      if edad < 12:
          return 0
      elif edad >= 65:
          return precio_general // 2
      return precio_general

  edad_asistente = int(input("¿Qué edad tiene el asistente? "))
  precio_general = int(input("¿Cuál es el precio general? "))
  print("Debe pagar:", cobro_entrada(edad_asistente, precio_general))
  ```

**Ejercicio 4 — Desafío: Escuela de Rock** *(opcional)*

La profesora de la Escuela de Rock de la comuna lleva el registro de horas de práctica de cada estudiante y necesita saber, para cualquiera de ellos, cuántas horas le faltan para llegar a las 20 horas mínimas del semestre. Como revisa a varios estudiantes seguidos antes de cada clase, quiere repetir el cálculo tantas veces como estudiantes tenga enfrente, sin cerrar el programa entre uno y otro.

**El programa debe:**
- Definir una función que reciba las horas que un estudiante ya practicó y devuelva cuántas horas le faltan para llegar a 20 (nunca un número negativo).
- Repetir el cálculo para distintos estudiantes hasta que la profesora escriba `"listo"` en vez de un nombre.
- Para cada estudiante, pedir su nombre y sus horas practicadas, llamar la función, y mostrar cuántas horas le faltan.

**Resultado esperado:**
```
¿Nombre del estudiante? (o "listo" para terminar) Fernanda
¿Cuántas horas practicó? 14
A Fernanda le faltan 6 horas.
¿Nombre del estudiante? (o "listo" para terminar) Benjamín
¿Cuántas horas practicó? 22
A Benjamín le faltan 0 horas.
¿Nombre del estudiante? (o "listo" para terminar) listo
```

- Solución:
  ```python
  def horas_faltantes(horas_practicadas):
      faltan = 20 - horas_practicadas
      if faltan < 0:
          return 0
      return faltan

  nombre_estudiante = input('¿Nombre del estudiante? (o "listo" para terminar) ')
  while nombre_estudiante != "listo":
      horas = int(input("¿Cuántas horas practicó? "))
      print("A", nombre_estudiante, "le faltan", horas_faltantes(horas), "horas.")
      nombre_estudiante = input('¿Nombre del estudiante? (o "listo" para terminar) ')
  ```

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
def triple(numero):
    return numero * 3

resultado = triple(4)
print("Resultado:", resultado)
```
¿Qué imprime este programa?
- A: Resultado: 4
- B: Resultado: 12
- C: Resultado: None
- D: No imprime nada, falta un `print()` dentro de la función

**Respuesta correcta:** B
**Justificación:** la función multiplica el parámetro por 3 y `return` entrega ese valor, que queda guardado en `resultado`.

**Pregunta 2:**
```python
def saluda(nombre):
    print("Hola,", nombre)

valor = saluda("Camila")
print(valor)
```
¿Qué imprime la última línea (`print(valor)`)?
- A: Hola, Camila
- B: Camila
- C: None
- D: Error, no se puede guardar el resultado de una función en una variable

**Respuesta correcta:** C
**Justificación:** `saluda` no tiene `return`, así que devuelve `None` por defecto y eso es lo que queda guardado en `valor`.

**Pregunta 3:**
```python
def clasifica(edad):
    if edad < 12:
        return "niño"
    return "adulto"
    print("Fin de la función")  # <- esta línea

resultado = clasifica(8)
print(resultado)
```
¿Qué se imprime en total al ejecutar este programa?
- A: niño
- B: niño y Fin de la función
- C: adulto
- D: Fin de la función y niño

**Respuesta correcta:** A
**Justificación:** el `return "niño"` corta la ejecución de la función ahí mismo; la línea marcada nunca se alcanza.

### Cierre (5 min)

**Objetivo de la clase:** Construir funciones propias con `def` que resuelvan una tarea puntual, con claridad.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan clara te quedó la diferencia entre `print()` y `return` dentro de una función?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación —dentro o fuera de la programación— ser claro/a al pedir o explicar una tarea evita que la otra persona tenga que preguntar de nuevo?

## Decisiones de diseño relevantes

- **Reestructuración permanente de Independiente/Guiada (default desde esta clase, 2026-08-12):** se actualizaron las reglas 15/16/20 del `CLAUDE.md` raíz del proyecto. Independiente pasa de "2 obligatorios + 1 desafío" a **3 obligatorios (2 directos + 1 contextualizado/complejo) + 1 desafío opcional**, y la Guiada sube su nivel de dificultad para igualar al Ejercicio 3 (antes no tenía un nivel de referencia explícito). Motivación de Diego: usar esta clase como base directa para diseñar el Control del Lunes Estándar del 24-ago sobre Funciones — los Ejercicios 1-2 modelan el tipo de ítem directo del Control, el Ejercicio 3/Guiada modela el ítem de cierre que combina conceptos.
- **Ejercicios 1-2 sin condicional interno; Ejercicio 3 y Guiada combinan `return` con condicionales (if/elif/else) ya vistos** — así el salto de dificultad hacia el Ejercicio 3 es real (más categorías, no solo cambio de contexto) y no una simple repetición de la Guiada con otro nombre.
- **Parámetros booleanos vía comparación (`input(...) == "si"`)** en vez de valores por omisión — Picuino N°20 (valores por omisión) es contenido de Clase 24b, todavía no visto. Se reutiliza el patrón de comparación que produce un booleano, ya conocido desde Clase 8a.
- **Sin conexión explícita al Lunes Estándar** — por pedido expreso de Diego, ningún texto de la clase (Haz Ahora, Guiada, enunciados) alude al control o a esa dinámica; la clase se diseñó de forma autónoma.
- **Ejercicio 4 (desafío) combina función + `while` + comparación de string** para reutilizar contenido ya visto (Clase 21b/22) sin adelantar nada nuevo, dándole al desafío su margen habitual de narrativa más rica.
