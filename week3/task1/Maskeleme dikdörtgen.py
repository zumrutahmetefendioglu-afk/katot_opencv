import cv2
import numpy as np


gorsel = cv2.imread("photo_2025-12-03_18-34-01.jpg")
k,h=960,1280

maske = np.zeros((h, k), dtype=np.uint8)


dikdortgen_kenar = int(k * 0.5)
dikdortgen_yukseklik= int(h * 0.5)

cx, cy = k // 2, h // 2

x1 = cx - dikdortgen_kenar // 2
y1 = cy - dikdortgen_yukseklik // 2
x2 = cx + dikdortgen_kenar// 2
y2 = cy +  dikdortgen_yukseklik// 2

cv2.rectangle(maske, (x1, y1), (x2, y2), 255, -1)


uc_kanal = cv2.merge([maske, maske, maske])


maske_gorsel = cv2.bitwise_and(gorsel,uc_kanal)
cv2.namedWindow("Maske",cv2.WINDOW_NORMAL)
cv2.namedWindow("Sonuc",cv2.WINDOW_NORMAL)

cv2.imshow("Maske", maske)
cv2.imshow("Maskelenmis Goruntu", maske_gorsel)
cv2.waitKey(0)


