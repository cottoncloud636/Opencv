"""
In imaging processing, there are a lot of places need bitwise operation, S.A. masks
"""

import cv2 as cv
import numpy as np



blank = np.zeros((400, 400), dtype='uint8')
"""
1) blank.copy(): use copy() instead of directly pass in "blank" is because, we don't want to modify the blank obj, 
   we just want the copy of it and do something on this copy

2) (200, 200): position of the circle that will be placed on the canvas
3) 200: radius of the circle.

4) 255: image is of type uint8 with values ranging from 0 to 255), 255 represents white. 

5) -1: filled the circle
"""
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) #(width, height)

cv.imshow('circleWin', circle)
cv.imshow('rectangleWin', rectangle)


#************ bitwise AND: returns the intersection of images ************#
bitwiseAND = cv.bitwise_and(circle, rectangle)
cv.imshow('bitwiseANDWin', bitwiseAND)


#************ bitwise OR: overlaps the images(keeps their original shapes) ************#
bitwiseOR = cv.bitwise_or(circle, rectangle)
cv.imshow('bitwiseORDWin', bitwiseOR)


#************ bitwise XOR: returns the non-intersect regions ************#
bitwiseXOR = cv.bitwise_xor(circle, rectangle)
cv.imshow('bitwiseXORWin', bitwiseXOR)


#************ bitwise NOT: reverse the binary color. Ex: if circle is white, canvas is black, it reverse
# the color by turning circle to black, canvas to white
# ************#
bitwiseNOT = cv.bitwise_not(circle)
cv.imshow('bitwiseNOTWin', bitwiseNOT)


"""
take away: "bitwise OR" substract "bitwise XOR", we get "bitwise AND"
"""

cv.waitKey(0)
