import cv2
import matplotlib.pyplot as plt

"""It is a magic function that renders the figure in a notebook (instead of displaying a dump of the figure object)."""

# Get  image and cascade names
imagePath = "lag.jpg"
cascPath = "haarcascade_frontalface_default.xml"
"""OpenCV stores all its pre-trained Haar classifiers to detect various objects, body parts, etc."""

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""
OpenCV uses BGR as its default colour order for images, matplotlib uses RGB. 
When you display an image loaded with OpenCv in matplotlib the channels will 
be back to front.
The easiest way of fixing this is to use OpenCV to explicitly convert it back 
to RGB, much like you do when creating the greyscale image.
"""

RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.imshow(RGB_img)
plt.show()


# Detect faces in the image
faces = faceCascade.detectMultiScale(
   gray,
   scaleFactor=1.1,
   minNeighbors=5,
   minSize=(30, 30),
   flags = cv2.CASCADE_SCALE_IMAGE #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)


print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.show()