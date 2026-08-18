---
name: generar-clase-impresa
description: Genera una versión impresa en PDF (Clase NN - Tema - Clase Impresa.tex/.pdf) de una clase, para un estudiante sin acceso a computador durante el estudio. No es una transcripción literal del Colab — fusiona el ICN con la Práctica Guiada en un solo ejemplo narrado y muy comentado, seguido de la Práctica Independiente con espacio para escribir a mano. Usa esta skill on-demand, cuando Diego pida una "versión impresa", "PDF para estudiar" o mencione que un estudiante no tiene computador en la casa — nunca automáticamente para toda clase nueva.
---

# Skill: Generar Clase Impresa (PDF de estudio sin computador)

## Propósito

Producir un documento LaTeX/PDF que le sirva a un estudiante para estudiar el contenido de una clase sin necesitar computador — a diferencia del `Clase.ipynb`, que asume Colab. No es una copia del notebook: es un material de estudio propio, con un ejemplo guiado paso a paso muy comentado y espacio físico para resolver ejercicios a mano.

## Cuándo usar esta skill

Actívate cuando Diego diga cosas como:

- "Genera la versión impresa de la clase X"
- "Necesito un PDF para que estudie en la casa"
- "[Estudiante] no tiene computador, hazle algo para estudiar"

**No se activa automáticamente para cada clase nueva** — es un workflow opcional y on-demand, igual que el Reel o el path Dodona. Ver `CLAUDE.md` § "Workflow opcional: versión impresa de una clase".

**Requisito previo:** `Clase NN - Tema - Spec.md` aprobado en `clases/clase-NN-tema/`. Si no existe, no procedas — indica a Diego que primero debe aprobar el spec.

**Privacidad:** igual que el apoyo individual (ver memoria `feedback_apoyo_individual_anonimo`), el documento nunca nombra al estudiante ni su situación. Nombre/Fecha quedan en blanco en la portada.

## Origen y decisiones de diseño (Clase 24a — 2026-08-17)

El primer intento (v1) hacía una transcripción casi literal del `Clase.ipynb` completo — Haz Ahora, los 4 conceptos del ICN por separado, Práctica Guiada, Práctica Independiente, aviso del Ticket de Salida y Cierre. Diego evaluó que **una copia textual no sirve como material de estudio** y pidió un rediseño completo. Ese rediseño (aprobado el 2026-08-17 sobre Clase 24a — Funciones) es el que documenta esta skill. El archivo `clases/clase-24a-funciones-def/Clase 24a - Funciones - Clase Impresa.tex` es la plantilla de referencia — cópiale la estructura y el sistema visual para cada clase nueva.

## Estructura del contenido (aplica a toda clase, ajustando el ejemplo/escenario)

1. **Portada:** logo + encabezado institucional + título + **Objetivo y Propósito de la clase** (tomados tal cual del Spec) + tabla Nombre/Fecha en blanco.
2. **Vocabulario nuevo:** caja de referencia rápida (`formulabox`) con los 3-5 términos nuevos de la clase, definición de una línea cada uno — sirve para consultar sin tener que buscar en el Colab.
3. **Apertura fusionada y expandida (reemplaza al Haz Ahora tal cual aparece en el Colab):** un párrafo narrativo (no una lista de preguntas) que explica (a) el problema o enredo concreto que genera la situación planteada, y (b) por qué el contenido nuevo de la clase es la herramienta que lo resuelve. Nunca copiar las preguntas del Haz Ahora tal cual — se reescribe como prosa que cumple el mismo rol de motivación.
4. **Conceptos del ICN restantes** (los que no quedaron cubiertos por la apertura fusionada): explicación compacta + ejemplo corto de código cada uno, en `cajacodigo`.
5. **Ejemplo guiado paso a paso (`estrategiabox`) — aquí se fusiona la Práctica Guiada:** resuelve el escenario de la apertura completo, con pasos numerados (`\textbf{Paso 1 --- ...}`) y código con comentarios cortos que referencian el concepto que se está aplicando en cada línea. Si el escenario del ICN y el de la Práctica Guiada del spec no comparten narrativa (a diferencia de Clase 24a, donde eran casi la misma función), evalúa con criterio propio si conviene unificarlos en un solo escenario o mantener el ejemplo guiado como una aplicación distinta que igual cierre con el mismo nivel de detalle — pregúntale a Diego si no es obvio.
6. **Errores típicos:** tabla del spec convertida a `alertabox`.
7. **Práctica Independiente:** justo después del título, la nota de autochequeo — *"Revisa en tu celular: cuando termines cada ejercicio, revisa tu respuesta en el celular — la solución completa está en el cuaderno Solucionario subido a Classroom."* Luego los ejercicios del spec, mismo formato canónico que el Colab (narrativa + "El programa debe" + tabla Entrada/Salida + caja en blanco para escribir), incluido el desafío opcional si el spec lo trae.
8. **Cierre motivacional (default desde esta sesión, 2026-08-17):** al final del documento, siempre, un mensaje corto, cercano y directo al grano — 1-2 frases, sin nombrar al estudiante ni su situación. No es el Cierre reflexivo del Colab (objetivo + preguntas de comprensión/propósito) — eso nunca va en este documento. Ejemplo usado en Clase 24a: *"Vas bien. Cada función que aprendes a construir es una herramienta más que te queda para siempre — sigue así."* Redacta uno nuevo y pertinente al contenido de cada clase, no reuses siempre la misma frase.

