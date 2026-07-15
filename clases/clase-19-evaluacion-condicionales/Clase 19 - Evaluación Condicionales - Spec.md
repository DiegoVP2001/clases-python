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
- **Contextos 100% nuevos**, sin repetir ninguno de Clase 17 (kiosco, teatro, ajedrez, transporte), del apoyo individual (tienda online, VIP, estacionamiento, cine, parque, delivery, biblioteca, gimnasio), de Clase 14 (viaje de estudio, cuotas, batería, reacción) ni de Clase 11/13 (pasaje, licencia, parque de juegos). Se usan contextos de videojuegos, música, redes sociales, tecnología/robots, deportes, Isla de Maipo (Vendimia, transporte) y finanzas simuladas.

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

Variables ya definidas. En "Arma la condición" el estudiante completa la línea que falta; en "Arregla el bug" corrige el único error del fragmento.

### Ítem 1.1 — Bloque 1 (Booleanos y comparaciones) — Arregla el bug (4 pts)

**Narrativa:** El servidor privado de Discord del club de videojuegos del liceo solo deja entrar a quien escribe el código de invitación correcto.

**Bug:** `if codigo_ingresado = codigo_correcto:` (falta el segundo `=`). Corrección: `==`.

```python
codigo_correcto = 4821
codigo_ingresado = 4821

if codigo_ingresado = codigo_correcto:
    mensaje_discord = "Acceso concedido al servidor."
else:
    mensaje_discord = "Código incorrecto."

print(mensaje_discord)
```

### Ítem 1.2 — Bloque 2 (Operadores lógicos) — Arma la condición, `and` simple (4 pts)

**Narrativa:** En la Feria de la Vendimia de Isla de Maipo, puede instalar su stand de comida quien tenga **permiso municipal** Y haya **pagado el arriendo** del espacio.

```python
tiene_permiso_municipal = True
pago_arriendo_stand = False

puede_instalar_stand =    # completar

print("¿Puede instalar el stand?", puede_instalar_stand)
```
Esperado: `False`.

### Ítem 1.3 — Bloque 2 (Operadores lógicos) — Arma la condición, `var1 and (var2 or var3)` (4 pts)

**Narrativa:** En el modo clasificatorio de un videojuego, puede entrar a la partida quien tenga la **cuenta verificada** Y además (haya alcanzado el **rango mínimo** O tenga una **invitación** de un jugador de rango alto).

```python
cuenta_verificada = True
alcanzo_rango_minimo = False
tiene_invitacion_rango_alto = True

puede_entrar_clasificatoria =    # completar

print("¿Puede entrar a la clasificatoria?", puede_entrar_clasificatoria)
```
Esperado: `True`.

### Ítem 1.4 — Bloque 3 (Análisis de condiciones, caso límite) — Arregla el bug (5 pts)

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

### Ítem 1.5 — Bloque 4 (if / else) — Arregla el bug (4 pts)

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

### Ítem 1.6 — Bloque 5 (if anidados) — Arregla el bug (4 pts)

**Narrativa:** Un robot aspirador doméstico revisa primero si está **encendido**, y solo entonces si **detecta un obstáculo** en el camino.

**Bug:** indentación incorrecta en la rama `if detecto_obstaculo:`.

```python
robot_encendido = True
detecto_obstaculo = False

if robot_encendido:
    if detecto_obstaculo:
    mensaje_robot = "El robot esquiva el obstáculo."
    else:
        mensaje_robot = "El robot sigue limpiando."
else:
    mensaje_robot = "El robot está apagado."

print(mensaje_robot)
```

### Ítem 1.7 — Bloque 6 (elif) — Arregla el bug (5 pts)

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

### Ejercicio 1 — Modo Fiesta de una playlist ⭐ Fácil — if/else simple (12 pts, ~10 min)

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

### Ejercicio 2 — Micro a Talagante ⭐⭐ Media — if anidados (16 pts, ~13 min)

