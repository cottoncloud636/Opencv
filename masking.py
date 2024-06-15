"""
masking: use masking to focus on the certain part of an image.
"""

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('imgWindow', img)


#!!!!!!!!!!! Noted: the mask size needs to be same as image size, hence blank used image's height and weight by using
# .shape[:2], and circleMask use the blank canvas. Other wise, it leads to error.
#!!!!!!!!!!!
blank = np.zeros(img.shape[:2], dtype='uint8')  #.shape[:2]--extract height and weight
cv.imshow('blankWin', blank)

circleMask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #(img.shape[1]//2, img.shape[0]//2)
                                        #position of the image in canvas. This place circle at the center.
cv.imshow('maskWin', circleMask)
"""
1) "maskedImg = cv.bitwise_and(img, img, mask=masking)": returns intersection of two images, using the
   "mask" rule we specify from "masking = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)"

2) Reason to pass in two "img": cv.bitwise_and function requires two images for the bitwise AND op, hence we should
   pass the same image twice if we want to apply a mask. 
"""
maskedImg = cv.bitwise_and(img, img, mask=circleMask)
cv.imshow('maskImgWin', maskedImg)


#************ create other shapes of the mask *************#
rectangle= cv.rectangle(blank.copy(), (30, 30), (280, 280), 255, -1)
cv.imshow('rectangleWin', rectangle)

createAshape = cv.bitwise_and(circleMask, rectangle)
cv.imshow('otherShapeWin', createAshape)

otherShapeMasked = cv.bitwise_and(img, img, mask=createAshape)
cv.imshow('otherShapeMaskedWin', otherShapeMasked)


cv.waitKey(0)