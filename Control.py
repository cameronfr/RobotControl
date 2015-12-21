#!/usr/bin/python

import Arm
import time

def main():
    horizJoint = Arm.Joint([Arm.Servo(0),Arm.Servo(1)],[1,-1])
    vertJoint = Arm.Joint([Arm.Servo(2),Arm.Servo(3)],[1,-1])
    elbowJoint = Arm.Joint([Arm.Servo(4)],[1])
    clawJoint = Arm.Joint([Arm.Servo(5),Arm.Servo(6)],[1,-1])

    currentHorizAngle = 90;
    currentVertAngle = 90;

    #for easy testing
    while (True):
        direction = raw_input("W or A or S or D").lower();
        if direction == "a":
            currentHorizAngle = max(currentHorizAngle - 30,0);
        elif direction == "d":
            currentHorizAngle = min(currentHorizAngle + 30,180);
        elif direction == "w":
            currentVertAngle = min(currentVertAngle + 30,180);
        elif direction == "s":
            currentVertAngle = max(currentVertAngle - 30,0);

        horizJoint.moveToAngle(currentHorizAngle)
        vertJoint.moveToAngle(currentVertAngle)

if __name__ == "__main__":
    main()
