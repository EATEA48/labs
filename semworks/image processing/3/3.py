from PIL import Image, ImageDraw, ImageFilter
import math
# image = Image.open('Lenna.png')
# draw = ImageDraw.Draw(image)
# w = image.size[0]
# h = image.size[1]
# pix = image.load()
#
#
# sigma = 1
# k = 0
#
# r = 10

img = Image.open('Lenna.png').convert('L')
r = 3

draw = ImageDraw.Draw(img)

def gauss_blur(img, r):
    imgData = list(img.getdata())

    bluredImg = Image.new(img.mode, img.size)
    bluredImgData = list(bluredImg.getdata())

    rs = int(math.ceil(r * 2.57))

    for i in range(0, img.height):
        for j in range(0, img.width):
            val = 0
            wsum = 0
            for iy in range(i - rs, i + rs + 1):
                for ix in range(j - rs, j + rs + 1):
                    x = min(img.width - 1, max(0, ix))
                    y = min(img.height - 1, max(0, iy))
                    dsq = (ix - j) * (ix - j) + (iy - i) * (iy - i)
                    weight = math.exp(-dsq / (2 * r * r)) / (math.pi * 2 * r * r)
                    val += imgData[y * img.width + x] * weight
                    wsum += weight
            bluredImgData[i * img.width + j] = round(val / wsum)

    # bluredImg.putdata(bluredImgData)
    # return bluredImg
    draw.point(bluredImgData)
    img.show()
img.close()


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