from lib.Adafruit_PWM_Servo_Driver import PWM
import time

class Servo:

    pwm = PWM(0x40) #may need to move later
    SERVOMIN = 500  # min pulse length out in us
    SERVOMAX = 2500  # max pulse length out in us
    ANGLEMIN = 0.0
    ANGLEMAX = 180.0
    PWMFREQ = 60

    def __init__(self, channel):
        Servo.pwm.setPWMFreq(Servo.PWMFREQ)
        self.channel = channel

    def setServoPulse(self, pulse):
	print("call: pwm: channel:" + str(self.channel) + " pulse:" + str(pulse))	
        pulseLength = 1000000                   # 1,000,000 us per second
        pulseLength /= Servo.PWMFREQ                       # 60 Hz
        pulseLength /= 4096                     # 12 bits of resolution
        pulse /= pulseLength
        pulse = int(pulse)
        Servo.pwm.setPWM(self.channel, 0, pulse)

    def angleToPulse(self, angle):
        return ((((float(angle)-Servo.ANGLEMIN)/(Servo.ANGLEMAX-Servo.ANGLEMIN)) * (Servo.SERVOMAX-Servo.SERVOMIN)) + Servo.SERVOMIN)

    def moveToAngle(self, angle, reversed = False):
        if not reversed:
            self.setServoPulse(self.angleToPulse(angle))
	    print("call: move: channel:" + str(self.channel) + " angle:" + str(angle)) 
        else:
            self.setServoPulse(self.angleToPulse(self.reverseAngle(angle)))
	    print("call: move: channel:" + str(self.channel) + " angle:" + str(self.reverseAngle(angle)))
  
    def reverseAngle(self, angle):
        return (Servo.ANGLEMIN + (Servo.ANGLEMAX - angle))

class Joint:

    def __init__(self, servoList, directionList):
        if len(servoList) != len(directionList):
            raise Exception('servo list length does not match direction list length')
        self.servoList = servoList
        self.directionList = directionList

    def moveToAngle(self, angle):
        for i in range(len(self.servoList)):
            direction = self.directionList[i]
            if direction == -1:
                self.servoList[i].moveToAngle(angle,True)
            else:
                self.servoList[i].moveToAngle(angle,False)
