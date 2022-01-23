import pytesseract
import cv2
import os
from gtts import gTTS

img = cv2.imread('image/quote3.jpg')
img = cv2.resize(img, (500, 600))
hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
xy = pytesseract.image_to_string(img)
for b in boxes.splitlines():
  b = b.split(' ')

x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

print(pytesseract.image_to_string(img))
cv2.imshow('Detected text', img)

audio = gTTS(text = xy, lang = 'en', slow = True)
audio.save("quote3.wav")
os.system("quote3.wav")
cv2.waitKey(0)