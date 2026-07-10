# Clase 8b — Operadores Lógicos

**Estado:** En revisión — 2026-05-30
**Clase Picuino:** N° 8 — El tipo Booleano (segunda parte)
**URL Picuino:** https://www.picuino.com/es/python-booleanos.html

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Clases 1–8a (print, input, variables, int, float, comentarios, palabras reservadas, tipo booleano, operadores de comparación, `bool()`)
- **Contenidos nuevos:** Operadores lógicos (`and`, `or`, `not`)
- **Contenidos NO incluidos:** `if`/`else` — se verán en clase 9
- **Contextos temáticos:** Streaming y redes sociales (Spotify, Instagram, YouTube, Discord)

## Objetivo

Combinar operadores lógicos (`and`, `or`, `not`) con comparaciones para evaluar condiciones múltiples **con precisión**.

## Propósito

Spotify, Instagram, YouTube y Discord revisan varias condiciones a la vez antes de decidir qué mostrarte. Hoy aprenderás a escribir esas decisiones en Python. Lo que entrenas es la **precisión**: no saltarse ningún factor antes de actuar.

## Estructura de la clase

### 1. Haz Ahora (7 min)

Actividad desconectada: lee cada situación y decide si el usuario puede o no puede hacer lo que quiere. Escribe V (puede) o F (no puede) sin abrir el computador.

1. Para ver un video en YouTube necesitas tener internet Y que el video no sea privado. Tienes internet, pero el video es privado. ¿Puedes verlo?
2. Recibes una notificación en Discord si estás en el servidor O si te mencionaron directamente. No estás en el servidor, pero te mencionaron. ¿Recibes la notificación?
3. En Spotify una canción aparece en "Descubierto esta semana" si es nueva O si nunca la escuchaste. La canción es nueva pero ya la escuchaste. ¿Aparece?
4. Puedes publicar en Instagram si tu cuenta existe Y no está suspendida. Tu cuenta existe, pero está suspendida. ¿Puedes publicar?
5. Un video no se recomienda si tiene contenido sensible Y no activaste "modo sin restricciones". El video tiene contenido sensible, pero sí activaste el modo. ¿Se recomienda?

En unos minutos revisaremos las respuestas y veremos cómo Python evalúa exactamente estas situaciones.

**Respuestas esperadas:** F, V, V, F, V

### 2. Introducción al Contenido Nuevo (15 min)

**Concepto 1: Operador `and`**
- Definición: `and` combina dos condiciones y devuelve `True` solo si **ambas** son verdaderas. Si cualquiera es `False`, el resultado es `False`.

  | A | B | `A and B` |
  |---|---|---|
  | `True` | `True` | `True` |
  | `True` | `False` | `False` |
  | `False` | `True` | `False` |
  | `False` | `False` | `False` |

- Ejemplo:
```python
tiene_suscripcion = True
contenido_disponible = True
print("¿Puede ver el video?", tiene_suscripcion and contenido_disponible)
```
- Idea clave: Con `and`, TODAS las condiciones deben cumplirse.

**Concepto 2: Operador `or`**
- Definición: `or` combina dos condiciones y devuelve `True` si al menos una es verdadera. Solo devuelve `False` si ambas son `False`.

  | A | B | `A or B` |
  |---|---|---|
  | `True` | `True` | `True` |
  | `True` | `False` | `True` |
  | `False` | `True` | `True` |
  | `False` | `False` | `False` |

- Ejemplo:
```python
es_suscriptor = False
tiene_prueba_gratis = True
print("¿Puede acceder al contenido?", es_suscriptor or tiene_prueba_gratis)
```
- Idea clave: Con `or`, basta con que UNA condición se cumpla.

**Concepto 3: Operador `not`**
- Definición: `not` invierte el valor booleano de una condición. Si es `True`, lo convierte en `False`; si es `False`, lo convierte en `True`.
- Ejemplo:
```python
esta_en_modo_avion = True
print("¿Tiene conexión?", not esta_en_modo_avion)
```
- Idea clave: `not` voltea el resultado — convierte el sí en no y viceversa.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Confundir `and` con `or` | El programa autoriza o bloquea en los casos equivocados | Pregúntate: ¿deben cumplirse TODAS o ALGUNA? |
| Escribir `AND`, `OR` o `NOT` en mayúscula | `SyntaxError` | Siempre en minúscula: `and`, `or`, `not` |
| Olvidar que `not` afecta solo lo que sigue inmediatamente | Puede negar solo parte de la expresión | Usa paréntesis: `not (condicion_a and condicion_b)` |
| Escribir `"sí"` con tilde al responder el `input()` | `respuesta == "si"` devuelve `False` aunque la intención fuera decir que sí | Agrega la variante con tilde: `respuesta == "si" or respuesta == "sí"` |

### 3. Práctica Guiada (20 min)

**Situación:** verificar si un usuario puede acceder a contenido en una plataforma de streaming.

**Dinámica:** todos abren Colab, el profesor escribe en vivo y los estudiantes replican.

**Pasos guiados:**
1. Crea una variable que registre si el usuario tiene suscripción activa. Asígnale directamente un valor booleano.
2. Crea una variable que registre si el contenido está disponible en su país. Asígnale directamente un valor booleano.
3. Combina ambas condiciones para determinar si puede ver el video. Imprime el resultado con texto explicativo.
4. Crea una variable que registre si el video está bloqueado en tu país. Imprime si el video es accesible desde tu ubicación.
5. Crea una variable que registre si el usuario tiene prueba gratuita. Imprime si puede acceder de alguna forma (por suscripción o por prueba gratuita).

**Resultado esperado:**
```
¿Puede ver el video? True
¿El video es accesible desde tu país? True
¿Puede acceder de alguna forma? True
```

