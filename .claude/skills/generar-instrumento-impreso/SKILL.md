---
name: generar-instrumento-impreso
description: Genera la versión impresa en PDF (Clase NN - Tema - [Evaluación|Ejercitación|Control] Impresa.tex/.pdf) de una Evaluación, Ejercitación/Simulacro o Control, para rendirse en papel sin computador y así evitar copia. A diferencia de generar-clase-impresa (material de estudio condensado y re-narrado), esta skill hace una transcripción fiel y completa del instrumento — mismos ítems, mismas narrativas, mismos códigos, nada resumido ni reordenado. Usa esta skill cuando Diego pida "pasar a papel" una evaluación/ejercitación/control, mencione evitar que copien/hagan trampa, o pida una versión impresa de un instrumento que se aplica en clase.
---

# Skill: Generar Instrumento Impreso (Evaluación/Ejercitación/Control antitrampa)

## Propósito

Producir un PDF que un estudiante rinda **en papel, sin computador**, para un instrumento que originalmente vive en Colab (`Evaluación.ipynb`, `Ejercitación.ipynb`, `Control.ipynb`). El objetivo es que no se pueda copiar/pegar ni buscar la respuesta en internet mientras se rinde. Por eso, a diferencia de `generar-clase-impresa`:

- **No se resume ni se re-narra nada.** Cada ítem/ejercicio del notebook original pasa tal cual: misma narrativa, mismo código (con bug o con blanco, según corresponda), mismas pistas, mismos ejemplos de entrada/salida.
- **Se preserva la estructura de secciones e ítems del notebook**, incluidos los puntajes si el instrumento lleva nota.
- Lo único que cambia es el **mecanismo de interacción**: donde el Colab pedía completar/corregir/escribir código en una celda, el papel ofrece un espacio equivalente para hacerlo a mano.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Pasa a papel la Evaluación/Ejercitación de la clase X"
- "Necesito una versión impresa para que no puedan copiar"
- "Quiero evitar que hagan trampa en el [Control/Evaluación/Ejercitación]"

**Requisito previo:** el notebook de estudiante del instrumento (`Evaluación.ipynb`, `Ejercitación.ipynb`, o `Control.ipynb`) ya debe existir y estar aprobado — esta skill transcribe, no diseña contenido nuevo.

**Primera vez en un proyecto/carpeta de clase:** propone el plan (qué transcribir, cómo tratar el verificador digital si lo hay, nombrado de archivo) y espera aprobación antes de generar el `.tex`. Una vez aprobado el patrón para un instrumento, aplícalo directo al siguiente instrumento similar sin volver a preguntar — solo avisa qué differences de contenido aplican (ver más abajo).

## Sistema de diseño (fijado 2026-08-21, sobre Clase 27 - Evaluación Ciclos y Clase 26 - Ejercitación Ciclos)

### Motor técnico (LaTeX + tectonic) — mismo que `generar-clase-impresa`

```latex
\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{a4paper, left=2.2cm, right=2.2cm, top=2.4cm, bottom=2.0cm, headheight=14.5pt}
\usepackage{fontspec}
\IfFontExistsTF{Consolas}{\setmonofont{Consolas}[Scale=0.92]}{}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage{fancyvrb}
\usepackage{tikz}
\usepackage[most]{tcolorbox}
\usepackage{tabularx}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{parskip}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{graphicx}
```

**Fuente monoespaciada — bug conocido y su fix.** La fuente Latin Modern Mono que tectonic descarga por defecto para bloques de código tuvo, en al menos un visor de PDF, un glitch de renderizado donde la letra "i" se veía como "1" y el texto quedaba corrido hacia la derecha. El fix es fijar explícitamente `Consolas` (instalada en Windows) como fuente monoespaciada: `\IfFontExistsTF{Consolas}{\setmonofont{Consolas}[Scale=0.92]}{}` en el preámbulo. No quitar esta línea.

**Compilar:**
```bash
"$USERPROFILE/tools/tectonic/tectonic.exe" "archivo.tex"
```
**Si el PDF de destino está bloqueado** (Diego lo tiene abierto en su propio visor — síntoma: tectonic reporta `El proceso no tiene acceso al archivo`), compila a una carpeta temporal con `-o _build` y entrega ese archivo directamente con `SendUserFile`; avísale a Diego que cierre su visor para poder guardar la versión final en la ruta correcta más tarde, y limpia `_build/` una vez copiado el resultado a su ruta definitiva.

