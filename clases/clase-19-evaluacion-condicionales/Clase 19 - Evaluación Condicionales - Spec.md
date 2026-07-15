# Clase 19 — Evaluación Individual de Condicionales — Spec

**Fecha:** martes 21 de julio, 2026
**Modalidad:** individual, en Google Colab (entrega vía Classroom)
**Duración:** 75 minutos efectivos
**Puntaje:** 100 pts, exigencia 50% (nota 4.0 al 50% de logro, escala 1.0–7.0)
**Temario de referencia:** `clases/clase-17-ejercitacion-condicionales/Clase 17.5 - Evaluación Condicionales - Temario.md`

## Renumeración curricular aplicada

Esta evaluación pasa a ser **N° 19** (antes N° 17.5 en `Historial-Curricular.md`). Se aprobó reordenar:
- N° 18 = Reforzamiento (repaso Clase 17 + nueva guía rápida) — pendiente, otra sesión.
- N° 19 = esta evaluación.
- N° 20 = for avanzado (antes 18), N° 21 = while (antes 19), N° 21.5 = Evaluación de Ciclos (antes 19.5), y así sucesivamente hasta N° 33 (antes 31).

## Decisiones de formato

- **Sin "predicción de output sin ejecutar"**: se evalúa en computador, así que ese formato de prueba en papel no aplica (mismo criterio usado en el repaso de Clase 17.5).
- **Con `input()`**: a diferencia del repaso de Clase 17.5 (que no lo usaba), esta evaluación sí lo incluye en la Sección 2, siendo siempre explícito en el enunciado sobre el tipo de dato esperado (entero, con decimales, o texto exacto), en lenguaje natural — nunca nombrando `int()`/`float()` en la narrativa.
- **Sección 1 sin `input()`**: variables ya definidas, para ir rápido armando condiciones y arreglando bugs.
- **Sin autocheck**: a diferencia de la Ejercitación de Clase 17.5, esta es una evaluación sumativa — no hay verificación `✅/❌` en vivo. La corrección es posterior, con la pauta del Solucionario.
- **Sin Práctica Guiada** dentro del documento — va directo de instrucciones a los ejercicios.
- **Contextos revisados dos veces (2026-07-15)** para no repetir ninguno de Clase 17 (kiosco, teatro, ajedrez, transporte, taller de música, feria de emprendedores Isla de Maipo, fútbol escolar, biblioteca, e-sports, cine, laboratorio de computación, sala de ensayo, taller de robótica, maratón de baile), del apoyo individual, de Clase 14 ni de Clase 11/13. Se usan contextos de videojuegos, música/eventos, redes sociales, tecnología, deportes, Isla de Maipo (transporte) y ahorro en dólares. Detalle de los reemplazos en `Historial.md`.
- **Montos en pesos siempre enteros** (el peso chileno no usa decimales); cuando el ejercicio necesita probar `float()` con `input()`, se usa un contexto en dólares (Ejercicio 3) en vez de forzar decimales en pesos.
- **Enunciados de Sección 2 con los desenlaces enumerados**: cada ejercicio con más de 2 caminos posibles (Ejercicio 2, 3 y 4) incluye un punteo con el mensaje exacto de cada caso — no solo los 2 que aparecen en la tabla de ejemplos — para que el estudiante sepa qué imprimir en todos los caminos, no solo en los que se ilustran. Esto es información de comportamiento (qué debe pasar), nunca de implementación (cómo programarlo): nunca se nombra `elif`, anidamiento, ni ninguna estructura de control específica en el enunciado — solo se exige explícitamente el uso de `input()` para pedir los datos.

---

## Distribución de puntaje y tiempo

| Sección | Ítems | Puntos | Minutos |
|---|---|---|---|
| 1 — Ítems cortos | 7 | 30 | 21 |
| 2 — Programas completos | 4 | 70 | 54 |
| **Total** | **11** | **100** | **75** |

---

## Instrucciones generales (para el encabezado del Colab)

- Esta evaluación tiene 2 secciones y dura **75 minutos**.
- Trabaja en orden y administra tu tiempo.
- Entrega este notebook a través de **Google Classroom** antes de que termine la clase.
- El código debe ejecutarse sin errores. Si no terminas un ejercicio, deja lo que alcanzaste.
- Usa nombres de variables en **snake_case en español**.
- Cuando el ejercicio pida un dato con `input()`, el enunciado siempre aclara si es un número entero, un número con decimales, o una palabra exacta.
- **Prohibido** copiar código de compañeros.

---

## Sección 1 — Ítems cortos (30 pts, sin `input()`, sin autocheck)

