"""
	Universidad Autónoma de Colombia
	Image Processing
	Course Project – 2018-2
	
	Dices Detection
	Juan Pablo Mosquera - Jhon Estiven Fonseca

"""

import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

#Function to load image
def loadImage(imgPath):
	img = cv2.imread(imgPath)
	return img

#GrayScale transform 
def trasform(img):
	grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return grayScale

#Borders detection filters
	# gaussianBlur filter
def gaussianBlur(img):
	gaussianBlurM = cv2.GaussianBlur(img,(5,5),0)
	return gaussianBlurM

	# medianBlur filter
def medianBlur(img):
	medianBlurM = cv2.medianBlur(img,5)
	return medianBlurM

	# blur filter
def blur(img):
	blurM = cv2.blur(img,(5,5))
	return blurM

	#bilateral filter
def bilateral(img):
	bilateralM = cv2.bilateralFilter(testB,9,75,75)
	return bilateralM

	#personalized filter
def personalized(img, kernel):
	dst = cv2.filter2D(img,-1,kernel)
	return dst

#Objects detection filters
	#Canny
def canny(grayScale):
	cannyM = cv2.Canny(grayScale,50,500)
	return cannyM

	#Laplacian
def laplacian(grayScale):
	laplacianM = np.uint8(np.absolute(cv2.Laplacian(imgG, cv2.CV_64F)))
	return laplacianM

#Filter for borders menu
def filter_menu(argument):
    switcher = {
        1: gaussianBlur,
        2: medianBlur,
        3: blur,
        4: bilateral,
        5: personalized
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid option")
    # Execute the function
    return func

# #Filter for objects menu
def filter_menu2(argument):
	switcher = {
        1: canny,
        2: laplacian
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid option")
    # Execute the function
    return func






