from PIL import Image

path = str(input())
img = Image.open(path)
pix = img.load()
sr = 0
sg = 0
sb = 0

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pix[i, j]
        sr += r
        sg += g
        sb += b

s = (sr + sg + sb) // (img.width * img.height)
for i in range(img.width):
    for j in range(img.height):
        pix[i, j] = (s, s, s)


img.show()