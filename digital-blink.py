import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

while True:
    GPIO.output(26, 1)
    time.sleep(0.5)
    GPIO.output(26, 0)
    time.sleep(0.5)