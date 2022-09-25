import cv2

img = cv2.imread("img/0301.png")
print(img.shape)
blur = cv2.GaussianBlur(img, (7, 7), 20)
cv2.imshow('Original', img)
cv2.imshow('Blur Effect 1', blur)
cv2.waitKey(0)
