import cv2
image = cv2.imread('image.jpg')
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
while(True):

    cv2.imshow('gray_image1' , image1)    
    cv2.imshow( 'BRG_image',image)

    if cv2.waitKey(1)  == ord('v') :
        break
