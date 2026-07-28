import React from "react";
import { AbsoluteFill } from "remotion";
import { COLORS } from "../fonts";

interface BackgroundProps {
  variant?: "default" | "error" | "success";
}

export const Background: React.FC<BackgroundProps> = ({ variant = "default" }) => {
  const accentMap = {
    default: COLORS.bgAccent,
    error: "#3a1a1a",
    success: "#0f2a1a",
  };

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 20% 20%, ${accentMap[variant]} 0%, ${COLORS.bg} 65%)`,
      }}
    />
  );
};
