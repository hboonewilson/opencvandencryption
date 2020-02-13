
'''
Use a opencv to find the user's face on their front camera, then instruct them how 
to move their face to center in the middle of the screen. could be used in selfie 
applications.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

#middleface is a list middleface[0]== xvalue middleface[1] == yvalue
def displaylines(copypic, middleface):
    '''Calculates what type of lines should be displayed
    by where the middle of the face is on the x-axis'''
    #xmid is value x
    xmid = middleface[0]
    #ymid is value of y
    ymid = middleface[1]


    #for x#

    ##640 is the middle of the screen for x##
    #if middleface is above the middle of the screen...
    #if middleface is above the middle of the screen...
    if xmid > 640:
        #calc disttomid == (middle of the face)-(the middle of the screen)
        disttomid = xmid - 640
        #Boolean isright is True == middleface is on the right side of screen
        isright = True
    #if middleface is below middle of the screen
    else:
        #disttomid is (middleofscreen) - (middleface)
        disttomid = 640 - xmid
        #isright is False == face is to the left
        isright = False
    #if the face is between pixels 560 and 720...
    if xmid > 560 and xmid < 720:
        #display green lines on each side of the screen to show you are centered
        cv2.line(copypic,(0,0), (0,720), (0, 255, 0), thickness=50)
        cv2.line(copypic, (1280,0), (1280,720),(0,255,0), thickness=50)
    #if the face is outside of pixles 473 and 608...
    else:
        #if isright is True and the face is to the right of the screen
        if isright:
            #put a line on the left side of the screen 1/2 the thickness of the
            #distance to the middle and red color
            cv2.line(copypic, (0,0), (0,720), (0,0,255), thickness=(disttomid//2))
        #if face is to the left of the scree
        else:
            #put line of the right side of screen 1/4 the thickness of distance
            #to the middle and red color
            cv2.line(copypic, (1280, 0), (1280,720), (0,0,255), thickness=(disttomid//2))


    #for y#

    ##middle is 360##
    #if y is higer than the middle...
    if ymid > 360:
        #calculate distance to middle
        dtomid = ymid - 360
        #set islow to True
        islow = True
    #if y lower than the middle..
    else:
        #calculate distance to the middle
        dtomid = 360 - ymid
        #islow to False
        islow = False

    #360
    #80
    #if ymid is between  280 #440
    if ymid > 280 and ymid < 440:
        #draw lines to show you're centered
        cv2.line(copypic,(0,0), (1280, 0), (0, 255, 0), thickness=50)
        cv2.line(copypic,(0,720), (1280,720), (0, 255, 0), thickness=50)
    else:
        #if is low is True...
        if islow:
            #draw line on top of screen 1/2 the thickness of the distance to the
            # middle and red color
            cv2.line(copypic,(0,0), (1280, 0), (0, 0, 255), thickness=ymid//2)
        #if islow is False...
        else:
            #draw line on bottom of screen 1/2 the thickness of the distance to the
            # middle and red color
            cv2.line(copypic,(0,720), (1280, 720), (0, 0, 255), thickness=ymid//2)

def centerFace(copypic, gray, faces):
    '''Calculate where the center of the face is from data on the face.'''
    #use first face out of faces as the face of intrest
    face_intrest = faces[0]
    #set variables x,y,h,w to the their corresponding variable in face_intrest
    (x,y,h,w) = face_intrest
    #midw and midh is half of height and with
    midw = w//2
    midh = h//2
    #use midw and midh variables to determine the center of the face by adding them
    #x and y
    mid_face_x, mid_face_y = x + midw , y + midh
    #create a circle in the middel of the face onto the original picture with
    #radius at the center of the face, radius of 12 pixles, red, and thickness of -2
    #which means that the circle will be filled
    cv2.circle(copypic, (mid_face_x, mid_face_y), 12, (255, 0 , 0), thickness=-2)
    #return list of x and y coordinates
    return [mid_face_x, mid_face_y]


#use cv2's CascadeClassifier to pass a cascade into the program to find faces in
#this case
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Use .VideoCapture(0) to record
cap = cv2.VideoCapture(0)

#while program is running...
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    if len(faces) != 0:
        #use centerFace() to draw dot on middle of face and return list of midface
        # x and y coordinates to use
        midfacelis = centerFace(img, gray, faces)
        #use displaylines() to calclate and display lines to the screen
        displaylines(img, midfacelis)
    cv2.imshow('img', img)
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


###For pictures to test##


# #read in image
# picture = cv2.imread('P4.JPG')
# #copy the picture from the original image
# copypic = np.copy(picture)
# #convert to grayscale using cv2.cvtColor()
# gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
# #find faces using the face_cascade variable
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# #use centerFace() to draw dot on middle of face and return mid_face_x to use
# mid_face_x = centerFace(copypic, gray, faces)
# #use displaylines() to calclate and display lines to the screen
# displaylines(copypic, mid_face_x)
#
#
# ##MAX SIDE LINE THICKNESS IS 150 AND MINIMUM IS 20##
#
# plt.imshow(copypic)
# plt.show()
#
# #608 to 473