**Revisar visualmente antes de entregar:** renderiza cada página a PNG (`pymupdf`, `page.get_pixmap(dpi=150)`) y revísalas — confirma que ninguna caja tenga overflow, que el contenido de "un ejercicio por plana" efectivamente quede en una plana, y que no quede ningún fondo de color.

### Colores y cajas

```latex
\definecolor{azuloscuro}{RGB}{0,51,102}
\definecolor{verdealerta}{RGB}{0,128,0}
\definecolor{rojoalerta}{RGB}{180,0,0}
\definecolor{marcogris}{RGB}{170,170,170}
\definecolor{guialinea}{gray}{0.65}
```

**Regla no negociable: ninguna caja lleva relleno de color (`colback` siempre `white`).** El documento se imprime en blanco y negro — un fondo de color se ve como un gris sucio o desaparece, y ensucia la fotocopia. Solo el borde y el título de la caja llevan color.

Cajas reutilizables (idénticas a las de `generar-clase-impresa`, con `colback=white` siempre):
- `cajacodigo`: código de ejemplo o código con bug, fondo blanco, borde gris, `Verbatim` de `fancyvrb` adentro.
- `cajaescribe[height=Ncm]`: rectángulo blanco vacío para escribir a mano, con **líneas guía verticales punteadas** cada 0.8cm (un nivel de indentación de Python) dibujadas con un `overlay` de `tikz` sobre el marco de la caja (`enhanced` es obligatorio en las opciones del `tcolorbox` para que `frame.north west` funcione). Calibra la altura al largo esperado de la solución (3cm para corregir un bug corto, 8.5–9.5cm para un programa completo).
- `formulabox`: azul, para instrucciones y la regla de indentación.
- `alertabox`: rojo, para errores típicos (si el instrumento los trae).
- `actitudbox`: verde, para la actitud de la evaluación o el objetivo/propósito de la sesión — siempre en su propia caja destacada, nunca como texto suelto en la portada.

### Encabezado compacto (nunca portada de una hoja completa)

Logo pequeño a la izquierda + título en `\Large` a la derecha, en dos `minipage[c]` una junto a la otra — **sin subtítulo**. Todo el resto de la portada (actitud/objetivo, Nombre/Fecha/Curso, instrucciones, regla de indentación, y la tabla de puntaje si aplica) debe caber en esa misma primera plana; ajusta los `\vspace` entre bloques hasta lograrlo, nunca sacrifiques contenido.

```latex
\noindent
\begin{minipage}[c]{0.11\textwidth}
    \IfFileExists{logo.png}{\includegraphics[width=\linewidth]{logo.png}}{}
\end{minipage}%
\hspace{0.03\textwidth}%
\begin{minipage}[c]{0.82\textwidth}
    {\Large \textbf{[EVALUACIÓN INDIVIDUAL|EJERCITACIÓN|CONTROL] --- TEMA}}
\end{minipage}
```

### Regla de indentación (siempre, en toda portada)

Explica que las líneas punteadas de las cajas de escritura marcan cada nivel de anidación, con un ejemplo corto ya resuelto (ej. un `for` con un `if` adentro). **El ejemplo se muestra como imagen (`\includegraphics`), no como texto LaTeX vivo** — evita cualquier riesgo de glitch de fuente entre visores. Si no existe aún una imagen de referencia, pide a Diego que la genere con una herramienta de "code screenshot" (ray.so, carbon.now.sh: pegar el código exacto, fondo blanco/transparente, sin números de línea, exportar PNG en alta resolución) y te la entregue; si ya existe una en otra carpeta de clase de este mismo proyecto (ej. `foto_ciclo_for_portada.png`), cópiala en vez de pedir una nueva — es un ejemplo genérico de indentación, no específico de un instrumento.

### Ítems "Arma el código" (completar)

El fragmento que falta se reemplaza por una **línea en blanco larga** (subrayado extendido, no un placeholder corto) en el lugar exacto donde iría en el código, dentro de la misma `cajacodigo`. El largo de la línea debe dar espacio de sobra para cualquier tamaño de letra.

