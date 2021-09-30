import cv2
import pytesseract
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r" Write tesseract.exe file path "

#Capture camera
kamera = cv2.VideoCapture(0)
cf = 0
#Resolution Settings
kamera.set(3, 640) 
kamera.set(4, 480)

# OCR function define
def tessfunc():
    text = pytesseract.image_to_string(thresh)
    print(text)

while 1:
      
    ret, kem = kamera.read()
    # Convert color to gray
    kam = cv2.cvtColor(kem, cv2.COLOR_BGR2GRAY)
    #Apply threshold 
    ret, thresh = cv2.adaptiveThreshold(kam,125,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11))
    #Display camera
    cv2.imshow('kamera', thresh)

    if cf == 1:
        tessfunc()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cf = 0
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cf = 1
    if cv2.waitKey(1) & 0xFF == ord('e'):
        print("Terminating the program")
        break
# Close the camera
kamera.release()
exit()
