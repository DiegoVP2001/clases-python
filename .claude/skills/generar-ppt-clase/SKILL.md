---
name: generar-ppt-clase
description: Genera la presentación PowerPoint (03-presentacion.pptx) de una clase a partir del spec aprobado. El PPT cubre desde la bienvenida hasta los errores típicos — todo lo que se trabaja en pantalla antes de abrir el computador. La Práctica Guiada, Independiente, Ticket y Cierre se trabajan desde el Colab. Usa esta skill después de que el 01-clase.ipynb esté aprobado.
---

# Skill: Generar presentación PowerPoint (03-presentacion.pptx)

## Propósito

Producir el archivo `.pptx` de una clase listo para usar en aula: fondo oscuro `#1A1A2E`, paleta turquesa + ámbar, Consolas para código. El PPT cubre lo que el profesor proyecta para presentar el contenido nuevo — no incluye las actividades que los estudiantes hacen en Colab.

## Cuándo usar

Actívate cuando Diego diga "Genera el PPT", "Pasemos al PowerPoint" o equivalente.

**Requisitos previos:**
1. `clases/clase-NN-tema/00-spec.md` existe y está aprobado.
2. `01-clase.ipynb` está aprobado (idealmente).
3. `python-pptx` instalado: `pip install python-pptx`.

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
- Nota de cierre en gris al fondo

**Tipo `libre`**: sin ítems numerados. Todo el texto va en una sola caja grande con borde ámbar.

**Caso futuro (TODO en código):** Haz Ahora con código Python y preguntas asociadas → tipo `codigo_preguntas`, pendiente de implementar.

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
python ".claude/skills/generar-ppt-clase/crear_ppt.py" "clases/clase-NN-tema/00-spec.md" "clases/clase-NN-tema/03-presentacion.pptx"
```

**Flags de preview** (para validar una sección antes del PPT completo):
```powershell
# Solo slides de ICN:
python crear_ppt.py spec.md preview-icn.pptx --preview-icn

# Solo slide de Haz Ahora:
python crear_ppt.py spec.md preview-ha.pptx --preview-hazahora
```

**Debug de decisiones del planificador:**
```powershell
$env:DEBUG_PPT=1; python crear_ppt.py spec.md salida.pptx
```

## Código inline con backticks

Cualquier texto entre backticks `` `código` `` en el spec se renderiza en el PPT con fuente Consolas y color verdoso `#4ADFCB`, automáticamente, en cualquier bloque de texto (definición, idea clave, tabla de errores, etc.).

## Iteración

- **Cambio de contenido:** editar `00-spec.md` y regenerar.
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

## Reglas críticas

1. **El PPT termina en errores típicos.** Guiada/Independiente/Ticket/Cierre solo en Colab.
2. **El spec es la fuente de verdad del contenido.** No edites el `.pptx` generado directamente.
3. **La plantilla es la fuente de verdad del estilo.** La marca no se toca clase a clase.
4. **Los demos siguen al concepto al que pertenecen** en el spec, no van al final.
5. **Si una slide queda apretada:** el texto del spec es demasiado largo — acórtalo en el spec y regenera.
