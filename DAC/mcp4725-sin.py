from mcp4725_driver import MCP4725
import RPi.GPIO as GPIO
import time
import math  

dac = MCP4725(5.11)

A = 3.0
freq = 1
dt = 0.001
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
    return 4 * math.pi * t * freq

while True:
    t += dt
    time.sleep(dt)
    dac.set_voltage((1 + math.sin(get_sin_wave_amplitude(freq, t))) * A / 2)