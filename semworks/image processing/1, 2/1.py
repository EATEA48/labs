from PIL import Image, ImageDraw

img = Image.open("Lenna.png")

draw = ImageDraw.Draw(img)

w = img.size[0]
h = img.size[1]

pix = img.load()

for i in range(w):
    for j in range(h):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        s = (a + b + c) // 3
        draw.point((i, j), (s, s, s))
img.show()
img = img.save("gray.png")
img.close()
