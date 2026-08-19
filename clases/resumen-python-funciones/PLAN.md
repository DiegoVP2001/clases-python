# Plan aprobado — Resumen Python: Fundamentos a Funciones

> Plan aprobado por Diego el 2026-08-19. Ejecutar en otra sesión: escribir el `.tex`, compilar con tectonic y mostrar el PDF para revisión visual antes de darlo por final.

## Estado: ✅ Completado y aprobado (2026-08-19)

`.tex`/`.pdf` generados, compilados con tectonic sin errores (2 páginas, 2 columnas). Contenido verificado contra `curriculo_picuino_completo.md` (fichas 1-20) y los specs de las clases reales listadas abajo — incluye el patrón `resultado = funcion(argumento)` y el pitfall de `None` (print vs return) identificado en el diagnóstico de Clase 24b. Aprobado por Diego sin cambios tras revisión visual del PDF.

## Qué es esto

Un PDF de referencia compacto (cheat sheet), **no** una versión impresa de una clase puntual (eso es `generar-clase-impresa`, que narra una clase con escenario + ejemplo guiado + ejercicios). Este documento resume todo el contenido Python visto por el curso hasta ahora, desde los fundamentos hasta Funciones — sin escenarios, sin ejercicios para resolver, sin narrativa. Es un formulario de sintaxis y definiciones esenciales.

## Destinatario

Resumen general para todo el curso (no es material de apoyo individual) — sin restricción de privacidad, sin nombre de estudiante.

## Alcance de contenido (confirmado contra `Historial-Curricular.md`)

Desde los fundamentos (Picuino 1-6, ya vistos antes del inicio del `Historial-Curricular.md` pero asumidos como base) hasta Funciones (Clase 24a/24b, lo último dictado). **No incluye Strings ni Listas** (Clases 25+, "Planificada", aún no se dictan) — si para cuando se ejecute este plan ya se dictaron más clases, confirmar con Diego si corresponde ampliar el alcance antes de escribir el documento.

## Archivo de salida

`clases/resumen-python-funciones/Resumen Python - Fundamentos a Funciones.tex` / `.pdf`

(Carpeta nueva porque este artefacto es transversal — no corresponde a una carpeta `clase-NN` de una clase puntual.)

## Formato

- Mismo motor y sistema de cajas que `generar-clase-impresa` (ver `.claude/skills/generar-clase-impresa/SKILL.md`): LaTeX + tectonic, `tcolorbox` (`cajacodigo`, `formulabox`), `fontspec` + `babel[spanish,es-noshorthands]` (nunca `inputenc`/`fontenc`), sin emojis (usar negrita en su lugar).
- **2 columnas** (`multicol`) para maximizar densidad.
- **Sin portada.** Sin tabla Nombre/Fecha. Arranca con un título compacto de una línea y va directo al contenido.
- **Sin sección de errores típicos/comunes** — decisión explícita de Diego para maximizar compactación (solo formulario de sintaxis, nada más).
- **Sin cierre motivacional** — no aplica, no es material de apoyo a un estudiante específico.
- Meta: 3-4 páginas, denso pero legible.
- Por sección: definición esencial (1-2 líneas) + caja de sintaxis mínima (`cajacodigo`) + ejemplo corto **solo cuando no sea obvio** de la sintaxis sola — evitar ejemplos redundantes que inflen el documento.

## Estructura — 6 secciones, en orden de progresión curricular

1. **Datos y variables** — `int`/`float`/`str`/`bool`, asignación, snake_case, palabras reservadas
2. **Operadores** — aritméticos (`+ - * / // % **`), comparación (`== != > < >= <=`), lógicos (`and`/`or`/`not`)
3. **Entrada y salida** — `print()` (sep/end), `input()`, conversión de tipos
4. **Condicionales** — `if`/`else`, anidados, `elif`, regla de indentación
5. **Ciclos** — `for` + `range()`, `for` anidado, `continue`/`break`, `while`
6. **Funciones** — `def`, parámetros, valores por omisión, `return`

## Fuentes de contenido a consultar al redactar

No inventar contenido nuevo — reorganizar y re-narrar (muy compacto) lo ya aprobado en los specs de cada clase:

- `.claude/skills/referencia-curriculo/curriculo_picuino_completo.md` — fichas 1-20 (fundamentos hasta valores por omisión) para sintaxis exacta y foco de cada tema
- Specs aprobados de las clases reales: `clase-07-input`, `clase-08a/8b/8c`, `clase-09-if-else`, `clase-13-if-anidadas`, `clase-14-elif`, `clase-16-for-range`, `clase-20-for-avanzado`, `clase-21b-continue-break`, `clase-22-while`, `clase-24a-funciones-def`, `clase-24b-funciones-valores-omision`

## Pasos de ejecución

1. Confirmar con Diego si el alcance sigue siendo "hasta Funciones" (por si ya se dictó Strings/Listas al momento de ejecutar).
2. Redactar el `.tex` a mano (sin script generador, mismo criterio que `generar-clase-impresa`), copiando el preámbulo LaTeX de una `Clase Impresa.tex` existente (ej. `clase-24a-funciones-def/`) y agregando `multicol`.
3. Compilar con tectonic: `"$USERPROFILE/tools/tectonic/tectonic.exe" "Resumen Python - Fundamentos a Funciones.tex"`.
4. Revisar el PDF página por página (overflow de texto, cajas de color, tildes/ñ) antes de mostrárselo a Diego.
5. Mostrar a Diego para aprobación visual antes de darlo por final.
