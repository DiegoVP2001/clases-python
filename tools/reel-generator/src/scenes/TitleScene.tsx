import React from "react";
import { AbsoluteFill } from "remotion";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { COLORS, textFont, codeFont } from "../fonts";

const OPERATORS = [
  { label: "for", color: COLORS.success },
  { label: "range()", color: "#FF9F43" },
  { label: "acumulador", color: COLORS.accent },
];

export const TitleScene: React.FC = () => (
  <AbsoluteFill>
    <Background />

    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "0 72px",
        gap: 48,
      }}
    >
      <AnimatedText delay={3} style={{ textAlign: "center" }}>
        <div
          style={{
            fontFamily: textFont,
            fontSize: 36,
            fontWeight: 600,
            color: COLORS.textMuted,
            letterSpacing: 4,
            textTransform: "uppercase",
          }}
        >
          Clase 16 · Python
        </div>
      </AnimatedText>

      <AnimatedText delay={12} style={{ textAlign: "center" }}>
        <div
          style={{
            fontFamily: textFont,
            fontSize: 88,
            fontWeight: 800,
            color: COLORS.text,
            lineHeight: 1.05,
            letterSpacing: -2,
          }}
        >
          for + range()
          <br />
          <span style={{ color: COLORS.pyYellow }}>repetir con orden</span>
        </div>
      </AnimatedText>

      <div style={{ display: "flex", gap: 24 }}>
        {OPERATORS.map((op, i) => (
          <AnimatedText key={op.label} delay={18 + i * 5}>
            <div
              style={{
                background: `${op.color}22`,
                border: `2px solid ${op.color}88`,
                borderRadius: 16,
                padding: "16px 36px",
                fontFamily: codeFont,
                fontSize: 44,
                fontWeight: 700,
                color: op.color,
              }}
            >
              {op.label}
            </div>
          </AnimatedText>
        ))}
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);
