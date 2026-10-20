"""Genera 'Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb' (rúbrica para estudiantes, v5, 2026-10-20).

Reemplaza al Colab de criterios del 19-oct (Calendario v4): cambia «Archivo usable» por «Conoce su base» (5 puntos por el
mínimo y 10 por una pregunta distinta), agrega el mapa de dónde se ve cada criterio en los cuadernos de Código y de Texto,
los hitos de Proceso con la sesión 37b, y los equipos y bases. La versión interna (con puntajes y niveles) está en
'Rúbricas y Evaluación - Proyecto Cierre Octubre (v5).md'.

Fuente de verdad del cuaderno: no editar el .ipynb a mano, editar acá y regenerar.
Uso:  python generar_rubrica.py
Notas de diseño: solo markdown (es una rúbrica para leer), sin signos de peso (MathJax) y voz colectiva.
"""
import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_markdown_cell, new_notebook

CARPETA = Path(__file__).resolve().parent
sys.path.insert(0, str(CARPETA))
from generar_cuadernos import EQUIPOS, escapar_pesos  # noqa: E402  (los equipos viven en un solo lugar)

SALIDA = CARPETA / "Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb"

cells = []


def md(texto):
    cells.append(new_markdown_cell(escapar_pesos(texto.strip("\n"))))


md("""
# 📋 Cómo se evalúa nuestro proyecto de cierre

**Curso:** 3ro y 4to medio  |  **Lectura:** ~8 min  |  **Plataforma:** Google Colab

---

Este cuaderno junta en un solo lugar **qué entregamos, cuándo, qué se mira en cada parte y cómo se calcula la nota**.
Lo leemos hoy y volvemos a él cuando tengamos dudas. *(Versión actualizada el 20-oct: reemplaza a la del 19-oct.)*
""")

md("""
## 🎯 La idea central

El proyecto mide una sola cosa: **¿podemos responder una pregunta real con datos y explicar cómo lo hicimos?**

Se traduce en **una sola nota** (vale doble en el promedio semestral), armada con 4 partes:

| Parte | Peso | ¿Grupal o individual? |
|---|---|---|
| 📓 **Producto** — nuestro Colab narrado | 35% | Grupal, con ajuste según el aporte de cada uno |
| 🎤 **Presentación** | 20% | Individual dentro del equipo (por las preguntas) |
| 🔍 **Defensa técnica** — código con errores | 30% | En pareja, con ajuste según el aporte de cada uno |
| 📒 **Proceso** — bitácora e hitos | 15% | Grupal, con ajuste según el aporte de cada uno |

Quien trabaja solo no tiene ajuste por aporte: su nota es la del equipo tal cual.
""")

filas_equipos = "\n".join(f"| {base} | {equipos} |" for base, equipos in EQUIPOS)
md(f"""
## 👥 Equipos y bases

| Base elegida | Equipos |
|---|---|
{filas_equipos}

¿Tu nombre no aparece, o tu equipo cambió de base? Avísale al profe: la lista se actualiza.
""")

md("""
## 📅 Fechas que no podemos olvidar

| Qué | Cuándo |
|---|---|
| 🧑‍💻 **Clase 38** — aprendemos la receta y abrimos nuestra base | Martes 20 de octubre |
| ✍️ **Clase 38b** — pregunta distinta y cuaderno de Texto | Jueves 22 de octubre |
| 📓 Entrega del **Colab final** (buzón en Classroom) | **Lunes 26 de octubre, 23:59** |
| 🔍 **Defensa técnica** (30 min, en pareja) | **Martes 27 de octubre**, 15:40 |
| 🖥️ Entrega del **PPT** (buzón en Classroom) | **Jueves 29 de octubre, 12:00** |
| 🎤 Presentan los equipos con **al menos un integrante de 4to medio** | **Jueves 29 de octubre**, 14:10 |
| 🎤 Presentan los equipos **solo de 3ro medio** | **Lunes 2 de noviembre**, 15:40 (pendientes: martes 3) |

- **El orden de presentación se sortea el mismo día.** Todos debemos llegar listos.
- El lunes 26 terminamos el Colab. Quienes terminen antes pueden ir partiendo con el PPT.
- El martes 27, después de la Defensa, seguimos con el PPT y ensayamos.
""")

