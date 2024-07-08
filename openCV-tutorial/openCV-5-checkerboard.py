import numpy as np
import cv2
imgSize = 800
squares = 8

darkColor = (0,0,0)
lightColor = (0,0,255)

while True:
    frame = np.zeros((imgSize,imgSize,3),dtype=np.uint8)
    for i in range(0,squares):
        for j in range(0,squares):
            if((i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)):
                frame[((imgSize//squares))*j:(imgSize//squares)*(j+1),
                      ((imgSize//squares))*i:(imgSize//squares)*(i+1)] = lightColor
            else:
                frame[((imgSize//squares))*j:(imgSize//squares)*(j+1),
                      ((imgSize//squares))*i:(imgSize//squares)*(i+1)] = darkColor

    cv2.imshow('Window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break