# Clase 26 — Simulacro Ciclos

**Estado:** Spec aprobada — 2026-08-20
**Fecha:** martes 25 de agosto, 2026
**Clase Picuino:** N/A — clase de repaso/aplicación, prepara la Clase 27 (Evaluación individual de Ciclos, jueves 27-ago)

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** individual (a diferencia del resto de las clases regulares — simula las condiciones de la evaluación del jueves)
- **Plataforma:** Google Colab
- **Entrega:** no se entrega — es formativo, sin nota
- **Tema breve (Form):** N/A — este simulacro no tiene Ticket de Salida vía Google Form con nota asociada al curso, pero sí proyecta 3 preguntas de alternativas con el mismo mecanismo (ver sección 4)
- **Contenidos previos asumidos:** todo lo de las 6 clases foco de ciclos — `for`+`range()` (N°16), `for` anidado (N°20), `continue`/`break` (N°21.5), `while` (N°22), más la Ejercitación/Control del Lunes N°23.
- **Contenidos nuevos:** ninguno. Esta sesión es 100% repaso/aplicación.
- **Restricción heredada de la Evaluación (Clase 27):** cero listas, cero métodos de string, en ningún ítem — solo `for`+`range()`, `if`, `while`, `continue`, `break`.
- **Contextos usados:** torneo de videojuegos (Guiada), radio escolar y parque de diversiones (Sección 1 — arma), campamento de verano y app de estudio (Sección 1 — bugs), feria de talentos e invernadero escolar (Sección 2 — desarrollo). Ninguno se repite de la Evaluación (Clase 27) ni de las 6 clases foco.

## Objetivo

Aplicar `for`+`range()`, `for` anidado, `while` y `continue`/`break` en problemas estilo evaluación, para llegar con seguridad a la Evaluación de Ciclos del jueves.

## Propósito

> Hoy simulamos las condiciones de la evaluación del jueves: mismos tipos de problemas, mismo trabajo individual, pero sin nota. Practicar bajo esa presión controlada, y revisar juntos los errores al final, es lo que te permite llegar con más confianza al día real.

## Decisión de diseño central (por qué cada ítem no es un clon de la Evaluación)

Cada ítem de este simulacro aplica el **mismo concepto** que su equivalente en la Evaluación (Clase 27), pero con una **operación distinta** — no solo un contexto distinto — para que resolver la Evaluación no se reduzca a reconocer un problema ya visto. El detalle ítem por ítem queda documentado en "Decisiones de diseño relevantes" al final de este Spec.

---

## Estructura de la sesión (80 min)

### 1. Práctica Guiada — se resuelve en conjunto (12 min)

**🎮 Torneo de videojuegos — el puntaje más alto**

Un torneo de videojuegos registra los puntajes de la ronda de clasificación. Cada jugador ingresa su puntaje, uno por uno, y el sistema debe seguir recibiendo puntajes hasta que se ingresa **-1**, que marca el fin de la ronda. Al terminar, el sistema debe informar cuál fue el **puntaje más alto** registrado en toda la ronda.

**El programa debe:**
- Pedir puntajes repetidamente con `while`, hasta recibir `-1`.
- Ir comparando cada puntaje ingresado con el más alto registrado hasta el momento, y quedarse con el mayor.
- Imprimir el puntaje más alto al terminar.
- Si el primer ingreso ya es `-1` (no se registró ningún puntaje), informar que no hubo puntajes, sin mostrar un máximo.

<details>
<summary>💡 Pista — Cómo partir el máximo</summary>
Antes de tener ningún puntaje, todavía no existe un "máximo". Puedes usar el primer puntaje válido que se ingrese como punto de partida, y desde ahí ir comparando los que vengan después.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`850`<br>`1200`<br>`690`<br>`-1` | 📥 *El usuario ingresa:*<br>`-1` |
| 📤 *El programa imprime:*<br>`Puntaje más alto: 1200` | 📤 *El programa imprime:*<br>`No se registró ningún puntaje.` |

- Solución:
  ```python
  puntaje_ingresado = int(input("Ingresa el puntaje (o -1 para terminar): "))
  puntaje_maximo = None

  while puntaje_ingresado != -1:
      if puntaje_maximo is None or puntaje_ingresado > puntaje_maximo:
          puntaje_maximo = puntaje_ingresado
      puntaje_ingresado = int(input("Ingresa el puntaje (o -1 para terminar): "))

  if puntaje_maximo is None:
      print("No se registró ningún puntaje.")
  else:
      print("Puntaje más alto:", puntaje_maximo)
  ```

---

### 2. Sección 1 — Ítems cortos (sin `input()`, 15 min)