- Solución:
```python
tiene_suscripcion = True
contenido_disponible = True
print("¿Puede ver el video?", tiene_suscripcion and contenido_disponible)

bloqueado_en_pais = False
print("¿El video es accesible desde tu país?", not bloqueado_en_pais)

tiene_prueba_gratis = True
print("¿Puede acceder de alguna forma?", tiene_suscripcion or tiene_prueba_gratis)
```

### 4. Práctica Independiente (28 min)

**Ejercicio 1 — Publicar en Instagram**
Pide al usuario si tiene cuenta activa y si esa cuenta está suspendida (usando `input()` con respuesta "si" o "no"). Imprime si puede publicar en Instagram, y también si definitivamente NO puede publicar.

Ejemplo: si tiene cuenta activa pero la cuenta está suspendida, el programa imprime:
```
¿Puede publicar en Instagram? False
¿Está bloqueado/a para publicar? True
```

- Solución:
```python
respuesta_cuenta = input("¿Tienes cuenta activa? (si/no): ")
tiene_cuenta_activa = respuesta_cuenta == "si"

respuesta_suspension = input("¿Está suspendida? (si/no): ")
cuenta_suspendida = respuesta_suspension == "si"

print("¿Puede publicar en Instagram?", tiene_cuenta_activa and not cuenta_suspendida)
print("¿Está bloqueado/a para publicar?", not (tiene_cuenta_activa and not cuenta_suspendida))
```

**Ejercicio 2 — Notificación en Discord**
Pide al usuario si está en el servidor y si fue mencionado directamente. Imprime si recibirá una notificación (cualquiera de las dos condiciones es suficiente) y si está en el servidor pero no fue mencionado.

Ejemplo: si está en el servidor pero no fue mencionado, el programa imprime:
```
¿Recibe notificación? True
¿Está en el servidor pero sin mención? True
```

- Solución:
```python
respuesta_servidor = input("¿Estás en el servidor? (si/no): ")
esta_en_servidor = respuesta_servidor == "si"

respuesta_mencion = input("¿Te mencionaron directamente? (si/no): ")
fue_mencionado = respuesta_mencion == "si"

print("¿Recibe notificación?", esta_en_servidor or fue_mencionado)
print("¿Está en el servidor pero sin mención?", esta_en_servidor and not fue_mencionado)
```

**Ejercicio 3 — Recomendación en YouTube**
Pide cuántas reproducciones tiene un video y si tiene contenido sensible. Un video aparece como recomendado solo si no tiene contenido sensible Y tiene más de 1.000 reproducciones. Imprime si el video es recomendable.

Ejemplo: si tiene 5.000 reproducciones y no tiene contenido sensible, el programa imprime:
```
¿El video aparece como recomendado? True
```

- Solución:
```python
reproducciones = int(input("¿Cuántas reproducciones tiene el video? "))
respuesta_sensible = input("¿Tiene contenido sensible? (si/no): ")
tiene_contenido_sensible = respuesta_sensible == "si"

print("¿El video aparece como recomendado?", not tiene_contenido_sensible and reproducciones > 1000)
```

### 5. Ticket de Salida (8 min)

Escribe un programa que determine si un usuario puede escuchar una canción en Spotify. Para poder hacerlo necesita tener suscripción activa Y que la canción no esté bloqueada en su país. Pide ambos datos e imprime el resultado.

Ejemplo: si tiene suscripción activa pero la canción está bloqueada en su país, el programa imprime:
```
¿Puedes escuchar la canción? False
```

- Solución:
```python
respuesta_suscripcion = input("¿Tienes suscripción activa? (si/no): ")
tiene_suscripcion = respuesta_suscripcion == "si"

respuesta_bloqueo = input("¿La canción está bloqueada en tu país? (si/no): ")
cancion_bloqueada = respuesta_bloqueo == "si"

print("¿Puedes escuchar la canción?", tiene_suscripcion and not cancion_bloqueada)
```

### Cierre (5 min)

**Objetivo de la clase**
Combinar operadores lógicos (`and`, `or`, `not`) con comparaciones para evaluar condiciones múltiples **con precisión**.

**Pregunta 1 — Metacognición (escala 1-5)**
En una escala del 1 al 5, donde 1 es "nada seguro/a" y 5 es "se lo explico a alguien", ¿qué tan seguro/a estás de poder escribir una condición que combine `and`, `or` o `not` sin ayuda?

**Pregunta 2 — Actitud proyectada al futuro**
La precisión que entrenaste hoy va más allá del código. ¿En qué decisión importante de tu vida te gustaría revisar TODOS los factores antes de actuar, en vez de solo uno?

## Decisiones de diseño relevantes

- La clase 8 de Picuino se dividió en 8a (comparaciones) y 8b (operadores lógicos) para no mezclar dos conceptos en una sola clase.
- Se eligió el contexto de streaming y redes sociales (Spotify, Instagram, YouTube, Discord) por ser de alta pertinencia para estudiantes de 4to medio y distinto al e-commerce de 8a.
- La Práctica Guiada usa valores booleanos asignados directamente (`True`/`False`) para que el foco cognitivo esté en los operadores, no en la conversión de datos.
- La Práctica Independiente recupera `input()` usando la comparación `== "si"` — operador que los estudiantes ya conocen de 8a — para evitar la complejidad de `bool(int(input()))`.
- Las tablas de verdad se incluyen en el ICN como referencia visual para `and` y `or`.
- El Cierre incorpora los tres elementos nuevos del sistema: objetivo reimpreso, pregunta de metacognición (escala 1-5) y pregunta de actitud proyectada al futuro.
- Las soluciones se agrupan al final del notebook en una sección "📋 Soluciones" con `<details>` individuales.
