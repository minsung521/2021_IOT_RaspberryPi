'''
이 프로그램은 코로나 거리두기 2M 간격을 지키기 위해 만들어졌다.

'''

#모듈 임포트
import RPi.GPIO as GPIO
import time

#PIN 초기화
TRIGGER_PIN = 10
ECHO_PIN = 8
SWITCH_PIN = 9
BUZZER_PIN = 6
LED_R_PIN = 18
LED_G_PIN = 4

#flag(on / off) 기능 변수
flag = False

#PIN 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(SWITCH_PIN,GPIO.IN,GPIO.PUD_UP) #풀업저항
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.setup(LED_R_PIN,GPIO.OUT)
GPIO.setup(LED_G_PIN,GPIO.OUT)

#pwm 설정 / 음계 중 '도' 소리가 출력된다.
pwm = GPIO.PWM(BUZZER_PIN,262)  
pwm.start(0)

try:
    #time 5초 간격 설정
    time_start=time.time()
    time_end=time_start+5

    while True:
        val = GPIO.input(SWITCH_PIN)
        if val == 0 and switch_status==0: #버튼을 눌러서 on으로 전환한다 / flag = True
            flag = not flag
            time.sleep(1) #버튼을 누르면 값이 계속 0이기 때문에 if문이 한번이 아니라 여러번 작동할 수 있다. 작동을 잠깐 멈추어서 반복하는 것을 막는다.
            
        elif val == 0 and switch_status==1: #버튼을 눌러서  off로 전환한다 / flag = False
            flag = not flag
            time.sleep(1) #버튼을 누르면 값이 계속 0이기 때문에 if문이 한번이 아니라 여러번 작동할 수 있다. 작동을 잠깐 멈추어서 반복하는 것을 막는다.
            
        GPIO.output(LED_G_PIN, GPIO.HIGH if flag else GPIO.LOW) #flag가 True라면 LED가 켜진다.
        
        #flag가 True일때만 실행한다
        if flag == False: continue
        else:
            #5초가 지났을 때 거리를 잰다.
            if time.time()>=time_end:
                #초음파 센서를 활용한 거리 측정
                GPIO.output(TRIGGER_PIN,True) #10us
                time.sleep(0.00001)
                GPIO.output(TRIGGER_PIN,False)
                while GPIO.input(ECHO_PIN) == 0: pass
                start = time.time()
                while GPIO.input(ECHO_PIN) == 1: pass
                stop = time.time()
                duration_time = stop -start 
                distance = 17160 * duration_time

                #시간 5초 루프 초기화
                time_start=time.time()
                time_end=time_start+5
                
                if(distance < 200): #거리가 2M 이내라면
                    #piezp_buzzer와 LED ON!
                    pwm.ChangeDutyCycle(50)
                    GPIO.output(LED_R_PIN,GPIO.HIGH)
                else:
                    #piezp_buzzer와 LED OFF!
                    pwm.ChangeDutyCycle(0)
                    GPIO.output(LED_R_PIN,GPIO.LOW)
            time.sleep(0.1)
finally:
    GPIO.cleanup()
