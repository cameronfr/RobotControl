import time
import RPi.GPIO as GPIO


class Ultrasonic:

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
