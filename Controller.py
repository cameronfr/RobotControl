import Motor
import Ultrasonic
import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    motor = Motor.Motor(23)
    sonar = Ultrasonic.Ultrasonic(24)
    motor.initialize(1600)
    while(True):
        motor.setSpeed(sonar.read()*5)
