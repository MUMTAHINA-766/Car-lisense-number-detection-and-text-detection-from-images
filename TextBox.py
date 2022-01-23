import cv2
import numpy
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR/tesseract.exe"
image = cv2.imread("image/quote3.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))

hImg,wimg,_=image.shape
boxes = pytesseract.image_to_boxes(image)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
  if x!=0:
    b = b.split(' ')
    print(b)

    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])

    cv2.rectangle(image,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(image,b[0],(x, hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
    

cv2.imshow('Result',image)
cv2.waitKey(0)