# Clase 36 — Pandas 1: abrir y mirar

**Estado:** Spec aprobada — 2026-09-24
**Clase Picuino:** N/A — análisis de datos, sin equivalente directo en el Tutorial Picuino
**Proyecto:** parte del bloque pandas del Proyecto Cierre Octubre (ver `clases/clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md`)

## Contexto

- **Curso:** 4to medio
- **Duración:** ~77 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo lo dictado hasta N°35 (variables, condicionales, ciclos, funciones `def`/`return`, strings, listas con `split()`/índice/slicing). Ninguno es prerrequisito técnico directo de pandas — se asume solo que el curso maneja el flujo general de Colab y `print()`.
- **Contenidos nuevos:** `pd.read_csv(...)` (con `sep=`/`encoding=` cuando el archivo lo necesita), `.head()`, `.shape`, `.columns`, elegir columnas con `df[["col1", "col2"]]`, `.isna().sum()` (contar vacíos) y `.notna()` (filtrar filas por ellos). **Sin funciones propias (`def`) en ningún punto.**
- **Contextos temáticos:** `bbdd_guaguas.csv` (Registro Civil, nombres inscritos en Chile 1920-2021) como hilo conductor de toda la clase — excepción autorizada a la restricción 3 del `CLAUDE.md` raíz, vigente para N°35 a N°40 (ver plan madre §6). Dos archivos chicos de apoyo, ajenos a `guaguas`, para el concepto de `sep=`/`encoding=` y para el desafío: `horario_buses_isla.csv` y `inscripciones_taller.csv` (ya creados en esta carpeta).

## Objetivo

Explorar una base de datos real con pandas —abriéndola, revisando su tamaño y columnas, eligiendo las que importan, y detectando valores faltantes—, con curiosidad.

## Propósito

La curiosidad es hacerle preguntas a algo nuevo antes de usarlo: ¿qué trae?, ¿cuánto tiene?, ¿falta algo? Hoy la practicamos mirando por primera vez una base de datos real con pandas.

## ¿Para qué sirve?

Así arranca cualquier periodista o analista con datos reales: antes de sacar una conclusión, primero mira qué tiene la tabla al frente. Es exactamente el primer paso que cada equipo va a dar en el proyecto de octubre con la base que elija.

## Estructura de la clase

### 1. Haz Ahora (6 min)

La periodista de la clase pasada ya no nos pide una sola fila: ahora nos pasa el archivo completo, `bbdd_guaguas.csv`, con cientos de miles de filas que van desde 1920 hasta 2021. Antes de escribir cualquier código, pensemos en cómo lo miraríamos:

1. Sin abrirlo en Excel, ¿qué dos números necesitas contar para saber "qué tan grande" es el archivo?
2. Antes de sacar cualquier conclusión de un archivo que nunca has visto, ¿revisarías todas las filas de una vez, o unas pocas primero para hacerte una idea?
3. Si la periodista solo necesita el año, el nombre y el sexo —no la cantidad ni la proporción— ¿qué harías con las columnas que no le sirven?
4. Si en algunas filas no se registró el sexo de la guagua, ¿cómo sabrías cuántas filas tienen ese problema?

La periodista, sabiendo que programamos, nos pide ayuda para revisar el archivo completo antes de usarlo en su nota — pero primero hay que mirarlo con calma.

**Respuestas esperadas:**
1. Cuántas filas y cuántas columnas tiene.
2. Unas pocas filas primero, para hacerse una idea.
3. Dejarlas fuera / no usarlas.
4. Contando cuántas filas no tienen ese dato.

### 2. Introducción al Contenido Nuevo (20 min)

