import cv2

img = cv2.imread("img/0301.png")
print(img.shape)
crop = img[1:700, 200:900]
cv2.imshow('Original', img)
cv2.imshow('Croped', crop)
cv2.waitKey(0)
