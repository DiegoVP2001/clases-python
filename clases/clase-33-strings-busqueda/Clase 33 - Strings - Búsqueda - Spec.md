# Clase 33 — Strings: búsqueda de texto (`in`, `find()`)

**Estado:** Spec aprobada — 2026-09-05
**Clase Picuino:** N° 23 — Métodos de cadenas de texto (parcial — complementaria a Clase 32)
**URL Picuino:** https://www.picuino.com/es/python-textos-metodos.html

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual (por defecto)
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** Strings — acceso por índice y rebanadas (Clase 28), recorrido de strings con `for` (Clase 29), métodos para modificar/separar texto (Clase 32). El Control estándar del Lunes N°31 solo repasó N°28 y N°29 (no los métodos de Clase 32).
- **Contenidos nuevos:** operador `in`, normalización con `.lower()` antes de comparar, método `find()`.
- **Contextos temáticos:** Los Mellis Al Paso (negocio ancla real de Isla de Maipo, escenario único de toda la clase — mismo criterio que Clase 32) — revisar notas de pedido por palabras de alerta/alergia.

**Recorte respecto a la ficha Picuino N°23:** solo cubre `in` y `find()` (el resto de la ficha — `upper()`, `lower()`, `swapcase()`, `title()`, `strip()`, `replace()`, `split()` — se enseñó en Clase 32).

## Objetivo

Aplicar los operadores `in` y `find()` para detectar si un texto contiene una palabra clave y en qué posición aparece, con rigor.

## Propósito

El rigor es revisar cada dato siguiendo siempre el mismo método, sin confiarse de un vistazo rápido. Hoy lo practicamos revisando notas de pedido en busca de palabras de alerta, como posibles alergias.

## ¿Para qué sirve?

Este mismo patrón —revisar si un texto contiene una palabra y en qué posición— es el que usan los buscadores (`Ctrl+F`) para encontrarte una palabra en un documento, y los filtros de spam o de contenido para detectar palabras prohibidas en un mensaje.

## OAs

OA2, OA3.

## Estructura de la clase

### 1. Haz Ahora (6 min)

En Los Mellis, algunos clientes agregan una nota extra al pedido cuando tienen alguna alergia o restricción: "sin maní", "sin gluten", "no le pongan palta". Antes de preparar el pedido, alguien tiene que leer la nota completa y no pasar por alto ninguna advertencia. Los Mellis, sabiendo que ustedes programan, les pide ayuda para automatizar esa revisión — pero antes quiere que tengan clara la lógica:

1. Si la nota dice "sin maní por favor", ¿qué palabra hay que encontrar ahí para activar la alerta?
2. Si la nota llega escrita "SIN MANÍ" en mayúsculas, ¿esa alerta debería detectarse igual?
3. Si la palabra "maní" aparece a la mitad de la nota, ¿el programa debería poder decir en qué parte exacta del texto empieza?
4. Si una nota no menciona ninguna palabra de alerta, ¿qué debería pasar con el pedido?

**Respuestas esperadas:**
1. La palabra "maní".
2. Sí, debería detectarse igual, sin importar mayúsculas/minúsculas.
3. Sí, indicando desde qué posición del texto empieza.
4. El pedido se prepara normalmente, sin alerta.

### 2. Introducción al Contenido Nuevo (18 min)

**Concepto 1: El operador `in`**
- Definición: `in` revisa si un texto está contenido dentro de otro y devuelve `True` o `False`. No dice en qué parte está, solo si está.
- Ejemplo:
  ```python
  nota_pedido = "sin maní por favor"
  tiene_alerta = "maní" in nota_pedido
  print("¿Tiene alerta?", tiene_alerta)
  ```
- Idea clave: `in` dice si un texto está dentro de otro, sin decir dónde.
- Resumen tabla: `"palabra" in texto`

**Concepto 2: Normalizar con `.lower()` antes de comparar**
- Definición: `in` y `find()` son sensibles a mayúsculas y minúsculas — "MANÍ" y "maní" no se consideran iguales. Por eso, antes de buscar, se normaliza el texto a minúscula con `.lower()`.
- Ejemplo:
  ```python
  nota_pedido = "SIN MANÍ POR FAVOR"
  tiene_alerta = "maní" in nota_pedido.lower()
  print("¿Tiene alerta?", tiene_alerta)
  ```
- Idea clave: antes de buscar, siempre pasar el texto a minúscula con `.lower()`.
- Resumen tabla: `"palabra" in texto.lower()`

