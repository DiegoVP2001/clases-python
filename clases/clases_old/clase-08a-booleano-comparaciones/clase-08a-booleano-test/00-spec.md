# Clase 8a — Tipo Booleano y Comparaciones

**Estado:** Spec aprobada — 2026-05-21 (versión de prueba layouts v6)
**Clase Picuino:** N° 8 — El tipo Booleano (parcial)
**URL Picuino:** https://www.picuino.com/es/python-booleanos.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Clases 1–7 (print, input, variables, int y float, comentarios, palabras reservadas)
- **Contenidos nuevos:** Tipo booleano (`True`/`False`), operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`), `bool()`
- **Contenidos NO incluidos:** `and`, `or`, `not` — se verán en clase 8b
- **Contextos temáticos:** E-commerce / Mercado Libre, Cuenta RUT

## Objetivo

Demostrar el uso de valores booleanos y operadores de comparación en Python mediante la evaluación de condiciones con datos cotidianos, para identificar cuándo una expresión devuelve `True` o `False`.

## Propósito

Los programas necesitan evaluar condiciones todo el tiempo. Hoy aprenderás a escribir esas condiciones en Python y a entender qué responde el programa — verdadero o falso. Es la base de toda lógica en programación.

## Estructura de la clase

### 1. Haz Ahora

Actividad desconectada: lee cada situación y decide si es verdadera (V) o falsa (F). Escribe tu respuesta en la celda de abajo sin abrir el computador.

1. El PIN guardado es 4821. Ingresaste 4821. ¿Son iguales?
2. Tu contraseña es "Gato99". Escribiste "gato99". ¿Son distintas?
3. Tu app pesa 450 MB. Tienes 380 MB libres. ¿Cabe la app?
4. Llevas 2 intentos fallidos. El límite es 5. ¿Estás bajo el límite?
5. Tienes 16 años. La app exige 16 o más. ¿Puedes entrar?
6. Tu usuario tiene 12 caracteres. El máximo es 15. ¿Es válido?

En unos minutos revisaremos en conjunto las respuestas y veremos cómo Python evalúa cada una de estas situaciones.

### 2. Introducción al Contenido Nuevo

**Concepto 1: Tipo booleano**
- Definición: En Python existe un tipo especial llamado `bool` que solo puede tener dos valores: `True` (verdadero) o `False` (falso). Se escribe con la primera letra en mayúscula. Usa `type()` para confirmar el tipo.
- Ejemplo:
```python
tiene_stock = True
esta_agotado = False
print(tiene_stock)
print(type(tiene_stock))
```

**Concepto 2: Operadores de comparación**
Tipo: anatomia
- Definición: Son símbolos que comparan dos valores y devuelven `True` o `False`.
- **Expresión:** `saldo_cuenta_rut >= precio_audifono`
- **Partes:**
  - `saldo_cuenta_rut` | el dinero disponible en la Cuenta RUT
  - `>=` | el operador — define qué tipo de comparación se hace
  - `precio_audifono` | el precio del artículo que queremos comprar
  - Resultado | siempre `True` o `False` — nunca otro valor
- Idea clave: Una comparación siempre devuelve `True` o `False` — nunca otro valor.

**Demostración: Operadores == != >**
Subtítulo: Comparando saldo_cuenta_rut = 45000 con precio = 60000.
- Fila: == | 45000 == 60000 | False — no son iguales
- Fila: != | 45000 != 60000 | True — sí son distintos
- Fila: > | 45000 > 60000 | False — el saldo no supera el precio

**Demostración: Operadores < >= <=**
Subtítulo: Comparando saldo_cuenta_rut = 45000 con precio = 60000.
- Fila: < | 45000 < 60000 | True — el saldo es menor al precio
- Fila: >= | 45000 >= 60000 | False — el saldo no alcanza el precio
- Fila: <= | 45000 <= 60000 | True — el saldo está bajo o igual al precio

**Concepto 3: La función `bool()`**
- Definición: `bool()` convierte un número en su valor booleano. El `0` se convierte en `False`; cualquier otro número se convierte en `True`.
- Ejemplo:
```python
print(bool(0))    # False — cero es siempre False
print(bool(150))  # True — cualquier otro número es True
```

**Concepto 4: Booleanos en la vida real**
Tipo: analogia
- Definición: Las comparaciones de Python reflejan preguntas que evaluamos todos los días.
- **Analogía:** Lo que te preguntas tú, Python lo resuelve con `True` o `False`.
  - ¿Te alcanza el saldo para el artículo? | `saldo >= precio` → `True` o `False`
  - ¿Hay unidades disponibles en la tienda? | `unidades != 0` → `True` o `False`
  - ¿El envío llega en 5 días o menos? | `dias_envio <= 5` → `True` o `False`

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Escribir `true` o `false` en minúscula | `NameError: name 'true' is not defined` | Siempre con mayúscula: `True`, `False` |
| Usar `=` en vez de `==` para comparar | Asigna un valor en vez de comparar | Para comparar, usar doble igual `==` |
| Comparar `"60000" >= 60000` | `TypeError` — texto vs número | Convertir con `int()` antes de comparar |

### 3. Práctica Guiada

**Situación:** el usuario quiere comprar unos audífonos de $60.000 en Mercado Libre y paga con Cuenta RUT.

**Dinámica:** todos abren Colab, el profesor escribe en vivo y los estudiantes replican en su cuaderno de Colab.

**Pasos guiados:**
1. Crea una variable que registre el saldo en Cuenta RUT del usuario. Pídele el dato con `input()`.
2. Compara el saldo con $60.000 e imprime el resultado con un mensaje que explique qué se está preguntando.
3. Crea una variable que registre cuántas unidades quedan en stock. Pídela con `input()`, compara con 0 e imprime con texto explicativo.
4. Crea una variable que registre en cuántos días llega el pedido. Pídela con `input()`, compara con 5 e imprime con texto.
5. Crea una variable que identifique si el vendedor tiene historial de ventas. Usa `bool()` e imprime con texto explicativo.

**Resultado esperado:**
```
¿Te alcanza para el audífono? True
¿Hay unidades disponibles? True
¿Llega en 5 días o menos? True
¿El vendedor tiene historial de ventas? True
```

- Solución:
```python
saldo_cuenta_rut = int(input("¿Cuánto dinero tienes en la Cuenta RUT? "))
print("¿Te alcanza para el audífono?", saldo_cuenta_rut >= 60000)

