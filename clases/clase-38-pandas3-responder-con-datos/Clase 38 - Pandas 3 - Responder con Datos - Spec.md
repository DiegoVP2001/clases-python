# Clase 38 — Pandas 3: responder con datos

**Estado:** Spec aprobada — 2026-10-14
**Clase Picuino:** N/A — análisis de datos, sin equivalente directo en el Tutorial Picuino
**Proyecto:** parte del bloque pandas del Proyecto Cierre Octubre (ver `clases/clases-octubre/Calendario v3 - Proyecto Cierre Octubre.md`). Fecha: martes 20-oct-2026. Absorbe las antiguas N°38 (filtrar), N°39 (agrupar, ordenar) y N°40 (graficar).

## Contexto

- **Curso:** 4to medio
- **Duración:** ~77 min
- **Modalidad:** individual
- **Plataforma:** Google Colab
- **Entrega:** Google Classroom
- **Contenidos previos asumidos:** todo lo dictado hasta N°37 (abrir un CSV con `pd.read_csv`, `dtype={"col": "str"}`, `.str.strip()`, `.str.replace()`, `pd.to_numeric(..., errors="coerce")`, `.notna()` como filtro). Dato del 2026-10-14: los 5 conceptos de N°37 se vieron en clase, pero no alcanzó el tiempo para ejercitarlos; eso ocurrió en la 37b (aplicación a su base).
- **Contenidos nuevos:** filtrar por un valor con `==`, `groupby(...)[...].sum()`, `.sort_values(ascending=False).head(n)` y `.plot(kind="bar", ...)`. **Sin funciones propias (`def`) en ningún punto.**
- **Contextos temáticos:** `bbdd_guaguas.csv` como hilo conductor único de toda la clase — excepción autorizada a la restricción 3 del `CLAUDE.md` raíz, vigente para N°35 a N°40.
- **OAs MINEDUC:** OA1 (organizar una solución en pasos y generalizarla a otra pregunta), OA4 (realizar un análisis de datos con apoyo computacional), OA6 (los datos son de personas reales: se leen con respeto).

## Objetivo

Construir una secuencia ordenada de pasos que responda una pregunta con una tabla de datos —quedarse con lo que interesa, resumirlo, ordenarlo y graficarlo—, con método.

## ¿Para qué sirve?

En dos días, cada equipo va a usar exactamente estos cuatro pasos con su propia base para armar la evidencia de su proyecto: el gráfico que responde su pregunta. Es la misma secuencia que hay detrás de cualquier ranking de una noticia, como los nombres más usados o las comunas con más matrícula.

## Estructura de la clase

### 1. Haz Ahora (6 min)

La periodista de las clases pasadas ya tiene la tabla de nombres limpia, y ahora quiere escribir sobre un nombre en particular: "Antonia". Quiere saber en qué años nacieron más Antonias, pero la tabla tiene cientos de miles de filas con todos los nombres de todos los años. La periodista, sabiendo de sus habilidades de programación, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:

1. De cientos de miles de filas con todos los nombres, ¿qué haces para trabajar solo con las de "Antonia"?
2. Si quieres el total de Antonias de cada año, ¿qué haces con las filas que comparten el mismo año?
3. Para ver cuáles son los años con más Antonias, ¿cómo acomodas los totales y con cuántos te quedas para que quepan en un gráfico?
4. Para comparar un año contra otro, ¿qué tipo de gráfico te sirve: de barras o de torta?

**Respuestas esperadas:**
1. Quedarme solo con las filas donde el nombre sea "Antonia" y descartar el resto.
2. Juntarlas por año y sumar sus cantidades, para tener un solo total por año.
3. Ordenarlos del mayor al menor y quedarme con los primeros (por ejemplo, 10).
4. De barras: cada año es una barra y se comparan por altura.

### 2. Introducción al Contenido Nuevo (22 min)

**Celda de inicio (puente, ya escrita, se ejecuta antes del primer concepto):**
```python
import pandas as pd
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"

tabla = pd.read_csv(URL, dtype={"n": "str"})
tabla["cantidad_guaguas"] = pd.to_numeric(
    tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
)
tabla = tabla[tabla["cantidad_guaguas"].notna()]
print("Tabla lista. Filas:", len(tabla))
```

