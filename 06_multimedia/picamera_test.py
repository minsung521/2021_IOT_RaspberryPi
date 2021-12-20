import picamera
import time

path = '/home/pi/src3/06_multimedia'

camera = picamera.PiCamera()

try:
  camera.resolution = (640,480)
  camera.start_preview()
  time.sleep(3)
  camera.rotation = 180
  while True:
   now_str = time.strftime("%Y%m%d_%H%M%S")
   a = input("photo: 1, video: 2, exit: 9> ")
   
   if a == '1':
    camera.capture('photo_%s.jpg' % now_str)
   elif a == '2':
    camera.start_recording('video_%s.h264' % now_str)
    time.sleep(10)
    camera.stop_recording()
   elif a == '9':
     break
    

finally:
  camera.stop_preview()