import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR/tesseract.exe"
from PIL import Image
import cv2

image = cv2.imread("image/Sample_image.png")
#converting image into gray scale image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 # converting it to binary image by Thresholding

 # this step is require if you have colored image because if you skip this part
 # then tesseract won't able to detect text correctly and this will give incorrect result

threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

 # display 
cv2.imshow('Result', image)

img = Image.open('image/Sample_image.png')
text = tess.image_to_string(img)

print(text)
cv2.waitKey(0)