md("""
## 📓 Producto — nuestro Colab narrado (35%)

Es el documento completo del equipo: los cuadernos de 🧑‍💻 **Código** y ✍️ **Texto** juntos. Se lee de corrido y **siempre en este orden**:
**pregunta → base → evidencia → límites → conclusión.**

| Criterio | ¿Qué tiene que verse? |
|---|---|
| **Conoce su base** | Describimos nuestra base y nos hacemos **preguntas propias y originales** (detalle abajo). |
| **Cada operación justificada** | Contamos nuestros pasos **en palabras** y cada uno con **por qué responde nuestra pregunta**. |
| **Evidencia que responde la pregunta** | El gráfico o la tabla final **sostiene nuestra conclusión**, con cifras de nuestra tabla. No basta con un gráfico bonito. |
| **Narración completa** | Se lee de principio a fin, en el orden de arriba, y cierra con una conclusión que responde la pregunta inicial. |
| **Límites del dato** | Escribimos **qué NO podemos concluir** con esta base, apoyándonos en un dato real (por ejemplo, cuántas filas se perdieron), no en una frase de relleno. |
| **Nota de prensa** | El hallazgo convertido en noticia, con **titular, bajada, entrada, desarrollo y cierre**, como la nota del LUN con la que partimos. |

### 🌟 Conoce su base

Son **15 puntos**, y se ganan así:

- **5 puntos por cumplir el mínimo:** explicamos qué es una fila de nuestra base, cuántas filas y columnas tiene, y qué columnas usamos y para qué (filtrar, agrupar o resumir).
- **10 puntos por la originalidad de nuestras preguntas:** cuanto más propia sea la pregunta que nos hacemos y que investigamos, más puntaje.

| Nuestra pregunta… | Puntos |
|---|---|
| **Cambia la comparación** que muestra el ejemplo de la base (otra columna para filtrar, agrupar o resumir, otro tipo de resumen), o usa una **columna fuera de las 5 sugeridas** | 10 |
| Cambia solo un **valor** (otra comuna, otro año) o el `N` | 5 |
| Es **el ejemplo tal cual** | 0 |

**Podemos hacer todos los análisis que queramos**, copiando y pegando la receta, siempre que **cada uno esté explicado** en el cuaderno de Texto: un análisis sin explicación no suma. Cuenta el **más original** que esté bien explicado; la cantidad no suma.

> ⭐ **Análisis principal:** marcamos cuál es. De él salen las diapositivas 3 a 5, la nota de prensa y los errores de la Defensa técnica. Se corrigen el principal y el más original; los demás se leen, pero no tienen puntaje.

### 🗺️ ¿Dónde lo escribimos?

| Criterio | En nuestros cuadernos |
|---|---|
| Conoce su base | Código: Paso 1 y todos los análisis · Texto: secciones 2 y 3 |
| Cada operación justificada | Texto: sección 3 («cómo lo investigamos») |
| Evidencia | Código: Paso 2 (gráfico y cifras) · Texto: sección 3 («hallazgo») |
| Narración completa | Todo el cuaderno de Texto, en orden |
| Límites del dato | Código: Paso 3 · Texto: sección 3 («límites») |
| Nota de prensa | Texto: sección 5 |
""")

