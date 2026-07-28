import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

interface AnimatedTextProps {
  children: React.ReactNode;
  delay?: number;
  style?: React.CSSProperties;
  direction?: "up" | "down" | "left" | "right";
  damping?: number;
  stiffness?: number;
}

export const AnimatedText: React.FC<AnimatedTextProps> = ({
  children,
  delay = 0,
  style,
  direction = "up",
  damping = 18,
  stiffness = 130,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const progress = spring({
    frame: frame - delay,
    fps,
    config: { damping, stiffness },
    from: 0,
    to: 1,
  });

  const offset = 60;
  const translateX =
    direction === "left" ? interpolate(progress, [0, 1], [offset, 0])
    : direction === "right" ? interpolate(progress, [0, 1], [-offset, 0])
    : 0;
  const translateY =
    direction === "up" ? interpolate(progress, [0, 1], [offset, 0])
    : direction === "down" ? interpolate(progress, [0, 1], [-offset, 0])
    : 0;

  const opacity = interpolate(progress, [0, 0.25], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        transform: `translate(${translateX}px, ${translateY}px)`,
        opacity,
        ...style,
      }}
    >
      {children}
    </div>
  );
};
