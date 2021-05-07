import numpy as np
import cv2 as cv


def nothing(x):
    pass


# * Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# * create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord("q"):
        break
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    img[:] = [b, g, r]

# * Destroy window
cv.destroyAllWindows()
