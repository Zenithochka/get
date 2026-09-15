import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)

#leds = [24, 22, 23, 27, 17, 25, 12, 16]
leds = [16, 12, 25, 17, 27, 23, 22, 24]

for i in range(0, 8):
         GPIO.setup(leds[i], GPIO.OUT)

point = 0
status1 = 0
status2 = 0
a = ''

while True:
    if GPIO.input(10) == 1:
        if status1 == 0:
            status1 = 1
            point += 1
        while GPIO.input(10) == 1:
            status1 = 1
    status1 = 0
    
    if GPIO.input(9) == 1:
        if status2 == 0:
            status2 = 1
            point -= 1
        while GPIO.input(9) == 1:
            status2 = 1
    status2 = 0
    
    if point > 255:
        point = 0
    if point < 0:
        point = 0
        
    #[::-1]
    #a = bin(256 - point)
    a = ((10 - len(bin(point))) * '0' + (bin(point)[2:]))
    
    for i in range(0, 8):
        if a[i] == '0':
            GPIO.output(leds[i], 0)
        else:
            GPIO.output(leds[i], 1)
    print(point, bin(point), a)
    