**Concepto 1: Abrir un CSV con pandas**
- Definición: pandas es una herramienta que abre un archivo CSV completo y lo convierte en una tabla que Python puede recorrer y manipular de una vez, sin leerlo fila por fila con `.split(",")` como hicimos la clase pasada.

  Así se ve `bbdd_guaguas.csv` una vez que pandas lo convierte en tabla:

  | anio | nombre | sexo | n |
  |---|---|---|---|
  | 2021 | Mateo | M | 3267 |
  | 2021 | Emma | F | 2352 |
  | 2021 | Sofía | F | 2251 |
  | ... | ... | ... | ... |
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  tabla.head()
  ```
- Idea clave: `pd.read_csv("archivo.csv")` abre el archivo completo y lo guarda como tabla.
- Instrucción: Abre `bbdd_guaguas.csv` con pandas y guarda el resultado en una variable llamada `tabla`.
- Punto de partida:
  ```python
  import pandas as pd
  ```
- Resumen tabla: `pd.read_csv("archivo.csv")`

**Concepto 2: Cuando el archivo no se abre bien — `sep=` y `encoding=`**
- Definición: A veces pandas no separa bien las columnas (el archivo usa `;` en vez de `,`) o las letras con tilde salen raras (`ó` se ve como `Ã³`). Dos síntomas, dos correcciones: si todo el contenido cae en una sola columna, falta `sep=";"`; si aparecen símbolos raros, falta `encoding=`.
- Ejemplo:
  ```python
  import pandas as pd

  horarios = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clase-36-pandas1-abrir-mirar/horario_buses_isla.csv", sep=";")
  horarios.head()
  ```
- Idea clave: si todo cae en una columna, falta `sep=";"`; si aparecen símbolos raros, falta `encoding=`.
- Instrucción: Abre `horario_buses_isla.csv` indicando que las columnas están separadas por punto y coma.
- Punto de partida:
  ```python
  import pandas as pd
  ```
- Resumen tabla: `pd.read_csv("archivo.csv", sep=";", encoding="utf-8")`

**Concepto 3: Mirar la tabla**
- Definición: Antes de trabajar con una tabla hay que mirarla: `.head()` muestra las primeras filas, `.shape` dice cuántas filas y columnas tiene (en ese orden), y `.columns` lista los nombres exactos de las columnas.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print("Filas y columnas:", tabla.shape)
  print("Columnas:", list(tabla.columns))
  tabla.head()
  ```
- Idea clave: `.head()` muestra las primeras filas, `.shape` da (filas, columnas), `.columns` lista los nombres.
- Instrucción: Imprime la forma de `tabla` (filas y columnas) y sus nombres de columna, y luego muestra sus primeras filas.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  ```
- Resumen tabla: `tabla.head()` / `tabla.shape` / `tabla.columns`

**Concepto 4: Elegir columnas**
- Definición: Cuando la tabla tiene columnas que no necesitamos, se eligen solo las que importan con doble corchete: una lista con los nombres exactos de las columnas deseadas.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  columnas_relevantes = tabla[["anio", "nombre", "sexo"]]
  columnas_relevantes.head()
  ```
- Idea clave: `tabla[["col1", "col2"]]` (con doble corchete) deja solo esas columnas.
- Instrucción: Quédate solo con las columnas `anio` y `nombre` de `tabla`, guardadas en una variable nueva.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  ```
- Resumen tabla: `tabla[["col1", "col2"]]`

**Concepto 5: Contar y filtrar vacíos**
- Definición: `.isna()` marca `True` donde falta un dato; sumándolo con `.sum()` se cuenta cuántos vacíos hay por columna. `.notna()` hace lo contrario (`True` donde sí hay dato) y se puede usar como condición para quedarse solo con las filas completas — la misma técnica de filtrar filas, con esta condición.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print("Vacíos en 'sexo':", tabla["sexo"].isna().sum())

  tabla_con_sexo = tabla[tabla["sexo"].notna()]
  print("Filas con sexo registrado:", len(tabla_con_sexo))
  ```
