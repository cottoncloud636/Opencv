"""
Thresholding (or binarizing) in OpenCV is a process used to convert a grayscale image into a binary image. In a 
binary image, each pixel is either black(0) or white(255). This is achieved by applying a threshold value to the 
pixel intensities of the grayscale image.

A general technique: set up a threshold, if value is less than threshold, set it to 0, else set it to 255
"""



import cv2 as cv
# import matplotlib.pyplot as plt #used for creating plots and visualizations.
# import numpy as np


#************ Simple thresholding ***************#
"""
1) threshold, thresh =cv.threshold(gray, 150, 255, cv.THRESH_BINARY):
   - pass in this gray image
   - 150: a threshold, if the pixel in this gray image is over 150, then set it to 255, else set it to 0. 
   - 255: pass in here as a limit
   - cv.THRESH_BINARY: Type of thresholding to be applied. cv.THRESH_BINARY means if the pixel value is greater than
     the threshold (150), it is set to the maximum value (255); otherwise, it is set to 0.
   - threshold and thresh are two return values. "threshold": This is the threshold value that was used (which will 
     be 150 in this case). It's often ignored but can be useful if the threshold is computed automatically (e.g., in
     Otsu's method). "thresh": The output binary image resulting from the thresholding operation.

"""
img = cv.imread('Photos/cat.jpg')
cv.imshow('imgWindow', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, threshImg = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshGrayWin', threshImg)
# the following is the "inverse" image of the above
threshold, inverseThreshImg = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # simply use cv.THRESH_BINARY_INV
                                     # method, it sets any pixel below 150 to 255, else to 0, the exact opposite
                                     # as cv.THRESH_BINARY method
cv.imshow('InverseThreshGrayWin', inverseThreshImg)


#************ Adaptive thresholding:
# The downside of simple thresholding is that we need to manually set the threshold, here the adaptive thresholding
# let the machine set the threshold to be more adaptive to the image
#***************#
"""
1) How does adaptive thresholding work: define a kernal size in the image, in this case 11x11, opencv then 
   computes the mean of these pixels, and find the optimal threshold value for that part, then the kernal 
   slides up, down, left, right, eventually spreads over every part of the image.

2) 255: the limit of the pixel can reach in an output binary image

3) cv.ADAPTIVE_THRESH_MEAN_C: means the threshold value is the mean of the neighborhood area minus the 
   constant C. Here the C is "3", which is the constant C that is subtracted from the mean or weighted mean
   calculated. It helps fine-tune the thresholding process.

4) 11: The size of the neighborhood area (a block size) used to calculate the threshold for a pixel. It must
   be an odd number (e.g., 3, 5, 7, 9, 11, etc.).
"""
# There are other method to calculate the pixel, such as cv.ADAPTIVE_THRESH_GAUSSIAN_C instead of 
# cv.ADAPTIVE_THRESH_MEAN_C, the latter calculate the mean, the former calculate pixel using Gaussian method.
# Gaussian method add weight to each pixel value, then compute the mean of these pixels.
adaptiveThreshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptiveThresholdWin', adaptiveThreshold)


cv.waitKey(0)