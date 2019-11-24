
import cv2
import numpy as np

img = cv2.imread('Lenna.png')
blur = cv2.GaussianBlur(img, (51, 51), 0)
# cv2.imshow(' ', blur)
# cv2.waitKey(0)

# Объеденяет и выводит сразу 2 изображения
vis = np.concatenate((img, blur), axis=1)
cv2.imshow('', vis)
cv2.waitKey(0)