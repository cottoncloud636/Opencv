import cv2 as cv
import numpy as np #Numerical computations and matrix operations.

img = cv.imread('Photos/leopard.jpg')
cv.imshow('leowindow', img)

"""
1)   np.zeros(): a function from the NumPy library that creates an array filled with "zeros". Prototype of this func:
numpy.zeros(shape, dtype=float, order='C', *, like=None)

2)   (500, 500): This tuple specifies the shape of the array, which in this case is 500 rows by 500 columns

3)   (500, 500, 3): it specifies that the image has three color channels (Red, Green, and Blue : RGB)allowing the 
representation of a full-color image.

4)   dtype='uint8': This specifies the data type of the elements in the array. uint8 stands for "unsigned 8-bit 
integer," which means each element of the array can hold an integer value from 0 to 255. This is a common data type 
for images, where each pixel's intensity is represented by a value between 0 (black) and 255 (white). Since we 
specify the function zeros(), hence the image will be all black.
"""
# blankImg = np.zeros((500, 500, 3), dtype = 'uint8')
blankImg1 = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('blankwindow', blankImg)
"""
1)   ":" is a slicing operator that means "select everything" along that axis. Here, it means all rows and all 
columns.

2) [0, 0, 225]: 0 for the Blue channel. 0 for the Green channel. 225 for the Red channel.
"""
#*************** Paint the window in red ***************#
# blankImg[:] = 0,0,225 
# cv.imshow('RedWindow', blankImg)
#*******************#

#*************** Paint the window by different color by specify the pixel **************#
blankImg1[200:300, 300:400]=0,0,225 
cv.imshow('Multicolorwindow', blankImg1)
#*******************#

"""
1)   (0,0),(250,250): the rectangle will from top left corner(at position 0,0) to right bottom corner (at position
250,250)

2)   (0,255,0): Blue=0, Green=255, Red=0
"""
#*************** Draw a rectangle **************#
# cv.rectangle(blankImg1, (0,0), (250,250), (0,255,0),thickness=6) ---- #a rectangle frame
                        # ---- (250,250) can also be written as (blankImg1.shape[1]//2, blankImg1.shape[0]//2)
cv.rectangle(blankImg1, (0,0), (250,500), (0,255,0),thickness=cv.FILLED) # fill the rectangle frame w. green color
                                                                         # same as "thickness=-1"
cv.imshow('Recwindow', blankImg1)


#*************** Draw a circle **************#
cv.circle(blankImg1, (blankImg1.shape[1]//2, blankImg1.shape[0]//2), 40, (250, 0, 0), thickness=-1) 
                    # tuple (blankImg1.shape[1]//2, blankImg1.shape[0]//2) is the position of the image on the canvas
                    # 40: specifies the radius of the circle in pixels.
cv.imshow('CircleWindow', blankImg1)


#*************** Draw a line **************#
cv.line(blankImg1, (0,0), (blankImg1.shape[1]//2, blankImg1.shape[0]//2), (0,0,0), thickness=8)
                                    # (0,0), (blankImg1.shape[1]//2, blankImg1.shape[0]//2) : lines draws from left
                                    #    top corner to the center of the canvas
cv.imshow('LineWindow', blankImg1)


#*************** Write text on an image **************#
"""
1) (0, 250) : position of the text horizontally, from left to right
2) 1.0 : size of the text
3) 2 : thickness of the text strokes in pixel
"""
cv.putText(blankImg1, 'Hello World, this is Natasha', (0, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), 2)
cv.imshow("TextWindow", blankImg1)

cv.waitKey(0)

