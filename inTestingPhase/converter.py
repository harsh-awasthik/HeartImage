import cv2
import os

directory = "heart"
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

for i in files:
    img_path = os.path.join(directory, i)
    img = cv2.imread(img_path)

    img = cv2.resize(img, (20, 20))
    cv2.imwrite(img_path, img)
    