### Ítems "Arregla el bug"

Se muestra el código con el error **tal cual está** (mismo texto que en el Colab) dentro de una `cajacodigo`, seguido de una `cajaescribe` en blanco rotulada `\textit{Código corregido:}` donde el estudiante reescribe el fragmento completo y corregido.

### Pistas

**Siempre visibles**, nunca colapsadas (el papel no permite ocultar/desplegar como el `<details>` del Colab). Formato: `{\footnotesize\textit{\textbf{Pista --- Subtítulo:} texto...}}`, inmediatamente después del código o de "El programa debe".

### Programas completos / ejercicios de desarrollo — un ejercicio por plana

Cada ejercicio de desarrollo (incluida la Práctica Guiada, si el instrumento la trae) arranca en `\newpage` y contiene, en este orden: narrativa + `\textbf{El programa debe:}` (bullets) + pistas (si las trae) + tabla `Ejemplo 1`/`Ejemplo 2` compacta (`{\footnotesize ... \renewcommand{\arraystretch}{0.85} ... \begin{tabularx}{\linewidth}{|Y|Y|}`, columnas `Y` con `raggedright` para que el texto no se corte) o el bloque `\textbf{El programa imprime:}` si no usa `input()` + `\textit{Escribe tu programa aquí:}` + una `cajaescribe` grande (8.5–9.5cm, calibrada al largo esperado de esa solución particular).

### Tabla de distribución de puntaje

Solo si el instrumento lleva nota (Evaluación, Control). Tabla compacta (`\small`, `\renewcommand{\arraystretch}{0.82}`) en la portada, después de la regla de indentación. Un instrumento sin nota (Ejercitación/Simulacro) no la lleva — usa ese espacio para una caja de "Objetivo y propósito de la sesión" en su lugar.

### Cierre de actitud

Solo si el instrumento lleva nota — reutiliza la pregunta ya elegida del banco de "Cierre de actitud en Control y Evaluación" del `CLAUDE.md` raíz del proyecto, con líneas en blanco para responder a mano, al final del documento. **Nunca en un instrumento sin nota** (Ejercitación/Simulacro no llevan esta pregunta).

### Qué NUNCA va en la versión impresa

- Verificador automático / celda de autochequeo (no hay cómputo en papel).
- Ticket de Salida (sigue siendo exclusivo del día, proyectado en la tele — independiente del papel).
- Mención de la duración en minutos en la portada (Diego pidió quitarla explícitamente — la evaluación real se administra con el tiempo que el profesor determine en el momento, no queda impreso).
- Cualquier caja con fondo de color.

## Instrucciones generales adaptadas a papel

Reescribe las instrucciones del Colab quitando lo específico de Classroom/Colab y agregando lo propio del papel: letra clara, tachar y escribir al lado si hay error, prohibido celular/computador/apuntes/ayuda de compañeros, entrega en papel al profesor al terminar.

## Nombrado de archivo

`Clase NN - Tema - [Evaluación|Ejercitación|Control] Impresa.tex` / `.pdf`, en la carpeta de la clase — mismo patrón que el resto de artefactos (`Tipo` = `Evaluación Impresa`, `Ejercitación Impresa`, o `Control Impresa`).

## Assets

Copia `logo.png` y la imagen de referencia de la regla de indentación desde otra carpeta de clase que ya las tenga, en vez de regenerarlas.

## Aprobación

Mismo patrón del proyecto: propone el plan si es la primera vez, genera el `.tex`, compila, revisa visualmente página por página, y muestra el PDF a Diego antes de darlo por final. Itera en vivo sobre el mismo `.tex` según su feedback — no regeneres desde cero.

## Publicación

El repo de este proyecto es público. Un instrumento con nota (Evaluación/Control) impreso **no debe pushearse hasta después de rendido** — mismo criterio que ya rige para el Ticket de Salida y el Colab de la Evaluación/Control. Un instrumento sin nota (Ejercitación/Simulacro) puede pushearse antes si Diego lo pide, ya que no contiene soluciones. Nunca asumas que "generar" implica "publicar ya" — confirma con Diego el momento del push.
