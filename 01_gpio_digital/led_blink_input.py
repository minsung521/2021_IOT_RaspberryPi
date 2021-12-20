import RPi.GPIO as GPIO
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)


try:
    while(True):
        val = input("1 : ON, 0 : OFF, 9 : EXIT > ")
        if val == '0':
            GPIO.output(LED_PIN,GPIO.LOW)
            print("LED OFF")
        elif val == '1':
            GPIO.output(LED_PIN,GPIO.HIGH)
            print("LED ON")
        elif val == '9':
            break
        else: continue
finally: 
    GPIO.cleanup()
    print("Cleanup and Exit")