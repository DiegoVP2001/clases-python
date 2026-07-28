import React from "react";
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame } from "remotion";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { COLORS, textFont, codeFont } from "../fonts";
const LOGO_FRAMES = 75;

interface LogoSceneProps {
  isOutro?: boolean;
}

export const LogoScene: React.FC<LogoSceneProps> = ({ isOutro = false }) => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });
  const fadeOut = interpolate(frame, [LOGO_FRAMES - 20, LOGO_FRAMES], [1, 0], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });
  const opacity = isOutro ? fadeOut : fadeIn;

  return (
    <AbsoluteFill>
      <Background />
      <AbsoluteFill
        style={{
          opacity,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 28,
        }}
      >
        <div
          style={{
            width: 260,
            height: 260,
            borderRadius: "50%",
            overflow: "hidden",
            boxShadow: `0 0 0 4px ${COLORS.pyYellow}`,
            background: COLORS.surface,
          }}
        >
          <Img
            src={staticFile("assets/foto-profesor.png")}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </div>

        <AnimatedText delay={10} style={{ textAlign: "center" }}>
          <div
            style={{
              fontFamily: textFont,
              fontSize: 52,
              fontWeight: 700,
              color: COLORS.text,
            }}
          >
            Prof. Diego
          </div>
        </AnimatedText>

        <AnimatedText delay={18} style={{ textAlign: "center" }}>
          <div
            style={{
              fontFamily: textFont,
              fontSize: 34,
              color: COLORS.textMuted,
            }}
          >
            Clases de Python · 4to Medio
          </div>
        </AnimatedText>

        <AnimatedText delay={26}>
          <div
            style={{
              background: `${COLORS.pyYellow}22`,
              border: `1px solid ${COLORS.pyYellow}55`,
              borderRadius: 100,
              padding: "10px 28px",
              fontFamily: codeFont,
              fontSize: 26,
              color: COLORS.pyYellow,
            }}
          >
            🐍 Santiago, Chile
          </div>
        </AnimatedText>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