Dos ítems de armar código + dos de arreglar un bug. No se rotula qué construcción se evalúa en cada uno.

**1A.1 — Radio escolar**

La radio escolar transmite un anuncio publicitario cada 3 minutos, desde el minuto 0 hasta el minuto 21 de un bloque de transmisión. El programa debe imprimir en qué minutos se transmite un anuncio.

```python
for minuto in    # completar
    print("Anuncio en el minuto", minuto)
```
Esperado:
```
Anuncio en el minuto 0
Anuncio en el minuto 3
Anuncio en el minuto 6
...
Anuncio en el minuto 21
```
Completar: `range(0, 22, 3)`

<details>
<summary>💡 Pista</summary>
Un `range()` de tres números es `range(inicio, fin, paso)` — recuerda que el fin queda excluido, así que debe ser un número más que el último minuto que quieres incluir.
</details>

**1A.2 — Parque de diversiones**

El sistema de un parque de diversiones revisa las atracciones numeradas del 1 al 12, buscando la primera que tiene mantenimiento programado: la atracción N°9. Apenas la encuentra, debe avisar cuál es y **detener la búsqueda de inmediato**, sin seguir revisando las que quedan.

```python
for atraccion in range(1, 13):
    if atraccion == 9:
        print("Atracción en mantenimiento: N°", atraccion)
        # completar: detener la búsqueda
```
Esperado:
```
Atracción en mantenimiento: N° 9
```
Completar: `break`

<details>
<summary>💡 Pista</summary>
Piensa en la instrucción que corta un ciclo de inmediato, sin esperar a que termine de recorrer los valores que quedan.
</details>

**1B.1 — Campamento de verano (bug de `for` anidado)**

Un campamento de verano organiza 3 cabañas con 4 actividades cada una. El sistema debe imprimir cada actividad de cada cabaña, pero algo salió mal: solo se imprime la última actividad de cada cabaña.

```python
for cabana in range(1, 4):
    for actividad in range(1, 5):
        numero_actividad = actividad
    print("Cabaña", cabana, "- Actividad", numero_actividad)
```
**Bug:** el `print()` quedó fuera del ciclo interno (mal indentado), así que solo se ejecuta una vez por cabaña, con el último valor de `numero_actividad`.

Corrección: indentar `print()` dentro del ciclo interno.

<details>
<summary>💡 Pista</summary>
Cuenta cuántas veces se ejecuta el `print()` tal como está escrito, y compáralo con cuántas veces debería ejecutarse según el enunciado.
</details>

**1B.2 — App de estudio (bug de `continue`)**

Una app de estudio revisa 8 flashcards numeradas del 1 al 8 y debe contar cuántas son de **repaso rápido**: las de número **par**. Las impares se saltan con `continue`. Pero el contador de repaso rápido nunca sube como corresponde — siempre termina en 8.

```python
contador_repaso_rapido = 0

for numero_flashcard in range(1, 9):
    contador_repaso_rapido = contador_repaso_rapido + 1
    if numero_flashcard % 2 != 0:
        continue

print("Repaso rápido:", contador_repaso_rapido)
```
**Bug:** el contador sube **antes** de revisar si la flashcard es par o impar, así que el `continue` nunca llega a protegerlo — se cuenta cada flashcard, no solo las pares.

Corrección: mover el incremento de `contador_repaso_rapido` después del `if`/`continue`.

<details>
<summary>💡 Pista</summary>
Revisa el orden: ¿la línea que suma el contador se ejecuta antes o después de que el programa decida si esa flashcard se salta?
</details>

---

### 3. Sección 2 — Desarrollo (30 min)

**2.1 — Feria de talentos (`for` anidado + acumulador)**

La feria de talentos del liceo tiene 4 bloques de presentaciones. El bloque *i* tiene *i* presentaciones, y cada presentación dura 8 minutos. El programa debe calcular el **total de minutos** de presentaciones en toda la feria, y además contar en **cuántos bloques se superaron los 24 minutos** de duración.

**El programa debe:**
- Usar `bloques_totales = 4`.
- Para cada bloque (empezando en 1), calcular los minutos de ese bloque sumando 8 minutos por cada presentación que le corresponde, y acumular ese subtotal en el total general de la feria.
- Contar en cuántos bloques la duración del bloque superó los 24 minutos (estrictamente mayor).
- Imprimir el total de minutos de toda la feria y la cantidad de bloques que superaron los 24 minutos, cada uno con su etiqueta.

