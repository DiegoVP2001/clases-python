# Clase 27 — Evaluación Individual de Ciclos — Spec

**Fecha:** jueves 27 de agosto, 2026
**Modalidad:** individual, en Google Colab (entrega vía Classroom)
**Duración:** 75 minutos efectivos (de los 80 disponibles)
**Puntaje:** 100 pts, exigencia 50% (nota 4.0 al 50% de logro, escala 1.0–7.0)
**Temario:** `for` + `range()` (N°16), `for` anidado (N°20), `continue`/`break` (N°21.5), `while` (N°22)

## Renumeración curricular aplicada (2026-08-19)

Esta semana suma tres sesiones nuevas con número entero propio: **N°25** (Lunes estándar — Control Funciones, 24-ago), **N°26** (Simulacro — Ciclos, 25-ago) y esta misma evaluación, que pasa de decimal (N°22.5) a **N°27** entero — Diego decidió que las evaluaciones sumativas ya no usan numeración decimal, toman el siguiente entero libre como cualquier otra sesión. Todo lo planificado después corrió +3 respecto al Historial previo a esta semana (Strings 28/29, Listas 30/31, Integración 32, Evaluación F+S+L 32.5, Proyecto OA4 33-34, Proyecto OA5 35-38 — ver `Historial-Curricular.md`).

## Decisiones de formato

- **Sin autocheck**: evaluación sumativa, no hay verificación ✅/❌ en vivo. La corrección es posterior, con la pauta del Solucionario.
- **Sin Práctica Guiada** dentro del documento — va directo de instrucciones a los ítems.
- **⚠️ Restricción crítica confirmada por Diego (2026-08-19): CERO listas y CERO métodos de string, en ningún ítem.** Aunque el temario incluye `for`, ese `for` **siempre se enseñó sobre `range()`**, nunca iterando directo sobre una lista literal (`for x in lista:`) — Listas es contenido de N°30, muy posterior, y no se ha visto. Tampoco se ha visto ningún método de string (`.strip()`, etc. — eso es N°29). La v1 de este Spec violaba esto en 1A.2, 1B.3, 1B.4 (iteraban sobre listas) y en 2.1 (lista) y 2.2 (usaba `.strip()`) — todos corregidos en esta versión para usar solo `for`+`range()`, `if`, `while`, `continue`, `break`. Cualquier iteración futura de este Spec debe preservar esta restricción.
- **Sección 1 sin `input()`**: variables ya definidas o código con un bug ya escrito, para ir rápido armando o corrigiendo lógica de ciclos.
- **Con `input()` en Sección 2** (ítems 2.1, 2.3 y 2.4): siempre explícito en el enunciado el tipo de dato esperado (entero, con decimales, o texto exacto), en lenguaje natural — nunca nombrando `int()`/`float()`.
- **Contextos revisados contra las 6 clases foco** (`clase-16-for-range`, `clase-20-for-avanzado`, `clase-21-ayudantia-ciclos`, `clase-21b-continue-break`, `clase-22-while`, `clase-23-lunes-while-break`) para no repetir ninguno de los ya usados ahí (fútbol/Mundial, cine Cinemark, ajedrez-carpintería, riego Isla de Maipo, Brawl Stars, Vendimia, Fiesta Criolla, Free Fire, playlist de música, vóleibol, redes sociales/TikTok, Centro de Estudiantes, aforo gimnasio, taller de fotografía, notebooks del laboratorio, kiosco sopaipillas, impresora, kermés, encuesta CCAA, biblioteca, robot repartidor, máquina de reciclaje). Se usan: feria de emprendimiento del liceo, cohete de feria científica, club de atletismo, dron de fotografía aérea, karaoke escolar, campeonato de ajedrez cronometrado (distinto del taller de carpintería ya usado), taller de robótica (cuadrícula de sensores), estacionamiento del liceo, almacén de barrio de Isla de Maipo, coreografía de baile para el Aniversario, estación meteorológica, y caja fuerte de un escape room escolar.
- **Casos de prueba `hidden: true/false`** en cada ítem de Sección 2, más un ejemplo válido de referencia — mismo formato que Control/Dodona.
- **Cierre de actitud (Rigurosidad, Familia 2 — Evidencia + consecuencia):** última celda del notebook de estudiante, después del último ítem, sin nota:
  > "Cuenta un momento en que aplicaste rigurosidad durante la evaluación. ¿Qué habría pasado con tu resultado si no lo hacías justo ahí?"

