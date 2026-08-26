# Ejercicios adicionales — Clase 07: La función input()

## Introducción

Estos ejercicios te dan más práctica con `input()` y las conversiones `int()` y `float()`. Intenta resolver cada uno por tu cuenta antes de mirar la solución — ese es el momento donde más aprendes. Calcula unos 10-15 minutos por ejercicio base y un poco más para los desafíos.

---

## Ejercicio 1 — Distancia al estadio

**Nivel:** Práctica base

**Enunciado:**
Escribe un programa que le pregunte al usuario en qué ciudad está y a cuántos kilómetros queda el estadio. El programa debe mostrar un mensaje que combine ambos datos.

**Resultado esperado:**
```
¿En qué ciudad estás? Valparaíso
¿A cuántos km queda el estadio? 120
Desde Valparaíso el estadio queda a 120 km.
```

**Solución:**
```python
ciudad = input("¿En qué ciudad estás? ")
distancia_km = int(input("¿A cuántos km queda el estadio? "))
print("Desde", ciudad, "el estadio queda a", distancia_km, "km.")
```

---

## Ejercicio 2 — Calculadora de pasos

**Nivel:** Práctica base

**Enunciado:**
Escribe un programa que le pregunte al usuario cuántos pasos dio hoy y cuántos pasos tiene como meta diaria. El programa debe calcular cuántos pasos le faltan para llegar a la meta y mostrar el resultado.

**Resultado esperado:**
```
¿Cuántos pasos diste hoy? 6760
¿Cuál es tu meta diaria de pasos? 10000
Te faltan 3240 pasos para llegar a tu meta.
```

**Solución:**
```python
pasos_hoy = int(input("¿Cuántos pasos diste hoy? "))
meta_pasos = int(input("¿Cuál es tu meta diaria de pasos? "))
pasos_restantes = meta_pasos - pasos_hoy
print("Te faltan", pasos_restantes, "pasos para llegar a tu meta.")
```

---

## Ejercicio 3 — Precio del café

**Nivel:** Práctica base

**Enunciado:**
Escribe un programa que le pregunte al usuario el precio de un café (en pesos) y cuántas tazas toma al mes. El programa debe calcular y mostrar el gasto mensual y el gasto anual.

**Resultado esperado:**
```
¿Cuánto cuesta un café? 2500
¿Cuántas tazas tomas al mes? 3
Gasto mensual en café: $7500
Gasto anual en café: $90000
```

**Solución:**
```python
precio_cafe = int(input("¿Cuánto cuesta un café? "))
tazas_mes = int(input("¿Cuántas tazas tomas al mes? "))
gasto_mensual = precio_cafe * tazas_mes
gasto_anual = gasto_mensual * 12
print("Gasto mensual en café: $" + str(gasto_mensual))
print("Gasto anual en café: $" + str(gasto_anual))
```

---

## Ejercicio 4 — Promedio de notas

**Nivel:** Práctica base

**Enunciado:**
Escribe un programa que le pida al usuario tres notas de un ramo (pueden tener decimales, como 5.5 o 6.0). El programa debe calcular y mostrar el promedio.

**Resultado esperado:**
```
Nota 1: 5.5
Nota 2: 6.0
Nota 3: 6.0
Tu promedio es: 5.833333333333333
```

**Solución:**
```python
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
promedio = (nota_1 + nota_2 + nota_3) / 3
print("Tu promedio es:", promedio)
```

---

## Ejercicio 5 — Configuración de personaje ⭐

**Nivel:** Desafío opcional

**Enunciado:**
Escribe un programa que le pida al usuario el nombre de su personaje, su nivel base y sus puntos de bonificación. El programa debe calcular el nivel final (nivel base + puntos de bonificación) y mostrar una ficha completa con todos los datos.

**Pistas:**
El nivel base y la bonificación son números enteros. El nombre es texto — no necesita conversión.

**Resultado esperado:**
```
Nombre del personaje: Zara
Nivel base: 10
Puntos de bonificación: 5
=== FICHA DE PERSONAJE ===
Nombre: Zara
Nivel base: 10
Bonificación: 5
Nivel final: 15
```

**Solución:**
```python
nombre_personaje = input("Nombre del personaje: ")
nivel_base = int(input("Nivel base: "))
puntos_bonificacion = int(input("Puntos de bonificación: "))
nivel_final = nivel_base + puntos_bonificacion
print("=== FICHA DE PERSONAJE ===")
print("Nombre:", nombre_personaje)
print("Nivel base:", nivel_base)
print("Bonificación:", puntos_bonificacion)
print("Nivel final:", nivel_final)
```

---

## Ejercicio 6 — Tiempo de viaje ⭐

**Nivel:** Desafío opcional

**Enunciado:**
Escribe un programa que le pida al usuario la distancia de un viaje en kilómetros y la velocidad promedio en km/h. El programa debe calcular cuántas horas dura el viaje y cuántos minutos equivale eso.

**Pistas:**
La duración en horas es `distancia / velocidad`. Para pasar a minutos, multiplica las horas por 60.

**Resultado esperado:**
```
Distancia del viaje (km): 250
Velocidad promedio (km/h): 100
Duración del viaje: 2.5 horas
Eso equivale a 150.0 minutos.
```

**Solución:**
```python
distancia_km = float(input("Distancia del viaje (km): "))
velocidad_kmh = float(input("Velocidad promedio (km/h): "))
duracion_horas = distancia_km / velocidad_kmh
duracion_minutos = duracion_horas * 60
print("Duración del viaje:", duracion_horas, "horas")
print("Eso equivale a", duracion_minutos, "minutos.")
```
