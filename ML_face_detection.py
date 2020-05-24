import cv2

# calling classifier
casclf=cv2.CascadeClassifier('face.xml')
# loading face data
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    # now we csn apply class
    face=casclf.detectMultiScale(frame,1.13,5)  # classifier tuning parameter
    print(face)
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        # only face
        facedata=frame[x:x+h,y:y+w]
        cv2.imshow('f',facedata)
    cv2.imshow('face',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
