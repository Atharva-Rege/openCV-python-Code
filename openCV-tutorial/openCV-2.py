import cv2

imgWidth = 640
imgHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,imgWidth)
cap.set(4,imgHeight)

while True:
    rep, frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video 1",frame)
    cv2.moveWindow("Video 1",0,0)
    cv2.imshow("Gray 1",imgGray)
    cv2.moveWindow("Gray 1",imgWidth,0)
    cv2.imshow("Gray 2",imgGray)
    cv2.moveWindow("Gray 2",0,imgHeight)
    cv2.imshow("Video 2",frame)
    cv2.moveWindow("Video 2",imgWidth,imgHeight)
                   
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()