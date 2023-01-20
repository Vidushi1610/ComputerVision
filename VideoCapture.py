import cv2
import imutils

capture = cv2.VideoCapture(0) 
while(True):

    ret, frame = capture.read()
    frame = imutils.resize(frame, width=600)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)  == ord('v'):
        break

