import RPi.GPIO as GPIO
import cv2


GPIO.setmode(GPIO.BCM)

class Button:
	def __init__(self, pin):
		self.pin = pin
		self.on_down = []
		self.on_up = []
		self.before = 1
		GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	
	def update(self):
		val = GPIO.input(self.pin)
		if val != self.before:
			if val == 0:
				for function in self.on_down:
					function(self.pin)
			else:
				for function in self.on_up:
					function(self.pin)
			self.before = val
  
class Snow:
	def __init__(self) -> None:
		self.filter_image = None
		self.cam = cv2.VideoCapture(0)
		if not self.cam.isOpened():
			print('Camera open failed')
			exit()

		self.face_cascade = cv2.CascadeClassifier('./xml/face.xml')

		self.cam_width  = self.cam.get(3)  # float `width`
		self.cam_height = self.cam.get(4)
	def __del__(self):
		self.cam.release()
	
	def set_filter_image(self, path:str):
		if path == None:
			self.filter_image = None
		else:
			self.filter_image = cv2.imread(path)

	def save_to_file(self, path):
		ret, frame = self.cam.read()
		if not ret:
			return
		
		if self.filter_image != None:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

			for (x, y, w, h) in faces:
				self.add_filter(frame, self.filter_image, x, y, w, h)
		cv2.imwrite(path, frame)
		

	def add_filter(self, original_img, filter_img, x, y, w, h):
		rows, cols, channels = filter_img.shape
		width_ratio, height_ratio = w / rows, h / cols
		max_ratio = max(width_ratio, height_ratio)
		resized_width, resized_height = cols * max_ratio, rows * max_ratio
		roi_x, roi_y =  x- (resized_width - w)//2, y - (resized_height - h)//2
		if roi_x < 0:
			resized_width += roi_x
			roi_x = 0
		if roi_x + resized_width > self.cam_width:
			resized_width -= roi_x + resized_width - self.cam_width
		if roi_y < 0:
			resized_height += roi_y
			roi_y = 0
		if roi_y + resized_height > self.cam_height:
			resized_height -= roi_y + resized_height - self.cam_height
		resized_width, resized_height = int(resized_width), int(resized_height)
		roi_x, roi_y = int(roi_x), int(roi_y)
		resized_animal_filter_img = cv2.resize(self.filter_image, dsize=(resized_width, resized_height), interpolation=cv2.INTER_NEAREST)
		ret, mask = cv2.threshold(resized_animal_filter_img[:, :, 2], 0, 255, cv2.THRESH_BINARY)
		mask_inv = cv2.bitwise_not(mask)
		roi = original_img[roi_y:roi_y+resized_height, roi_x:roi_x+resized_width]
		dst = cv2.add(cv2.bitwise_and(roi, roi, mask=mask_inv), resized_animal_filter_img)
		original_img[roi_y:roi_y+resized_height, roi_x:roi_x+resized_width] = dst

	def update(self):
		ret, frame = self.cam.read()
		if not ret:
			return
		
		if self.filter_image != None:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

			for (x, y, w, h) in faces:
				self.add_filter(frame, self.filter_image, x, y, w, h)

		cv2.imshow('frame', frame)

		if cv2.waitKey(10) == 13:
			exit()

def print_button(pin):
	print(pin)

update_queue = []

red_button = Button(5)
yellow_button = Button(6)
blue_button = Button(13)
black_button = Button(19)
white_button = Button(26)


snow = Snow()

red_button.on_down.append(print_button)
yellow_button.on_down.append(print_button)
blue_button.on_down.append(print_button)
black_button.on_down.append(print_button)
white_button.on_down.append(print_button)

update_queue.append(red_button)
update_queue.append(yellow_button)
update_queue.append(blue_button)
update_queue.append(black_button)
update_queue.append(white_button)
update_queue.append(눈)

snow.set_filter_image('assets/racoon.png')


def set_filter_none():
	snow.set_filter_image(None)

def set_filter_racoon():
	snow.set_filter_image('assets/racoon.png')

red_button.on_down.append(set_filter_racoon)
white_button.on_down.append(set_filter_none)

def update():
	for element in update_queue:
		element.update()

if __name__ == '__main__':
	try:
		while True:
			update()
	finally:
		print('ended')
		cv2.destroyAllWindows()
		GPIO.cleanup()