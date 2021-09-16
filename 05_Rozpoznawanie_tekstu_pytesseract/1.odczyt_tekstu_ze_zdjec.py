import pytesseract
import imutils
import cv2
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr(filename):
    return pytesseract.image_to_string(filename)


img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\OCR_text.png')

print(ocr(img))
