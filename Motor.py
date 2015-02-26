import RPIO.PWM as PWM

class Motor:


    def __init__ (self,pin):
        self.setPin(pin);
        self.servo = PWM.Servo()

    def setPin(self, pin):
        self.pinNumber = pin

    def initMotor(self,freq):
        self.freq = freq
        self.servo.set_servo(self.pinNumber,freq)

    def setMotor(self, speed)
        self.servo.set_servo(self.punNimber,freq+speed)
