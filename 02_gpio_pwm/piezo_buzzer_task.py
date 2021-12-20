import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,1)

#         도0  레1  미2 파3  솔4  라5  시6
melody = [262,294,330,349,391,440,494]
song = [4,4,5,5,4,4,2,4,4,2,2,1,4,4,5,5,4,4,2,4,2,1,2,0]
pwm.start(50)

for i in song:
  pwm.ChangeFrequency(melody[i])
  print(i)
  time.sleep(0.5)

pwm.stop()
GPIO.cleanup()  