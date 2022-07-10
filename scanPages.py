# scans pages for numbers in a specified format
import pytesseract

def ocr_core(file):
    text = pytesseract.image_to_string(file, lang='ger')
    return text

print(ocr_core('~/Pictures/Screenshots/2022-02-13_19-38-07_screenshot.png'))
