// Timing constants shared between Composition (duration calculation) and scene components (internal animation).
// Both must use the same formula — never duplicate these numbers.

export const CHARS_PER_FRAME = 0.65; // ~20 chars/sec at 30fps

export const TYPING_START = 35; // frames before code starts typing
export const OUTPUT_REVEAL_DELAY = 20; // frames after typing finishes before output appears
export const OUTPUT_REVEAL_FRAMES = 20; // frames for output fade-in
export const HOLD_AFTER = 75; // 2.5s hold after output is fully visible → then transition

export function conceptDuration(code: string): number {
  const typeDuration = Math.ceil(code.length / CHARS_PER_FRAME);
  return TYPING_START + typeDuration + OUTPUT_REVEAL_DELAY + OUTPUT_REVEAL_FRAMES + HOLD_AFTER;
}

// 160 frames for header + first error; each additional error adds 60 frames; 120 frames hold at end
export function errorDuration(count: number): number {
  return 160 + (count - 1) * 60;
}

export const CTA_DURATION = 190;
export const CTA_BAR_FILL_FRAME = 160; // bar fills here; video ends 1s (30f) later at CTA_DURATION

export const TRANSITION_FRAMES = 18;

// Scene durations used by both Composition (sequence lengths) and timing calculations
export const HOOK_FRAMES = 90;
export const TITLE_FRAMES = 75;

// Global frame where Title→And transition begins (no LogoScene)
export const BEAT_DROP_FRAME =
  HOOK_FRAMES + TITLE_FRAMES - 2 * TRANSITION_FRAMES; // = 129

// Audio file offset so that the beat (at second 10 of the file) lands exactly at BEAT_DROP_FRAME.
// At global frame 0, audio plays from AUDIO_START_FROM. After BEAT_DROP_FRAME frames, it reaches frame 300 (10s).
export const AUDIO_START_FROM = 10 * 30 - BEAT_DROP_FRAME; // = 171 (second 5.7 of file)
