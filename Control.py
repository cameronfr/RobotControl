#!/usr/bin/python

import Arm
import time

def main():
    horizJoint = Joint([0,1],[1,-1])
    vertJoint = Joint([2,3],[1,-1])
    elbowJoint = Joint([4],[1])
    clawJoint = Joint([5,6],[1,-1])

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
