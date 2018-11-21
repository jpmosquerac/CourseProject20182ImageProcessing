"""
	Demo of Dices Detection

"""
import dicesDetectection as dd
import numpy as np
import cv2

def runDemo():

	#Variables
	images = []

	grayScale = []
	titlesGray = []

	threshed = []
	titlesThreshed = []

	circles = []

	kernel = dd.doKernel(1,10)

	for i in range(6):
		#Load the images
		images.append(dd.loadImage('demo_images/d'+str(i)+'.png'))
		#transform all imgages to grayScale
		grayScale.append(dd.trasform(images[i]))
		titlesGray.append('gray d'+str(i))

		threshed.append(dd.threshBinary(grayScale[i]))
		titlesThreshed.append('threshed d'+str(i))

		threshed[i] = dd.gaussianBlur(threshed[i])
		threshed[i] = cv2.morphologyEx(threshed[i], cv2.MORPH_OPEN, kernel)
		threshed[i] = cv2.erode(threshed[i],kernel,iterations = 1)
		threshed[i] = cv2.morphologyEx(threshed[i], cv2.MORPH_CLOSE, kernel)
		threshed[i] = dd.bilateral(threshed[i])

		
		circles.append(cv2.HoughCircles(threshed[i],cv2.HOUGH_GRADIENT,2,38,
                            param1=200,param2=60,minRadius=3,maxRadius=50))

		threshed[i] = dd.trasform2(threshed[i])

		circles[i] = np.uint16(np.around(circles[i]))
		for ii in circles[i][0,:]:
		    # draw the outer circle
		    cv2.circle(threshed[i],(ii[0],ii[1]),ii[2],(0,255,0),8)
		    # draw the center of the circl5
		    cv2.circle(threshed[i],(ii[0],ii[1]),2,(0,0,255),8)

		#cv2.imshow('detected circles',cimg)
		
	dd.multipleView(grayScale, titlesGray)
	dd.multipleView(threshed, titlesThreshed)

#execut the demo
runDemo()