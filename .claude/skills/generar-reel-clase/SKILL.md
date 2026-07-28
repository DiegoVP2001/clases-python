---
name: generar-reel-clase
description: Genera el Reel de contenido de una clase (Clase NN - Tema - Reel.mp4) en formato vertical 1080×1920 usando Remotion. Activa esta skill después de que el PPT esté aprobado y Diego confirme que quiere el reel. Es un paso opcional al final del flujo de producción.
metadata:
  tags: remotion, video, reel, contenido, python, instagram, shorts
---

## Cuándo usar

Etapa 6 del flujo de producción de clases, después del PPT aprobado. Solo si Diego confirma que quiere el reel. No generar sin confirmación explícita.

## Qué produce

`clases/clase-NN-tema-breve/Clase NN - Tema - Reel.mp4` — video vertical ~45s para Instagram Reels, YouTube Shorts y TikTok.

---

## Proyecto Remotion

- **Ubicación**: `tools/reel-generator/` (raíz del repo)
- **Archivo principal a editar por clase**: `tools/reel-generator/src/Composition.tsx`
- **Preview**: `cd tools/reel-generator && npm run dev` → http://localhost:3000
- **Render final**: ver sección "Renderizar el MP4"

---

## Flujo de trabajo

### Paso 1 — Leer el Spec y proponer el contenido en chat

Lee `clases/clase-NN-tema/Clase NN - Tema - Spec.md` y extrae:

**Hook (1 pregunta):**
- Basada en el Propósito o el Haz Ahora del spec
- Debe apelar a contextos reales que los estudiantes reconocen (redes sociales, streaming, juegos, apps)
- Formato: "¿Sabías que [app/plataforma real] usa [concepto] para [acción cotidiana]?"

**Conceptos (N escenas, uno por concepto del ICN):**
Por cada concepto, extraer:
- `operator`: nombre del concepto en Python (`and`, `if`, `for`, etc.)
- `emoji`: emoji representativo
- `accentColor`: color de la paleta según tipo (ver tabla)
- `rule`: regla en UNA línea, sin jerga técnica, que un estudiante entienda sin saber Python
- `ruleHighlight`: UNA palabra de la regla para resaltar
- `code`: código Python de ejemplo, máximo 5 líneas, variables en español snake_case
- `output`: resultado exacto del print (una línea)

**Errores típicos (1, 2 o 3):**
- Preguntar a Diego: "¿Cuántos errores típicos quieres mostrar? (1, 2 o 3)"
- Por cada error: `title` (nombre del error), `bad` (código incorrecto, ≤4 líneas), `good` (código correcto, ≤3 líneas)

Presentar todo esto en chat y esperar aprobación explícita de Diego antes de tocar ningún archivo.

---

### Paso 2 — Actualizar Composition.tsx

Una vez aprobado el contenido, editar `tools/reel-generator/src/Composition.tsx`.

**Estructura de variables a reemplazar:**

```typescript
// ── Códigos de ejemplo (uno por concepto) ────────────────────────
const CONCEPTO_1_CODE = `
variable_1 = valor
variable_2 = valor
resultado = variable_1 operador variable_2
print("Descripción:", resultado)`;

// ── Errores típicos ────────────────────────────────────────────────
const ERRORS: ErrorExample[] = [
  {
    title: "Nombre del error",
    bad: `código incorrecto aquí`,
    good: `código correcto aquí`,
  },
  // Agregar según ERRORS_TO_SHOW
];
const ERRORS_TO_SHOW = 2; // 1, 2 o 3

// ── En el JSX de ClassReel, una ConceptScene por concepto ─────────
<ConceptScene
  operator="nombre"
  emoji="🔢"
  accentColor="#4B8BBE"
  rule="Regla en una línea sin jerga"
  ruleHighlight="Palabra clave"
  code={CONCEPTO_1_CODE}
  output="Resultado del print"
/>
```

**Ajustar `NUM_TRANSITIONS`:** 
- Hook→Título + Título→Concepto_1 + entre conceptos (N-1) + último_concepto→Errores + Errores→CTA
- Fórmula: `2 + (N-1) + 1 + 1 = N + 3`

