import cv2

img = cv2.imread("img/0301.png")
result = cv2.resize(img, (400, 300))
cv2.imshow('Original', img)
cv2.imshow('New Size', result)
cv2.waitKey(0)
