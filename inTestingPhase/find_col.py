## RUN THE FILES ONLY TO RETEST OTW COLOR_DATA WILL GET DISTURBED
#-----------------------------$--------------------------------------#
# import cv2
# import numpy as np


# def beg(i):
#     j = i-25
#     return str(j)

# def end(i):
#     if i == 225:
#         return '255'
#     else:
#         j = i+24
#         return str(j)


# img = np.zeros((480, 480, 3), dtype=np.uint8)
# values = [25, 75, 125, 175, 225]
# colors = ["black", "blue", "brown","green", "grey", "lblue", "orange", "pink", "purple", "red", "white", "yellow"]
# with open("colordata.txt", "w", newline="") as file:
#     for i in values:
#         for j in values:
#             for k in values:                
#                 color = (i, j, k)
#                 height = 1080
#                 width = 600
#                 image = np.full((height, width, 3), color, dtype=np.uint8)
#                 cv2.imshow("type the color in the terminal" , image)
#                 cv2.waitKey(2)
#                 text = ""
#                 while text not in colors:
#                     text = input("Enter the Color seen: ").lower().strip()

#                 file.write("if " + beg(i) + "<b<" + end(i) + " and " + beg(j) + "<g<" + end(j) + " and " + beg(k) + "<r<" + end(k) + ":\n")
#                 file.write("    return " + "\'"+text + "\'" + "\n")

#--------------------------------------------------------------------------#
            

            
