---
name: generar-ppt-clase
description: Genera la presentación PowerPoint (Clase NN - Tema - Presentación.pptx) de una clase a partir del spec aprobado. El PPT cubre desde la bienvenida hasta los errores típicos — todo lo que se trabaja en pantalla antes de abrir el computador. La Práctica Guiada, Independiente, Ticket y Cierre se trabajan desde el Colab. Usa esta skill después de que el Clase NN - Tema - Clase.ipynb esté aprobado.
---

# Skill: Generar presentación PowerPoint (Clase NN - Tema - Presentación.pptx)

## Propósito

Producir el archivo `.pptx` de una clase listo para usar en aula: fondo oscuro `#1A1A2E`, paleta turquesa + ámbar, Consolas para código. El PPT cubre lo que el profesor proyecta para presentar el contenido nuevo — no incluye las actividades que los estudiantes hacen en Colab.

## Cuándo usar

Actívate cuando Diego diga "Genera el PPT", "Pasemos al PowerPoint" o equivalente.

**Requisitos previos:**
1. `clases/clase-NN-tema/Clase NN - Tema - Spec.md` existe y está aprobado.
2. `Clase NN - Tema - Clase.ipynb` está aprobado. Si no existe o no ha sido aprobado, avisa a Diego y pregunta si quiere generarlo primero con `generar-colab-clase` antes de continuar — el PPT se basa en el spec, pero el Colab aprobado es la señal de que el contenido ya está validado.
3. `python-pptx` instalado: `pip install python-pptx`.

## Previews — regla de uso

**No generes previews (`--preview-icn`, `--preview-hazahora`) salvo que tengas una razón técnica concreta** (ej.: necesitas validar que un bloque nuevo renderiza antes de continuar con el PPT completo). Diego solo quiere el archivo final `Clase NN - Tema - Presentación.pptx`. Los previews son para depuración interna del skill, no para el flujo normal.

## Alcance del PPT (regla permanente)

**El PPT termina en la tabla de Errores típicos. Nunca incluye Práctica Guiada, Práctica Independiente, Ticket de Salida ni Cierre.** Esas secciones se trabajan desde el Colab.

Estructura fija de slides:

```
1. Bienvenida
2. Objetivo / Propósito / Reglas
3. Haz Ahora
4..N  ICN — cantidad y composición decidida por el planificador
N+1.  Errores típicos  ← última slide
```

## Arquitectura del generador

El generador tiene tres capas:

1. **Parser** (`parsear_spec` en `crear_ppt.py`) — lee el spec y produce una estructura semántica. Los demos (`**Demostración:**`) se parsean en el cuerpo de cada concepto para que queden asociados al concepto que los precede en el spec.

2. **Planificador** (`planificar_slides.py`) — recibe los conceptos + demos y decide cuántos slides genera la ICN, qué composición tiene cada uno, y dónde intercalar los demos.

3. **Renderizador** (`crear_ppt.py`) — toma las decisiones del planificador y compone los slides con bloques visuales (cajas de definición, terminal de código, tabla, idea clave, anatomía, analogía).

## ICN: decisiones del planificador

El planificador aplica estas reglas por concepto:

| Tipo de concepto | Slide generado |
|---|---|
| Clásico (definición + código ± idea clave) | `icn_flexible`: bloques compuestos dinámicamente |
| `Tipo: anatomia` o tiene `**Partes:**` | Slide anatomía (expresión + hasta 4 partes) |
| `Tipo: analogia` o tiene `**Analogía:**` | Slide analogía (tabla vida real ↔ Python, hasta 4 filas) |
| `Tipo: antes_despues` o tiene `**Antes:**` + `**Después:**` | Slide antes/después (dos snippets paralelos) |
| `Tipo: frase_clave` | Slide frase clave grande sola |
| `**Demostración:**` en el cuerpo del concepto | Slide apilado (hasta 3 filas código + resultado), insertado inmediatamente después del concepto |

**Fusión de conceptos clásicos:** si dos conceptos clásicos adyacentes tienen densidad combinada ≤ 14 filas visuales, el planificador los fusiona en un solo slide.

**Presupuesto de densidad:** 14 filas visuales = objetivo cómodo; 16 = referencia (puede superarse si el contenido es pedagógicamente necesario). El planificador registra justificación cuando supera 16.

## ICN flexible: bloques visuales disponibles

Para conceptos clásicos, el slide se compone de bloques apilados verticalmente con alturas proporcionales a su costo:

| Bloque | Apariencia | Se genera cuando |
|---|---|---|
| `definicion` | Caja fondo oscuro, borde turquesa, label "Definición" | El concepto tiene `- Definición:` |
| `codigo` | Terminal negro, franja turquesa, fuente Consolas autoajustada | El concepto tiene `- Ejemplo:` con ```python``` |
| `idea_clave` | Caja fondo oscuro, borde ámbar, label "Idea clave" | El concepto tiene `- Idea clave:` |
| `separador` | Espacio visual entre dos conceptos fusionados | Fusión de dos conceptos |

Los bloques se distribuyen en el área 1.65"–7.20" con alturas proporcionales a su densidad estimada.

## Haz Ahora flexible

El slide de Haz Ahora se compone dinámicamente según el tipo de actividad:

**Tipo `situaciones`** (más común): el spec tiene ítems numerados (`1. ... 2. ...`). El slide tiene:
- Caja intro (borde ámbar) con la instrucción — altura calculada según largo del texto
- Caja grande (borde turquesa) con las situaciones numeradas — 20pt si ≤6 ítems, 18pt si más
- Nota de cierre en gris al fondo — **nunca incluye las respuestas esperadas**; la nota es solo logística ("¿Listo? Avísale a tu profe" o similar)

