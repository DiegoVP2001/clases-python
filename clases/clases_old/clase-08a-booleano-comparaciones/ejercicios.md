# Ejercicios adicionales — Clase 8a — Tipo Booleano y Comparaciones

## Introducción

Estos ejercicios te permiten seguir practicando comparaciones y valores booleanos en distintos contextos. Intenta resolver cada uno antes de ver la solución — la idea es que el programa te dé un resultado que puedas verificar. Los dos últimos son desafíos opcionales para quienes quieran ir más lejos.

---

## Ejercicio 1 — Biblioteca de música offline

**Nivel:** Práctica base

**Enunciado:**
Una app de streaming permite guardar hasta 150 canciones en el plan gratuito. Pide cuántas canciones tiene guardadas el usuario. Luego muestra si todavía cabe una canción más, si llegó exactamente al límite, y si superó el máximo permitido.

**Resultado esperado:**
```
Ejemplo: si alguien tiene 148 canciones guardadas, el programa imprime:
¿Cabe una canción más? True
¿Llegó exactamente al límite? False
¿Superó el máximo? False
```

**Solución:**
```python
canciones_guardadas = int(input("¿Cuántas canciones tienes guardadas? "))
print("¿Cabe una canción más?", canciones_guardadas < 150)
print("¿Llegó exactamente al límite?", canciones_guardadas == 150)
print("¿Superó el máximo?", canciones_guardadas > 150)
```

---

## Ejercicio 2 — Puntos en un videojuego

**Nivel:** Práctica base

**Enunciado:**
Un jugador acumula puntos durante la partida. El siguiente nivel requiere 5.000 puntos y el nivel élite requiere 10.000. Pide los puntos actuales del jugador. Muestra si desbloqueó el siguiente nivel, si llegó al nivel élite, y si tiene algún punto acumulado (usa `bool()`).

**Resultado esperado:**
```
Ejemplo: si alguien tiene 6.200 puntos, el programa imprime:
¿Desbloqueó el siguiente nivel? True
¿Llegó al nivel élite? False
¿Tiene puntos acumulados? True
```

**Solución:**
```python
puntos_jugador = int(input("¿Cuántos puntos tiene el jugador? "))
print("¿Desbloqueó el siguiente nivel?", puntos_jugador >= 5000)
print("¿Llegó al nivel élite?", puntos_jugador >= 10000)
print("¿Tiene puntos acumulados?", bool(puntos_jugador))
```

---

## Ejercicio 3 — Recarga de teléfono

**Nivel:** Práctica base

**Enunciado:**
El usuario quiere recargar su teléfono. La recarga mínima cuesta $1.000 y la recarga premium cuesta $5.000. Pide el saldo que tiene disponible. Muestra si le alcanza para la recarga mínima, si le alcanza para la premium, y si tiene algún saldo disponible (usa `bool()`).

**Resultado esperado:**
```
Ejemplo: si alguien tiene $3.500 en su cuenta, el programa imprime:
¿Alcanza para la recarga mínima ($1.000)? True
¿Alcanza para la recarga premium ($5.000)? False
¿Tiene algún saldo disponible? True
```

**Solución:**
```python
saldo_disponible = int(input("¿Cuánto saldo tienes en tu cuenta? "))
print("¿Alcanza para la recarga mínima ($1.000)?", saldo_disponible >= 1000)
print("¿Alcanza para la recarga premium ($5.000)?", saldo_disponible >= 5000)
print("¿Tiene algún saldo disponible?", bool(saldo_disponible))
```

---

## Ejercicio 4 — Licencia de conducir

**Nivel:** Práctica base

**Enunciado:**
En Chile se puede obtener licencia de conducir a los 18 años y licencia profesional a los 21. Pide la edad del usuario. Muestra si puede sacar la licencia de conducir, si puede sacar la licencia profesional, y si tiene exactamente la edad mínima para conducir.

**Resultado esperado:**
```
Ejemplo: si alguien tiene 18 años, el programa imprime:
¿Puede sacar licencia de conducir? True
¿Puede sacar licencia profesional? False
¿Tiene exactamente la edad mínima para conducir? True
```

**Solución:**
```python
edad_usuario = int(input("¿Cuántos años tienes? "))
print("¿Puede sacar licencia de conducir?", edad_usuario >= 18)
print("¿Puede sacar licencia profesional?", edad_usuario >= 21)
print("¿Tiene exactamente la edad mínima para conducir?", edad_usuario == 18)
```

---

## Ejercicio 5 — Velocidad de internet para streaming ⭐

**Nivel:** Desafío opcional

**Enunciado:**
Para ver video en HD se necesitan al menos 5 Mbps y para 4K al menos 25 Mbps. Pide la velocidad de internet del usuario en Mbps. Muestra si puede ver en HD, si puede ver en 4K, si su velocidad es exactamente la mínima para HD, y si tiene alguna conexión (usa `bool()`).

**Pistas:**
Recuerda que `bool()` devuelve `False` cuando el valor es 0. Piensa: ¿qué pasa si alguien ingresa una velocidad de 0 Mbps?

**Resultado esperado:**
```
Ejemplo: si alguien tiene 12 Mbps, el programa imprime:
¿Puede ver en HD? True
¿Puede ver en 4K? False
¿Tiene exactamente el mínimo para HD? False
¿Tiene conexión a internet? True
```

**Solución:**
```python
velocidad_internet = int(input("¿Cuál es tu velocidad de internet en Mbps? "))
print("¿Puede ver en HD?", velocidad_internet >= 5)
print("¿Puede ver en 4K?", velocidad_internet >= 25)
print("¿Tiene exactamente el mínimo para HD?", velocidad_internet == 5)
print("¿Tiene conexión a internet?", bool(velocidad_internet))
```

---

## Ejercicio 6 — Control de asistencia ⭐

**Nivel:** Desafío opcional

**Enunciado:**
Un ramo tiene 20 clases en el semestre. Para aprobar por asistencia se necesita haber asistido a más de la mitad. Pide cuántas clases asistió el estudiante. Muestra si aprobó la asistencia, si tuvo asistencia perfecta, si asistió exactamente a la mitad de las clases, y si asistió alguna vez (usa `bool()`).

**Pistas:**
La mitad de 20 clases es 10. "Más de la mitad" significa estrictamente mayor que 10, no igual.

**Resultado esperado:**
```
Ejemplo: si alguien asistió a 11 clases, el programa imprime:
¿Aprobó por asistencia? True
¿Asistencia perfecta? False
¿Asistió exactamente a la mitad? False
¿Asistió alguna vez? True
```

**Solución:**
```python
clases_asistidas = int(input("¿A cuántas clases asististe? "))
print("¿Aprobó por asistencia?", clases_asistidas > 10)
print("¿Asistencia perfecta?", clases_asistidas == 20)
print("¿Asistió exactamente a la mitad?", clases_asistidas == 10)
print("¿Asistió alguna vez?", bool(clases_asistidas))
```
