from PIL import Image


img = Image.open("./data/cat_concatenate.png")
(w, h) = img.size

#the parameters include coordinates of top-left and bottom-right corner
imgCrop = img.crop((w/4, h/4, w/2, h))

imgCrop.save("./data/cat_crop.png")