# Car-lisense-number-detection-and-text-detection-from-images!
[car1](https://user-images.githubusercontent.com/64628178/150674440-ad2165e4-7b55-4a79-ac46-29b5fbdd58fa.PNG)

![car1](https://user-images.githubusercontent.com/64628178/150674444-18515420-0063-4278-b468-1c694ce5a107.PNG)

![car2](https://user-images.githubusercontent.com/64628178/150674447-d68cb07f-6090-4a3a-8cf2-9a164e8d5f92.PNG)

![car3](https://user-images.githubusercontent.com/64628178/150674448-df04b8f9-6d85-4144-b8a6-5cfafcd7f7b9.PNG)

![car4](https://user-images.githubusercontent.com/64628178/150674455-fe40a573-8877-43de-999b-d21d3924549b.PNG)

![imgttxt1](https://user-images.githubusercontent.com/64628178/150674465-ba4a7196-5101-4110-9cd4-a56519c4061a.PNG)

[imgttxt3](https://user-images.githubusercontent.com/64628178/150674474-108dd578-ace7-4ce3-bc7f-800820561258.PNG)

![textbox1](https://user-images.githubusercontent.com/64628178/150674480-bdd939ab-9420-4725-93a4-dd2eeb21727c.PNG)

![textbox2](https://user-images.githubusercontent.com/64628178/150674482-e895b1c9-0bd7-4bb3-b828-6045c129c740.PNG)

![AudioDet1](https://user-images.githubusercontent.com/64628178/150674502-7a51b555-70d8-452f-8d7e-1e213a29f020.PNG)

## Step : 1 :- Installation and environment setup

Here, I’ll use Python as a programming language to complete the OCR task.Make sure we have python 3 installed in our system then we are ready to install OCR and Tesseract, use the commands mentioned below one by one:

pip install opencv-python

pip install pytesseract

## Step 2:-  import libraries in visual studio code:

import pytesseract

import cv2

import os

from gtts import gTTS

import numpy as np

import imutils

## Step 3:- Read and image and detect the texts show as output:
image = cv2.imread("image/Sample_image.png")

## (converting image into gray scale image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## (Converting it to binary image by Thresholding

 this step is require if you have colored image because if you skip this part
  then tesseract won't able to detect text correctly and this will give incorrect result)

threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

## (display  image)

cv2.imshow('Result', image)

img = Image.open('image/Sample_image.png')

## (Display the image until press any key)

cv2.waitKey(0)

## (Detect the text from image and print it:)

text = tess.image_to_string(img)

print(text)

## Step 4 : Make the text audible and save the audio file:

audio = gTTS(text = xy, lang = 'en', slow = True)

audio.save("quote3.wav")

os.system("quote3.wav")
