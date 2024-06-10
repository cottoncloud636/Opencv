"""
Color spaces:
are various models and systems used to represent and interpret colors. Different color spaces provide different ways
to describe and manipulate the colors in an image. 

Some common color spaces:
- BGR (Blue, Green, Red): default color model used by OpenCV
- RGB (Red, Green, Blue): outside opencv, default mode is RGB
- GRAY (Grayscale): many color can be converted to each other, except, gray can't convert to HSV
- HSV (Hue, Saturation, Value)
- YCrCb (Luma, Chroma Blue, Chroma Red)
- YCrCb (Luma, Chroma Blue, Chroma Red)
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/deer.jpg')
cv.imshow('window', img)

#*************** BGR to grayscale ************#
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # BGR is a default color model used by OpenCV, while outside of opencv,
                                            #RGB is the default color model
cv.imshow('GrayWin', grayscale) 


#*************** HSV: represent colors that is more intuitive for human perception ************#
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsvWin', hsv) 


#*************** LAB, aka. L*A*B ************#
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB) # BGR is a default color model used by OpenCV
cv.imshow('LABWin', lab)


#*************** RGB: a default color model outside opencv ************#
# let's use matplotlib to test a color model outside opencv
#///// print(dir(plt))
#///// plt.imshow(img)
#///// plt.show()


#*************** convert BGR to RGB using opencv method ************#
bgr2rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('bgr2rgb',bgr2rgb)
# compare with using matplotlib method. Since in plt, default is RGB (which is converted internally from BGR), now I pass in
# a RGB, but internaly it still apply RGB technique again, hence it invert the RGB to BGR 
plt.imshow(bgr2rgb)
plt.show()

cv.waitKey(0) 