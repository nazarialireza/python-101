import cv2

img = cv2.imread("img/0309.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
moment = cv2.moments(gray)
X = int(moment["m10"] / moment["m00"])
Y = int(moment["m01"] / moment["m00"])

cv2.circle(img, (X, Y), 50, (0, 255, 0), 3)
cv2.circle(img, (X, Y), 150, (255, 0, 0), 3)
cv2.circle(img, (X, Y), 250, (0, 0, 255), 3)
cv2.imshow('Image_center', img)

cv2.waitKey(0)
