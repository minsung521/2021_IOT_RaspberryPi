import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHTPIN = 18

try :
  while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor,DHTPIN)
    if humidity is not None and temperature is not None:
      print(f"Temperature={temperature:.1f}C,Humidity:{humidity:.1f}%")
    else :
      print('read error')
    time.sleep(1)

finally:
  GPIO.cleanup()
  print("end")

