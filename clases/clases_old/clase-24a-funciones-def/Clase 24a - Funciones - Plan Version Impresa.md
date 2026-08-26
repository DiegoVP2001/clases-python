# Plan de trabajo: versión impresa (.tex → PDF) del Colab de clase

**Fecha:** 2026-08-17
**Estado:** Cerrado — v1 (copia textual del Colab) generada, compilada y revisada, pero Diego determinó que ese enfoque no sirve como material de estudio. Ver "Clase 24a - Funciones - Prompt Rediseño Impresa.md" (misma carpeta) para el rediseño pedido, que otra sesión debe ejecutar preguntando en el camino.

## Contexto y decisión

Diego pidió que, de ahora en adelante, en el mismo ciclo inicial donde se generan los Jupyter (Colab de clase), el Ticket de Salida y Dodona, también se genere un `.tex` del Colab de clase adaptado y renderizado a PDF — para una estudiante que no puede estudiar en computador. Este documento es el plan aprobado en chat antes de ejecutar el ejemplo para `clase-24a-funciones-def`.

**Confirmado con Diego (vía preguntas antes de este plan):**
- Cobertura completa de `Clase.ipynb`: Haz Ahora + ICN + Práctica Guiada + Práctica Independiente + Cierre.
- La estudiante sí tiene acceso a computador en otros momentos → **no** se necesita versión impresa del Solucionario, el `Solucionario.ipynb` normal le sirve igual.
- Las celdas de código vacías ("Tu programa", "Tu solución del Ejercicio N") se resuelven a mano: recuadro rectangular en blanco para escribir.
- Se genera en el mismo gate que `Clase.ipynb` (Etapa 3, dentro de la skill `generar-colab-clase`), no como paso aparte.

## Verificaciones técnicas previas

- **Tectonic 0.17.0 está instalado localmente** (`tectonic --version` funciona). Es un motor LaTeX autocontenido (XeTeX), compila `.tex → .pdf` sin necesitar una instalación completa de TeXLive/MiKTeX. Se puede compilar el PDF directamente, no solo generar el `.tex` fuente.
- **`crear_colab.py`** (el generador actual de `Clase.ipynb`, en `.claude/skills/generar-colab-clase/`) ya parsea `Spec.md` a un diccionario estructurado vía `parsear_spec()` antes de construir las celdas del notebook. Esa función se reutiliza como fuente de verdad del `.tex`, en vez de convertir el `.ipynb` ya generado — evita parsear HTML/JSON frágil y evita tener dos fuentes de verdad divergentes.

## Arquitectura

- Nuevo script `crear_pdf_clase.py` en `.claude/skills/generar-colab-clase/`, que importa `parsear_spec()` de `crear_colab.py` y emite LaTeX desde el mismo dict de secciones.
- Compilación con `tectonic archivo.tex` (autodescarga paquetes la primera vez, luego cachea).
- Paquetes: `fontspec` (UTF-8 nativo, tildes/ñ sin drama), `babel[spanish]`, `listings` (código Python resaltado, sin depender de `minted`/pygments que necesita `--shell-escape`), `tcolorbox`/`mdframed` (cajas de pista y cajas de "escribe aquí"), `geometry`, `tabularx`.

## Conversión de contenido

| Elemento en Clase.ipynb | Tratamiento en el PDF |
|---|---|
| Emojis (💡📥📤🎯...) | Etiqueta de texto en negrita equivalente (**Pista**, **Entrada:**, **Salida esperada:**) — evita depender de una fuente emoji instalada |
| `<details>` (pistas colapsables) | Recuadro con fondo gris, encabezado "Pista (opcional)" — siempre visible (no se puede colapsar en papel) |
| Celda de código vacía ("Tu programa", "Tu solución del Ejercicio N") | Recuadro rectangular en blanco de altura fija para escribir a mano |
| Celda de ejemplo/demo ya resuelta | Bloque de código con salida esperada debajo, misma convención `>>` que ya usa el proyecto |
| Tabla Ejemplo 1/Ejemplo 2 | Tabla LaTeX de 2 columnas |
| Aviso del Ticket de Salida | Se mantiene igual (texto informativo) — la estudiante responde el Form en clase con el resto del curso, eso no cambia |

## Dónde queda documentado (si se aprueba el ejemplo)

Cambio sistémico, no solo de esta clase (regla de "Convenciones de iteración y feedback" del CLAUDE.md del proyecto):

- `CLAUDE.md`: nuevo `Tipo` de archivo ("Clase Impresa") en la convención de nombrado + fila en el árbol de "Organización de archivos".
- `generar-colab-clase/SKILL.md`: este paso queda documentado como parte fija de la Etapa 3, junto a `Clase.ipynb` + `Solucionario.ipynb` + Ticket de Salida.

## Ejecución del ejemplo (clase-24a-funciones-def)

1. Escribir `crear_pdf_clase.py`.
2. Generar `Clase 24a - Funciones - Clase Impresa.tex` desde el Spec.md ya aprobado.
3. Compilar con `tectonic` → `.pdf`.
4. Mostrar el resultado a Diego para revisión visual antes de fijarlo como parte permanente del flujo.
5. Con la aprobación del ejemplo, actualizar CLAUDE.md/SKILL.md para que aplique desde ahora a toda clase nueva.

## Riesgos / puntos a calibrar con el ejemplo

- Tamaño de los recuadros en blanco: ¿espacio suficiente para todos los ejercicios, o varía según complejidad?
- Extensión total del PDF: una clase completa impresa es más larga que en pantalla — puede requerir ajustar tamaño de letra o layout.
- Confirmar en la compilación de prueba que tildes/ñ y caracteres especiales se ven bien con tectonic+xelatex (debería ser automático por UTF-8 nativo).

## Cierre — 2026-08-17

El ejemplo se generó, se compiló con tectonic y se revisó visualmente (7 páginas, cobertura completa de Haz Ahora + ICN + Guiada + Independiente + Cierre, con recuadros en blanco y tablas de resultado funcionando bien tras 2 rondas de corrección). Pero el veredicto de Diego fue que **una transcripción literal del Colab a PDF no sirve como material de estudio**. Pidió en cambio un rediseño con otro enfoque de contenido (ICN como un solo ejemplo guiado, muy bien comentado, en vez de conceptos sueltos) y otro sistema visual (tomando como referencia `a_tex_Guía Final Funciones Trigonométricas.tex` + `logo.png`, ambos en esta misma carpeta). El rediseño completo queda especificado en **`Clase 24a - Funciones - Prompt Rediseño Impresa.md`** — no se ejecutó en esta sesión a pedido explícito de Diego; queda para que otra sesión lo tome y pregunte en el camino.

**Qué sigue siendo válido de este plan / de la v1 para el rediseño:**
- Tectonic 0.17.0 quedó instalado en este equipo en `%USERPROFILE%\tools\tectonic\tectonic.exe` y agregado al PATH de usuario (no estaba pese a que este plan lo daba por hecho — probablemente por la migración de PC). No hace falta reinstalarlo.
- `parsear_spec()` de `crear_colab.py` sigue siendo una fuente de verdad parseada del Spec.md, reutilizable si el rediseño decide seguir generando desde el spec en vez de redactar el `.tex` a mano (como parece hacerse en el archivo de referencia de trigonometría).
- `.claude/skills/generar-colab-clase/crear_pdf_clase.py` (el script de la v1) y los archivos `Clase 24a - Funciones - Clase Impresa.tex`/`.pdf` generados quedan en el repo como referencia técnica del intento rechazado — no como base de diseño a mantener. El rediseño puede reescribirlos por completo.
