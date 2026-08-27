# Clase 30 — Strings: métodos para modificar y separar texto

**Estado:** Spec aprobada — 2026-08-27
**Clase Picuino:** N° 23 — Métodos de cadenas de texto (parcial — ver recorte abajo)
**URL Picuino:** https://www.picuino.com/es/python-textos-metodos.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual (por defecto)
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Strings — acceso por índice y rebanadas (Clase 28), recorrido de strings con `for` (Clase 29)
- **Contenidos nuevos:** Operadores `+`/`*` sobre strings, métodos `upper()`, `lower()`, `title()`, `strip()`, `replace()`, `split()` (con asignación múltiple)
- **Contextos temáticos:** Los Mellis Al Paso (negocio ancla real de Isla de Maipo, escenario único de toda la clase — Haz Ahora, ICN, Guiada e Independiente)

**Recorte respecto a la ficha Picuino N°23:** excluye `swapcase()` (sin aplicación real en el escenario) y `in`/`find()` (búsqueda de texto, movida a Clase 32). El formateo con f-strings (Picuino N°24) se sacó por completo del currículo cercano — ver `Historial-Curricular.md`, nota de renumeración 2026-08-26 (segunda pasada).

## Objetivo

Aplicar métodos de cadenas y operadores de texto para transformar datos desordenados en un formato limpio y estándar, con orden.

## Propósito

El orden es tomar datos desordenados y dejarlos siempre en el mismo formato estándar — la misma lógica que resuelve problemas reales en cualquier sistema que recibe información escrita de forma libre. Hoy lo trabajamos ayudando a Los Mellis Al Paso a poner en regla el formato de sus boletas, que el SII exige que cumplan.

## OAs

OA2, OA3.

## Estructura de la clase

### 1. Haz Ahora (6 min)

En Los Mellis los pedidos llegan por WhatsApp escritos como quiera cada cliente: algunos en mayúsculas, otros con espacios de más, algunos con errores de tipeo. Antes de emitir la boleta, alguien tiene que dejar cada pedido en el mismo formato, siempre. Los Mellis, sabiendo que ustedes programan, les pide ayuda — pero antes quiere que tengan clara la lógica:

1. Si un pedido llega con espacios de sobra al principio y al final, ¿qué parte del texto hay que sacar?
2. Si en la boleta el nombre del producto va con la primera letra de cada palabra en mayúscula, pero llegó escrito todo en minúscula, ¿qué hay que cambiarle?
3. Un pedido llega en un solo texto: producto y precio separados por una coma. ¿En qué dos partes se debería dividir antes de armar la boleta?
4. Si Los Mellis quiere repetir la palabra "GRACIAS" tres veces al pie de la boleta, ¿qué habría que hacer con ese texto?

**Respuestas esperadas:**
1. Los espacios de más al principio y al final.
2. Ponerle mayúscula a la primera letra de cada palabra (y minúscula al resto).
3. En el nombre del producto y en el precio, separando por la coma.
4. Repetir el texto "GRACIAS" tres veces seguidas.

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: Operadores `+` y `*` en strings**
- Definición: `+` une dos textos formando uno solo; `*` repite un texto una cantidad de veces. Son operadores (no llevan punto), no métodos.
- Ejemplo:
  ```python
  mensaje = "Gracias" + " " + "por tu compra"
  print(mensaje)
  linea = "-" * 20
  print(linea)
  ```
- Idea clave: `+` une texto, `*` lo repite — son operadores, no métodos con punto.

**Concepto 2: `upper()`, `lower()`, `title()`**
- Definición: métodos que devuelven una copia del texto en mayúsculas, en minúsculas, o con la primera letra de cada palabra en mayúscula. Se llaman con punto sobre el string.
- Ejemplo:
  ```python
  producto = "papas fritas"
  print(producto.upper())
  print(producto.title())
  ```
- Idea clave: `upper()`, `lower()` y `title()` no cambian la variable original — devuelven una copia nueva.

