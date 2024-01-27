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

   #Flatten Image
   flat = np.array(grey)
   flatImg = flat.flatten()

   #blur grayscale image
   # gauss = cv.GaussianBlur(grey,(13,13),15)
   # cv.imshow('gauss',gauss)
   # cv.waitKey(0)

   #Blur using blur
   blur = cv.blur(flat,(17,17))
   cv.imshow('blur',blur)
   cv.waitKey(0)

   #Use HoughCircles transform to detect circular objects
   circles = cv.HoughCircles(blur,cv.HOUGH_GRADIENT,1,36,param1=100,param2=65,minRadius=310,maxRadius=500)

   #Convert circles to integers
   circles = np.uint16(np.around(circles))

   try:
   #Draw detected circles
       for i in circles[0,:]:
           #Draw outer circle
           cv.circle(grey,(i[0],i[1]),i[2],(34,255,0),8)

           #Draw midpoint
           cv.circle(grey, (i[0], i[1]), 2, (0, 255, 0), 8)
   except:
       return None

   #show frame and wait for break
   cv.imshow('final',grey)
   cv.waitKey(0)