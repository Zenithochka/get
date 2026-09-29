import RPi.GPIO as GPIO
import time
import math                              

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 100)
duty = 0.0
k = 1.0
t = 0.0
dt = 0.01
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(dt)
    t += dt
    duty = k * 0.5 * (math.sin(t) + 1.)
    print(duty)