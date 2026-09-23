# Clase 35 — Listas: Creación y Acceso

**Estado:** Spec aprobada — 2026-09-23
**Clase Picuino:** N° 25 — Listas + N° 26 — Índices de listas
**URL Picuino:** ver `referencia-curriculo`

## Contexto

- **Curso:** 4to medio
- **Duración:** 80 min totales, de los cuales ~56 min corresponden a los 5 pasos (los primeros 15-20 min los ocupa la Presentación de proyecto, ver sección propia más abajo)
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo hasta N°34 inclusive (Strings completo: indexing/slicing, recorrido con `for`, métodos para modificar/separar —incluido `split()`, Clase 32—, búsqueda de texto con `in`/`find()`, el lunes estándar de control N°31 y el Control N°34). f-strings **no** se ha visto.
- **Contenidos nuevos:** convertir texto en lista con `split(",")`, acceso por índice (positivo y negativo), slicing, convertir un dato de la lista con `int()` antes de operar. Al pasar, sin ser concepto propio: crear una lista con `[ ]` literal y `len()`.
- **Contextos temáticos:** `bbdd_guaguas.csv` (nombres inscritos en Chile 1920-2021, Registro Civil) — hilo conductor autorizado de N°35, N°36 y las mini-clases de pandas del 1/5/6-oct (excepción a la restricción 3 del CLAUDE.md raíz, ver `clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` §6).

## Objetivo

Extraer datos específicos de una fila real de nombres de guaguas de Chile en preparación del proyecto, convirtiéndola en lista con `split(",")` y accediendo a sus elementos por índice y slicing, con atención al detalle.

## Propósito

La atención al detalle es fijarse en lo pequeño, porque con datos reales un detalle chico cambia toda la respuesta. Hoy lo practicamos sacando datos exactos de filas reales de nombres de guaguas inscritas en Chile.

## ¿Para qué sirve?

Así lee un programa una base de datos real: separa cada fila por comas y toma la columna que necesita por su posición. Es exactamente lo que van a hacer con la base de datos que elijan para el proyecto de octubre.

## Presentación de proyecto (antes del Haz Ahora, no descuenta tiempo de los 5 pasos)

**Duración:** 15-20 min, al inicio de la sesión.

Espacio para:
1. El pitch del menú de 9 bases — guion completo en `clases/clases-octubre/Catastro de Bases y Banco de Preguntas - Proyecto Octubre.md` §4 (noticia del LUN + las 5 áreas temáticas + apertura del formulario de elección de base, que cierra el martes 29-sep a las 23:59).
2. Mención breve de que el 13-oct se presentan las rúbricas completas de evaluación del proyecto (`clases-octubre/instrumentos-proyecto/Lanzamiento del Proyecto - 13 Octubre.html`) — no se detalla hoy, solo se anuncia.

No se incluye en el PPT de esta clase (`Presentación.pptx` es contenido de aula regular); el material del pitch es aparte.

## Estructura de la clase

### 1. Haz Ahora (4 min)

Diego trae una noticia real: cada año el Registro Civil registra, fila por fila, todos los nombres inscritos en Chile — la base se llama `bbdd_guaguas.csv`. Una periodista está armando una nota sobre 2021 y les muestra una fila tal cual aparece en la base, separada por comas: `2021,Mateo,M,3267`. Ella, sabiendo que ustedes programan, les pide ayuda para sacar datos exactos de filas como esta — pero antes quiere que tengan clara la lógica de contarlas:

1. Contando desde el principio, ¿en qué posición de la fila aparece el nombre?
2. ¿Cuál es el dato que ocupa la última posición de la fila?
3. Si quisiera revisar solo los dos primeros datos de la fila, ¿cuáles serían?

**Respuestas esperadas:**
1. 2ª posición
2. 3267
3. 2021 y Mateo

### 2. Introducción al Contenido Nuevo (15 min)

