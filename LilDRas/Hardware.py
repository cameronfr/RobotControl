import RPIO.PWM as PWM
import RPi.GPIO as GPIO
import time

class Motor:

    def __init__ (self,pin):
        self.setPin(pin);
        self.servo = PWM.Servo()

    def setPin(self, pin):
        self.pinNumber = pin

    def initialize(self,freq):
        self.freq = freq
        self.servo.set_servo(self.pinNumber,freq)
        time.sleep(0.10)

    def setSpeed(self, speed):
        self.servo.set_servo(self.pinNumber,self.freq+round(speed,-1))

class Sonar:

    TIMEOUT = 0.020

    def __init__ (self, pin):
        self.setPin(pin)

    def setPin(self, pin):
        self.pinNumber = pin

    def read(self):

        GPIO.setup(self.pinNumber, GPIO.OUT)
        GPIO.output(self.pinNumber, 0)
        time.sleep(0.000002)

        GPIO.output(self.pinNumber, 1)
        time.sleep(0.000005)
        GPIO.output(self.pinNumber, 0)

        GPIO.setup(self.pinNumber, GPIO.IN)

        while GPIO.input(self.pinNumber)==0:
            starttime=time.time()

        while GPIO.input(self.pinNumber)==1:
            endtime=time.time()

        duration=endtime-starttime
        distance=duration*34000/2
        return distance
