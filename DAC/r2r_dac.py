import RPi.GPIO as GPIO
import time
import math                              

'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(16, 28):
    GPIO.setup(i, GPIO.OUT)
'''

'''
#bits = [22, 27, 17, 26, 25, 21, 20, 16]
gpio_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
'''

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        g = '0' * (8 - len(bin(number)[2:])) + bin(number)[2:]
        print(g)
        for i in range(0, 8):
            GPIO.output(self.gpio_bits[i], int(g[i]))

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return 0
        self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()