#내부 풀업 / 풀다운 저항 사용하기
import RPi.GPIO as GPIO
import time

SWITCH_PIN = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)
        

finally:
    GPIO.cleanup()
    print("cleanup and exit!")
