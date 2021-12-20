#도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

#주파수 : 도(262Hz)
pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(10)
#10 : 작게 들리고 도인지 모름.
#50 : 굵어짐
#100 : 삐! (도)음인가...? 확실히 잘 들림
time.sleep(2)

pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
