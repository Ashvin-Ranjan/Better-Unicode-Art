from PIL import Image
import numpy as np

WIDTH = 70

chars = ""

with open("256_characters.txt", "r", encoding="utf-8") as f:
    chars = f.read()

img = Image.open('image.png').convert('L')
img = img.resize((WIDTH, round(WIDTH*img.height/img.width)))

data = np.array(img)


for row in data:
    for pixel in row:
        print(chars[pixel], end="")
    print()