**Concepto 1: Filtrar por un valor**
- Definición: La tabla trae todos los nombres de todos los años, pero una pregunta casi siempre es sobre una parte. Para quedarte solo con las filas de un nombre, comparas la columna con ese valor usando `==`, y usas ese resultado para elegir filas dentro de la tabla. La tabla original no cambia: obtienes una nueva con solo lo que cumple.
- Ejemplo:
  ```python
  import pandas as pd

  URL = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"
  tabla = pd.read_csv(URL, dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla = tabla[tabla["cantidad_guaguas"].notna()]

  filtrada = tabla[tabla["nombre"] == "Antonia"]
  print("Filas de Antonia:", len(filtrada))
  ```
- Idea clave: `tabla[tabla["columna"] == valor]` deja solo las filas donde la columna vale ese valor.
- Instrucción: Quédate solo con las filas donde `nombre` sea `"Antonia"`, guardadas en `filtrada`, e imprime cuántas filas quedaron.
- Punto de partida:
  ```python
  # La tabla ya está lista (celda de inicio).
  ```
- Resumen tabla: `tabla[tabla["col"] == valor]`

**Concepto 2: Agrupar y resumir**
- Definición: Para responder "¿cuántas Antonias por año?" no sirve mirar fila por fila: hay que juntar las filas que comparten el año y sumar sus cantidades. `.groupby("grupo")["columna"].sum()` hace justo eso: junta por grupo y entrega un solo total por cada uno. El resultado es una serie con un valor por año.
- Ejemplo:
  ```python
  import pandas as pd

  URL = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"
  tabla = pd.read_csv(URL, dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla = tabla[tabla["cantidad_guaguas"].notna()]

  filtrada = tabla[tabla["nombre"] == "Antonia"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  print("Años con datos:", len(resumen))
  ```
- Idea clave: `tabla.groupby("grupo")["número"].sum()` junta las filas por grupo y entrega un total por grupo.
- Instrucción: Junta `filtrada` por `anio` y suma `cantidad_guaguas`, guardado en `resumen`, e imprime cuántos años hay.
- Punto de partida:
  ```python
  filtrada = tabla[tabla["nombre"] == "Antonia"]
  ```
- Resumen tabla: `tabla.groupby("grupo")["número"].sum()`

**Concepto 3: Ordenar y quedarse con los primeros**
- Definición: Un resumen con cien años es muy largo para leerlo o graficarlo. `.sort_values(ascending=False)` ordena de mayor a menor, y `.head(n)` deja solo los primeros `n`. Juntos entregan un "top": los `n` con el valor más alto.
- Ejemplo:
  ```python
  import pandas as pd

  URL = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"
  tabla = pd.read_csv(URL, dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla = tabla[tabla["cantidad_guaguas"].notna()]

  filtrada = tabla[tabla["nombre"] == "Antonia"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(10)
  print("Años en el top:", len(top))
  ```
- Idea clave: `.sort_values(ascending=False).head(n)` ordena de mayor a menor y deja solo los primeros `n`.
- Instrucción: Ordena `resumen` de mayor a menor y quédate con los 10 primeros, guardados en `top`, e imprime cuántos quedaron.
- Punto de partida:
  ```python
  filtrada = tabla[tabla["nombre"] == "Antonia"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  ```
- Resumen tabla: `serie.sort_values(ascending=False).head(n)`

**Concepto 4: Graficar en barras**
- Definición: Una tabla de 10 números se lee, pero un gráfico se entiende de un vistazo. `.plot(kind="bar")` convierte la serie en un gráfico de barras: cada categoría es una barra y se comparan por altura. Con `title`, `xlabel` y `ylabel` le pones nombre al gráfico y a sus ejes, y `plt.show()` lo muestra.
- Ejemplo:
  ```python
  import pandas as pd
  import matplotlib.pyplot as plt

  URL = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/bbdd_guaguas.csv"
  tabla = pd.read_csv(URL, dtype={"n": "str"})
  tabla["cantidad_guaguas"] = pd.to_numeric(
      tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
  )
  tabla = tabla[tabla["cantidad_guaguas"].notna()]

  filtrada = tabla[tabla["nombre"] == "Antonia"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(10)
  top.plot(kind="bar", title="Años con más Antonias", xlabel="Año", ylabel="Cantidad de guaguas")
  plt.show()
  ```
