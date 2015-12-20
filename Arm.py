from lib.Adafruit_PWM_Servo_Driver import PWM
import time

class Servo:

    pwm = PWM(0x40) #may need to move later
    SERVOMIN = 500  # min pulse length out in us
    SERVOMAX = 2500  # max pulse length out in us
    ANGLEMIN = 0
    ANGLEMAX = 180
    PWMFREQ = 60

    def __init__(self, channel):
        pwm.setPWMFreq(PWMFREQ)
        self.channel = channel

    def setServoPulse(channel, pulse):
        pulseLength = 1000000                   # 1,000,000 us per second
        pulseLength /= PWMFREQ                       # 60 Hz
        pulseLength /= 4096                     # 12 bits of resolution
        pulse /= pulseLength
        pulse = int(pulse)
        pwm.setPWM(channel, 0, pulse)

    def angleToPulse(angle):
        return ((((angle-ANGLEMIN)/(ANGLEMAX-ANGLEMIN)) * (SERVOMAX-SERVOMIN)) + SERVOMIN)

    def moveToAngle(angle, reversed = False):
        if not reversed:
            self.setServoPulse(self.channel,self.angleToPulse(angle))
        else:
            setServoPulse(self.channel,self.angleToPulse(self.reverseAngle(angle)))

    def reverseAngle(angle):
        return (ANGLEMIN + (ANGLEMAX - angle))

class Joint:

    def __init__(self, servoList, directionList):
        if len(servoList) != len(directionList):
            raise Exception('servo list length does not match direction list length')
        self.servoList = servoList
        self.directionList = directionList

    def moveToAngle(angle)
        for i in range(len(servoList)):
            direction = self.directionList[i]
            if direction == -1:
                servoList[i].moveToAngle(angle,True)
            else:
                servoList[i].moveToAngle(angle,False)
