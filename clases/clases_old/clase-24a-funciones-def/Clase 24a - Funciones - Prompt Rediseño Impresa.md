# Prompt: rediseño de la versión impresa (Clase 24a — Funciones)

**Fecha:** 2026-08-17
**Estado:** Pendiente de ejecución. Diego pidió explícitamente NO ejecutar este rediseño en la sesión donde se escribió este prompt — queda para que otra sesión lo tome.

**Instrucción de Diego para quien tome esto:** "pregúntame en el camino" — no asumas las decisiones de diseño que quedan abiertas más abajo. Interactúa con Diego antes de comprometerte a una versión (la skill `conoce-tus-incognitas` de este proyecto tiene técnicas para esto — blindspot pass, entrevista antes de proponer, plan modificable — úsala si el trabajo lo amerita). Este es un flujo `clases/claude_python/` normal: sigue el patrón de aprobación explícita antes de generar el artefacto final.

**Importante — la propuesta de contenido de la sección siguiente NO está escrita en piedra.** Diego fue explícito: lo que sigue es *su propuesta inicial*, para que el agente que retome esto también la evalúe con criterio propio, no solo la ejecute. Trátala como punto de partida de la conversación, no como especificación cerrada. Si el agente ve una mejor forma de resolver "ICN como ejemplo guiado + espacio de Independiente" — o considera que alguna parte de la propuesta no es la mejor opción pedagógica u óptica —, debe decírselo a Diego y proponer alternativas antes de construir, no simplemente implementar lo que sigue al pie de la letra.

## Contexto

Ya existe un intento previo (v1) de generar una versión impresa (PDF) del Colab de clase para una estudiante sin acceso a computador durante el estudio. Ese intento está documentado completo en `Clase 24a - Funciones - Plan Version Impresa.md` (misma carpeta) — léelo primero para el contexto técnico (parser reutilizado, instalación de tectonic, etc.), pero su diseño **fue rechazado por Diego** y no debe repetirse.

**Qué se generó en la v1 (rechazado):** una transcripción casi literal y en orden del `Clase.ipynb` completo — Haz Ahora, los 4 conceptos del ICN uno por uno, Práctica Guiada, los 4 ejercicios de Práctica Independiente, aviso del Ticket de Salida, y Cierre — con recuadros en blanco para escribir a mano. Técnicamente compiló bien (tectonic, sin errores, tildes/ñ correctos), pero **Diego evaluó que la copia textual no sirve como material de estudio.**

## Propuesta de Diego para el rediseño (a evaluar, no fija — ver aviso arriba)

1. **No es una copia textual.** El documento necesita un enfoque distinto, no una transcripción del Colab.
2. **Debería enfocarse desde el contenido nuevo (ICN)**, resuelto como **un ejemplo guiado bien explicado paso a paso** — código muy bien comentado y referenciado con lo que se está pidiendo/enseñando en cada paso. Es decir: en vez de los 4 conceptos sueltos de la v1 (función/por qué, `def`+parámetros, llamar con argumentos, `return`), construir **un solo recorrido narrado y paso a paso** donde el código mismo (con comentarios ricos) va enseñando cada concepto en el punto donde aparece — algo en el espíritu de los "Ejercicio modelado" y las cajas `estrategiabox` con `\textbf{Paso 1 --- ...}` del archivo de referencia de trigonometría (ver más abajo).
3. **Después, el espacio respectivo para las prácticas independientes** — la Práctica Independiente (los 4 ejercicios, con su narrativa + "El programa debe" + resultado esperado + espacio en blanco para escribir) sí debería seguir presente, a continuación del ejemplo guiado.
4. **Sin el Ticket de Salida ni el Cierre del Colab** — ninguno de los dos va en este documento impreso, en ninguna forma (ni siquiera como aviso informativo, que es como quedó en la v1 rechazada).

## Preguntas abiertas — CONFÍRMALAS CON DIEGO ANTES DE CONSTRUIR

Diego no las respondió explícitamente en su pedido; no las asumas:

