import RPIO.PWM as PWM
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
