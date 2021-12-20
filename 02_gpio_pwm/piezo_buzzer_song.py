import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

melody = [262,294,330,349,392,440,494,523] #도 레 미 파 솔 라 시 도

'''
학교종 계 이름



솔솔라라 솔솔미  솔솔미미레
1 1 1 1  1 1 2  1 1 1 1 4 #박자 비율


솔솔라라 솔솔미 솔미레미도
1 1 1 1  1 1 2  1 1 1 1 4
'''
do = melody[0]
re = melody[1]
mi = melody[2]
sol = melody[4]
la = melody[5]

sounds = [
    sol,sol,la,la,sol,sol,mi,sol,sol,mi,mi,re,
    sol,sol,la,la,sol,sol,mi,sol,mi,re,mi,do
]

beats = [1,1,1,1,1,1,2,1,1,1,1,4,1,1,1,1,1,1,2,1,1,1,1,4]

def sing(beat):
    pwm.start(50)
    for i in range(len(sounds)):
        pwm.ChangeFrequency(sounds[i])
        time.sleep(beat * beats[i])
    pwm.stop()




#주파수 : 도(262Hz)
pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(50)

try:
    sing(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()
ly:
    pwm.stop()
    GPIO.cleanup()