<details>
<summary>💡 Pista 1 — Reinicia el contador de minutos en cada bloque</summary>
Antes de empezar a contar las presentaciones de un bloque nuevo, la variable que acumula los minutos de ese bloque debe volver a partir en 0.
</details>

<details>
<summary>💡 Pista 2 — El contador de bloques se revisa después del ciclo interno</summary>
Recién cuando terminaste de sumar todas las presentaciones de un bloque sabes si ese bloque superó los 24 minutos.
</details>

📤 <em>El programa imprime:</em>
<pre>
Total de minutos de la feria: 80
Bloques que superaron los 24 minutos: 1
</pre>

- Solución:
  ```python
  bloques_totales = 4
  total_minutos_feria = 0
  bloques_sobre_24 = 0

  for bloque in range(1, bloques_totales + 1):
      minutos_bloque = 0
      for presentacion in range(1, bloque + 1):
          minutos_bloque = minutos_bloque + 8
      total_minutos_feria = total_minutos_feria + minutos_bloque
      if minutos_bloque > 24:
          bloques_sobre_24 = bloques_sobre_24 + 1

  print("Total de minutos de la feria:", total_minutos_feria)
  print("Bloques que superaron los 24 minutos:", bloques_sobre_24)
  ```

**2.2 — Invernadero escolar (`for`+`range()` con `input()`, clasificación doble)**

Un invernadero escolar registra la temperatura de sus primeros 6 sensores del día, ingresada manualmente uno por uno. El programa debe contar cuántas lecturas fueron **"normales"** (entre 18 y 28 grados, ambos límites incluidos) y cuántas fueron **"de alerta"** (fuera de ese rango).

**El programa debe:**
- Usar un `for` con `range(6)` para repetir exactamente 6 veces.
- Por cada vuelta, pedir la temperatura del sensor correspondiente con `input()` (puede tener decimales).
- Clasificar cada lectura como normal o de alerta, según el rango indicado.
- Imprimir ambos conteos al terminar, cada uno con su etiqueta.

<details>
<summary>💡 Pista 1 — Dos contadores, uno por categoría</summary>
Necesitas una variable que cuente las lecturas normales y otra distinta que cuente las de alerta — cada lectura suma a una sola de las dos.
</details>

<details>
<summary>💡 Pista 2 — Ambos límites incluidos</summary>
Una lectura de exactamente 18 o exactamente 28 grados cuenta como normal, no como de alerta.
</details>

**Resultado esperado:**

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 *El usuario ingresa:*<br>`20`<br>`30`<br>`18`<br>`28`<br>`15`<br>`22` | 📥 *El usuario ingresa:*<br>`15`<br>`35`<br>`20`<br>`25`<br>`10`<br>`40` |
| 📤 *El programa imprime:*<br>`Lecturas normales: 4`<br>`Lecturas de alerta: 2` | 📤 *El programa imprime:*<br>`Lecturas normales: 2`<br>`Lecturas de alerta: 4` |

- Solución:
  ```python
  normales = 0
  alerta = 0

  for sensor in range(6):
      temperatura = float(input("Temperatura del sensor (°C): "))
      if temperatura >= 18 and temperatura <= 28:
          normales = normales + 1
      else:
          alerta = alerta + 1

  print("Lecturas normales:", normales)
  print("Lecturas de alerta:", alerta)
  ```

---

### 4. Ticket de Salida (8 min)

