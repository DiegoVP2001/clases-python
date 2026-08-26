# Clase 11 — if else

**Estado:** Spec aprobada — 2026-06-05
**Clase Picuino:** N° 9 — Sentencia if else
**URL Picuino:** https://www.picuino.com/es/python-if-else.html

---

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:**
  - Booleanos y comparadores (`==`, `!=`, `<`, `>`, `<=`, `>=`) — clase 08a
  - Operadores lógicos (`and`, `or`, `not`) — clase 08b
  - Análisis de condiciones compuestas — clase 08c
  - `input()`, `int()`, `print()` con etiquetas — clases 1-7
- **Contenidos nuevos:**
  - Sentencia `if`
  - Cláusula `else`
  - Indentación obligatoria (4 espacios)
  - `IndentationError` y `SyntaxError` asociados
- **Contextos temáticos:** cumpleaños, cine en Santiago, transporte desde Isla de Maipo, TNE

---

## Objetivo

Demostrar el uso de `if / else` en Python para ejecutar bloques de código distintos según si una condición es verdadera o falsa, con atención.

---

## Propósito

> Cada vez que tomas una decisión —¿me alcanza la plata?, ¿llegué a tiempo?, ¿vale la pena ir?— estás ejecutando un `if / else` en tu cabeza. Hoy le vas a enseñar a Python a hacer eso por ti. Así funciona casi todo lo que automatiza decisiones: apps de banco, alarmas, semáforos inteligentes.

---

## Hilo narrativo

Un estudiante del Liceo Mario Bertero Cevasco celebra su cumpleaños yendo con amigos a Santiago a ver el estreno de *The Mandalorian & Grogu*. Se olvidó la TNE en casa, así que tiene que pagar tarifa completa con la tarjeta BIP. El código toma 5 decisiones en su nombre a lo largo del día.

---

## Estructura de la clase

### 1. Haz Ahora (8 min) — papel o pizarra

Hoy es el cumpleaños de un estudiante del Liceo Mario Bertero. Salió de Isla de Maipo a Santiago a ver ***The Mandalorian & Grogu*** 🎬 Pero el día estuvo lleno de decisiones difíciles...

Para cada situación, escribe en la celda de abajo **qué debería pasar** y **qué pasaría si NO se cumple**:

1. Tienes $1.800 en la tarjeta BIP. El pasaje completo ida y vuelta (sin TNE) cuesta $2.800. ¿Alcanza?
2. Llegas al paradero a las 13:10. El bus a Santiago salió a las 13:00. ¿Alcanzaste el bus?
3. Tienes $7.500 y la entrada al cine cuesta $8.000. ¿Puedes entrar?
4. Después de pagar la entrada te quedan $3.000. El combo de palomitas + bebida cuesta $4.500. ¿Te alcanza?

**Propósito:** activa que los estudiantes ya saben evaluar condiciones booleanas (unidades 08a-08c). Spoiler sutil: el código va a hacer exactamente lo que ellos acaban de razonar, solo que escrito en Python.

**Respuestas esperadas:** 1) No alcanza ($1.800 < $2.800) / 2) No alcanzó el bus (llegó a las 13:10, salió a las 13:00) / 3) No puede entrar ($7.500 < $8.000) / 4) No alcanza el combo ($3.000 < $4.500)

---

### 2. Introducción al Contenido Nuevo (15 min)

**Concepto 1: La sentencia `if`**
- Definición: ejecuta un bloque de código solo si la condición es `True`. Si la condición es `False`, el bloque se salta completamente.
- Ejemplo:
  ```python
  saldo_bip = 3000
  if saldo_bip >= 2800:
      print("Saldo suficiente. Te subes al bus.")
  # >> Saldo suficiente. Te subes al bus.
  ```
- Idea clave: el bloque indentado solo se ejecuta si la condición es `True`.

**Concepto 2: La cláusula `else`**
- Definición: define qué hacer cuando la condición del `if` es `False`. Solo uno de los dos bloques se ejecuta — nunca los dos al mismo tiempo.
- Ejemplo:
  ```python
  saldo_bip = 1800
  if saldo_bip >= 2800:
      print("Saldo suficiente. Te subes al bus.")
  else:
      print("No alcanza el saldo. Se olvidó la TNE y no hay plata.")
  # >> No alcanza el saldo. Se olvidó la TNE y no hay plata.
  ```
- Idea clave: `if` y `else` son dos caminos. El programa siempre toma uno, nunca los dos.

