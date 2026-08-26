# Clase 17 — Ejercitación Condicionales (if / if anidados / elif)

**Estado:** Spec aprobada — 2026-07-09
**Tipo:** Clase de consolidación (ejercitación en parejas, con décimas) — sin contenido nuevo
**Clases Picuino de referencia:** N°9 (if/else), N°11 (if anidados), N°12 (elif)
**Consolida:** clases reales 11 (if/else), 13 (if anidadas), 14 (elif)

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Parejas
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** `input()`, booleanos (comparaciones, `and`/`or`/`not`), `if`/`else`, `if` anidados, `elif`
- **Contenidos nuevos:** Ninguno. Se combina un `if` anidado **dentro de una rama `elif`** — patrón no mostrado explícitamente en C13 ni C14, pero construido solo con sintaxis ya conocida.
- **Contextos temáticos:** descuentos por compra (Guiada), delivery (Ejercicio 1), gimnasio (Ejercicio 2), furgón escolar (Ejercicio 3), entradas a un festival (Ejercicio 4)
- **Décimas:** +1 por ejercicio resuelto y funcionando en Ejercicios 1-3, **+2 en el Ejercicio 4** (máximo 5 décimas). Corrección en vivo durante la revisión proyectada — no hay autocorrección oculta.

## Objetivo

Resolver problemas de decisión aplicando `if`/`else`, `if` anidados y `elif` según corresponda a cada situación — reconociendo cuál estructura es la más adecuada en lugar de aplicar siempre la misma — trabajando en pareja y persistiendo ante errores de sintaxis e indentación.

## Propósito

Elegir la herramienta correcta para cada problema —en vez de usar siempre la misma por costumbre— es una habilidad que trasciende la programación: aplica al elegir cómo resolver un conflicto, qué método de estudio usar según la materia, o qué herramienta usar en un trabajo en equipo. Hoy vas a practicar ese criterio decidiendo, para cada ejercicio, si conviene anidar, encadenar con `elif`, o combinar ambas.

## Estructura de la clase

### 1. Apertura (5 min)

Diego presenta el objetivo y el encuadre: hoy no hay contenido nuevo que aprender, es una sesión de ejercitación en parejas con décimas por ejercicio resuelto. Se recuerda brevemente qué cubre cada estructura (if/else, if anidados, elif) sin ejemplos de código — solo para activar memoria antes de la Guiada.

### 2. Práctica Guiada (10 min)

**Situación:** Un local registra el monto de una compra y si la persona tiene tarjeta de fidelización, para decidir qué descuento aplicar.

**Variables:**
```python
monto_compra = 12000
tiene_tarjeta = True
```

**Pasos guiados (tabla):**

- Paso 1: Crea las variables del monto y la tarjeta, y escribe el `if` para compras muy bajas (menos de \$5.000)
  Resultado:
  ```
  (no se ejecuta con este monto — sigue evaluando)
  ```

- Paso 2: Agrega el `elif` para el rango medio (entre \$5.000 y \$19.999), y dentro de él anida un `if`/`else` según si tiene tarjeta
  Resultado:
  ```
  Tienes 10% de descuento por ser socio.
  ```

- Paso 3: Cierra con el `else` final para compras de \$20.000 o más
  Resultado:
  ```
  (no se ejecuta con este monto)
  ```

- Solución:
  ```python
  monto_compra = 12000
  tiene_tarjeta = True

  if monto_compra < 5000:
      print("Compra muy baja: sin descuento por ahora.")
  elif monto_compra < 20000:
      if tiene_tarjeta:
          print("Tienes 10% de descuento por ser socio.")
      else:
          print("Sin descuento — hazte socio para la próxima.")
  else:
      print("Compra alta: 15% de descuento automático.")
  ```

### 3. Trabajo en parejas — 4 ejercicios (40 min)

**Ejercicio 1 — Delivery (calentamiento)**

Una app de delivery del barrio ofrece despacho gratis cuando el pedido supera cierto monto mínimo. Si el pedido no alcanza ese mínimo, se cobra un costo fijo de envío. Escribe el programa que, dado el monto del pedido, informe si el envío es gratis o si debe pagar el costo de despacho.

