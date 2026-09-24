# Clase 37 — Pandas 2, Clase 1 (A+C): limpiar a número + descartar filas sucias

**Estado:** Spec aprobada — 2026-09-24
**Clase Picuino:** N/A — análisis de datos, sin equivalente directo en el Tutorial Picuino
**Proyecto:** parte del bloque pandas del Proyecto Cierre Octubre (ver `clases/clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md`)

## Contexto

- **Curso:** 4to medio
- **Duración:** ~77 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo lo dictado hasta N°36 (Pandas 1 — abrir un CSV con `read_csv`, `.head()`, `.shape`, `.columns`, elegir columnas, `.isna()`/`.notna()`).
- **Contenidos nuevos:** leer una columna forzando `dtype={"columna": "str"}`, `.str.strip()`, `.str.replace(".", "", regex=False)`, `pd.to_numeric(..., errors="coerce")`, y reutilizar `.notna()` (ya visto) sobre una columna derivada. **Sin funciones propias (`def`) en ningún punto.**
- **Contextos temáticos:** `bbdd_guaguas.csv` como hilo conductor único de toda la clase — excepción autorizada a la restricción 3 del `CLAUDE.md` raíz, vigente para N°35 a N°40.

## Objetivo

Convertir una columna numérica sucia en datos confiables, descartando solo las filas que de verdad no se puedan recuperar, con perseverancia.

## Propósito

La perseverancia es seguir intentando arreglar algo aunque el primer intento no alcance. Hoy la practicamos limpiando una columna de datos sucia hasta dejarla realmente utilizable.

## ¿Para qué sirve?

Cualquiera que trabaje con datos reales —un portal público, un Excel exportado, una encuesta— se topa con números guardados como texto por errores de formato; limpiarlos antes de analizar es trabajo real, no un ejercicio de clase. En un par de semanas cada equipo va a hacer exactamente esto con la base que eligió para el proyecto.

## Estructura de la clase

### 1. Haz Ahora (6 min)

La periodista de la clase pasada ya tiene la tabla reducida a año, nombre y sexo — pero ahora quiere escribir sobre los nombres que más se repitieron, y para eso necesita confiar en la columna que cuenta cuántas guaguas tuvo cada nombre. El problema: cuando la mira de cerca, hay valores como `"2.908"`, `" 15 "`, y algunas filas completamente vacías.

1. Si ves el valor `"2.908"` escrito así en una tabla de conteos, ¿qué cantidad real crees que representa: dos coma nueve cero ocho, o dos mil novecientos ocho?
2. Si un valor viene con espacios de más alrededor del número (como `" 15 "`), ¿ese es un dato realmente distinto, o es el mismo 15 solo mal escrito?
3. Si una fila no tiene ningún valor en esa columna, ¿tiene sentido inventar un número para no perderla, o es mejor dejarla fuera del análisis?
4. Antes de confiar en que un programa "leyó bien" una columna de números, ¿cómo te asegurarías de que no se equivocó en silencio?

La periodista, sabiendo que programamos, nos pide ayuda para dejar esta columna de conteos realmente confiable antes de escribir su nota — pero el primer intento puede no alcanzar, así que toca perseverar.

**Respuestas esperadas:**
1. Dos mil novecientos ocho (separador de miles).
2. Es el mismo 15, solo escrito con espacios de más.
3. Mejor dejarla fuera — inventar un valor sería mentir sobre el dato.
4. Revisando algunos valores concretos después de que el programa los "arregló", no solo confiando en que no tiró error.

### 2. Introducción al Contenido Nuevo (25 min)

