import spidev
import time

spi = spidev.SpiDev()

spi.open(0,0)

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
        voltage = reading * 3.3/1023
        print("Reading=%d, Voltage=%f" % (reading,voltage))
        time.sleep(0.05)
finally:
    spi.close()
