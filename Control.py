#!/usr/bin/python

from lib.Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

#Note: configure these later
SERVOMIN = 500  # Min pulse length out in us
SERVOMAX = 2500  # Max pulse length out in us
PWMFREQ = 60

#Servo Port configuration
topHorizShoulderServo = 0;
botHorizShoulderServo = 1;
topVertShoulderServo = 2;
botVertShoulderServo = 3;

#For Demo Purposes
currentHorizAngle = 90;
currentVertAngle = 90;

#takes pulse in ms and outputs to servo channel (modified from example)
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= PWMFREQ                       # 60 Hz
  #print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  #print "%d us per bit" % pulseLength 				
  pulse /= pulseLength
  pulse = int(pulse)
  pwm.setPWM(channel, 0, pulse)

def init():
	pwm.setPWMFreq(PWMFREQ)                        # Set frequency to 60 Hz

def angleToPulse(angle):
	return (((angle/180.0) * (SERVOMAX-SERVOMIN)) + SERVOMIN)

def moveHorizShoulder(angle):
	setServoPulse(topHorizShoulderServo,angleToPulse(angle))
	setServoPulse(botHorizShoulderServo,angleToPulse(180-angle))

def moveVertShoulder(angle):
	setServoPulse(topVertShoulderServo,angleToPulse(angle))
	setServoPulse(botVertShoulderServo,angleToPulse(180-angle))

init()
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

    moveHorizShoulder(currentHorizAngle)
    moveVertShoulder(currentVertAngle)
