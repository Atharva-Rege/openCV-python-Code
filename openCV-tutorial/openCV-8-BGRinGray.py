import cv2
import time

imgWidth = 640
imgHeight = 480
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

topLeftX = 270
topLeftY = 130
bottomRightX = 370
bottomRightY = 230

toRight = True
toBottom = True

while True:
    rep, frame = cap.read()
    if(topLeftX <= 0):
        toRight = True
    elif(topLeftY <= 0):
        toBottom = True
    elif(bottomRightX >= imgWidth):
        toRight = False
    elif(bottomRightY >= imgHeight):
        toBottom = False
    
    if(toRight):
        if(toBottom):
            topLeftX += 1
            topLeftY += 1
            bottomRightX += 1
            bottomRightY += 1
        else:
            topLeftX += 1
            topLeftY -= 1
            bottomRightX +=1
            bottomRightY -=1
    else:
        if(toBottom):
            topLeftX -= 1
            topLeftY += 1
            bottomRightX -= 1
            bottomRightY += 1
        else:
            topLeftX -= 1
            topLeftY -= 1
            bottomRightX -=1
            bottomRightY -=1
    
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameROI = frame[topLeftY:bottomRightY, topLeftX:bottomRightX]
    frameGray2BGR = cv2.cvtColor(frameGray,cv2.COLOR_GRAY2BGR)
    frameGray2BGR[topLeftY:bottomRightY, topLeftX:bottomRightX] = frameROI
    
    cv2.imshow("Window",frameGray2BGR)
    cv2.moveWindow('Window',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