- Idea clave: `.plot(kind="bar", title=..., xlabel=..., ylabel=...)` convierte el resultado en un gráfico de barras para comparar categorías.
- Instrucción: Grafica `top` en barras, con un título y nombres para ambos ejes, y muéstralo.
- Punto de partida:
  ```python
  filtrada = tabla[tabla["nombre"] == "Antonia"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(10)
  ```
- Resumen tabla: `serie.plot(kind="bar", title="...")`

**Receta (callout tras la tabla-resumen, no es un concepto nuevo):** estas cuatro líneas juntas son una receta. Para otra pregunta no hay que pensar todo de nuevo: solo cambias el nombre, la columna o el número.
```python
# ── Lo único que cambias ──
NOMBRE = "Antonia"   # a quién filtras
N = 10               # cuántos del top

# ── La receta ──
filtrada = tabla[tabla["nombre"] == NOMBRE]
resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
top = resumen.sort_values(ascending=False).head(N)
top.plot(kind="bar", title="Años con más " + NOMBRE, xlabel="Año", ylabel="Cantidad de guaguas")
plt.show()
```

**Torpedo: otras preguntas con la misma receta** *(celda de referencia, sin "Escríbelo tú", sin resultado esperado; se avisa que NO se evalúa hoy. Cada línea se ejecutó sobre `guaguas` el 2026-10-14 y corre sin error.)*

| Si quieres saber... | Qué cambias en la receta | Línea resultante |
|---|---|---|
| El **promedio** en vez del total | `.sum()` → `.mean()` | `filtrada.groupby("anio")["cantidad_guaguas"].mean()` |
| **Cuántas filas** hay por grupo | `.sum()` → `.count()` | `filtrada.groupby("anio")["cantidad_guaguas"].count()` |
| El **mayor** valor de cada grupo | `.sum()` → `.max()` | `filtrada.groupby("anio")["cantidad_guaguas"].max()` |
| Los **menores** en vez de los mayores | `ascending=False` → `ascending=True` | `resumen.sort_values(ascending=True).head(10)` |
| Solo valores **sobre un umbral** | `==` → `>` | `tabla[tabla["cantidad_guaguas"] > 1000]` |
| Todo **menos** un valor | `==` → `!=` | `tabla[tabla["nombre"] != "Antonia"]` |
| Barras **horizontales** (nombres largos) | `"bar"` → `"barh"` | `top.plot(kind="barh")` |
| **Otro grupo** o **otra columna** | `"anio"` / `"cantidad_guaguas"` por la tuya | `groupby("tu_columna")["tu_número"]` |

Nota en una línea bajo la tabla: con `guaguas`, `.mean()` y `.count()` calculan por fila (no por guagua); en bases donde cada fila es una persona, un registro o una carrera, sí significan lo que uno espera. Hay que pensar qué mide cada fila antes de elegir el resumen.

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Usar `=` en vez de `==` al filtrar | `SyntaxError`: `=` guarda un valor, `==` compara | Usar `==` para comparar la columna con el valor |
| Escribir el nombre con otra mayúscula o tilde (`"antonia"`, `"Sofia"`) | El filtro devuelve 0 filas, sin ningún error | Imprimir `len(filtrada)` y copiar el valor tal cual está en la tabla |
| Pedir `.sort_values(ascending=False)` sobre la tabla filtrada completa en vez del resumen | `TypeError`: falta decir por qué columna ordenar | Ordenar el resumen (una serie), no la tabla entera |

### 3. Práctica Guiada (18 min)

La periodista ya conoce a las Antonias, y ahora quiere comparar con otro nombre: "Sofía". Necesita saber cuántas filas tiene ese nombre en la tabla y ver en un gráfico en qué años nacieron más Sofías, para decidir si la comparación vale la pena en su nota.

