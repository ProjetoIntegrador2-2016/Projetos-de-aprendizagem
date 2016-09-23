# Perform calibration and apply triangle similarity
import cv2

class DistanceFinder:

	# Store the known width of the object (in inches, meters, etc.) and known distance
	# to the object (again, in inches, meters, etc.)
	def __init__(self, knownWidth, knownDistance):
		self.knownWidth = knownWidth
		self.knownDistance = knownDistance
		# initialize the focal length
		self.focalLength = 0

	# Compute and store the focal length for calibration
	def calibrate(self, knwonWidthPixels):
	 	self.focalLength = (knwonWidthPixels * self.knownDistance) / self.knownWidth

	def distance(self, perceivedWidthPixels):
		# compute and return the distance from the marker to the camera
		return (self.knownWidth * self.focalLength) / perceivedWidthPixels

 	
 	#  Find the largest approximately square object in an image
	@staticmethod
	def findSquareMarker(image):

		# convert the image to grayscale
 		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 		
 		# blur the image
 		gray = cv2.GaussianBlur(gray, (5, 5), 0)
 		
 		# find edges in the image
 		edged = cv2.Canny(gray, 35, 125)
		
		# find contours in the edged image
		# flag RETR_EXTERNAL: extract only the outer contours
		# prerequisite: marker will be one of the largest objects in an image
 		(contours, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 		
 		# sort contours by their size (from largest to smallest)
 		contours = sorted(contours, key=cv2.contourArea, reverse=True)
 		
 		# initialize the marker dimensions 	
 		markerDimensions = None

 		# loop over the contours
 		for c in contours:
	 		# approximate the contour
	 		perimeter = cv2.arcLength(c, True)
	 		approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
	 		# ensure that the contour is a rectangle
			if len(approx) == 4:
				# compute the bounding box and aspect ratio of the approximated contour
				(x, y, width, height) = cv2.boundingRect(approx)
				aspectRatio = width / float(height)
				# check to see if the aspect ratio is within tolerable bounds
				# to be considered as a square
				# if so, store the marker dimensions and break from the loop
				if aspectRatio > 0.9 and aspectRatio < 1.1:
					markerDimensions = (x, y, width, height)
					break
		return markerDimensions

	# Draw a bounding box around the marker and display the distance 
	# to the marker on the image
	@staticmethod
	def draw(image, boundingBox, dist, color=(0, 255, 0), thickness=2)
		(x, y, width, height) = boundingBox
		cv2.rectangle(image, (x, y), (x + widtht, y + height), color, 2)
		cv2.putText(image, "%.2fft" % (dist / 12), (image.shape), 
			cv2.FONT_HERSHEY_SIMPLEX, 2.0, color, 3)
		return image