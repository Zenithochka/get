import RPi.GPIO as GPIO
import time
import math                              

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

st = 100
pwm = GPIO.PWM(12, st)
duty = 0.0
A = 3.0
N = 1
t = 0.0
dt = 0.001
pwm.start(duty)



def tri(t):
    return 4 * A * N * abs(((t - 1/(8 * N)) % (1 / (2 * N))) - 1/(4 * N))

while True:
    t += dt
    time.sleep(dt)
    pwm.ChangeDutyCycle(tri(t) / 3.183 * 255)


    