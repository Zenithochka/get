import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(6, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

while True:
    if GPIO.input(6) == 0:
        GPIO.output(26, 1)
    else:
        GPIO.output(26, 0)
    #GPIO.output(23, 1)
#cd Desktop/Scripts/