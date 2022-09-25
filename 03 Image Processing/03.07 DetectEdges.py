import cv2

img = cv2.imread("img/0301.png")
edge = cv2.Canny(img, 100, 200)
cv2.imshow("Original", img)
cv2.imshow("Detected Edges", edge)
cv2.waitKey(0)
