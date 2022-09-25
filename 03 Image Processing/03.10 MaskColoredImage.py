from turtle import circle
import cv2
import numpy as np

img = cv2.imread("img/0301.png")
imgCr = cv2.imread("img/0301.png")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# detect circles
gray = cv2.medianBlur(cv2.cvtColor(imgRGB, cv2.COLOR_RGB2GRAY), 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

# draw mask
mask = np.full((imgRGB.shape[0], imgRGB.shape[1]), 0, dtype=np.uint8)  # mask is only
for i in circles[0, :]:
    cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

for i in circles[0, :]:
    cv2.circle(imgCr, (i[0], i[1]), i[2], (255, 255, 255), 1)

# get first masked value (foreground)
fg = cv2.bitwise_or(imgRGB, imgRGB, mask=mask)

# get second masked value (background) mask must be inverted
mask = cv2.bitwise_not(mask)
background = np.full(imgRGB.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(background, background, mask=mask)

# combine foreground+background
final = cv2.bitwise_or(fg, bk)
cv2.imshow('Original', img)
cv2.imshow('Mask Path', imgCr)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', final)

cv2.waitKey(0)
