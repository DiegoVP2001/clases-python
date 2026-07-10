# Clase 9b — Análisis de Condiciones

**Estado:** Spec aprobada — 2026-06-02
**Clase Picuino:** N/A — clase adicional de consolidación (se inserta entre 8a y 8b)

## Contexto

- **Curso:** 3ro y 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Clases 1–8a (`print`, `input`, variables, `int`, `float`, comentarios, palabras reservadas, tipo booleano, operadores de comparación `==`, `!=`, `>`, `<`, `>=`, `<=`, `bool()`)
- **Contenidos nuevos:** Ninguno — clase de consolidación y análisis
- **Contenidos NO incluidos:** `and`, `or`, `not` — se verán en clase 10 (8b)
- **Contextos temáticos:** Reglas cotidianas (colegios, apps), gaming, streaming, comercio

## Objetivo

Analizar condiciones Python incorrectas o imprecisas para identificar el error lógico y corregirlo, con rigor.

## Propósito

Un programa no solo tiene que funcionar con los datos de prueba — tiene que funcionar con *todos* los datos posibles. Hoy aprenderás a leer una condición y encontrar exactamente el caso que la rompe. Es la diferencia entre un programa que *parece* funcionar y uno que *realmente* funciona.

## Estructura de la clase

### 1. Haz Ahora (7 min)

Actividad desconectada, sin computador. Lee cada situación y decide si la "regla" está bien escrita o si hay un caso donde fallaría. Escribe tu respuesta y justifícala en una oración.

1. El sistema del colegio dice: "Aprueba quien tenga **más de** 4.0". Una compañera tiene exactamente 4.0. ¿Aprueba?
2. Una app de descuento dice: "El descuento aplica si el precio es **menor a** \$10.000". El precio es exactamente \$10.000. ¿Aplica?
3. Un juego en línea dice: "Ganas el nivel si tu puntaje es **mayor a** 100". Tienes exactamente 100 puntos. ¿Ganaste?
4. Una sala de eventos dice: "Entran personas de **menos de** 18 años". Tienes 18 años. ¿Entras?

*En unos minutos veremos cómo Python evalúa estas mismas reglas — y por qué una sola palabra puede cambiar completamente el resultado.*

**Respuestas esperadas:** 1. No aprueba — "más de 4.0" en Python es `> 4.0`, y `4.0 > 4.0` es `False`. 2. No aplica — "menor a \$10.000" es `< 10000`, y `10000 < 10000` es `False`. 3. No ganaste — "mayor a 100" es `> 100`, y `100 > 100` es `False`. 4. No entras — "menos de 18" es `< 18`, y `18 < 18` es `False`.

### 2. Introducción al Contenido Nuevo (15 min)

**Concepto 1: Una condición correcta funciona para todos los datos, no solo los de prueba**
- Definición: Una condición que da el resultado correcto con los datos que usaste para probarla puede igual fallar con otros datos. Una condición es realmente correcta solo cuando no existe ningún dato que la haga dar un resultado equivocado.
- Ejemplo:
  ```python
  puntaje_jugador = 100
  print("¿Ganaste el nivel?", puntaje_jugador > 100)
  # >> ¿Ganaste el nivel? False
  ```
- Idea clave: "Funciona con mis datos" no significa "funciona siempre".

**Concepto 2: El caso límite — el dato que revela si la condición está mal**
- Definición: El *caso límite* es el valor exacto donde dos operadores similares (`>` y `>=`) dan resultados distintos. Si pruebas con ese valor y el resultado no es el esperado, encontraste el error.
- Ejemplo:
  ```python
  nota_alumno = 4.0
  print("¿Aprueba?", nota_alumno > 4.0)
  # >> ¿Aprueba? False
  print("¿Aprueba?", nota_alumno >= 4.0)
  # >> ¿Aprueba? True
  ```
- Idea clave: para encontrar el error, prueba siempre con el valor exacto del umbral.

**Concepto 3: Los errores de operador más frecuentes**
- Definición: Cada error de operador tiene exactamente un dato que lo delata.

| Operador usado | Operador correcto | Caso que lo revela |
|---|---|---|
| `>` | `>=` | cuando ambos valores son iguales |
| `<` | `<=` | cuando ambos valores son iguales |
| `>=` | `>` | cuando ambos valores son iguales |
| `==` | `!=` | cuando los valores son distintos |
| `!=` | `==` | cuando los valores son iguales |