**Concepto 3: `strip()` y `replace()`**
- Definición: `strip()` elimina espacios sobrantes al inicio y al final del texto; `replace()` busca un fragmento de texto y lo reemplaza por otro.
- Ejemplo:
  ```python
  pedido = "  hamburguesa classica  "
  pedido_limpio = pedido.strip()
  pedido_corregido = pedido_limpio.replace("classica", "clásica")
  print(pedido_corregido)
  ```
- Idea clave: `strip()` limpia los bordes, `replace()` corrige o cambia contenido interno.

**Concepto 4: `split()` con asignación múltiple**
- Definición: `split()` corta un texto en partes según un separador y las devuelve; si se sabe que son exactamente dos partes, se pueden guardar directo en dos variables con una asignación múltiple.
- Ejemplo:
  ```python
  linea = "Papas Fritas,3400"
  producto, precio_texto = linea.split(",")
  print(producto)
  print(precio_texto)
  ```
- Idea clave: `split()` corta en el separador indicado; con asignación múltiple, cada parte queda en su propia variable.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Pensar que `strip()`/`upper()`/etc. modifican la variable original | El texto original queda igual y el programa sigue usando datos sin limpiar | Guardar el resultado en una variable nueva (o reasignar la misma) |
| Usar `+` para pegar texto y número sin convertir | `TypeError: can only concatenate str` | Convertir con `str()`, o imprimir con comas en vez de `+` |
| Esperar que `split(",")` devuelva más o menos partes de las que hay comas | Error al asignar a variables de más o de menos ("too many values to unpack") | Contar cuántas comas trae el texto antes de decidir cuántas variables usar |

### 3. Práctica Guiada (22 min)

Los Mellis les pasó un pedido real que llegó por WhatsApp: espacios de sobra al principio y al final, el producto y el precio juntos separados por una coma, y un error de tipeo en el nombre del producto. Antes de emitir la boleta necesitan dejarlo listo.

**El programa debe:**
- Guardar el pedido crudo tal como llegó.
- Sacar los espacios sobrantes del inicio y el final.
- Separar el texto en producto y precio usando la coma como referencia.
- Corregir el error de tipeo del nombre del producto.
- Dejar el nombre del producto con el formato de boleta (primera letra de cada palabra en mayúscula).
- Imprimir el producto ya formateado y el precio, cada uno con su etiqueta.

<details>
<summary>💡 Pista — orden de los pasos</summary>
Limpia los espacios de sobra antes de separar por la coma, y aplica el formato de mayúsculas recién al final, sobre el nombre ya corregido.
</details>

**Resultado esperado:**
```
Producto: Hamburguesa Clásica
Precio: 4500
```

- Solución:
  ```python
  pedido_crudo = "  HAMBURGUESA clasica,4500  "
  pedido_limpio = pedido_crudo.strip()
  producto_texto, precio_texto = pedido_limpio.split(",")
  producto_corregido = producto_texto.replace("clasica", "clásica")
  producto_formateado = producto_corregido.title()
  print("Producto:", producto_formateado)
  print("Precio:", precio_texto)
  ```

### 4. Práctica Independiente (16 min)