**`REEL_DURATION` se recalcula automáticamente** vía `conceptDuration()` — no hardcodear.

**Actualizar el HookScene si el texto del hook cambia:**
Editar `tools/reel-generator/src/scenes/HookScene.tsx` — el texto de la pregunta está hardcodeado en el JSX.

**Actualizar el TitleScene si el tema cambia:**
Editar `tools/reel-generator/src/scenes/TitleScene.tsx` — el título, subtítulo y badges están hardcodeados.

---

### Paso 3 — Preview y aprobación

```bash
cd tools/reel-generator
npm run dev          # → http://localhost:3000
```

Para ver frames específicos sin abrir el Studio:
```bash
npx remotion still ClassReel --frame=60  --output=preview/hook.png   --scale=0.3
npx remotion still ClassReel --frame=200 --output=preview/concepto.png --scale=0.3
npx remotion still ClassReel --frame=N   --output=preview/frame-N.png  --scale=0.3
```

Esperar aprobación de Diego. Iterar sobre diseño si es necesario.

---

### Paso 4 — Renderizar el MP4

```bash
cd tools/reel-generator
npx remotion render ClassReel \
  --output "../../clases/clase-NN-tema-breve/Clase NN - Tema - Reel.mp4"
```

El render tarda 3-8 minutos dependiendo de la duración.

---

### Paso 5 — Cierre

1. Confirma a Diego que `Clase NN - Tema - Reel.mp4` se renderizó y dónde está.
2. Registra en `Clase NN - Tema - Historial.md`:

   ```markdown
   ## [fecha] — Reel generado
   - Archivo: Clase NN - Tema - Reel.mp4
   - Errores mostrados: N
   - [notas de iteraciones si las hubo]
   ```

3. Commitea y pushea **solo la carpeta de esta clase** a GitHub (ver "Protocolo de cierre de etapa" en el `CLAUDE.md` raíz):

   ```
   git add "clases/clase-NN-tema-breve/"
   git commit -m "Clase NN - Tema: Reel generado"
   git push
   ```

   Si el push falla, avisa a Diego con el error explícito — no reintentes con `--force`. El `.mp4` puede tardar más en subir que los demás artefactos; avisa a Diego si el push se demora.

4. Con esto la clase queda ✅ completa — no hay siguiente fase ni `/compact` pendiente.

---

## Sistema de diseño definitivo (NO modificar sin instrucción de Diego)

### Dimensiones y formato
| Parámetro | Valor |
|---|---|
| Ancho | 1080 px |
| Alto | 1920 px |
| Relación | 9:16 (portrait, Reels/Shorts) |
| FPS | 30 |
| Duración típica | ~45s |

### Paleta de colores (`src/fonts.ts → COLORS`)
| Token | Hex | Uso |
|---|---|---|
| `bg` | `#0D1117` | Fondo principal |
| `bgAccent` | `#1C2A4A` | Acento del gradiente radial |
| `surface` | `#161B22` | Bloques de código, tarjetas |
| `border` | `#30363D` | Bordes sutiles |
| `text` | `#E6EDF3` | Texto primario |
| `textMuted` | `#8B949E` | Texto secundario |
| `pyYellow` | `#FFE873` | Amarillo Python — badges, highlight, barra CTA |
| `pyBlue` | `#4B8BBE` | Azul Python — concepto `and`, elementos primarios |
| `accent` | `#58A6FF` | Azul claro — concepto `or`, énfasis |
| `success` | `#3FB950` | Verde — output correcto, código bueno |
| `error` | `#FF6B6B` | Rojo — errores, código incorrecto |

### Colores de acento sugeridos por tipo de concepto
| Tipo de concepto | Color sugerido |
|---|---|
| `and` | `#4B8BBE` (pyBlue) |
| `or` | `#58A6FF` (accent) |
| `not` | `#BC8CFF` (purple) |
| `if` / condicionales | `#FFE873` (pyYellow) |
| `for` / `while` | `#3FB950` (success) |
| Funciones | `#FF9F43` (orange) |
| Listas / datos | `#58A6FF` (accent) |

