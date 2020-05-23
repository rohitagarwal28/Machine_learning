#!/usr/bin/python3
import cv2

# starting camera
cap=cv2.VideoCapture(0)     # this is first camera

# to check camera is started or not
if cap.isOpend():
	print("camera is ready to take pictures")

else:
	print("check your web cam drivers")

# now we can read input from camera
status,img=cap.read() # it will take first picture
status1,img1=cap.read()
# now showing
cv2.imshow('liveimage',img)
cv2.imshow('liveimage',img1)
cv2.waitKey(0)

# to close camera
cap.release()



