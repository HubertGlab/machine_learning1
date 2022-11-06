import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('lena.jpg')

custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('lena.jpg')

pytesseract.image_to_string(img)
