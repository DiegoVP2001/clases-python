import React from "react";
import { AbsoluteFill } from "remotion";
import { Background } from "../components/Background";
import { AnimatedText } from "../components/AnimatedText";
import { CodeBlock } from "../components/CodeBlock";
import { COLORS, textFont, codeFont } from "../fonts";
import {
  CHARS_PER_FRAME,
  TYPING_START,
  OUTPUT_REVEAL_DELAY,
} from "../config";

interface ConceptSceneProps {
  operator: string;
  emoji: string;
  accentColor: string;
  rule: string;
  ruleHighlight: string;
  code: string;
  output: string;
}

export const ConceptScene: React.FC<ConceptSceneProps> = ({
  operator,
  emoji,
  accentColor,
  rule,
  ruleHighlight,
  code,
  output,
}) => {
  const typeDuration = Math.ceil(code.length / CHARS_PER_FRAME);
  const ruleParts = rule.split(ruleHighlight);

  return (
    <AbsoluteFill>
      <Background />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          padding: "80px 64px",
          gap: 36,
        }}
      >
        <AnimatedText delay={3}>
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                background: `${accentColor}22`,
                border: `2px solid ${accentColor}88`,
                borderRadius: 20,
                padding: "14px 36px",
                fontFamily: codeFont,
                fontSize: 64,
                fontWeight: 700,
                color: accentColor,
              }}
            >
              {operator}
            </div>
            <div style={{ fontSize: 64 }}>{emoji}</div>
          </div>
        </AnimatedText>

        <AnimatedText delay={15}>
          <div
            style={{
              fontFamily: textFont,
              fontSize: 42,
              fontWeight: 600,
              color: COLORS.text,
              lineHeight: 1.35,
              borderLeft: `4px solid ${accentColor}`,
              paddingLeft: 24,
            }}
          >
            {ruleParts[0]}
            <span
              style={{
                color: accentColor,
                background: `${accentColor}22`,
                borderRadius: 8,
                padding: "2px 10px",
              }}
            >
              {ruleHighlight}
            </span>
            {ruleParts[1]}
          </div>
        </AnimatedText>

        <AnimatedText delay={26}>
          <CodeBlock
            code={code}
            startFrame={TYPING_START}
            typeDurationFrames={typeDuration}
            output={output}
            outputStartDelay={OUTPUT_REVEAL_DELAY}
          />
        </AnimatedText>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