**El programa debe:**
- Quedarse solo con las filas del nombre "Sofía" e imprimir cuántas son.
- Sumar las cantidades de guaguas de cada año.
- Ordenar esos totales de mayor a menor y quedarse con los 10 primeros, e imprimir cuántas guaguas suman esos 10 años.
- Graficar esos 10 años en barras, con un título y nombres para los dos ejes.

**Resultado esperado:**
```
Filas de Sofía: 107
Guaguas en los 10 mejores años: 46857
```
Y debajo, un gráfico de 10 barras, con el año 2008 como la barra más alta.

- Solución:
  ```python
  filtrada = tabla[tabla["nombre"] == "Sofía"]
  print("Filas de Sofía:", len(filtrada))

  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(10)
  print("Guaguas en los 10 mejores años:", int(top.sum()))

  top.plot(kind="bar", title="Años con más Sofías", xlabel="Año", ylabel="Cantidad de guaguas")
  plt.show()
  ```

### 4. Práctica Independiente (16 min)

Todos los ejercicios parten de `tabla`, ya cargada en la celda de inicio. No vuelvan a leer el archivo. **No agreguen columnas nuevas a `tabla`** (los ejercicios se verifican contra la tabla compartida).

**Celda de configuración:**
```python
#@title 🔧 Verificador automático — ejecuta esta celda antes de empezar (no la edites)

import io, re, contextlib, unicodedata, types
from IPython import get_ipython
import matplotlib.pyplot as _plt

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
    espacio = dict(get_ipython().user_ns)
    if "tabla" not in espacio:
        print("⬜ No encuentro la variable tabla. Ejecuta primero la celda de inicio de la clase.")
        return
    espacio["plt"] = types.SimpleNamespace(show=lambda: None)
    salida = io.StringIO()
    try:
        with contextlib.redirect_stdout(salida):
            exec(compile(fuente, "<tu solución>", "exec"), espacio)
    except Exception as error:
        print("❌ Tu programa se detuvo con un error:", type(error).__name__, "-", error)
        return
    finally:
        _plt.close("all")
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

def verificar_ejercicio_1():
    esperadas = ["Filas de Martín: 109", "Años con datos: 101"]
    _revisar("# Tu solución — Ejercicio 1", esperadas)

def verificar_ejercicio_2():
    esperadas = ["Guaguas en los 5 mejores años: 24362"]
    _revisar("# Tu solución — Ejercicio 2", esperadas)

def verificar_ejercicio_3():
    esperadas = ["Años en el gráfico: 5", "Guaguas en esos años: 40800"]
    _revisar("# Tu solución — Ejercicio 3", esperadas)

def verificar_ejercicio_4():
    esperadas = ["Nombres en el gráfico: 8", "Guaguas de esos nombres: 3560264"]
    _revisar("# Tu solución — Ejercicio 4", esperadas)
```

**Ejercicio 1 — La ficha de un nombre**
Una amiga que arma el álbum de aniversario del colegio quiere saber cuánto "aparece" el nombre Martín en los registros: cuántas filas tiene en la tabla y en cuántos años distintos hay guaguas con ese nombre, para ver si es un nombre de todas las épocas o de una sola.

**El programa debe:**
- Quedarse solo con las filas del nombre "Martín" e imprimir cuántas son.
- Juntar esas filas por año, sumando las cantidades de guaguas, e imprimir cuántos años distintos quedaron.

<details>
<summary>💡 Pista — con qué contar los años</summary>
Después de juntar por año, cada año queda como una sola fila del resumen. Contar esas filas es contar los años.
</details>

<details>
<summary>💡 Pista — escribe el nombre tal cual</summary>
El nombre debe estar escrito igual que en la tabla, con la misma mayúscula y la misma tilde. Si la primera cifra te da 0, revisa eso primero.
</details>

**Resultado esperado:**
```
Filas de Martín: 109
Años con datos: 101
```

**Celda de verificación:**
```python
verificar_ejercicio_1()
```

