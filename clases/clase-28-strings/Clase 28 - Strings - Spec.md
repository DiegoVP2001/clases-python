# Clase 28 — Strings: indexing y slicing

**Estado:** Spec aprobada — 2026-08-26
**Clase Picuino:** N° 21 — Cadenas de texto + N° 22 — Índices de cadenas de texto (combinadas, foco recortado a acceso por índice y rebanadas — ver "Decisiones de diseño relevantes")
**URL Picuino:** https://www.picuino.com/es/python-textos.html (N°21) / https://www.picuino.com/es/python-textos-indices.html (N°22)

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min
- **Modalidad:** Individual (no se menciona en el notebook — ver regla del CLAUDE.md)
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo hasta N°27 inclusive (Ciclos completo: `for`, `range()`, `for` anidado, `continue`/`break`, `while`; Funciones N°24a/24b)
- **Contenidos nuevos:** cadena como secuencia de caracteres + `len()`, acceso por índice positivo y negativo, rebanadas (`slicing`) con `[inicio:fin]`, omitir límites, y comportamiento de rebanadas fuera de rango
- **Contextos temáticos:** patente de auto en el Registro Civil (Haz Ahora + ICN + Guiada, mismo escenario), código de seguimiento de pedido online (Ejercicio 1), tag de un clan gamer (Ejercicio 2), RUT — cuerpo y dígito verificador (Ejercicio 3), código de acceso simétrico de un clan (Ejercicio 4 — desafío)
- **Tema breve (Form):** strings índice y slicing

## Objetivo

Extraer caracteres y segmentos específicos de una cadena de texto mediante índices y rebanadas, con precisión.

## Propósito

La precisión es acertar en el número exacto, sin margen de error, cuando cada posición cuenta. Hoy la practicamos ubicando caracteres exactos dentro de un texto, usando índices y rebanadas.

## OAs MINEDUC

`OA2, OA3`

## Estructura de la clase

### 1. Haz Ahora (6 min)
El Registro Civil está migrando sus registros de patentes vehiculares a un sistema digital. Cada patente llega como texto, por ejemplo `BRTZ21`: los primeros 4 caracteres son letras y los últimos 2 son números. El funcionario a cargo, sabiendo que ya saben programar, les pide ayuda para automatizar la lectura de estos registros — pero antes, quiere que tengan clara la lógica:

1. ¿Cuál es el primer carácter de la patente `BRTZ21`?
2. ¿Cuántos caracteres tiene en total esa patente?
3. ¿Cuál es el último carácter?
4. Si quisieras quedarte solo con el bloque de números, ¿qué trozo tomarías?
5. Si alguien te dicta mal la patente y solo alcanza a escribir 5 caracteres, ¿qué pasaría si igual intentas leer el 6to carácter?

**Respuestas esperadas:**
1. La letra "B".
2. 6 caracteres.
3. El número "1".
4. Los 2 últimos caracteres: "21".
5. No se podría — esa posición no existiría, así que sería un error.

### 2. Introducción al Contenido Nuevo (18 min)

Contexto de ejemplos: patente de auto del Registro Civil — mismo contexto del Haz Ahora, para que el "aha" sea inmediato.

**Concepto 1: Cadena como secuencia de caracteres + `len()`**
- Definición: una cadena de texto (`str`) es una secuencia ordenada de caracteres. Cada carácter, incluidos espacios y símbolos, ocupa una posición numerada dentro de esa secuencia. `len()` entrega cuántos caracteres tiene en total una cadena.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  print("Cantidad de caracteres:", len(patente))
  >> Cantidad de caracteres: 6
  ```
- Idea clave: toda cadena es una fila de caracteres contados por posición, y `len()` dice cuántas posiciones hay.

**Concepto 2: Acceso por índice (positivo y negativo)**
- Definición: cada carácter de una cadena se puede acceder por su posición entre corchetes. Los índices positivos parten en `0` desde el inicio; los índices negativos parten en `-1` desde el final, y van creciendo hacia atrás (`-2`, `-3`...). Pedir un índice que no existe en la cadena produce un error.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  print("Primer carácter:", patente[0])
  print("Último carácter:", patente[-1])
  >> Primer carácter: B
  >> Último carácter: 1
  ```
