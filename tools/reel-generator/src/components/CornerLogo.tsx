import React from "react";
import { Img, interpolate, staticFile, useCurrentFrame } from "remotion";
import { COLORS } from "../fonts";

export const CornerLogo: React.FC = () => {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 30], [0, 0.88], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        top: 56,
        right: 56,
        opacity,
        zIndex: 10,
      }}
    >
      <div
        style={{
          width: 84,
          height: 84,
          borderRadius: "50%",
          overflow: "hidden",
          boxShadow: `0 0 0 2px ${COLORS.pyYellow}88, 0 4px 16px #00000066`,
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
};