- Solución:
  ```python
  # Tu solución — Ejercicio 1
  filtrada = tabla[tabla["nombre"] == "Martín"]
  print("Filas de Martín:", len(filtrada))

  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  print("Años con datos:", len(resumen))
  ```

**Ejercicio 2 — Los mejores años de un nombre**
El profe de Historia prepara una línea de tiempo y quiere los cinco años en que más guaguas se llamaron Diego, para ubicar de qué década es el nombre. Necesita además saber cuánto suman esos cinco años juntos.

**El programa debe:**
- Quedarse solo con las filas del nombre "Diego".
- Sumar las cantidades de guaguas de cada año.
- Ordenar esos totales de mayor a menor y quedarse con los 5 primeros.
- Imprimir cuántas guaguas suman esos 5 años.

<details>
<summary>💡 Pista — cuántos quedarse</summary>
En esta clase aprendiste el número que va dentro de `.head()`: cámbialo por la cantidad de años que pide el enunciado.
</details>

<details>
<summary>💡 Pista — qué sumar al final</summary>
Al final tienes una serie con 5 totales, uno por año. Súmalos con `.sum()` y envuélvelos en `int()` para que no salga con decimales.
</details>

**Resultado esperado:**
```
Guaguas en los 5 mejores años: 24362
```

**Celda de verificación:**
```python
verificar_ejercicio_2()
```

- Solución:
  ```python
  # Tu solución — Ejercicio 2
  filtrada = tabla[tabla["nombre"] == "Diego"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(5)
  print("Guaguas en los 5 mejores años:", int(top.sum()))
  ```

**Ejercicio 3 — La receta completa, con gráfico**
La radio del pueblo prepara un programa sobre los nombres que marcaron los años 90 y 2000, y le encargó a un equipo de datos un gráfico del nombre Camila: debe mostrar los cinco años en que más guaguas se llamaron así. Para ordenar el guion del programa, el equipo también debe informar cuántos años quedaron en el gráfico y cuántas guaguas suman en total.

**El programa debe:**
- Quedarse solo con las filas del nombre "Camila".
- Sumar las cantidades de guaguas de cada año, ordenar de mayor a menor y quedarse con los 5 primeros.
- Imprimir cuántos años quedaron y cuántas guaguas suman.
- Graficar esos 5 años en barras, con un título y nombres para los dos ejes.

<details>
<summary>💡 Pista — el orden de los cuatro pasos</summary>
Es la misma receta de la Guiada con otro nombre y otro número: filtrar, juntar por año, ordenar y quedarse con los primeros, y graficar al final.
</details>

<details>
<summary>💡 Pista — antes de graficar</summary>
Primero imprime lo que se pide y después grafica: así, si el gráfico sale raro, ya viste los números.
</details>

**Resultado esperado:**
```
Años en el gráfico: 5
Guaguas en esos años: 40800
```
Y debajo, un gráfico de 5 barras con título y ejes con nombre.

**Celda de verificación:**
```python
verificar_ejercicio_3()
```

- Solución:
  ```python
  # Tu solución — Ejercicio 3
  filtrada = tabla[tabla["nombre"] == "Camila"]
  resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(5)
  print("Años en el gráfico:", len(top))
  print("Guaguas en esos años:", int(top.sum()))

  top.plot(kind="bar", title="Años con más Camilas", xlabel="Año", ylabel="Cantidad de guaguas")
  plt.show()
  ```

**Ejercicio 4 — Desafío: los nombres más usados de todos**
La periodista cierra su nota con un ranking general: los nombres más usados en toda la historia de la tabla. Esta vez no se filtra por ningún nombre: la pregunta es sobre todos a la vez, así que cambia qué se junta. Quiere el gráfico de los ocho primeros y cuántas guaguas suman entre todos.

**El programa debe:**
- Sumar las cantidades de guaguas de cada nombre, sin filtrar antes.
- Ordenar de mayor a menor y quedarse con los 8 primeros.
- Imprimir cuántos nombres quedaron y cuántas guaguas suman.
- Graficar esos 8 nombres en barras, con un título y nombres para los dos ejes.

