from PIL import Image, ImageDraw, ImageFilter
import math
image = Image.open('Lenna.png')
draw = ImageDraw.Draw(image)
w = image.size[0]
h = image.size[1]
pix = image.load()

k = 0

r = 10

matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i-1])):
            if (matrix[i + 1] or matrix[i - 1]) and (matrix[j + 1] or matrix[j - 1]) and (j != 2) and (i != 2):
                print(matrix[i][j])
            else:
                i += 1



# for i in range(w):
#     for j in range(h):
#         if (w + 1 or w - 1) and (h + 1 or h - 1):
#             r = pix[i, j][0]
#             g = pix[i, j][1]
#             b = pix[i, j][2]
#             rgb = (r + g + b)
#
#             a = 0.1 * rgb
#
#         draw.point((i, j), (round(a), round(a), round(a)))
#
#
# image.show()
# image.close()