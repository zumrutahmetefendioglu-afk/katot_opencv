import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Canny")
def bos_fonksiyon(x):
    pass
cv2.createTrackbar("Beyaz Kenar", "Canny", 50, 300, bos_fonksiyon)
cv2.createTrackbar("Siyah Kenar", "Canny", 150, 300, bos_fonksiyon)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    t1 = cv2.getTrackbarPos("Beyaz Kenar", "Canny")
    t2 = cv2.getTrackbarPos("Siyah Kenar", "Canny")
    manuel = cv2.Canny(gri, t1, t2)
    median = np.median(gri)
    alt_sinir= int(max(0, 0.66 * median))
    ust_sinir= int(min(255, 1.33 * median))
    otomatik = cv2.Canny(gri, alt_sinir, ust_sinir)
    cv2.imshow("Manuel Canny", manuel)
    cv2.imshow("Auto Canny", otomatik)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


