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
        if direction == "a":
            currentHorizAngle = max(currentHorizAngle - 10,0);
        elif direction == "d":
            currentHorizAngle = min(currentHorizAngle + 10,180);
        if direction == "w":
            currentVertAngle = min(currentVertAngle + 10,180);
        elif direction == "s":
            currentVertAngle = max(currentVertAngle - 10,0);
	if direction == "q":
	    currentElbowAngle = min(currentElbowAngle + 10, 180)
	elif direction == "e":
	    currentElbowAngle = max(currentElbowAngle - 10, 0)
	if direction == "g":
	    currentClawAngle = min(currentClawAngle + 10, 180)
	elif direction == "r":
	    currentClawAngle = max(currentClawAngle - 10, 0)  

        horizJoint.moveToAngle(currentHorizAngle)
        vertJoint.moveToAngle(currentVertAngle)
	elbowJoint.moveToAngle(currentElbowAngle)
	clawJoint.moveToAngle(currentClawAngle)

if __name__ == "__main__":
    main()