md("""
## 🎤 Presentación (20%)

**6 diapositivas, 7 minutos exactos.** No hay preguntas después de cada equipo: se hacen **al final del día**, a un integrante de cada equipo, **por nombre**. Por eso todos debemos poder responder sobre cualquier parte del trabajo.

| N.º | Diapositiva | Tiempo | ¿Qué mostramos? |
|---|---|---|---|
| 1 | **Contexto, pregunta e hipótesis** | 1:00 | Qué fenómeno investigamos, por qué importa y qué esperábamos encontrar. |
| 2 | **Datos** | 0:45 | De dónde salen, qué contienen y qué columnas usamos. |
| 3 | **Cómo lo investigamos** | 1:45 | 3 o 4 pasos **en palabras**, cada uno con su porqué ("filtramos X porque…"). **Sin pegar código.** |
| 4 | **Hallazgo y evidencia** | 1:45 | El **título es la frase** que responde la pregunta. Un gráfico o tabla de nuestro Colab, con la parte que respalda la afirmación resaltada. |
| 5 | **Límites** | 0:45 | Una limitación **específica** de nuestra base y cómo afecta cuánto confiamos en la conclusión. |
| 6 | **Conclusión y próximo paso** | 1:00 | Respondemos la pregunta, volvemos a la hipótesis, descartamos una explicación alternativa y proponemos un próximo paso. |

Las diapositivas salen del cuaderno de ✍️ Texto: la 1 de la sección 1, la 2 de la sección 2, las 3 a 5 de nuestro **análisis principal** (sección 3) y la 6 de la sección 4.

**Puntaje (sobre 100):**

| Criterio | Pts |
|---|---|
| Claridad del hallazgo (diapositiva 4) | 10 |
| Cómo lo investigamos + evidencia (diapositivas 3 y 4) | 25 |
| Límites explicados en voz alta (diapositiva 5) | 20 |
| Conclusión argumentada (diapositiva 6) | 15 |
| Preguntas del final: respondemos nosotros, con criterio propio, y si no sabemos lo decimos | 20 |
| Formalidad: no leemos las diapositivas, buen ritmo, miramos al público, hablan todos | 10 |

**Reglas de formato:**
- Máximo ~25 palabras por diapositiva. Las diapositivas apoyan lo que decimos, no son el guion.
- **Cada integrante habla en al menos 2 diapositivas.**
- No hay nota por diseño: importa el contenido y cómo lo comunicamos.

⚠️ **Descuento aparte:** -0,1 por cada 3 faltas de ortografía en las diapositivas, con tope de -1,0 sobre la nota final. Revisemos el texto antes de entregar.
""")

md("""
## 🔍 Defensa técnica (30%)

Es un cuaderno **escrito** de **30 minutos** que respondemos **en pareja** (quien trabaja solo, lo hace solo). Recibimos **una copia de nuestro propio Colab** con **3 errores puestos a propósito en nuestro análisis principal**, que pueden estar en los espacios de la receta (la columna, el valor del filtro, el resumen, el `N`) o en la receta misma.

| Sección | Pts | ¿Qué hacemos? |
|---|---|---|
| **A. Explicar código** | 15 | Contamos en palabras qué hace 1 bloque marcado de nuestro Colab. |
| **B. Predecir** | 20 | Decimos **qué cambiaría en el resultado** si modificamos un espacio (la columna, el valor del filtro, el `N`), sin ejecutar. |
| **C. Errores** | 45 | Por cada uno de los 3 errores: lo **encontramos**, explicamos **por qué es un error y qué efecto tiene**, y lo **corregimos**. |
| **D. Proceso** | 20 | Respondemos 2 preguntas cortas sobre decisiones que tomamos (por ejemplo, por qué elegimos esa columna para agrupar). |

Ejemplo de lo que podría salir en la sección B:

```python
VALOR = "Maipú"
```

*"Si cambiamos `"Maipú"` por `"Providencia"`, ¿qué esperamos que pase con la cantidad de filas y con el gráfico?"*

**No se pide escribir código nuevo.** Solo entender, predecir y arreglar el código que ya está.

> **¿Por qué esta evaluación?** Quien entendió el código que entregó lo pasa, aunque se haya apoyado en IA. Quien no lo entendió, no. Por eso en el resto del proyecto no se persigue el uso de IA: lo que cuenta es poder responder por lo que entregamos.
""")