- Idea clave: si sospechas del operador, prueba con el valor exacto del límite.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Probar solo con datos "cómodos" | La condición parece correcta pero falla en el límite | Siempre prueba con el valor exacto del umbral |
| Confundir `>` con `>=` | El programa excluye el caso exacto de empate | Pregúntate: ¿el umbral mismo cuenta o no? |
| Corregir el operador sin verificar | Puede que la nueva versión tampoco sea correcta | Vuelve a ejecutar con el caso límite y confirma |

### 3. Práctica Guiada (20 min)

**Situación:** Durante el CyberDay de esta semana, Steam activó un cupón de descuento automático para juegos con precio de \$15.000 o más. La plataforma permite que cualquier usuario consulte si el juego que quiere comprar califica para el cupón — solo ingresa el precio y el sistema responde.

Un jugador le contó a un amigo que su juego costaba exactamente \$15.000 y que el sistema le dijo que no calificaba — aunque las reglas del CyberDay decían que sí debería. Juntos escribirán el programa correcto.

**Pasos guiados:**
1. Según las reglas del CyberDay, ¿un juego de exactamente \$15.000 debería activar el cupón? ¿Por qué?
2. La frase es "precio de \$15.000 o más". ¿El límite exacto está incluido o excluido? ¿Qué operador lo representa mejor?
3. Para confirmar que tu programa funciona en todos los casos, ¿con qué tres precios distintos lo probarías?

Escribe el programa que usa la plataforma Steam: le pide el precio del juego al usuario e imprime si califica para el cupón CyberDay.

- Solución:
```python
precio_juego = int(input("¿Cuánto cuesta el juego? "))
print("¿Califica para el cupón CyberDay?", precio_juego >= 15000)
```

### 4. Práctica Independiente (25 min)

**Ejercicio 1 — Descuento en Discord**

Durante el CyberDay, una marca gaming activó un descuento exclusivo para administradores de servidores de Discord con 500 miembros o más. Cualquier admin puede verificar si su servidor califica ingresando el número de miembros. Una compañera que tiene exactamente 500 miembros en su servidor intentó acceder y el sistema se lo negó.

**Parte A — Análisis y escritura**
1. Según las reglas de la marca, ¿un servidor con exactamente 500 miembros debería calificar? ¿Por qué?
2. La frase es "500 miembros o más". ¿Qué operador la representa mejor?
3. ¿Con qué tres valores probarías tu programa para confirmar que el caso límite funciona?

Escribe el programa que le pide al admin el número de miembros de su servidor e imprime si califica para el descuento.

**Parte B — Escritura desde cero**
La marca también quiere avisar a los admins con menos de 100 miembros que aún no califican para ninguna promoción. Escribe ese programa.

- Solución Parte A:
```python
miembros_servidor = int(input("¿Cuántos miembros tiene tu servidor? "))
print("¿Califica para el descuento CyberDay?", miembros_servidor >= 500)
```

- Solución Parte B:
```python
miembros_servidor = int(input("¿Cuántos miembros tiene tu servidor? "))
print("¿Aún no califica para promociones?", miembros_servidor < 100)
```

**Ejercicio 2 — Oferta Spotify**

Para el CyberDay, Spotify activó 3 meses gratis del plan Premium para usuarios que llevaran 12 meses o más usando la versión gratuita. Cualquier usuario puede revisar si califica ingresando cuántos meses lleva en la app. Una usuaria con exactamente 12 meses esperaba recibir la oferta, pero el sistema le dijo que no calificaba.

**Parte A — Análisis y escritura**
1. Según las reglas de Spotify, ¿una usuaria con 12 meses exactos debería recibir la promoción? ¿Por qué?
2. La frase es "12 meses o más en la versión gratuita". ¿Qué operador la representa mejor?
3. ¿Con qué tres valores probarías tu programa para confirmar que el caso límite funciona?

Escribe el programa que le pide al usuario cuántos meses lleva en Spotify e imprime si califica para la oferta CyberDay.

**Parte B — Escritura desde cero**
Spotify también ofrece una semana gratis de Audiolibros solo para quienes tengan menos de 5 playlists guardadas, para que exploren nuevos contenidos. Escribe ese programa.

- Solución Parte A:
```python
meses_usuario = int(input("¿Cuántos meses llevas en Spotify? "))
print("¿Califica para los 3 meses gratis?", meses_usuario >= 12)
```