Variables ya definidas. Reorganizada en dos subsecciones explícitas (mismo patrón que la Ejercitación de Clase 17): **1A — Arma la condición** primero, **1B — Arregla el bug** después. En el notebook de estudiante el ítem NO muestra "Bloque N" ni el patrón técnico (ej. `and` simple) — esos metadatos quedan solo en el Solucionario, para no regalar de antemano qué construcción se evalúa.

**Contextos revisados 2026-07-15:** 4 de los 7 ítems originales se cambiaron por ser demasiado parecidos a los de la Ejercitación de Clase 17 (mismo patrón de código/clave de acceso, mismo evento "feria de Isla de Maipo", ambos "elegibilidad de cuenta gamer", o ambos literalmente "robot"). Ver Historial.md para el detalle de qué se reemplazó.

### 1A.1 — Arma la condición, `and` simple (4 pts)

**Narrativa:** El concurso de fotografía de Instagram del liceo solo acepta la publicación de quien tenga la **cuenta pública** Y haya usado el **hashtag oficial** del concurso.

```python
cuenta_publica = True
uso_hashtag_oficial = False

participa_concurso =    # completar

print("¿Participa en el concurso?", participa_concurso)
```
Esperado: `False`.

### 1A.2 — Arma la condición, `var1 and (var2 or var3)` (4 pts)

**Narrativa:** Para entrar al backstage de un festival de música, se necesita la **pulsera VIP** Y además (tener **acreditación de prensa** O **invitación del staff**).

```python
tiene_pulsera_vip = True
tiene_acreditacion_prensa = False
tiene_invitacion_staff = True

puede_entrar_backstage =    # completar

print("¿Puede entrar al backstage?", puede_entrar_backstage)
```
Esperado: `True`.

### 1B.1 — Bloque 1 (Booleanos y comparaciones) — Arregla el bug (4 pts)

**Narrativa:** La máquina expendedora de bebidas del liceo solo entrega el producto cuando el monto insertado es exactamente igual al precio (no da vuelto).

**Bug:** `if monto_insertado = precio_bebida:` (falta el segundo `=`). Corrección: `==`.

```python
precio_bebida = 900
monto_insertado = 900

if monto_insertado = precio_bebida:
    mensaje_maquina = "Bebida entregada."
else:
    mensaje_maquina = "Monto incorrecto, no se entrega vuelto."

print(mensaje_maquina)
```

### 1B.2 — Bloque 3 (Análisis de condiciones, caso límite) — Arregla el bug (5 pts)

**Narrativa:** En el torneo de básquetbol del liceo, un equipo clasifica a semifinales cuando su puntaje **alcanza** el mínimo de la fase de grupos (no solo cuando lo supera).

**Bug:** usa `>` en vez de `>=`.

```python
puntaje_equipo = 18
puntaje_minimo_clasificacion = 18

if puntaje_equipo > puntaje_minimo_clasificacion:
    mensaje_torneo = "El equipo clasifica a semifinales."
else:
    mensaje_torneo = "El equipo queda eliminado."

print(mensaje_torneo)
```

### 1B.3 — Bloque 4 (if / else) — Arregla el bug (4 pts)

**Narrativa:** Antes de publicar un video en TikTok, el sistema revisa si pasó la verificación de derechos de autor.

**Bug:** falta el `:` al final del `if`.

```python
paso_revision_derechos = True

if paso_revision_derechos
    mensaje_tiktok = "Video publicado con éxito."
else:
    mensaje_tiktok = "Video retenido por derechos de autor."

print(mensaje_tiktok)
```

### 1B.4 — Bloque 5 (if anidados) — Arregla el bug (4 pts)

**Narrativa:** Un parlante inteligente revisa primero si está **conectado a internet**, y solo entonces si **reconoció el comando de voz**.

**Bug:** indentación incorrecta en la rama `if reconocio_comando:`.

```python
conectado_internet = True
reconocio_comando = False

if conectado_internet:
    if reconocio_comando:
    mensaje_parlante = "El parlante ejecuta la acción pedida."
    else:
        mensaje_parlante = "El parlante no entendió el comando."
else:
    mensaje_parlante = "El parlante está desconectado."

print(mensaje_parlante)
```

### 1B.5 — Bloque 6 (elif) — Arregla el bug (5 pts)

**Narrativa:** Una app de hábitos de estudio clasifica la racha de días seguidos estudiando en categorías, de la más exigente a la más básica.

**Bug:** condiciones en orden incorrecto (la más amplia va primero y tapa a las siguientes).