**Concepto 1: De fila de texto a lista con `split(",")`**
- Definición: Una fila de `bbdd_guaguas.csv` llega como un solo texto separado por comas. El método `.split(",")` corta ese texto en cada coma y arma una lista con cada dato por separado.
- Ejemplo:
  ```python
  fila = "2021,Mateo,M,3267"
  datos = fila.split(",")
  print("La fila como lista:", datos)
  ```
  ```
  >> La fila como lista: ['2021', 'Mateo', 'M', '3267']
  ```
- Idea clave: `variable.split(",")` corta un texto en cada coma y arma una lista.
- Resumen tabla: `datos = fila.split(",")`
- **Nota (mostrada al pasar, no es concepto propio):** una lista también se puede escribir directo entre corchetes (`nombres = ["Mateo", "Emma"]`), y `len(datos)` cuenta cuántos elementos tiene.

**Concepto 2: Acceso por índice, incluidos los negativos**
- Definición: Cada dato de la lista tiene una posición, llamada índice. Python empieza a contar desde 0, así que el primer dato es `datos[0]`. Los índices negativos cuentan desde el final: `datos[-1]` es el último dato.
- Ejemplo:
  ```python
  print("Año:", datos[0])
  print("Último dato (cantidad):", datos[-1])
  ```
  ```
  >> Año: 2021
  >> Último dato (cantidad): 3267
  ```
- Idea clave: El índice empieza en 0; `datos[-1]` es el último dato sin saber cuántos hay.
- Resumen tabla: `datos[0]`, `datos[-1]`

**Concepto 3: Slicing**
- Definición: El slicing `lista[inicio:fin]` saca un tramo de la lista, desde `inicio` hasta justo antes de `fin` (el final queda excluido).
- Ejemplo:
  ```python
  print("Año y nombre:", datos[0:2])
  ```
  ```
  >> Año y nombre: ['2021', 'Mateo']
  ```
- Idea clave: `lista[inicio:fin]` incluye `inicio` pero excluye `fin`.
- Resumen tabla: `datos[0:2]`

**Concepto 4: Convertir un dato antes de operar (`int()`)**
- Definición: Todo lo que sale de `.split(",")` es texto (`str`), incluso si parece un número. Para operar matemáticamente con un dato hay que convertirlo primero con `int()`.
- Ejemplo:
  ```python
  print("El doble sin convertir:", datos[3] * 2)
  cantidad = int(datos[3])
  print("El doble convertido:", cantidad * 2)
  ```
  ```
  >> El doble sin convertir: 32673267
  >> El doble convertido: 6534
  ```
- Idea clave: Un dato que viene de `split()` siempre es texto — conviértelo con `int()` antes de operar.
- Resumen tabla: `int(datos[3])`

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Contar desde 1 en vez de 0 | Se accede al dato equivocado (ej. esperar el año en `datos[1]`, pero ahí está el nombre) | Recordar que el primer dato es `datos[0]` |
| `IndexError: list index out of range` | Se pide un índice que no existe en la lista | Revisar cuántos datos tiene la lista antes de acceder |
| Creer que el slicing incluye el fin | `datos[0:2]` no incluye `datos[2]`, y se esperaba que sí | Recordar que `fin` no se incluye, solo hasta justo antes |
| Operar con el dato tal cual sale de `split()` | `datos[3] * 2` repite el texto en vez de multiplicar | Convertir con `int()` antes de operar |

### 3. Práctica Guiada (12 min)

La periodista te pasa ahora la fila del nombre más popular de 2021: `"2021,Emma,F,2352"`. Quiere una nota con el nombre, cuántas inscripciones habría si se repitieran dos años seguidos, y un resumen rápido con el año y el nombre juntos.

**El programa debe:**
- Guardar la fila como texto y convertirla en lista con `split(",")`.
- Extraer el nombre y mostrarlo con una etiqueta clara.
- Extraer la cantidad, convertirla a número, y mostrar el doble de esa cantidad.
- Mostrar juntos el año y el nombre usando slicing.

