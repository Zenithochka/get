import RPi.GPIO as GPIO
import time
import math                              

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 1000)
duty = 0.0
k = 1.0
t = 0.0
q = 2.
#rrr = 3.3 * 1. #0.001
dt = 0.001
pwm.start(duty)


while True:
    
    t = 0.
    while (duty > 0.0):
        duty = k * (t)
        time.sleep(dt)
        t += dt
        pwm.ChangeDutyCycle(duty)
        print(duty)
    t = 0.
    while (duty < 100.0):
        duty = 100. - k * (t)
        time.sleep(dt)
        t += dt
        pwm.ChangeDutyCycle(duty)
        print(duty)
    
    

