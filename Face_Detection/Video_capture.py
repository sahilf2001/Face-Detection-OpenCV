import cv2,time

video = cv2.VideoCapture(0)

a=1

while True: # to iterate through the frames
    a+=1
    check, frame = video.read()
    print(frame)

    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# convert each frame to grayscale

    cv2.imshow('Capturing',img)

    key = cv2.waitKey(1) #this will generate a new frame after every 1 ms

    if key == ord('q'): #once you enter 'q' the window will be destroyed
        break
print(a) # this will print the number of frames
video.release()
cv2.destroyAllWindows()
