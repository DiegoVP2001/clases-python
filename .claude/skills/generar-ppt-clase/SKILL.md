---
name: generar-ppt-clase
description: Genera la presentación PowerPoint (03-presentacion.pptx) de una clase a partir del spec aprobado, aplicando una marca visual oscura (fondo #1A1A2E) con identidad de programación. Produce un slide por concepto del ICN cuando el spec está enriquecido, y slides compactos "Código + Resultado apilado" cuando el spec define bloques de Demostración. Usa esta skill después de que el 01-clase.ipynb esté aprobado.
---

# Skill: Generar presentación PowerPoint (03-presentacion.pptx)

## Propósito

Producir el archivo `.pptx` de una clase con fondo oscuro consistente, listo para usar en aula. La marca aplica al 100%: paleta azul petróleo + turquesa + ámbar, Consolas para código, identidad `>>>` en la portada.

## Cuándo usar

Actívate cuando Diego diga "Genera el PPT", "Pasemos al PowerPoint" o equivalente.

**Requisitos previos:**
1. `clases/clase-NN-tema/00-spec.md` existe y está aprobado.
2. `01-clase.ipynb` está aprobado (idealmente).
3. `python-pptx` instalado.

## Instalación de python-pptx (una sola vez)

```bash
pip install python-pptx
```

En Windows si falla: `python -m pip install python-pptx`.

## Estructura del PPT generado

El script genera slides según el contenido del spec. Hay 10 tipos de slide modelo en la plantilla:

| # | Tipo | Cuándo se usa |
|---:|---|---|
| 0 | Bienvenida | Portada de la clase |
| 1 | Objetivo/Propósito/Reglas | Slide 2, marca obligatoria |
| 2 | Stock título | Haz Ahora, intros, cierres genéricos |
| 3 | Concepto del ICN | **UN slide por cada concepto** del Contenido Nuevo (definición + ejemplo + idea clave). **No hay límite de conceptos**: si el spec define 3, salen 3 slides; si define 6, salen 6 slides. Cada concepto debe ser pedagógicamente coherente y enfocado. |
| 4 | Código + Resultado | Práctica guiada, ejemplos con output esperado (UN par código/resultado) |
| 5 | Tabla | Errores típicos (header oscuro + 3 filas) |
| 6 | Ejercicio | Práctica independiente (enunciado + resultado esperado) |
| 7 | Ticket | Ticket de salida con tarea y entrega |
| 8 | Cierre | Tres preguntas de metacognición listadas |
| 9 | **Código + Resultado apilado** | **Layout estrella compacto.** Hasta 3 filas en una sola diapositiva, cada una con etiqueta + código (izquierda) + resultado (derecha). Ideal para mostrar variantes de un mismo concepto (`sep`, `end`, combinaciones) sin gastar 3 diapositivas. Se dispara con bloques **Demostración** en el spec (ver más abajo). |

**Importante sobre el ICN:** la skill genera tantos slides como conceptos defina el spec. Lo recomendable son 3-5 conceptos por clase, pero técnicamente no hay tope.

**Layout adaptativo (v5):** cada slide de concepto y el Haz Ahora adaptan su layout automáticamente según el contenido real del spec — no hay estructura rígida obligatoria:

| Contenido del concepto | Layout generado |
|---|---|
| Definición + código + idea clave | Slide estándar de tres zonas |
| Definición con tabla markdown + idea clave | Zona de código reemplazada por tabla visual estilizada con la marca |
| Definición + idea clave (sin código) | Zona de código eliminada; definición e idea clave se expanden para usar el espacio |

**Haz Ahora adaptativo:** si el Haz Ahora no contiene código, la zona de código se elimina automáticamente y el texto se expande para ocupar todo el espacio disponible.

## Formato de código inline (backticks)

**Regla general:** cualquier texto del spec que esté entre backticks ` `código` ` se renderiza automáticamente en el PPT con fuente Consolas y color verdoso `#4ADFCB`, sin importar el contexto.

Esto aplica a:
- Definiciones del ICN
- Ideas clave del ICN
- Objetivo y Propósito (slide 2)
- Subtítulo de Práctica Guiada
- Enunciados de ejercicios
- Tarea del Ticket de Salida
- Celdas de la tabla de errores
- Preguntas del Cierre
- Cualquier otro texto que pase por reemplazo de placeholder

**Convención al escribir el spec:** usa backticks SIEMPRE que menciones código Python o términos técnicos. Por ejemplo:
- ✅ "La función `input()` detiene el programa"
- ❌ "La función input() detiene el programa"
- ✅ "Devuelve un `TypeError` si los tipos no coinciden"
- ❌ "Devuelve un TypeError si los tipos no coinciden"

Estructura típica de un PPT generado (clase 7, formato enriquecido):

```
Slide 1:  Bienvenida
Slide 2:  Objetivo/Propósito/Reglas
Slide 3:  Haz Ahora
Slide 4:  Concepto 1 del ICN ← UN slide rico por concepto
Slide 5:  Concepto 2 del ICN
Slide 6:  Concepto 3 del ICN
Slide 7:  Demostración apilada (sep/end) ← tipo 9, si el spec la define
Slide 8:  Tabla de errores típicos
Slide 9:  Práctica guiada
Slide 10: Ejercicio 1
Slide 11: Ejercicio 2
Slide 12: Ticket de salida
Slide 13: Cierre con preguntas
```

Nota: los slides de **Demostración apilada** (tipo 9) se generan justo después de los conceptos y la tabla de errores, dentro del bloque de Contenido Nuevo.

## Formato del spec enriquecido (CRÍTICO)

Para que la skill genere un slide rico por concepto, el spec debe tener el ICN así:

```markdown
### 2. Introducción al Contenido Nuevo

**Concepto 1: [nombre breve]**
- Definición: [1-2 frases claras]
- Ejemplo:
  ```python
  [código mínimo, 2-4 líneas]
  ```
- Idea clave: [frase memorable]

**Concepto 2: [nombre breve]**
- Definición: ...
- Ejemplo: ...
- Idea clave: ...

**Errores típicos:**
| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| ... | ... | ... |
```

Si el spec usa el formato antiguo (`**Conceptos:** 1. ... 2. ...` con `**Ejemplos a usar:**`), la skill lo parsea en modo compatibilidad y produce slides básicos, **pero el resultado es mucho más pobre**. Si Diego acaba de migrar al sistema, recomiéndale enriquecer el spec antes de regenerar el PPT.

## Slide compacto "Código + Resultado apilado" (tipo 9)

Este es el **layout estrella para contenido denso**: una sola diapositiva con hasta 3 filas, cada una con código a la izquierda y su resultado a la derecha. Sirve para mostrar variantes de un mismo concepto de un vistazo (por ejemplo `sep`, `end` y su combinación), en lugar de gastar 3 diapositivas separadas. Engancha más a estudiantes de enseñanza media porque el "¿y esto qué imprime?" queda resuelto en la misma pantalla.

**Cómo se dispara desde el spec.** Dentro de la sección `### 2. Introducción al Contenido Nuevo`, agrega uno o más bloques `**Demostración: ...**`. Cada bloque genera UNA diapositiva apilada. El formato recomendado (con bloque de código) es:

```markdown
**Demostración: "sep" y "end"**
Subtítulo: Dos parámetros que cambian cómo se ve la salida.
- Fila: sep — separa los elementos
  ```python
  print("a", "b", "c", sep=" | ")
  ```
  Resultado: a | b | c
- Fila: end — cómo termina el print()
  ```python
  print("Hola", end=" ")
  print("mundo")
  ```
  Resultado: Hola mundo
- Fila: combinados
  ```python
  print(1, 2, sep="-", end="!")
  ```
  Resultado: 1-2!
```

Reglas y límites del slide apilado:
- **Máximo 3 filas por slide.** Si una demostración necesita más, divídela en dos bloques `**Demostración: ...**` (saldrán dos diapositivas).
- **Las filas no usadas se ocultan solas.** Si defines 2 filas, la tercera no aparece (sin cajas vacías ni placeholders).
- **Etiquetas cortas.** El texto después de `Fila:` es la etiqueta ámbar. Mantenla corta (`sep`, `end`, `sep + end`); etiquetas muy largas se extienden sobre la columna de resultado.
- **El subtítulo es opcional** (línea `Subtítulo:`). Si no lo pones, el slide queda con más aire.
- **Regla mixta de fuente (automática).** El código se renderiza a 20 pt por defecto y baja a 18 o 16 pt **solo si la línea es demasiado larga para caber**. No tienes que hacer nada: el script mide la línea más larga y elige el tamaño. Aun así, conviene mantener cada línea de código por debajo de ~45 caracteres para que se lea a 20 pt desde el fondo de la sala.
- **Formato en línea (`R`).** El parámetro destacado (como `sep=" | "`) no se resalta automáticamente en negrita dentro del bloque de código apilado; si quieres énfasis, ponlo en la etiqueta de la fila.

Formato alternativo en una sola línea (para código corto, sin bloque ```python```):

```markdown
**Demostración: Operadores compuestos**
- Fila: suma | cuenta += 1000 | aumenta el valor
- Fila: resta | cuenta -= 500 | disminuye el valor
```

(En este formato, `\n` literal dentro del campo de código fuerza un salto de línea.)

## Cómo se ejecuta

```bash
python .claude/skills/generar-ppt-clase/crear_ppt.py clases/clase-NN-tema/00-spec.md clases/clase-NN-tema/03-presentacion.pptx
```

En Windows: usar comillas si las rutas tienen espacios.

## Después de generar

1. Confirma a Diego que el archivo se creó.
2. Sugiere abrirlo en PowerPoint/Keynote/Google Slides para revisar.
3. Si Diego pide ajustes, edita el spec y regenera; no edites el .pptx directamente.

## Iteración

- **Cambio de contenido:** editar `00-spec.md` + regenerar.
- **Cambio de marca visual** (colores, posiciones, tamaños): editar `construir_plantilla.py` y volverlo a correr para regenerar `plantilla_marca.pptx`. Después regenerar todos los PPT afectados.
- **Cambio de lógica del script** (qué slides se generan, cómo): editar `crear_ppt.py`.

## Archivos en esta carpeta

- `SKILL.md` — este archivo
- `crear_ppt.py` — el generador del PPT (lo invoca Claude)
- `construir_plantilla.py` — script que reconstruye la plantilla desde cero (se corre solo si se cambia la marca)
- `plantilla_marca.pptx` — la plantilla con los 9 slides modelo

## Reglas críticas

1. **No editar el .pptx generado directamente** y esperar regenerar — los cambios se pierden.
2. **El spec es la fuente de verdad** del contenido.
3. **La plantilla es la fuente de verdad** del estilo.
4. **Tildes obligatorias** en todo texto en español.
5. **Si una slide queda apretada o cortada** después de generar: en los slides de concepto, ejercicio o ticket, suele ser el spec demasiado largo (acorta el texto). En los slides apilados (tipo 9), el código se autoajusta de tamaño, pero si una **etiqueta de fila** es muy larga o pones más de 3 filas, divide la demostración en dos bloques `**Demostración: ...**`.

## Limitaciones conocidas

- El bloque de definición y de idea clave en los slides de concepto tienen alto fijo; si el texto es muy largo, puede desbordarse. Mantén definiciones < 200 caracteres e ideas clave < 120 caracteres.
- La tabla de errores soporta hasta 3 filas de datos.
- Las preguntas del cierre soportan exactamente 3 (si hay menos quedan en blanco, si hay más se ignoran las extras).
- El slide apilado (tipo 9) soporta **hasta 3 filas**; las filas extra se ignoran. Usa otro bloque `**Demostración: ...**` para más variantes.
- En los slides apilados, el **código** aplica una regla mixta de fuente (20 → 18 → 16 pt) que evita el desborde horizontal automáticamente. El texto narrativo (definición, idea clave, enunciado) sigue usando el auto-fit de PowerPoint, que a veces lo hace más pequeño de lo ideal; si lo notas frecuentemente, ajusta los tamaños en `construir_plantilla.py` y regenera.
