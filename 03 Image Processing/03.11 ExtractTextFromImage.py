# from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string('img/0311.png'))
