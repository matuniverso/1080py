import cv2

# * Read
img = cv2.imread("assets/snake.jpg", cv2.IMREAD_GRAYSCALE)

# * Resize to half width and half height
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# * Rotate
# img = cv2.rotate(img, cv2.ROTATE_180)

# * Blur
# img = cv2.blur(img, (10, 10))

# * Show
cv2.imshow("Snake", img)
cv2.waitKey(0)

# * Download
cv2.imwrite("assets/snake_grayscale.jpg", img)
