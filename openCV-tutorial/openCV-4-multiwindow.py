import cv2

rows = int(input("Enter Rows: "))
cols = int(input("Enter Columns: "))

imgWidth = 1280
imgHeight = 720
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    rep, frame = cap.read()
    frame = cv2.resize(frame, ((imgWidth//cols), (imgHeight//cols)))
    for i in range(0, rows):
        for j in range(0, cols):
            windName = 'Window'+str(i+1)+' x '+str(j+1)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, (imgWidth//cols) * j, (imgHeight//cols + 30) * i)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
