import sys
import cv2
cap=cv2.VideoCapture(0) # open camera
if cap.isOpened():  
    print("camera is ready to take pictures")
else:
    print("camera driver error")
# addding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# saving video
output=cv2.VideoWriter('rohit.mp4',plugin,25,(640,480))
while cap.isOpened():
    status,frame=cap.read()  # clicking image
    cv2.imshow('live',frame)  # showing image
    output.write(frame) # sending data to videowWiter
    if cv2.waitKey(10) & 0xff == ord('q'):
        break 
cv2.destroyAllWindows()
cap.release()