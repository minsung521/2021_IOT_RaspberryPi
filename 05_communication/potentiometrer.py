import spidev
import time

# ㅇSPI 인스탄스 생서으
spi = spidev.Spiredef

spi.open() #(bus : 0, dev = 0 (CE0,CE1))

#SPI 통신의 최대 속도 설정
spi.max_speed_hz = 1000000

# 0~7까지 채널에서 SPI 데이터 읽기
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 -> 0000 1000 << 4 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (channel + 8) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:
    while True:
        reading = analog_read(0)
        #전압 수치값 변환(0~3.3V)
        voltage = reading * 3.3 / 1023
        print("Reading = %d, Voltage = %.2f" % (reading,voltage))
        time.sleep(0.5)
finally:
    spi.close()