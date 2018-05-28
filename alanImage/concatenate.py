from PIL import Image


img = Image.open("./data/cat_256.png")
(w, h) = img.size

imgConcatenate = Image.new('RGB', (w * 3, h))
imgConcatenate.paste(img, (0, 0))
imgConcatenate.paste(img, (w, 0))
imgConcatenate.paste(img, (w * 2, 0))

imgConcatenate.save("./data/cat_concatenate.png")