---

## Distribución de puntaje y tiempo

**Actualizado 2026-08-19 (v3):** Diego pidió rebalancear la Sección 1 a **4 ítems de armar código + 4 de arregla el bug** (en vez de 2+6). Los dos bugs nuevos de la v2 (grilla de sensores, estacionamiento) pasaron a ser ítems "arma" (1A.3, 1A.4) en vez de "arregla el bug", conservando el mismo contexto y dificultad. Además, Diego pidió que la Sección 2 ("de desarrollo") pese más que la Sección 1 ("rápidas"), con puntaje distinto por ejercicio según su dificultad real — ya no 15 pts parejo. Sección 1 baja a 32 pts (8 ítems × 4 pts); Sección 2 sube a 68 pts, repartidos 15/17/18/18 según complejidad.

| Sección | Ítems | Puntos | Minutos |
|---|---|---|---|
| 1 — Ítems cortos | 8 (4 arma + 4 bug) | 32 | 30 |
| 2 — Programas completos | 4 | 68 | 45 |
| **Total** | **12** | **100** | **75** |

---

## Instrucciones generales (para el encabezado del Colab)

- Esta evaluación tiene 2 secciones y dura **75 minutos**.
- Trabaja en orden y administra tu tiempo.
- Entrega este notebook a través de **Google Classroom** antes de que termine la clase.
- El código debe ejecutarse sin errores. Si no terminas un ítem, deja lo que alcanzaste.
- Usa nombres de variables en **snake_case en español**.
- Cuando un ítem pida un dato con `input()`, el enunciado siempre aclara si es un número entero, un número con decimales, o una palabra exacta.
- **Prohibido** copiar código de compañeros.

---

## Sección 1 — Ítems cortos (32 pts, sin `input()`, sin autocheck)

Reorganizada en dos subsecciones: **1A — Arma el código** (4 ítems) primero, **1B — Arregla el bug** (4 ítems) después. El notebook de estudiante no rotula qué construcción se evalúa (ese metadato queda solo en el Solucionario). Todos los `for` iteran sobre `range()`, nunca sobre una lista.

### 1A.1 — Arma el `range()`, conteo regresivo (4 pts)

**Narrativa:** Para la feria científica del liceo, un grupo programó la cuenta regresiva del lanzamiento de su cohete a escala: debe imprimir los números del 10 al 1, uno por línea, terminando con "¡Despegue!".

```python
for numero in    # completar
    print(numero)

print("¡Despegue!")
```
Esperado:
```
10
9
8
...
1
¡Despegue!
```

### 1A.2 — Arma el `for` + `range()` con condición y contador (4 pts)

**Narrativa:** En el club de atletismo, un corredor entrena dando 10 vueltas a la pista, numeradas del 1 al 10. Cada vuelta múltiplo de 3, el entrenador le toma el tiempo con cronómetro. El programa debe contar cuántas veces le tomó el tiempo en total.

```python
tomas_de_tiempo = 0

for vuelta in range(1, 11):
        # completar: sumar 1 a tomas_de_tiempo si la vuelta es múltiplo de 3

print("Tomas de tiempo:", tomas_de_tiempo)
```
Esperado: `Tomas de tiempo: 3`.

### 1A.3 — Arma el `for` anidado, completa el rango interno (4 pts) — antes bug, ahora arma (v3)

**Narrativa:** En el taller de robótica se arma una cuadrícula de prueba de sensores de 3 filas por 3 columnas: el sistema debe imprimir en qué fila y columna está cada sensor.

```python
for fila in range(3):
    for columna in    # completar
        print("Sensor en fila", fila, "columna", columna)
```
Esperado:
```
Sensor en fila 0 columna 0
Sensor en fila 0 columna 1
Sensor en fila 0 columna 2
Sensor en fila 1 columna 0
Sensor en fila 1 columna 1
Sensor en fila 1 columna 2
Sensor en fila 2 columna 0
Sensor en fila 2 columna 1
Sensor en fila 2 columna 2
```

### 1A.4 — Arma el `while`, completa la condición de corte (4 pts) — antes bug, ahora arma (v3)

**Narrativa:** El estacionamiento del liceo tiene 5 cupos, numerados del 1 al 5. El sistema debe registrar la entrada de vehículos exactamente hasta llenar el estacionamiento, sin registrar ninguno de más.

