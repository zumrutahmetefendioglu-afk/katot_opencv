import cv2
import numpy as np 

gorsel=cv2.imread("photo_2025-12-03_18-34-01.jpg")
gorsel_boyutu = np.zeros((300, 300, 3), dtype=np.uint8)
cizgili_gorsel=cv2.line(gorsel_boyutu,(0,250),(300,250),(255,0,255),3)

cv2.imshow("gorsel",(cizgili_gorsel))
cv2.waitKey(0)
cv2.destroyAllWindows()






