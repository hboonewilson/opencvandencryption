import cv2
import numpy as np

#open cascade .xml file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#begin video capture from camera 0... home cam of MAC
cap = cv2.VideoCapture(0)

#while program is running...
while True:
    # img is now the a frame being taken by camera
    ret, img = cap.read()
    #convert img to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces in gray scale images using these sensitivity parameters
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #for each face found in picture split them up into x,y,width,height coordinates
    for (x,y,w,h) in faces:
        #create a rectangle onto the image with 225 blue and point 4 
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
    cv2.imshow('img', img)
    #this is how often we show each new frame in miliseconds
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