**Resultado esperado:**
```
Nombre: Emma
El doble de las inscripciones: 4704
Año y nombre juntos: ['2021', 'Emma']
```

- Solución:
  ```python
  fila = "2021,Emma,F,2352"
  datos = fila.split(",")

  print("Nombre:", datos[1])
  cantidad = int(datos[3])
  print("El doble de las inscripciones:", cantidad * 2)
  print("Año y nombre juntos:", datos[0:2])
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

**Ejercicio 0a — Práctica directa: convertir y acceder por índice**
Aplica el patrón base:

**El programa debe:**
- Guardar el texto `"2021,Sofía,F,2251"` en una variable y convertirlo en lista con `split(",")`.
- Imprimir el año (índice 0) y el nombre (índice 1), cada uno con su propia etiqueta.

**Resultado esperado:**
```
Año: 2021
Nombre: Sofía
```

- Solución:
  ```python
  fila = "2021,Sofía,F,2251"
  datos = fila.split(",")
  print("Año:", datos[0])
  print("Nombre:", datos[1])
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_0a():
    esperadas = ["Año: 2021", "Nombre: Sofía"]
    _revisar("# Tu solución — Ejercicio 0a", esperadas)

verificar_ejercicio_0a()
```

**Ejercicio 1 — El registro más antiguo**
La periodista quiere comparar el presente con el pasado: te pasa la fila más antigua de la base, del año 1920: `"1920,Aaron,M,1"`. Necesita el nombre y el sexo registrado, usando la posición de cada uno, para contarte que ese año casi no había variedad de nombres.

**El programa debe:**
- Guardar la fila como texto y convertirla en lista con `split(",")`.
- Imprimir el nombre (índice 1).
- Imprimir el sexo registrado, contando la posición desde el final de la lista (índice negativo).

<details>
<summary>💡 Pista — contar desde el final</summary>
El sexo es el penúltimo dato de la fila. Contando desde el final, el último dato es índice -1, así que el penúltimo es índice -2.
</details>

**Resultado esperado:**
```
Nombre: Aaron
Sexo registrado: M
```

- Solución:
  ```python
  fila = "1920,Aaron,M,1"
  datos = fila.split(",")
  print("Nombre:", datos[1])
  print("Sexo registrado:", datos[-2])
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_1():
    esperadas = ["Nombre: Aaron", "Sexo registrado: M"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

verificar_ejercicio_1()
```

**Ejercicio 2 — Dos años iguales**
Ahora te pasa la fila de Julieta, otro nombre popular de 2021: `"2021,Julieta,F,1723"`. Quiere en una sola nota el año y el nombre juntos, y además cuántas inscripciones tendría si se sumaran dos años iguales seguidos.

**El programa debe:**
- Guardar la fila como texto y convertirla en lista.
- Imprimir juntos el año y el nombre usando slicing.
- Convertir la cantidad a número e imprimir el resultado de sumarla dos veces.

<details>
<summary>💡 Pista — slicing de los dos primeros</summary>
Para tomar los dos primeros datos de la lista, el slicing va desde el índice 0 hasta el índice 2 (que queda excluido).
</details>

**Resultado esperado:**
```
Año y nombre: ['2021', 'Julieta']
Inscripciones en dos años iguales: 3446
```

- Solución:
  ```python
  fila = "2021,Julieta,F,1723"
  datos = fila.split(",")
  print("Año y nombre:", datos[0:2])
  cantidad = int(datos[3])
  print("Inscripciones en dos años iguales:", cantidad + cantidad)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_2():
    esperadas = ["Año y nombre: ['2021', 'Julieta']", "Inscripciones en dos años iguales: 3446"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

verificar_ejercicio_2()
```

**Ejercicio 3 — ¿Son la misma persona?** *(contextualizado)*
La periodista encontró algo raro en un apunte viejo: dos filas de la base que se ven casi iguales pero no lo son. `"2021,Emilia,F,2044"` y `"2021,Emiliano,M,1357"` — quiere confirmar, dato por dato, que son registros distintos antes de publicar la nota, y necesita el nombre de cada una y la diferencia entre ambas cantidades.

**El programa debe:**
- Guardar ambas filas como texto y convertir cada una en lista con `split(",")`.
- Imprimir el nombre de cada fila, con etiquetas que las distingan.
- Convertir ambas cantidades a número e imprimir la diferencia entre la primera y la segunda.

<details>
<summary>💡 Pista — dos listas separadas</summary>
Necesitas dos variables de lista, una por cada fila — no mezcles los datos de ambas en una misma lista.
</details>

**Resultado esperado:**
```
Nombre 1: Emilia
Nombre 2: Emiliano
Diferencia de inscripciones: 687
```

- Solución:
  ```python
  fila_1 = "2021,Emilia,F,2044"
  fila_2 = "2021,Emiliano,M,1357"
  datos_1 = fila_1.split(",")
  datos_2 = fila_2.split(",")

  print("Nombre 1:", datos_1[1])
  print("Nombre 2:", datos_2[1])

  cantidad_1 = int(datos_1[3])
  cantidad_2 = int(datos_2[3])
  print("Diferencia de inscripciones:", cantidad_1 - cantidad_2)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_3():
    esperadas = [
        "Nombre 1: Emilia",
        "Nombre 2: Emiliano",
        "Diferencia de inscripciones: 687",
    ]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

verificar_ejercicio_3()
```

**Ejercicio 4 — Desafío: ¿cuánto le faltó?**
Antes de cerrar la nota, la periodista quiere un dato extra: comparar el nombre más popular de 2021 (Mateo, 3267 inscripciones) con el segundo más popular (Emma, 2352 inscripciones), mostrando primero los datos completos de ambas filas —tal como llegan de la base— y después solo la diferencia de inscripciones.

**El programa debe:**
- Guardar las dos filas: `"2021,Mateo,M,3267"` y `"2021,Emma,F,2352"`, y convertir cada una en lista.
- Imprimir la lista completa de cada fila.
- Imprimir, usando slicing, solo los dos primeros datos de la fila del segundo lugar (año y nombre).
- Convertir ambas cantidades a número e imprimir cuánto le faltó a Emma para alcanzar a Mateo.

**Resultado esperado:**
```
Fila completa 1: ['2021', 'Mateo', 'M', '3267']
Fila completa 2: ['2021', 'Emma', 'F', '2352']
Año y nombre del segundo lugar: ['2021', 'Emma']
Le faltaron: 915
```

- Solución:
  ```python
  fila_1 = "2021,Mateo,M,3267"
  fila_2 = "2021,Emma,F,2352"
  datos_1 = fila_1.split(",")
  datos_2 = fila_2.split(",")

  print("Fila completa 1:", datos_1)
  print("Fila completa 2:", datos_2)
  print("Año y nombre del segundo lugar:", datos_2[0:2])

  cantidad_1 = int(datos_1[3])
  cantidad_2 = int(datos_2[3])
  print("Le faltaron:", cantidad_1 - cantidad_2)
  ```

**Celda de verificación:**
```python
def verificar_ejercicio_4():
    esperadas = [
        "Fila completa 1: ['2021', 'Mateo', 'M', '3267']",
        "Fila completa 2: ['2021', 'Emma', 'F', '2352']",
        "Año y nombre del segundo lugar: ['2021', 'Emma']",
        "Le faltaron: 915",
    ]
    _revisar("# Tu solución — Ejercicio 4", esperadas)

verificar_ejercicio_4()
```

### 5. Ticket de Salida (5 min)

**Pregunta 1:**
```python
fila = "2021,Sofía,F,2251"
datos = fila.split(",")
print(datos[-1])
```
¿Qué imprime este programa?
- A: `2021`
- B: `Sofía`
- C: `F`
- D: `2251`
**Respuesta correcta:** D
**Justificación:** El índice -1 apunta al último dato de la lista, que es la cantidad.

**Pregunta 2:**
```python
fila = "2021,Sofía,F,2251"
datos = fila.split(",")
print(datos[0:2])
```
¿Qué imprime este programa?
- A: `['2021', 'Sofía']`
- B: `['2021', 'Sofía', 'F']`
- C: `['Sofía', 'F']`
- D: `['2021']`
**Respuesta correcta:** A
**Justificación:** El slicing `[0:2]` incluye el índice 0 pero excluye el índice 2, así que llega solo hasta el índice 1.

**Pregunta 3:**
```python
fila = "2021,Sofía,F,2251"
datos = fila.split(",")
print(datos[3] * 2)  # <- esta línea
```
¿Qué imprime la línea marcada?
- A: `4502`
- B: `22512251`
- C: Error, porque no se puede multiplicar
- D: `2251`
**Respuesta correcta:** B
**Justificación:** `datos[3]` es texto (`"2251"`), no un número — multiplicar un string por 2 lo repite, no lo multiplica.

### Cierre (3 min)

**Objetivo de la clase:** Extraer datos específicos de una fila real de nombres de guaguas de Chile en preparación del proyecto, convirtiéndola en lista con `split(",")` y accediendo a sus elementos por índice y slicing, con atención al detalle.

**Pregunta 1 — Metacognición (escala 1-5):** Del 1 al 5, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro", ¿cuánto entendiste sobre sacar datos exactos de una fila usando índices y slicing?

**Pregunta 2 — Actitud proyectada al futuro:** Cuenta una situación donde un detalle chico —una posición, una coma, un tipo de dato— podría cambiar por completo un resultado, dentro o fuera de la programación.

## Decisiones de diseño relevantes

- **Alcance recortado respecto a Picuino N°25-26 (decisión 2026-09-23):** se dejan fuera `+`/`*` de listas, `in`/`not in`, modificar un elemento por índice, y listas anidadas/multilínea — ninguno aporta al puente hacia el proyecto con `guaguas`, y sumarlos habría sobrecargado una sesión ya acotada a ~56 min. `[ ]` literal y `len()` se muestran solo al pasar dentro del Concepto 1, sin ser concepto propio con su propia Idea clave.
- **Tiempos comprimidos:** la sesión completa son 80 min, pero 15-20 min los ocupa la Presentación de proyecto (lanzamiento del menú de bases) antes de entrar a los 5 pasos — de ahí que la suma de los 5 pasos dé ~56 min en vez de 80.
- **`bbdd_guaguas.csv` como nombre del dataset:** a pedido de Diego, se nombra la fuente de datos con el formato que usan las bases de datos reales (`bbdd_...`), no solo "el archivo" o "el texto".
- **Fuente de los datos de ejemplo:** todas las filas usadas (Mateo, Emma, Sofía, Aaron, Julieta, Emilia, Emiliano) son reales, extraídas de `clases-octubre/bbdd-descargadas/otros/RegistroCivil_nombres-inscritos-chile_1920-2021_guaguas.csv`, recortadas a 4 columnas (año, nombre, sexo, cantidad) sin la columna `proporcion`.
- **Actitud "Atención al detalle"** elegida por Diego entre 4 opciones (Precisión, Orden, Curiosidad, Rigor propuestas primero; Atención al detalle, Método, Honestidad con los datos, Asombro/Exploración propuestas en una segunda ronda).
- **Ejercicio 3 vs. Guiada:** ambos manejan `int()` + slicing/índice, pero el Ejercicio 3 sube el nivel al trabajar con dos filas paralelas en vez de una sola — fija el techo de dificultad, como exige la regla 20 del CLAUDE.md raíz.
