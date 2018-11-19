"""
	Demo of Dices Detection

"""
import dicesDetectection as dd
import numpy as np
import cv2

def runDemo():

	#Variables
	images = []
	titles = []

	grayScale = []
	titlesGray = []

	filtered = []
	titlesFiltered = []

	threshed = []
	titlesThreshed = []

	contours = []
	titlesContours = []

	circles = []

	kernel = dd.doKernel(1,20)

	for i in range(6):
		#Load the images
		images.append(dd.loadImage('demo_images/d'+str(i)+'.png'))
		titles.append('img: d'+str(i))
		#transform all imgages to grayScale
		grayScale.append(dd.trasform(images[i]))
		titlesGray.append('gray: d'+str(i))
		#applying GaussianBlur filter
		filtered.append(dd.gaussianBlur(grayScale[i]))
		titlesFiltered.append('GaussianBlur: d'+str(i))

		filtered[i]=dd.blur(filtered[i])
		filtered[i]=dd.gaussianBlur(filtered[i])
		#adaptative gaussian thresholding
		threshed.append(dd.adaptativeGaussianThresholdingInv(filtered[i]))
		titlesThreshed.append('threshed: d'+str(i))

		#OPENNING
		threshed[i] = dd.morphologyOpen(threshed[i], kernel)

	dd.multipleView(images, titles)
	dd.multipleView(grayScale, titlesGray)
	dd.multipleView(filtered, titlesFiltered)
	dd.multipleView(threshed, titlesThreshed)

#execut the demo
runDemo()