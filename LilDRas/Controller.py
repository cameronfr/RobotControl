import Motor
import Ultrasonic
import RPi.GPIO as GPIO


class Controller:

    LEFT_MOTOR_PORT = 7
    RIGHT_MOTOR_PORT = 15
    START_FREQ = 1600

    def __init__ (self):
        GPIO.setmode(GPIO.BCM)
        self.leftMotor = Motor.Motor(self.LEFT_MOTOR_PORT)
        self.rightMotor = Motor.Motor(self.RIGHT_MOTOR_PORT)
        self.leftMotor.initialize(self.START_FREQ)
        self.rightMotor.initialize(self.START_FREQ)
