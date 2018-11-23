"""
	Demo of Dices Detection

"""
import dicesDetectection as dd
import numpy as np
import cv2

print('')
print('	 _______   ______   ______   ________        _______   ________  ________  ________   ______   ________  ______   ______   __    __')
print('	/       \\ /      | /      \\ /        |      /       \\ /        |/        |/        | /      \\ /        |/      | /      \\ /  \\  /  |')
print('	$$$$$$$  |$$$$$$/ /$$$$$$  |$$$$$$$$/       $$$$$$$  |$$$$$$$$/ $$$$$$$$/ $$$$$$$$/ /$$$$$$  |$$$$$$$$/ $$$$$$/ /$$$$$$  |$$  \\ $$ |')
print('	$$ |  $$ |  $$ |  $$ |  $$/ $$ |__          $$ |  $$ |$$ |__       $$ |   $$ |__    $$ |  $$/    $$ |     $$ |  $$ |  $$ |$$$  \\$$ |')
print('	$$ |  $$ |  $$ |  $$ |      $$    |         $$ |  $$ |$$    |      $$ |   $$    |   $$ |         $$ |     $$ |  $$ |  $$ |$$$$  $$ |')
print('	$$ |  $$ |  $$ |  $$ |   __ $$$$$/          $$ |  $$ |$$$$$/       $$ |   $$$$$/    $$ |   __    $$ |     $$ |  $$ |  $$ |$$ $$ $$ |')
print('	$$ |__$$ | _$$ |_ $$ \\__/  |$$ |_____       $$ |__$$ |$$ |_____    $$ |   $$ |_____ $$ \\__/  |   $$ |    _$$ |_ $$ \\__$$ |$$ |$$$$ |')
print('	$$    $$/ / $$   |$$    $$/ $$       |      $$    $$/ $$       |   $$ |   $$       |$$    $$/    $$ |   / $$   |$$    $$/ $$ | $$$ |')
print('	$$$$$$$/  $$$$$$/  $$$$$$/  $$$$$$$$/       $$$$$$$/  $$$$$$$$/    $$/    $$$$$$$$/  $$$$$$/     $$/    $$$$$$/  $$$$$$/  $$/   $$/')
print('')
print('                                                                                              By Jhon Esteven Fonseca & Juan Pablo Mosquera')
print('''                                                                                                             python version 2.7.13 or 3.6.x
                                                                                                                  cv2(OpenCV) version 3.4.1''')

print('')


def runDemo():

	#Variables
	images = []
	grayScale = []
	titlesGray = []
	titlesthreshed = []
	#For circles
	threshedC = []
	circles = []
	countC = []
	#For Squares
	threshedS = []
	contours = []

	kernel = dd.doKernel(1,10)

	for i in range(6):
		#Load the images
		images.append(dd.loadImage('demo_images/d'+str(i)+'.png'))
		#transform all imgages to grayScale
		grayScale.append(dd.trasform(images[i]))
		titlesGray.append('gray #%d' %i)

		threshedC.append(dd.threshBinary(grayScale[i]))
		titlesthreshed.append('threshed #%d' %i)

		threshedC[i] = dd.gaussianBlur(threshedC[i])
		threshedC[i] = cv2.morphologyEx(threshedC[i], cv2.MORPH_OPEN, kernel)
		threshedC[i] = cv2.erode(threshedC[i],kernel,iterations = 1)
		threshedC[i] = cv2.morphologyEx(threshedC[i], cv2.MORPH_CLOSE, kernel)
		threshedC[i] = dd.bilateral(threshedC[i])
		#making a copy
		threshedS.append(threshedC[i])

	for i in range(6):
		#detect circles
		circles.append(dd.detectCircles(threshedC[i]))

		#transform thresh to rgb
		threshedC[i] = dd.trasform2(threshedC[i])
		#painting the circles
		circles[i] = np.uint16(np.around(circles[i]))
		countC.append(0)

		for ii in circles[i][0,:]:
			countC[i]+=1
			# draw the outer circle
			cv2.circle(threshedC[i],(ii[0],ii[1]),ii[2],(0,255,0),8)
			# draw the center of the circl5
			cv2.circle(threshedC[i],(ii[0],ii[1]),2,(0,0,255),8)

	for i in range(6):
		print('''imagen #%d 
			cantidad de dados: %d 
			suma de los dados: %d''' % (i, len(contours), countC[i]))

	dd.multipleView(grayScale, titlesGray)
	dd.multipleView(threshedC, titlesthreshed)
	dd.multipleView(threshedS, titlesthreshed)


#execut the demo
runDemo()