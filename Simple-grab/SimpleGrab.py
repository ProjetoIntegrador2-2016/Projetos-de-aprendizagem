import numpy as np
import cv2

cap =cv2.VideoCapture(0)

if cap.isOpened() == False:
    printf('Error: Unable to open the camera')
else:
    print('Start grabbing, press any key on Live window to terminate')

    cv2.namedWindow('Live')
    while( cap.isOpened() ):
        ret,frame = cap.read()
        if ret==False:
            print('Error: Unable to grab camera')
            break;

        cv2.imshow('Live', frame)
        if cv2.waitKey(1) >= 0:
            break;

    print('Closing the camera')

cap.release()
cv2.destroyAllWindows()

print('bye')