- Idea clave: `.isna().sum()` cuenta vacíos por columna; `tabla[tabla["col"].notna()]` deja solo las filas con dato.
- Instrucción: Cuenta cuántos vacíos tiene la columna `sexo`, y luego quédate solo con las filas donde sí hay un valor de `sexo`.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  ```
- Resumen tabla: `tabla["col"].isna().sum()` / `tabla[tabla["col"].notna()]`

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Olvidar `import pandas as pd` | `NameError: name 'pd' is not defined` | Agregar el `import` al inicio de la celda |
| Escribir un nombre de columna distinto al de `.columns` (mayúscula, tilde, espacio) | `KeyError` | Copiar el nombre exacto desde `.columns` |
| Usar corchete simple en vez de doble para elegir varias columnas (`tabla["anio", "nombre"]`) | Error | Recordar el doble corchete: `tabla[["anio", "nombre"]]` |

### 3. Práctica Guiada (22 min)

La periodista ya tiene el archivo completo y, antes de escribir su nota, quiere saber si puede confiar en el dato de sexo: cuántos registros no lo tienen, y cuántos sí.

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas.
- Mostrar cuántas filas y columnas tiene en total.
- Quedarse solo con las columnas año, nombre y sexo.
- Contar cuántos valores faltan en la columna sexo.
- Quedarse solo con las filas donde sí hay dato de sexo, e imprimir cuántas quedaron.

**Resultado esperado:**
```
Filas y columnas: (858782, 5)
Vacíos en 'sexo': 4293
Filas con sexo registrado: 854489
```

- Solución:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print("Filas y columnas:", tabla.shape)

  columnas_relevantes = tabla[["anio", "nombre", "sexo"]]
  print("Vacíos en 'sexo':", columnas_relevantes["sexo"].isna().sum())

  tabla_con_sexo = columnas_relevantes[columnas_relevantes["sexo"].notna()]
  print("Filas con sexo registrado:", len(tabla_con_sexo))
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

**Ejercicio 0a — Práctica directa: abrir y mirar**
Aplica el patrón base de abrir y mirar una tabla:

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas, guardado en una variable llamada `tabla`.
- Imprimir su forma (filas y columnas) y la lista de sus columnas.
- Mostrar sus primeras filas.

**Resultado esperado:**
```
Filas y columnas: (858782, 5)
Columnas: ['anio', 'nombre', 'sexo', 'n', 'proporcion']
```

- Solución:
  ```python
  # Tu solución — Ejercicio 0a
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print("Filas y columnas:", tabla.shape)
  print("Columnas:", list(tabla.columns))
  tabla.head()
  ```

**Celda de verificación:**
```python
verificar_ejercicio_0a()
```

**Ejercicio 0b — Práctica directa: contar y filtrar vacíos**
Aplica el patrón base de contar y filtrar vacíos, ahora en la columna `n`:

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas.
- Contar cuántos vacíos tiene la columna `n` e imprimirlo.
- Quedarse solo con las filas donde `n` sí tiene dato, e imprimir cuántas quedaron.

**Resultado esperado:**
```
Vacíos en 'n': 4293
Filas con 'n' registrado: 854489
```

- Solución:
  ```python
  # Tu solución — Ejercicio 0b
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print("Vacíos en 'n':", tabla["n"].isna().sum())

  tabla_con_n = tabla[tabla["n"].notna()]
  print("Filas con 'n' registrado:", len(tabla_con_n))
  ```

**Celda de verificación:**
```python
verificar_ejercicio_0b()
```

**Ejercicio 1 — El profe de Historia**
El profesor de Historia está preparando una actividad sobre nombres que se repitieron en distintas épocas, pero no necesita saber cuántas veces se registró cada nombre ni qué proporción representa — solo el año y el nombre. Nos pasa `bbdd_guaguas.csv` y nos pide dejar la tabla lista con solo esas dos columnas.

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas.
- Quedarse solo con las columnas año y nombre, guardadas en una variable nueva.
- Imprimir la forma final de esa tabla reducida.
- Mostrar sus primeras filas.

<details>
<summary>💡 Pista — doble corchete</summary>
Para elegir más de una columna a la vez, usa doble corchete: una lista con los nombres exactos, tal como aparecen en `.columns`.
</details>

**Resultado esperado:**
```
Forma final: (858782, 2)
```

- Solución:
  ```python
  # Tu solución — Ejercicio 1
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  columnas_relevantes = tabla[["anio", "nombre"]]
  print("Forma final:", columnas_relevantes.shape)
  columnas_relevantes.head()
  ```

**Celda de verificación:**
```python
verificar_ejercicio_1()
```

**Ejercicio 2 — Dos columnas a la vez**
Un compañero del equipo de datos quiere saber, de un vistazo, cuántos vacíos hay en las dos columnas más importantes del proyecto: sexo y cantidad registrada.

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas.
- Contar los vacíos de las columnas sexo y `n` al mismo tiempo, con una sola instrucción.
- Imprimir el resultado.

<details>
<summary>💡 Pista — contar varias columnas juntas</summary>
`.isna().sum()` funciona igual sobre una tabla con varias columnas elegidas — no hace falta repetir la instrucción para cada una.
</details>

**Resultado esperado:**
```
sexo    4293
n       4293
dtype: int64
```

- Solución:
  ```python
  # Tu solución — Ejercicio 2
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  print(tabla[["sexo", "n"]].isna().sum())
  ```

**Celda de verificación:**
```python
verificar_ejercicio_2()
```

**Ejercicio 3 — Una versión liviana para el proyecto**
El equipo de datos del proyecto pidió una versión más liviana de la base para trabajar más rápido: solo año, nombre y sexo — y sin las filas donde no se registró el sexo, porque esas no les sirven para el análisis.

**El programa debe:**
- Abrir `bbdd_guaguas.csv` con pandas.
- Quedarse solo con las columnas año, nombre y sexo.
- Mostrar cuántas filas y columnas tiene esa tabla reducida, antes de sacar las filas sin sexo.
- Quedarse solo con las filas donde sí hay dato de sexo.
- Mostrar cuántas filas y columnas quedaron después.

<details>
<summary>💡 Pista — un paso a la vez</summary>
Primero elige las columnas, y sobre esa tabla más chica aplica el filtro de `sexo` — el resultado final es el mismo que filtrar antes, pero así vas armando la tabla paso a paso.
</details>

**Resultado esperado:**
```
Antes de filtrar: (858782, 3)
Después de filtrar: (854489, 3)
```

- Solución:
  ```python
  # Tu solución — Ejercicio 3
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv")
  columnas_relevantes = tabla[["anio", "nombre", "sexo"]]
  print("Antes de filtrar:", columnas_relevantes.shape)

  tabla_final = columnas_relevantes[columnas_relevantes["sexo"].notna()]
  print("Después de filtrar:", tabla_final.shape)
  ```

**Celda de verificación:**
```python
verificar_ejercicio_3()
```

**Ejercicio 4 — Desafío: el archivo que no se abre bien**
Un profesor de otro colegio te pasa un registro de asistencia a talleres extracurriculares, `inscripciones_taller.csv`, pero cuando lo abres con pandas todo el contenido cae en una sola columna.

**El programa debe:**
- Descubrir por qué el archivo no se abre bien y corregirlo.
- Mostrar su forma y sus columnas una vez abierto correctamente.
- Contar cuántas filas no tienen dato de asistencia.
- Quedarse solo con las filas donde sí hay un dato de asistencia, e imprimir cuántas quedaron.

**Resultado esperado:**
```
Forma: (6, 3)
Columnas: ['taller', 'estudiante', 'asistencia']
Vacíos en 'asistencia': 2
Filas con asistencia registrada: 4
```

- Solución:
  ```python
  # Tu solución — Ejercicio 4
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clase-36-pandas1-abrir-mirar/inscripciones_taller.csv", sep=";")
  print("Forma:", tabla.shape)
  print("Columnas:", list(tabla.columns))
  print("Vacíos en 'asistencia':", tabla["asistencia"].isna().sum())

  tabla_con_asistencia = tabla[tabla["asistencia"].notna()]
  print("Filas con asistencia registrada:", len(tabla_con_asistencia))
  ```

**Celda de verificación:**
```python
verificar_ejercicio_4()
```

### 5. Ticket de Salida (7 min)

**Pregunta 1:**
```python
import pandas as pd

