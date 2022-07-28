from getImage import getImagePath
from readText import getStringContentOfImage
import prepImage
import cv2
import printContours
import util

def main():
    imagePath = getImagePath()
    readImage = cv2.imread(imagePath)
    image = prepImage.Image(readImage)
    preppedImg = image.toGreyscale()

    redparts_outlined_image = image.contoursOfColor()
    cv2.imwrite("red_contours.png", redparts_outlined_image)

    onlyRedparts = image.reduceImageToColor()
    cv2.imwrite("red_only.png", onlyRedparts)

    contoursObj = image.findContours(preppedImg)
    image.drawContours(contoursObj.contours)

    #stringContentOfImage = getStringContentOfImage(preppedImg)
    #print(stringContentOfImage)

    onlyRedparts_prep = prepImage.Image(onlyRedparts)
    onlyRedparts_Inv_greyscale = onlyRedparts_prep.toGreyscale()
    cv2.imwrite("redparts_grayscale_inv.png", onlyRedparts_Inv_greyscale)
    readImageInvGreyscale = cv2.imread("redparts_grayscale.png")
    onlyRedparts_Inv_greyscale_Image = prepImage.Image(readImageInvGreyscale)
    onlyRedparts_greyscale = onlyRedparts_Inv_greyscale_Image.toInvertedGreyscale()
    cv2.imwrite("redparts_grayscale.png", onlyRedparts_greyscale)

    stringContentRed = getStringContentOfImage(onlyRedparts_greyscale)
    print(stringContentRed)

main()
