import cv2

img = cv2.imread('Lenna.png')
cv2.imshow('Original image', img)
cv2.waitKey(0)

grayimg = cv2.cvtColor(img[..., 0], cv2.COLOR_GRAY2RGB)
cv2.imshow('Gray image', grayimg)
cv2.waitKey(0)

cv2.imwrite('gray.png', grayimg)