```python
racha_dias_estudio = 12

if racha_dias_estudio >= 3:
    mensaje_racha = "Racha en marcha: no la cortes."
elif racha_dias_estudio >= 7:
    mensaje_racha = "Buena constancia."
elif racha_dias_estudio >= 14:
    mensaje_racha = "Racha de élite."
else:
    mensaje_racha = "Recién empezando."

print(mensaje_racha)
```
Esperado (con el orden corregido y `racha_dias_estudio = 12`): `"Buena constancia."`

---

## Sección 2 — Programas completos (70 pts, con `input()`)

### Ejercicio 1 — Modo Fiesta de una playlist — if/else simple (12 pts, ~10 min)

**Narrativa:** Una playlist compartida arma automáticamente el "Modo Fiesta": cualquier canción con un nivel de energía alto entra a la lista; el resto se guarda para otro momento. Escribe el programa que, dado el nivel de energía de una canción, informe si entra o no al Modo Fiesta.

**El programa debe:**
- Pedir con `input()` el **nivel de energía de la canción** (**un número entero** entre 0 y 100)
- Verificar si la energía **alcanza el mínimo** para el Modo Fiesta (70)
- Mostrar un **mensaje distinto** según corresponda

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 El usuario ingresa: `70` | 📥 El usuario ingresa: `45` |
| 📤 Imprime: `¡Entra al Modo Fiesta! 🎉` | 📤 Imprime: `Se guarda para otro momento.` |

**Solución:**
```python
nivel_energia_cancion = int(input("Ingresa el nivel de energía de la canción (0 a 100): "))

if nivel_energia_cancion >= 70:
    print("¡Entra al Modo Fiesta! 🎉")
else:
    print("Se guarda para otro momento.")
```

### Ejercicio 2 — Micro a Talagante — if anidados (16 pts, ~13 min)

**Narrativa:** Para subir al micro que va desde Isla de Maipo hasta Talagante, el sistema revisa primero si la persona tiene pase escolar vigente; si no lo tiene, revisa si el saldo de su tarjeta bip alcanza para pagar el pasaje. Escribe el programa que, según esos datos, muestre cómo puede subir la persona.

**El programa debe:**
- Pedir con `input()` si tiene **pase escolar vigente** (la persona responde **exactamente** "si" o "no")
- Si **no** tiene pase, pedir además con `input()` el **saldo de la tarjeta bip** (un **número entero**, en pesos — el peso chileno no tiene decimales)
- Verificar primero el pase escolar; solo si no lo tiene, verificar si el saldo **alcanza** el costo del pasaje (\$800)
- Mostrar el mensaje que corresponda a cada uno de estos tres caminos:
  - Tiene pase escolar vigente → `"Sube gratis con su pase escolar."`
  - No tiene pase Y el saldo alcanza el pasaje → `"Paga el pasaje con la tarjeta bip."`
  - No tiene pase Y el saldo no alcanza → `"No le alcanza el saldo para el pasaje."`

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 El usuario ingresa: `si` | 📥 El usuario ingresa: `no` luego `500` |
| 📤 Imprime: `Sube gratis con su pase escolar.` | 📤 Imprime: `No le alcanza el saldo para el pasaje.` |

**Solución:**
```python
tiene_pase_escolar = input("¿Tiene pase escolar vigente? (si/no): ")

if tiene_pase_escolar == "si":
    print("Sube gratis con su pase escolar.")
else:
    saldo_tarjeta_bip = int(input("Ingresa el saldo de la tarjeta bip: "))
    if saldo_tarjeta_bip >= 800:
        print("Paga el pasaje con la tarjeta bip.")
    else:
        print("No le alcanza el saldo para el pasaje.")
```

### Ejercicio 3 — Ahorro semanal en dólares — elif con 4 categorías (18 pts, ~14 min)

**Narrativa:** Una alcancía digital lleva el registro de cuánto ahorras en dólares cada semana — varias personas en Chile prefieren ahorrar en esta moneda para protegerse de la fluctuación del peso. Escribe el programa que, dado el monto ahorrado, muestre el nivel correspondiente.

**El programa debe:**
- Pedir con `input()` el **monto ahorrado esta semana, en dólares** (**puede tener decimales**)
- Clasificar el monto en estos 4 niveles:
  - Menos de 10 dólares → `"Nivel: Recién empezando."`
  - Entre 10 y 29,99 dólares → `"Nivel: En camino."`
  - Entre 30 y 59,99 dólares → `"Nivel: Buen ahorro."`
  - 60 dólares o más → `"Nivel: ¡Excelente semana!"`

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 El usuario ingresa: `15` | 📥 El usuario ingresa: `62.5` |
| 📤 Imprime: `Nivel: En camino.` | 📤 Imprime: `Nivel: ¡Excelente semana!` |

