"""
gradients are used to represent the change in intensity or color in an image
"""
import cv2 as cv
import numpy as np

img = cv.imread('Photos/fox.jpg')
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#************ Laplacian *************#
"""
1) The Laplacian operator is a second-order derivative operator used in image processing and computer
   vision to highlight regions of rapid intensity change(the gradient), which often correspond to edges. It is 
   particularly useful for edge detection and feature extraction.

2) First-order derivative of an image measures the rate of change of pixel intensities. It highlights
   areas where there is a significant change in intensity, such as edges.
   Second-order derivative measures the rate at which the first-order derivative changes. It captures
   information about the curvature of the image intensity function.

3) cv.CV_64F: specifies the desired depth (data type) of the output image. CV_64F indicates that the
   output image will have a 64-bit floating-point depth. This is important because the Laplacian 
   computation can result in negative values, and using a floating-point representation helps 
   preserve these values before further processing.

4) np.uint8: this function converts the image data to an unsigned 8-bit integer format. This format 
   is commonly used for image display and storage, where pixel values range from 0 to 255. Might lose
   some precision, but is necessary for compatibility with standard image display functions.
"""
laplacian = cv.Laplacian(gray, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv.imshow('Laplacian', laplacian)


#************ Sobel *************#
"""
1) Sobel computes the gradient of the image intensity at each pixel, in two directions, x and y, giving the 
  direction of the largest possible increase in intensity from light to dark and the rate of change in that 
  direction. The Sobel operator uses two 3x3 convolution kernels. One kernel estimates the gradient in the 
  x-direction (horizontal changes), and the other estimates the gradient in the y-direction (vertical 
  changes).
  
2) soble method structure: sobel(src, ddepth, dx, dy), dx: The order of the derivative in the x direction.
   dx=1 means the first derivative with respect to x. dx=0 means no derivation with respect to y.

3) Canny is a multi-stage method, one of the stage is the sobel.
"""
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelX, sobelY)
#compare with canny edge detector
canny = cv.Canny(gray, 125, 175)
cv.imshow('sobelX', sobelX)
cv.imshow('sobelY', sobelY)
cv.imshow('combinedSobel', combined_sobel)
cv.imshow("Canny", canny)


cv.waitKey(0)