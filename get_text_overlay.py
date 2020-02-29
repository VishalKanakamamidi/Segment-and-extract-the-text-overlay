# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np
import os

def getTextOverlay(img):
	# Write your code here for output
    
    rows,cols,k = img.shape 				#Changing all the pixels whose value is not black to white
    for i in range(rows):
    	for j in range(cols):
    		if(img[i,j][0]>5 and img[i,j][1]>5 and img[i,j][2]>5 ):
    			img[i,j][0] = 255
    			img[i,j][1] = 255
    			img[i,j][2] = 255
    		else:
    			img[i,j][0] = 0
    			img[i,j][1] = 0
    			img[i,j][2] = 0
    cv2.imwrite("test.png",img)
    img = cv2.imread("test.png",0)		# changing the pixel values to grayscale
    os.remove("test.png")
    rows,cols = img.shape
    for i in range(rows):				# cropping the rectangle in which the text lies and removing everything else
    	for j in range(cols):
    		if(j< 263 or j>2341):
    			img[i,j]=255
    		if(i>1153 or i<219):
    			img[i,j]=255
    output = img
    return output

if __name__ == '__main__':
	image = cv2.imread('simpsons_frame0.png')
	output = getTextOverlay(image)
	cv2.imwrite('simpons_text.png', output)
#####################