**Solución:**
```python
monto_ahorrado_semana = float(input("Ingresa cuántos dólares ahorraste esta semana: "))

if monto_ahorrado_semana < 10:
    print("Nivel: Recién empezando.")
elif monto_ahorrado_semana < 30:
    print("Nivel: En camino.")
elif monto_ahorrado_semana < 60:
    print("Nivel: Buen ahorro.")
else:
    print("Nivel: ¡Excelente semana!")
```

### Ejercicio 4 — Sala de juego según tu rango — Bloque 7: elif + anidado (24 pts, ~17 min)

**Narrativa:** El sistema de un videojuego arma la sala de partida según el rango del jugador. Para el rango más alto, además revisa si el jugador tiene una racha de victorias activa, porque eso le da una sala especial. Escribe el programa que, dado el rango del jugador y —cuando corresponda— si tiene racha activa, muestre en qué sala queda.

**El programa debe:**
- Pedir con `input()` el **rango del jugador** (la persona responde **exactamente** una de estas palabras: "bronce", "plata" u "oro")
- Si el rango es **"oro"**, pedir además con `input()` si tiene **racha de victorias activa** (responde **exactamente** "si" o "no") — esta pregunta no se hace para los otros rangos
- Mostrar el mensaje que corresponda a cada uno de estos casos:
  - rango "bronce" → `"Sala de nivel bronce."`
  - rango "plata" → `"Sala de nivel plata."`
  - rango "oro" sin racha activa → `"Sala de nivel oro."`
  - rango "oro" con racha activa → `"Sala especial de racha activa."`
- **Nota de diseño:** no se le dice explícitamente al estudiante que use `elif` ni que anide la pregunta de la racha — solo se le exige usar `input()` para pedir los datos. Que descubra la estructura de control es parte de lo que se evalúa (el tercer caso, "bronce", perfectamente puede resolverse con un `else` en vez de un tercer `elif`).

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 El usuario ingresa: `oro` luego `si` | 📥 El usuario ingresa: `plata` |
| 📤 Imprime: `Sala especial de racha activa.` | 📤 Imprime: `Sala de nivel plata.` |

**Solución:**
```python
rango_jugador = input("Ingresa tu rango (bronce/plata/oro): ")

if rango_jugador == "oro":
    tiene_racha_activa = input("¿Tienes racha de victorias activa? (si/no): ")
    if tiene_racha_activa == "si":
        print("Sala especial de racha activa.")
    else:
        print("Sala de nivel oro.")
elif rango_jugador == "plata":
    print("Sala de nivel plata.")
else:
    print("Sala de nivel bronce.")
```

---

## Criterios de corrección (Revisión 3, 2026-07-15 — agregado al Solucionario)

El Solucionario está pensado como fuente de verdad para el agente que corrige (skill `revisar-evaluacion`), no solo para el profesor humano. La pauta prioriza la lógica de las condiciones y que el programa funcione por sobre la forma exacta del código, con un sistema de **3 niveles de descuento** aplicado a cada uno de los 11 ítems/ejercicios:

1. **✅ Acepta sin descuento** — variantes que logran lo mismo que la solución (nombres de variable, redacción del `print()`, estructuras equivalentes como `if/elif/else` vs. anidados, orden de definición de variables, etc.).
2. **⚠️ Descuenta 1-2 pts** — la lógica central está bien pero algo quedó impreciso (tipo de dato no exacto, caso límite no probado en los ejemplos mal cubierto, un `input()` de más). Tope explícito de 2 pts; ante la duda entre 0 y 1-2, se prefiere 0.
3. **❌ Descuenta la mayoría o todo el puntaje** — errores de lógica reales: operador de comparación incorrecto, rama faltante, tipo de dato mal leído que rompe el programa, código que no ejecuta.

El detalle específico de qué variación cae en cada nivel, ítem por ítem, vive en el bloque `🔍 Rúbrica flexible para este ítem` de cada solución en `Solucionario.ipynb` (no se duplica aquí para no mantenerlo en dos lugares).

Es un punto de partida ya calibrado a este solucionario — no reemplaza que la skill `revisar-evaluacion` siga afinando con Diego si aparece un patrón nuevo no cubierto.

---

## Archivos a generar

- `Clase 19 - Evaluación Condicionales - Evaluación.ipynb` — para estudiantes, sin soluciones.
- `Clase 19 - Evaluación Condicionales - Solucionario.ipynb` — pauta completa + puntaje, solo para el profesor.
- `generar_evaluacion.py` — script fuente de verdad (no editar los `.ipynb` a mano).
- `Clase 19 - Evaluación Condicionales - Historial.md` — registro de esta generación.
