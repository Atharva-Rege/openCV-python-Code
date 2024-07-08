import cv2

imgWidth = 640
imgHeight = 360
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow('Video')
evt=0
def mouseClick(event,xPos,yPos,flags,params):
    global evt,pnt
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        pnt = (xPos,yPos)
    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        pnt = (xPos,yPos)
    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event
cv2.setMouseCallback("Video",mouseClick)

while True:
    rep, frame = cap.read()
    if evt == 1:
        topLeftPnt = pnt
        cv2.line(frame,topLeftPnt,(topLeftPnt[0]+20,topLeftPnt[1]),(0,0,255),2)
        cv2.line(frame,topLeftPnt,(topLeftPnt[0],topLeftPnt[1]+20),(0,0,255),2)
    if evt == 4:
        bottomRightPnt = pnt
        cv2.rectangle(frame,topLeftPnt,bottomRightPnt,(0,0,255),2)
        frameROI = frame[topLeftPnt[1]:bottomRightPnt[1],topLeftPnt[0]:bottomRightPnt[0]]
        cv2.imshow("ROI", frameROI)
        cv2.moveWindow("ROI", imgWidth+30,0)
    if evt == 2:
            cv2.destroyWindow('ROI')
            evt = 0
    cv2.imshow("Video", frame)
    cv2.moveWindow("Video", 0, 0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
