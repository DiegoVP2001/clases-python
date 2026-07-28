---
name: generar-kahoot
description: Genera un Kahoot diagnóstico o de repaso para las clases de Python. Propone las preguntas en chat para aprobación, luego produce un .txt importable y, si hay bloques de código o se solicita explícitamente, imágenes PNG estilo VS Code Dark+ listas para proyectar.
---

# Skill: Generar Kahoot

## Propósito

Diseñar y producir un Kahoot de diagnóstico o repaso para una clase de Python de 3ro/4to medio. El flujo tiene dos fases: primero proponer las preguntas en chat para que Diego las apruebe o ajuste; luego generar los artefactos finales.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Genera un Kahoot para la clase X"
- "Hagamos un Kahoot de repaso"
- "Necesito un Kahoot diagnóstico"
- "Crea preguntas para Kahoot"

## Preguntas iniciales (hacer todas antes de proponer nada)

Antes de diseñar las preguntas, confirma con Diego:

1. **¿Qué contenidos cubre el Kahoot?** (diagnóstico post-vacaciones, repaso de un tema específico, cierre de unidad, etc.)
2. **¿Cuántas preguntas?** — por defecto: **12**
3. **¿Es diagnóstico o evaluativo?** — afecta el tono: diagnóstico = sin consecuencias de nota, liviano; evaluativo = más exigente
4. **¿Hay algún contexto temático preferido?** (videojuegos, deportes, precios, etc.) — si no, mezclar

Si Diego ya entregó esta información al activar la skill, no preguntes de nuevo.

## Fase 1 — Propuesta de preguntas (en chat)

Presenta las preguntas organizadas en bloques temáticos. Cada pregunta en este formato exacto:

```
**Pregunta N:**
[enunciado en español con tildes y ¿/? correctos]
[bloque de código si aplica, indentado con 4 espacios]
- opción 1
- opción 2
- opción 3
- opción 4
✅ Respuesta correcta: [texto completo de la alternativa correcta]
⏱ Tiempo: [15 seg conceptual / 20 seg con código]
```

### Reglas de diseño de preguntas

- **Sin A) B) C) D)** en las alternativas — solo el texto de cada opción
- **Distractores plausibles**, no absurdos: si la respuesta correcta es `str`, los distractores son `int`, `float`, `bool`, no `lista` o `función`
- **Preguntas con código**: usar variables en español snake_case y contextos chilenos (precios CLP, nombres locales)
- **No usar** `elif`, funciones, listas, ciclos ni contenido no visto en la progresión Picuino hasta la clase indicada
- **Tiempo**: 20 seg para predicciones de output o bugs; 15 seg para preguntas conceptuales
- **Distribución sugerida** para un Kahoot de 12 preguntas de repaso general:
  - Variables y tipos: 3 preguntas
  - Booleanos y comparaciones: 3 preguntas
  - Operadores lógicos: 2 preguntas
  - if / else: 4 preguntas
  - Ajustar la distribución según los contenidos indicados por Diego

### Preguntas con código: hacerlas concretas

Evita preguntas abstractas como "¿Qué devuelve `True and False`?". En cambio, usa un bloque de código con variables reales:

```python
# Bien
tiene_plata = True
llego_a_tiempo = False
print(tiene_plata and llego_a_tiempo)
```

Esto hace la pregunta más clara para proyectar y más fácil de entender para los estudiantes.

**Espera aprobación explícita de Diego antes de generar cualquier archivo.**

---

## Fase 2 — Generación de artefactos

Una vez aprobadas las preguntas, genera los siguientes artefactos:

### Artefacto 1 — Archivo .txt

Guárdalo en `clases/clase-NN-tema/Clase NN - Tema - Kahoot.txt`.

Formato exacto del archivo:

```
KAHOOT — [título descriptivo]
[subtítulo opcional]
=====================================


── BLOQUE 1: [nombre del bloque] ──────────────────────────────


Pregunta 1:
[enunciado]
[código si aplica, indentado con 8 espacios]
opción 1
opción 2
opción 3
opción 4
Respuesta correcta: [texto completo]


Pregunta 2:
...
```

Reglas del .txt:
- `Pregunta N:` sola en su línea; el enunciado en la línea siguiente
- Las alternativas sin prefijo de letra (sin A), B), etc.)
- `Respuesta correcta:` con el texto completo de la alternativa, no la letra
- Separar preguntas con una línea en blanco
- Tildes, ¿/? y caracteres especiales correctos

### Artefacto 2 — Imágenes PNG (cuando aplica)

Generar imágenes para **todas las preguntas que contengan un bloque de código**. También generarlas si Diego lo solicita explícitamente.

Guardarlas en `clases/clase-NN-tema/imagenes-codigo/` con nombres `pNN.png` (p02.png, p07.png, etc., según el número de pregunta).

**Especificaciones de imagen (no cambiar sin instrucción de Diego):**

```python
FONT_PATH = 'C:/Windows/Fonts/consola.ttf'  # Consolas
FONT_SIZE = 42
PAD_X, PAD_Y = 60, 50
LINE_H = FONT_SIZE + 18  # 60px por línea

# Colores VS Code Dark+
BG      = '#1e1e1e'
KEYWORD = '#569cd6'   # if, else, print, True, False, and, or, not
STRING  = '#ce9178'   # "texto"
NUMBER  = '#b5cea8'   # números
VAR     = '#9cdcfe'   # variables
DEFAULT = '#d4d4d4'   # operadores y resto
BLANK   = '#ff6b6b'   # ___ (hueco en preguntas de completar)
```

El ancho de la imagen se ajusta automáticamente al contenido; el alto depende del número de líneas.

El script de generación usa `Pillow` con tokenización manual para syntax highlighting. Seguir el mismo patrón del script ya usado en `clase-10-recordatorio` (tokenize por strings, keywords, números, variables).

---

## Organización de archivos

```
clases/clase-NN-tema/
├── Clase NN - Tema - Kahoot.txt
└── imagenes-codigo/
    ├── pNN.png
    └── ...
```

## Notas de uso

- El .txt es el artefacto principal para importar en Kahoot vía "Importar con IA" (subir PDF o .txt).
- Las imágenes son para proyectar en aula durante la sesión del Kahoot — tamaño optimizado para proyector.
- Si Diego pide ajustar el tamaño de fuente de las imágenes, modificar `FONT_SIZE` y `PAD_X/PAD_Y` proporcionalmente.
