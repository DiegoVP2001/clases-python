# Ejercicios adicionales — Clase 8b: Operadores Lógicos

## Introducción

Estos ejercicios te permiten seguir practicando `and`, `or` y `not` en situaciones distintas a las de la clase. Intenta resolver cada uno sin mirar la solución — si te atascas, lee el enunciado de nuevo antes de rendirte. El desafío final combina los tres operadores a la vez.

---

## Ejercicio 1 — Reserva de cancha de pádel

**Nivel:** Práctica base

**Enunciado:**
Crea las siguientes variables con exactamente estos valores:

- `cancha_disponible = True`
- `pago_confirmado = True`
- `socio_activo = False`

Una aplicación de canchas confirma la reserva solo si las tres condiciones se cumplen al mismo tiempo. Imprime si puedes reservar la cancha, y también si el problema específico es la membresía de socio.

**Resultado esperado:**
```
¿Puedes reservar? False
¿El problema es la membresía? True
```

**Solución:**
```python
cancha_disponible = True
pago_confirmado = True
socio_activo = False

print("¿Puedes reservar?", cancha_disponible and pago_confirmado and socio_activo)
print("¿El problema es la membresía?", not socio_activo)
```

---

## Ejercicio 2 — Acceso a una transmisión en vivo

**Nivel:** Práctica base

**Enunciado:**
Pide al usuario si tiene suscripción activa y si tiene un código de acceso gratuito (usa `input()` en ambos casos, con respuesta `"si"` o `"no"`).

El usuario puede ver la transmisión si cumple al menos una de las dos condiciones. Imprime si puede ver la transmisión y si definitivamente no puede verla.

**Resultado esperado:**
```
¿Tienes suscripción activa? (si/no): no
¿Tienes código de acceso gratuito? (si/no): si
¿Puede ver la transmisión? True
¿Definitivamente no puede verla? False
```

**Solución:**
```python
respuesta_suscripcion = input("¿Tienes suscripción activa? (si/no): ")
tiene_suscripcion = respuesta_suscripcion == "si"

respuesta_codigo = input("¿Tienes código de acceso gratuito? (si/no): ")
tiene_codigo_gratis = respuesta_codigo == "si"

print("¿Puede ver la transmisión?", tiene_suscripcion or tiene_codigo_gratis)
print("¿Definitivamente no puede verla?", not (tiene_suscripcion or tiene_codigo_gratis))
```

---

## Ejercicio 3 — Entrar a un servidor de juego en línea

**Nivel:** Práctica base

**Enunciado:**
Pide al usuario si tiene cuenta activa y si está baneado/a (usa `input()` en ambos casos, con respuesta `"si"` o `"no"`).

El usuario puede entrar al servidor si tiene cuenta activa y no está baneado/a. Imprime si puede entrar y si está definitivamente bloqueado/a para jugar.

**Resultado esperado:**
```
¿Tienes cuenta activa? (si/no): si
¿Estás baneado/a? (si/no): si
¿Puede entrar a jugar? False
¿Está bloqueado/a para jugar? True
```

**Solución:**
```python
respuesta_cuenta = input("¿Tienes cuenta activa? (si/no): ")
tiene_cuenta_activa = respuesta_cuenta == "si"

respuesta_ban = input("¿Estás baneado/a? (si/no): ")
esta_baneado = respuesta_ban == "si"

print("¿Puede entrar a jugar?", tiene_cuenta_activa and not esta_baneado)
print("¿Está bloqueado/a para jugar?", not (tiene_cuenta_activa and not esta_baneado))
```

---

## Ejercicio 4 — Compra en tienda en línea

**Nivel:** Práctica base

**Enunciado:**
Pide el saldo disponible (número entero) y si la tienda está en mantenimiento (respuesta `"si"` o `"no"`).

El usuario puede comprar si tiene más de $5.000 de saldo y la tienda no está en mantenimiento. Imprime si puede comprar y si hay algún problema que se lo impide.

**Pistas:**
Convierte el saldo a entero con `int()` antes de compararlo.

**Resultado esperado:**
```
¿Cuál es tu saldo disponible? 8000
¿La tienda está en mantenimiento? (si/no): si
¿Puede comprar? False
¿Hay algún problema para comprar? True
```

**Solución:**
```python
saldo = int(input("¿Cuál es tu saldo disponible? "))
respuesta_mantenimiento = input("¿La tienda está en mantenimiento? (si/no): ")
en_mantenimiento = respuesta_mantenimiento == "si"

print("¿Puede comprar?", saldo > 5000 and not en_mantenimiento)
print("¿Hay algún problema para comprar?", saldo <= 5000 or en_mantenimiento)
```

---

## Ejercicio 5 — Algoritmo de recomendaciones ⭐

**Nivel:** Desafío opcional

**Enunciado:**
Crea las siguientes variables con exactamente estos valores:

- `tiene_historial = True`
- `contenido_sensible = False`
- `es_tendencia = True`
- `bloqueado_en_region = False`

Un algoritmo recomienda un video si se cumple lo siguiente: el usuario tiene historial de reproducción **o** el video está en tendencias, **y** el video no tiene contenido sensible, **y** no está bloqueado en la región del usuario.

Imprime si el video es recomendable y si hay algún motivo para no recomendarlo.

**Pistas:**
Recuerda que `and` tiene mayor prioridad que `or`. Usa paréntesis para asegurarte de que `or` se evalúe primero donde corresponda.

**Resultado esperado:**
```
¿El video es recomendable? True
¿Hay motivo para no recomendarlo? False
```

**Solución:**
```python
tiene_historial = True
contenido_sensible = False
es_tendencia = True
bloqueado_en_region = False

print("¿El video es recomendable?", (tiene_historial or es_tendencia) and not contenido_sensible and not bloqueado_en_region)
print("¿Hay motivo para no recomendarlo?", contenido_sensible or bloqueado_en_region)
```
