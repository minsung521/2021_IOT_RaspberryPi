'''
LED RED,YELLOW,GREEN... 3가지를 연결한 후 2초 간격으로 켜지도록 해보자
Ex) RED 2초 ON, RED OFF & YELLOW 2초 ON, YELLOW OFF & GREEN 2초 ON, GREEN OFF
'''
import RPi.GPIO as GPIO
import time

LED_PIN_R = 4
LED_PIN_Y = 17
LED_PIN_G = 27
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN_R,GPIO.OUT) #GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN_Y,GPIO.OUT)
GPIO.setup(LED_PIN_G,GPIO.OUT)

GPIO.output(LED_PIN_R,GPIO.HIGH) 
time.sleep(2)
GPIO.output(LED_PIN_R,GPIO.LOW)

GPIO.output(LED_PIN_Y,GPIO.HIGH) 
time.sleep(2)
GPIO.output(LED_PIN_Y,GPIO.LOW)

GPIO.output(LED_PIN_G,GPIO.HIGH) 
time.sleep(2)
GPIO.output(LED_PIN_G,GPIO.LOW)
GPIO.cleanup() #GPIO 핀 상태 초기화 xls