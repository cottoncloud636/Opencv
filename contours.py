# contours are boundaries of an obj, it's lines or curve that joins the continous points along the boundary of an obj
# contour vs edge: contour is used for shape analysis, obj detection and recognition.

from xml.dom import HierarchyRequestErr
import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow("img", img)

#firstly, gray the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayWindow', gray)

#secondly, find the edges of the image, here I use canny techinque
canny = cv.Canny(img, 125, 175)
cv.imshow('cannyWindow', canny)

#thirdly, find contours by using find contours method
"""
1) RETR_TREE: Retrieves all contours and reconstructs the full hierarchy of nested 
   RETR_EXTERNAL: return only the external contours
   RETR_LIST: return all contours in the image, w/o establishing any hierarchical relationships. Each contour is 
              treated independently.

2) CHAIN_APPROX_NONE: contour approximation method. It determines how the contour points are stored. stores all the 
   contour points, resulting in a large number of points for each contour.

   There are other approximation method, S.A. CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal 
   segments, and leaves only their end points. Ex: a rectangle with four points would be stored as only four points.

3) hierarchies: It contains information about the relationship between contours, S.A. which contours are nested 
   w/i others. Ex: a rectangle contains a square inside, inside the square, there is a circle, so on.
"""
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #this method returns two variables, contours and hierarchies
print(f'total {len(contours)} contours found') # total 1414 contours found

# I can blur the image first to reduce the contours
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurredImgWindow', blur)
canny1 = cv.Canny(blur, 125, 175)
cv.imshow('canny1Window', canny1)
contours1, hierarchies1 = cv.findContours(canny1, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #this method returns two variables, contours and hierarchies
print(f'total {len(contours1)} contours found after blurring') # total 239 contours found after blurring


#************** use threshold to count contours ****************#
"""
1) threshold convert image to binary form

2) 125, 255: if pixel is below 125, pixel sets to zero or blank. If above 125, it sets to white or 255.
"""
returnValue, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours2, hierarchies2 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #this method returns two variables, contours and hierarchies
print(f'total {len(contours2)} contours found using threshold') #total 642 contours found using threshold
cv.imshow('thresholdWindow', thresh)



#************** visualize contours by drawing on the image ****************#
"""
1) blank = np.zeros(img.shape, dtype = 'uint8') vs blank = np.zeros((500, 500, 3), dtype = 'uint8')
   the left one use the size of an existing image to create a blank canvas
   the right one defines the size of this blank canvas

2) -1: This indicates that all contours in the contours list should be drawn. If you wanted to draw a specific 
   contour, you would replace -1 with the index of that contour.

3) (0,0,255): color of the contours that will display

4) 1: contour lines will be 1 pixel thick. this number represent the thickness of the contour lines.
"""
# firstly, draw a blank canvas
blank = np.zeros(img.shape, dtype = 'uint8') 
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('countContourWindow', blank)


"""
take away: recommend using canny method first, then find contours using that canny image. Instead of using threshold
then find contours.
"""


cv.waitKey(0)