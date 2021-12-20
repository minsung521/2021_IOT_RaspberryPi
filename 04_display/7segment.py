import RPi.GPIO as GPIO
import time

#GPIO 7개 pin 번호 설정
#              A,B,C,D,E,F,G
SEGMENT_PINS = [2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]
SWITCH_PIN = 14

GPIO.setmode(GPIO.BCM)
for segment in SEGMENT_PINS : 
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)

#자릿수 제어는 HIGH->OFF, LOW -> ON
for digit in DIGIT_PINS:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit,GPIO.IN)

GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

option = 0

def display(digit,number):
    for i in range(len(DIGIT_PINS)):
        if i+1 == digit:
            GPIO.output(DIGIT_PINS[i],GPIO.LOW)
        else:
             GPIO.output(DIGIT_PINS[i],GPIO.HIGH)
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i],data[number][i])
    time.sleep(0.1) 


def output(time,option):
    one = 0, two = 0
    if(len(time) == 1): two = int(time[0])
    else: one = int(time[0]),two = int(time[1])

    if(option == 0): display(1,one),display(2,two)
    else: display(3,one),display(4,two)

try:
    while(1):

        val = GPIO.input()
        if(val == GPIO.HIGH): val+=1

        if(option == 0):
            hour,min = time.ctime()[11:16].split(":")
            output(hour,0),output(min,1)
        elif(option == 1):
            ...
        elif(option == 2):
            ...
        
finally:
    GPIO.cleanup()
    print("Bye")

