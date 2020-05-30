
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Lenna.png')

sobel= cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2),plt.imshow(sobel, cmap='gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])

plt.show()