**Concepto 3: La indentación**
- Definición: los 4 espacios (o Tab) antes de cada línea del bloque le indican a Python qué instrucciones pertenecen al `if` o al `else`. Sin indentación, Python no puede ejecutar el programa.
- Ejemplo:
  ```python
  saldo_bip = 3000
  if saldo_bip >= 2800:
  print("Te subes al bus.")  # sin indentación → IndentationError
  
  # Corrección: agregar 4 espacios
  if saldo_bip >= 2800:
      print("Te subes al bus.")  # funciona
  ```
- Idea clave: la indentación no es estética, es sintaxis. Python la lee como parte del código.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Olvidar los `:` al final del `if` o `else` | `SyntaxError` | Agregar `:` al final de la condición y después de `else` |
| No indentar el bloque | `IndentationError` | Agregar 4 espacios o Tab antes de cada línea del bloque |
| Poner `else` sin `if` previo | `SyntaxError` | `else` siempre va después de un `if` |

---

### 3. Práctica Guiada (20 min) — Momentos 1 y 2

El curso construye los primeros dos momentos del día junto al profe.

**Situación:** Un estudiante del Liceo Mario Bertero Cevasco sale a celebrar su cumpleaños a Santiago. Primero tiene que alcanzar el bus de la 1, y luego verificar si tiene saldo BIP suficiente para pagar la tarifa completa (se olvidó la TNE en casa).

**Pasos guiados:**
1. Crea una variable que guarde la hora a la que salió el estudiante de su casa (número entero, formato 24h).
2. Verifica si esa hora es menor que 13.
3. Si la condición se cumple, muestra un mensaje que diga que alcanzó el bus de la 1.
4. Si no se cumple, muestra un mensaje que diga que lo perdió y tiene que esperar el siguiente.
5. Pide al usuario que ingrese su saldo actual en la tarjeta BIP (en pesos).
6. Guarda en una variable el costo del pasaje completo ida y vuelta sin TNE: $2.800.
7. Verifica si el saldo alcanza para cubrir ese costo.
8. Muestra el resultado con un mensaje que incluya ambos valores.

**Resultado esperado:**
```
¿A qué hora saliste de tu casa? (formato 24h): 12
¿Alcanzaste el bus? True  →  Alcanzaste el bus de la 1. ¡A Santiago!
¿Cuánto tienes en la tarjeta BIP? $3500
Saldo BIP: $3500  |  Pasaje sin TNE (ida+vuelta): $2800
¿Alcanza? True  →  Alcanza. Te subes al bus, aunque duele pagar tarifa completa.
```

- Solución:
```python
# Momento 1 — El bus de la 1
hora_salida = int(input("¿A qué hora saliste de tu casa? (formato 24h): "))
if hora_salida < 13:
    print("¿Alcanzaste el bus? True  →  Alcanzaste el bus de la 1. ¡A Santiago!")
else:
    print("¿Alcanzaste el bus? False  →  Lo perdiste. El siguiente sale en una hora.")

# Momento 2 — El saldo BIP sin TNE
saldo_bip = int(input("¿Cuánto tienes en la tarjeta BIP? $"))
costo_pasaje = 2800
if saldo_bip >= costo_pasaje:
    print("Saldo BIP: $" + str(saldo_bip) + "  |  Pasaje sin TNE (ida+vuelta): $" + str(costo_pasaje))
    print("¿Alcanza? True  →  Alcanza. Te subes al bus, aunque duele pagar tarifa completa.")
else:
    print("Saldo BIP: $" + str(saldo_bip) + "  |  Pasaje sin TNE (ida+vuelta): $" + str(costo_pasaje))
    print("¿Alcanza? False  →  No alcanza. O cargas la tarjeta o el cumpleaños se celebra en Isla de Maipo.")
```

---

### 4. Práctica Independiente (25 min) — Momentos 3 y 4

Los estudiantes trabajan solos. Los enunciados describen qué hacer sin revelar nombres de variables ni operadores.

**Ejercicio 1 — La entrada al cine**

Llegaron a Santiago. El estreno de *The Mandalorian & Grogu* cuesta $8.000 la entrada.

Escribe un programa que pregunte cuánta plata trae el estudiante para el cine. Si tiene suficiente para pagar la entrada ($8.000), muestra un mensaje que diga que puede entrar al estreno. Si no tiene suficiente, muestra que no puede entrar y tiene que esperar afuera.

Resultado esperado:
```
¿Cuánta plata traes para el cine? $10000
Plata disponible: $10000  |  Entrada: $8000
¿Alcanza? True  →  Puedes entrar al estreno. ¡Que empiece la película!
```

