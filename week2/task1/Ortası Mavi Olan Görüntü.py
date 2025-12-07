import cv2
import numpy as np 

gorsel=cv2.imread("photo_2025-12-03_18-34-01.jpg")
gorsel_bos = np.zeros((300, 300, 3), dtype=np.uint8)

gorsel_bos[150,150,0] = 255  
gorsel_bos[150,150,1] = 0    
gorsel_bos[150,150,2] = 0    

cv2.imshow("orta piksel",(gorsel_bos))
cv2.waitKey(0)
cv2.destroyAllWindows(0)





