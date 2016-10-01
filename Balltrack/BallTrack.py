# imports
import numpy as np
import imutils
import cv2
import library

GREEN_LOWER = [48, 48, 49]
GREEN_UPPER = [73, 255, 220]
OBJECT_WIDTH = 5.5


# define the lower and upper bounds of the color (green)
# ball in HSV color space, then initialize the list of tracked points
greenLowerBound = np.array(GREEN_LOWER, np.uint8)
greenUpperBound = np.array(GREEN_UPPER, np.uint8)

# if a video path was not supplied, grab the webcam
# otherwise, grab the reference video
camera = cv2.VideoCapture(0)

while camera.isOpened():

    # grab current frame
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=600)

    mask = library.applyMasks(frame, greenUpperBound, greenLowerBound)

    # find contours in the mask and initialize the current (x,y) center
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    position = ""
    radius = 1
    focalLenght = (114*16) / OBJECT_WIDTH
    distance = (OBJECT_WIDTH * focalLenght)/radius

    # only proceed if at least one contour was found
    if len(contours) > 0:
        center = None

        ((x,y), radius) = findCircleContour(contours)

        centroid = library.calculateCentroid(largestContour)

        #only proceed if the raidus meets a minimun size
        if radius > 10:
            #draws the circle and centroid on the frame then update the list of
            # tracked points
            library.drawCircle(frame, (int(x), int(y)), int(radius))

            distance = (OBJECT_WIDTH * focalLenght) / radius

            position = library.findScreenPosition(centroid, frame)

    else:
        print('Not Found')

    library.printDistance(frame, distance)
    library.printPosition(frame, position)

    #show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    #if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
#cleanup the camera and close any windows
camera.release()
cv2.destroyAllWindows()
