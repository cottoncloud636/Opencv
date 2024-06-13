"""
1) Image smoothing technique 1: blurring. It sounds contradictory, but image smoothing does not mean to make the image
clearer, but it simply improve the image by such softening the edge, reduce the noise, etc.
"""

import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('imgWindow', img)

#********** Averaging: a blurring technique ***********#
# System defines a kernal window of a user specified size, S.A. (3,3),  compute this kernal window's
# center value using average of its surrounding pixels, This process is repeated for every 
# pixel in the image, resulting in a blurred effect. The higher the kernal window size, the
# more blur the image would be.
average = cv.blur(img, (3,3))
cv.imshow('averageBlurWin', average)


#********** Gaussian blur **************#
# Same as averaging tech:nique, except each surrouding pixel is given a particular weight. The average came from 
# these weight. Gaussian blur image is less blur than using averaging technique, but it's more natural for human eye
gaussianBlur = cv.GaussianBlur(img, (3,3), 0) # 0: A standard deviation (σ) in the X direction. A value of
                                          # 0 indicates that the standard deviation is calculated based on the kernel
                                          # size. If a different value is specified, it overrides the automatic 
                                          # calculation and uses the provided standard deviation for the Gaussian 
                                          # function.
cv.imshow('gaussianBlurWin', gaussianBlur)



#********** Median blur: finds the median of surrounding pixels. Median is more effective than averaging technique
# **************#
medianBlur = cv.medianBlur(img, 3) # opencv automatically recongnize it's a 3x3 kernal by this single integer 3
cv.imshow('medianBlurWin', medianBlur)


#********** Bilateral blur: the most effective and used on advanced cv project, blur the image but retains its edges
"""
1) Filter sigma: it's the standard deviation used in Gaussian-based filtering methods. It determines the extent to 
   which the filter smooths the image by affecting how much influence neighboring pixels have on the computation of 
   the new pixel value.

2) 5: The diameter of each pixel neighborhood used during filtering. The larger the diameter, the more pixels around 
each pixel are used to compute the result.

3) 15 (sigmaColor): This is the filter sigma in the color space. A larger value means that farther colors within the
   pixel neighborhood will be mixed together, resulting in larger areas of semi-equal color.

4) 15 (sigmaSpace): This is the filter sigma in the coordinate space. A larger value means that farther pixels will 
   influence each other as long as their colors are close enough (as determined by sigmaColor).
"""

bilateralBlur = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateralWin', bilateralBlur)


cv.waitKey(0)
