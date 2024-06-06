# translate, rotate, flip image

import cv2 as cv
import numpy as np

img = cv.imread('Photos/fox.jpg')
cv.imshow("img", img)

#************* image translation: 
# a geometric transformation that moves every point of an image by a certain distance in a specified direction. 
# This transformation shifts the entire image horizontally, vertically, or both, without altering its orientation, 
# size, or shape.
#*************
"""
1) np.float32: is used to ensure the matrix elements are in the float32 data type, which is required by OpenCV for 
   transformation matrices.

2) The matrix [[1, 0, x], [0, 1, y]] is a 2x3 matrix used for translation.
   [1, 0, x]: 
    - 1: This means the x-coordinate of the point is multiplied by 1, move along horizontal direction,
                (no scaling or rotation is applied). 
    - 0: This means the y-coordinate does not affect the new x-coordinate (no shearing -- crop).
    - x is the translation component. It adds tx to the x-coordinate, shifting the point horizontally by tx units.

   [0, 1, y]: 
    - 1: This means the y-coordinate of the point is multiplied by 1, move along vertical direction,
                (no scaling or rotation is applied). 
    - 0: This means the x-coordinate does not affect the new x-coordinate (no shearing -- crop).
    - y is the translation component. It adds ty to the y-coordinate, shifting the point vertically by ty units.

3) shape[1]: width. shape[0]: height

4) use -x : shift left
   use x: shift right
   use -y: shift up
   use y: shift down
"""
def translation(img, x, y): #pass in an img and move it along x and y axis
    transMatrix = np.float32([[1,0,x],[0,1,y]])# need a canvas to perform the translation, which is esentially a matrix 
    dimention = (img.shape[1], img.shape[0])# need to have img's original height and width
    return cv.warpAffine(img, transMatrix, dimention)

transResult = translation(img, 100, 100) #shift right down
cv.imshow('transWindow', transResult)



#************* Rotate an image*************#
"""
1) rotatePoint: a tuple (x, y) that specifies the coordinates of the point around which the image will be rotated. 
   aka. the pivot point. If rotatePoint is None, the code sets it to the center of the image by default.

2) getRotationMatrix2D(rotatePoint, angle, 1.0): 
   - This function creates a 2x3 rotation matrix for rotating an image around a specified point by a certain angle.
   - 1.0: scaling factor. Means enlarge or shrink the image
"""
def rotate(img, angle, rotatePoint=None):
    (height, width) = img.shape[:2] # get the img's height and width
    if rotatePoint is None:
        rotatePoint = (height//2, width//2) 
    rotateMatrix = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    dimension = (width, height) # It's better to specify the dimensions in the order (width, height) always
    return cv.warpAffine(img, rotateMatrix, dimension)

rotateResult = rotate(img, 45) # 1) rotate image counter-clockwise
                           # 2) When apply angle, opencv actually creates a black triangle, make an illusion that 
                           #    the image rotates, hence in "rotateResult2" img, the img looks like a parallelogram
                           #    that is because opencv applies another triangle on top of the previous triangles

rotateResult1 = rotate(img, -45) #rotate image clockwise

rotateResult2 = rotate(rotateResult1, -45) 

cv.imshow('counterRotateWindow', rotateResult)
cv.imshow('clockRotateWindow', rotateResult1)
cv.imshow('furtherRotateWindow', rotateResult2)


#************* Flip an image*************#
flipped = cv.flip(img, 1) #flip code can only be -1, 0, 1. Where 0: flip img vertically, over the x axis. 
                # Where 1: flip img horizontally, over y axis. -- mirror effect compared with original img.
                # Where -1: flip img both horizontally and vertically
cv.imshow('flipWindow', flipped)

cv.waitKey(0)