1. **¿Entra el Haz Ahora?** Diego dijo que el documento "debería enfocarse *desde* el contenido nuevo" — eso podría significar que el Haz Ahora tampoco va (se dejó fuera de la lista de lo que sí debe incluirse), o simplemente que quiso decir que el ICN es el punto de partida *conceptual* del rediseño sin pronunciarse sobre el Haz Ahora. Pregúntale directamente.
2. **¿Entra el Objetivo/Propósito de la clase?** Tampoco se mencionó. Podría ir en la portada (como hace la guía de trigonometría, que no tiene objetivo/propósito de clase sino un encabezado institucional) o quedar fuera.
3. **¿La Práctica Guiada de la v1 desaparece, se fusiona con el ejemplo guiado del ICN, o se mantiene aparte?** Por cómo está redactado el pedido ("un ejemplo guiado... y después el espacio... para las prácticas independientes"), lo más probable es que el "ejemplo guiado paso a paso" del punto 2 de arriba *reemplace* tanto al recorrido conceptual del ICN como a la Práctica Guiada actual (fusionándolos en un solo recorrido narrado), pero confírmalo — es una decisión de contenido, no solo de forma.
4. **¿La tabla de "Errores típicos a evitar" del ICN se mantiene?** No se mencionó. Podría integrarse como una caja `alertabox` (rojo) al estilo del archivo de referencia, ya que ese estilo visual existe justo para eso.
5. **¿Se conserva el bloque introductorio de "En cada ejercicio escribe tu programa dentro de la celda que ya trae el comentario..."?** Ese texto es específico de Colab/Jupyter (celdas, verificador automático) y no tiene sentido tal cual en papel — probablemente haya que reescribirlo o quitarlo, pero confírmalo.
6. **¿Tamaño/cantidad de página objetivo?** La v1 dio 7 páginas. Un solo ejemplo guiado muy comentado puede ocupar bastante espacio — vale la pena preguntar si Diego tiene una extensión en mente (o si prefiere que quede lo que quede, priorizando claridad sobre longitud).

## Referencia de diseño visual — usar como base

Diego indicó que le gustó cómo funciona el estilo de **`a_tex_Guía Final Funciones Trigonométricas.tex`** (en esta misma carpeta) y pidió usar el logo **`logo.png`** (también en esta carpeta — el logo del Liceo Bicentenario Mario Bertero Cevasco). Nota: ese archivo `.tex` es de un ramo distinto (Matemáticas M2, guía de Funciones Trigonométricas) — está en esta carpeta solo como referencia de estilo que Diego dejó a mano, no es un artefacto de este curso de Python. No tiene relación temática con Clase 24a; solo se reutiliza su sistema visual.

**Elementos concretos a reutilizar/adaptar de ese archivo** (con número de línea aproximado en la versión actual):

- **Preámbulo y paquetes** (líneas 1–24): `babel[spanish]`, `inputenc`/`fontenc` (nota: es el combo clásico de pdfLaTeX, no fontspec/XeLaTeX como usó la v1 rechazada — probar que compila bien con tectonic antes de asumir que sirve tal cual), `geometry`, `fancyhdr`, `enumitem`, `booktabs`, `xcolor`, `tcolorbox`, `titlesec`.
- **Paleta de colores** (líneas 37–40): `azuloscuro` (RGB 0,51,102), `grisclaro`, `verdealerta`, `rojoalerta`.
- **Formato de secciones** (líneas 43–45) vía `titlesec`: `\section` en azul con regla horizontal debajo, `\subsection` en azul, `\subsubsection` tipo run-in.
- **Cajas temáticas `tcolorbox`** (líneas 56–86): `formulabox` (gris/azul, para reglas o definiciones fijas), `alertabox` (rojo, para errores frecuentes — encaja directo con la tabla "Errores típicos" del spec), `estrategiabox` (verde, para procedimientos/pasos — encaja directo con el "ejemplo guiado paso a paso" que pidió Diego), `ejemplobox` (azul claro, para ejemplos resueltos). Repropone nombres/colores si conviene para el dominio de programación (ej. una caja para "idea clave" de cada concepto, si al final se conservan como apoyo del ejemplo guiado).
- **Portada** (líneas 113–153): logo centrado vía `\IfFileExists{logo.png}{\includegraphics[width=0.35\textwidth]{logo.png}}`, encabezado institucional (Liceo, departamento, profesor), título grande, tabla Nombre/Fecha con `\rule{9cm}{0.4pt}`, regla horizontal de cierre, `\newpage`.
- **Encabezado de página** (líneas 159–161) vía `fancyhdr`: nombre del ramo a la izquierda, profesor a la derecha.
- **Ejemplo paso a paso numerado** (patrón usado repetidamente, ej. líneas 395–420 y 466–504): dentro de una `ejemplobox`, pasos con `\textbf{1. ...}`, `\textbf{2. ...}` etc., cada uno con su fórmula/código y una frase que conecta con el paso anterior. Este es el patrón más relevante para lo que pidió Diego: aplicarlo a un programa Python real en vez de a álgebra.
- **Tablas resumen** con `booktabs` (`\toprule`/`\midrule`/`\bottomrule`) en vez de las tablas HTML `<table>` que trae el spec — más prolijas en papel.

