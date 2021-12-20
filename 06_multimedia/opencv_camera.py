import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Camera open failed')
    exit()

ret, frame = cam.read()

cv2.imshow('frame', frame)
cv2.imwrite('output.jpg',frame)

cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()