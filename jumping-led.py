import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

for i in range(0, 8):
         GPIO.setup(leds[i], GPIO.OUT)

while True:
    for i in range(0, 8):
         GPIO.output(leds[i], 1)
         time.sleep(0.2)
         GPIO.output(leds[i], 0)
    for i in range(7, -1, -1):
         GPIO.output(leds[i], 1)
         time.sleep(0.2)
         GPIO.output(leds[i], 0)