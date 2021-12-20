import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 10
ECHO_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN,True) #10us
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN,False)

        while GPIO.input(ECHO_PIN) == 0: pass
        start = time.time()
        while GPIO.input(ECHO_PIN) == 1: pass
        stop = time.time()
        duration_time = stop -start 
        distance = 17160 * duration_time
        print("Distance : %.1f" % distance)
        time.sleep(0.1)

finally:
    
    GPIO.cleanup()