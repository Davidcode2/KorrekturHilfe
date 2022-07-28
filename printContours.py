# scans pages for numbers in a specified format
import cv2
from contours import Contours

def findContours(readImage, im):
    contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoursObj = Contours(readImage, contours)
    return contoursObj

def drawContours(im, contours):
    img = cv2.drawContours(im, contours, -1, (70,7,80), 2)
    return img
