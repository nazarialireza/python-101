import cv2

img = cv2.imread("img/0314.png")
result = cv2.fastNlMeansDenoisingColored(img, None, 20, 10, 7, 21)
cv2.imshow('Original', img)
cv2.imshow('De-noised', result)
cv2.waitKey(0)