### Tipografía
| Uso | Fuente | Pesos |
|---|---|---|
| Texto general | Poppins | 400, 600, 700, 800 |
| Código Python | JetBrains Mono | 400, 500, 700 |

Cargadas en `src/fonts.ts` con `@remotion/google-fonts`.

### Timing (`src/config.ts`)
| Constante | Valor | Descripción |
|---|---|---|
| `CHARS_PER_FRAME` | 0.65 | Velocidad typewriter (~20 chars/s a 30fps) |
| `TYPING_START` | 35 | Frames de delay antes de empezar a escribir |
| `OUTPUT_REVEAL_DELAY` | 20 | Frames tras terminar el typing |
| `OUTPUT_REVEAL_FRAMES` | 20 | Frames de fade-in del output |
| `HOLD_AFTER` | 75 | 2.5s de pausa post-output → luego transición |
| `CTA_DURATION` | 190 | Total de la escena CTA |
| `CTA_BAR_FILL_FRAME` | 160 | Frame donde la barra llega al 100% |
| `TRANSITION_FRAMES` | 18 | Duración de cada transición |
| `HOOK_FRAMES` | 90 | Duración escena Hook |
| `TITLE_FRAMES` | 75 | Duración escena Título |

### Transiciones
| Transición | Tipo |
|---|---|
| Hook → Título | `slide from-right` |
| Título → Concepto 1 | `slide from-right` |
| Entre conceptos | `slide from-right` |
| Último concepto → Errores | `slide from-right` |
| Errores → CTA | `fade` |

Todas usan `springTiming({ config: { damping: 200 }, durationInFrames: 18 })`.

### Animaciones
- **Texto**: spring slide-up con `AnimatedText` (delay escalonado)
- **Código**: typewriter letra a letra con cursor `█` activo
- **Output**: fade-in tras `OUTPUT_REVEAL_DELAY` frames
- **Errores**: cada bloque hace slide-up secuencialmente (+60 frames por error)
- **Botón CTA**: escala pulsante senoidal sutil
- **Barra CTA**: relleno lineal → al completarse, el video termina 1s después
- **FadeToBlack**: overlay negro desde frame `REEL_DURATION - 45` hasta `REEL_DURATION`

---

## Assets fijos (no cambiar entre clases)

### Foto del profesor
- **Archivo**: `tools/reel-generator/public/assets/foto-profesor.png`
- **Hook**: círculo 540px centrado debajo del texto, borde `pyYellow` 3px
- **CTA**: círculo 540px centrado debajo de la barra de progreso, borde `pyYellow` 3px
- **Corner watermark**: `src/components/CornerLogo.tsx` — 84px, esquina top-right, visible toda la duración

### Música
- **Archivo**: `tools/reel-generator/public/music/after_hours.mp3`
- **Comportamiento**: arranca desde el segundo 0, fade-in 60 frames (2s), volumen base 0.13, fade-out 60 frames (2s) al final

---

## Convención de nombres de output

```
clases/clase-NN-tema-breve/Clase NN - Tema - Reel.mp4
```

Ejemplos:
- `clases/clase-08b-operadores-logicos/Clase 8b - Operadores Lógicos - Reel.mp4`
- `clases/clase-09-condicionales/Clase 9 - Condicionales if-else - Reel.mp4`
- `clases/clase-13-ciclo-for/Clase 13 - Ciclo for - Reel.mp4`

---

## Restricciones del reel

1. **Código corto**: cada snippet máximo 5 líneas para que quepa bien en pantalla sin scroll.
2. **Variables en español**: igual que en los Colabs (`puede_ver`, `logueado`, `tiene_prueba`).
3. **Output en una línea**: el resultado del print debe caber en una sola línea (sin saltos).
4. **Regla sin jerga**: la `rule` de cada ConceptScene debe ser entendible por alguien que no sabe Python.
5. **Palabra a resaltar existe en la regla**: `ruleHighlight` debe ser exactamente una subcadena de `rule`.
6. **No spoilear errores en los conceptos**: los errores típicos van solo en `ErrorScene`, no en el código de las ConceptScenes.
7. **Contextos reales**: el hook y los ejemplos de código usan contextos que los estudiantes reconocen.