**El programa debe:**
- Registrar el **monto del pedido** como variable al inicio
- Verificar si el monto **alcanza el mínimo** para envío gratis (\$15.000)
- Mostrar un **mensaje distinto** según corresponda

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>monto_pedido = 8000</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>monto_pedido = 18000</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>No alcanza el envío gratis. Se cobra $ 1500 de despacho.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>¡Envío gratis! Tu pedido superó el mínimo.</pre></td>
</tr>
</table>

- Solución:
  ```python
  monto_pedido = 8000
  minimo_envio_gratis = 15000
  costo_despacho = 1500

  if monto_pedido >= minimo_envio_gratis:
      print("¡Envío gratis! Tu pedido superó el mínimo.")
  else:
      print("No alcanza el envío gratis. Se cobra $", costo_despacho, "de despacho.")
  ```

---

**Ejercicio 2 — Gimnasio**

Un gimnasio del barrio quiere automatizar su recepción. Antes de dejar entrar a alguien, el sistema revisa dos cosas en orden: primero si el gimnasio está abierto a esa hora, y solo si lo está, si hay cupo disponible en la sala de máquinas. Escribe el programa que informe el resultado según ambas condiciones.

**El programa debe:**
- Registrar si el gimnasio **está abierto** y si hay **cupo disponible**
- Verificar primero si está **abierto**
- Solo si está abierto, verificar si hay **cupo**
- Mostrar un **mensaje distinto** para cada uno de los tres caminos posibles

<details><summary>💡 Pista 1 — ¿Cuántos caminos hay?</summary>
Antes de programar, cuenta los resultados posibles: cerrado, abierto pero sin cupo, abierto y con cupo. Eso te dice cuántos mensajes necesitas.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>gimnasio_abierto = True
hay_cupo = True</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>gimnasio_abierto = False
hay_cupo = True</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>¡Bienvenido! Hay cupo disponible.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>El gimnasio está cerrado en este horario.</pre></td>
</tr>
</table>

- Solución:
  ```python
  gimnasio_abierto = True
  hay_cupo = True

  if gimnasio_abierto:
      if hay_cupo:
          print("¡Bienvenido! Hay cupo disponible.")
      else:
          print("El gimnasio está abierto, pero no hay cupo en este momento.")
  else:
      print("El gimnasio está cerrado en este horario.")
  ```

---

**Ejercicio 3 — Furgón escolar**

El furgón escolar de tu colegio registra cuántos minutos de atraso lleva cada mañana. Según ese tiempo, el sistema clasifica el estado del recorrido en distintas categorías para avisar a los apoderados con anticipación. Escribe el programa que, dado el atraso en minutos, muestre la categoría correspondiente.

**El programa debe:**
- Registrar el **atraso en minutos** como variable al inicio
- Clasificar el estado usando **cuatro categorías** según el atraso
- Mostrar un **mensaje claro** con la categoría obtenida

<details><summary>💡 Pista 1 — Orden de las condiciones</summary>
Ordena los rangos de menor a mayor (o mayor a menor) de forma consistente en todos los `elif`, igual que en la clase de `elif`.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>atraso_minutos = 3</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>atraso_minutos = 20</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Leve atraso: llega en unos minutos más.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Recorrido cancelado: contacta al colegio.</pre></td>
</tr>
</table>

- Solución:
  ```python
  atraso_minutos = 3

  if atraso_minutos == 0:
      print("Puntual: el furgón llegó a la hora.")
  elif atraso_minutos <= 5:
      print("Leve atraso: llega en unos minutos más.")
  elif atraso_minutos <= 15:
      print("Atraso considerable: revisa con el conductor.")
  else:
      print("Recorrido cancelado: contacta al colegio.")
  ```

---

**Ejercicio 4 — Entradas al festival (desafío, +2 décimas)**

Un festival de música vende entradas por etapas según cuántas quedan disponibles. Cuando las entradas están en la etapa intermedia, el sistema revisa además si la persona tiene un código de preventa, porque eso le da prioridad de compra frente al resto. Escribe el programa que, dado el número de entradas restantes y si la persona tiene código de preventa, muestre el resultado correspondiente.