- Idea clave: el índice `0` siempre es el primer carácter, y el índice `-1` siempre es el último — sin importar cuán largo sea el texto.

**Concepto 3: Rebanadas (`slicing`)**
- Definición: una rebanada `texto[inicio:fin]` extrae varios caracteres seguidos, desde la posición `inicio` hasta justo antes de la posición `fin` (`fin` nunca se incluye). Omitir `inicio` o `fin` equivale a tomar desde el comienzo o hasta el final. A diferencia de un índice único, una rebanada que se pasa del largo de la cadena no produce error: simplemente devuelve lo que alcanza a existir, o una cadena vacía.
- Ejemplo:
  ```python
  patente = "BRTZ21"
  print("Bloque de letras:", patente[0:4])
  print("Bloque de números:", patente[4:])
  >> Bloque de letras: BRTZ
  >> Bloque de números: 21
  ```
- Idea clave: en una rebanada, `fin` marca dónde se detiene, no la última posición que se incluye.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Pedir un índice que no existe (ej. `texto[50]` en un texto de 10 caracteres) | `IndexError: string index out of range` | Revisar que el índice sea menor que `len(texto)` |
| Pensar que `[inicio:fin]` incluye el carácter en la posición `fin` | Ese carácter queda afuera, la rebanada corta justo antes | Recordar que `fin` es un límite exclusivo, no inclusivo |
| Contar mal los índices negativos (pensar que `-1` es "el penúltimo") | `-1` es el ÚLTIMO carácter, `-2` es el penúltimo | Practicar contando hacia atrás desde el final |

### 3. Práctica Guiada (22 min)
El Registro Civil te pasó una patente recién ingresada, guardada como texto: `BRTZ21`. Antes de guardar el registro en el sistema, necesita anotar por separado la primera letra (para ordenar el archivo alfabéticamente), el bloque completo de letras, y el bloque de números.

**El programa debe:**
- Guardar la patente en una variable de texto
- Extraer y mostrar la primera letra
- Extraer y mostrar el bloque completo de letras
- Extraer y mostrar el bloque de números

**Resultado esperado:**
```
Primera letra: B
Bloque de letras: BRTZ
Bloque de números: 21
```

- Solución:
  ```python
  patente = "BRTZ21"

  primera_letra = patente[0]
  bloque_letras = patente[0:4]
  bloque_numeros = patente[4:]

  print("Primera letra:", primera_letra)
  print("Bloque de letras:", bloque_letras)
  print("Bloque de números:", bloque_numeros)
  ```

### 4. Práctica Independiente (16 min)

Resuelve los siguientes ejercicios. Si te traban, pregunta al profe.

- Antes de empezar, ejecuta la celda de configuración de abajo: deja listos los verificadores para que revises tu propio trabajo sin esperar a que el profe pase por el puesto.
- No necesitas usar nombres de variable específicos: el verificador revisa lo que tu programa imprime, no cómo llamaste tus variables.
- Después de cada ejercicio, ejecuta su celda de revisión: vuelve a correr tu programa y lo compara, línea por línea, con el resultado esperado.
- Ojo: no borres el comentario de la primera línea de cada celda de solución — es lo que usa el verificador para encontrar tu código.

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
    esperadas = ["Carácter en índice 4: R", "Carácter en índice -3: I"]
    _revisar("# Tu solución — Ejercicio 0a", esperadas)

def verificar_ejercicio_0b():
    esperadas = ["Primera rebanada: COMP", "Segunda rebanada: TACION"]
    _revisar("# Tu solución — Ejercicio 0b", esperadas)

