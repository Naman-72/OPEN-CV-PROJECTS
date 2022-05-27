import cv2, numpy as np , math 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
noses = cv2.CascadeClassifier('nose.xml')
while True :
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ans = noses.detectMultiScale(gray,1.3,5)
    if len(ans) == 0 :
        cv2.putText(frame,"No Nose 😄",(100,100),2,cv2.FONT_HERSHEY_COMPLEX_SMALL,(255,0,0),1)
    else :
        for (x,y,w,h) in ans :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,250),4)
    cv2.imshow("Nose Detector",frame)
    if cv2.waitKey(12) == 13 or cv2.waitKey(12) == 27 :
        break
cv2.destroyAllWindows 