**El programa debe:**
- Registrar las **entradas restantes** y si la persona tiene **código de preventa**
- Verificar primero si las entradas **se agotaron**
- Si quedan **pocas entradas** (etapa intermedia), verificar además el **código de preventa**
- Si quedan **muchas entradas**, mostrar que la compra está disponible sin restricciones

<details><summary>💡 Pista 1 — La misma estructura de la Guiada</summary>
Este ejercicio usa el mismo patrón que armaste en la Guiada: un `if`, un `elif` con un `if` anidado adentro, y un `else` final. Solo cambia el contexto y los números.
</details>

<table>
<tr>
  <th>Ejemplo 1</th>
  <th>Ejemplo 2</th>
</tr>
<tr>
  <td>📥 <em>El usuario escribe</em><pre>entradas_restantes = 30
codigo_preventa = True</pre></td>
  <td>📥 <em>El usuario escribe</em><pre>entradas_restantes = 30
codigo_preventa = False</pre></td>
</tr>
<tr>
  <td>📤 <em>El programa imprime</em><pre>Tienes prioridad de compra por tu código de preventa.</pre></td>
  <td>📤 <em>El programa imprime</em><pre>Quedan pocas entradas — sin código de preventa debes esperar la venta general.</pre></td>
</tr>
</table>

- Solución:
  ```python
  entradas_restantes = 30
  codigo_preventa = True

  if entradas_restantes == 0:
      print("Entradas agotadas.")
  elif entradas_restantes <= 50:
      if codigo_preventa:
          print("Tienes prioridad de compra por tu código de preventa.")
      else:
          print("Quedan pocas entradas — sin código de preventa debes esperar la venta general.")
  else:
      print("Entradas disponibles sin restricciones.")
  ```

### 4. Revisión proyectada (18 min)

Diego proyecta el Colab de una pareja por ejercicio (o el propio, según lo que se recoja en la ronda) y esa pareja explica su solución al curso — ambos integrantes participan. Prioridad de revisión: Ejercicio 2 (if anidado con else en cada nivel) y Ejercicio 4 (el patrón nuevo, elif con if anidado adentro), por ser los más propensos a errores de indentación.

### 5. Cierre (7 min)

**Objetivo de la clase**
Resolver problemas de decisión aplicando `if`/`else`, `if` anidados y `elif` según corresponda a cada situación — reconociendo cuál estructura es la más adecuada en lugar de aplicar siempre la misma — trabajando en pareja y persistiendo ante errores de sintaxis e indentación.

**Pregunta 1 — Metacognición (escala 1-5)**
"¿Qué tan seguro/a te sientes decidiendo si un problema necesita `if` anidados, `elif`, o ambos combinados? (1 = no entendí nada, 5 = puedo explicárselo a otro)"

**Pregunta 2 — Actitud proyectada**
"¿En qué ejercicio te costó más decidir qué estructura usar, y cómo lo resolviste con tu pareja?"

## Decisiones de diseño relevantes

- **Sin Haz Ahora ni ICN:** es una clase de consolidación pura (mismo tipo que `clase-12-recordatorio`), no hay contenido nuevo que activar ni introducir — se reemplaza por una Apertura breve y se va directo a la Guiada.
- **Guiada con contexto neutro (descuentos por compra):** se evita el contexto de restricción de edad para las variables de la Guiada, siguiendo la convención de `generar-colab-clase/SKILL.md`.
- **Patrón "elif con if anidado adentro" como hilo conductor:** la Guiada lo enseña de forma simple (enunciado corto, 2 variables), y el Ejercicio 4 pide aplicarlo de forma independiente en un contexto distinto — mismo patrón, sin repetir el contexto de la Guiada.
- **Décimas escalonadas (+1 / +2):** el Ejercicio 4 vale el doble porque exige combinar dos estructuras y decidir el patrón correcto, no solo ejecutar sintaxis conocida.
- **Sin Ticket de Salida con preguntas de alternativas:** al no haber contenido nuevo que verificar con MCQ, el cierre se resuelve con las dos preguntas de metacognición/actitud a viva voz, igual que en `clase-12-recordatorio`.
- **Contextos sin repetir C13/C14:** streaming, básquetbol, viaje de estudio, batería, museo y ciber café ya se usaron en clases anteriores — esta clase usa delivery, gimnasio, furgón escolar, festival y descuentos por compra.
