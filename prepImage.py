import cv2
import numpy as np
import util
from contours import Contours

class Image:
    def __init__(self, image):
        self.image = image

    def toGreyscale(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh

    def toInvertedGreyscale(self):
        img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret, im = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
        return im

    def contoursOfColor(self):
        imghsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([155,25,0])
        upper_red = np.array([179,255,255])
        mask_red = cv2.inRange(imghsv, lower_red, upper_red)
        contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        im = np.copy(self.image)
        cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        return im

    def reduceImageToColor(self):
        result = self.image.copy()
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower = np.array([155,25,0])
        upper = np.array([179,255,255])
        mask = cv2.inRange(image, lower, upper)
        result = cv2.bitwise_and(result, result, mask=mask)
        return result
    
    def findContours(self, preppedImage):
        contours, hierarchy  = cv2.findContours(preppedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contoursObj = Contours(self.image, contours)
        return contoursObj

    def drawContours(self, contours):
        img = cv2.drawContours(self.image, contours, -1, (70,7,80), 2)
        return img
