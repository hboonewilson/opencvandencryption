#Use openCV and other libraries to find lanes in a road
import cv2
import numpy as np

def make_coordinates(image, line_parameters):
    #separate the slope and intercept
    slope, intercept = line_parameters
    #y1 is equal to the bottom of the image
    y1 = image.shape[0]
    #y2 is equal to bottom of the image * 3/5
    y2 = int(y1*(3/5))
    #x1 is y1 - the intercept div by the slope
    x1 = int((y1 - intercept)/ slope)
    #x2 is y2 - intercept div by the slope
    x2 = int((y2 - intercept)/ slope)
    #return an array with end point coordinates for the line
    return np.array([x1,y1,x2,y2])

def average_slope_intercept(image, lines):
    '''for each line making up the road...
    create a consistent line with averages of lane line'''
    #create lists to add to later for left and right fits
    left_fit = []
    right_fit = []
    #iterate for each line found in lines
    for line in lines:
        #reshape lines found into individual xy corrdinates
        x1,y1,x2,y2 = line.reshape(4)
        #set parameters to function .polyfit() that returns m and b parameters
        #for line that is being evaluated should return an array of two values
        parameters = np.polyfit((x1,x2), (y1,y2), 1)
        #slope is first value in parameters array
        slope = parameters[0]
        #intercept is second value in parameters array
        intercept = parameters[1]
        #if slope smaller than zero: (negative)
        if slope < 0:
            #line is left side of lanes so append to left_fit as a tuple
            left_fit.append((slope, intercept))
        #otherwise if slope is larger than zero...
        else:
            #line is right side of lanes so append to right_fit as tuple
            right_fit.append((slope, intercept))

    #averages of slopes and y intercepts for right and left sides
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)

    #create left and right lines using make_coordinates() function
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    #return an array of the two lines coordinates
    return np.array([left_line, right_line])

def canny(image):
    '''create a gradient of the image passed in'''
    #turn image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #give image a blur to single out biggest contrasts
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    #use canny to create an image that shows only the sharp contrasts
    canny = cv2.Canny(blur, 50, 150)
    return canny




def display_lines(image, lines):
    '''Display the lines that are detected in the image'''
    #line_image = an array of zeros the same size as the pixels in the image
    line_image = np.zeros_like(image)
    #if there are lines found in lines argument..
    if lines is not None:
        #iterate through them
        for line in lines:
            #reshape line into 4 seprate variables
            x1, y1, x2, y2 = line.reshape(4)
            #write a line onto line image using the endpoints
            #.line(image_writing_on, end point1, end point2, RBG color Blue, font size 10)
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 10)
    return line_image




def region_of_interest(image):
    '''From our gradient image... specify what the area of intrest is'''
    #height = bottom of the image
    height = image.shape[0]
    #the area of intrest (or this triangle) is...
    #pixel 200xbottom, pixel 1100xbottom, 550x250
    triangle = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    #create an image with all black pixels (np.zeros_like, bec 0 == to black)
    #with the same amount of pixels as the jpeg
    mask = np.zeros_like(image)
    #edit mask to include the dimensions of the triangle as all white (255==white)
    cv2.fillPoly(mask, triangle, 255)
    #asked image is = bitwise and the two images... mask and images
    # white = 1111111 black = 0000000 by & operation we cancel out everything
    #outside of the triangle and leave the gradient of the area of intrest
    masked_image = cv2.bitwise_and(image, mask)
    #return edited mask
    return masked_image


# #read image specified
# image = cv2.imread('test_image.jpg')
# #before creating the contrasted image, copy the image
# lane_image = np.copy(image)
#
# #use canny function
# canny = canny(lane_image)
#
# #pass in canny in to the region of interest function and set to cropped image
# cropped_image = region_of_interest(canny)
#
# #use HoughLinesP to find straight lines int a gradient image
# #.HoughLinesP(image to read, 2pixelbin, radian, threshold of intersections, empty array, minLength of line, max gap of line)
# lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
#
# averaged_lines = average_slope_intercept(lane_image, lines)
#
# #line_image is equal to function display_lines passed in with lane_image as the image argument
# #and lines as the lines found using .HoughLinesP()
# line_image = display_lines(lane_image, averaged_lines)
#
# #combo_image is lane_image weighted against line_image
# combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
#
# #show results of algorithm so far as a window
# # .imshow(name_of_window, variable_being_displayed)
# cv2.imshow("result", combo_image)
# #leave for as long as i need to
# #!!(to properly end program.. press anywhere on keyboard NOT the X button)!!
# cv2.waitKey(0)
#read image specified

#cap is equal to cv2.VideoCapture('video_file.mp4')
cap = cv2.VideoCapture('test2.mp4')
#while the video is opened and running...
while(cap.isOpened()):
    _, frame = cap.read()
    #use canny function
    canny_image = canny(frame)

    #pass in canny in to the region of interest function and set to cropped image
    cropped_image = region_of_interest(canny_image)

    #use HoughLinesP to find straight lines int a gradient image
    #.HoughLinesP(image to read, 2pixelbin, radian, threshold of intersections, empty array, minLength of line, max gap of line)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

    averaged_lines = average_slope_intercept(frame, lines)

    #line_image is equal to function display_lines passed in with lane_image as the image argument
    #and lines as the lines found using .HoughLinesP()
    line_image = display_lines(frame, averaged_lines)

    #combo_image is lane_image weighted against line_image
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    #show results of algorithm so far as a window
    # .imshow(name_of_window, variable_being_displayed)
    cv2.imshow("result", combo_image)
    #this is how often we show each new frame in miliseconds
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
