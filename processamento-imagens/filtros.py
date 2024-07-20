from PIL import Image, ImageFilter
import numpy as np


def show_vertical(im1, im2):
    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()

img = Image.open('input/miniatura.jpg')
filtered = img.filter(ImageFilter.BLUR)

# Mais Filtros: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# img.show()
# filtered.show()

show_vertical(img, filtered)

