import RPi.GPIO as GPIO
import time

LED_PIN = 4
SWITCH_PIN = 12  

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        GPIO.output(LED_PIN,val)
finally:
    GPIO.cleanup()
    print("cleanup and exit!!")''