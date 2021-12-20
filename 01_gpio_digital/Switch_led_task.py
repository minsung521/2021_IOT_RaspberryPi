import RPi.GPIO as GPIO


LEDR = 5
LEDY = 6
LEDG = 13

bt1 = 17
bt2 = 27
bt3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDR,GPIO.OUT)
GPIO.setup(LEDY,GPIO.OUT)
GPIO.setup(LEDG,GPIO.OUT)

GPIO.setup(bt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운
GPIO.setup(bt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운
GPIO.setup(bt3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운


try :
  while True:
    val1 = GPIO.input(bt1)
    val2 = GPIO.input(bt2)
    val3 = GPIO.input(bt3)
    GPIO.output(LEDR, val1)
    GPIO.output(LEDY, val2)
    GPIO.output(LEDG, val3)
    if val1 == val2 == val3 == True : break
finally:
    GPIO.cleanup()
    print("cleanup and exit")