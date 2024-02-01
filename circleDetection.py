#import libraries
import cv2 as cv
import numpy as np

#define function with image as only parameter
def circleDetection(img):

   #open image in color
    snap = cv.imread(img, cv.IMREAD_COLOR)
    cv.imshow('frame',snap)
    cv.waitKey(0)

   #convert image to grayscale
    grey = cv.cvtColor(snap, cv.COLOR_BGR2GRAY)
    cv.imshow('grey',grey)
    cv.waitKey(0)

   #blur grayscale image
    gauss = cv.GaussianBlur(grey,(11,11),0)
    cv.imshow('gauss',gauss)
    cv.waitKey(0)

   #Blur twice for good luck

   #Use HoughCircles transform to detect circular objects
    circles = cv.HoughCircles(gauss,cv.HOUGH_GRADIENT,1,38,param1=100,param2=65,minRadius=500,maxRadius=0)


   #Convert circles to integers
    circles = np.uint16(np.around(circles))

   #Draw detected circles
    for i in circles[0,:]:
        #Draw outer circle
        cv.circle(grey,(i[0],i[1]),i[2],(34,255,0),7)

        #Draw midpoint
        cv.circle(grey, (i[0], i[1]), 2, (0, 255, 0), 3)


   #show frame and wait for break
    cv.imshow('final',grey)
    cv.waitKey(0)