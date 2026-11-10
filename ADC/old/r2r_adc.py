import RPi.GPIO as GPIO
import time
import math

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def number_to_dac(self, number):
        g = '0' * (8 - len(bin(number)[2:])) + bin(number)[2:]
        print(g)
        for i in range(0, 8):
            GPIO.output(self.bits_gpio[i], int(g[i]))

    def sequential_counting_adc(self, dynamic_range, stat = 1):
        a = 0
        while a <= 255:
            self.number_to_dac(a)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 0:
                if stat == 1:
                    print("Число на входе: ", a * dynamic_range / 255)
                return a
            a += 1
        if GPIO.input(self.comp_gpio) == 0:
            if stat == 1:
                print("Число на входе: ", dynamic_range)
        return a

    def get_sc_voltage(self, dynamic_range):
        v = self.sequential_counting_adc(dynamic_range, 0)
        return (v * dynamic_range / 255)

    def successive_approximation_adc(self):


        
        a = 0
        while a <= 255:
            self.number_to_dac(a)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 0:
                if stat == 1:
                    print("Число на входе: ", a * dynamic_range / 255)
                return a
            a += 1
        if GPIO.input(self.comp_gpio) == 0:
            if stat == 1:
                print("Число на входе: ", dynamic_range)
        return a
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.183)
        
        while True:
            voltage = adc.get_sc_voltage
            print("Напряжение на входе: ", voltage)

    finally:
        adc.deinit()