**Qué NO es necesario traer:** `tikz`/`pgfplots` (son para las gráficas trigonométricas, no aplican a una clase de funciones Python), el índice (`\tableofcontents`) probablemente no hace falta para un documento de una sola clase (evaluar con Diego), las secciones de "Ejercicios tipo DEMRE"/"Ticket de salida"/"Solucionario" de ese archivo son estructura de una guía de repaso M2 — no calzan con esta clase y no deben copiarse tal cual, solo su *sistema visual*.

## Fuente de contenido

El contenido en bruto (narrativas, código de ejemplo, "El programa debe", resultado esperado de cada ejercicio) sigue viviendo en `Clase 24a - Funciones - Spec.md` (misma carpeta) — es la fuente de verdad aprobada de la clase. El rediseño no debería inventar contenido nuevo desde cero, sino reorganizar y re-narrar el contenido ya aprobado del spec bajo el nuevo formato. Si hace falta contenido que el spec no tiene (ej. comentarios de código más extensos para el ejemplo guiado), constrúyelo a partir de lo que el spec ya define (los 4 conceptos del ICN + la Práctica Guiada), no de cero — y muéstraselo a Diego para aprobación antes de darlo por definitivo, como en cualquier otro artefacto de este flujo.

`.claude/skills/generar-colab-clase/crear_pdf_clase.py` (el script Python que generó la v1, reutilizando `parsear_spec()` de `crear_colab.py`) puede servir de referencia técnica para los helpers de escapado LaTeX / markdown inline (`esc()`, `md_inline()`, etc.) si el rediseño sigue generándose por script — pero su arquitectura de "una sección por cada campo del spec, en el mismo orden" es exactamente el enfoque que Diego rechazó, así que no uses su `construir_documento()` como plantilla de estructura. Evalúa con Diego si conviene seguir generando por script (como la v1) o redactar el `.tex` directamente a mano por clase (como parece estar hecho el archivo de referencia de trigonometría) — dado que el nuevo enfoque es más narrativo y menos mecánico, redactar a mano (o con más criterio editorial que un parser genérico) podría ser lo que mejor sirve aquí. Es otra decisión para preguntar, no asumir.

## Notas técnicas heredadas (siguen vigentes)

- **Tectonic 0.17.0** está instalado en este equipo en `%USERPROFILE%\tools\tectonic\tectonic.exe` y agregado al PATH de usuario (efectivo en terminales nuevas). No hace falta reinstalar.
- Compilar con: `tectonic "ruta\al\archivo.tex"` desde la carpeta de la clase (o con ruta completa).
- Si se reutiliza el preámbulo `inputenc`/`fontenc` del archivo de trigonometría (en vez de `fontspec` como usó la v1), probar la compilación con tectonic antes de dar por sentado que las tildes/ñ se ven bien — la v1 confirmó que `fontspec` + `babel[spanish,es-noshorthands]` funciona sin problemas, pero no se probó el combo `inputenc`/`fontenc` del archivo de trigonometría en este entorno.

## Alcance de esta tarea

**Qué SÍ hacer cuando se retome:**
1. Evaluar con criterio propio la propuesta de contenido de Diego (sección de arriba) — no es una especificación cerrada. Si hay una mejor forma de resolverla, o dudas sobre alguna parte, decírselo y discutirlo antes de dar la dirección por definida.
2. Responder las preguntas abiertas de la sección de arriba con Diego (entrevista breve, no todo de una vez si no hace falta).
3. Proponer una estructura del nuevo documento en chat (secciones, qué cajas se usan para qué) y esperar aprobación antes de escribir el `.tex`.
4. Generar el `.tex`, compilar con tectonic, y volver a mostrar el PDF a Diego para revisión visual — igual que se hizo con la v1.
5. Recién con la aprobación del rediseño, evaluar si esto se documenta como parte fija del flujo (`CLAUDE.md`/`SKILL.md` de `generar-colab-clase`) para las próximas clases, o si queda como un artefacto puntual de Clase 24a.

**Qué NO hacer sin que Diego lo pida de nuevo:**
- No reescribir ni borrar `Clase 24a - Funciones - Clase Impresa.tex`/`.pdf` (v1) sin confirmar — quedan como referencia del intento rechazado hasta que el rediseño los reemplace explícitamente.
- No asumir ninguna de las preguntas abiertas de la sección anterior.
- No generalizar el rediseño a otras clases hasta que Diego apruebe el resultado de Clase 24a.
