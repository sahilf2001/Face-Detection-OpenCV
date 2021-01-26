import cv2,time

video = cv2.VideoCapture(0) # for using the in-built camera / video link can also be provided

check, frame = video.read()
# check is a bool type that returns if Python is able to read the VideoCapture object
# frame is a numpy array it represents first image that video captures
print(check)
print(frame)

time.sleep(3)

cv2.imshow('Capturing',frame) #used to capture the first image/frame of the video

cv2.waitKey(0)

video.release() #this will release the camera in some milliseconds

cv2.destroyAllWindows()
