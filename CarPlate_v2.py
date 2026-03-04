#Number Plate Recognition with OpenCV and EasyOCR

#Data Collection/Plates/0a69ed8e-b58b-418c-a38c-11fe2e9e8fb3.jpg

from easyocr import Reader
import cv2
import urllib.request
import numpy as np
import os
import time
import PIL as Image

global plate_cnt
path ='F:/L2/S2/Work-based Professional Project in Computer Science (I)/New folder/licencePlatesUPDATE/Detected_Plates'
url = 'http://192.168.0.44/cam-hi.jpg'
count = 1
while True:
 img_response = urllib.request.urlopen(url)
 img_array = np.array(bytearray(img_response.read()), dtype=np.uint8)
 imgt =cv2.imread('7.png' ,1)
 im = cv2.imdecode(img_array, -1)
 car = cv2.resize(im, (800, 600))
 gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
 blur = cv2.GaussianBlur(gray, (5,5), 0)
 edged = cv2.Canny(blur, 10, 200)
 cont, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 cont = sorted(cont, key = cv2.contourArea, reverse = True)[:5]
 for c in cont:
    arc = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * arc, True)
    if len(approx) == 4:
        plate_cnt = approx
        break
 (x, y, w, h) = cv2.boundingRect(plate_cnt)
 plate = gray[y:y + h, x:x + w]

 reader = Reader(['ar'] ,  gpu=False, verbose=False)
 detection = reader.readtext(plate)
 print(detection)

 if len(detection) == 0:
    text = "Impossible to read the text from the license plate"
    cv2.putText(car, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 3)
    cv2.imshow('Image', car)
    cv2.waitKey(0)
 else:
    cv2.drawContours(car, [plate_cnt], -1, (0, 255, 0), 3)
    text = f"{detection[0][1]} {detection[0][2] * 100:.2f}%"
    cv2.putText(car, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    print(text)
    cv2.imshow('license plate', plate)
    cv2.imshow('Image', car)
    cv2.imwrite(os.path.join(path , f'{count}.png'), plate)
    count += 1
    cv2.waitKey(0)


    

    # Restart the code
    # ...