<details>
<summary>💡 Pista — qué cambia respecto a la receta</summary>
Solo cambia la columna por la que juntas: en vez de `"anio"`, ahora es la de los nombres. Y como no filtras, partes directo de `tabla`.
</details>

<details>
<summary>💡 Pista — el filtro se va</summary>
Si no filtras, no necesitas la variable de las filas de un nombre: junta `tabla` directamente.
</details>

**Resultado esperado:**
```
Nombres en el gráfico: 8
Guaguas de esos nombres: 3560264
```
Y debajo, un gráfico de 8 barras, con María como la barra más alta.

**Celda de verificación:**
```python
verificar_ejercicio_4()
```

- Solución:
  ```python
  # Tu solución — Ejercicio 4
  resumen = tabla.groupby("nombre")["cantidad_guaguas"].sum()
  top = resumen.sort_values(ascending=False).head(8)
  print("Nombres en el gráfico:", len(top))
  print("Guaguas de esos nombres:", int(top.sum()))

  top.plot(kind="bar", title="Nombres más usados", xlabel="Nombre", ylabel="Cantidad de guaguas")
  plt.show()
  ```

### 5. Ticket de Salida (7 min)

**4 preguntas** (excepción de esta clase al default de 3 — una por cada paso de la receta). Todas citan una línea del ICN con `tabla` ya existente; ninguna crea tablas ni usa comandos no vistos.

**Pregunta 1:**
```python
filtrada = tabla[tabla["nombre"] == "Antonia"]
```
¿Qué contiene `filtrada` después de esta línea?
- A: Todas las filas de `tabla`, pero con la palabra "Antonia" en la columna `nombre`
- B: Solo las filas de `tabla` donde `nombre` es "Antonia"
- C: Solo la columna `nombre`, con todos los nombres
- D: Un número: cuántas filas tienen "Antonia"

**Respuesta correcta:** B
**Justificación:** `tabla[tabla["nombre"] == "Antonia"]` usa la comparación para elegir filas: queda una tabla nueva con solo las filas que cumplen. No cambia la tabla original ni devuelve un número (para eso habría que usar `len()`).

**Pregunta 2:**
```python
resumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()
```
¿Qué contiene `resumen` después de esta línea?
- A: Las mismas filas de `filtrada`, ordenadas por año
- B: Un único número: el total de todas las guaguas
- C: Solo el año con más guaguas
- D: Un total de guaguas por cada año distinto

**Respuesta correcta:** D
**Justificación:** `.groupby("anio")` junta las filas que comparten el año y `.sum()` suma sus cantidades: queda un valor por cada año. No es un solo número (eso sería sumar sin agrupar) ni se queda con un solo año.

**Pregunta 3:**
```python
top = resumen.sort_values(ascending=False).head(10)
```
¿Qué contiene `top` después de esta línea?
- A: Los 10 años con mayor total, ordenados de mayor a menor
- B: Los 10 primeros años de `resumen` (los más antiguos), sin ordenar por total
- C: Los 10 años con menor total, ordenados de menor a mayor
- D: Un solo número: la suma de los 10 mejores años

**Respuesta correcta:** A
**Justificación:** `ascending=False` ordena de mayor a menor, y `.head(10)` conserva los 10 primeros de ese orden: los de mayor total. Con `ascending=True` serían los menores; sin ordenar, `.head(10)` entregaría los 10 primeros según el orden original.

**Pregunta 4:**
```python
top.plot(kind="bar", title="Años con más Antonias", xlabel="Año", ylabel="Cantidad de guaguas")
plt.show()
```
Si en la línea anterior de `top` se cambia `.head(10)` por `.head(5)` y se vuelve a ejecutar todo, ¿qué cambia en este gráfico?
- A: Las barras son más altas, porque ahora se suman menos años
- B: Aparece un error, porque `.plot()` solo acepta 10 valores
- C: El gráfico pasa a tener 5 barras: las de los 5 años con mayor total
- D: El gráfico pasa a tener 5 barras: las de los 5 años más antiguos

**Respuesta correcta:** C
**Justificación:** el gráfico dibuja una barra por cada valor de `top`. Con `.head(5)` quedan los 5 primeros del orden de mayor a menor, así que se ven 5 barras y son las de los mejores años. La altura de cada barra no cambia.