tabla = pd.read_csv("mini.csv")
print(tabla.shape)  # <- esta línea
```
Si `mini.csv` tiene 5 filas y 3 columnas, ¿qué imprime esta línea?
- A: `(3, 5)`
- B: `(5, 3)`
- C: `5`
- D: `[5, 3]`

**Respuesta correcta:** B
**Justificación:** `.shape` siempre entrega primero las filas y después las columnas, como una tupla `(filas, columnas)`.

**Pregunta 2:**
```python
tabla = pd.read_csv("mini.csv")
columnas = tabla["nombre", "curso"]  # <- esta línea
```
¿Qué ocurre al ejecutar esta línea?
- A: Muestra las columnas `nombre` y `curso` correctamente
- B: Muestra todas las columnas de la tabla
- C: Da error, porque falta un corchete extra alrededor de la lista de nombres
- D: Cambia el orden de las columnas

**Respuesta correcta:** C
**Justificación:** para elegir más de una columna se necesita doble corchete (`tabla[["nombre", "curso"]]`): una lista de nombres dentro del corchete de selección. Con un solo corchete, pandas no entiende que son dos nombres de columna.

**Pregunta 3:**
```python
import pandas as pd

tabla = pd.DataFrame({
    "nombre": ["Ana", "Beto", "Cata"],
    "sexo": ["F", None, "M"],
})
print(tabla["sexo"].isna().sum())
```
¿Qué imprime este programa?
- A: `3`
- B: `0`
- C: `True`
- D: `1`

**Respuesta correcta:** D
**Justificación:** `.isna()` marca `True` solo en la fila donde falta el dato (la de Beto); `.sum()` cuenta esos `True` como si fueran 1, dando 1 en total.

### Cierre (5 min)

**Objetivo de la clase:** Explorar una base de datos real con pandas —abriéndola, revisando su tamaño y columnas, eligiendo las que importan, y detectando valores faltantes—, con curiosidad.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes abriendo y mirando una base de datos real con pandas, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otro archivo real de tu vida (notas, gastos, un catastro, una planilla del colegio) usarías esta misma curiosidad de mirar antes de sacar conclusiones?

**Nota obligatoria en la clase:** decir explícito que pandas NO entra en la Evaluación de Funciones+Strings+Listas (fecha aún sin definir) — para no generar ansiedad antes de la prueba.

## Decisiones de diseño relevantes

- **Dataset real:** se reutiliza `clases/clases-octubre/entregas-ideales/datos/guaguas_maquillada.csv` (858.782 filas × 5 columnas; 4.293 vacíos en `sexo` y en `n`), copiado a `clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv` (misma convención de nombre que fijó N°35). **Distribución resuelta (2026-09-24):** todo `pd.read_csv(...)` de esta clase (`bbdd_guaguas.csv`, `horario_buses_isla.csv`, `inscripciones_taller.csv`) apunta a la URL raw de GitHub del archivo ya pusheado, en vez de un nombre de archivo suelto — así cada estudiante lo lee directo en su sesión de Colab sin subir nada a mano ni montar Google Drive. `bbdd_guaguas.csv` queda en una carpeta compartida (`clases-octubre/datos-compartidos/`, no en la carpeta de esta clase) porque N°37-N°40 reutilizan el mismo archivo — evita 5 copias de 23 MB. Ver `clases-octubre/datos-compartidos/README.md`.
- **Celda de preparación (`!pip install pandas`) — agregada a pedido explícito de Diego (2026-09-24).** pandas ya viene preinstalado en el entorno estándar de Colab, así que no es estrictamente necesaria, pero Diego la quiere como respaldo antes de la primera celda de código de la clase. Se insertó manualmente en `Clase.ipynb` (no es un campo que el generador de `generar-colab-clase` parsee desde el spec todavía) — si se regenera el notebook desde este spec, hay que volver a insertarla a mano justo después de la celda de intro y antes del Haz Ahora.
- **Tabla markdown de vista previa (Concepto 1) — nuevo default para esta clase, a pedido de Diego (2026-09-24):** cualquier clase que abra un archivo/base de datos real por primera vez incluye, en el concepto donde se presenta esa apertura, una tabla markdown chica (3-4 filas reales + `...`) mostrando cómo se ve la tabla ya abierta — para que los estudiantes se la imaginen antes de ejecutar el código. Se registra también como default en `disenar-clase/SKILL.md`.
- **Dos archivos chicos de apoyo, creados junto a esta spec:** `horario_buses_isla.csv` (Concepto 2, `sep=";"`) e `inscripciones_taller.csv` (Ejercicio 4, mismo síntoma sin avisar). Ninguno usa el contexto `guaguas` a propósito — son la excepción puntual dentro de la excepción, porque necesitan un archivo realmente mal separado, y `guaguas` no lo está.
- **`sep=`/`encoding=` como concepto propio (Concepto 2), no solo mención al pasar:** aunque `guaguas` no los necesita, el resto de las 9 bases del proyecto sí (ver `Catastro de Bases y Banco de Preguntas...md` §1: DEMRE y SIMCE requieren `sep=";"`; SIMCE y Matrícula requieren `encoding="latin-1"`) — se enseña ahora para que cada equipo lo reconozca en octubre.
- **Sin filtrado por valor específico (`tabla[tabla["col"] == valor]`):** aunque es la misma técnica sintáctica que `.notna()`, filtrar por un valor exacto es contenido propio de N°38 ("el regalo" de normalizar `sexo`) — no se adelanta aquí, ni en la Guiada ni en la Independiente.
- **Ejercicio 3 fija el techo de dificultad** (combina elegir columnas + filtrar vacíos, reportando forma antes/después) — mismo nivel que retoma la Guiada, según la regla 20 del `CLAUDE.md` raíz.
- **`guaguas` como hilo conductor único:** Haz Ahora, ICN, Guiada, Ejercicios 0a-3 (todos, salvo el Ejercicio 4 desafío) usan `bbdd_guaguas.csv` — excepción explícita y autorizada a la restricción 3 del `CLAUDE.md` raíz, vigente para todo el bloque N°35-N°40 del proyecto.
