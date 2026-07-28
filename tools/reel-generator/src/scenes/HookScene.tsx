import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { COLORS, textFont } from "../fonts";

const AuthorBadge: React.FC = () => (
  <div style={{ display: "flex", justifyContent: "center" }}>
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
);

export const HookScene: React.FC = () => (
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
            lineHeight: 1.25,
            letterSpacing: -1,
          }}
        >
          ¿Sabías que apps como Google, para mostrarte los resultados partido por partido del Mundial,{" "}
          <span style={{ color: COLORS.pyYellow }}>repiten un solo bloque de código</span> en vez de escribirlo 7 veces seguidas?
        </div>
      </AnimatedText>

      <AnimatedText delay={20} style={{ textAlign: "center" }}>
        <div
          style={{
            fontFamily: textFont,
            fontSize: 38,
            fontWeight: 600,
            color: COLORS.textMuted,
          }}
        >
          Hoy lo aprendes tú. 🐍
        </div>
      </AnimatedText>

      <AnimatedText delay={35}>
        <AuthorBadge />
      </AnimatedText>
    </AbsoluteFill>
  </AbsoluteFill>
);
