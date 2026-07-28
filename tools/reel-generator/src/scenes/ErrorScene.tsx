import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import SyntaxHighlighter from "react-syntax-highlighter";
import { atomOneDark } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { COLORS, textFont, codeFont } from "../fonts";

export interface ErrorExample {
  title: string;
  bad: string;
  good: string;
}

interface ErrorSceneProps {
  errors: ErrorExample[];
}

const CodeSnippet: React.FC<{ code: string; variant: "bad" | "good" }> = ({ code, variant }) => {
  const borderColor = variant === "bad" ? COLORS.error : COLORS.success;
  return (
    <div
      style={{
        background: `${borderColor}15`,
        border: `1px solid ${borderColor}44`,
        borderRadius: 12,
        overflow: "hidden",
      }}
    >
      <SyntaxHighlighter
        language="python"
        style={atomOneDark}
        customStyle={{
          background: "transparent",
          padding: "12px 20px",
          margin: 0,
          fontSize: 31,
          lineHeight: 1.55,
          fontFamily: codeFont,
        }}
        codeTagProps={{ style: { fontFamily: codeFont } }}
      >
        {code}
      </SyntaxHighlighter>
    </div>
  );
};

export const ErrorScene: React.FC<ErrorSceneProps> = ({ errors }) => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill>
      <Background variant="error" />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          padding: "80px 64px",
          gap: 24,
        }}
      >
        <AnimatedText delay={3}>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <span style={{ fontSize: 48 }}>⚠️</span>
            <div
              style={{
                fontFamily: textFont,
                fontSize: 52,
                fontWeight: 800,
                color: COLORS.error,
              }}
            >
              Errores típicos
            </div>
          </div>
        </AnimatedText>

        {errors.map((error, i) => {
          const revealFrame = 20 + i * 60;
          const opacity = interpolate(frame, [revealFrame, revealFrame + 20], [0, 1], {
            extrapolateRight: "clamp",
            extrapolateLeft: "clamp",
          });
          const translateY = interpolate(frame, [revealFrame, revealFrame + 20], [28, 0], {
            extrapolateRight: "clamp",
            extrapolateLeft: "clamp",
          });

          return (
            <React.Fragment key={i}>
              {i > 0 && (
                <div
                  style={{
                    opacity,
                    height: 1,
                    background: COLORS.border,
                    marginTop: 4,
                    marginBottom: 4,
                  }}
                />
              )}
              <div
                style={{
                  opacity,
                  transform: `translateY(${translateY}px)`,
                  display: "flex",
                  flexDirection: "column",
                  gap: 10,
                }}
              >
                <div
                  style={{
                    fontFamily: textFont,
                    fontSize: 30,
                    fontWeight: 700,
                    color: COLORS.error,
                  }}
                >
                  ❌ {error.title}
                </div>

                <CodeSnippet code={error.bad} variant="bad" />

                <div
                  style={{
                    fontFamily: textFont,
                    fontSize: 26,
                    fontWeight: 700,
                    color: COLORS.success,
                    paddingLeft: 4,
                  }}
                >
                  ✓ En cambio:
                </div>

                <CodeSnippet code={error.good} variant="good" />
              </div>
            </React.Fragment>
          );
        })}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
