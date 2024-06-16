"""
Histogram allows a visualization of the distribution of pixel intensity of an image
Histogram can be used on both grayscale and RGB image
"""

import cv2 as cv
import matplotlib.pyplot as plt #used for creating plots and visualizations.
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('imgWindow', img)


#************* display historgram on an entire image **************#
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
"""
1) gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) : 
   - [gray]: gray is the image that I want to process, allows pass in multiple images at the same time
   - [0]: channel index, 0 indicates the first channel, which is the only channel in a grayscale image.
   - None: The mask is none, means the histogram is calculated for the entire image. Pass in a mask, to specify if I
     want to compute histogram on a specific part of an image
   - [256]: The number of bins. Here, 256 bins represent the range of possible pixel values (0-255).
   - [0, 256]: The range of pixel values to consider. 0 to 256 covers all possible values for an 8-bit image.

2) plt.figure(): Creates a new figure for plotting. Plot, in the context of data visualization, is a graphical representation of data. 

3) plt.plot(gray_hist): gray_hist contains the frequency of each pixel intensity.

4) plt.xlim([0, 256]): Sets the limits of the x-axis from 0 to 256, covering all possible pixel values.
"""
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('Grayscale image histogram')
# plt.xlabel('Bins')  # the label for x axis
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()



#************* display historgram on an image with masking **************#
# blank = np.zeros(img.shape[:2], dtype='uint8')
# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('maskWin', mask)

# gray_hist_mask = cv.calcHist([gray], [0], circle, [256], [0,256])
# plt.figure()
# plt.title('Grayscale masked image histogram')
# plt.xlabel('Bins')  # the label for x axis
# plt.ylabel('# of pixels')
# plt.plot(gray_hist_mask)
# plt.xlim([0, 256])
# plt.show()


#************* display historgram on each color from an image **************#
"""
1) colors = ('b','g','r'): The colors ('b', 'g', 'r') are understood by Matplotlib, not OpenCV. The color parameter 
   in the plt.plot function is used by Matplotlib to set the color of the plotted line. These color codes are 
   standard shorthand notations in Matplotlib for blue, green, and red, respectively.

2) for i, col in enumerate(colors): 
   - The "enumerate" function: 
        ### colors = ['red', 'green', 'blue']
        ### for index, color in enumerate(colors):
        ### print(index, color)
        # Output: 0 red
                  1 green
                  2 blue
    If I don't specify the index start, by default is 0.
    I can also specify the index start:
        ### colors = ['red', 'green', 'blue']
        ### for index, color in enumerate(colors, start=1):
        ### print(index, color)
        # Output: 1 red
                  2 green
                  3 blue
    
    - hence, i refers to the index, col refers to the value

1) The "color" parameter is a predefined keyword argument in the Matplotlib plot function that specifies the color
    of the line in the plot. 
  has multiple channels, hence pass in i
"""
# plt.figure()
# plt.title('Color histogram for an image')
# plt.xlabel('Bins')  # the label for x axis
# plt.ylabel('# of pixels')
# colors = ('b','g','r')
# for i, col in enumerate(colors):
#     color_hist = cv.calcHist([img], [i], None, [256], [0,256])
#     plt.plot(color_hist, color=col)
#     plt.xlim([0, 256])
# plt.show()


#************* display historgram on each color from an image with masking **************#
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(img, img, mask=circle) # the sole purpose of this is to visualize the "mask"
cv.imshow('maskWin', mask)

plt.figure()
plt.title('Color histogram for an image with masking')
plt.xlabel('Bins')  # the label for x axis
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], circle, [256], [0,256]) # denote: I want to calculate histogram on the 
                                        #original image with the circle as a mask. Will not use "mask" from line 103
                                        #to replace "circle".
    plt.plot(color_hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)