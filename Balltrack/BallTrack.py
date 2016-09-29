# imports
import numpy as np
import imutils
import cv2

# define the lower and upper bounds of the color (green)
# ball in HSV color space, then initialize the list of tracked points

# simple green
# greenLower = np.array([27, 68, 38], np.uint8)
# greenUpper = np.array([88, 255, 255], np.uint8)

# optimized for the target ball
greenLower = np.array([48, 48, 49], np.uint8)
greenUpper = np.array([73, 255, 220], np.uint8)


# if a video path was not supplied, grab the webcam
# otherwise, grab the reference video
camera = cv2.VideoCapture(0)

while camera.isOpened():

    # grab current frame
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # creates a mask for the color, the do dilatations and erosions
    # to remove small blobs in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current (x,y) center
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    radius = 1
    focalLenght = (114*16) / 5.5
    distance = (5.5*focalLenght)/radius
    position = ""

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        #find the largest contour in the mask, then use it to compute the minimunm enclosing circle and centroid
        c = max(cnts, key = cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        #only proceed if the raidus meets a minimun size
        if radius > 10:
            #draws the circle and centroid on the frame then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            distance = (5.5 * focalLenght) / radius

            if center[0] < (frame.shape[1] / 3):
                position = "Esquerda"
            elif center[0] < (frame.shape[1] / 3) * 2:
                position = "Centro"
            else:
                position = "Direita"

            if center[1] < (frame.shape[0]/3):
                position += "-Cima"
            elif center[1] < (frame.shape[0] / 3) * 2:
                position += "-Centro"
            else:
                position += "-Baixo"

    else:
        print('Not Found')

    cv2.putText(frame, "%.2f cm" % distance, (frame.shape[1] - 200, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    cv2.putText(frame, position, (50, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    #show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    #if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

#cleanup the camera and close any windows
camera.release()
cv2.destroyAllWindows()
