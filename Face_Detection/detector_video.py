import cv2,time

# Create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

a=1

while True: # to iterate through the frames
    a+=1
    check, frame = video.read()
    print(frame)

    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# convert each frame to grayscale

    # Search the co-ordinates of the image
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.05,
                                          minNeighbors=5)  # Decreases the shape value by 5% until the face is found, smaller this value, the greater the accuracy

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow('Capturing',img)

    key = cv2.waitKey(1) #this will generate a new frame after every 1 ms

    if key == ord('q'): #once you enter 'q' the window will be destroyed
        break
print(a) # this will print the number of frames
video.release()
cv2.destroyAllWindows()