**Concepto 1: Leer con cuidado**
- Definición: Antes de limpiar cualquier columna, hay que asegurarse de que pandas no la haya "arreglado" en secreto. Si una columna tiene números escritos de forma rara (como con punto de miles), pandas puede interpretarlos igual como si fueran números válidos —aunque el valor quede mal— sin mostrar ningún error. Para evitarlo, se le dice explícitamente que trate esa columna como texto con `dtype={"columna": "str"}` al leer el archivo: así ningún valor se transforma solo, y queda tal cual está escrito en el archivo original.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("guaguas.csv", dtype={"n": "str"})
  print(tabla["n"].dtype)
  tabla[["n"]].head()
  ```
- Idea clave: `dtype={"columna": "str"}` en `pd.read_csv()` evita que pandas adivine mal el tipo de una columna sucia.
- Instrucción: Abre `bbdd_guaguas.csv` con pandas, indicando que la columna `n` se debe leer como texto.
- Punto de partida:
  ```python
  import pandas as pd
  ```
- Resumen tabla: `pd.read_csv(archivo, dtype={"col": "str"})`

**Concepto 2: Sacar los espacios sobrantes**
- Definición: Algunos valores de texto vienen con espacios de más al inicio o al final (por ejemplo `" 15 "`), que no cambian el número pero sí impiden convertirlo directamente. `.str.strip()` saca esos espacios sobrantes, dejando el texto limpio por los bordes.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("guaguas.csv", dtype={"n": "str"})
  tabla["n_sin_espacios"] = tabla["n"].str.strip()
  tabla[["n", "n_sin_espacios"]].head()
  ```
- Idea clave: `.str.strip()` saca los espacios sobrantes al inicio y al final de un texto.
- Instrucción: Saca los espacios sobrantes de la columna `n`, guardando el resultado en una columna nueva llamada `n_sin_espacios`.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv", dtype={"n": "str"})
  ```
- Resumen tabla: `columna.str.strip()`

**Concepto 3: Sacar el punto de miles**
- Definición: En Chile los números grandes suelen escribirse con un punto como separador de miles (`"2.908"` para 2908). Ese punto no es un error de tipeo, pero hay que sacarlo antes de convertir el texto a número, o el programa lo va a confundir con un punto decimal. `.str.replace(".", "", regex=False)` saca todos los puntos de un texto.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("guaguas.csv", dtype={"n": "str"})
  tabla["n_sin_puntos"] = tabla["n"].str.strip().str.replace(".", "", regex=False)
  tabla[["n", "n_sin_puntos"]].head()
  ```
- Idea clave: `.str.replace(".", "", regex=False)` saca todos los puntos de un texto.
- Instrucción: Sácale el punto de miles a `n_sin_espacios`, guardando el resultado en una columna nueva llamada `n_sin_puntos`.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv", dtype={"n": "str"})
  tabla["n_sin_espacios"] = tabla["n"].str.strip()
  ```
- Resumen tabla: `columna.str.replace(".", "", regex=False)`

**Concepto 4: Convertir a número real**
- Definición: Aunque `n_sin_puntos` ya se ve como un número, para Python sigue siendo texto — no se puede sumar ni ordenar todavía. `pd.to_numeric()` lo convierte a número real. Si algún valor no se puede convertir de ninguna forma, `errors="coerce"` lo deja como `NaN` en vez de detener el programa con un error.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("guaguas.csv", dtype={"n": "str"})
  texto_limpio = tabla["n"].str.strip().str.replace(".", "", regex=False)
  tabla["cantidad_guaguas"] = pd.to_numeric(texto_limpio, errors="coerce")
  tabla[["n", "cantidad_guaguas"]].head()
  ```
