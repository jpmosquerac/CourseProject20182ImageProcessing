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

	threshedC = []
	titlesthreshedC = []

	threshedCS = []
	titlesthreshedCS = []

	circles = []

	kernel = dd.doKernel(1,10)

	for i in range(6):
		#Load the images
		images.append(dd.loadImage('demo_images/d'+str(i)+'.png'))
		#transform all imgages to grayScale
		grayScale.append(dd.trasform(images[i]))
		titlesGray.append('gray d'+str(i))

		threshedC.append(dd.threshBinary(grayScale[i]))
		titlesthreshedC.append('threshedC d'+str(i))

		threshedC[i] = dd.gaussianBlur(threshedC[i])
		threshedC[i] = cv2.morphologyEx(threshedC[i], cv2.MORPH_OPEN, kernel)
		threshedC[i] = cv2.erode(threshedC[i],kernel,iterations = 1)
		threshedC[i] = cv2.morphologyEx(threshedC[i], cv2.MORPH_CLOSE, kernel)
		threshedC[i] = dd.bilateral(threshedC[i])

		#making a copy
		threshedS = threshedC
		titlesthreshedS = titlesthreshedC

		#detect circles
		circles.append(dd.detectCircles(threshedC[i]))
		#transform thresh to rgb
		threshedC[i] = dd.trasform2(threshedC[i])

	for i in range(6):
		#painting the circles
		circles[i] = np.uint16(np.around(circles[i]))
		for ii in circles[i][0,:]:
		    # draw the outer circle
		    cv2.circle(threshedC[i],(ii[0],ii[1]),ii[2],(0,255,0),8)
		    # draw the center of the circl5
		    cv2.circle(threshedC[i],(ii[0],ii[1]),2,(0,0,255),8)
		
	dd.multipleView(grayScale, titlesGray)
	dd.multipleView(threshedC, titlesthreshedC)

#execut the demo
runDemo()