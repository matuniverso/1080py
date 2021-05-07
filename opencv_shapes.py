import numpy as np
import cv2 as cv

# * create a black image
img = np.zeros((512, 512, 3), np.uint8)

# * draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# * draw a green rectangle at the top-right corner of image.
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# * draw a circle inside the rectangle drawn above.
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# * draw a half ellipse at the center of the image.
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# * Show
cv.imshow("Shapes", img)
cv.waitKey(0)
