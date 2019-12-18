from PIL import Image, ImageDraw
image = Image.open('Lenna.png')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        s = (a + b + c) // 3
        draw.point((i, j), (s, s, s))
image.show()
image.close()

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
