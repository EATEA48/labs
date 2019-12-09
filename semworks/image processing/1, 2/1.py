# import cv2
#
# img = cv2.imread('Lenna.png')
# cv2.imshow('Original image', img)
# cv2.waitKey(0)
#
# grayimg = cv2.cvtColor(img[..., 0], cv2.COLOR_GRAY2RGB)
# cv2.imshow('Gray image', grayimg)
# cv2.waitKey(0)

# cv2.imwrite('gray.png', grayimg)

import random
from PIL import Image, ImageDraw

# mode = 0
# image = Image.open('Lenna.png')
# draw = ImageDraw.Draw(image)
# width = image.size[0]
# height = image.size[1]
# pix = image.load()
#
# if (mode == 0):
#     for i in range(width):
#         for j in range(height):
#             a = pix[i, j][0]
#             b = pix[i, j][1]
#             c = pix[i, j][2]
#             s = (a + b + c) // 3
#             draw.point((i, j), (s, s, s))