- Idea clave: `pd.to_numeric(columna, errors="coerce")` convierte texto a número real, dejando `NaN` donde no se pudo.
- Instrucción: Convierte `n_sin_puntos` a número real, guardado en una columna nueva llamada `cantidad_guaguas`.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv", dtype={"n": "str"})
  tabla["n_sin_espacios"] = tabla["n"].str.strip()
  tabla["n_sin_puntos"] = tabla["n_sin_espacios"].str.replace(".", "", regex=False)
  ```
- Resumen tabla: `pd.to_numeric(columna, errors="coerce")`

**Concepto 5: Descartar filas que no se pudieron limpiar**
- Definición: Después de convertir, algunas filas quedan en `NaN` —porque nunca tuvieron dato, o porque el formato no se pudo arreglar con esta técnica. `.notna()` identifica las filas donde sí quedó un número válido, y se usa como filtro para quedarse solo con esas, igual que ya se hizo con `sexo` en la clase pasada.
- Ejemplo:
  ```python
  import pandas as pd

  tabla = pd.read_csv("guaguas.csv", dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla_limpia = tabla[tabla["cantidad_guaguas"].notna()]
  print("Filas antes:", len(tabla))
  print("Filas después:", len(tabla_limpia))
  ```
- Idea clave: `tabla[tabla["col"].notna()]` deja solo las filas donde la limpieza sí funcionó.
- Instrucción: Quédate solo con las filas donde `cantidad_guaguas` sí tiene un valor, e imprime cuántas quedaron.
- Punto de partida:
  ```python
  import pandas as pd

  tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv", dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  ```
- Resumen tabla: `tabla[tabla["col"].notna()]`

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Olvidar `dtype={"n": "str"}` al leer | pandas ya convirtió mal los valores sucios a número, sin ningún error visible, y el resto de la limpieza ya no tiene nada que arreglar | Agregar `dtype={"columna": "str"}` en `pd.read_csv()` para cualquier columna que se vaya a limpiar |
| Olvidar `errors="coerce"` en `pd.to_numeric()` | `ValueError` al primer valor que no se puede convertir | Agregar `errors="coerce"` para que esos valores queden como `NaN` en vez de detener el programa |
| Usar `.str.replace()` o `.str.strip()` sobre una columna que ya es número | `AttributeError: Can only use .str accessor with string values` | Verificar con `.dtype` que la columna sea texto antes de usar `.str` |

### 3. Práctica Guiada (18 min)

La periodista ya tiene claro el problema de la columna de conteos, y ahora quiere saber cuántas filas realmente puede usar para su nota, antes de empezar a contar nombres populares.

**El programa debe:**
- Abrir `bbdd_guaguas.csv`, indicando que la columna de conteos se debe leer como texto.
- Sacarle los espacios sobrantes y el punto de miles a esa columna.
- Convertirla a número real, guardada en una columna nueva.
- Mostrar cuántas filas tenía la tabla antes de limpiar.
- Quedarse solo con las filas donde la limpieza sí funcionó, y mostrar cuántas quedaron.

**Resultado esperado:**
```
Filas antes: 858782
Filas después: 854489
```

- Solución:
  ```python
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )

  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  print("Filas antes:", len(tabla))

  tabla_limpia = tabla[tabla["cantidad_guaguas"].notna()]
  print("Filas después:", len(tabla_limpia))
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
```

**Ejercicio 0a — Práctica directa: limpiar a número**
Aplica el patrón base de limpiar una columna sucia a número:

**El programa debe:**
- Abrir `bbdd_guaguas.csv`, leyendo la columna `n` como texto.
- Limpiarla a número real (sin espacios ni punto de miles), guardada en una columna nueva llamada `cantidad_guaguas`.
- Imprimir cuántos valores quedaron con un número válido (no nulos) después de limpiar.

**Resultado esperado:**
```
Valores limpios: 854489
```

- Solución:
  ```python
  # Tu solución — Ejercicio 0a
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  print("Valores limpios:", tabla["cantidad_guaguas"].notna().sum())
  ```

**Celda de verificación:**
```python
verificar_ejercicio_0a()
```

**Ejercicio 0b — Práctica directa: descartar con `.notna()`**
Aplica el patrón base de quedarte solo con las filas ya limpias:

**El programa debe:**
- Abrir `bbdd_guaguas.csv` y limpiar `cantidad_guaguas` igual que en el ejercicio anterior.
- Quedarte solo con las filas donde `cantidad_guaguas` sí tiene un valor.
- Imprimir cuántas filas quedaron.

**Resultado esperado:**
```
Filas con cantidad_guaguas válida: 854489
```

- Solución:
  ```python
  # Tu solución — Ejercicio 0b
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla_limpia = tabla[tabla["cantidad_guaguas"].notna()]
  print("Filas con cantidad_guaguas válida:", len(tabla_limpia))
  ```

**Celda de verificación:**
```python
verificar_ejercicio_0b()
```

**Ejercicio 1 — Una versión limpia para el resto del equipo**
Un compañero del equipo de datos necesita una versión de la tabla con año, nombre y la cantidad de guaguas ya limpia — sin las filas que no se pudieron arreglar.

**El programa debe:**
- Abrir `bbdd_guaguas.csv`, leyendo la columna de conteos como texto.
- Limpiarla a número real, guardada en `cantidad_guaguas`.
- Quedarse solo con las columnas año, nombre y `cantidad_guaguas`.
- Quedarse solo con las filas donde `cantidad_guaguas` sí tiene un valor.
- Imprimir cuántas filas y columnas quedaron.

<details>
<summary>💡 Pista — el orden importa</summary>
Limpia la columna sobre la tabla completa primero, y recién después elige las columnas y filtra las filas válidas.
</details>

**Resultado esperado:**
```
Forma final: (854489, 3)
```

- Solución:
  ```python
  # Tu solución — Ejercicio 1
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  columnas_relevantes = tabla[["anio", "nombre", "cantidad_guaguas"]]
  tabla_limpia = columnas_relevantes[columnas_relevantes["cantidad_guaguas"].notna()]
  print("Forma final:", tabla_limpia.shape)
  ```

**Celda de verificación:**
```python
verificar_ejercicio_1()
```

**Ejercicio 2 — Cuánto se perdió al limpiar**
El profe de Historia quiere saber cuántos registros se van a perder al limpiar la columna de conteos, antes de decidir si esta base le sirve para su actividad.

**El programa debe:**
- Abrir `bbdd_guaguas.csv`, leyendo la columna de conteos como texto.
- Limpiarla a número real.
- Contar cuántos valores quedaron sin poder limpiarse (nulos).
- Imprimir ese número.

<details>
<summary>💡 Pista — lo opuesto de notna()</summary>
`.isna()` marca las filas sin dato válido; súmalas con `.sum()`, igual que ya hiciste con `sexo` en la clase pasada.
</details>

**Resultado esperado:**
```
Valores que no se pudieron limpiar: 4293
```

- Solución:
  ```python
  # Tu solución — Ejercicio 2
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  print("Valores que no se pudieron limpiar:", tabla["cantidad_guaguas"].isna().sum())
  ```

**Celda de verificación:**
```python
verificar_ejercicio_2()
```

**Ejercicio 3 — La versión que se va a usar en el proyecto**
El equipo de datos del proyecto pidió una versión bien liviana de la base para practicar: solo el nombre y la cantidad de guaguas, ya limpia — y quiere ver cuánto cambió el tamaño de la tabla en el proceso.

**El programa debe:**
- Abrir `bbdd_guaguas.csv`, leyendo la columna de conteos como texto.
- Quedarse solo con las columnas nombre y conteo (aún sin limpiar), y mostrar su forma.
- Limpiar la columna de conteo a número real.
- Quedarse solo con las columnas nombre y la cantidad ya limpia, y con las filas donde la limpieza funcionó.
- Mostrar la forma final.

<details>
<summary>💡 Pista — un paso a la vez</summary>
Limpia siempre sobre la tabla completa (nunca sobre una versión ya recortada de columnas) — así evitas advertencias de pandas. Recorta las columnas al final, sobre el resultado ya limpio.
</details>

**Resultado esperado:**
```
Antes de limpiar: (858782, 2)
Después de limpiar: (854489, 2)
```

- Solución:
  ```python
  # Tu solución — Ejercicio 3
  import pandas as pd

  tabla = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  columnas_relevantes = tabla[["nombre", "n"]]
  print("Antes de limpiar:", columnas_relevantes.shape)

  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla_final = tabla[["nombre", "cantidad_guaguas"]]
  tabla_final = tabla_final[tabla_final["cantidad_guaguas"].notna()]
  print("Después de limpiar:", tabla_final.shape)
  ```

**Celda de verificación:**
```python
verificar_ejercicio_3()
```

**Ejercicio 4 — Desafío: lo que casi se nos escapa**
Antes de conocer la técnica de hoy, alguien del equipo leyó la base sin decirle a pandas que tratara la columna de conteos como texto, y sumó todos sus valores sin darse cuenta de que varios habían quedado mal calculados en silencio.

**El programa debe:**
- Abrir `bbdd_guaguas.csv` SIN indicar el tipo de la columna de conteos, y sumar todos sus valores tal como quedaron.
- Abrir de nuevo, esta vez leyendo la columna de conteos como texto y aplicando la limpieza completa.
- Sumar los valores ya limpios.
- Imprimir ambos totales, para comparar.

<details>
<summary>💡 Pista — compara el total</summary>
Si una columna se leyó mal, sumar sus valores va a dar un número más chico que si se leyó y limpió bien — ahí está la evidencia de lo que se estaba perdiendo en silencio.
</details>

**Resultado esperado:**
```
Suma leyendo mal: 21909375
Suma leyendo bien: 22000272
```

- Solución:
  ```python
  # Tu solución — Ejercicio 4
  import pandas as pd

  tabla_mal_leida = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"
  )
  print("Suma leyendo mal:", round(tabla_mal_leida["n"].sum()))

  tabla_bien_leida = pd.read_csv(
      "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv",
      dtype={"n": "str"},
  )
  tabla_bien_leida["cantidad_guaguas"] = pd.to_numeric(
      tabla_bien_leida["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  print("Suma leyendo bien:", round(tabla_bien_leida["cantidad_guaguas"].sum()))
  ```

**Celda de verificación:**
```python
verificar_ejercicio_4()
```

### 5. Ticket de Salida (7 min)

**Pregunta 1:**
```python
import pandas as pd

tabla = pd.read_csv("mini.csv")  # sin dtype
print(tabla["cantidad"].dtype)  # <- esta línea
```
Si `mini.csv` tiene una columna `cantidad` con valores como `"1.234"` y `"56"`, ¿qué imprime esta línea?
- A: `object`
- B: `str`
- C: `float64`
- D: Error, porque pandas no puede leer texto y números juntos

**Respuesta correcta:** C
**Justificación:** pandas convierte toda la columna a `float64` porque todos los valores —incluido `"1.234"`— son números válidos para él, aunque el valor quede semánticamente mal (1,234 en vez de 1234). No hay error ni aviso.

**Pregunta 2:**
```python
import pandas as pd

valores = pd.Series(["10", "abc", "30"])
resultado = pd.to_numeric(valores, errors="coerce")  # <- esta línea
print(resultado.tolist())
```
¿Qué imprime este programa?
- A: `[10, 'abc', 30]`
- B: `[10.0, nan, 30.0]`
- C: Error, porque `"abc"` no es un número
- D: `[10, 0, 30]`

**Respuesta correcta:** B
**Justificación:** `errors="coerce"` convierte lo que sí se puede, y deja `NaN` —no cero, no el texto original— en los valores que no se pueden convertir a número. El programa no se detiene.

**Pregunta 3:**
```python
import pandas as pd

tabla = pd.DataFrame({"n": ["1.500", "200", None]})
tabla["limpio"] = pd.to_numeric(
    tabla["n"].str.replace(".", "", regex=False), errors="coerce"
)
print(tabla["limpio"].notna().sum())  # <- esta línea
```
¿Qué imprime esta línea?
- A: `2`
- B: `3`
- C: `1`
- D: `0`

**Respuesta correcta:** A
**Justificación:** `"1.500"` y `"200"` se limpian y quedan como número válido; el valor `None` original nunca tuvo dato, así que sigue siendo `NaN`. `.notna().sum()` cuenta los 2 que sí quedaron con valor.

### Cierre (5 min)

**Objetivo de la clase:** Convertir una columna numérica sucia en datos confiables, descartando solo las filas que de verdad no se puedan recuperar, con perseverancia.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes limpiando una columna de datos sucia hasta dejarla realmente confiable, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación de tu vida el primer intento no alcanzó y tuviste que perseverar hasta lograrlo?

**Nota obligatoria en la clase:** decir explícito que pandas NO entra en la Evaluación de Funciones+Strings+Listas (fecha aún sin definir) — para no generar ansiedad antes de la prueba.

## Decisiones de diseño relevantes

- **Hallazgo técnico previo a esta spec (2026-09-24), ya resuelto:** `pd.read_csv()` sin más, sobre `bbdd_guaguas.csv`, convierte la columna `n` a `float64` en silencio — un valor sucio con punto de miles (`"2.908"`) se lee como el número 2.908 en vez de 2908, sin error ni `NaN`. Fix: `pd.read_csv(..., dtype={"n": "str"})`, verificado sin pérdida de datos (4.293 nulos antes de leer = 4.293 nulos después de limpiar). Detalle completo y la nota para N°39 en `clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` §6. No requirió tocar `maquillar_guaguas.py` ni regenerar ningún archivo.
- **Concepto 1 dividido en 5 pasos graduales (pedido explícito de Diego, 2026-09-24):** la cadena completa (`dtype` → `strip` → `replace` → `to_numeric` → `notna`) se enseña de a una pieza por vez, cada una con su propio "Escríbelo tú" que retoma el código acumulado del concepto anterior — nunca de una vez, dado que el prompt original ya marcaba esta técnica como "la más densa del bloque".
- **Sin filtrado por valor específico (`tabla[tabla["col"] == valor]`) ni `groupby`:** aunque hubiera sido natural para el Ejercicio 1 (ej. sumar solo el año 2021), esas técnicas están reservadas para N°38 (filtrar por valor) y N°39 (agrupar) — no se adelantan aquí. Los ejercicios de esta clase evitan explícitamente el operador `==` para filtrar filas.
- **`guaguas` como hilo conductor único:** todos los ejercicios (Haz Ahora, ICN, Guiada, 0a-4) usan `bbdd_guaguas.csv` — a diferencia de N°36, esta clase no necesitó un archivo de apoyo aparte para el desafío, porque el propio hallazgo técnico de esta sesión (leer mal vs. leer bien) ya daba material suficiente para un Ejercicio 4 con sentido.
- **Actitud Perseverancia, elegida entre 8 opciones ofrecidas en dos tandas** (la primera tanda — Rigor/Precisión/Criterio/Paciencia — se descartó por sentirse "todas muy parecidas"; la segunda —Honestidad/Responsabilidad/Humildad/Perseverancia— sí dio variedad real). Se prefirió por sobre "Rigor" (que hubiera calzado más directo con el hallazgo técnico de hoy) porque ancla mejor en el proceso de varios intentos que exige limpiar datos reales, no solo en la verificación puntual.
- **Ejercicio 4 (desafío) reutiliza el propio hallazgo técnico de esta sesión** (comparar la suma de `n` leyendo mal vs. leyendo bien) en vez de introducir un archivo o escenario nuevo — cierra el círculo narrativo del Haz Ahora ("¿cómo te asegurarías de que no se equivocó en silencio?") con evidencia numérica concreta.
- **Personaje "la periodista" reutilizado de N°36** para el hilo del Haz Ahora/Guiada, en vez de introducir un personaje nuevo — mantiene continuidad narrativa entre sesiones consecutivas del mismo bloque.
