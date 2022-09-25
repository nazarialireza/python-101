import cv2
import np

# # add image contrast

img = cv2.imread("img/0301.png")
print(img.shape)
contrasted = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)

cv2.imshow('original', img)
cv2.imshow('contrasted_Image', contrasted)
cv2.waitKey(0)
