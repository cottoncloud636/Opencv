"""
 Color channels: refer to Red, Green, Blue...
 In opencv, we can split or merge these channels
"""

import cv2 as cv
import numpy as np

img = cv.imread('Photos/nature1.jpg')
cv.imshow('window', img)


#*************** Split channels ******************#
blue, green, red = cv.split(img)
# if an img is split to blue, then the blue part will look very light visually, same as for other two colors
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape) # output: (296, 474, 3) -- 3: # of color channels
print(blue.shape) # output: (296, 474) -- the undering num in this tuple at last position is 1
print(green.shape) # output: (296, 474)
print(red.shape) # output: (296, 474)


#*************** Merge channels ******************#
merged = cv.merge([blue, green, red])
cv.imshow("mergedWin", merged)


#*************** restruct an image on a blank canvas******************#
# draw a blank canvas, we need to use numpy
blank = np.zeros(img.shape[:2], dtype = 'uint8') # shape attribute provides the dimensions in the order 
                                   # (height, width, channels). shape[:2]: extract the first two elements: height, 
                                   # weight
b = cv.merge([blue, blank, blank]) # set the green and red part to black (since we pass in blank image, by default the color is black)
g = cv.merge([blank, green, blank]) 
r = cv.merge([blank, blank, red])
cv.imshow('BlueOnly', b)
cv.imshow('GreenOnly', g)
cv.imshow('RedOnly', r)

cv.waitKey(0)