md("""
## 📒 Proceso — bitácora e hitos (15%)

Se mira lo que vamos registrando en la **Bitácora** de nuestro cuaderno de Texto, clase a clase, y lo que dejamos hecho en cada sesión:

| Criterio | ¿Qué tiene que verse? |
|---|---|
| **Pregunta inicial y descartadas** | Probamos y descartamos preguntas antes de quedarnos con la definitiva, y anotamos por qué. |
| **Hitos cumplidos** | En cada sesión dejamos avance real, no solo una promesa. Es lo que más pesa en esta parte. |
| **Cambios después de comentarios** | Se nota que mejoramos algo luego de recibir comentarios (en el ensayo o en clase). |
| **Avance de a poco** | El registro fechado muestra construcción clase a clase, no todo entregado de golpe al final. |

**Los hitos son:**

1. **Lunes 19-oct (Clase 37b):** cuenta el avance que dejó cada equipo ese día. Se mira **cuánto se avanzó**, no si todo estaba perfecto.
2. **Martes 20-oct (Clase 38):** receta entendida y primera pregunta corrida sobre nuestra base.
3. **Jueves 22-oct (Clase 38b):** pregunta distinta y cuaderno de Texto avanzado.
4. **Lunes 26-oct:** Colab final entregado.
""")

md("""
## 🤖 Cómo podemos usar la IA

| Nivel | ¿Dónde? | Regla |
|---|---|---|
| 🚫 **Nada de IA** | Todo el **código** (receta, filtros, gráficos) y todo el **texto del Colab narrado** (justificaciones, razonamiento, conclusión y nota de prensa) | No se genera ni se corrige con IA. Es justo lo que se defiende en la Defensa técnica. |
| ✅ **Libre** | **Diseño de las diapositivas** y recursos visuales | Podemos usar plantillas o imágenes de internet, **siempre citando**: *"Descripción o título — Autor/Plataforma — Link"*. |
""")

md("""
## 🧮 Cómo se calcula la nota

1. Cada una de las 4 partes se puntúa sobre **100**.
2. Se combinan con los pesos de la tabla de arriba (35% · 20% · 30% · 15%) y queda **un solo puntaje sobre 100**.
3. Se aplica la **exigencia del 50%** una sola vez: **50 puntos equivalen a un 4,0** (escala 2,0 a 7,0).
4. En Producto, Proceso y Defensa técnica se aplica el **ajuste por aporte** de cada integrante, según la ficha de autoevaluación y coevaluación que completaremos al final.
5. La nota final del proyecto **vale doble** en el promedio del semestre.

**Si faltamos** a la Defensa o a la presentación, avisemos: son actos de un día específico y hay **2 semanas para rendirlos** (mientras tanto la nota queda "Pendiente").
""")

md("""
## ✅ Antes de entregar

**Colab final — lunes 26, 23:59**
- ☐ Entregamos los dos cuadernos (🧑‍💻 Código y ✍️ Texto), con nuestro nombre y el de nuestra pareja al inicio.
- ☐ Describimos nuestra base, hicimos preguntas propias y marcamos con ⭐ nuestro **análisis principal**.
- ☐ Cada operación tiene su texto de por qué.
- ☐ Declaramos qué NO podemos concluir, con un dato real.
- ☐ Incluimos la nota de prensa, con titular, bajada, entrada, desarrollo y cierre.
- ☐ La Bitácora está al día, con las tres sesiones.
- ☐ Ejecutamos el Código de arriba hacia abajo y no hay errores.

**PPT — jueves 29, 12:00**
- ☐ Son 6 diapositivas, en el orden de la tabla.
- ☐ Máximo ~25 palabras por diapositiva y nada de código pegado.
- ☐ El título de la diapositiva 4 es la frase que responde nuestra pregunta.
- ☐ Revisamos la ortografía.
- ☐ Citamos plantillas e imágenes al final.
- ☐ Sabemos quién habla en cada diapositiva (cada uno en al menos 2).

---

Si algo no queda claro, lo conversamos en clase.
""")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["colab"] = {"provenance": []}
nbformat.validate(nb)
nbformat.write(nb, SALIDA)
print("OK", SALIDA.name, len(cells), "celdas")
