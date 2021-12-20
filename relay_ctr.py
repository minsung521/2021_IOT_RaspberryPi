import RPi.GPIO as GPIO
import time

class relay:
  def __init__ (self) :
    self.LED_PIN = 17    
    GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
    GPIO.setup(LED_PIN,GPIO.OUT) 

  def takePicture(self,delayT,lightT) :
    time.sleep(delayT)
    GPIO.output(self.LED_PIN,GPIO.HIGH)
    time.sleep(lightT)
    GPIO.output(self.LED_PIN,GPIO.LOW)
  def relayON() :
    GPIO.output(self.LED_PIN,GPIO.HIGH)

