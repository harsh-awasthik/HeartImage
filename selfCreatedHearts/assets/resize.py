import cv2
import numpy as np

img = cv2.imread("6.png")
img = cv2.resize(img, (40, 40))

height, width = img.shape[:2]
zero = np.zeros(3)
for h in range(height):
    for w in range(width):
        if img[h][w].all() != zero.all():
            img[h][w] = np.array([255, 255, 255])
        
cv2.imwrite("heart_small.jpg", img)