**Tipo `libre`**: sin ítems numerados. Todo el texto va en una sola caja grande con borde ámbar.

## Orden de demos en el PPT

Los bloques `**Demostración:**` del spec se insertan **inmediatamente después del concepto al que pertenecen** (el que los precede en el texto del spec), no al final de todos los conceptos. Esto asegura que la analogía, si aparece como último concepto, quede justo antes de los errores típicos.

## Sintaxis del spec (resumen)

### Concepto clásico
```markdown
**Concepto 1: Tipo booleano**
- Definición: En Python existe un tipo `bool` que solo puede ser `True` o `False`.
- Ejemplo:
  ```python
  tiene_stock = True
  print(type(tiene_stock))
  ```
- Idea clave: `True` y `False` siempre con mayúscula.
```

### Anatomía
```markdown
**Concepto 2: Operadores de comparación**
Tipo: anatomia
- Definición: Comparan dos valores y devuelven `True` o `False`.
- **Expresión:** `saldo >= precio`
- **Partes:**
  - `saldo` | operando izquierdo
  - `>=` | el operador — define el tipo de comparación
  - `precio` | operando derecho
  - Resultado | siempre `True` o `False`
- Idea clave: Una comparación siempre devuelve `True` o `False`.
```

### Analogía
```markdown
**Concepto 4: Booleanos en la vida real**
Tipo: analogia
- Definición: Las comparaciones de Python reflejan preguntas cotidianas.
- **Analogía:** Lo que te preguntas tú, Python lo resuelve con `True` o `False`.
  - ¿Te alcanza el saldo? | `saldo >= precio` → `True` o `False`
  - ¿Hay unidades? | `unidades != 0` → `True` o `False`
```

### Demostración apilada
```markdown
**Demostración: Operadores == != >**
Subtítulo: Comparando saldo = 45000 con precio = 60000.
- Fila: == | 45000 == 60000 | False — no son iguales
- Fila: != | 45000 != 60000 | True — sí son distintos
- Fila: >  | 45000 > 60000  | False — el saldo no supera el precio
```

## Cómo se ejecuta

```powershell
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" "clases/clase-NN-tema/Clase NN - Tema - Spec.md" "clases/clase-NN-tema/Clase NN - Tema - Presentación.pptx"
```

**Flags de preview** (solo si hay necesidad técnica concreta — ver sección "Previews"):
```powershell
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" spec.md preview.pptx --preview-icn
python -X utf8 ".claude/skills/generar-ppt-clase/crear_ppt.py" spec.md preview.pptx --preview-hazahora
```

**Debug de decisiones del planificador:**
```powershell
$env:DEBUG_PPT=1; python crear_ppt.py spec.md salida.pptx
```

## Código inline con backticks

Cualquier texto entre backticks `` `código` `` en el spec se renderiza en el PPT con fuente Consolas y color verdoso `#4ADFCB`, automáticamente, en cualquier bloque de texto (definición, idea clave, tabla de errores, etc.).

## Iteración

- **Cambio de contenido:** editar `Clase NN - Tema - Spec.md` y regenerar.
- **Cambio de marca visual** (colores, tipografías, posiciones): editar `construir_plantilla.py` y correrlo para regenerar `plantilla_marca.pptx`. Luego regenerar los PPT afectados.
- **Cambio de lógica de planificación:** editar `planificar_slides.py`.
- **Cambio de renderizado:** editar `crear_ppt.py`.

## Archivos en esta carpeta

| Archivo | Rol |
|---|---|
| `SKILL.md` | Este archivo |
| `crear_ppt.py` | Orquestador: parser + renderizador + constructores de slide |
| `planificar_slides.py` | Capa de planificación pedagógica (cuántos slides, qué composición) |
| `construir_plantilla.py` | Define paleta, tipografías y helpers visuales; regenera `plantilla_marca.pptx` |
| `plantilla_marca.pptx` | Plantilla con slides modelo (bienvenida, objetivo, tabla, anatomía, analogía, apilado, etc.) |

## Limitaciones conocidas

- **Haz Ahora con código Python y preguntas asociadas (`codigo_preguntas`):** el planificador no tiene un tipo dedicado para esto todavía. Si el spec trae un Haz Ahora de este tipo, el generador lo trata como tipo `libre` (todo el texto en una sola caja con borde ámbar). Si el resultado queda apretado o poco legible, avisa a Diego — puede que convenga reformular el Haz Ahora como `situaciones` o `libre` en el spec, o pausar para implementar el tipo dedicado en `planificar_slides.py`.

## Reglas críticas

1. **El PPT termina en errores típicos.** Guiada/Independiente/Ticket/Cierre solo en Colab.
2. **El spec es la fuente de verdad del contenido.** No edites el `.pptx` generado directamente.
3. **La plantilla es la fuente de verdad del estilo.** La marca no se toca clase a clase.
4. **Los demos siguen al concepto al que pertenecen** en el spec, no van al final.
5. **Si una slide queda apretada:** el texto del spec es demasiado largo — acórtalo en el spec y regenera.
6. **El slide de Reglas siempre incluye "🦻 No ocupen audífonos"** como ítem fijo. Agrégalo al construir ese slide, independiente de lo que diga el spec.
7. **Sin Markdown en el texto del PPT.** El PPT no renderiza Markdown: `**palabra**` aparece literal con los asteriscos. La negrita se aplica vía `run.font.bold = True` en python-pptx donde el diseño lo requiere, nunca con `**...**` en el texto plano.
8. **En demos/ejemplos de código, mostrar el output con `>>`** en la línea siguiente al `print()`. Ejemplo: `print("¿Te alcanza?", True)` → línea siguiente `>> ¿Te alcanza? True`. Esto va en el texto del bloque terminal del slide.
