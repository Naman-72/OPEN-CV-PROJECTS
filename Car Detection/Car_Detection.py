import cv2
import numpy as np

cap = cv2.VideoCapture('carv.mp4')

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret,frames = cap.read()
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.3,3)

    if  cars is not None :
        cv2.putText(frames,"Cars Present",(60,30),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),4)
    else :
        cv2.putText(frames,"No Car Present",(60,30),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),4)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),3)
        
    cv2.imshow("CAR DETECTOR",frames)

    key = cv2.waitKey(1)
    if key == 27 or key == 13 :
        break

cv2.destroyAllWindows()