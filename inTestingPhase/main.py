import cv2
import numpy as np
import os
from helper import assign_emoji

img = cv2.imread("img2.jpg")

height, width = img.shape[:2]
w, h = width//5, height//5


small = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
cv2.imwrite("small.jpg", small)

out = np.zeros((h*20, w*20, 3), dtype=np.uint8)

for i in range(h):
    for j in range(w):
        color = small[i, j]
        
        heart = os.path.join("heart", assign_emoji(color) + ".jpg")

        heart_img = cv2.imread(heart)
        heart_img = cv2.resize(heart_img, (20, 20))

        start_h = i*20
        start_w = j*20
        # Compute end indices and clip them to the `out` dimensions
        end_h = min(start_h + 20, out.shape[0])
        end_w = min(start_w + 20, out.shape[1])
        
        # Resize heart_img if it exceeds bounds
        heart_img = heart_img[:end_h - start_h, :end_w - start_w]
        
        # Insert the resized heart image into the output array
        out[start_h:end_h, start_w:end_w] = heart_img

print(out.shape)
print(height, width)


# heart_img = cv2.resize(out, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)

cv2.imwrite("heart.jpg",out)
cv2.waitKey(0)
cv2.destroyAllWindows()