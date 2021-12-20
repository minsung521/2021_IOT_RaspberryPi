import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN,GPIO.IN)
line = 0;
try:
  while True:
    val = GPIO.input(SWITCH_PIN)
    #print(val)
    if val == 0:
      line = line + 1
    else :
      line = line - 1
    print("-"*line)
    time.sleep(0.1)
finally:
  GPIO.cleanup()
  print('cleanup and exit')