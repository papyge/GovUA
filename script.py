import os
import pytesseract 
import imutils
import cv2
from skimage.segmentation import clear_border


class ImageParse():
    
    def __init__(self, minAR=4, maxAR=5, debug=False):
        self.minAR = minAR
        self.maxAR = maxAR
        self.debug = debug
        


directory = "185.5.194.36"

images = os.listdir('/home/papyge/Hakathon/screenshots/185.5.194.36')

print(images)
