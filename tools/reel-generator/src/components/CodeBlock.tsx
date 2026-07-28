import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import SyntaxHighlighter from "react-syntax-highlighter";
import { atomOneDark } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { COLORS, codeFont } from "../fonts";

interface CodeBlockProps {
  code: string;
  startFrame?: number;
  typeDurationFrames?: number;
  output?: string;
  outputStartDelay?: number;
}

export const CodeBlock: React.FC<CodeBlockProps> = ({
  code,
  startFrame = 0,
  typeDurationFrames = 120,
  output,
  outputStartDelay = 20,
}) => {
  const frame = useCurrentFrame();

  const charsToShow = Math.floor(
    interpolate(frame, [startFrame, startFrame + typeDurationFrames], [0, code.length], {
      extrapolateRight: "clamp",
      extrapolateLeft: "clamp",
    })
  );

  const doneTyping = charsToShow >= code.length;
  const visibleCode = code.slice(0, charsToShow) + (doneTyping ? "" : "█");

  const outputFrame = startFrame + typeDurationFrames + outputStartDelay;
  const outputOpacity = interpolate(frame, [outputFrame, outputFrame + 20], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  const blockOpacity = interpolate(frame, [startFrame - 15, startFrame], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  return (
    <div style={{ opacity: blockOpacity }}>
      <div
        style={{
          background: COLORS.surface,
          borderRadius: 20,
          border: `1px solid ${COLORS.border}`,
          overflow: "hidden",
        }}
      >
        <div
          style={{
            display: "flex",
            gap: 8,
            padding: "16px 20px 12px",
            borderBottom: `1px solid ${COLORS.border}`,
          }}
        >
          {["#FF5F57", "#FEBC2E", "#28C840"].map((color) => (
            <div
              key={color}
              style={{ width: 14, height: 14, borderRadius: 7, background: color }}
            />
          ))}
        </div>
        <div style={{ padding: "8px 4px" }}>
          <SyntaxHighlighter
            language="python"
            style={atomOneDark}
            customStyle={{
              background: "transparent",
              padding: "12px 20px",
              margin: 0,
              fontSize: 36,
              lineHeight: 1.65,
              fontFamily: codeFont,
            }}
            codeTagProps={{ style: { fontFamily: codeFont } }}
          >
            {visibleCode}
          </SyntaxHighlighter>
        </div>
      </div>

      {output && (
        <div
          style={{
            opacity: outputOpacity,
            marginTop: 16,
            background: "#0a0f14",
            borderRadius: 14,
            border: `1px solid ${COLORS.success}44`,
            padding: "14px 24px",
            fontFamily: codeFont,
            fontSize: 34,
            color: COLORS.success,
          }}
        >
          <span style={{ color: COLORS.textMuted, marginRight: 12 }}>▶</span>
          {output}
        </div>
      )}
    </div>
  );
};