**Narrativa:** Para subir al micro que va desde Isla de Maipo hasta Talagante, el sistema revisa primero si la persona tiene pase escolar vigente; si no lo tiene, revisa si el saldo de su tarjeta bip alcanza para pagar el pasaje. Escribe el programa que, según esos datos, muestre cómo puede subir la persona.

**El programa debe:**
- Pedir con `input()` si tiene **pase escolar vigente** (la persona responde **exactamente** "si" o "no")
- Si **no** tiene pase, pedir además con `input()` el **saldo de la tarjeta bip** (**puede tener decimales**, en pesos)
- Verificar primero el pase escolar; solo si no lo tiene, verificar si el saldo **alcanza** el costo del pasaje (\$800)
- Mostrar un **mensaje distinto** para cada uno de los tres caminos posibles

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
    saldo_tarjeta_bip = float(input("Ingresa el saldo de la tarjeta bip: "))
    if saldo_tarjeta_bip >= 800:
        print("Paga el pasaje con la tarjeta bip.")
    else:
        print("No le alcanza el saldo para el pasaje.")
```

### Ejercicio 3 — Ahorro semanal ⭐⭐ Media-alta — elif con 4 categorías (18 pts, ~14 min)

**Narrativa:** Una app ficticia de ahorro semanal clasifica cuánto guardaste esta semana en cuatro niveles, para motivarte a seguir ahorrando. Escribe el programa que, dado el monto ahorrado, muestre el nivel correspondiente.

**El programa debe:**
- Pedir con `input()` el **monto ahorrado esta semana** (**puede tener decimales**, en pesos)
- Clasificar el monto en **cuatro niveles**, del más bajo al más alto
- Mostrar un **mensaje claro** con el nivel obtenido

| Ejemplo 1 | Ejemplo 2 |
|---|---|
| 📥 El usuario ingresa: `8000` | 📥 El usuario ingresa: `31000.50` |
| 📤 Imprime: `Nivel: En camino.` | 📤 Imprime: `Nivel: ¡Excelente semana!` |

**Solución:**
```python
monto_ahorrado_semana = float(input("Ingresa el monto ahorrado esta semana: "))

if monto_ahorrado_semana < 5000:
    print("Nivel: Recién empezando.")
elif monto_ahorrado_semana < 15000:
    print("Nivel: En camino.")
elif monto_ahorrado_semana < 30000:
    print("Nivel: Buen ahorro.")
else:
    print("Nivel: ¡Excelente semana!")
```

### Ejercicio 4 — Salas de matchmaking (desafío) ⭐⭐⭐ Difícil — Bloque 7: elif + anidado (24 pts, ~17 min)

**Narrativa:** El sistema de emparejamiento de un videojuego arma las salas según el rango del jugador. Para el rango más alto, además revisa si el jugador tiene una racha de victorias activa, porque eso le da una sala especial. Escribe el programa que, dado el rango del jugador y —cuando corresponda— si tiene racha activa, muestre en qué sala queda.

**El programa debe:**
- Pedir con `input()` el **rango del jugador** (la persona responde **exactamente** una de estas palabras: "bronce", "plata" u "oro")
- Si el rango es **"oro"**, pedir además con `input()` si tiene **racha de victorias activa** (responde **exactamente** "si" o "no")
- Asignar la sala usando `elif` para los tres rangos, y anidar la pregunta de la racha solo dentro de la rama "oro"
- Mostrar un **mensaje distinto** con la sala asignada para cada camino posible

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

## Archivos a generar

- `Clase 19 - Evaluación Condicionales - Evaluación.ipynb` — para estudiantes, sin soluciones.
- `Clase 19 - Evaluación Condicionales - Solucionario.ipynb` — pauta completa + puntaje, solo para el profesor.
- `generar_evaluacion.py` — script fuente de verdad (no editar los `.ipynb` a mano).
- `Clase 19 - Evaluación Condicionales - Historial.md` — registro de esta generación.