- Solución Parte B:
```python
playlists_guardadas = int(input("¿Cuántas playlists tienes guardadas? "))
print("¿Califica para la semana de Audiolibros?", playlists_guardadas < 5)
```

**Ejercicio 3 — Envío gratis en tienda gaming**

Durante el CyberDay, una tienda de merch gaming activó envío gratuito para pedidos de \$25.000 o más. Cualquier comprador puede verificar si su pedido califica antes de pagar, solo ingresando el monto total. Un comprador que gastó exactamente \$25.000 en una polera y stickers se encontró con que el sistema no le activó el envío gratuito.

**Parte A — Análisis y escritura**
1. Según las reglas de la tienda, ¿un pedido de exactamente \$25.000 debería tener envío gratuito? ¿Por qué?
2. La frase es "pedidos de \$25.000 o más". ¿Qué operador la representa mejor?
3. ¿Con qué tres valores probarías tu programa para confirmar que el caso límite funciona?

Escribe el programa que le pide al comprador el monto de su pedido e imprime si tiene envío gratuito.

**Parte B — Escritura desde cero**
La tienda también rechaza pedidos con menos de \$5.000 (monto mínimo para despachar). Escribe el programa que avisa si el pedido no alcanza el mínimo.

- Solución Parte A:
```python
total_pedido = int(input("¿Cuánto suma tu pedido? "))
print("¿Tienes envío gratuito?", total_pedido >= 25000)
```

- Solución Parte B:
```python
total_pedido = int(input("¿Cuánto suma tu pedido? "))
print("¿No alcanza el mínimo para despachar?", total_pedido < 5000)
```

### 5. Ticket de Salida (8 min)

Durante el CyberDay, cualquier persona puede usar el verificador de la Cuenta RUT para saber si le alcanza el saldo antes de confirmar una compra. La regla es simple: el saldo disponible tiene que ser igual o mayor al precio del producto. Una compañera quería comprar una polera que costaba exactamente \$15.000 y tenía exactamente \$15.000 en su cuenta. El verificador le dijo que no le alcanzaba.

1. ¿Debería alcanzarle con exactamente \$15.000 cuando el precio también es \$15.000? ¿Por qué?
2. La regla dice "saldo igual o mayor al precio". ¿Qué operador la representa mejor?

Escribe el verificador de la Cuenta RUT: le pide al usuario el precio del producto y su saldo disponible, e imprime si le alcanza para comprar.

- Solución:
```python
precio_producto = int(input("¿Cuánto cuesta el producto? "))
saldo_cuenta = int(input("¿Cuánto tienes en tu Cuenta RUT? "))
print("¿Te alcanza para comprar?", saldo_cuenta >= precio_producto)
```

### Cierre (5 min)

**Objetivo de la clase**
Analizar condiciones Python incorrectas o imprecisas para identificar el error lógico y corregirlo, con rigor.

**Pregunta 1 — Metacognición (escala 1-5)**
¿Qué tan seguro/a te sientes para, dado un programa con una condición incorrecta, encontrar el caso que la rompe y corregirla? Donde 1 es "todavía no lo veo claro" y 5 es "puedo explicárselo a un compañero".

**Pregunta 2 — Actitud proyectada al futuro**
El rigor significa no conformarse con que algo *parece* funcionar. ¿En qué otra área de tu vida — en otro ramo, en tu trabajo, en una decisión importante — te gustaría aplicar esa misma exigencia antes de dar algo por bueno?

## Decisiones de diseño relevantes

- Esta clase es adicional al currículo Picuino: se inserta entre 8a (comparadores) y 8b (operadores lógicos) para consolidar el análisis de condiciones antes de agregar complejidad.
- El Haz Ahora usa situaciones en lenguaje natural (sin Python) que anticipan exactamente el problema del caso límite — los estudiantes llegan al ICN con la intuición ya activada.
- El ICN no introduce sintaxis nueva: el "contenido nuevo" es la estrategia analítica (cómo encontrar el caso límite).
- La práctica guiada invierte el flujo habitual: en vez de construir desde cero, se parte de código existente con errores.
- Los 3 ejercicios usan contextos distintos (streaming, cupos, comercio) y el mismo tipo de error (`<` vs `<=`, `<=` vs `<`, `>=` vs `>`) para reforzar el patrón sin repetir contexto.
- El ticket usa el contexto Cuenta RUT / polera para activar memoria episódica de una clase anterior.
- El objetivo sigue el nuevo formato aprobado: `[verbo] [contenido] [para + propósito], [actitud]`.
