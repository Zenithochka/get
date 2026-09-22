import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0