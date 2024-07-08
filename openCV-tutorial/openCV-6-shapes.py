import cv2
import time

imgWidth = 640
imgHeight = 360
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

myRadius = 30
myColor = (255,255,0)

while True:
    rep, frame = cap.read()
    
    #frame[270:370,130:230] = (0,0,0)
    cv2.rectangle(frame, (130,270), (230,370), (0,0,255), -1 #thickness = -1 for filled rectangle 
                  )
    cv2.circle(frame, (imgWidth//2, imgHeight//2), myRadius, myColor,-1)
    cv2.putText(frame,'Hello World',(140,370), #Lower Left Corner Coordinates 
                 cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", frame)
    cv2.moveWindow("Video", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
