"use client"
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import SmallText from "../components/SmallText"
import XLargeText from "../components/XLargeText"

const renderTime = ({ remainingTime }) => {
    if (remainingTime === 0) {
      return <SmallText  value={"Great Job"}></SmallText>
    }
    return (
        <XLargeText>{remainingTime}</XLargeText>
    );
  };


export default function Timer({time=4}){
    return (
            <CountdownCircleTimer
              isPlaying
              duration={time}
              trailColor="#121212"
              colors={["#FFFFFF"]}
              colorsTime={[0]}
              onComplete={() => ({ shouldRepeat: false, delay: 1 })}
            >
              {renderTime}
            </CountdownCircleTimer>
      );
}