import cv2 as cv  #use cv as a shortcut name for cv2

#read deer.jpg image, and store in "image" variable
image = cv.imread('Photos/deer.jpg')

#display image in a new window
cv.imshow('Deer', image) # (name of the window, that variable)
cv.waitKey(0) 