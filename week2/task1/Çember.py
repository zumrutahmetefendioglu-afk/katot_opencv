import cv2
import numpy as np 

fotograf=cv2.imread("photo_2025-12-03_18-34-01.jpg")
fotograf_boyutu = np.zeros((300, 300, 3), dtype=np.uint8)
fotograf_cemberi=cv2.circle(fotograf_boyutu,(150,150),5,(0,255,255),3)

cv2.imshow("cember",(fotograf_cemberi))
cv2.waitKey(0)
cv2.destroyAllWindows()









