import sys
import cv2
cap=cv2.VideoCapture(0) # open camera
if cap.isOpened():  
    print("camera is ready to take pictures")
else:
    print("camera driver error")
n=0
while cap.isOpened():
    status,frame=cap.read()  # clicking image
    # converting image frame into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(frame.shape)
    # now we can draw al those patterns
    # line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    # rectangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),4)
    # circle
    cv2.circle(frame,(200,300),30+n,(13,44,123),2)
    # text writing
    font=cv2.FONT_HERSHEY_SIMPLEX # this is font type
    cv2.putText(frame,'ROHIT',(10,50),font,2,(0,2,255),2,cv2.LINE_AA)
    cv2.imshow('live',frame)  # showing image
    #cv2.imshow('livegray',grayimg) # showing second image
    n=n+1
    if cv2.waitKey(10) & 0xff == ord('q'):
        break 
cv2.destroyAllWindows()
cap.release()