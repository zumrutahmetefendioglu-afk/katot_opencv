import cv2
import numpy as np 

fotograf=cv2.imread("photo_2025-12-03_18-34-01.jpg")
fotograf_boyutu = np.zeros((300, 300, 3), dtype=np.uint8)
yazili_fotograf=cv2.putText(fotograf_boyutu,"Zumrut Ahmetefendioglu",(0,280),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,255,0),1)

cv2.imshow("Yazi",yazili_fotograf)
cv2.waitKey(0)
cv2.destroyAllWindows()
                             





                             