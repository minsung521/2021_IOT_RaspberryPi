from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
import Adafruit_DHT
from bs4 import BeautifulSoup
import requests #request  - scripts 폴더까지 이동 후 pip install requests, pip install beautifulsoup4
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) 
lcd = LCD()
sensor = Adafruit_DHT.DHT11
DHTPIN = 18
url = "http://openapi.seoul.go.kr:8088/7a4f4452736b6d7333384e747a466f/xml/RealtimeCityAir/1/5/도심권/용산구" #도심권 중구의 데이터를 받아오는 api 주소

try:
  while True:
    lcd.clear()
    humidity, temperature = Adafruit_DHT.read_retry(sensor,DHTPIN)
    res = requests.get(url) # res 에 api 에서 받아온 xml 을 저장한다.
    soup = BeautifulSoup(res.content, 'html.parser') #bs4를 활용해 xml 데이터값을 받아온다.
    print(soup.pm10.get_text()+"㎍/m")
    pm10_str = soup.pm10.get_text()
    pm10 = int(soup.pm10.get_text())
    if pm10 <= 20 :   # 조건문 - 미세먼지 지수가 올라가면 표시하는 문구를 바꾼다.
      lcd.text("Open the door",1)
      GPIO.output(LED_PIN,0)
    elif pm10 <= 70:
      lcd.text("Not bad.",1)
      GPIO.output(LED_PIN,1)

    elif pm10 <= 140 :
      lcd.text("Dont open")
      GPIO.output(LED_PIN,1)

    else :
      lcd.text("NEVER OPEN!")
      GPIO.output(LED_PIN,1)

    lcd.text(pm10_str+"-fd"+f"T={temperature:.0f}C,H:{humidity:.1f}%",2) #두번쨰 줄에 실내 온도, 습도, 외부 미세먼지 농도를 표시한다
    time.sleep(10)
finally:
  lcd.clear()
  GPIO.cleanup()
  print("end")