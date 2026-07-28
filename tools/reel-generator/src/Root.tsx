import "./index.css";
import React from "react";
import { Composition } from "remotion";
import { ClassReel, REEL_DURATION } from "./Composition";

export const RemotionRoot: React.FC = () => (
  <Composition
    id="ClassReel"
    component={ClassReel}
    durationInFrames={REEL_DURATION}
    fps={30}
    width={1080}
    height={1920}
  />
);
