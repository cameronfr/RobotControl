#!/usr/bin/python

import Arm
import time

def main():
    horizJoint = Arm.Joint([Arm.Servo(0),Arm.Servo(1)],[1,-1])
    vertJoint = Arm.Joint([Arm.Servo(2),Arm.Servo(3)],[1,-1])
    elbowJoint = Arm.Joint([Arm.Servo(4)],[1])
    clawJoint = Arm.Joint([Arm.Servo(5),Arm.Servo(6)],[1,-1])

    currentHorizAngle = 90
    currentVertAngle = 90
    currentElbowAngle = 90
    currentClawAngle = 90

    #for easy testing
    while (True):
        direction = raw_input("W, A, S, D, Q, E, G, R: ").lower();
        if "a" in direction:
            currentHorizAngle = max(currentHorizAngle - 10,0);
        elif "d" in direction:
            currentHorizAngle = min(currentHorizAngle + 10,180);
        if "w" in direction:
            currentVertAngle = min(currentVertAngle + 10,180);
        elif "s" in direction:
            currentVertAngle = max(currentVertAngle - 10,0);
	if "q" in direction:
	    currentElbowAngle = min(currentElbowAngle + 10, 180)
	elif "e" in direction:
	    currentElbowAngle = max(currentElbowAngle - 10, 0)
	if "g" in direction:
	    currentClawAngle = min(currentClawAngle + 10, 180)
	elif "r" in direction:
	    currentClawAngle = max(currentClawAngle - 10, 0)  

        horizJoint.moveToAngle(currentHorizAngle)
        vertJoint.moveToAngle(currentVertAngle)
	elbowJoint.moveToAngle(currentElbowAngle)
	clawJoint.moveToAngle(currentClawAngle)

if __name__ == "__main__":
    main()
