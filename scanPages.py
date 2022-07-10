# scans pages for numbers in a specified format
import os
import pytesseract
import cv2
from pdf2image import convert_from_path
from PIL import Image

# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/WS21/AuD2/Altklausuren/Algo Prüfung 21-22.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Altklausuren/Lingel_Korr_2.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Altklausuren/Ostermann_Korrektur.pdf"
# filePath = "/home/jakob/OneDrive/HochschuleAA/bachelor-2/SS22/Rechnernetze/Aufschrieb.pdf"
image = "/home/jakob/Pictures/ocr_testdata1.jpg"

# use the below for images
viewedImage = cv2.imread(image)
string = pytesseract.image_to_string(viewedImage)
print(string)

try:
    doc = convert_from_path(filePath)
    for page_number, page_data in enumerate(doc):
        txt = pytesseract.image_to_string(page_data, lang="deu").encode("utf-8")
        print("Page # {} - {}".format(str(page_number),txt))
except:
    print("error")

