import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
status = 0

while True:
    if GPIO.input(13) == 1:
        status = not (status)
        while GPIO.input(13) == 1:
            status = status
    GPIO.output(26, status)