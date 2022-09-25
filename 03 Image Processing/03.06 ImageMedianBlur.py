import cv2

img = cv2.imread("img/0306.png")
print(img.shape)
blur = cv2.medianBlur(img, 5)
cv2.imshow('Original', img)
cv2.imshow('Blur Effect 2', blur)
cv2.waitKey(0)