def verificar_ejercicio_1():
    esperadas = ["Comuna: ISM", "Correlativo: 240815"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    esperadas = ["Tag del clan: LOB", "Apodo: NieblaGamer"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    esperadas = ["Cuerpo: 198765432", "Dígito verificador: 1"]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

def verificar_ejercicio_4():
    esperadas = ["¿Es un código simétrico? True"]
    _revisar("# Tu solución — Ejercicio 4", esperadas)
```

**Ejercicio 0a — Práctica directa: índice puntual**
Aplica el acceso por índice sobre el siguiente texto guardado.

**El programa debe:**
- Guardar el texto `"PROGRAMACION"` en una variable
- Extraer y guardar el carácter que está en el índice `4`
- Extraer y guardar el carácter que está en el índice `-3`
- Imprimir ambos resultados con una etiqueta clara

**Resultado esperado:**
```
Carácter en índice 4: R
Carácter en índice -3: I
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 0a — puedes correrlo las veces que quieras
verificar_ejercicio_0a()
```

- Solución:
  ```python
  texto = "PROGRAMACION"
  caracter_4 = texto[4]
  caracter_menos_3 = texto[-3]
  print("Carácter en índice 4:", caracter_4)
  print("Carácter en índice -3:", caracter_menos_3)
  ```

**Ejercicio 0b — Práctica directa: rebanada**
Ahora aplica una rebanada sobre el mismo tipo de texto.

**El programa debe:**
- Guardar el texto `"COMPUTACION"` en una variable
- Extraer y guardar la rebanada `[0:4]`
- Extraer y guardar la rebanada `[5:]`
- Imprimir ambos resultados con una etiqueta clara

**Resultado esperado:**
```
Primera rebanada: COMP
Segunda rebanada: TACION
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 0b — puedes correrlo las veces que quieras
verificar_ejercicio_0b()
```

- Solución:
  ```python
  texto = "COMPUTACION"
  primera_rebanada = texto[0:4]
  segunda_rebanada = texto[5:]
  print("Primera rebanada:", primera_rebanada)
  print("Segunda rebanada:", segunda_rebanada)
  ```

**Ejercicio 1 — Código de seguimiento de un pedido**
Una tienda online genera un código de seguimiento por cada pedido, como `"ISM240815"`: las primeras 3 letras indican la comuna de despacho, y los dígitos siguientes son el número correlativo del pedido. El sistema de bodega necesita separar ambos datos para organizar los despachos del día.

**El programa debe:**
- Guardar el código de seguimiento en una variable
- Extraer y guardar la comuna de despacho (los primeros 3 caracteres)
- Extraer y guardar el número correlativo (todo lo que viene después)
- Imprimir ambos datos con una etiqueta clara

<details>
<summary>💡 Pista — contar la posición exacta</summary>
Las 3 primeras letras ocupan las posiciones 0, 1 y 2. El correlativo empieza justo en la posición 3.
</details>

**Resultado esperado:**
```
Comuna: ISM
Correlativo: 240815
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 1 — puedes correrlo las veces que quieras
verificar_ejercicio_1()
```

- Solución:
  ```python
  codigo_seguimiento = "ISM240815"
  comuna = codigo_seguimiento[0:3]
  correlativo = codigo_seguimiento[3:]
  print("Comuna:", comuna)
  print("Correlativo:", correlativo)
  ```

**Ejercicio 2 — Tag de un clan gamer**
En un clan de un videojuego móvil, cada integrante elige un nombre de usuario que junta el tag del clan con su apodo, por ejemplo `"LOBNieblaGamer"` (clan `LOB` + apodo `NieblaGamer`). El líder del clan quiere revisar rápido el tag de cada integrante sin tener que leer el apodo completo.

**El programa debe:**
- Guardar el nombre completo de usuario en una variable
- Extraer y guardar el tag del clan (los primeros 3 caracteres)
- Extraer y guardar el apodo (todo lo que viene después del tag)
- Imprimir ambos datos con una etiqueta clara

<details>
<summary>💡 Pista — mismo patrón que el Ejercicio 1</summary>
Igual que con el código de seguimiento, el tag ocupa una cantidad fija de caracteres al inicio, y el resto es lo que sobra.
</details>

**Resultado esperado:**
```
Tag del clan: LOB
Apodo: NieblaGamer
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 2 — puedes correrlo las veces que quieras
verificar_ejercicio_2()
```

- Solución:
  ```python
  usuario = "LOBNieblaGamer"
  tag_clan = usuario[0:3]
  apodo = usuario[3:]
  print("Tag del clan:", tag_clan)
  print("Apodo:", apodo)
  ```

**Ejercicio 3 — RUT: cuerpo y dígito verificador**
El sistema de matrícula del liceo guarda el RUT de cada estudiante como texto, sin puntos y con guion, por ejemplo `"198765432-1"`: todos los caracteres antes del guion forman el cuerpo del RUT, y el último carácter es el dígito verificador. Antes de validar un RUT, la secretaría necesita separar ambas partes.

**El programa debe:**
- Guardar el RUT completo en una variable de texto
- Extraer y guardar el cuerpo del RUT (todo excepto el guion y el dígito verificador final)
- Extraer y guardar el dígito verificador (el último carácter)
- Imprimir ambos datos con una etiqueta clara

<details>
<summary>💡 Pista — el cuerpo no tiene un largo fijo</summary>
Como el cuerpo del RUT puede tener distinta cantidad de dígitos según la persona, conviene contar los dos últimos caracteres (guion + dígito verificador) desde el final, con índices negativos, en vez de contarlos desde el inicio.
</details>

**Resultado esperado:**
```
Cuerpo: 198765432
Dígito verificador: 1
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 3 — puedes correrlo las veces que quieras
verificar_ejercicio_3()
```

- Solución:
  ```python
  rut = "198765432-1"
  cuerpo = rut[:-2]
  digito_verificador = rut[-1]
  print("Cuerpo:", cuerpo)
  print("Dígito verificador:", digito_verificador)
  ```

**Ejercicio 4 — Desafío: código de acceso simétrico**
El clan quiere una contraseña de acceso especial: un código de 4 caracteres que se lea igual al derecho y al revés (por ejemplo `"ABBA"` o `"1221"`), como un candado simétrico. Antes de aceptar un código nuevo, el sistema del clan debe comprobar si cumple esa simetría, comparando cada posición con la que le corresponde desde el otro extremo.

**El programa debe:**
- Guardar un código de acceso de exactamente 4 caracteres en una variable
- Comparar el primer carácter con el último
- Comparar el segundo carácter con el penúltimo
- Guardar si el código es simétrico según si ambas comparaciones coinciden, e imprimirlo con una etiqueta clara

<details>
<summary>💡 Pista — el penúltimo también tiene índice negativo</summary>
El último carácter es el índice `-1`, y el penúltimo es el índice `-2` — igual que ya practicaste con el dígito verificador del RUT.
</details>

**Resultado esperado:**
```
¿Es un código simétrico? True
```

**Celda de verificación:**
```python
# Ejecuta esto para revisar tu Ejercicio 4 — puedes correrlo las veces que quieras
verificar_ejercicio_4()
```

- Solución:
  ```python
  codigo_acceso = "ABBA"
  primera_comparacion = codigo_acceso[0] == codigo_acceso[-1]
  segunda_comparacion = codigo_acceso[1] == codigo_acceso[-2]
  es_simetrico = primera_comparacion and segunda_comparacion
  print("¿Es un código simétrico?", es_simetrico)
  ```

### 5. Ticket de Salida (6 min)
**Pregunta 1:**
```python
texto = "VIRTUAL"
print(texto[0], texto[-1])
```
¿Qué imprime este programa?
- A: L V
- B: VIRTUAL VIRTUAL
- C: V L
- D: V AL

**Respuesta correcta:** C
**Justificación:** `texto[0]` es el primer carácter ("V") y `texto[-1]` es el último ("L"), sin importar el largo del texto.

**Pregunta 2:**
```python
texto = "VIRTUAL"
print(texto[2:5])
```
¿Qué imprime este programa?
- A: IRTU
- B: RTU
- C: RTUA
- D: TUAL

**Respuesta correcta:** B
**Justificación:** La rebanada toma desde el índice 2 hasta justo antes del índice 5 — las posiciones 2, 3 y 4 ("R", "T", "U") — sin incluir la posición 5.

**Pregunta 3:**
```python
texto = "SOL"
print(texto[1:10])
print(texto[10])
```
¿Qué ocurre al ejecutar este programa?
- A: Imprime "OL" y luego se detiene con un error, porque el índice único sí exige que la posición exista
- B: Imprime "OL" y "" (vacío), sin ningún error
- C: Se detiene con error en la primera línea, porque la rebanada también está fuera de rango
- D: Imprime "SOL" dos veces

**Respuesta correcta:** A
**Justificación:** Una rebanada fuera de rango no da error, solo devuelve lo que alcanza a existir ("OL"); un índice único fuera de rango sí produce un error, porque exige que esa posición exista.

### Cierre (5 min)
**Objetivo de la clase:** Extraer caracteres y segmentos específicos de una cadena de texto mediante índices y rebanadas, con precisión.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes extrayendo un carácter o un segmento exacto de un texto usando índices y rebanadas? (1 = no entendí nada, 5 = puedo explicárselo a otro)

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación real tendrías que acertar en una posición exacta, sin margen de error, igual que hoy con los índices?

## Decisiones de diseño relevantes

- **Recorte de alcance respecto a Picuino N°21+N°22 completos** (acordado en sesión de diseño 2026-08-26, ver `Prompt.md`): esta clase cubre solo acceso por índice y rebanadas. Quedan fuera creación básica de cadenas (comillas/escapes/Unicode), unión (`+`) y repetición (`*`) — se evalúa moverlas a la Clase N°30 (métodos/f-strings) — y el recorrido con `for`, que se traslada íntegro a la Clase N°29 nueva (`clase-29-strings-recorrido`).
- **Conceptos del ICN fusionados a pedido de Diego (2026-08-26):** la propuesta inicial separaba índice positivo / índice negativo / rebanada / rebanada fuera de rango en 4 conceptos; Diego pidió fusionar índice positivo+negativo en un solo concepto, y rebanada+fuera de rango en otro — quedando 3 conceptos en total (cadena+`len()`, índices, rebanadas).
- **Escenario compartido Haz Ahora/ICN/Guiada cambiado a patente de auto/Registro Civil (2026-08-26, a propuesta de Diego, reemplaza el primer diseño con código de sala de torneo gamer):** patente chilena vigente (4 letras + 2 números, ej. `BRTZ21`) — dato real y verificable, sin inventarle significado a cada letra/número (el sistema actual no codifica región ni categoría en la patente, a diferencia del sistema anterior a 2007). Se trata solo como "bloque de letras" + "bloque de números". Como la patente tiene naturalmente 2 segmentos (no 3, como el código de sala descartado), se agregó la extracción de la primera letra por separado (para "ordenar el archivo alfabéticamente") como tercera pieza de la Guiada, así se mantiene la combinación de índice único + rebanada en el mismo nivel de dificultad. Las preguntas del Haz Ahora son cerradas y concretas, sin revelar sintaxis; la última pregunta (5) anticipa el concepto de error de índice sin nombrarlo.
- **RUT se mantiene sin cambios como Ejercicio 3 (contextualizado)**, pese a que el escenario compartido ahora también es un documento oficial chileno — se marcó como punto abierto al proponer el cambio de contexto y Diego aprobó la propuesta completa sin objetarlo. Encaja con la actitud de Precisión (cada posición del RUT importa) y obliga a combinar índice negativo + rebanada, porque el cuerpo del RUT no tiene largo fijo — a diferencia de los Ejercicios 1 y 2, donde el prefijo sí es de largo fijo.
- **Ejercicio 4 (desafío) evita sintaxis no vista:** se descartó `texto[::-1]` (slicing con paso) porque no es parte del recorte de esta clase — el desafío logra el mismo espíritu de "verificar simetría" comparando manualmente posiciones opuestas con índices ya enseñados, sin `for` (tampoco visto aún para strings) ni paso negativo en el slicing.
- **Ejercicios "0a"/"0b" (default desde 2026-08-21):** se usan los 2, porque la clase tiene dos matices claramente separables que ameritan drill aparte — acceso por índice puntual (0a) y rebanada (0b) — antes de pasar a los ejercicios contextualizados.
