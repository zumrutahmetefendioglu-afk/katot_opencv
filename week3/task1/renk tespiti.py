import cv2 
import numpy as  np 

kamera = cv2.VideoCapture(0)
altsinirrenk = np.array([100, 150, 50])
ustsinirrenk = np.array([140, 255, 255])

while True:
    ret, frame = kamera.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maske = cv2.inRange(hsv, altsinirrenk, ustsinirrenk)
    kernel = np.ones((5, 5), np.uint8)
    maske = cv2.morphologyEx(maske, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    merkez= []  
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                merkez.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
    if len(merkez) >= 2:
        cv2.line(frame, merkez[0], merkez[1], (255, 0, 0), 2)
    cv2.imshow("Maske", maske)
    cv2.imshow("Renk Tespiti", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()




