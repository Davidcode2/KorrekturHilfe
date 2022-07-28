import pytesseract
import sys

def getStringContentOfImage(viewedImage):
    print("searching content of", str(sys.argv[1]))
    # use the below for images
    string = pytesseract.image_to_string(viewedImage, lang="deu")
    return string

def readMultiplePages():
    try:
        doc = convert_from_path(filePath)
        for page_number, page_data in enumerate(doc):
            txt = pytesseract.image_to_string(page_data, lang="deu").encode("utf-8")
            print("Page # {} - {}".format(str(page_number),txt))
    except:
        print("error")

