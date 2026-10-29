# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 8: Read an image and identify its shape

import cv2

img = cv2.imread('../data/sample_image.jpg')

print("Shape of the image:", img.shape)        # (height, width, channels)
print("Height   :", img.shape[0])
print("Width    :", img.shape[1])
print("Channels :", img.shape[2], "(3 = colour image: B, G, R)")
