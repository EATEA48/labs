import cv2

img = cv2.imread('Lenna.png')
blur = cv2.GaussianBlur(img, (51, 51), 0)
cv2.imshow(' ', blur)
cv2.waitKey(0)