**Celda de configuración:**
```python
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)

import io, re, contextlib, unicodedata
from IPython import get_ipython

def _fuente_solucion(marca):
    for fuente in reversed(get_ipython().user_ns.get("In", [])):
        if fuente.strip().startswith(marca):
            return fuente
    return None

def _normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()

def _revisar(marca, esperadas):
    fuente = _fuente_solucion(marca)
    if fuente is None:
        print("⬜ No encuentro tu solución. Ejecuta la celda de arriba sin borrar")
        print("   su primera línea:", marca)
        return
    if not [l for l in fuente.splitlines()[1:] if l.strip()]:
        print("⬜ Tu celda de solución todavía está vacía. Escribe tu programa y ejecútala.")
        return
    salida = io.StringIO()
    try:
        with contextlib.redirect_stdout(salida):
            exec(compile(fuente, "<tu solución>", "exec"), {"__name__": "__main__"})
    except Exception as error:
        print("❌ Tu programa se detuvo con un error:", type(error).__name__, "-", error)
        return
    obtenidas = [l.rstrip() for l in salida.getvalue().splitlines() if l.strip()]
    correctas, primer_error = 0, None
    for i, esperada in enumerate(esperadas):
        obtenida = obtenidas[i] if i < len(obtenidas) else ""
        if _normalizar(obtenida) == _normalizar(esperada):
            correctas += 1
        elif primer_error is None:
            primer_error = (i + 1, esperada, obtenida)
    print("Líneas correctas:", correctas, "de", len(esperadas))
    if primer_error is None and len(obtenidas) == len(esperadas):
        print("✅ ¡Perfecto! Tu programa imprime exactamente lo que se pedía.")
        return
    if len(obtenidas) > len(esperadas):
        print("⚠️ Tu programa imprimió", len(obtenidas) - len(esperadas), "línea(s) de más.")
    if primer_error:
        numero, esperada, obtenida = primer_error
        print("❌ La primera diferencia está en la línea", numero)
        print("   Se esperaba:", esperada)
        print("   Tu programa dio:", obtenida if obtenida else "(nada)")

def verificar_ejercicio_0a():
    esperadas = ["Despedida: Gracias por tu compra", "Separador: ---"]
    _revisar("# Tu solución — Ejercicio 0a", esperadas)

def verificar_ejercicio_0b():
    esperadas = ["Producto: Papas Fritas", "Precio: 3400"]
    _revisar("# Tu solución — Ejercicio 0b", esperadas)

def verificar_ejercicio_1():
    esperadas = ["Pedido listo: Papas Fritas"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    esperadas = ["Pedido corregido: chorrillana especial"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    esperadas = ["Producto: Bebida Cola", "Precio: 1500"]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

def verificar_ejercicio_4():
    esperadas = ["Papas Fritas - $3400"]
    _revisar("# Tu solución — Ejercicio 4", esperadas)
```

**Ejercicio 0a — Práctica directa: operadores de texto**
Aplica el patrón base:

**El programa debe:**
- Definir dos variables de texto y unirlas con `+` en una sola línea de despedida para el cliente.
- Definir una variable que repita el texto `"-"` 3 veces usando `*`.
- Imprimir ambos resultados con su etiqueta.

**Resultado esperado:**
```
Despedida: Gracias por tu compra
Separador: ---
```

**Celda de verificación:**
```python
verificar_ejercicio_0a()
```

- Solución:
  ```python
  saludo = "Gracias" + " " + "por tu compra"
  separador = "-" * 3
  print("Despedida:", saludo)
  print("Separador:", separador)
  ```

**Ejercicio 0b — Práctica directa: `split()` con asignación múltiple**
Aplica el patrón base:

**El programa debe:**
- Guardar el texto `"Papas Fritas,3400"` en una variable.
- Separarlo en dos variables usando la coma como referencia, con una sola asignación múltiple.
- Imprimir cada variable con su etiqueta.

**Resultado esperado:**
```
Producto: Papas Fritas
Precio: 3400
```

**Celda de verificación:**
```python
verificar_ejercicio_0b()
```

- Solución:
  ```python
  linea = "Papas Fritas,3400"
  producto, precio = linea.split(",")
  print("Producto:", producto)
  print("Precio:", precio)
  ```

**Ejercicio 1 — Pedido con espacios y minúsculas**
Otro pedido llegó a Los Mellis con espacios de sobra y todo en minúscula. Antes de sumarlo a la boleta del día hay que dejarlo prolijo: sin espacios de más y con el nombre en el mismo formato que usan las demás boletas.

**El programa debe:**
- Guardar el pedido tal como llegó, con los espacios de más.
- Sacar los espacios sobrantes del inicio y el final.
- Dejar el nombre con la primera letra de cada palabra en mayúscula.
- Imprimir el resultado final con una etiqueta.

