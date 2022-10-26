import cv2
import pytesseract
from PIL import Image


imagem = cv2.imread("placa4.jpg")

caminho= r"C:\Program Files\Tesseract-OCR"
#definir caminho
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

###prhase = pytesseract.image_to_string(Image.open('placa4.jpg'))

texto= pytesseract.image_to_string(imagem)



print(texto)