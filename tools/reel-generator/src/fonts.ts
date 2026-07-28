import { loadFont } from "@remotion/google-fonts/Poppins";
import { loadFont as loadMono } from "@remotion/google-fonts/JetBrainsMono";

export const { fontFamily: textFont } = loadFont("normal", {
  weights: ["400", "600", "700", "800"],
  subsets: ["latin"],
});

export const { fontFamily: codeFont } = loadMono("normal", {
  weights: ["400", "500", "700"],
  subsets: ["latin"],
});

export const COLORS = {
  bg: "#0D1117",
  bgAccent: "#1c2a4a",
  surface: "#161B22",
  border: "#30363D",
  text: "#E6EDF3",
  textMuted: "#8B949E",
  pyYellow: "#FFE873",
  pyBlue: "#4B8BBE",
  success: "#3FB950",
  error: "#FF6B6B",
  accent: "#58A6FF",
} as const;
