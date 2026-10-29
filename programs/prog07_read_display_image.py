# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 7: Read an image and display it using Python
# Put your own image in the 'data' folder and change the file name below.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../data/sample_image.jpg')   # read the image
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # OpenCV reads BGR, matplotlib needs RGB

plt.imshow(img_rgb)
plt.title('Image')
plt.axis('off')                                # hide the axes
plt.show()