- Solución:
```python
plata = int(input("¿Cuánta plata traes para el cine? $"))
entrada = 8000
if plata >= entrada:
    print("Plata disponible: $" + str(plata) + "  |  Entrada: $" + str(entrada))
    print("¿Alcanza? True  →  Puedes entrar al estreno. ¡Que empiece la película!")
else:
    print("Plata disponible: $" + str(plata) + "  |  Entrada: $" + str(entrada))
    print("¿Alcanza? False  →  No alcanza. Afuera esperando a que cuenten el final.")
```

**Ejercicio 2 — El combo de palomitas**

Ya tiene la entrada. Ahora ve si le queda para el combo de palomitas grandes + bebida ($4.500), contando que ya gastó $8.000 en la entrada.

Escribe un programa que pregunte cuánta plata traía en total. Calcula cuánto le queda después de pagar la entrada ($8.000). Si lo que queda es suficiente para el combo ($4.500), muestra que puede pedir el combo. Si no, que tendrá que aguantar sin comer durante la película.

Resultado esperado:
```
¿Cuánta plata traías en total? $15000
Plata total: $15000  |  Después de entrada: $7000  |  Combo: $4500
¿Alcanza para el combo? True  →  ¡Palomitas aseguradas! Cumpleaños completo.
```

- Solución:
```python
plata_total = int(input("¿Cuánta plata traías en total? $"))
entrada = 8000
combo = 4500
plata_restante = plata_total - entrada
if plata_restante >= combo:
    print("Plata total: $" + str(plata_total) + "  |  Después de entrada: $" + str(plata_restante) + "  |  Combo: $" + str(combo))
    print("¿Alcanza para el combo? True  →  ¡Palomitas aseguradas! Cumpleaños completo.")
else:
    print("Plata total: $" + str(plata_total) + "  |  Después de entrada: $" + str(plata_restante) + "  |  Combo: $" + str(combo))
    print("¿Alcanza para el combo? False  →  Sin combo. Ver a Grogu con hambre nomás.")
```

---

### 5. Ticket de Salida (10 min) — Momento 5: la función

*Contexto:* La función de *The Mandalorian & Grogu* empieza a las 17:00. ¿El estudiante llegó a tiempo?

Escribe un programa que pregunte a qué hora llegaste al cine (número entero, formato 24h). Si llegaste antes de las 17:00, muestra que alcanzas a ver la película completa desde el inicio. Si no, muestra que te perdiste el principio de la historia.

Luego agrega una celda de texto (`+ Text`) con esta frase completa:
> "En mi programa, el `if` ejecuta [describe qué hace tu bloque if] y el `else` ejecuta [describe qué hace tu bloque else]."

- Solución:
```python
hora_llegada = int(input("¿A qué hora llegaste al cine? (formato 24h): "))
if hora_llegada < 17:
    print("¿Llegaste a tiempo? True  →  Alcanzas a ver la película completa desde el inicio.")
else:
    print("¿Llegaste a tiempo? False  →  Te perdiste el principio de la historia.")
```

---

### Cierre (5 min)

**Objetivo de la clase**
Demostrar el uso de `if / else` en Python para ejecutar bloques de código distintos según si una condición es verdadera o falsa, con atención.

**Pregunta 1 — Metacognición (escala 1-5)**
"¿Qué tan seguro/a te sientes escribiendo un `if / else` desde cero?, donde 1 es 'no entendí nada' y 5 es 'puedo explicárselo a otro'."

**Pregunta 2 — Actitud proyectada al futuro**
"Piensa en una decisión que tomas seguido —en tu casa, con tus amigos, en tu rutina. ¿Cómo la describirías como un `if / else`? ¿Qué condición se evalúa, qué pasa si se cumple y qué pasa si no?"

---

## Decisiones de diseño relevantes

- **Hilo narrativo único:** en vez de 4 ejercicios aislados, la clase cuenta un solo día del estudiante del Mario Bertero. Cada momento del hilo es un `if / else` con sentido narrativo propio. Esto hace que los ejercicios se sientan conectados y no arbitrarios.
- **TNE olvidada:** el detalle de olvidar la TNE es auténtico para estudiantes islamaipinos que viajan a Santiago. Obliga a calcular tarifa completa y hace el ejercicio del saldo BIP más realista.
- **Santiago como destino:** más coherente que Talagante para ir al cine en estreno. La distancia también justifica el problema del transporte.
- **Solo `if / else`, sin `elif`:** los operadores lógicos ya se vieron en 08b; en esta clase el foco es la bifurcación binaria y la indentación. `elif` va en la clase siguiente.
- **Indentación como foco explícito:** demo con error intencional en el ICN. El ticket pide describir en texto el `if` y el `else`, lo que fuerza comprensión conceptual además de sintáctica.
