"""
To rescale an image or video frame 
"""

import cv2 as cv

#****************rescale image**************#
# img = cv.imread('Photos/fox.jpg') # first, read the image file
# cv.imshow('foxwindow', img) #second, display on window using imshow()
# cv.waitKey(0) #this line is necessary, if not this code, window exit automatically immediately
# # with this code, I am telling the compiler that "wait for my key press", once I press any key

"""
Noted, a video or image can't be rescaled beyond the camera resolution (ex: 1080P)
"""
def rescaleFrame (frame, scale=0.2): #pass in frame var, and set scale to 75% of original frame
    """
    1)    The shape attribute comes from NumPy, as OpenCV uses NumPy arrays to represent images and frames. When read 
    an image or a video frame using OpenCV, it is stored as a NumPy array. The shape attribute of a NumPy array 
    provides the dimensions of the array.
        For an image (or a video frame), which is typically a 3D array, shape returns a tuple of the form (height, width,
    channels):
              height: The number of rows (pixels) in the image.
              width: The number of columns (pixels) in the image.
              channels: The number of color channels (e.g., 3 for RGB images).
    """
    h = int(frame.shape[0] * scale) #convert int as the result could be a float, since pixel dimensions must be 
                                    #whole number
    w = int(frame.shape[1] * scale)
    dimension = (w, h) #Noted that w has to come first, this is how resize() is designed
    """
    1)    cv2.resize(src, dsize, dst=None, fx=0, fy=0, interpolation=cv2.INTER_LINEAR) where, 
    -- 1. src: ource image or frame
    -- 2. dsize: size of the output image. It's a tuple (width, height). 
    -- 3. dst: optional parameter that specifies the destination image. If not provided, the function returns the 
    resized image. 
    -- 4. fx, fy specify the scale factor along the x-axis and y-axis, respectively. If dsize is specified, these 
       are ignored. 
    -- 5. cv.INTER_AREA: interpolation method used to resize the image. There are a few interpolation methods, this
       cv2.INTER_AREA: Resampling using pixel area relation. This method is preferred for image shrinking as it 
       provides better results in terms of reducing moiré patterns and aliasing.
    """
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA) #call resize method and pass in these vars

# resized_img = rescaleFrame(img)
# cv.imshow('resized_fox_window', resized_img)


#**************rescale a video***************#
vc = cv.VideoCapture('Videos/figure.mp4')
if not vc.isOpened():
    print(f"Error: Could not open video file.")
    exit()
while True: 
    isTrue, frame = vc.read() 
    resized_frame = rescaleFrame(frame)
    cv.imshow('videoWindow', frame)
    cv.imshow('resizedvideowindow', resized_frame)
   

    if cv.waitKey(20) & 0xFF==ord('d'): #every frame run every 20ms, meahile wait for keyboard press, and only lower
                                        #8 bits are considered, once key "d" is pressed, break out this loop
        break

vc.release() #release videoCapture pointer
cv.destroyAllWindows() #then destroy all windows

# cv.waitKey(0)


#*********** rescale "live video", the following method will not work on "stand alone video" or image, only work on
#live video. It rescale by change resolution
#*****************#
def changeRes (w, h):
    vc.set(3, w) #3 and 4 are property identifiers. 3 represent cv.CAP_PROP_FRAME_WIDTH
    vc.set(4, h) #4 represent cv.CAP_PROP_FRAME_HEIGHT


