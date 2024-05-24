import cv2 as cv  #use cv as a shortcut name for cv2

#read deer.jpg image, and store in "image" variable
# image = cv.imread('Photos/deer.jpg')

#************display image in a new window**************#
# cv.imshow('Deer', image) # (name of the window, that variable)
# cv.waitKey(0) #just a keyboard event



#************display videoe in a new window**************#
"""
1) videoCapture is an "instance" of VideoCapture (a class)
2) para can be int, which can represent camera No.
3) A video is a sequence of images displayed rapidly, so for machine,
                    #   when it displays, it displays frame by frame
"""
vc = cv.VideoCapture('Videos/figure.mp4')
if not vc.isOpened():
    print(f"Error: Could not open video file .")
    exit()
while True: #since video display frame by frame, use a while loop to traverse each frame
    isTrue, frame = vc.read() #after each read, it returns a boolean isTrue, and 
                                        #the frame it captures, and put it in frame variable
    cv.imshow('videoWindow', frame) # display video uses "imshow" method, unlike imread which is to read img file
    """
    1) If a key is pressed within the delay period, cv.waitKey returns the ASCII value of the 
    key. If no key is pressed, it returns -1.

    2) cv.waitKey(20): 20ms is a frame display rate, meanwhile, cv is also watching a key
    press and once key is pressed, video exit or pause.

    3) The bitwise AND operation with 0xFF (which is 255 in decimal) is used to ensure that only the lower 8 bits of
    the result are considered. This is important for compatibility and consistency across different systems and 
    platforms. 
    A byte consists of 8 bits, and can represent values from 0 to 255 in decimal (or 0x00 to 0xFF in hexadecimal).
    The lower 8 bits refer to the least significant 8 bits in a binary number. Ex, the 16-bit binary number
    0b1010101111001101, High bits:  10101011, Low bits: 11001101. The low bits are the lower 8 bits, here the low bits
    equivalent to 0xCD in hexadecimal or 205 in decimal.
    The lower 8 bits are where the ASCII key codes are stored, and cv.waitKey() function might return more 
    information than just the key code, By applying the mask 0xFF, we extract these 8 bits and exclude other bits, 
    ensuring that we are working with the correct key code.

    4) The ord() function returns the ASCII value of the given character. Ex: ord('d') converts char 'd' to its 
    ASCII value, which is 100.

    """
    if cv.waitKey(20) & 0xFF==ord('d'): #every frame run every 20ms, meahile wait for keyboard press, and only lower
                                        #8 bits are considered, once key "d" is pressed, break out this loop
        break

vc.release() #release videoCapture pointer
cv.destroyAllWindows() #then destroy all windows