unidades_en_stock = int(input("¿Cuántas unidades quedan en stock? "))
print("¿Hay unidades disponibles?", unidades_en_stock != 0)

dias_de_envio = int(input("¿En cuántos días llega? "))
print("¿Llega en 5 días o menos?", dias_de_envio <= 5)

ventas_realizadas = int(input("¿Cuántas ventas tiene el vendedor? "))
print("¿El vendedor tiene historial de ventas?", bool(ventas_realizadas))
```

### 4. Práctica Independiente

**Ejercicio 1 — Validar compra con Cuenta RUT**
Pide el saldo de la Cuenta RUT del usuario y el precio de un teclado inalámbrico. Imprime si el saldo alcanza para comprarlo, si el precio supera los $20.000, y si el saldo y el precio son exactamente iguales.

Ejemplo: si alguien ingresa un saldo de Cuenta RUT de $80.000 y un precio de teclado de $35.000, el programa imprime:
```
¿Te alcanza para el teclado? True
¿El teclado vale más de $20.000? True
¿Tu saldo es exactamente igual al precio? False
```

- Solución:
```python
saldo_cuenta_rut = int(input("¿Cuánto tienes en tu Cuenta RUT? "))
precio_teclado = int(input("¿Cuánto cuesta el teclado? "))
print("¿Te alcanza para el teclado?", saldo_cuenta_rut >= precio_teclado)
print("¿El teclado vale más de $20.000?", precio_teclado > 20000)
print("¿Tu saldo es exactamente igual al precio?", saldo_cuenta_rut == precio_teclado)
```

**Ejercicio 2 — Comparar ofertas**
Pide el precio del mismo producto en dos tiendas distintas de Mercado Libre. Imprime si la primera tienda es más barata, si los precios son iguales, y si la diferencia entre ambos precios supera los $5.000.

Ejemplo: si alguien ingresa un precio de $45.000 en la primera tienda y $55.000 en la segunda, el programa imprime:
```
¿La tienda 1 es más barata? True
¿Tienen el mismo precio? False
¿La diferencia supera los $5.000? True
```

- Solución:
```python
precio_tienda_1 = int(input("¿Cuánto cuesta en la tienda 1? "))
precio_tienda_2 = int(input("¿Cuánto cuesta en la tienda 2? "))
print("¿La tienda 1 es más barata?", precio_tienda_1 < precio_tienda_2)
print("¿Tienen el mismo precio?", precio_tienda_1 == precio_tienda_2)
diferencia = precio_tienda_2 - precio_tienda_1
print("¿La diferencia supera los $5.000?", diferencia > 5000)
```

**Ejercicio 3 — Historial del vendedor**
Pide la calificación del vendedor en estrellas (del 1 al 5) y la cantidad de ventas que ha realizado. Imprime si la calificación es de 4 estrellas o más, si tiene más de 10 ventas, y si tiene historial de ventas.

Ejemplo: si alguien ingresa una calificación de 5 estrellas y 20 ventas realizadas, el programa imprime:
```
¿El vendedor tiene 4 estrellas o más? True
¿Tiene más de 10 ventas? True
¿Tiene historial de ventas? True
```

- Solución:
```python
calificacion_vendedor = int(input("¿Cuántas estrellas tiene el vendedor (1-5)? "))
ventas_realizadas = int(input("¿Cuántas ventas tiene el vendedor? "))
print("¿El vendedor tiene 4 estrellas o más?", calificacion_vendedor >= 4)
print("¿Tiene más de 10 ventas?", ventas_realizadas > 10)
print("¿Tiene historial de ventas?", bool(ventas_realizadas))
```

### 5. Ticket de Salida

Escribe un programa que pregunte cuánto dinero tiene disponible el usuario en su Cuenta RUT y muestre si le alcanza para comprar unos audífonos de $60.000 en Mercado Libre.

Ejemplo: si alguien ingresa un saldo de Cuenta RUT de $45.000, el programa imprime:
```
¿Te alcanza para los audífonos ($60.000)? False
```

- Solución:
```python
saldo_cuenta_rut = int(input("¿Cuánto tienes en tu Cuenta RUT? "))
precio_audifono = 60000
print("¿Te alcanza para los audífonos ($60.000)?", saldo_cuenta_rut >= precio_audifono)
```

### Cierre

1. ¿Qué aprendiste a hacer hoy que antes no podías?
2. ¿En qué situación del Haz Ahora te equivocaste y por qué?
3. ¿Dónde podrías usar esto fuera de la clase?

## Decisiones de diseño relevantes

- La clase 8 de Picuino se dividió en 8a (comparaciones) y 8b (operadores lógicos) para no mezclar dos conceptos en una sola clase.
- Se eligió el contexto de e-commerce (Mercado Libre + Cuenta RUT) por ser cotidiano y relevante para estudiantes de 4to medio.
- El Haz Ahora es desconectado sin mostrar los operadores Python — eso vendría después.
- Las Demostraciones de los 6 operadores aparecen inmediatamente después del Concepto 2.
- Se incluye `type()` en el Concepto 1 para verificar el tipo `bool`.
- Cada ejercicio incluye un ejemplo de ejecución con inputs concretos y output esperado.
- Las soluciones están agrupadas al final del notebook en una sección separada.
