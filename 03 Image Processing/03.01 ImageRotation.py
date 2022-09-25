import cv2
import imutils

img = cv2.imread("img/0301.png")
rotated = imutils.rotate(img, 45)

cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
