from PIL import Image, ImageDraw

img = Image.open("Lenna.png")

draw = ImageDraw.Draw(img)

w = img.size[0]
h = img.size[1]

matrix = [[0.5, 0.75, 0.5],
          [0.75, 1, 0.75],
          [0.5, 0.75, 0.5]
          ]

div = 1 / 6

pix = img.load()
for z in range(len(matrix)):
    m = matrix[z]
    for i in range(w):
        for j in range(h):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = pix[i, j] * matrix[z, i]
            draw.point((i, j), (int(a), int(b), int(c)))
img.show()
img.close()
