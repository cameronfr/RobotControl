#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

#Note: configure these later
SERVOMIN = 1400  # Min pulse length out in ms
SERVOMAX = 1600  # Max pulse length out in ms
PWMFREQ = 60

#Servo Port configuration
botLeftShoulderServo = 0;
botRightShoulderServo = 1;
topLeftShoulderServo = 2;
topRightShoulderServo = 3;

#For Demo Purposes
currentBottomAngle = 90;
currentTopAngle = 90;

#takes pulse in ms and outputs to servo channel (modified from example)
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= PWMFREQ                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def init():
    pwm.setPWMFreq(PWMFREQ)                        # Set frequency to 60 Hz

def moveBottomShoulder(angle):
    pulselen = map(angle, 0, 180, SERVOMIN, SERVOMAX)
    setServoPulse(botLeftShoulderServo,pulselen)
    setServoPulse(botLeftShoulderServo,pulselen)

def moveBottomShoulder(angle):
    pulselen = map(angle, 0, 180, SERVOMIN, SERVOMAX)
    setServoPulse(botLeftShoulderServo,pulselen)
    setServoPulse(botLeftShoulderServo,pulselen)

def moveTopShoulder(angle):
    pulselen = map(angle, 0, 180, SERVOMIN, SERVOMAX)
    setServoPulse(topLeftShoulderServo,pulselen)
    setServoPulse(topLeftShoulderServo,pulselen)

init()
#for easy testing
while (True):
    direction = input("W or A or S or D").lower();
    if direction == "a":
        currentBottomAngle = max(currentBottomAngle - 1,0);
    elif direction == "d"
        currentBottomAngle = min(currentBottomAngle + 1,180);
    elif direction == "w":
        currentTopAngle = min(currentTopAngle + 1,180);
    elif direction == "s":
        currentTopAngle = max(currentTopAngle - 1,0);
    moveBottomShoulder(currentBottomAngle)
    moveTopShoulder(currentTopAngle)
