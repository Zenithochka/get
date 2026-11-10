import RPi.GPIO as GPIO
import time
import math
from r2r_adc import R2R_ADC
from adc_plot import PLOT





try:
        dac = R2R_ADC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