### Cierre (5 min)

**Objetivo de la clase:** Construir una secuencia ordenada de pasos que responda una pregunta con una tabla de datos —quedarse con lo que interesa, resumirlo, ordenarlo y graficarlo—, con método.

**Pregunta 1 — Metacognición (escala 1-5):** ¿Qué tan seguro/a te sientes encadenando los pasos para que una tabla responda una pregunta, donde 1 es "no entendí nada" y 5 es "puedo explicárselo a otro"?

**Pregunta 2 — Actitud proyectada al futuro:** ¿En qué otra situación de tu vida —estudios, deporte, una tarea de la casa— seguir los pasos en orden, sin saltarte ninguno, te evitó un error o te dio un mejor resultado?

## Decisiones de diseño relevantes

- **Actitud Método, elegida por Diego (2026-10-14)** entre Honestidad, Criterio, Método y Claridad. Se descartó Perseverancia por ser la de la N°37. Método calza con la receta parcelada línea por línea.
- **Esta clase no tiene sección Propósito** (pedido explícito de Diego, 2026-10-14). La actitud queda en el objetivo ("con método") y en la pregunta 2 del Cierre; la sección "¿Para qué sirve?" se ligó directamente al proyecto de los equipos. Decisión solo de esta clase: no cambia el default de las demás.
- **Ticket de Salida con 4 preguntas** (pedido de Diego), una por cada paso de la receta, todas con el código tal como se vio en el ICN. Excepción de esta clase al default de 3 (regla 17): el Form tiene la 4ta columna "Respuestas a ticket [4]". No se usan `pd.DataFrame` ni funciones no enseñadas; Diego lo pidió explícitamente tras ver comandos de creación de bases en tickets anteriores.
- **Una sola agregación aplicada en el ICN (`.sum()`)**; `.mean()`, `.count()`, `.max()` y otras variantes quedan en el torpedo como referencia. Razón técnica medida el 2026-10-14: con `guaguas`, `.mean()` y `.count()` calculan por fila y no por guagua (Antonia tiene 105 filas en 102 años por el `sexo` sin normalizar); además `groupby("sexo")` está descartado por lo mismo ("F"/"f"/"Femenino"). Las operaciones del torpedo no se evalúan hoy ni en el Ticket; si cuentan o no para la Defensa del 26-oct queda pendiente de decisión de Diego (recomendación: no).
- **Celda de inicio (puente) única.** La tabla se lee y se limpia una sola vez, con el mismo código de N°37 (con `strip`, tal como se dictó), y todo lo demás parte de `tabla`: los "Punto de partida" del ICN, la Guiada y los ejercicios no vuelven a leer el CSV (23,5 MB). Para que el verificador vea `tabla`, ejecuta la solución sobre una copia del espacio del cuaderno (`dict(user_ns)`), con `plt.show` desactivado y `plt.close("all")` al final. **Para quien genera el Colab:** la celda de inicio, la receta y el torpedo son bloques nuevos que el parser puede no reconocer; revisar el notebook generado.
- **Sin Ejercicios 0** (decisión de Diego, 2026-10-14): en la N°37 no alcanzó el tiempo para ejercitar y esta clase ya tiene cuatro conceptos.
- **Ejercicios imprimen con lo ya visto** (`len()`, `.sum()`, `int()`), nunca la serie completa, para que el verificador compare líneas simples. Todas las cifras esperadas salen de ejecutar la receta sobre el CSV el 2026-10-14. Los ejercicios eligen nombres de varias décadas (Martín, Diego, Camila) y la Guiada usa Sofía, distinto del Antonia del ICN.
- **Personaje "la periodista"** reutilizado de N°36 y N°37 para el hilo Haz Ahora → ICN → Guiada.
- **Para la 38b:** `Prompt - Generar 38b.md` toma esta receta y el torpedo como fuente del "torpedo" del cuaderno de aplicación; hay que decir ahí que los marcadores `NOMBRE` y `N` son nombres a reemplazar.