**Concepto 3: El método `find()`**
- Definición: `find()` busca un texto dentro de otro y devuelve la posición (el índice) donde empieza. Si el texto buscado no aparece, devuelve `-1`.
- Ejemplo:
  ```python
  nota_pedido = "sin maní por favor"
  posicion = nota_pedido.find("maní")
  print("Posición de la alerta:", posicion)
  ```
- Idea clave: `find()` dice en qué posición empieza el texto buscado, o `-1` si no está.
- Resumen tabla: `texto.find("palabra")`

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Buscar sin normalizar mayúsculas | `in`/`find()` no detectan "MANÍ" si se busca "maní" tal cual | Aplicar `.lower()` al texto completo antes de comparar |
| Confundir `in` con `find()` | Usar `in` cuando se necesita saber la posición, o `find()` cuando solo se necesita sí/no | `in` responde sí/no; `find()` responde en qué posición |
| Interpretar `-1` como una posición real | Tratar `-1` como si fuera el índice de un carácter válido | `-1` es un valor especial que significa "no está", no una posición |

### 3. Práctica Guiada (22 min)

Retomando la nota "sin maní por favor" del Haz Ahora, Los Mellis quiere ahora no solo saber si hay alerta, sino en qué posición exacta del texto aparece, para destacarla al imprimir la boleta.

**El programa debe:**
- Guardar la nota del pedido y la palabra de alerta en variables separadas.
- Normalizar la nota a minúscula antes de comparar.
- Verificar si la palabra de alerta está dentro de la nota normalizada.
- Si está, mostrar en qué posición del texto normalizado empieza.
- Si no está, mostrar que la nota no tiene alerta.

**Resultado esperado:**
```
¿Tiene alerta? True
Posición de la alerta: 4
```

- Solución:
  ```python
  nota_pedido = "Sin maní por favor, gracias"
  palabra_alerta = "maní"

  nota_normalizada = nota_pedido.lower()
  tiene_alerta = palabra_alerta in nota_normalizada
  print("¿Tiene alerta?", tiene_alerta)

  if tiene_alerta:
      posicion = nota_normalizada.find(palabra_alerta)
      print("Posición de la alerta:", posicion)
  else:
      print("La nota no tiene alerta.")
  ```

### 4. Práctica Independiente (17 min)

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
```

**Ejercicio 0a — Práctica directa: usar `in`**
Aplica el operador `in`:

**El programa debe:**
- Guardar un texto y una palabra a buscar en dos variables.
- Verificar con `in` si la palabra está dentro del texto.
- Imprimir el resultado con una etiqueta.

**Resultado esperado:**
```
¿Está la palabra? True
```

- Solución:
  ```python
  texto = "el pan se vende en la panadería"
  palabra = "pan"
  esta = palabra in texto
  print("¿Está la palabra?", esta)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_0a():
    esperadas = ["¿Está la palabra? True"]
    _revisar("# Tu solución — Ejercicio 0a", esperadas)

verificar_ejercicio_0a()
```

**Ejercicio 0b — Práctica directa: usar `find()`**
Aplica el método `find()`:

**El programa debe:**
- Guardar un texto y una palabra a buscar en dos variables.
- Usar `find()` para obtener la posición donde empieza la palabra.
- Imprimir la posición con una etiqueta.

**Resultado esperado:**
```
Posición: 3
```

- Solución:
  ```python
  texto = "el pan se vende en la panadería"
  palabra = "pan"
  posicion = texto.find(palabra)
  print("Posición:", posicion)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_0b():
    esperadas = ["Posición: 3"]
    _revisar("# Tu solución — Ejercicio 0b", esperadas)

