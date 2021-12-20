dafruit_DHT.read_retry(sensor,DHT_PIN)
        if(h is not None and t is not None):
            print("Temperature : %.1f* Humidity : %.1f%%" % (t,h))
            print(now.strftime("%x %X"))
            display.lcd_display_string(now.strftime("%x %X"),1)
            display.lcd_disp
