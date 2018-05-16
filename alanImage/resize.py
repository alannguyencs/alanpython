from PIL import Image


img = Image.open("./data/cat.jpg")

(newWidth, newHeight) = (256, 256)
img = img.resize((newWidth,newHeight), Image.ANTIALIAS)

img.save("./data/cat_256.png")