**Qué NUNCA va en este documento:** Ticket de Salida (ni las preguntas ni el aviso informativo) ni el Cierre reflexivo del Colab (objetivo + preguntas de comprensión/propósito a viva voz) — ambos son exclusivos del aula.

## Arquitectura: se redacta el `.tex` a mano

**No hay script generador.** El contenido requiere criterio editorial por clase (qué fusionar con qué, cómo narrar el problema) — automatizarlo con un parser mecánico del spec fue exactamente el enfoque que Diego rechazó en la v1. Redacta el `.tex` directamente, usando `Clase 24a - Funciones - Clase Impresa.tex` como plantilla de estructura y estilo, y el `Spec.md` de la clase como fuente de contenido (nunca inventes contenido nuevo — reorganiza y re-narra lo ya aprobado).

*Nota histórica:* existe un script `crear_pdf_clase.py` en `.claude/skills/generar-colab-clase/`, de la v1 rechazada — generaba una sección por cada campo del spec, en el mismo orden mecánico. No lo uses como base.

## Sistema técnico (LaTeX + tectonic)

**Motor confirmado funcionando** (no cambiar sin volver a probar):
```latex
\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{a4paper, left=2.2cm, right=2.2cm, top=3cm, bottom=2.4cm, headheight=14.5pt}
\usepackage{fontspec}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage{fancyvrb}
\usepackage[most]{tcolorbox}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{parskip}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{graphicx}
```
**Importante:** usar `fontspec` + `babel[spanish,es-noshorthands]`, NUNCA el combo `inputenc`/`fontenc` (es el que usa la guía de referencia de trigonometría, pero no está probado con tectonic en este equipo — no arriesgarlo).

**Cajas (`tcolorbox`) reutilizables** — defínelas en el preámbulo de cada `.tex` (no hay paquete compartido, se copian):
- `cajacodigo`: código de ejemplo, fondo gris (`cajagris`/`marcogris`), usa `Verbatim` de `fancyvrb` adentro — no `listings` (evita depender de `--shell-escape`).
- `cajaescribe[height=Ncm]`: rectángulo blanco vacío para escribir a mano. Calibra la altura al tamaño real de la solución (4.5cm para programas cortos, 6cm+ para los que tienen `while`/bucles).
- `formulabox`: azul (`azuloscuro`), para el vocabulario/referencia rápida.
- `alertabox`: rojo (`rojoalerta`), para errores típicos.
- `estrategiabox`: verde (`verdealerta`), para el ejemplo guiado paso a paso.

**Bug conocido — sin comas en el título de una caja.** `\begin{estrategiabox}[Texto, con coma]` rompe: tcolorbox interpreta el contenido del corchete como opciones separadas por coma y tira `pgfkeys Error: I do not know the key`. Usa `---` (guion largo) en vez de coma en cualquier título de `formulabox`/`alertabox`/`estrategiabox`.

**Sin emojis.** No hay fuente de emoji instalada — un 📥/📤/📱 sin reemplazar puede no renderizar. Siempre usar la etiqueta en negrita equivalente: `\textbf{Entrada:}`, `\textbf{Salida:}`, `\textbf{Revisa en tu celular:}`.

**Logo institucional:** portada con `\IfFileExists{logo.png}{\includegraphics[...]}{...}` — si `logo.png` no está en la carpeta de la clase nueva, cópialo desde otra carpeta de clase que ya lo tenga (ej. `clases/clase-24a-funciones-def/logo.png`) antes de compilar, o el bloque se salta solo sin romper la compilación.

**Compilar:**
```bash
"$USERPROFILE/tools/tectonic/tectonic.exe" "Clase NN - Tema - Clase Impresa.tex"
```
(o `tectonic archivo.tex` si el PATH de la sesión ya lo resuelve). Tectonic 0.17.0 está instalado en `%USERPROFILE%\tools\tectonic\tectonic.exe`. Compila dos pasadas solo si hace falta (`.aux` cambia) — es automático, no requiere intervención.

**Después de compilar:** revisa el PDF página por página (el tool `Read` puede extraer páginas como imágenes) antes de mostrárselo a Diego — confirma que no haya overflow de texto, que las cajas de color rindan bien, y que las tildes/ñ se vean correctas.

## Nombrado de archivo

`Clase NN - Tema - Clase Impresa.tex` / `.pdf`, mismo patrón que el resto de artefactos de la clase (ver `CLAUDE.md` § Organización de archivos, `Tipo` = `Clase Impresa`).

## Aprobación

Sigue el mismo patrón de aprobación explícita del resto del proyecto: propone contenido nuevo (apertura fusionada, ejemplo guiado) en chat antes de escribir el `.tex` si hay decisiones de narrativa no obvias, compila, y muestra el PDF a Diego para revisión visual antes de darlo por final.
