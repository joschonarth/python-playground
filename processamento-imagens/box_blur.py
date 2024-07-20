from PIL import Image, ImageFilter
import os
from show_image import show_vertical, show_horizontal
from utils import in_file, out_file


def show_box_blur(filename, r=1):
    original = Image.open(in_file(filename))
    filtered = original.filter(ImageFilter.BoxBlur(r))
    
    show_horizontal(original, filtered)
    filtered.save(
        os.path.join(out_file('{}_boxblur_{}.jpg'.format(filename[:filename.index('.')], r)))
    )


if __name__ == "__main__":
    show_box_blur('ellie.jpg', 8)