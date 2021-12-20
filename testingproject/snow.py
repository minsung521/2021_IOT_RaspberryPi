import cv2

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

cam_width  = cam.get(3)  # float `width`
cam_height = cam.get(4)


def add_filter(original_img, filter_img, x, y, w, h):
	rows, cols, channels = filter_img.shape
	width_ratio, height_ratio = w / rows, h / cols
	max_ratio = max(width_ratio, height_ratio)
	resized_width, resized_height = cols * max_ratio, rows * max_ratio
	roi_x, roi_y =  x- (resized_width - w)//2, y - (resized_height - h)//2
	if roi_x < 0:
		resized_width += roi_x
		roi_x = 0
	if roi_x + resized_width > cam_width:
		resized_width -= roi_x + resized_width - cam_width
	if roi_y < 0:
		resized_height += roi_y
		roi_y = 0
	if roi_y + resized_height > cam_height:
		resized_height -= roi_y + resized_height - cam_height
	resized_width, resized_height = int(resized_width), int(resized_height)
	roi_x, roi_y = int(roi_x), int(roi_y)
	resized_animal_filter_img = cv2.resize(animal_filter_img, dsize=(resized_width, resized_height), interpolation=cv2.INTER_NEAREST)
	ret, mask = cv2.threshold(resized_animal_filter_img[:, :, 2], 0, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	roi = original_img[roi_y:roi_y+resized_height, roi_x:roi_x+resized_width]
	print(cam_width, cam_height, roi_x, roi_x + resized_width, roi_y, roi_y + resized_height)
	dst = cv2.add(cv2.bitwise_and(roi, roi, mask=mask_inv), resized_animal_filter_img)
	original_img[roi_y:roi_y+resized_height, roi_x:roi_x+resized_width] = dst


if not cam.isOpened():
	print('Camera open failed')
	exit()

while True:
	ret, frame = cam.read()
	if not ret:
		break
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	animal_filter_img = cv2.imread('assets/racoon.png')
	rows, cols, channels = animal_filter_img.shape

	for (x, y, w, h) in faces:
		add_filter(frame, animal_filter_img, x, y, w, h)

	cv2.imshow('frame', frame)

	if cv2.waitKey(10) == 13:
		break

cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()