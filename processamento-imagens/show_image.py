from PIL import Image, ImageFilter
import numpy as np

def show_vertical(im1, im2):
    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()
    return im

def show_horizontal(im1, im2):
    im = Image.fromarray(np.hstack((np.array(im1), np.array(im2))))
    im.show()
    return im