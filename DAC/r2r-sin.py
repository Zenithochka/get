from r2r_dac import R2R_DAC
import RPi.GPIO as GPIO
import time
import math  

dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)

A = 1.6
freq = 1000
dt = 0.000001
t = 0

'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(16, 28):
    GPIO.setup(i, GPIO.OUT)

#bits = [22, 27, 17, 26, 25, 21, 20, 16]
bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
'''

def get_sin_wave_amplitude(freq, t):
    return 2 * math.pi * t * freq

while True:
    t += dt
    time.sleep(dt)
    dac.set_voltage((1 + math.sin(get_sin_wave_amplitude(freq, t))) * A / 2)