import cv2

img = cv2.imread("img/0301.png")
print(img.shape)
h, w, le = img.shape
size = 1.55
resized = cv2.resize(img, (round(w*size), round(h*size)))
cv2.imshow('Original', img)
cv2.imshow('New size with same ratio', resized)
cv2.waitKey(0)
