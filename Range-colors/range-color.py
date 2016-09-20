import cv2
import numpy as np

img = cv2.imread('test2.jpg')

purple_min = np.array([3,51,40],np.uint8)
purple_max = np.array([13,255,255],np.uint8)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, purple_min, purple_max)
cv2.imwrite('result.jpg', frame_threshed)
