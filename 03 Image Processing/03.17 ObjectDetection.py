import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

img = cv2.imread("img/0318.jpg")
# Altering properties of image with cv2
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Importing Haar cascade classifier xml data
data = cv2.CascadeClassifier('img/data.xml')

# Detecting object in the image with Haar cascade classifier
detecting = data.detectMultiScale(img_gray, minSize=(20, 20))

# Amount of object detected
amountDetecting = len(detecting)

# Using if condition to highlight the object detected
if amountDetecting != 0:
    for (x, y, width, height) in detecting:
        cv2.rectangle(img_rgb, (x, y),  # Highlighting detected object with rectangle
                      (x + height, y + width),
                      (0, 255, 0), 5)
# Plotting image with subplot() from plt
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