3 preguntas de alternativas, mismo Google Form de siempre (https://forms.gle/sjRpbgmQzrpkEBsH9). Se proyectan una por una, sin revelar nada, y se completan recién al terminar la última.

**Pregunta 1:**
```python
for numero in range(2, 10, 2):
    print(numero)
```
¿Qué imprime este programa?
- A: 2, 4, 6, 8
- B: 2, 4, 6, 8, 10
- C: 2, 3, 4, 5, 6, 7, 8, 9
- D: 10, 8, 6, 4, 2

**Respuesta correcta:** A
**Justificación:** `range(2, 10, 2)` empieza en 2, avanza de 2 en 2, y se detiene antes de llegar a 10 — el límite superior queda excluido.

**Pregunta 2:**
```python
total = 0
for fila in range(1, 4):
    for columna in range(1, 3):
        total = total + 1
print("Total:", total)
```
¿Qué imprime este programa?
- A: Total: 3
- B: Total: 6
- C: Total: 2
- D: Total: 9

**Respuesta correcta:** B
**Justificación:** el ciclo interno se ejecuta 2 veces por cada una de las 3 vueltas del ciclo externo, así que el contador suma 1 un total de 3×2 = 6 veces.

**Pregunta 3:**
```python
numero = 0
while numero < 6:
    numero = numero + 1
    if numero % 2 == 0:
        continue
    if numero == 5:
        break
    print(numero)
```
¿Qué imprime este programa?
- A: 1, 3, 5
- B: 1, 2, 3, 4, 5
- C: 1, 3
- D: 1

**Respuesta correcta:** C
**Justificación:** `continue` salta el `print()` de los pares (2 y 4) pero no termina el ciclo; `break` sí lo termina, y ocurre en `numero == 5` antes de llegar a su `print()`, así que el 5 nunca se imprime. Solo se imprimen 1 y 3.

---

## Decisiones de diseño relevantes

- **Origen de esta sesión:** prepara la Evaluación individual de Ciclos (Clase 27, jueves 27-ago), aplicando problemas estilo evaluación dos días antes, con revisión conjunta de errores en la misma clase.
- **Sin nota, individual, sin autocheck durante el trabajo** — simula las condiciones reales de la evaluación del jueves, pero es formativo: no se entrega a Classroom con calificación. El `Solucionario.ipynb` es lo que se usa para la revisión conjunta al final de la clase.
- **Cada ítem aplica el mismo concepto que su equivalente en la Evaluación, con una operación distinta** (acordado con Diego el 2026-08-20, tras revisar ítem por ítem qué tan lejos quedaba cada uno):
  - **Guiada** (máximo vía `while`+centinela) vs. Evaluación 2.3 (promedio vía `while`+centinela): mismo esqueleto de ciclo (inevitable, es el concepto que se practica), pero la lógica interna cambia de acumular+dividir a comparar y quedarse con el mayor; el caso borde cambia de "división por cero" a "no hubo puntajes".
  - **1A.1** (radio, `range()` con paso) vs. Evaluación 1A.1 (cuenta regresiva descendente): `range()` de 3 parámetros ascendente con paso, no un paso negativo de a uno.
  - **1A.2** (parque de diversiones, arma el `break`) — la Evaluación nunca pide *escribir* un `break`, solo corregirlo; tarea sin equivalente directo en la prueba.
  - **1B.1** (campamento, bug de `for` anidado) — la Evaluación no tiene ningún bug de `for` anidado (en su v3 ese ítem pasó a ser "armar"); no hay clon posible.
  - **1B.2** (flashcards, bug de `continue`) vs. Evaluación 1B.4 (`continue` con condición invertida): mismo constructo y misma tarea (arreglar un bug de `continue`), pero el mecanismo del error es de **orden de instrucciones** (el contador queda sin protección del filtro), no de comparación invertida. Es el ítem que queda estructuralmente más cercano a la prueba — inevitable si se quiere seguir practicando `continue` como bug.
  - **2.1** (feria de talentos, `for` anidado + acumulador ponderado + contador de bloques) vs. Evaluación 2.2 (`for` anidado que imprime + cuenta impresiones): acumula un valor ponderado (minutos, no +1 por vuelta) y agrega un contador condicional a nivel del ciclo externo; no exige imprimir cada unidad.
  - **2.2** (invernadero, clasificación doble) vs. Evaluación 2.1 (suma total + contador de umbral): sin acumulador de suma, dos contadores de clasificación mutuamente excluyentes en su lugar.
  - `break` como bug (de la Evaluación) queda sin ítem propio en este simulacro — aparece en cambio como "arma" (1A.2) y en la Pregunta 3 del Ticket (predicción de salida combinando `continue` y `break`).
- **Contextos nuevos**, ninguno repetido de la Evaluación (torneo/atletismo/dron/karaoke/ajedrez/robótica/estacionamiento/almacén/baile/estación meteorológica/escape room) ni de las 6 clases foco (fútbol, cine, ajedrez-carpintería, riego, Brawl Stars, Vendimia, Fiesta Criolla, Free Fire, playlist música, vóleibol, redes sociales/TikTok, Centro de Estudiantes, aforo gimnasio, taller fotografía, notebooks laboratorio, kiosco sopaipillas, impresora, kermés, encuesta CCAA, biblioteca, robot repartidor, máquina de reciclaje).
- **Pistas desplegables en todos los ítems de práctica** (Guiada, Sección 1 y Sección 2), siguiendo el default vigente desde Clase 25 para cualquier serie de ejercicios sin nota.
- **Ticket de Salida con rotación de letra correcta** (A, B, C) y sin repetir la misma dos veces, cubriendo `range()` con paso, `for` anidado, y la combinación `continue`+`break` en un mismo `while`.
- **Sin Cierre de actitud del banco** (el que usan `Control.ipynb`/`Evaluación.ipynb`): este simulacro no es un instrumento formal de esa categoría, así que no aplica esa sección.
