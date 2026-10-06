import RPi.GPIO as GPIO
import time
import math  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(16, 28):
    GPIO.setup(i, GPIO.OUT)

#bits = [22, 27, 17, 26, 25, 21, 20, 16]
bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    g = '0' * (8 - len(bin(number)[2:])) + bin(number)[2:]
    print(g)
    for i in range(0, 8):
        GPIO.output(bits[i], int(g[i]))
    
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()