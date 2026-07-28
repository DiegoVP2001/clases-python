import React from "react";
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame } from "remotion";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { COLORS, textFont } from "../fonts";
import { CTA_BAR_FILL_FRAME } from "../config";

export const CTAScene: React.FC = () => {
  const frame = useCurrentFrame();

  const pulseScale = 1 + 0.035 * Math.sin((frame / 30) * Math.PI * 2);

  const barProgress = interpolate(frame, [30, CTA_BAR_FILL_FRAME], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  const photoOpacity = interpolate(frame, [50, 70], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  return (
    <AbsoluteFill>
      <Background />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "0 72px",
          gap: 36,
        }}
      >
        <AnimatedText delay={5} style={{ textAlign: "center" }}>
          <div
            style={{
              fontFamily: textFont,
              fontSize: 52,
              fontWeight: 800,
              color: COLORS.text,
              lineHeight: 1.2,
            }}
          >
            ¡Ahora{" "}
            <span style={{ color: COLORS.pyYellow }}>te toca</span> a ti!
          </div>
        </AnimatedText>

        <AnimatedText delay={18} style={{ textAlign: "center" }}>
          <div
            style={{
              fontFamily: textFont,
              fontSize: 40,
              fontWeight: 600,
              color: COLORS.textMuted,
            }}
          >
            Practica for + range() en el Colab de hoy
          </div>
        </AnimatedText>

        <AnimatedText delay={30}>
          <div
            style={{
              transform: `scale(${pulseScale})`,
              background: `linear-gradient(135deg, ${COLORS.pyYellow}, ${COLORS.pyBlue})`,
              borderRadius: 24,
              padding: "28px 56px",
              fontFamily: textFont,
              fontSize: 44,
              fontWeight: 800,
              color: "#0D1117",
              letterSpacing: -0.5,
              display: "flex",
              alignItems: "center",
              gap: 16,
            }}
          >
            <span style={{ fontSize: 48 }}>⚡</span>
            Abrir Google Colab
          </div>
        </AnimatedText>

        {/* Progress bar */}
        <div
          style={{
            width: "80%",
            height: 6,
            background: COLORS.surface,
            borderRadius: 3,
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${barProgress * 100}%`,
              height: "100%",
              background: `linear-gradient(90deg, ${COLORS.pyBlue}, ${COLORS.pyYellow})`,
              borderRadius: 3,
            }}
          />
        </div>

        {/* Author photo */}
        <div style={{ opacity: photoOpacity }}>
          <div
            style={{
              width: 540,
              height: 540,
              borderRadius: "50%",
              overflow: "hidden",
              boxShadow: `0 0 0 3px ${COLORS.pyYellow}99`,
              background: COLORS.surface,
            }}
          >
            <Img
              src={staticFile("assets/foto-profesor.png")}
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