<details>
<summary>💡 Pista — orden de los métodos</summary>
Puedes aplicar los métodos uno después del otro, guardando el resultado de cada paso en su propia variable.
</details>

**Resultado esperado:**
```
Pedido listo: Papas Fritas
```

**Celda de verificación:**
```python
verificar_ejercicio_1()
```

- Solución:
  ```python
  pedido = "  papas fritas  "
  pedido_sin_espacios = pedido.strip()
  pedido_formateado = pedido_sin_espacios.title()
  print("Pedido listo:", pedido_formateado)
  ```

**Ejercicio 2 — Corregir un error de tipeo**
Un cliente escribió mal el nombre de un producto en su pedido. Antes de imprimir la boleta, Los Mellis necesitan corregir ese error para que quede como en su carta oficial.

**El programa debe:**
- Guardar el texto del pedido tal como llegó, con el error.
- Reemplazar la palabra mal escrita por la palabra correcta.
- Imprimir el pedido ya corregido con una etiqueta.

<details>
<summary>💡 Pista — qué reemplazar</summary>
El error está en una sola palabra dentro del texto; `replace()` busca exactamente ese fragmento.
</details>

**Resultado esperado:**
```
Pedido corregido: chorrillana especial
```

**Celda de verificación:**
```python
verificar_ejercicio_2()
```

- Solución:
  ```python
  pedido = "chorrillana especiall"
  pedido_corregido = pedido.replace("especiall", "especial")
  print("Pedido corregido:", pedido_corregido)
  ```

**Ejercicio 3 — Separar y formatear un pedido completo**
Los Mellis reciben pedidos completos en una sola línea de WhatsApp, con el producto y el precio juntos separados por una coma. Para armar la boleta necesitan separar ambas partes, y además el nombre del producto tiene que quedar con el formato prolijo de siempre.

**El programa debe:**
- Guardar la línea completa del pedido en una variable.
- Separarla en dos partes usando la coma como referencia, con asignación múltiple.
- Dejar el nombre del producto con el formato de boleta.
- Imprimir el nombre formateado y el precio, cada uno con su etiqueta.

<details>
<summary>💡 Pista — separar antes de formatear</summary>
Primero separa el texto completo en sus dos partes; recién después aplica el formato solo a la parte del producto.
</details>

**Resultado esperado:**
```
Producto: Bebida Cola
Precio: 1500
```

**Celda de verificación:**
```python
verificar_ejercicio_3()
```

- Solución:
  ```python
  linea_pedido = "bebida cola,1500"
  producto_texto, precio_texto = linea_pedido.split(",")
  producto_formateado = producto_texto.title()
  print("Producto:", producto_formateado)
  print("Precio:", precio_texto)
  ```

**Ejercicio 4 — Desafío: armar la línea completa de la boleta**
Los Mellis quieren ir un paso más allá: además de limpiar el pedido, arman la línea final que se imprime en la boleta, uniendo el nombre ya formateado con el precio y el símbolo \$. El pedido llegó con espacios de sobra y un error de tipeo en el nombre del producto.

**El programa debe:**
- Guardar el pedido tal como llegó.
- Sacar los espacios sobrantes.
- Separar el nombre del producto y el precio usando la coma.
- Corregir el error de tipeo del nombre.
- Dejar el nombre con el formato de boleta.
- Armar un solo texto final que una el nombre formateado, el precio y el símbolo \$, usando el operador de unión.
- Imprimir ese texto final.

**Resultado esperado:**
```
Papas Fritas - $3400
```

**Celda de verificación:**
```python
verificar_ejercicio_4()
```

