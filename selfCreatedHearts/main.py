#--------------------------------Requirements--------------------------------#
import cv2
import numpy as np
import os
#----------------------------------------------------------------------------#


#---------------------------------Parameters---------------------------------#

img_path = "img2.jpg" #path for the image

saturation_scale = 1.5

heart_template_path = 'assets/heart_small.jpg' #path for heart template
heart_img_size = 40 #px Change when you changed the hearts in assets
hsize_multiple = 1 # Increse this if you wanna Zoom the hearts (not necessary)

factor_pixelation = 10 # lesser the pixelation greter the time smaller the hearts

out_rescaling = 0.5 # Increase to make out-image blurry (small size)

#----------------------------------------------------------------------------#




#----------------------------------Main Code----------------------------------#

img = cv2.imread(img_path)
heart_img = cv2.imread(heart_template_path)

# Preprocessing the images
height, width = img.shape[:2]
w, h = width//factor_pixelation, height//factor_pixelation
small = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

hsize = heart_img_size * hsize_multiple 

# Applying Saturation
hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation_scale, 0, 255)
small = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# cv2.imwrite("small.jpg", small)


out = np.zeros((h*hsize, w*hsize, 3), dtype=np.uint8)

for i in range(h):
    for j in range(w):
        color = small[i, j]
        heart = heart_img.copy()
        
        for k in range(hsize):
            for l in range(hsize):
                if heart[k][l][0] != 0:
                    heart[k][l] = color

        start_h = i*hsize
        start_w = j*hsize

        # Compute end indices and clip them to the `out` dimensions
        end_h = min(start_h + hsize, out.shape[0])
        end_w = min(start_w + hsize, out.shape[1])
        
        # Resize heart_img if it exceeds bounds
        heart = heart[:end_h - start_h, :end_w - start_w]
        
        # Insert the resized heart image into the output array
        out[start_h:end_h, start_w:end_w] = heart

# print(out.shape)
# print(height, width)

out = cv2.resize(out, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
print(out.shape)


counter = 1
base_path = 'image_outputs/out'
file_path = f"{base_path}.jpg"

# Check if the file exists and increment the counter
while os.path.exists(file_path):
    file_path = f"{base_path}_{counter}.jpg"
    counter += 1

# Save the image with the unique path
cv2.imwrite(file_path, out)
print(f"Image saved as: {file_path}")

#----------------------------------------------------------------------------#