import cv2

imgWidth = 640
imgHeight = 360
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',400,100)
cv2.moveWindow('Trackbars',imgWidth,0)
xPos = imgWidth//2
yPos = imgHeight//2
myRadius = 25
def myCallBack1(val):
    global xPos
    print('xPos: ',val)
    xPos = val
def myCallBack2(val):
    global yPos
    print('yPos: ',val)
    yPos = val
def myCallBack3(val):
    global myRadius
    print('Radius: ',val)
    myRadius = val
cv2.createTrackbar('xPos','Trackbars',320, #Initial value (not the starting value)
                   640,myCallBack1)
cv2.createTrackbar('yPos','Trackbars',240,480,myCallBack2)
cv2.createTrackbar('Radius','Trackbars',25,imgHeight//2,myCallBack3)



while True:
    rep, frame = cap.read()

    cv2.circle(frame,(xPos,yPos),myRadius,(0,0,255),2)

    cv2.imshow("Video", frame)
    cv2.moveWindow("Video", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
