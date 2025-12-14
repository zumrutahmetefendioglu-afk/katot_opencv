import cv2
import numpy as np

gorsel= cv2.imread("photo_2025-12-03_18-34-01.jpg")
yeni_gorsel = cv2.resize(gorsel, (300, 300))
gri_gorsel = cv2.cvtColor(yeni_gorsel, cv2.COLOR_BGR2GRAY)

def bos_fonksiyon(x):
    pass

cv2.namedWindow("Sonuc")
cv2.createTrackbar("Bulaniklastirma", "Sonuc", 0, 50, bos_fonksiyon)
cv2.createTrackbar("Dilation+Erosion", "Sonuc", 0, 50, bos_fonksiyon)

while True: 
    b = cv2.getTrackbarPos("Bulaniklastirma", "Sonuc")
    bulaniklastirma_kernel= 2 * b + 1
    bulanik = cv2.GaussianBlur(gri_gorsel, (bulaniklastirma_kernel, bulaniklastirma_kernel), 0) 
    _, binary = cv2.threshold(bulanik, 127, 255, cv2.THRESH_BINARY) 

    m = cv2.getTrackbarPos("Dilation+Erosion", "Sonuc")
    k_size = 2 * m + 1
    kernel = np.ones((k_size, k_size), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    cv2.imshow("Bulaniklastirma", bulanik)
    cv2.imshow("Dilation + Erosion", eroded)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

