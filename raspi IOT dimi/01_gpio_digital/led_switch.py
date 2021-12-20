import RPi.GPIO as GPIO

SWITCH_PIN = 4
LED_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#������ �ʾ��� �� : 0, ������ ��: 1
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #����Ǯ�ٿ�

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')