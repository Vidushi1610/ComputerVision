import cv2
capture = cv2.VideoCapture(1)

while(True):
  ret,frame= capture.read()
  cv2.imshow('frame', frame)
  if cv2.waitkey(1) == ord('v'):
    break