verificar_ejercicio_0b()
```

**Ejercicio 1 — Alerta de gluten**
En Los Mellis, algunos pedidos llegan con una nota escrita por el cliente, a veces en mayúsculas, a veces mezclando mayúsculas y minúsculas. Antes de despachar el pedido, alguien tiene que revisar si la nota menciona la palabra "gluten", sin importar cómo esté escrita, para avisar en cocina.

**El programa debe:**
- Guardar la nota del pedido y la palabra de alerta "gluten" en variables separadas.
- Normalizar la nota a minúscula antes de comparar.
- Verificar si la palabra de alerta está dentro de la nota normalizada.
- Imprimir si la nota tiene alerta o no, con una etiqueta clara.

<details>
<summary>💡 Pista — Normalizar antes de comparar</summary>
Guarda el resultado de aplicar `.lower()` a la nota en una variable aparte antes de usar `in`, así te aseguras de comparar siempre en minúscula.
</details>

**Resultado esperado:**
```
¿Tiene alerta? True
```

- Solución:
  ```python
  nota_pedido = "SIN GLUTEN por favor, gracias!"
  palabra_alerta = "gluten"

  nota_normalizada = nota_pedido.lower()
  tiene_alerta = palabra_alerta in nota_normalizada
  print("¿Tiene alerta?", tiene_alerta)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_1():
    esperadas = ["¿Tiene alerta? True"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

verificar_ejercicio_1()
```

**Ejercicio 2 — Ubicar la palabra "urgente"**
Cuando un pedido es para llevar rápido porque el cliente espera afuera, la nota incluye la palabra "urgente" en algún lugar del texto. Para resaltarla en el ticket que sale impreso en cocina, Los Mellis necesita saber exactamente en qué posición del texto empieza esa palabra.

**El programa debe:**
- Guardar la nota de despacho en una variable de texto (ya viene escrita en minúscula).
- Usar `find()` para obtener la posición donde empieza la palabra "urgente".
- Imprimir esa posición con una etiqueta.

<details>
<summary>💡 Pista — Contar desde 0</summary>
`find()` cuenta las posiciones desde 0, igual que el indexing de strings que ya vieron: la primera letra del texto está en la posición 0, no en la 1.
</details>

**Resultado esperado:**
```
Posición: 7
```

- Solución:
  ```python
  nota_despacho = "pedido urgente para el cliente de la esquina"
  posicion = nota_despacho.find("urgente")
  print("Posición:", posicion)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_2():
    esperadas = ["Posición: 7"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

verificar_ejercicio_2()
```

**Ejercicio 3 — Dos alertas posibles**
Algunos clientes escriben notas más completas, mezclando el pedido con la alerta en cualquier parte del texto y sin cuidar mayúsculas. Los Mellis necesita revisar si la nota menciona "maní", "gluten", ninguna de las dos, o ambas, y en ese caso mostrar en qué posición empieza cada una para no perder ningún aviso.

**El programa debe:**
- Guardar la nota del pedido y las dos palabras de alerta ("maní", "gluten") en variables separadas.
- Normalizar la nota a minúscula antes de comparar.
- Verificar por separado si cada palabra de alerta está presente.
- Para cada alerta presente, mostrar en qué posición del texto normalizado empieza.
- Si ninguna alerta está presente, mostrar que la nota no tiene alertas.

<details>
<summary>💡 Pista — Revisar cada alerta por separado</summary>
Guarda el resultado de `in` para cada palabra en su propia variable (por ejemplo, si tiene maní y si tiene gluten) antes de decidir qué mostrar — así puedes revisar ambas sin que una tape a la otra.
</details>

**Resultado esperado:**
```
Alerta de maní en la posición: 4
Alerta de gluten en la posición: 15
```

- Solución:
  ```python
  nota_pedido = "Sin MANÍ y sin GLUTEN por favor"
  palabra_mani = "maní"
  palabra_gluten = "gluten"

  nota_normalizada = nota_pedido.lower()
  tiene_mani = palabra_mani in nota_normalizada
  tiene_gluten = palabra_gluten in nota_normalizada

  if tiene_mani:
      print("Alerta de maní en la posición:", nota_normalizada.find(palabra_mani))
  if tiene_gluten:
      print("Alerta de gluten en la posición:", nota_normalizada.find(palabra_gluten))
  if not tiene_mani and not tiene_gluten:
      print("La nota no tiene alertas.")
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_3():
    esperadas = [
        "Alerta de maní en la posición: 4",
        "Alerta de gluten en la posición: 15",
    ]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

verificar_ejercicio_3()
```

**Ejercicio 4 — Desafío: ¿cuál alerta aparece primero?**
Cuando una nota tiene ambas alertas, Los Mellis quiere saber cuál de las dos aparece primero en el texto, para destacarla primero en el ticket de cocina.

**El programa debe:**
- Guardar la nota del pedido y las dos palabras de alerta en variables separadas.
- Normalizar la nota a minúscula antes de comparar.
- Si ambas alertas están presentes, encontrar la posición de cada una y determinar cuál aparece primero, comparando las posiciones.
- Si solo una alerta está presente, indicar cuál. Si ninguna, indicarlo también.

**Resultado esperado:**
```
La alerta de gluten aparece primero.
```

- Solución:
  ```python
  nota_pedido = "El cliente pidió sin gluten, pero también sin maní"
  palabra_mani = "maní"
  palabra_gluten = "gluten"

  nota_normalizada = nota_pedido.lower()
  tiene_mani = palabra_mani in nota_normalizada
  tiene_gluten = palabra_gluten in nota_normalizada

  if tiene_mani and tiene_gluten:
      posicion_mani = nota_normalizada.find(palabra_mani)
      posicion_gluten = nota_normalizada.find(palabra_gluten)
      if posicion_gluten < posicion_mani:
          print("La alerta de gluten aparece primero.")
      else:
          print("La alerta de maní aparece primero.")
  elif tiene_mani:
      print("Solo aparece la alerta de maní.")
  elif tiene_gluten:
      print("Solo aparece la alerta de gluten.")
  else:
      print("La nota no tiene alertas.")
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_4():
    esperadas = ["La alerta de gluten aparece primero."]
    _revisar("# Tu solución — Ejercicio 4", esperadas)

verificar_ejercicio_4()
```

### 5. Ticket de Salida (6 min)

**Pregunta 1:**
```python
texto = "Hola Mundo"
print("mundo" in texto)
```
¿Qué imprime este programa?
- A: True
- B: False
- C: Error
- D: None
**Respuesta correcta:** B
**Justificación:** `in` es sensible a mayúsculas/minúsculas. "mundo" (minúscula) no coincide con "Mundo" (con mayúscula) dentro del texto, así que la comparación da `False`.

**Pregunta 2:**
```python
texto = "programar es divertido"
print(texto.find("es"))
```
¿Qué imprime este programa?
- A: 9
- B: 11
- C: 10
- D: -1
**Respuesta correcta:** C
**Justificación:** `find()` cuenta los caracteres desde la posición 0. "programar " ocupa las posiciones 0 a 9 (incluido el espacio), así que "es" empieza justo en la posición 10.

**Pregunta 3:**
```python
texto = "clase de programación"
posicion = texto.find("python")
print(posicion)
```
¿Qué significa el valor que imprime este programa?
- A: Que "python" no fue encontrado dentro del texto.
- B: Que "python" está en la posición 0 del texto.
- C: Que ocurrió un error al buscar.
- D: Que el texto tiene exactamente -1 caracteres de "python".
**Respuesta correcta:** A
**Justificación:** `find()` devuelve `-1` como valor especial cuando la palabra buscada no aparece en el texto — no es una posición real, sino la señal de "no está".

### Cierre (5 min)

**Objetivo de la clase:** Aplicar los operadores `in` y `find()` para detectar si un texto contiene una palabra clave y en qué posición aparece, con rigor.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes usando `in` y `find()` para revisar si un texto contiene una palabra y en qué posición aparece, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro:** Pensando en el rigor con que revisaste hoy cada nota, ¿en qué otra situación real —dentro o fuera de la programación— tendrías que revisar algo con ese mismo cuidado, sin confiarte de un vistazo rápido?

## Decisiones de diseño relevantes

- **Actitud elegida: Rigor.** Conecta directo con la sensibilidad a mayúsculas/minúsculas de `in`/`find()`, que obliga a normalizar con `.lower()` en vez de confiar en una comparación descuidada.
- **Escenario único: Los Mellis Al Paso**, continuando el mismo negocio ancla real de Isla de Maipo usado en Clase 32, para dar continuidad narrativa entre las dos clases de strings.
- **Propósito en formato corto estándar** (2 frases, sin nombrar la empresa) — no se usó el piloto "compañía real" de Clase 30/32, que sigue sin generalizarse.
- **Sección nueva "¿Para qué sirve?"** — propuesta por Diego durante el diseño de esta clase (2026-09-05): un bloque corto (máx. 2 frases) después del Propósito, con ejemplos reales de dónde se usa el contenido técnico (no la actitud), ligados a lo que se practica en la clase. Diego aprobó el texto y pidió dejarlo **como default** para todas las clases futuras — ver actualización de `disenar-clase/SKILL.md`, `generar-colab-clase/SKILL.md`, `generar-ppt-clase/SKILL.md` y regla 24 del `CLAUDE.md` raíz de este proyecto.
- **Ejercicio 4 (desafío) reutiliza solo sintaxis ya vista** (`if`/`elif`/`else`, `in`, `find()`) — no introduce el segundo argumento opcional de `find(sub, inicio)`, para no adelantar contenido no visto.
