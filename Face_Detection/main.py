import cv2

# Create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread("El.jpg")

# Reading the image as gray scale image
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(grayimg,scaleFactor=1.05,minNeighbors=5) # Decreases the shape value by 5% until the face is found, smaller this value, the greater the accuracy


for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("Face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
