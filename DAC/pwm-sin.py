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
A = 3.0
freq = 10
duty = 0.0
t = 0.0
dt = 0.001
pwm.start(duty)

def get_sin_wave_amplitude(freq, t):
    return 4 * math.pi * t * freq

while True:
    t += dt
    time.sleep(dt)
    pwm.ChangeDutyCycle(((1 + math.sin(get_sin_wave_amplitude(freq, t))) * A / 2) / 3.183 * 255)