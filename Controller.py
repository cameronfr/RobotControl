import Motor
import Ultrasonic

if __name__ == '__main__':
    motor = Motor.Motor(23)
    sonar = Ultrasonic.Ultrasonic(24)
    motor.initialize(1600)
    while(True):
        motor.setSpeed(sonar.read*5)