```python
cupos_ocupados = 0
cupos_totales = 5

while    # completar
    cupos_ocupados = cupos_ocupados + 1
    print("Vehículo N°", cupos_ocupados, "estacionado.")
```
Esperado:
```
Vehículo N° 1 estacionado.
Vehículo N° 2 estacionado.
Vehículo N° 3 estacionado.
Vehículo N° 4 estacionado.
Vehículo N° 5 estacionado.
```

### 1B.1 — Bloque `range()` — Arregla el bug (4 pts)

**Narrativa:** El encargado de turnos de la feria de emprendimiento del liceo necesita atender exactamente a los primeros **5** puestos inscritos, numerados del 1 al 5.

**Bug:** `range(1, 5)` (falta el puesto N°5 — error de límite).

```python
for puesto in range(1, 5):
    print("Atendiendo puesto N°", puesto)
```
Corrección: `range(1, 6)`.

### 1B.2 — Bloque `while` — Arregla el bug (4 pts)

**Narrativa:** Un dron de fotografía aérea debe avisar cada vez que su batería baja un 10%, partiendo de 100%, hasta llegar a 0%.

**Bug:** dentro del `while` nunca se actualiza `bateria`, así que el ciclo nunca termina.

```python
bateria = 100

while bateria > 0:
    print("Batería:", bateria, "%")
    bateria - 10
```
Corrección: `bateria = bateria - 10` (o `bateria -= 10`).

### 1B.3 — Bloque `break` — Arregla el bug (4 pts)

**Narrativa:** El sistema del karaoke escolar recorre la cola de canciones numeradas del 1 al 6, buscando la canción número 4 (la primera disponible), y debe detenerse apenas la encuentra.

**Bug:** el `break` está fuera del `if`, así que el ciclo se corta en la primera vuelta sin haber encontrado la canción.

```python
for numero_cancion in range(1, 7):
    if numero_cancion == 4:
        print("Canción encontrada: N°", numero_cancion)
    break
```
Corrección: indentar `break` dentro del `if`.

### 1B.4 — Bloque `continue` — Arregla el bug (4 pts)

**Narrativa:** En el campeonato de ajedrez cronometrado, los jugadores llegan numerados del 1 al 6 a la mesa de resultados. Los jugadores con número **par** fueron descalificados por tiempo y no deben mostrarse; el sistema debe imprimir solo a los jugadores con número **impar**, que siguen en competencia.

**Bug:** la condición está invertida — salta (`continue`) a los impares, que son justo los que deben mostrarse.

```python
for numero_jugador in range(1, 7):
    if numero_jugador % 2 != 0:
        continue
    print("Jugador N°", numero_jugador, "sigue en competencia.")
```
Corrección: `if numero_jugador % 2 == 0:`.

---

## Sección 2 — Programas completos (68 pts, puntaje distinto por dificultad)

### 2.1 — `for` + `range()` con `input()` y acumulador (15 pts)

**Narrativa:** El almacén de barrio de Isla de Maipo va a registrar las ventas de sus primeras 5 transacciones del día. El programa debe pedir cada venta y, al terminar, informar el total vendido y cuántas ventas individuales superaron los \$5.000.

**El programa debe:**
- Usar un `for` con `range(5)` para repetir exactamente 5 veces.
- Por cada vuelta del `for`, pedir la venta correspondiente con `input()` (número entero).
- Acumular el **total vendido** en el día.
- Contar cuántas ventas fueron **superiores a \$5.000**.
- Imprimir ambos resultados con etiqueta al terminar.

**Pista 1 — Reutiliza la variable:** No necesitas crear una variable distinta para cada venta que pides — puedes usar el mismo nombre de variable en cada vuelta del ciclo, porque solo te interesa el valor que acabas de ingresar para sumarlo y compararlo, no guardarlos todos por separado.

Ejemplo válido: ingresos `3000`, `5500`, `12000`, `4200`, `8000` → total: `32700`, ventas sobre \$5.000: `3`.

Casos ocultos: las 5 ventas bajo el umbral (cuenta en 0), todas las ventas exactamente en \$5.000 (no cuentan, el umbral es estricto).

### 2.2 — `for` anidado + acumulador (17 pts) — extendido en v3

