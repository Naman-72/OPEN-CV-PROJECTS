# INSTALLATION OF ALL USEFUL LIBRARIES
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# VIDEO CAMERA 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# FONT
font = cv2.FONT_HERSHEY_PLAIN

# NOW WORK ON EACH FRAME
while True:
    # READ EACH FRAME 
    suc,frame= cap.read()
    # DECODE THE DATA IN THE FRAME 
    d = pyzbar.decode(frame)
    # IF NOT FOUNDED ANY QR CODE
    if not d :
        cv2.putText(frame,"NOT FOUNDED ANY QR CODE",(50,50),font,2,(0,0,0),4)
    # IF MULTIPLE DATA 
    for i in d:
        # WE WANT TO DISPLAY THE DATA FIELD ONLY 
        str1 = str(i.data)
        # WE DON'T WANT EXTRA TEXT SO WE SUBSTRING
        str1 = str1[2:-1]
        # print(str1)
        # PUTTING IN TEXT IN FRAME
        # putText(frame,"string",co-ordinates,font,size,BGR COLOR , thickness)
        cv2.putText(frame,str1,(5,50),font,2,(255,0,0),4)
    # NAME OF THE WINDOW
    cv2.imshow("QR CODE DECODER",frame)
    # FOR TERMINATING
    key = cv2.waitKey(1)
    # 27 : ESC KEY 
    # 13 : ENTER KEY
    if key == 27 or  key == 13 :
        break

cv2.destroyAllWindows()