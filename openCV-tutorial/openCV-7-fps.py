import cv2
import time

imgWidth = 640
imgHeight = 360
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

pTime = 0.
fpsFiltered = 20

while True:
    rep, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    fpsFiltered = fpsFiltered * 0.97 + fps * 0.03  #smoothen the change in fps - Low Pass Filter
    cv2.rectangle(frame,(0,0),(165,45),(255,0,255),-1)
    cv2.putText(frame,'FPS: '+str(int(fpsFiltered)),(15,30),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 2)
    cv2.imshow("Video", frame)
    cv2.moveWindow("Video", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