**Narrativa:** Para el número de baile del Aniversario, cada integrante de una fila debe gritar el número de su fila: la fila 1 tiene 1 integrante, la fila 2 tiene 2, y así sucesivamente hasta la fila indicada. Además, la profesora a cargo quiere saber cuántos integrantes participan en total en el número completo.

**El programa debe:**
- Usar `filas = 4`.
- Para cada fila (empezando en 1), imprimir el número de esa fila una vez por cada integrante que le corresponde (una impresión por línea).
- Contar el **total de integrantes** que participan en el número completo (la suma de todas las filas) e imprimirlo al final, con etiqueta.

**Por qué se extendió (2026-08-19):** en la v2, el código solución de este ejercicio era mucho más corto que el de 2.1, sintiéndose "como si no tuviera nada" en comparación — se le agregó este segundo requisito (acumulador sobre el ciclo anidado) para equilibrar la exigencia real entre ambos ejercicios.

Esperado:
```
1
2
2
3
3
3
4
4
4
4
Total de integrantes: 10
```

Casos ocultos: `filas = 1` (una sola línea `1` + `Total de integrantes: 1`), `filas = 6`.

### 2.3 — `while` con `input()` y centinela (18 pts)

**Narrativa:** Una estación meteorológica escolar recibe temperaturas ingresadas manualmente durante el día. El programa debe seguir pidiendo temperaturas (números que pueden tener decimales) hasta que se ingrese **-999**, que marca el fin del registro, y luego mostrar el promedio del día.

**El programa debe:**
- Pedir temperaturas repetidamente con `while`, hasta recibir `-999`.
- Acumular la suma y contar cuántas temperaturas válidas se ingresaron (sin contar el -999).
- Imprimir el **promedio** al terminar.
- Si no se ingresó ninguna temperatura válida antes del -999, imprimir un mensaje indicando que no hay datos, sin calcular el promedio (evita la división por cero).

**Pista 1 — Cómo se calcula un promedio:** el promedio de un conjunto de datos es la suma de todos los valores dividida por la cantidad de valores que sumaste — asegúrate de tener ambos datos disponibles al momento de calcularlo.

**Pista 2 — No olvides contar cuántas veces registraste:** además de ir sumando las temperaturas, necesitas otra variable que vaya guardando cuántas temperaturas válidas se han ingresado hasta el momento — ese conteo es justamente lo que necesitas para calcular el promedio y para saber si hubo o no datos.

Ejemplo válido: ingresos `18.5`, `20.0`, `19.2`, `-999` → promedio `19.23...`.

Casos ocultos: el primer ingreso ya es `-999` (mensaje de "no hay datos"), una sola temperatura antes del `-999`.

### 2.4 — `while` + `break`, intentos limitados (18 pts)

**Narrativa:** En el escape room del liceo, una caja fuerte tiene un código de 4 dígitos. Cada equipo dispone de **como máximo 5 intentos**; el programa debe cortar apenas alguien acierte el código, o informar que se acabaron los intentos si nadie lo logra.

**El programa debe:**
- Usar `codigo_correcto = 4271` y `intentos_maximos = 5`.
- Pedir un intento (número entero) repetidamente, contando cuántos van.
- Si el intento es correcto, felicitar y **cortar el ciclo** de inmediato (sin seguir pidiendo intentos).
- Si se agotan los 5 intentos sin acertar, informar que la caja quedó bloqueada.

**Pista 1 — Qué es un contador:** un contador es una variable que va sumando de a uno cada vez que ocurre algo (por ejemplo, cada intento que se realiza), para saber cuántas veces ha pasado ese algo.

**Pista 2 — Qué es un flag (bandera):** un flag o bandera es una variable que solo guarda Verdadero o Falso, y sirve para recordar si algo ya ocurrió (por ejemplo, si ya se acertó el código) para poder usar esa información más adelante en el programa, incluso fuera del ciclo.

Ejemplo válido: intentos `1234`, `4321`, `4271` → acierta al 3er intento, corta ahí (salida: "¡Código correcto! Caja abierta en el intento 3").

Casos ocultos: acierta en el primer intento, agota los 5 intentos sin acertar.

---

## Cierre de actitud (sin nota, celda final)

**Actitud:** Rigurosidad
**Pregunta (Familia 2 — Evidencia + consecuencia):**
> "Cuenta un momento en que aplicaste rigurosidad durante la evaluación. ¿Qué habría pasado con tu resultado si no lo hacías justo ahí?"
