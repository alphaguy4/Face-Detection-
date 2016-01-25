import cv2

print 'The image and program should be in same folder'
imagePath = str(raw_input("Enter the image file name with extension.\n"))
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)
