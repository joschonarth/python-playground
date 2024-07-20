from PIL import Image, ImageFilter
import os
from show_image import show_vertical, show_horizontal
from utils import in_file, out_file
from math import sqrt


def show_vertical_edges(filename, offset=0):
    original = Image.open(in_file(filename)).convert('L')
    filtered = original.filter(ImageFilter.Kernel(
        (3, 3),
        [-1, 0, 1,
         -2, 0, 2,
         -1, 0, 1],
         1,
         offset)
         )
    
    show_horizontal(original, filtered)
    filtered.save(
        out_file('{}_vsobel_{}.jpg'.format(filename[:filename.index('.')], offset)
        )
    )


def show_edges(filename, direction='x', offset=0):
    original = Image.open(in_file(filename)).convert('L')
    XSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, 0, 1,
                                -2, 0, 2,
                                -1, 0, 1],
                                1,
                                offset)
    YSOBEL = ImageFilter.Kernel((3,3),
                                [-1, -2, -1,
                                 0, 0, 0,
                                 1, 2, 1],
                                 1,
                                 offset)
    
    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        w, h = original.size
        filtered = Image.new('L', (w, h))

        for i in range(w):
            for j in range(h):
                value = sqrt(
                    vsobel.getpixel((i, j))**2 + hsobel.getpixel((i, j))**2
                )
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)


    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_{}sobel_{}.jpg'.format(
                filename[:filename.index('.')],
                 direction,
                 offset)
        )
    )

if __name__ == "__main__":
    show_edges('death_stranding.jpg', 'a', 0)