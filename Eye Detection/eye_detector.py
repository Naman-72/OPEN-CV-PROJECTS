import cv2 , numpy as np , math
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
eye_classifier = cv2.CascadeClassifier('eye.xml')
while True :
    ret,frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes = eye_classifier.detectMultiScale(img,1.2,4)
    if len(eyes) == 0 :
        cv2.putText(frame,"No Eye Present",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(250,0,0),3)
    else :
        cv2.putText(frame,"Eyes Present",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(250,0,0),3)
        for (x,y,w,h) in eyes :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow("Eye Detector",frame)
    if cv2.waitKey(2) == 13 or cv2.waitKey(2) == 27 :
        break
cv2.destroyAllWindows
