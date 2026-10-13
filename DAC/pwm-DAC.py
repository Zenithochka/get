import RPi.GPIO as GPIO
import time
import math                              

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 1000)
rez = 2
duty = 0.0
k = 1.0
t = 0.0
q = 2.
dt = 0.001
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(100.*rez/3.3)
