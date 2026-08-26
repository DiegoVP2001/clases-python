# Clase 07 — La función input()

**Estado:** Spec aprobada — 2026-05-16
**Clase Picuino:** N° 7 — La función input()
**URL Picuino:** https://www.picuino.com/es/python-input.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 90 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** clases 1-6 (Python básico, datos numéricos, variables, palabras reservadas, comentarios, `print()`)
- **Contenidos nuevos:** `input()`, conversión de tipos con `int()` y `float()`
- **Contextos temáticos:** videojuegos, Steam, perfil de jugador, suscripción gaming

## Objetivo

Aplicar la función `input()` con conversiones `int()` y `float()` en Python para construir programas que reciban datos del usuario por teclado y operen con ellos.

## Propósito

> Hasta ahora tus programas siempre usaban los mismos datos. Hoy aprenderás a pedirle información al usuario mientras el programa corre — como cuando Steam te pide tu nombre de usuario o una app de juegos te pregunta tu edad para calcular tu nivel.

## Estructura de la clase

### 1. Haz Ahora (7 min)

**Propósito:** Activar lo aprendido sobre `print()` y variables.

**Actividad:** Ver un programa con `print()` que muestra datos de un jugador ficticio (nombre, nivel, horas jugadas). Pregunta oral: *"¿Qué tendría que cambiar en este código para que mostrara TUS datos en vez de los de este jugador?"* — discusión breve, no código aún.

---

### 2. Introducción al Contenido Nuevo (18 min)

**Conceptos:**
1. `input()` detiene el programa y espera que el usuario escriba algo
2. Todo lo que devuelve `input()` es texto (`string`), aunque el usuario escriba un número
3. Para operar matemáticamente, hay que convertir: `int()` o `float()`
4. El error clásico: intentar sumar texto + número sin convertir (produce `TypeError`)

**Ejemplos a usar:**
```python
nombre_usuario = input("Ingresa tu nombre de usuario: ")
edad = int(input("Ingresa tu edad: "))
horas_semana = float(input("Horas jugadas esta semana: "))
```

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| `horas + 10` sin convertir | `TypeError` al sumar string con int | Envolver con `int()` |
| Olvidar guardar en variable | El valor se pierde | `nivel = input(...)` |
| `int()` con texto no numérico | `ValueError` | Ingresar solo números cuando se pide número |

---

### 3. Práctica Guiada (22 min)

**Situación:** Registro de perfil en un juego. El programa le pregunta al jugador su nombre de usuario, su edad y cuántas horas ha jugado esta semana. Al final calcula un `puntaje_rango` sumando `edad` + `horas_semana` y muestra un resumen del perfil.

**Variables:**
```python
nombre_usuario = input("Ingresa tu nombre de usuario: ")
edad = int(input("Ingresa tu edad: "))
horas_semana = float(input("Horas jugadas esta semana: "))
puntaje_rango = edad + horas_semana
```

**Pasos guiados:**
1. Primero solo `input()` con strings — mostrar el nombre con `print()`
2. Agregar conversión `int()` para la edad
3. Agregar conversión `float()` para las horas
4. Calcular `puntaje_rango` y mostrar el resumen completo

**Resultado esperado:**
```
=== PERFIL DE JUGADOR ===
Usuario: ProGamer99
Edad: 17
Horas esta semana: 12.5
Puntaje de rango: 29.5
```

---

### 4. Práctica Independiente (25 min)

**Ejercicio 1 — Calculadora de daño (videojuegos)**
El programa pide al usuario su `nivel_ataque` y el `nivel_defensa` del enemigo. Calcula el daño neto (`nivel_ataque - nivel_defensa`) y lo muestra.

Resultado esperado:
```
Daño causado: 8
```

**Ejercicio 2 — Costo de suscripción**
El programa pregunta cuántos meses quiere suscribirse a un servicio gaming y cuántos juegos del catálogo piensa descargar. Calcula el costo total usando precios fijos definidos en el código (`precio_mes` y `precio_juego`).

Resultado esperado:
```
Costo total de tu suscripción: $18500
```

**Ejercicio 3 — Presentación de equipo**
Pide nombre, país y personaje favorito a dos jugadores (6 `input()` en total). Muestra una presentación formateada de ambos. Solo strings — refuerza que no siempre hay que convertir.

Resultado esperado:
```
=== JUGADOR 1 ===
Nombre: Ana
País: Chile
Personaje favorito: Jinx

=== JUGADOR 2 ===
Nombre: Mateo
País: Argentina
Personaje favorito: Yasuo
```

---

### 5. Ticket de Salida (8 min)

**Tipo:** escritura de código mínimo

**Tarea:** *"Escribe un programa de exactamente 3 líneas que: (1) pida un número al usuario, (2) le sume 100, (3) muestre el resultado."*

**Entrega:** captura del output con un número ingresado, subida a Google Classroom.

---

### Cierre y metacognición (5 min)

1. ¿Cuándo es necesario convertir lo que devuelve `input()` y cuándo no?
2. ¿Qué diferencia hay entre un programa que siempre muestra lo mismo y uno que usa `input()`?
3. ¿En qué app o juego que uses tú se le piden datos al usuario?

## Decisiones de diseño relevantes

- Se descartó `math.gcd()` para no introducir importación de módulos, que excede el foco de la clase.
- El ejercicio 3 usa solo strings intencionalmente, para evitar que los estudiantes asuman que `input()` siempre requiere conversión.
- El ticket de salida está intencionalmente acotado a 3 líneas para que sea realizable en 8 minutos y evidencie el foco exacto: `input()` + conversión con `int()` + operación.
