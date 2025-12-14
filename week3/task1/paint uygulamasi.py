import cv2 
import numpy as np 
gorsel= np.zeros((300, 300, 3), dtype=np.uint8)
mode = 0
cizim = False  
def fare_imleci(event, x, y, flags, param):
    global gorsel, cizim, mode
    if mode == 0:
        if event == cv2.EVENT_MOUSEMOVE:
            gorsel[y, x] = (255, 0, 0)  
    elif mode == 1:
        if event == cv2.EVENT_LBUTTONDOWN:
            gorsel[y, x] = (255, 0, 0)
    elif mode == 2:
        if event == cv2.EVENT_LBUTTONDOWN:
            cizim = True
        elif event == cv2.EVENT_LBUTTONUP:
            cizim = False
        elif event == cv2.EVENT_MOUSEMOVE and cizim:
            gorsel[y, x] = (255, 0, 0)
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", fare_imleci)
while True:
    cv2.imshow("Paint", gorsel)
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    elif key == ord('e'):
        gorsel[:] = 0
    elif key == ord('s'):
        cv2.imwrite("cizim.png", gorsel)
        print("Görüntü kaydedildi")   
    elif key == ord('0'):
        mode = 0       
    elif key == ord('1'):
        mode = 1     
    elif key == ord('2'):
        mode = 2
cv2.destroyAllWindows()