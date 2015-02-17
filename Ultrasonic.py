import time
import RPi.GPIO as GPIO


class Ultrasonic:

    TIMEOUT = 0.020

    def __init__ (self, pin):
        #GPIO.setmode(GPIO.BCM)
        self.setPin(pin);

    def setPin(self, pin):
        self.pinNumber = pin

    def read(self):
        GPIO.setup(self.pinNumber, GPIO.OUT)
        GPIO.output(self.pinNumber, 0)

        time.sleep(0.000002)
        GPIO.output(pinNumber, 1)
        time.sleep(0.000005)

        GPIO.output(self.pinNumber, 0)
        GPIO.setup(self.pinNumber, GPIO.IN)

        goodread=True
        watchtime=time.time()
        while GPIO.input(self.pinNumber)==0 and goodread:
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while GPIO.input(self.pinNumber)==1 and goodread:
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False

        if goodread:
                duration=endtime-starttime
                distance=duration*34000/2
                return distance
