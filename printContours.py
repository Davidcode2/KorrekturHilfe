# scans pages for numbers in a specified format
import os
import pytesseract
import cv2
from pdf2image import convert_from_path
from PIL import Image
import sys
import numpy as np

# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/WS21/AuD2/Altklausuren/Algo Prüfung 21-22.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Altklausuren/Lingel_Korr_2.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Altklausuren/Ostermann_Korrektur.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Aufschrieb.pdf"

def main():
    image = getImage()
    viewedImage = cv2.imread(image)
    stringContentOfImage = getStringContentOfImage(viewedImage)
    print(stringContentOfImage)

    img_gray = cv2.cvtColor(viewedImage, cv2.COLOR_BGR2GRAY)
    ret, im = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoursObj = Contours(viewedImage, contours)
    img = cv2.drawContours(im, contours, -1, (70,7,80), 2)

    show_image(img)

    #findShapes(contours)
    #drawBorders(contours)

    contoursObj.findShapesAndDrawBorders()

    try:
        doc = convert_from_path(filePath)
        for page_number, page_data in enumerate(doc):
            txt = pytesseract.image_to_string(page_data, lang="deu").encode("utf-8")
            print("Page # {} - {}".format(str(page_number),txt))
    except:
        print("error")

def checkArguments():
    if len(sys.argv) == 1:
        print("no argument given")
        return False
    return True

def checkPath():
    ...
    return True

def getStringContentOfImage(viewedImage):
    print("searching content of ", str(sys.argv[1]))

    # use the below for images
    string = pytesseract.image_to_string(viewedImage)
    return string

def getImage():
    if not checkArguments():
        return False

    if not checkPath():
        return False

    image = sys.argv[1]
    return image

def show_image(image):
    cv2.imshow('image',image)
    c = cv2.waitKey()
    if c >= 0 : return -1
    return 0

class Contours():
    def __init__(self, image, contours):
        self.viewedImage = image
        self.contours = contours

    def findShapesAndDrawBorders(self):
        print("print borders on the found contours")
        # list for storing names of shapes
        i = 0
        for contour in self.contours:
            # here we are ignoring first counter because
            # findcontour function detects whole image as shape
            if i == 0:
                i = 1
                continue

            # cv2.approxPloyDP() function to approximate the shape
            approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)

            # using drawContours() function
            cv2.drawContours(self.viewedImage, [contour], 0, (0, 0, 255), 5)

            # finding center point of shape
            M = cv2.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])

            # putting shape name at center of each shape
            if len(approx) == 3:
                cv2.putText(self.viewedImage, 'Triangle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            elif len(approx) == 4:
                cv2.putText(self.viewedImage, 'Quadrilateral', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            elif len(approx) == 5:
                cv2.putText(self.viewedImage, 'Pentagon', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            elif len(approx) == 6:
                cv2.putText(self.viewedImage, 'Hexagon', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            else:
                cv2.putText(self.viewedImage, 'circle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # displaying the image after drawing contours
        cv2.imshow('shapes', self.viewedImage)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

def reduceImageToColor(img):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask_blue = cv2.inRange(imghsv, lower_blue, upper_blue)
    _, contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im = np.copy(img)
    cv2.drawContours(im, contours, -1, (0, 255, 0), 1)
    cv2.imwrite("contours_blue.png", im)

main()
