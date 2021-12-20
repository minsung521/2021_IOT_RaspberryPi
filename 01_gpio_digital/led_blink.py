import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN,GPIO.OUT) #GPIO.OUT or GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN,GPIO.HIGH) #1,TRUE
    print("LED ON")
    time.sleep(1)
    GPIO.output(LED_PIN,GPIO.LOW) #0,FALSE
    print("LED OFF")
    time.sleep(1)

GPIO.cleanup() #GPIO 핀 상태 초기화 xls