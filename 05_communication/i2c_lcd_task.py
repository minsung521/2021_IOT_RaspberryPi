from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
display = drivers.Lcd()
now = datetime.datetime.now()

DHT_PIN = 15

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        if(h is not None and t is not None):
            print("Temperature : %.1f* Humidity : %.1f%%" % (t,h))
            # print(now.strftime("%x %X"))
            # display.lcd_display_string(now.strftime("%x %X"),1)
            display.lcd_display_string("%0.1f*C, 0.1f%",2)
        else : print("Read Error")
finally:
    print("Bye")



