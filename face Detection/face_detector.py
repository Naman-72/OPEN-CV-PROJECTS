import cv2
import numpy as np
import math
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
face_classifier = cv2.CascadeClassifier('face.xml')
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Faces is A tuple So We Check is empty by len(Faces)
    faces = face_classifier.detectMultiScale(gray,1.2,3)
    if len(faces) == 0  :
        cv2.putText(frame,"No Face Found",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)
    else :
        for (x,y,w,h) in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    cv2.imshow("Screen",frame)
    if cv2.waitKey(1) == 13 or cv2.waitKey == 27 :
        break
cv2.destroyAllWindows