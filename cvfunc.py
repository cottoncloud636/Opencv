# this file demonstrate common functions in opencv used in computer vision

from configparser import Interpolation
import cv2 as cv

img = cv.imread('Photos/panda.jpg')
cv.imshow("ImgWindow", img)

#*********** convert image to gray scale ************#
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayImgWindow", gray)


#*********** blur an image ************#
"""
1) There are a lot of blur techniques
2) (7,7): tuple represents the size of the Gaussian kernel. The Gaussian kernel is the matrix used to perform the 
    convolution the higher the num, the blurer the images are.
3) When applying a filter, pixels near the border need to be handled in some way because the kernel may extend 
   beyond the image edges. cv.BORDER_DEFAULT uses the default border mode in OpenCV, which is typically equivalent 
   to cv.BORDER_REFLECT_101. This means the border pixels are reflected with slight modifications.
"""
blurredImg = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurredImgWindow', blurredImg)


#*********** Edge cascade: find the edge of an image (image will display in black and white with image 
# represented by edges
#************
"""
1) There are a lot of Edge cascade techniques, Canny is one of them
2) 125 (lower threshold): The lower threshold for the hysteresis(滞后效应) procedure. Pixel values below this 
   threshold are considered non-edges.
   175 (upper threshold): The upper threshold for the hysteresis procedure. Pixel values above this threshold are 
   considered strong edges.
"""
canny = cv.Canny(img, 125, 175) #to reduce the edges, we can first apply blur technique on an image, then edge cascade
cv.imshow('CannyWindow', canny)


#*********** dilate an image: to enlarge the boundaries of an object. To removing small noise from images.
# to Bridging gaps between object parts.
#************#
"""
1) (7,7): A (7,7) kernel means that the kernel is 7 pixels wide and 7 pixels tall.
2) iterations=3: means the dilation operation will be applied three times sequentially. Each iteration will further 
   dilate the result of the previous iteration.
"""
dilatedImg = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('DialatedWindow', dilatedImg)


#*********** erode an image: to shrink the boundaries of an object. ************#
erodedImg = cv.erode(dilatedImg, (7,7), iterations=3)
cv.imshow('ErodedWindow', erodedImg)


#*********** resize an image: also mentioned in rescale.py, here this resize we use another way ************#
"""
1) (500, 500): image size
2) INTER_AREA: a method used to shrink an image. 
   INTER_LINEAR: a method used to enlarge an image.
   INTER_CUBIC: a method also used to enlarge an image. This method is slowest but provides high quality image.
"""
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('ResizedWindow', resized)


#*********** crop an image *************#
"""
1) Theory of crop an image: image consists 2D arrays, by slicing the array, we can select portion of an image based 
   on the pixel values. 
2) [50:200, 300:400]: 50 is the starting row index (inclusive). 200 is the ending row index (exclusive). Means rows 
   50 through 199 are selected.
   300 is the starting column index (inclusive). 400 is the ending column index (exclusive). Means columns 200 
   through 399 are selected.
"""
cropped = img[50:200, 300:400]
cv.imshow('CropWindow', cropped)


cv.waitKey(0)