- Solución:
  ```python
  pedido_crudo = "  papas ARROLLADAS,3400"
  pedido_limpio = pedido_crudo.strip()
  producto_texto, precio_texto = pedido_limpio.split(",")
  producto_corregido = producto_texto.replace("ARROLLADAS", "fritas")
  producto_formateado = producto_corregido.title()
  linea_boleta = producto_formateado + " - $" + precio_texto
  print(linea_boleta)
  ```

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
texto = "  hola MUNDO  "
print(texto.strip().title())
```
¿Qué imprime este programa?
- A: `"  hola MUNDO  "`
- B: `Hola Mundo`
- C: `HOLA MUNDO`
- D: `hola mundo`
**Respuesta correcta:** B
**Justificación:** `strip()` quita los espacios de los extremos, `title()` deja la primera letra de cada palabra en mayúscula y el resto en minúscula.

**Pregunta 2:**
```python
pedido = "Papas Fritas,3400"
producto, precio = pedido.split(",")
print(precio)
```
¿Qué imprime este programa?
- A: `Papas Fritas,3400`
- B: `Papas Fritas`
- C: `3400`
- D: Error, porque `split()` no se puede guardar en dos variables
**Respuesta correcta:** C
**Justificación:** `split(",")` corta el texto en dos partes por la coma; la asignación múltiple guarda cada parte en su variable en orden, así que `precio` queda con `"3400"`.

**Pregunta 3:**
```python
separador = "-" * 4
mensaje = "Total" + separador
print(mensaje)
```
¿Qué imprime este programa?
- A: `Total----`
- B: `Total-4`
- C: `TotalTotalTotalTotal`
- D: Error, porque no se puede sumar texto con texto
**Respuesta correcta:** A
**Justificación:** `*` repite el texto `"-"` 4 veces (`"----"`), y `+` une ese resultado con `"Total"`.

### Cierre (5 min)

**Objetivo de la clase:** Aplicar métodos de cadenas y operadores de texto para transformar datos desordenados en un formato limpio y estándar, con orden.

**Pregunta 1 — Metacognición (escala 1-5):** Del 1 al 5, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro", ¿cuánto entendiste el objetivo de hoy?

**Pregunta 2 — Actitud proyectada al futuro:** Piensa en algún trabajo, estudio o proyecto que te imagines a futuro: ¿en qué situación vas a necesitar tomar datos desordenados y dejarlos siempre en el mismo formato?

## Decisiones de diseño relevantes

- **Los Mellis Al Paso como negocio ancla único** (decisión consciente de Diego, aparta la regla 3 de "contextos variados" del `CLAUDE.md` raíz — ver `referencia-empresas-isla-de-maipo`). Narrativa: su sistema de boletas está fallando y el SII exige que el formato cumpla ciertas reglas. El problema es ficticio; el negocio, real.
- **Propósito con compañía real (piloto)** — primer caso de este formato, ver `disenar-clase/SKILL.md` Paso 3. Pendiente que Diego confirme al cerrar esta clase si se generaliza a default.
- **Recorte de contenido:** se excluyó `swapcase()` (sin aplicación real en el escenario), `in`/`find()` (movidos a Clase 32 — habilidad de búsqueda, distinta de modificar/separar) y f-strings (Picuino N°24, sacado del currículo cercano sin fecha asignada).
- **`split()` con asignación múltiple, no como lista:** se evita mostrar/explicar el objeto lista completo porque Listas recién se enseña en Clase 33. `producto, precio = texto.split(",")` alcanza para el caso de uso (siempre 2 partes) sin adelantar contenido.
- **Unión y repetición de strings (`+`/`*`) como sección corta y separada, antes de los métodos:** contenido de Picuino N°21, sacado de la Clase 28 para no reforzar el patrón `print("texto" + variable)` prohibido por la regla 14 del CLAUDE.md. Aquí se presentan como operadores (sin punto), en contraste explícito con los métodos que siguen.
- **Ejercicios "0" (2, no 1):** el contenido tiene dos matices claramente separables que ameritan drill aparte — operadores (`+`/`*`, sin punto) vs. `split()` con asignación múltiple (patrón de dos variables a la vez) — a diferencia de `upper()`/`lower()`/`title()`/`strip()`/`replace()`, que se cubren con la exigencia natural de los ejercicios 1-3.
