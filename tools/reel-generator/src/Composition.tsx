import React from "react";
import { AbsoluteFill, Audio, interpolate, staticFile, useCurrentFrame } from "remotion";
import { TransitionSeries, springTiming } from "@remotion/transitions";
import { slide } from "@remotion/transitions/slide";
import { fade } from "@remotion/transitions/fade";
import { COLORS } from "./fonts";
import { HookScene } from "./scenes/HookScene";
import { TitleScene } from "./scenes/TitleScene";
import { ConceptScene } from "./scenes/ConceptScene";
import { ErrorScene, ErrorExample } from "./scenes/ErrorScene";
import { CTAScene } from "./scenes/CTAScene";
import { CornerLogo } from "./components/CornerLogo";
import {
  conceptDuration,
  errorDuration,
  CTA_DURATION,
  TRANSITION_FRAMES,
  HOOK_FRAMES,
  TITLE_FRAMES,
} from "./config";

// ─── Content ──────────────────────────────────────────────────────────────────

const CONCEPTO_1_CODE = `for numero_partido in range(1, 8, 1):
    ultimo_partido = numero_partido

print("Partido revisado:", ultimo_partido)`;

const CONCEPTO_2_CODE = `for numero in range(1, 8, 1):
    ultimo_valor = numero

print("Último valor generado:", ultimo_valor)`;

const CONCEPTO_3_CODE = `goles_totales = 0

for numero_partido in range(1, 5):
    goles_totales = goles_totales + 2

print("Goles totales:", goles_totales)`;

const ERRORS: ErrorExample[] = [
  {
    title: "El fin de range() no se incluye",
    bad: `for numero_partido in range(1, 8):
    print(numero_partido)
# Esperaban ver el 8, pero nunca aparece`,
    good: `for numero_partido in range(1, 9):
    print(numero_partido)  # ahora sí llega al 8`,
  },
  {
    title: "Olvidar la indentación bajo el for",
    bad: `for numero_partido in range(1, 8):
print("Partido", numero_partido)`,
    good: `for numero_partido in range(1, 8):
    print("Partido", numero_partido)`,
  },
  {
    title: "Acumulador inicializado dentro del bucle",
    bad: `for numero_partido in range(1, 4):
    goles_totales = 0
    goles_totales = goles_totales + 2`,
    good: `goles_totales = 0
for numero_partido in range(1, 4):
    goles_totales = goles_totales + 2`,
  },
];

const ERRORS_TO_SHOW = 3; // workflow param: 1, 2 o 3

// ─── Duration ─────────────────────────────────────────────────────────────────

// Hook→Título + Título→C1 + C1→C2 + C2→C3 + C3→Errores + Errores→CTA
const NUM_TRANSITIONS = 6;

export const REEL_DURATION =
  HOOK_FRAMES +
  TITLE_FRAMES +
  conceptDuration(CONCEPTO_1_CODE) +
  conceptDuration(CONCEPTO_2_CODE) +
  conceptDuration(CONCEPTO_3_CODE) +
  errorDuration(ERRORS_TO_SHOW) +
  CTA_DURATION -
  NUM_TRANSITIONS * TRANSITION_FRAMES;

// ─── Sub-components ───────────────────────────────────────────────────────────

const BASE_VOLUME = 0.13;
const FADE_IN_FRAMES = 60; // 2s fade-in from silence
const FADE_OUT_FRAMES = 60; // 2s fade-out to silence at end

// Volume callback receives the global composition frame
const musicVolume = (f: number): number => {
  if (f < FADE_IN_FRAMES) {
    return interpolate(f, [0, FADE_IN_FRAMES], [0, BASE_VOLUME]);
  }
  if (f > REEL_DURATION - FADE_OUT_FRAMES) {
    return interpolate(
      f,
      [REEL_DURATION - FADE_OUT_FRAMES, REEL_DURATION],
      [BASE_VOLUME, 0]
    );
  }
  return BASE_VOLUME;
};

const FadeToBlack: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [REEL_DURATION - 45, REEL_DURATION],
    [0, 1],
    { extrapolateRight: "clamp", extrapolateLeft: "clamp" }
  );
  return <AbsoluteFill style={{ background: "black", opacity }} />;
};

// ─── Transitions ──────────────────────────────────────────────────────────────

const slideRight = {
  presentation: slide({ direction: "from-right" }),
  timing: springTiming({ config: { damping: 200 }, durationInFrames: TRANSITION_FRAMES }),
};

const fadeTrans = {
  presentation: fade(),
  timing: springTiming({ config: { damping: 200 }, durationInFrames: TRANSITION_FRAMES }),
};

// ─── Composition ──────────────────────────────────────────────────────────────

export const ClassReel: React.FC = () => (
  <AbsoluteFill>
    {/* Music: plays from the beginning, fade-in / fade-out only */}
    <Audio
      src={staticFile("music/after_hours.mp3")}
      volume={musicVolume}
    />

    {/* Video scenes */}
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={HOOK_FRAMES}>
        <HookScene />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...slideRight} />

      <TransitionSeries.Sequence durationInFrames={TITLE_FRAMES}>
        <TitleScene />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...slideRight} />

      <TransitionSeries.Sequence durationInFrames={conceptDuration(CONCEPTO_1_CODE)}>
        <ConceptScene
          operator="for"
          emoji="🔁"
          accentColor={COLORS.success}
          rule="El for repite un bloque de código una vez por cada valor de la secuencia que recorre"
          ruleHighlight="una vez por cada valor"
          code={CONCEPTO_1_CODE}
          output="Partido revisado: 7"
        />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...slideRight} />

      <TransitionSeries.Sequence durationInFrames={conceptDuration(CONCEPTO_2_CODE)}>
        <ConceptScene
          operator="range(inicio, fin, salto)"
          emoji="🔢"
          accentColor="#FF9F43"
          rule="range(inicio, fin, salto) genera números desde inicio hasta fin, sin incluir fin"
          ruleHighlight="sin incluir fin"
          code={CONCEPTO_2_CODE}
          output="Último valor generado: 7"
        />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...slideRight} />

      <TransitionSeries.Sequence durationInFrames={conceptDuration(CONCEPTO_3_CODE)}>
        <ConceptScene
          operator="acumulador"
          emoji="➕"
          accentColor={COLORS.accent}
          rule="El acumulador se inicializa en 0 antes del for, y en cada vuelta va sumando"
          ruleHighlight="antes del for"
          code={CONCEPTO_3_CODE}
          output="Goles totales: 8"
        />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...slideRight} />

      <TransitionSeries.Sequence durationInFrames={errorDuration(ERRORS_TO_SHOW)}>
        <ErrorScene errors={ERRORS.slice(0, ERRORS_TO_SHOW)} />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition {...fadeTrans} />

      <TransitionSeries.Sequence durationInFrames={CTA_DURATION}>
        <CTAScene />
      </TransitionSeries.Sequence>
    </TransitionSeries>

    {/* Corner watermark on top of all scenes */}
    <CornerLogo />

    {/* Fade to black — last layer, covers everything including watermark */}
    <FadeToBlack />
  </AbsoluteFill>
);
